---
game_id: GAME-0391
slug: uncharted-2-among-thieves
game_title: "Uncharted 2: Among Thieves"
analysis_status: reviewed
reviewed: 2026-09-24
combination_ids: []
gene_ids:
  action:
    - ACT-008
  system:
    - SYS-036
    - SYS-1049
  constraint: []
  information: []
  objective:
    - OBJ-231
  time:
    - TIM-003
---

# Game: Uncharted 2: Among Thieves

Use the canonical [vocabulary, genome signature and comparison
rules](../../../docs/ARCHITECTURE.md#canonical-vocabulary). The handhold
positions, train angle, event timings and named character are parameters, not
separate genes.

## Analysis scope

- Version / ruleset: the original 2009 English PlayStation 3 single-player
  campaign, Chapter 1 *A Rock and a Hard Place*, on its opening suspended-train
  escape. The exact disc revision and selected difficulty were not inspected;
  no remaster-specific assistance is inferred.
- Structured analysis target: `GAME-0391` in
  [`knowledge/platforms/games.json`](../../platforms/games.json).
- Entry: the first controllable moment when wounded Nathan Drake hangs from
  the passenger car suspended over a snowy chasm.
- Primary decision loop: inspect the next visible rail, pipe, seat, ledge or
  carriage opening; move along reachable handholds, jump across a gap or pull
  up, then respond to an authored shift or break in the support by taking the
  next reachable route before the falling car removes it.
- Positive terminal: jump from the final falling carriage and pull up onto the
  stable cliff ledge. The ensuing flashback and the later walk, gun pickup,
  shooting and remainder of Chapter 1 are outside this packet. This is a
  bounded escape checkpoint, not a claim of chapter or campaign completion.
- Negative terminal: missing a required hold or remaining on a support as
  the final car falls can send Drake into the chasm and end that attempt. The
  exact restart checkpoint or number of permitted retries was not verified
  and is not encoded.
- Included: direct body movement, handhold-to-handhold climbing, swing-jumps,
  ledge pull-ups, continuous falling and collision, authored support breaks,
  the final timed exit from the dropping car, and local visible route geometry.
- Excluded: later Chapter 1 train-wreck traversal and enemies, firearm or
  melee combat, health regeneration, collectibles, the Istanbul flashback,
  later train chapters, multiplayer, remastered editions, trophies and exact
  frame counts. Scripted falling rocks are not asserted to be damage sources.
- Reproducible parameterisation: start Chapter 1 on the original PS3 rules,
  record successive yellow rails, exposed pipes, seat holds and roof route;
  log each required jump or pull-up and each authored support break; finish
  when the player reaches the cliff ledge. The route, not a score or treasure
  count, defines success. The source packet establishes qualitative sequence
  but not exact timing or checkpoint coordinates.
- Potential scoped modules: the rest of Chapter 1 with a firearm and enemy;
  Chapter 13 moving-train combat; later climbing and puzzle chapters; PS4
  remaster-specific rules.
- Direct-play status: none. The 2009 official BradyGames guide sample documents
  the controls and opening sequence; two independent original-PS3 written
  routes corroborate the escape. No disc, executable, save, controller trace,
  screenshot, video or audio was inspected.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `UC2-001` | The original PS3 opening starts with Drake hanging from a passenger car over a snowy chasm. | Confirmed | Direct | High | P1 |
| `UC2-002` | Nearby holds allow left-stick climbing, while wider gaps require a jump; ledges permit pull-ups. | Confirmed | Direct | High | P1 |
| `UC2-003` | The pipe and seats move or fail in scripted sequence, redirecting the climb rather than making every break an immediate death. | Observation | Corroborated | High | P1, S1, S2 |
| `UC2-004` | Waiting too long on the failing pipe or final falling carriage can end the attempt; crossing to the cliff edge completes this bounded escape. | Observation | Corroborated | Medium | P1, S1 |
| `UC2-005` | Later in Chapter 1 Drake finds a firearm and fights, but that is after this selected cliff-escape boundary. | Observation | Corroborated | High | S1, S2 |
| `UC2-006` | Exact disc revision, difficulty, input windows and failure-restart coordinates were not verified by direct play. | Observation | Direct | High | R1 |

## Basic data

- Release / origin: Naughty Dog and Sony Computer Entertainment's 2009
  *Uncharted 2: Among Thieves* on PlayStation 3; the official PlayStation
  overview distinguishes it from the later Nathan Drake Collection.
- Platform or physical form: original PS3 single-player third-person action
  adventure. The structured target is `PLAT-PLAYSTATION-3`.
- Puzzle family: `FAM-010` real-time system pressure, because the authored
  support failure advances while the player is still choosing grips and jumps.
- Primary sources, checked 2026-09-24:
  - **[P1]** [BradyGames' 2009 official strategy-guide sample](https://ptgmedia.pearsoncmg.com/images/9780744011166/samplepages/1116-6_uncharted2.pdf),
    published with Naughty Dog and Sony credits, pp. 24–27 for the opening
    climb, support breaks, swing-jump, falling carriage and cliff exit.
  - **[P2]** [PlayStation's official Uncharted overview](https://www.playstation.com/en-us/uncharted/),
    for original title and the later collection distinction, not for exact
    climbing timing.
- Corroborating original-PS3 routes:
  - **[S1]** [2009 GameFAQs guide by thecrobar](https://gamefaqs.gamespot.com/ps3/955125-uncharted-2-among-thieves/faqs/58006),
    Chapter 1 opening and later firearm boundary.
  - **[S2]** [Gamepressure Chapter 1 route](https://www.gamepressure.com/uncharted-2-among-thieves/a-rock-and-a-hard-place/zccea3),
    yellow railing, damaged pipe and route into the carriage; this is a
    corroborating route, not a copied image or prose source.
  - **[R1]** bounded source and no-direct-play audit in this record.
- Claim IDs: `UC2-001`–`UC2-006`.

## Mechanical decomposition

### Action Genes

- `ACT-008`: directly steer and jump Drake between reachable railings, pipes,
  seats and the final ledge. The PS3 guide treats climbing, swing-jumps and
  pull-ups as contextual local movement, not separately equipped abilities.
- Candidate genes: none. Actor identity and particular grip geometry remain
  parameters. Claim IDs: `UC2-001`, `UC2-002`.

### System Behaviour Genes

- `SYS-036`: gravity, jumps and collision determine whether a transfer lands
  on a supported hold or sends the body into the chasm.
- `SYS-1049`: at authored points, a pipe or seat gives way and changes the
  immediately usable route; the final car falls when Drake must cross to the
  cliff. A preliminary break can redirect rather than kill.
- Resolution order: movement and jump → contact with reachable support →
  gravity and collision → any authored support shift or break → new reachable
  support or failed fall. Claim IDs: `UC2-002`–`UC2-004`.

### Constraint Genes

- No additional constraint ID: reachable handholds and finite jump distance
  are local geometry and collision parameters of `ACT-008` and `SYS-036`;
  no stamina, equipment, key or ammo gate is documented for this packet.
  Claim IDs: `UC2-002`, `UC2-006`.

### Information Genes

- No separate information gene: the local carriage, yellow rails and next
  visible holds are ordinary rendered world geometry, not a HUD forecast or
  concealed-clue system. The unobserved exact future break timing is not
  promoted to an information rule. Claim IDs: `UC2-002`, `UC2-006`.

### Objective Genes

- `OBJ-231`: leave the collapsing train and reach the stable cliff ledge.
  Reaching a roof hold alone does not complete the selected escape.
- Claim IDs: `UC2-003`, `UC2-004`.

### Time Genes

- `TIM-003`: the final support continues to fail while movement and jumps are
  accepted. This is not a separate visible countdown or a full-stage time
  trial. Claim IDs: `UC2-004`.

## Reproducible transitions

| Before | Action | Resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| Drake hangs at the initial car | Move along the yellow rail and reachable pipes | The body stays attached to compatible local holds | local traversal, not remote route selection | `UC2-001`, `UC2-002` |
| A next hold is beyond simple lateral movement | Swing and jump toward it | A successful reach attaches to the next support; a missed route risks the chasm | gravity and geometry constrain transfer | `UC2-002` |
| Drake climbs a stressed pipe or seats | Continue after the authored break | The current support shifts or tears away, requiring another route; not every break kills immediately | authored support change is distinct from ordinary falling | `UC2-003` |
| The final carriage begins dropping | Run and jump to the cliff ledge | Pulling up to stable ground ends the selected escape; lingering can fail | bounded real-time terminal | `UC2-004` |

## Strategic and experiential structure

- Local decision: identify the next reachable support and choose when to
  traverse or leap as the suspended car moves.
- Medium-term planning: follow the authored loop through underside, carriage
  interior and roof toward the cliff rather than search for free-form routes.
- Long-term structure: the positive terminal is an escape checkpoint before
  the campaign continues; neither chapter completion nor combat is claimed.
- Failure attribution: missed contact or remaining on a falling support is
  relevant; exact input and reset behavior remain unverified. Claim IDs:
  `UC2-002`–`UC2-006`.

## Replay and variation

- The guide describes one authored geometry and event sequence. Different
  input timing may change success, but no procedural route generation or
  alternate reward is established for this opening packet.
- Repeated attempts or a changed difficulty are not asserted to alter the
  fixed support order. Claim IDs: `UC2-003`, `UC2-006`.

## Adjacent systems and history

- The rest of this chapter adds a firearm and hostile encounter, so expanding
  the scope to its named chapter end would change the signature. This unit
  deliberately stops at the first cliff exit.
- Later moving-train combat and the PS4 remaster remain separately bounded
  subjects. The official PlayStation overview establishes the collection's
  existence, not rule identity with this PS3 scene.

## Normalised genome

| Type | Active genes | Parameters outside signature |
|---|---|---|
| Action | `ACT-008` | route, jump and handhold locations |
| System | `SYS-036`, `SYS-1049` | support-break order and falling-car timing |
| Constraint | none | reachable contact geometry |
| Information | none | locally visible rails and holds |
| Objective | `OBJ-231` | cliff-ledge terminal |
| Time | `TIM-003` | qualitative urgency, not measured frames |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `390` (`GAME-0001`–`GAME-0390`).
- Exact genome matches: none.
- Tied near matches: `GAME-0112` — Human: Fall Flat (`3 / 10 = 0.300000`).
- Supported combination subsets: none.
- Scan date: 2026-09-24.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0112` Human: Fall Flat | `ACT-008`, `SYS-036` and `TIM-003` share direct movement, falling under geometry and a live simulation. | The Human: Fall Flat room relies on separately controlled hands and a movable crate to reach a static exit. Drake follows an authored sequence of supports that fail while he climbs, then escapes to the cliff before the car falls. The equal three-gene overlap does not equate the grip control or objective. | `3 / 10 = 0.300000`; tied near maximum, not an equivalent traversal loop |

### Preserved research notes

- New genes: `SYS-1049`, `OBJ-231`.
- Classification result: New gene.
- Evidence and reasoning: the official opening route distinguishes authored
  support failure from ordinary body gravity and makes stable-cliff escape a
  terminal separate from the later Chapter 1 combat.

## Taxonomy impact

- Registry changes: add `SYS-1049` and `OBJ-231` without changing an older
  signature or lifecycle.
- Taxonomy-change record: `TAXONOMY_CHANGE_129`.
- Candidate terms affected: support break and bounded train escape; train
  angle, rail colour and character name remain parameters.

## Negative results

- No separate negative-result record. Checkpoint mechanics, health and gunplay
  are excluded for lack of evidence inside the selected interval.

## Delta summary

## New facts

- [Observation | Corroborated | High] The original opening climb uses
  reachable handholds and an authored collapsing carriage before its cliff
  escape (`UC2-001`–`UC2-004`).

## New genes

- [Observation | Corroborated | Medium] `SYS-1049` changes authored supports
  during the traversal interval.
- [Observation | Corroborated | Medium] `OBJ-231` ends the bounded escape on
  the stable cliff ledge.

## New combinations

- [Observation | Direct | High] No new verified combination is proposed;
  existing subset support is determined by the deterministic scan.

## Taxonomy changes

- [Observation | Corroborated | Medium] `TAXONOMY_CHANGE_129` adds the two
  bounded distinctions without altering earlier signatures.

## New questions

- Does a directly inspected original PS3 build confirm the same restart
  coordinates and failure window on every difficulty?

## Next recommended game

- [Hypothesis | Limited | Medium] `GAME-0392` Mario Party 2.
- Optimisation criterion: alternate the scripted action-escape loop with
  turn-based party-board decisions and different visual geometry.
- Expected information gain: board turns, minigame transition and star/coin
  economy without transferring rules from later ports.
- Backlog impact: the next reserved subject in the 388–396 horizon.

## Why this game

- [Hypothesis | Limited | Medium] A recognisable cinematic action scene adds
  a focused timed traversal counterexample between city planning and a party
  board game, without mistaking the whole campaign for one comparable genome.
