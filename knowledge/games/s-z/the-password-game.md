---
game_id: GAME-0102
slug: the-password-game
game_title: The Password Game
analysis_status: reviewed
reviewed: 2026-08-15
combination_ids:
  - COMB-0102
gene_ids:
  action:
    - ACT-103
  system:
    - SYS-135
    - SYS-136
  constraint:
    - CON-156
  information:
    - INF-030
  objective:
    - OBJ-006
  time:
    - TIM-002
---

# Game: The Password Game

## Analysis scope

- Version / ruleset: Neal Agarwal's live browser game, bounded to the fixed
  opening Rules 1-9 and the transition that reveals Rule 10.
- Included: one persistent editable password; live per-rule feedback; fixed
  sequential revelation; retained earlier rules; minimum length, number,
  uppercase and special-character predicates; digit sum 25; month name; Roman
  numeral; one of three displayed sponsors; Roman-numeral product 35; no timer.
- Excluded: Rule 10's generated CAPTCHA and Rules 10-35, including daily
  Wordle, country, chess, Paul, formatting, fire, sacrifice, time and final
  confirmation; full-game victory, advertisements and platform metadata.
- Direct-play status: conducted on 2026-08-15. Entering
  `A!997maypepsiVqVII` revealed Rule 10 with Rules 1-9 satisfied. Removing `!`
  left the later rules revealed while Rule 4 regressed to failure; restoring it
  recovered the all-valid state. The executable control models only this fixed
  packet and does not reproduce later generated content.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `TPG-001` | The browser game begins with one editable password and reveals 35 rules sequentially | Confirmed | Direct | High | P1, S1 |
| `TPG-002` | Rules 1-9 are the fixed predicates recorded in this scope | Confirmed | Direct | High | P1, S1 |
| `TPG-003` | A new rule appears only after all currently revealed rules pass | Observation | Direct | High | P1, V1 |
| `TPG-004` | Revealed earlier rules remain active and may regress after later edits | Observation | Direct | High | P1, V1 |
| `TPG-005` | `A!997maypepsiVqVII` satisfies Rules 1-9 and reveals Rule 10 | Observation | Direct | High | P1, V1 |

## Basic data

- Release / origin: created by Neal Agarwal and released as a free browser game
  in 2023.
- Platform or physical form: single-player web puzzle with one rich-text input
  and a growing stack of rule cards.
