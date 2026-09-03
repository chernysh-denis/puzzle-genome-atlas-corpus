---
game_id: GAME-0067
slug: simon
game_title: Simon
analysis_status: reviewed
reviewed: 2026-08-14
combination_ids:
  - COMB-0067
gene_ids:
  action:
    - ACT-076
  system:
    - SYS-004
    - SYS-107
    - SYS-108
  constraint: []
  information:
    - INF-002
    - INF-033
  objective:
    - OBJ-002
  time:
    - TIM-012
---

# Game: Simon

## Analysis scope

- Version / ruleset: Hasbro Simon product `B7962`, 2015 English instructions,
  one fresh solo attempt from the one-cue opening through the first incorrect
  response and displayed score.
- Included: four coloured pads; one light-and-sound cue per pad; automatic
  serial presentation; exact ordered reproduction; retention of the previous
  sequence; one randomly selected appended cue after each correct round;
  immediate failure after an incorrect pad; score as the longest completed
  sequence; stored high score as an optional replay benchmark; mute mode.
- Excluded: the original 1978 model's Games 2 and 3, skill levels, automatic
  tempo thresholds, five-second response rule, Last / Longest recall controls
  and multiplayer procedures; later themed, wearable, app and Mini variants;
  battery handling, volume adjustment as strategy, inactivity shutdown,
  accessibility quality and competitive speed records.
- Direct-play status: no physical-device attempt was conducted. The bounded
  transition system was reproduced from the current official instructions and
  corroborated by the original patent. A fixed generated stream `G R G Y B R`
  produced five exact rounds. On round six, response `G R G Y B B` first
  differs at position six, ends the attempt and preserves score five.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `SIM-001` | The current device has four coloured pads and associates each with light-and-sound feedback | Confirmed | Direct | High | P1, P2 |
| `SIM-002` | A solo attempt begins with one presented cue and requires the player to press the corresponding pad | Confirmed | Direct | High | P2 |
| `SIM-003` | Every completely correct response causes the system to replay the retained sequence and append exactly one cue | Confirmed | Corroborated | High | P1, P2, H1, A1 |
| `SIM-004` | Response identity and ordinal position must both match; the first wrong pad ends the attempt | Confirmed | Corroborated | High | P2, H1, A1 |
| `SIM-005` | The next appended cue is randomly selected and unavailable before the next presentation | Confirmed | Corroborated | High | P1, H1 |
| `SIM-006` | The score measures the longest sequence completed in the attempt, not the cumulative number of pad presses | Confirmed | Direct | High | P1, P2 |
| `SIM-007` | Earlier target cues are transient rather than retained as a visible symbolic history during response | Pattern | Corroborated | High | P1, P2, A1 |
| `SIM-008` | Current mute mode makes sound redundant rather than mechanically mandatory; the coloured lights remain sufficient cues | Confirmed | Direct | High | P2 |
| `SIM-009` | The current core loop does not document the original model's five-second input limit or fixed skill targets | Confirmed | Direct | High | P2, H2 |
| `SIM-010` | Simon requires new ordered-reproduction, retained-extension, transient-presentation and alternating-phase boundaries without a new gene type | Observation | Corroborated | High | `SIM-001`–`SIM-009` |

## Basic data

- Release / origin: the Smithsonian dates the Milton Bradley electronic game
  to 1978 and credits Ralph Baer's design work; the scoped record uses the
  current Hasbro `B7962` rules rather than importing every original mode.
- Platform or physical form: handheld tabletop electronic device with four
  coloured pressable pads, lights and sound.
