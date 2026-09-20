---
game_id: GAME-0328
slug: warcraft-iii-reign-of-chaos
game_title: "Warcraft III: Reign of Chaos"
analysis_status: reviewed
reviewed: 2026-09-20
combination_ids: []
gene_ids:
  action:
    - ACT-189
    - ACT-190
    - ACT-191
  system:
    - SYS-215
    - SYS-297
    - SYS-298
    - SYS-299
    - SYS-305
    - SYS-380
    - SYS-821
  constraint:
    - CON-269
    - CON-270
    - CON-273
    - CON-330
  information:
    - INF-119
    - INF-125
    - INF-224
    - INF-225
    - INF-268
  objective:
    - OBJ-155
  time:
    - TIM-003
---

# Game: Warcraft III: Reign of Chaos

Use the canonical [vocabulary, genome signature and comparison
rules](../../../docs/ARCHITECTURE.md#canonical-vocabulary). Thrall, Grunts,
Gnolls, Murlocs, Chain Lightning, the Prophet and named mission locations are
carrier parameters, not gene names.

## Analysis scope

- Version / ruleset: original English North American Windows retail
  *Warcraft III: Reign of Chaos* base game from 2002, Prologue campaign
  `Exodus of the Horde`, Chapter One `Chasing Visions`. The exact disc pressing,
  executable patch and installed binary were not observed. This is not *The
  Frozen Throne*, *Reforged*, multiplayer, the World Editor or a later balance
  ruleset.
- Structured analysis target: licensed original Windows base-game package; see
  `GAME-0328` in
  [`knowledge/platforms/games.json`](../../platforms/games.json).
- Primary decision loop: read the current narrated instruction and visible
  route state; select Thrall or the controllable group; commit a move, attack or
  attack-move order; let pathing and live combat resolve under current sight;
  after the authored hero-level gate, spend the available ability point and
  cast Chain Lightning; advance to the next beacon only after the current
  teaching predicate has settled.
- Entry: first ordinary control of Thrall beside his camp after the opening
  dream sequence and the narrator's first movement instruction.
- Positive terminal: Thrall and the supplied Grunts have followed the mandatory
  tutorial route, Thrall reaches the final beacon beside the Prophet, the
  chapter's closing sequence settles and `Departures` becomes the authored
  successor. The next chapter is not played.
- Negative state: Thrall's defeat prevents the mission from continuing; an
  unfinished narrated predicate leaves the current instruction active. Restart,
  save/load and post-failure persistence were not observed and are excluded.
- Included: contextual unit orders; selection and group control; authored
  delivery of three Grunts; controlled pathing and attack acquisition; the
  mandatory Gnoll and Murloc encounters on the documented route; nearby combat
  experience, one level threshold, one ability point, learned Chain Lightning,
  its target/mana legality and typed damage; health, mana, level, experience,
  selection, command card, objective, minimap, explored terrain, current fog,
  narrated teaching steps, beacons, Thrall survival and the final rendezvous.
- Excluded: optional Ogre, Golem and Forest Troll detours; optional treasure,
  consumables and item handling; exhaustive hostile clearance; speed or score;
  economy, Peon orders, gold, lumber, food, base construction, upgrades,
  production and upkeep introduced in `Departures`; every later prologue or
  campaign chapter; Battle.net, LAN and custom games; the World Editor;
  *The Frozen Throne*; *Reforged*; current balance data; save/load behaviour;
  achievements; cheats, glitches, speedrun routes and modifications.
- Reproducible parameterisation: start a fresh original base-game prologue and
  accept the default authored `Chasing Visions` route. Follow each narrator
  instruction, meet the three Grunts, clear only the mandatory blocking
  encounters, spend the first available hero point on Chain Lightning, use it
  when instructed and move Thrall onto the final beacon. Unit formation,
  incidental basic-attack targets and exact order timing are parameters.
- Potential scoped modules: optional creep camps and items, `Departures` with
  economy and production, later campaign missions, multiplayer factions,
  expansion rules and remade presentation require separate terminals and
  evidence.
- Direct-play status: not conducted. No original disc, installed executable,
  input trace, save, screenshot, video or audio was used. Blizzard's original
  manual and classic command documentation establish product, command, hero,
  ability and fog rules; three written routes establish the bounded tutorial
  sequence. This is a source-bounded reconstruction, not a claimed playthrough
  or reload test.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `W3R-001` | The packet is the original 2002 English Windows base game and excludes the expansion and remake | Confirmed | Direct | High | P1 |
| `W3R-002` | `Chasing Visions` is the first prologue chapter and teaches commands through a staged narrated route | Observation | Corroborated | High | S1, S2, S3 |
| `W3R-003` | Three Grunts join Thrall at an authored point without cost or production | Observation | Corroborated | High | S2, S3 |
| `W3R-004` | The bounded main route requires group movement and live combat against blocking Gnolls and Murlocs, while several camps and items remain optional | Observation | Corroborated | High | S1, S2, S3 |
| `W3R-005` | Nearby combat experience raises Thrall's hero level and exposes one ability point that the tutorial directs into Chain Lightning | Observation | Corroborated | High | P1, S1, S2 |
| `W3R-006` | Legal Chain Lightning use consumes current mana/readiness and resolves typed damage through eligible targets | Confirmed | Corroborated | High | P1, S2, S3 |
| `W3R-007` | Selection, health, mana, experience, commands, current objective, minimap, explored terrain and fog expose the next actionable state | Confirmed | Direct | High | P1, P2, P3 |
| `W3R-008` | Thrall is mission-critical and the ordinary success terminal is reaching the final beacon beside the Prophet | Observation | Corroborated | High | S1, S2, S3 |
| `W3R-009` | Base construction and unit production begin in the successor `Departures`, not in this packet | Observation | Corroborated | High | S1 |

## Basic data

- Release / origin: Blizzard Entertainment, Windows, North American retail
  release 2002-07-03.
- Platform or physical form: licensed English Windows retail base game; exact
  disc pressing and executable patch not observed.
- Puzzle family: real-time agent routing and tactical counterplay inside an
  ordered authored command tutorial.
- Primary sources:
  - **[P1]** [Blizzard's original *Warcraft III* manual](https://ftp.blizzard.com/pub/misc/Warcraft%20III%20Manual.pdf),
    original product identity, heroes, experience, abilities, mana, fog and
    interface framing.
  - **[P2]** [Blizzard classic unit-command documentation](https://classic.battle.net/war3/basics/specialcommands.shtml),
    group orders, selection, formations, control groups and queued commands.
  - **[P3]** [Blizzard classic hero-control documentation](https://classic.battle.net/war3/basics/herocontrol.shtml),
    hero selection, experience, abilities and survival framing; the classic
    site explicitly warns that later data can differ from the base game, so it
    is used only where the original-manual boundary agrees.
- Secondary sources:
  - **[S1]** [GameSpot *Reign of Chaos* walkthrough](https://www.gamespot.com/articles/warcraft-iii-reign-of-chaos-walkthrough/1100-2875830/),
    contemporary written `Chasing Visions` and `Departures` separation.
  - **[S2]** [StrategyWiki `Chasing Visions` route](https://strategywiki.org/wiki/Warcraft_III%3A_Reign_of_Chaos/Chasing_Visions),
    Grunt join, blocking encounters, Chain Lightning lesson, optional detours
    and final beacon.
  - **[S3]** [Gamer Walkthroughs `Chasing Visions` route](https://gamerwalkthroughs.com/warcraft-3-reign-of-chaos/prologue-exodus-of-the-horde/chasing-visions/),
    independent route corroboration and Prophet terminal.
- Claim IDs: `W3R-001`–`W3R-009`.

## Mechanical decomposition

### Action Genes

- Existing `ACT-189`: select Thrall, one Grunt or the group and commit a move,
  attack, attack-move, stop or hold order to a point or eligible target.
- Existing `ACT-190`: commit learned Chain Lightning against a legal hostile
  target while its mana and readiness gates are satisfied.
- Existing `ACT-191`: spend the newly awarded hero-development point on the
  currently taught Chain Lightning rank.
- Control-group key, formation, queued waypoint and exact target are parameters.
  Claims: `W3R-002`–`W3R-006`.

### System Behaviour Genes

- Existing `SYS-215`: continuously resolve ordered combatants' range, cadence,
  damage, defence, health and defeat.
- Existing `SYS-297`: execute committed navigation, acquire the ordered target
  and repeat legal basic attacks.
- Existing `SYS-298`: award nearby eligible creep defeats as scoped hero
  experience; no gold or economy is imported into this packet.
- Existing `SYS-299`: convert the first documented experience threshold into a
  hero level and one spendable ability point.
- Existing `SYS-305`: propagate controlled-unit sight through current terrain
  and fog while live hostile state outside sight remains hidden.
- Existing `SYS-380`: resolve Chain Lightning into its authored primary and
  linked damage effects against eligible live targets.
- Existing `SYS-821`: place the three scripted Grunts under player control at
  the declared camp event without cost, request or production.
- Resolution order: narrated gate exposes the present task; the player commits
  an order; pathing, sight and combat update; eligible defeat awards experience;
  a crossed threshold exposes the point; spending and a legal cast satisfy the
  ability lesson; later orders reach the final beacon. Claims: `W3R-002`–`W3R-007`.

### Constraint Genes

- Existing `CON-269`: Chain Lightning requires a learned rank, eligible target,
  legal reach, sufficient mana and current readiness.
- Existing `CON-270`: the hero point can enter only an ability rank admitted by
  the current level and authored tutorial state.
- Existing `CON-273`: ordinary direct targeting of hostile units requires
  current allied sight through fog.
- Existing `CON-330`: the authored mission continues only while the
  mission-critical Thrall remains viable.
- Exact unit radii, damage values, experience threshold and mana cost are
  parameters. Claims: `W3R-005`–`W3R-008`.

### Information Genes

- Existing `INF-119`: Thrall's health, mana, experience, level, learned ability
  and ability readiness are visible before the next commitment.
- Existing `INF-125`: current objective text, route beacons and minimap expose
  the present authored destination, not the full future chain.
- Existing `INF-224`: the command view exposes selected-unit identity, health
  and available orders even though this scoped chapter has no player economy or
  production.
- Existing `INF-225`: explored terrain persists on the world view and minimap
  while live hostile occupancy outside current sight returns to fog.
- Existing `INF-268`: the narrator explains the current command or risk,
  acknowledges completion and only then advances to the next tutorial step.
- Claims: `W3R-002`, `W3R-005`–`W3R-008`.

### Objective Genes

- Existing `OBJ-155`: satisfy the ordered mandatory interactions of one bounded
  authored action chapter, preserve the critical actor, accept explicit chapter
  completion and expose the immediate successor chapter.
- The Prophet beacon and settled `Chasing Visions` boundary, not optional camp
  clearance or entry into `Departures`, is the terminal. Claims: `W3R-008`,
  `W3R-009`.

### Time Genes

- Existing `TIM-003`: movement, pathing, sight, attacks, mana and encounter
  state advance continuously while commands remain available; pauses and
  authored sequences interrupt that live cadence.

## Reproducible transitions

| Before | Action | Deterministic or bounded resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| Thrall is beside his tent and the movement lesson is current | Select Thrall and right-click the declared destination | pathing carries the selected hero toward the beacon while fog and minimap state update | an abstract destination order drives autonomous movement | `W3R-002`, `W3R-007` |
| Thrall reaches the authored Orc camp | approach the waiting group as instructed | exactly three Grunts join the controllable force without spending or production | scripted arrival changes the available friendly roster | `W3R-003` |
| A blocking hostile group is visible | select the group and issue attack or attack-move orders | units path, acquire legal targets and exchange attacks until one side is defeated | group command and live combat are distinct from direct avatar locomotion | `W3R-004` |
| Eligible hostile defeats occur near Thrall | keep Thrall inside the admitted experience relation | experience increases; crossing the documented threshold raises hero level and grants a point | live events feed hero progression | `W3R-005` |
| One hero point is available and the taught rank is eligible | spend the point on Chain Lightning | the rank becomes learned and its cast control becomes actionable | level gate and point commitment are separate transitions | `W3R-005` |
| Murlocs are visible and Chain Lightning is learned and ready | cast Chain Lightning on a legal target | mana/readiness is consumed and authored linked damage resolves through eligible targets | an active ability has target, resource and typed-effect rules | `W3R-006` |
| Mandatory tutorial encounters and instructions are settled | order Thrall onto the final beacon beside the Prophet | the closing sequence accepts the rendezvous and exposes `Departures` | the packet ends at an authored successor boundary | `W3R-008`, `W3R-009` |

## Edge-case audit

- Three Grunts are authored reinforcements, not trained units: no production,
  resource, supply or build prerequisite enters the signature.
- Creep experience is included only as the source of the documented first hero
  threshold. Optional camp farming, gold and item rewards are excluded.
- Chain Lightning's name, number of jumps, exact damage and mana cost are
  parameters; the reusable boundary is a legal selected ability producing a
  typed live effect.
- The optional Ogre, Golems, Trolls, treasure and consumables are deliberately
  absent from the reproducible route and cannot justify pickup, inventory or
  optional-clearance genes.
- `Departures` introduces economy, buildings and production after this terminal;
  importing them would collapse two mechanically different tutorial packets.
- The route sources establish ordinary progression but not save/reload or
  failure persistence. Those behaviours remain unclaimed.

## Strategic and experiential structure

- Local decision: select the relevant force, choose a destination or hostile
  target, preserve Thrall, and use Chain Lightning only when the visible
  target and mana state make it legal.
- Medium-term planning: keep the supplied group together through authored
  encounters, obtain the first hero threshold and satisfy each teaching gate
  without detouring into optional camps.
- Long-term structure: convert a lone hero into a commanded squad with one
  learned active ability, then bring that retained force to the Prophet so the
  prologue can advance into its economy lesson.
- Common heuristics: attack through the group rather than exposing Thrall;
  inspect current fog before focus fire; spend the first point promptly; use
  Chain Lightning where its linked targets produce immediate value.
- Failure attribution: an unreachable order, hidden target, dead Grunt,
  defeated Thrall, unspent point, illegal cast or unreached beacon remains
  distinguishable through selection, HUD, objective and tutorial feedback.
- Player trust: equivalent commands at equivalent tutorial state must resolve
  through the same pathing, sight, experience, ability and mission gates;
  optional detours must not silently become terminal requirements.

## Replay and variation

- Route geometry, Grunt arrival, teaching order, mandatory encounters and the
  Prophet terminal are authored; no procedural map generation is claimed.
- Formation, order timing, target priority and optional detours can vary, but
  the reproducible trace fixes the shortest documented mandatory route.
- Replay within this packet compares unit preservation and command efficiency,
  not economy, faction build orders or random map play.
- Claims: `W3R-002`–`W3R-009`.

## Adjacent systems and history

- Direct predecessor: *Warcraft II* supplies series context but is not evidence
  for this packet.
- Variants: *The Frozen Throne* extends the original product and *Reforged*
  changes presentation and later rule data. Neither is merged here.
- Similar games: *StarCraft II* `Liberation Day` and *Command & Conquer
  Remastered Collection* also route supplied real-time forces under fog through
  authored mission gates.
- Important differences: this packet makes hero experience, one build-point
  commitment and one active spell part of the mandatory tutorial, while its
  positive terminal is a rendezvous rather than destruction of a designated
  structure or complete hostile set.
- Claim IDs: `W3R-001`–`W3R-009`.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-189`, `ACT-190`, `ACT-191` | group order, target, Chain Lightning and first point |
| System Behaviour | `SYS-215`, `SYS-297`, `SYS-298`, `SYS-299`, `SYS-305`, `SYS-380`, `SYS-821` | combat, pathing, experience, level, sight, spell effect and three Grunts |
| Constraint | `CON-269`, `CON-270`, `CON-273`, `CON-330` | mana/readiness, level gate, current sight and Thrall survival |
| Information | `INF-119`, `INF-125`, `INF-224`, `INF-225`, `INF-268` | hero HUD, beacons, selection, remembered terrain and narrator |
| Objective | `OBJ-155` | settle `Chasing Visions` at the Prophet beacon |
| Time | `TIM-003` | live orders, pathing, combat, sight and mana |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `327` (`GAME-0001`–`GAME-0327`).
- Exact genome matches: none.
- Tied near matches: `GAME-0317` — StarCraft II (`11 / 22 = 0.500000`).
- Supported combination subsets: none.
- Scan date: 2026-09-20.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0317` — StarCraft II | `ACT-189`, `SYS-215`, `SYS-297`, `SYS-305`, `SYS-821`, `CON-273`, `CON-330`, `INF-125`, `INF-224`, `INF-225`, `TIM-003` | Both route supplied real-time groups through command execution, live combat, sight, fog and authored mission gates while preserving one critical hero. *StarCraft II* destroys a designated structure without hero build allocation. *Warcraft III* instead crosses a hero-experience threshold, spends one ability point, casts one typed spell and ends at a rendezvous. | Near, `0.500000` |

### Preserved research notes

- New genes: none.
- Classification result: `New composition`.
- Evidence and reasoning: every observed boundary is already established by
  command-scale RTS, hero-progression, active-ability and authored-chapter
  records. The informative result is their mandatory tutorial composition, not
  a new vocabulary label.

## Taxonomy impact

- Registry changes: extend supporting evidence for the reused command, combat,
  progression, ability, fog, reinforcement, mission and information genes.
- Taxonomy-change record: none.
- Candidate terms affected: Thrall, Grunt, Gnoll, Murloc, Chain Lightning,
  Prophet, `Chasing Visions`, `Departures` and prologue beacons remain carrier
  parameters or labels rather than new genes.

## Negative results

- No separate negative-result record. Economy, production, inventory, pickup,
  exhaustive-clearance and procedural-map genes were tested and rejected
  because their establishing observations are optional or begin only after the
  scoped chapter.

## Delta summary

## New facts

- [Confirmed | Direct | High] Blizzard's original manual and classic command
  documentation establish a hero-led real-time command layer with group orders,
  experience, abilities, mana, sight and fog (`W3R-001`, `W3R-005`–`W3R-007`).
- [Observation | Corroborated | High] The first prologue chapter supplies three
  Grunts, teaches mandatory group combat and Chain Lightning, then settles when
  Thrall reaches the Prophet beacon (`W3R-002`–`W3R-009`).

## New genes

- [Observation | Corroborated | High] No new gene. Twenty-one established
  boundaries cover the complete packet.

## New combinations

- [Observation | Corroborated | High] No new verified combination.

## Taxonomy changes

- [Observation | Direct | High] No taxonomy change.

## New questions

- Which economy and production genes first become necessary when `Departures`
  adds Peons, resources, supply, buildings and a trained force?
- Does the original retail executable preserve optional item and explored-map
  state identically after a clean save/reload?

## Next recommended game

- [Hypothesis | Limited | Medium] `GAME-0329` Donkey Kong Country, original
  SNES first-level packet.
- Optimisation criterion: move from mouse-directed group command to direct
  side-scrolling movement, partner state, rolling attacks and authored exits.
- Expected information gain: test whether character-pair retention and animal
  interaction reuse existing platform-action boundaries without importing the
  full game's collectible and save structure.
- Backlog impact: `GAME-0329` remains next; no later unit starts in this commit.

## Why this game

- [Hypothesis | Limited | High] *Warcraft III* is a recognisable RTS anchor
  whose first chapter isolates hero-led orders, squad delivery, fog,
  progression and one active spell before the economy usually associated with
  the genre appears.
