---
game_id: GAME-0101
slug: chants-of-sennaar
game_title: Chants of Sennaar
analysis_status: reviewed
reviewed: 2026-08-15
combination_ids:
  - COMB-0101
gene_ids:
  action:
    - ACT-049
    - ACT-101
    - ACT-102
  system:
    - SYS-134
  constraint:
    - CON-154
    - CON-155
  information:
    - INF-051
    - INF-052
  objective:
    - OBJ-026
  time:
    - TIM-002
---

# Game: Chants of Sennaar

## Analysis scope

- Version / ruleset: released game and official demo's opening Devotee
  tutorial, from the first lever and door through the first forced notebook
  page and six-valve instruction `open, open, closed, open, closed, open` to
  passage through the next gate.
- Included: one traveller; three recurring untranslated glyphs for open,
  closed and door; contextual observation; editable notebook glosses; six
  reachable binary valves; one illustrated three-slot journal page; complete-
  page correction and canonicalisation; a forced validation gate; self-paced
  traversal.
- Excluded: later Devotee glyphs; the other four languages; grammar, plural
  and word-order inference; stealth; later conversations; terminals, links,
  collectibles, achievements and the ending.
- Direct-play status: not conducted. Official material establishes the five-
  language observation and notebook loop. Creator testimony establishes
  recurring context, annotations and automatic translation. A Rundisc
  developer confirms that only the first three words are forcibly validated
  before progress. Two walkthroughs corroborate their meanings, illustrated
  page and six-valve order. The executable control tests that bounded rule,
  not the production glyph artwork or internal code.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `COS-001` | The game asks the player to decipher five interconnected fictional languages by observing, conversing and recording symbols | Confirmed | Direct | High | P1, P2 |
| `COS-002` | Its design supports provisional annotation and later automatic translation, with words repeated across different contexts | Confirmed | Direct | High | P2 |
| `COS-003` | The opening tutorial introduces exactly three forced words: open, closed and door | Confirmed | Corroborated | High | P3, S1 |
| `COS-004` | The first valve instruction resolves to open, open, closed, open, closed, open | Confirmed | Corroborated | High | S1, S2 |
| `COS-005` | The first journal page requires a complete one-to-one match of those glyphs to illustrated meanings and gates progress | Confirmed | Corroborated | High | P3, S1 |
| `COS-006` | The control rejects incomplete, duplicate and wrong mappings, preserves revision, then locks the correct mapping and gate | Observation | Direct | High | V1 |

## Basic data

- Release / origin: developed by Rundisc and published by Focus Entertainment
  in 2023.
- Platform or physical form: single-player digital exploration puzzle; an
  official opening demo is available from the Steam product page.