- Puzzle family: escalating transient-sequence reproduction.
- Primary and official sources:
  - **[P1] Hasbro product instructions page:** [Simon Game](https://instructions.hasbro.com/en-us/instruction/simon-game),
    product `B7962`. It identifies the random light sequence, exact pad-order
    response, progressive lengthening, solo play and high-score objective.
  - **[P2] Hasbro instruction PDF:** [Simon Game B7962 rules](https://instructions.hasbro.com/api/download/B7962_en-us_simon-game.pdf),
    document `B79620000`, 2015. It supplies the start procedure, repeat-and-add
    loop, failed-sequence termination, light-encoded score, mute option and
    high-score storage.
- Historical and formal sources:
  - **[H1] US Patent 4,207,087:** [Microcomputer controlled game](https://patents.google.com/patent/US4207087A/en),
    Howard J. Morrison and Ralph H. Baer. It formalises four keys with paired
    tone / light cues, random sequence generation, exact response comparison,
    replay plus one item and error termination.
  - **[H2] Original 1978 instruction sheet:** [Simon 4850 rules](https://www.hasbro.com/common/documents/3f4e2ca0206011ddbd0b0800200c9a66/620962835056900B10D1688756D7BA4A.pdf).
    It is used only to identify excluded old skill levels, games and timing.
  - **[H3] Smithsonian National Museum of American History:** [Simon electronic game](https://www.si.edu/object/nmah_1302005),
    documenting the four-button increasingly long repeat task and 1978 object.
- Academic corroboration:
  - **[A1] Huang et al.:** [“Fast-backward replay of sequentially memorized items in humans”](https://doi.org/10.7554/eLife.35164),
    *eLife* 7, 2018. Its digest independently describes Simon as ordered
    coloured-light reproduction whose sequence lengthens per trial and whose
    attempt ends after one wrong response. The neural findings are not imported
    as game mechanics.
- Claim IDs: `SIM-001`–`SIM-010`.

## Mechanical decomposition

### Action Genes

- `ACT-076` — reproduce presented ordered cue sequence. During the response
  phase, each pad press asserts one symbol at its current ordinal position. A
  complete round is not an editable proposal submitted afterward: every press
  is already compared against the displayed target prefix.
- `ACT-073` does not apply. Mastermind permits composing a whole row before one
  aggregate query; Simon serially adjudicates a remembered target and ends on
  the first wrong input.
- Claim IDs: `SIM-001`, `SIM-002`, `SIM-004`, `SIM-010`.

### System Behaviour Genes

- `SYS-004` — random outcome selection. After a successful round, the appended
  pad identity is selected by the device rather than by the player.
- `SYS-107` — retained-sequence replay with one-cue extension. The next target
  is the complete prior target followed by exactly one new cue, then the whole
  longer target is presented from its start.
- `SYS-108` — ordered-response first-mismatch adjudication. Each input is
  compared with the same ordinal cue. Full equality scores one completed
  sequence and advances; the first mismatch produces failure and termination.
- Random selection and extension are distinct: a deterministic authored stream
  could still retain and extend, while random selection alone need not create
  an accumulating ordered target.
- Claim IDs: `SIM-003`–`SIM-006`, `SIM-010`.

### Constraint Genes

- No active Constraint Gene is required. Exact order is the comparison rule in
  `SYS-108`, not merely a legality filter, because inputs are accepted and can
  terminate the attempt as state transitions.
- The four-pad vocabulary and one-cue extension are parameters of action and
  system behaviours. The current instructions do not establish the original
  model's five-second deadline, so `CON-068` is excluded.
- Claim IDs: `SIM-001`, `SIM-004`, `SIM-009`.

### Information Genes

- `INF-002` — unpreviewed random future event. Before successful completion of
  the current prefix, the player does not know which pad will be appended.
- `INF-033` — transient ordered-cue presentation. The entire current target is
  exposed one light at a time, then must be reconstructed without a persistent
  visible list. Each pad's sound can duplicate its identity, but mute mode
  proves that sound is not a separate mandatory rule channel.
- `INF-001` does not apply to the target: the complete decision-relevant
  sequence is not simultaneously visible while the response is entered.
- Claim IDs: `SIM-001`, `SIM-005`, `SIM-007`, `SIM-008`, `SIM-010`.

### Objective Genes

- `OBJ-002` — maximise accumulated score. The attempt score is the count of the
  longest fully reproduced sequence. It can be compared with a stored personal
  high score, but no fixed score threshold defines universal completion.
- The score is not the triangular number of individual pad presses. Completing
  sequences of lengths one through five displays five, not fifteen.
- Claim IDs: `SIM-006`.

### Time Genes

- `TIM-012` — alternating automatic presentation and player reproduction. The
  device owns the show phase; the player owns the following response phase;
  exact completion hands control back for the extended replay.
- `TIM-003` does not apply. There is no continuously progressing world that the
  player can interrupt while it advances, and the scoped current rules do not
  require a response deadline.
- Claim IDs: `SIM-002`–`SIM-004`, `SIM-009`, `SIM-010`.

## Reproducible transitions

The local control fixes one possible randomly generated stream as
`G R G Y B R`. `G`, `R`, `Y` and `B` identify green, red, yellow and blue. The
stream is a reproducible test fixture, not a claim about Hasbro's random-number
algorithm.

| Before | Automatic presentation / player action | Resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| Fresh attempt, score 0 | System presents `G`; player presses `G` | Position 1 matches; score becomes 1 | one-cue opening and exact response | `SIM-002`, `SIM-004` |
| Retained target `G`, score 1 | System presents `G R`; player presses `G R` | Prior cue is retained, one cue appended; score becomes 2 | replay-plus-one invariant | `SIM-003`, `SIM-006` |
| Retained target `G R`, score 2 | System presents `G R G`; player presses `G R G` | Repeated cue identity is legal; score becomes 3 | sequence is ordered, not a set of colours | `SIM-003`, `SIM-004` |
| After exact rounds of lengths 4 and 5, score 5 | System presents `G R G Y B R`; player presses `G R G Y B B` | Positions 1–5 match; position 6 does not; failure occurs and score remains 5 | first-mismatch terminal boundary | `SIM-004`, `SIM-006` |
| Before any correct response to round 6 | Ask which new pad follows `G R G Y B` | Only the presentation reveals `R`; no persistent target list remains during response | unpreviewed extension and transient evidence | `SIM-005`, `SIM-007` |

The verifier also substitutes each of the four pads at position six. Exactly
`R` completes the target; `G`, `Y` and `B` all fail first at position six. It
asserts at every round that the new target equals the complete prior target
plus one member of the four-pad vocabulary.

## Strategic and experiential structure

- Local decision: retrieve the next ordinal cue and press the matching pad,
  using light identity, spatial location and optionally tone as redundant
  memory traces.
- Medium-term planning: chunk the growing sequence into short motifs, rehearse
  the stable prefix during replay and allocate attention to the one appended
  suffix cue.
- Long-term structure: preserve exact serial recall across successively longer
  prefixes to raise the session score and, optionally, exceed the stored high
  score.
- Common heuristics: verbalise colours, encode spatial paths, group repeated
  motifs, or exploit rhythm while not confusing rhythm with the identity-order
  predicate.
- Failure attribution: the fail signal proves at least the current response
  position was wrong, but the attempt ends rather than allowing correction or
  displaying the remaining target as a persistent answer.
- Player-trust factors: earlier prefixes must replay unchanged, exactly one cue
  must be appended, every pad must retain stable light / spatial identity, and
  scoring must equal the longest completed length.
- Claim IDs: `SIM-003`–`SIM-008`.

## Replay and variation

- What changes between sessions: random cue identities create another ordered
  stream, while the four controls and repeat-and-extend rules remain fixed.
- Randomness or procedural generation: one cue is selected only after the
  current target is completed. The next cue is therefore unpredictable, but
  every already presented prefix is known and invariant.
- Multiple viable strategies: colour names, locations, tones, motor chunks and
  rhythmic grouping can encode the same target; mute mode removes tone without
  changing correctness.
- Typical replay motive: surpass the personal longest-sequence score or test a
  different mnemonic strategy against another random stream.
- Claim IDs: `SIM-003`, `SIM-005`, `SIM-006`, `SIM-008`.

## Adjacent systems and history

- Mastermind also uses ordered symbols, but its secret remains hidden and is
  inferred through editable complete queries with aggregate duplicate-aware
  feedback. Simon directly presents the target transiently and asks for exact
  reproduction, terminating at the first mismatching symbol.
- Black Box also separates hidden state from visible evidence, but its probes
  accumulate persistent spatial constraints toward one accepted layout. Simon
  removes the presented list and continually grows it instead of solving one
  fixed concealed state.
- Braid alternates neither target presentation nor memory recall: its real-time
  scene remains visible and the player reverses an authored simulation history.
- The 1978 device introduced additional games, skill caps, faster tempo and a
  five-second rule. Those properties demonstrate historical variation but are
  not evidence for the current `B7962` solo genome.
- Claim IDs: `SIM-003`, `SIM-004`, `SIM-007`, `SIM-009`.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-076` | four pads, per-symbol input |
| System Behaviour | `SYS-004`, `SYS-107`, `SYS-108` | random cue, plus-one extension, first mismatch |
| Constraint | none | four-symbol vocabulary is a parameter |
| Information | `INF-002`, `INF-033` | unknown suffix; transient audiovisual sequence |
| Objective | `OBJ-002` | longest completed sequence / high score |
| Time | `TIM-012` | presentation / response alternation |

Canonical signature:

`ACT-076; SYS-004,SYS-107,SYS-108; ; INF-002,INF-033; OBJ-002; TIM-012`

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `66` (`GAME-0001`–`GAME-0066`).
- Exact genome matches: none.
- Tied near matches: `GAME-0001` — 2048 (`3 / 19 = 0.157895`).
- Supported combination subsets: `COMB-0067`.
- Scan date: 2026-08-14.

### Selected-neighbour interpretation

No pre-migration reviewed selected-neighbour table row exists for: `GAME-0001`.

## Taxonomy impact

- Added five active genes: `ACT-076`, `SYS-107`, `SYS-108`, `INF-033` and
  `TIM-012`.
- Reused `SYS-004`, `INF-002` and `OBJ-002` without broadening their boundaries.
- No Constraint Gene applies and no seventh gene type is justified.
- Registered `COMB-0067` as the proper interaction subset that excludes the
  generic randomness, unknown-future and score shell.

## Negative results

- No evidence supports importing the original five-second response rule into
  current `B7962`; inactivity shutdown is not treated as a gameplay deadline.
- No evidence supports a persistent visible sequence history, editable
  response, aggregate partial-credit score or correction after one error.
- Sound is not encoded as a separate requirement because the official mute
  mode preserves play through lights and stable pad locations.
- The next cue's random generator algorithm and probability distribution are
  undocumented; the control stream demonstrates rules, not implementation.
- The stored high score does not add a second objective gene: it is a retained
  benchmark for the same longest-sequence measurement.
