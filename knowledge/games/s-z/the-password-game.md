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

- Genome signature `(ACT; SYS; CON; INF; OBJ; TIM)`:
  `(ACT-103; SYS-135,SYS-136; CON-156; INF-030; OBJ-006; TIM-002)`.
- Indexed games scanned: 102, including this record.
- Indexed combinations scanned: 102.
- Exact genome matches: none.
- Near match: `GAME-0062` — Hexologic at `3 / 12 = 0.250000`.
- Supported combination subsets: `COMB-0102` only.
- Scan date: 2026-08-15.

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| Hexologic (`GAME-0062`) | `INF-030`, `OBJ-006`, `TIM-002` | fixed visible line constraints over many cells versus an authored growing rule stack over one string | nearest at `3 / 12 = 0.250000` |
| Sudoku (`GAME-0005`) | `OBJ-006`, `TIM-002` | fixed grid domains and units versus unrestricted string editing and sequential revelation | background at `2 / 12 = 0.166667` |

### Full prior-game Jaccard scan

- `GAME-0001`: `0 / 21 = 0.000000`; `GAME-0002`: `1 / 13 = 0.076923`; `GAME-0003`: `0 / 16 = 0.000000`; `GAME-0004`: `0 / 22 = 0.000000`.
- `GAME-0005`: `2 / 12 = 0.166667`; `GAME-0006`: `1 / 15 = 0.066667`; `GAME-0007`: `1 / 14 = 0.071429`; `GAME-0008`: `2 / 12 = 0.166667`.
- `GAME-0009`: `0 / 23 = 0.000000`; `GAME-0010`: `0 / 16 = 0.000000`; `GAME-0011`: `1 / 19 = 0.052632`; `GAME-0012`: `2 / 14 = 0.142857`.
- `GAME-0013`: `0 / 20 = 0.000000`; `GAME-0014`: `0 / 22 = 0.000000`; `GAME-0015`: `0 / 21 = 0.000000`; `GAME-0016`: `0 / 22 = 0.000000`.
- `GAME-0017`: `0 / 20 = 0.000000`; `GAME-0018`: `0 / 26 = 0.000000`; `GAME-0019`: `0 / 17 = 0.000000`; `GAME-0020`: `0 / 21 = 0.000000`.
- `GAME-0021`: `0 / 16 = 0.000000`; `GAME-0022`: `0 / 19 = 0.000000`; `GAME-0023`: `1 / 16 = 0.062500`; `GAME-0024`: `1 / 18 = 0.055556`.
- `GAME-0025`: `0 / 18 = 0.000000`; `GAME-0026`: `0 / 19 = 0.000000`; `GAME-0027`: `0 / 19 = 0.000000`; `GAME-0028`: `0 / 24 = 0.000000`.
- `GAME-0029`: `0 / 19 = 0.000000`; `GAME-0030`: `0 / 21 = 0.000000`; `GAME-0031`: `0 / 18 = 0.000000`; `GAME-0032`: `0 / 18 = 0.000000`.
- `GAME-0033`: `0 / 20 = 0.000000`; `GAME-0034`: `0 / 21 = 0.000000`; `GAME-0035`: `0 / 25 = 0.000000`; `GAME-0036`: `1 / 18 = 0.055556`.
- `GAME-0037`: `0 / 16 = 0.000000`; `GAME-0038`: `0 / 23 = 0.000000`; `GAME-0039`: `2 / 14 = 0.142857`; `GAME-0040`: `1 / 14 = 0.071429`.
- `GAME-0041`: `0 / 18 = 0.000000`; `GAME-0042`: `0 / 16 = 0.000000`; `GAME-0043`: `0 / 21 = 0.000000`; `GAME-0044`: `0 / 17 = 0.000000`.
- `GAME-0045`: `0 / 21 = 0.000000`; `GAME-0046`: `1 / 16 = 0.062500`; `GAME-0047`: `0 / 21 = 0.000000`; `GAME-0048`: `0 / 21 = 0.000000`.
- `GAME-0049`: `0 / 16 = 0.000000`; `GAME-0050`: `0 / 22 = 0.000000`; `GAME-0051`: `0 / 23 = 0.000000`; `GAME-0052`: `0 / 17 = 0.000000`.
- `GAME-0053`: `0 / 16 = 0.000000`; `GAME-0054`: `0 / 18 = 0.000000`; `GAME-0055`: `0 / 17 = 0.000000`; `GAME-0056`: `0 / 15 = 0.000000`.
- `GAME-0057`: `0 / 15 = 0.000000`; `GAME-0058`: `0 / 16 = 0.000000`; `GAME-0059`: `0 / 14 = 0.000000`; `GAME-0060`: `0 / 14 = 0.000000`.
- `GAME-0061`: `2 / 15 = 0.133333`; `GAME-0062`: `3 / 12 = 0.250000`; `GAME-0063`: `1 / 13 = 0.076923`; `GAME-0064`: `1 / 11 = 0.090909`.
- `GAME-0065`: `1 / 13 = 0.076923`; `GAME-0066`: `1 / 16 = 0.062500`; `GAME-0067`: `0 / 15 = 0.000000`; `GAME-0068`: `1 / 14 = 0.071429`.
- `GAME-0069`: `1 / 14 = 0.071429`; `GAME-0070`: `0 / 15 = 0.000000`; `GAME-0071`: `2 / 12 = 0.166667`; `GAME-0072`: `2 / 13 = 0.153846`.
- `GAME-0073`: `2 / 12 = 0.166667`; `GAME-0074`: `2 / 14 = 0.142857`; `GAME-0075`: `2 / 14 = 0.142857`; `GAME-0076`: `2 / 12 = 0.166667`.
- `GAME-0077`: `2 / 12 = 0.166667`; `GAME-0078`: `2 / 12 = 0.166667`; `GAME-0079`: `2 / 12 = 0.166667`; `GAME-0080`: `2 / 12 = 0.166667`.
- `GAME-0081`: `2 / 13 = 0.153846`; `GAME-0082`: `2 / 13 = 0.153846`; `GAME-0083`: `2 / 13 = 0.153846`; `GAME-0084`: `2 / 15 = 0.133333`.
- `GAME-0085`: `1 / 17 = 0.058824`; `GAME-0086`: `1 / 19 = 0.052632`; `GAME-0087`: `0 / 17 = 0.000000`; `GAME-0088`: `1 / 15 = 0.066667`.
- `GAME-0089`: `0 / 16 = 0.000000`; `GAME-0090`: `1 / 21 = 0.047619`; `GAME-0091`: `0 / 16 = 0.000000`; `GAME-0092`: `0 / 17 = 0.000000`.
- `GAME-0093`: `1 / 15 = 0.066667`; `GAME-0094`: `0 / 17 = 0.000000`; `GAME-0095`: `0 / 19 = 0.000000`; `GAME-0096`: `0 / 17 = 0.000000`.
- `GAME-0097`: `0 / 15 = 0.000000`; `GAME-0098`: `0 / 14 = 0.000000`; `GAME-0099`: `0 / 15 = 0.000000`; `GAME-0100`: `0 / 18 = 0.000000`.
- `GAME-0101`: `1 / 16 = 0.062500`.

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

## Delta summary

## Нові факти

- [Observation | Direct | High] Перші дев’ять правил утворюють сталу
  кон’юнкцію над одним рядком; нова вимога не скасовує попередніх
  (`TPG-002`–`TPG-005`).

## Нові гени

- [Observation | Direct | High] `ACT-103` — редагування одного сталого
  вільного рядка відповіді.
- [Observation | Direct | High] `SYS-135` — жива повторна перевірка всіх
  відкритих предикатів.
- [Observation | Direct | High] `SYS-136` — відкриття наступного правила лише
  після одночасного виконання поточного набору.
- [Observation | Direct | High] `CON-156` — усі відкриті правила залишаються
  обов’язковими для тієї самої відповіді.

## Нові комбінації

- [Confirmed | Direct | High] `COMB-0102` — розширювати кумулятивну систему
  правил над одним редагованим рядком.

## Зміни таксономії

- Не потрібні: нові межі додаються без зміни чинних визначень.