- Puzzle family: contextual language decipherment with notebook validation.
- Creator and primary sources:
  - **[P1]** [Official Steam page](https://store.steampowered.com/app/1931770/),
    for the five languages, observation loop, notebook and official demo.
  - **[P2]** [Rundisc creator interview](https://www.gamedeveloper.com/design/immersing-players-in-the-culture-of-a-people-with-language-puzzler-chants-of-sennaar),
    for annotations, recurring evidence and automatic translation.
  - **[P3]** [Rundisc developer clarification](https://steamcommunity.com/app/1931770/discussions/0/3825300093319506641/),
    for the first three words as the only forced early validation.
- Secondary sources:
  - **[S1]** [Neoseeker Abbey walkthrough](https://www.neoseeker.com/chants-of-sennaar/walkthrough/Abbey),
    for the opening page and valve sequence.
  - **[S2]** [TrueAchievements walkthrough](https://www.trueachievements.com/game/Chants-of-Sennaar/walkthrough/3),
    for independent sequence corroboration.
  - **[V1]** [`verify_chants_first_journal.py`](../../../scripts/verify_chants_first_journal.py),
    an independent bounded state model.

## Mechanical decomposition

### Action Genes

- `ACT-049` — toggle reachable world switch. The traveller sets each of six
  valves to the state specified by the interpreted instruction.
- `ACT-101` — record editable provisional glyph gloss. Each repeated glyph can
  carry a revisable hypothesis before confirmation.
- `ACT-102` — match discovered glyph to illustrated meaning slot. The player
  assigns all three glyph cards to the opening, closing and doorway pictures.

### System Behaviour Genes

- `SYS-134` — validate and canonicalise complete glyph page. Wrong mappings
  remain revisable; the correct bijection locks the three canonical meanings.
- Resolution order: expose glyph contexts; accept editable annotations;
  resolve valves; reveal the page; require three distinct assignments; reject
  or canonicalise; then release the onward progression gate.

### Constraint Genes

- `CON-154` — complete one-to-one glyph-to-meaning page mapping. All three
  slots and all three glyphs must participate exactly once.
- `CON-155` — first glyph-page validation gates onward traversal. Correct valve
  state alone does not bypass the forced confirmation.
- Scarce strategic resources: none; hypotheses and valve states are revisable.

### Information Genes

- `INF-051` — stable unknown glyph identity across contextual occurrences.
  Repetition lets lever, door and instruction contexts constrain one meaning.
- `INF-052` — persistent provisional glossary with illustrated validation cues.
  The notebook retains guesses and supplies the answer categories.
- `INF-050` does not transfer: one player can inspect world and notebook by
  switching interfaces; no second human role owns inaccessible rules.

### Objective Genes

- `OBJ-026` — reach designated traversable world location. Interpreting the
  instruction and clearing the notebook check make the next route usable.

### Time Genes

- `TIM-002` — self-paced sequential action. No deadline or autonomous update
  advances between annotations, matches, valve toggles or walking inputs.

## Reproducible transitions

| Before | Action | Deterministic resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| Recurring glyph beside operated lever | Annotate `open`, then revise | Provisional gloss remains attached to that glyph | editable contextual hypothesis | `COS-002`, `COS-006` |
| Six valves in arbitrary states | Set `O, O, C, O, C, O` | World mechanism reaches accepted state | meaning drives world control | `COS-004`, `COS-006` |
| Page lacks door assignment | Submit | Page rejects and remains editable | complete mapping | `COS-005`, `COS-006` |
| One glyph fills two slots | Submit | Page rejects before canonicalisation | one-to-one requirement | `COS-005`, `COS-006` |
| Open and closed are swapped | Submit | Page rejects and can be corrected | exact semantic validation | `COS-005`, `COS-006` |
| All three match pictures | Submit | Meanings lock as open, closed and door | canonicalisation | `COS-002`, `COS-005`, `COS-006` |
| Correct valves, unvalidated page | Continue | Progress remains blocked | forced knowledge gate | `COS-005`, `COS-006` |
| Correct valves and page | Walk onward | Traveller passes to next area | objective completion | `COS-005`, `COS-006` |

## Strategic and experiential structure

- Local decision: compare a glyph's present context against earlier
  occurrences rather than trust one appearance.
- Medium-term planning: retain tentative meanings, use the six-item instruction
  as a consistency test and revise before submitting the page.
- Long-term structure: outside this packet, confirmed vocabulary underpins
  later linguistic and social interpretation.
- Common heuristics: distinguish nouns from state words, seek repetitions and
  use illustrations to falsify a favourite guess.
- Failure attribution: rejected page composition stays visible and editable;
  duplicate, missing or swapped assignments can be isolated.
- Player-trust factors: one glyph identity must preserve one meaning,
  contextual repetitions must agree and the correct complete mapping must lock.

## Replay and variation

- The packet is authored: glyph identities, meanings, valve order and pictures
  do not randomise.
- Annotation wording and inference order vary between players.
- After validation there is little mechanical replay value inside this packet;
  replay chiefly revisits the inference path.

## Adjacent systems and history

- Return of the Obra Dinn and The Case of the Golden Idol externalise revisable
  hypotheses, but accepted entries reconstruct people and events rather than a
  reusable lexicon.
- Heaven's Vault is a close language-decipherment predecessor, but remains a
  future comparison rather than an unsupported transfer claim here.
- Keep Talking and Nobody Explodes separates state and procedure between human
  roles. Chants stores both in one player's world/notebook loop, so `INF-050`
  remains role-specific.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-049`, `ACT-101`, `ACT-102` | note wording; six valves |
| System Behaviour | `SYS-134` | page feedback; label replacement |
| Constraint | `CON-154`, `CON-155` | three slots; forced gate |
| Information | `INF-051`, `INF-052` | glyph identities; pictures |
| Objective | `OBJ-026` | next traversable gate |
| Time | `TIM-002` | no forced clock |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `100` (`GAME-0001`–`GAME-0100`).
- Exact genome matches: none.
- Tied near matches: `GAME-0040` — Carto (`2 / 16 = 0.125000`).
- Supported combination subsets: `COMB-0101`.
- Scan date: 2026-08-15.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| Carto (`GAME-0040`) | `OBJ-026`, `TIM-002` | map topology is directly rearranged from known fragments; Chants infers unknown semantics and validates a lexicon before operating fixed-world switches | Near, `0.125000` |

### Preserved research notes

- New genes: `ACT-101`, `ACT-102`, `SYS-134`, `CON-154`, `CON-155`,
  `INF-051`, `INF-052`.
- Classification result: `New gene` and `New combination of known and new genes`.
- Evidence and reasoning: note, validation and glyph-information boundaries are
  absent; world switch, traversal objective and self-paced timing transfer.

## Taxonomy impact

- Registry changes: seven Active IDs and three new evidence transfers.
- Taxonomy-change record: none; no boundary is merged or retired.
- Candidate terms affected: `INF-050` remains role-exclusive.

## Negative results

- `INF-050` rejected: one player owns both interfaces.
- `ACT-007` rejected: semantics are assigned to a glyph, not a board cell.
- `ACT-060` and `SYS-086` rejected: no phrase answer is assembled.

## Delta summary

## Нові факти

- [Confirmed | Corroborated | High] Перші три примусово підтверджувані значення
  — open, closed і door; правильна сторінка відкриває продовження
  (`COS-003`–`COS-005`).

## Нові гени

- [Observation | Corroborated | High] Додано сім генів для редагованих
  гіпотез, зіставлення, перевірки, knowledge gate і glyph information.

## Нові комбінації

- [Confirmed | Corroborated | High] `COMB-0101` — контекстно вивести й
  підтвердити малий словник через повну ілюстровану бієкцію.

## Зміни таксономії

- [Observation | Direct | High] Змін немає; негативний transfer-test зберіг
  межу `INF-050`.

## Нові питання

- Чи більші сторінки додають структуру, чи лише параметризують `CON-154`?

## Наступна рекомендована гра

- [Hypothesis | Limited | Medium] The Password Game.
- Optimisation criterion: cumulative live constraints over one mutable string.
- Expected information gain: distinguish rule accumulation from page validation.
- Backlog impact: retains Papers, Please and Heaven's Vault.

## Чому саме вона

- [Hypothesis | Limited | Medium] It moves from semantic inference to a visible
  dynamically expanding constraint set, maximising boundary contrast.
