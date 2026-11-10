---
game_id: GAME-0494
slug: dead-or-alive-2
game_title: Dead or Alive 2
analysis_status: reviewed
reviewed: 2026-10-04
combination_ids: []
gene_ids:
  action:
    - ACT-008
    - ACT-202
    - ACT-223
    - ACT-294
    - ACT-295
    - ACT-296
    - ACT-297
    - ACT-605
  system:
    - SYS-215
    - SYS-522
    - SYS-1328
    - SYS-1329
    - SYS-1330
    - SYS-1331
  constraint:
    - CON-442
    - CON-446
    - CON-763
  information:
    - INF-142
    - INF-209
    - INF-210
  objective:
    - OBJ-282
  time:
    - TIM-003
---

# Game: Dead or Alive 2

Use the canonical [vocabulary and signature](../../../docs/ARCHITECTURE.md#canonical-vocabulary).
Fighter names, move inputs, selected round settings and tier dimensions are
instance parameters, not independent genes.

## Analysis scope

- Version / ruleset: original North American English 2000 Tecmo Dreamcast
  Dead or Alive 2, ordinary local two-player Versus with Kasumi and Ein on
  The Great Opera. Explicitly choose COMMAND TYPE DREAMCAST for both,
  VS MATCH POINT 2, VS LIFE GAUGE NORMAL, ROUND TIME 60 and enable VS stage
  selection. The manual lists these available values, not their factory
  defaults. Retain ordinary default buttons F=A, P=X, K=Y and B=F+P.
  Exact regional disc serial, binary hash, numerical life and frames are
  uninspected; no Hardcore, Ultimate or Japanese Limited Edition parity.
- Structured analysis target: `PLAT-DREAMCAST` in the matching
  `analysisTarget`; this does not assert every release platform.
- Primary decision loop: read relative body position, incoming height, life,
  clock and round lights; step, free-step, crouch or jump; choose an eligible
  character attack/string, guard, throw/escape, timed hold or recovery;
  resolve contact, stagger, counters, wall response and eligible tier falls;
  repeat through awarded rounds and any required sudden-death adjudication.
- Entry and exit: confirm the named pair and Opera with the declared options
  before the first active round. Exit at the fixed-pair Versus result, after
  required round awards and any simultaneous-threshold tiebreak, or deliberate
  abandonment. Previous matches, costumes and persistent records do not enter
  this packet. The manual calls the fallback winner of a further unresolved
  sudden death the "champion" without defining which side owns that status;
  do not substitute P1, the previous winner or a guessed identity.
- Included: all available commands of the selected pair, not only listed
  example strings: steps, dash/run, jump/crouch, retained free-step motion,
  high/middle/low and special high strikes, directional strings, ordinary
  and character-specific throws, crouching-target throws and eligible throw
  escapes; standing/crouching guard, three-class Dreamcast holds including
  the stagger exception, launch/juggle and downed attacks, quick stand,
  ground rolls, rising kicks and eligible pre-landing recovery; wall-induced
  weakening, wall-compatible throws and pivot recovery; eligible forced
  falls, damaged defender and safe attacker following; KO/time comparison,
  drawn round awards, round reset and lower-life sudden death.
- Excluded: partner selection/tagging, off-stage partner regeneration and
  joint tag commands; Survival life carry, items and score; Story/Time Attack
  ladders, Team Battle, Sparring, costume unlocks, VMU persistence, online
  claims, later-edition mechanics and imported four-class Arcade holds.
  Hidden frame counts, internal damage arithmetic and an exhaustive exact
  input chart are not reconstructed. The manual's character examples are
  not claimed to exhaust either fighter's repertoire.
- Potential scoped modules: two-member tag combat; Survival with carried
  vitality, healing items and scoring; a Story tournament ladder.
- Direct-play status: not conducted. Original Tecmo USA booklet text and
  printed pp. 3–6, 11–18 and 29 were inspected as pixels. An independently
  authored first-hand North American review corroborates Dreamcast hold
  mapping, moving fighters and wall interaction. No game, disc, emulator,
  save, video or audio was executed. A pre-release Arcade guide's speculative
  Dreamcast instructions are not used to assert original-console parity.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| DOA-001 | Original USA booklet supports fixed local Versus, selected fighters and explicit available settings | Observation | Direct | High | P1 pp. 7, 11–14, 18, 29 |
| DOA-002 | Direct steps, crouch/jump, strings, guard, throws and state-compatible recovery organise live combat | Observation | Direct | High | P1 pp. 3–6, 15, 18, 29 |
| DOA-003 | DREAMCAST high/middle/low timed holds intercept strikes and counterattack, including while stagger blocks ordinary attack/guard | Observation | Corroborated | High | P1 p. 6; P2 control paragraphs |
| DOA-004 | Same-type counters increase damage; strike against throw and throw against hold receive stronger high-counter damage | Observation | Direct | High | P1 p. 15 |
| DOA-005 | Eligible edge falls damage the defender; the attacker follows without that fall damage; not every edge/move qualifies | Observation | Direct | High | P1 p. 16 |
| DOA-006 | Wall contact can weaken and permit pivot recovery; selected throws change near walls | Observation | Corroborated | High | P1 p. 16; P2 Ein wall-throw account |
| DOA-007 | KO or greater life at time expiry earns a set; a draw awards both; simultaneous threshold opens lower-life sudden death | Observation | Direct | High | P1 pp. 11–12 |
| DOA-008 | Further unresolved sudden death is assigned to the booklet's champion, whose side identity remains unverified | Observation | Limited | Medium | P1 p. 11; no executed result |
| DOA-009 | Paired bodies, animation and life/time/set indicators expose decision-relevant state, not numerical hidden frames | Observation | Corroborated | Medium | P1 pp. 3–6, 12, 15–16; P2 motion account |
| DOA-010 | No exact native execution, complete input chart, regional or later-edition parity was observed | Observation | Direct | High | inspection boundary; P2 incomplete manual warning |
| DOA-011 | Every prior signature and verified proper combination subset is scanned without modifying older genomes | Observation | Direct | High | canonical comparator |

## Basic data

- Release / origin: Team Ninja / Tecmo, original North American Dreamcast
  Dead or Alive 2, 2000; no later publisher build is substituted.
- Platform or physical form: authorised Dreamcast GD-ROM, two local controllers;
  structured authority is `PLAT-DREAMCAST`.
- Puzzle family: existing `FAM-009` tactical forecast and counterplay and
  `FAM-010` real-time system pressure. Height/hold/throw relations, tier
  positioning and continuing opponent motion change each decision.
- Primary sources, checked 2026-10-04: **P1**, [Tecmo's original USA Dreamcast booklet](https://www.digitpress.com/library/manuals/dreamcast/dead_or_alive_2.pdf),
  archival scan, printed controls/rules/HUD/options/wall and fighter panels
  inspected as text and pixels. USA warranty/copyright identifies its context;
  the archive PDF's creation date is not a release or executable version.
  **P2**, [Reno's first-hand North American Dreamcast review](https://www.the-nextlevel.com/reviews/dreamcast/doa2/),
  independently written play testimony with three-height Dreamcast controls,
  wall-throw and animation observations. Its numerical critical-hold damage
  is not accepted as a verified universal constant.
- Scope-warning source: **P3**, [Jimbo's Arcade Basics guide](https://www.gamesurge.com/strategies/Arcade/Walkthroughs-C/Dead%20Or%20Alive%202%20B.shtml),
  readable original author guide whose Dreamcast controller discussion is
  explicitly speculative. Its four-class Arcade directions are not transferred.
- Secondary sources: none used to override the original scoped booklet.
- Claim IDs: `DOA-001`–`DOA-010`.

## Mechanical decomposition

### Action Genes

- Existing gene IDs: `ACT-008`, `ACT-202`, `ACT-223`, `ACT-294`, `ACT-295`,
  `ACT-296`, `ACT-297`, `ACT-605`.
- Direct movement includes one-step/dash/run and retained lateral free steps;
  entering up+F or down-down+F opens free-step motion, holding F+direction
  continues it and release returns normal movement. Crouch changes high-strike
  exposure; jump can avoid a low strike but is not universally invulnerable.
- `ACT-295` covers the pair's entire eligible strike/string vocabulary,
  special command-grab attacks as roster parameters, down attacks and rising
  kicks. Kasumi's listed PPKKK and Ein's PPP are examples, not the whole list.
  `ACT-297` is ordinary close F+P seizure/escape; down/diagonal-forward+F+P
  requests a compatible crouching-target throw. Do not promise every special
  throw is escapable with the ordinary input.
- Guard is back or F while standing, and down or down+F while crouching.
  Timed holds are separately requested: for right-facing DREAMCAST controls,
  up-back+F high, back+F middle, down-back+F low. Middle punch versus kick
  splitting belongs to the excluded Arcade mapping.
- Downed direction/repeated P, direction+repeated F rolls and eligible
  pre-landing P/K/F request recovery. Rising K/down+K is a separate attack,
  not automatic healing. Selected wall pivot is a state-compatible recovery.
- New action genes: none. Controls, fighters and frames remain parameters.
- Claim IDs: `DOA-001`–`DOA-003`, `DOA-006`.

### System Behaviour Genes

- Existing gene IDs: `SYS-215`, `SYS-522` for ordinary live strike/guard,
  whiff, height, stagger, launch, juggle, knockdown/wall response and finite
  round result/reset. No new gene duplicates every ordinary attack member.
- New genes: `SYS-1328` height-compatible damaging hold with the stagger
  exception; `SYS-1329` typed counter-damage relation; `SYS-1330` asymmetric
  fall/automatic-follow continuation; `SYS-1331` drawn double award and
  simultaneous-threshold reduced-life adjudication.
- Resolution order: eligible input, timing/height/range contact, compatible
  strike/guard/throw/hold consequence, counter class and displacement/wall or
  permitted fall response, resulting vitality and KO; absent KO, timer expiry
  compares remaining vitality. Award markers, either reset the ordinary round,
  settle a unique threshold winner or begin the required sudden death.
  The source does not expose internal same-frame event ordering; this is a
  causal reconstruction, not engine code.
- Parameters: command mapping, move family, height, timing, damage class,
  current tier/edge, round settings and champion designation. No exact
  multipliers, health totals, window lengths or universal wall explosion.
- Claim IDs: `DOA-003`–`DOA-008`.

### Constraint Genes

- Existing gene IDs: `CON-442`, `CON-446`. Fighter pose/recovery and target
  posture gate commands; ordinary attack/guard are unavailable while staggered,
  but a suitable hold remains an explicit exception. Zero life or declared
  time boundary demands round adjudication; required count is necessary but
  not sufficient for simultaneous-threshold victory.
- New gene: `CON-763`, lateral spacing on wall-bounded tiers with selective
  forced-departure edges. `CON-625` excludes tier transitions, `CON-667`
  excludes walls and `CON-733` requires terminal ring departure; none admits
  this complete arena unchanged.
- Scarce strategic resources: round-local vitality and remaining clock,
  limited safe positioning and recovery opportunities, not inventory or a
  later game's super/guard resource meter.
- Claim IDs: `DOA-002`–`DOA-008`.

### Information Genes

- Existing gene IDs: `INF-142`, `INF-209`, `INF-210`. Paired body geometry,
  attack/recovery poses, two life bars, current round timer and set lights.
  `INF-209` is conservatively Limited/Medium for uninterrupted framing and
  every recovery form: the manual contains static views and P2 describes
  moving fighters, not a locally inspected continuous sequence. Sound was
  not played; exact numerical timing is not asserted from these sources.
- Candidate genes: none; no future-command preview, full frame table, or
  generic genre label masquerading as a mechanic.
- Claim IDs: `DOA-009`, `DOA-010`.

### Objective Genes

- New gene: `OBJ-282`, final fixed-pair victory after required awards and any
  simultaneous-threshold adjudication. `OBJ-099` requires earning the count
  before the opponent; `OBJ-259` includes terminal ring departure and the
  retained simultaneous drawn VS outcome. Neither is silently rewritten.
- Success, evaluation and failure: the declared side receives the match
  victory; KO/time loss can award the opponent a round, not always the match.
  Both reaching the threshold is not itself victory for either. No ranking,
  unlock or Survival score enters this objective.
- Claim IDs: `DOA-007`, `DOA-008`.

### Time Genes

- Existing gene ID: `TIM-003`. Both participants' movement and attacks,
  recovery and round time advance while further eligible input remains open.
- Candidate genes: none; command windows and the selected 60-second option
  are parameters, not a separate turn clock.
- Claim IDs: `DOA-002`, `DOA-007`, `DOA-009`.

## Reproducible transitions

Qualitative source-derived cases, not recorded native runs or numeric traces.

| Before | Action | Qualitative source-derived resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| Right-facing fighter receives a middle strike | Time back+F in DREAMCAST | Suitable middle hold intercepts and counters; no separate punch/kick input | Three-class mapping, not four-class Arcade | DOA-003 |
| A compatible stagger blocks ordinary attack and guard | Time the matching hold on the next strike | Hold remains an allowed way to reverse that strike | Explicit restricted-state exception | DOA-003 |
| Opponent attempts a hold in compatible range/state | Land a throw against it | High-counter damage class applies, not an assumed universal escape | Typed counter opportunity | DOA-004 |
| Ordinary throw catches the fighter | Time F+P in its response window | Eligible ordinary throw is escaped | Throw response differs from strike hold | DOA-002 |
| Fighter is about to land from an eligible knockdown | Input P/K/F | Defensive position avoids going down; certain attacks disallow it | State-gated recovery | DOA-002 |
| Fighter is knocked against a wall and weakened | Hold the documented lateral direction while rising | Pivot recovery changes the response | Wall state is not an instant terminal | DOA-006 |
| Positive-life defender is at an eligible Opera edge | Land a compatible displacing strike/throw | Defender falls and loses life; attacker follows safely; surviving duel continues below | Fall is not Ring Out | DOA-005 |
| Same pair faces an ineligible edge/move | Attempt forced departure | No universal departure is promised | Arena/move predicates remain necessary | DOA-005 |
| Timer reaches zero, life differs | Adjudicate | Greater remaining life earns a set | Finite time condition | DOA-007 |
| Both have one set, then double KO | Award the drawn set | Both receive the second marker; lower-life sudden death begins | Simultaneous qualification is not final victory | DOA-007 |
| Lower-life sudden death still has no clear winner | Adjudicate under the booklet | Designated champion wins; identity is unresolved here | Explicit uncertainty, not guessed P1 | DOA-008 |

## Strategic and experiential structure

- Local decision: distinguish strike height from throw/hold opportunities and
  choose positioning, block, reversal or a recovery compatible with the body.
- Medium-term planning: preserve life and advantageous wall/edge position;
  a hold can reverse pressure but exposes a typed throw punishment.
- Long-term structure: collect required rounds; simultaneous thresholds change
  the remaining decision into a lower-life adjudicating fight.
- Common heuristics: do not substitute standing guard for every low, do not
  assume every hold catches every class, and do not confuse a tier drop with
  a positive-life ring-out victory. These are source-derived advice, not
  empirically measured optimal policy.
- Failure attribution: wrong class, range, timing or actionable state, unsafe
  wall/edge placement, zero life or inferior life at expiry.
- Player-trust factors: visible set/health/time feedback supports attribution;
  unavailable numeric frames and unresolved fallback champion identity limit
  exact reproduction, expressly rather than concealed in prose.
- Claim IDs: `DOA-002`–`DOA-010`.

## Replay and variation

- What changes between sessions: human choices, timing and movement. The
  analytical pair/stage/options stay fixed; a different fighter is a parameter
  change needing repertoire review, not a random board claim.
- Randomness or procedural generation: none asserted for the scoped rules.
- Multiple viable strategies: safer guard/spacing, timed holds and throw
  punishment, or eligible wall/tier displacement; no performance ranking.
- Typical replay motive: improve attack recognition and counter choice.
- Claim IDs: `DOA-002`–`DOA-009`.

## Adjacent systems and history

- Direct predecessors: original Dead or Alive is historical context, not an
  independently admitted signature or verified rules equivalence here.
- Variants: Arcade control type, Hardcore, Ultimate, Japanese Limited Edition
  and Tag/Survival are not substituted for original ordinary Dreamcast Versus.
- Similar games: selected corpus neighbour below; no non-selected score list.
- Important differences: damaging holds versus impact priority, tier
  continuation versus terminal ring departure, and additional threshold
  adjudication versus retaining a final simultaneous drawn VS result.
- Claim IDs: `DOA-003`–`DOA-011`.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-008`, `ACT-202`, `ACT-223`, `ACT-294`, `ACT-295`, `ACT-296`, `ACT-297`, `ACT-605` | Fighters, button/direction sequence and recovery form |
| System Behaviour | `SYS-215`, `SYS-522`, `SYS-1328`, `SYS-1329`, `SYS-1330`, `SYS-1331` | Counter class, tier transition, life and draw protocol |
| Constraint | `CON-442`, `CON-446`, `CON-763` | Compatible state, round options and eligible edge |
| Information | `INF-142`, `INF-209`, `INF-210` | Body framing, animations and HUD fields |
| Objective | `OBJ-282` | Declared side, required count and tiebreak |
| Time | `TIM-003` | Real-time update and input windows |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `493` (`GAME-0001`–`GAME-0493`).
- Exact genome matches: none.
- Tied near matches: `GAME-0393` — Mortal Kombat II (`14 / 24 = 0.583333`).
- Supported combination subsets: none.
- Scan date: 2026-10-04.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0393` — Mortal Kombat II | `ACT-008`, `ACT-202`, `ACT-294`, `ACT-295`, `ACT-296`, `ACT-297`, `SYS-215`, `SYS-522`, `CON-442`, `CON-446`, `INF-142`, `INF-209`, `INF-210`, `TIM-003` | Both expose a live paired-body duel, posture, attack/guard/throw, vitality/time and repeated round awards. The SNES first CPU match has a bounded side-view line and first-to-two/five-round disqualification. Dreamcast Opera permits lateral tier positioning, height-compatible damaging holds even during stagger, stronger typed counters and asymmetric fall continuation; simultaneous qualification requires lower-life adjudication rather than simply reaching the count before the opponent. Controller mappings and names do not prove executable parity | Near, `0.583333` |

### Preserved research notes

- New genes: six additions in `TAXONOMY_CHANGE_231`.
- Classification result: `New gene`.
- Evidence and reasoning: original-console source boundaries remain
  distinct from existing impact and ring-out carriers without revising them.

## Taxonomy impact

- Registry changes: four system, one constraint and one objective addition;
  sixteen unchanged transfers. No older signature or English boundary changes.
- Taxonomy-change record: `TAXONOMY_CHANGE_231`.
- Candidate terms affected: no suggestion-term promotion or external novelty.
- Named presentation review partitions all 22 uses into five defining,
  thirteen structural and four supporting roles with complete bilingual causal
  cards. Existing `FAM-009` and `FAM-010` suffice. Roles do not weight Jaccard.

## Negative results

No gene for Kasumi/Ein, costume, named Opera, two sets or 60 seconds, numerical
damage, copied full move list, every wall exploding, generic instant ring-out,
four-class holds in the selected mapping, guessed champion identity or
later-edition resources. No new recurring combination from one carrier.

## Delta summary

## New facts

- [Observation | Corroborated | High] Original Dreamcast three-height holds
  differ from Arcade inputs; eligible stagger does not remove holds, DOA-003.
- [Observation | Direct | High] Tier falling applies asymmetric damage and
  continues the same duel, DOA-005.
- [Observation | Limited | Medium] The further-draw champion rule is retained
  without assigning an unverified participant identity, DOA-008.

## New genes

- [Observation | Corroborated | High] `SYS-1328`.
- [Observation | Direct | High] `SYS-1329`, `SYS-1330`, `CON-763`, `OBJ-282`.
- [Observation | Limited | Medium] `SYS-1331`; its final champion identity
  parameter remains unresolved, not fabricated.

## New combinations

- [Observation | Direct | High] Complete proper-subset scan recorded above;
  no new recurring pattern is established merely by this carrier.

## Taxonomy changes

- [Observation | Direct | Medium] `TAXONOMY_CHANGE_231` admits six boundaries
  and sixteen transfers without modifying earlier signatures.

## New questions

- Which exact side is the original USA Versus champion after a further
  drawn sudden death, and can a native controlled trace settle this?
- What are the complete pair-specific input chart and exact timing/damage
  windows of the pinned original disc, without importing later revisions?

## Next recommended game

- [Hypothesis | Limited | Medium] Donkey Kong Country Returns, original Wii
  2010, final approved `GAME-0495` unit.
- Optimisation criterion: complete the approved cross-platform horizon rather
  than select another fighting-game carrier.
- Expected information gain: cooperative platforming, motion-driven actions
  and route-state progression after a fixed two-fighter packet.
- Backlog impact: stop after this final approved unit; no further batch or
  public publication is implied.

## Why this game

- [Hypothesis | Limited | Medium] Original Dreamcast controls and arena
  transitions provide operational transfer tests rather than genre resemblance.