- Puzzle family: cumulative constraint satisfaction over one mutable string.
- Creator and primary sources:
  - **[P1]** [Official live game](https://neal.fun/password-game/), for the
    executable input, exact opening rules, live feedback and reveal order.
- Secondary sources:
  - **[S1]** [PCGamesN complete rule list](https://www.pcgamesn.com/the-password-game/rules),
    for an independently recorded ordering of all 35 rules and exact Rules 1-9.
  - **[S2]** [Wikipedia overview](https://en.wikipedia.org/wiki/The_Password_Game),
    for creator, year and the cumulative 35-rule structure.
  - **[V1]** [`verify_password_game_rules.py`](../../../scripts/verify_password_game_rules.py),
    an independent bounded state model.

## Mechanical decomposition

### Action Genes

- `ACT-103` — edit one persistent free-form answer string. Insertions and
  deletions anywhere revise the same password rather than submit separate guesses.

### System Behaviour Genes

- `SYS-135` — live revalidation of every revealed answer predicate. Each edit
  reevaluates all visible rules and can invalidate an earlier green card.
- `SYS-136` — all-valid state reveals the next authored rule. Passing the
  current conjunction permanently extends the rule stack by one.
- Resolution order: accept edit; evaluate every revealed predicate; update
  pass/fail feedback; if all pass, reveal the next fixed rule and evaluate again.

### Constraint Genes

- `CON-156` — revealed rules remain jointly binding on one mutable answer.
  Solving Rule 9 does not retire Rules 1-8.
- Rules 1-9 are parameters of this boundary: length at least five; at least one
  digit, uppercase letter and special character; digit sum 25; a month name; a
  Roman numeral; Pepsi, Starbucks or Shell; Roman-numeral product 35.

### Information Genes

- `INF-030` — live exact-subconstraint satisfaction indication. Every visible
  rule card exposes whether its own current predicate passes before completion.

### Objective Genes

- `OBJ-006` — complete constraint-satisfying assignment. The bounded success
  state is one password satisfying all nine declared predicates simultaneously.

### Time Genes

- `TIM-002` — self-paced sequential action. The opening window has no deadline
  or autonomous state change between edits.

## Reproducible transitions

| Before | Action | Deterministic resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| Only Rule 1 visible | Enter `A!997maypepsiVqVII` | Rules cascade in fixed order until Rule 10 appears | sequential reveal | `TPG-002`, `TPG-003`, `TPG-005` |
| Rules 1-9 pass | Delete `!` | Rule 4 fails; Rules 5-9 remain revealed | persistent cumulative scope | `TPG-004` |
| Rule 4 fails after regression | Restore `!` | All Rules 1-9 pass again | live revalidation and recovery | `TPG-004`, `TPG-005` |
| Digit sum is 25 | Remove one `9` | Rule 5 fails without replacing later cards | exact local predicate | `TPG-002`, `TPG-004` |
| Roman product is 35 | Change `VII` to `VI` | Rule 9 fails | full-string interaction | `TPG-002` |

## Strategic and experiential structure

- Local decision: change as few characters as possible while watching which
  previously passing rule cards regress.
- Medium-term planning: choose substrings that satisfy several predicates
  without accidentally introducing conflicting digits or Roman numerals.
- Long-term structure: outside this packet, later rules increase cross-rule
  interference; no claim about their generated values transfers here.
- Common heuristics: reserve distinct substrings for arithmetic, month,
  sponsor and Roman constraints; preserve a known-good prefix; edit minimally.
- Failure attribution: per-rule feedback identifies the currently broken
  predicates, but the player must discover which shared characters caused them.
- Player-trust factors: authored order must be stable, all visible rules must be
  reevaluated consistently, and a passed rule cannot be silently retired.

## Replay and variation

- Rules 1-9 and their order are fixed, but many strings satisfy them.
- Different construction orders produce different cascades and regressions.
- Random and daily variation begins outside the boundary at Rule 10.

## Adjacent systems and history

- Hexologic also gives live local satisfaction feedback and pursues a complete
  constraint assignment, but exposes its fixed clue set up front across many
  cells rather than growing rules over one string.
- Baba Is You changes active rules by moving word objects. Here the authored
  rules are immutable and accumulate automatically, so `SYS-017`, `SYS-018`
  and `INF-008` do not transfer.
- Wordle submits separate immutable guesses against a concealed answer; it does
  not preserve one freely editable string or an accumulating rule conjunction.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-103` | character repertoire; formatting |
| System Behaviour | `SYS-135`, `SYS-136` | evaluation order; reveal animation |
| Constraint | `CON-156` | nine opening predicates |
| Information | `INF-030` | pass/fail styling |
| Objective | `OBJ-006` | reveal Rule 10 boundary |
| Time | `TIM-002` | no forced clock |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `101` (`GAME-0001`–`GAME-0101`).
- Exact genome matches: none.
- Tied near matches: `GAME-0062` — Hexologic (`3 / 12 = 0.250000`).
- Supported combination subsets: `COMB-0102`.
- Scan date: 2026-08-15.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| Hexologic (`GAME-0062`) | `INF-030`, `OBJ-006`, `TIM-002` | fixed visible line constraints over many cells versus an authored growing rule stack over one string | Near, `0.250000` |

### Preserved research notes

- New genes: `ACT-103`, `SYS-135`, `SYS-136`, `CON-156`.
- Classification result: `New gene` and `New combination of known and new genes`.
- Evidence and reasoning: editable string, cumulative revalidation and reveal
  boundaries are absent; live local feedback, assignment objective and timing transfer.

## Taxonomy impact

- Registry changes: four Active IDs and three transfers to a new game.
- Taxonomy-change record: none; no existing boundary is merged or retired.
- Candidate terms affected: new boundaries recorded in `CANDIDATE_TERMS.md`.

## Negative results

- `ACT-060` rejected: there are no typed phrase slots or supplied word bank.
- `SYS-073` and `SYS-086` rejected: validation is live, not submit-time.
- `SYS-017`, `SYS-018` and `INF-008` rejected: rule text is not movable syntax.
- `ACT-073` rejected: edits revise one answer rather than submit a fixed guess.
