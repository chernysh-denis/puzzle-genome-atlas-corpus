---
game_id: GAME-0304
slug: azul
game_title: Azul
analysis_status: reviewed
reviewed: 2026-09-18
combination_ids: []
gene_ids:
  action:
    - ACT-464
    - ACT-465
  system:
    - SYS-004
    - SYS-880
    - SYS-881
    - SYS-882
    - SYS-883
    - SYS-884
    - SYS-885
    - SYS-886
  constraint:
    - CON-001
    - CON-640
    - CON-641
    - CON-642
    - CON-643
  information:
    - INF-001
    - INF-002
  objective:
    - OBJ-002
    - OBJ-177
  time:
    - TIM-004
    - TIM-024
---

# Game: Azul

Use the canonical [vocabulary, genome signature and comparison
rules](../../../docs/ARCHITECTURE.md#canonical-vocabulary). Product-specific
counts, colours and scoring values parameterise portable genes.

## Analysis scope

- Version / ruleset: the original physical **Azul** base set by Next Move
  Games, using the standard coloured side of two player boards and the
  publisher's current English base-game rulebook checked 2026-09-18. This is
  a two-player game with five factory displays, not a digital port, Azul Mini,
  gray-board variant or expansion. No manufacturing print run was inspected.
- Structured analysis target: `PLAT-PHYSICAL-TABLETOP`, original base game;
  the exact target is recorded in `knowledge/platforms/games.json`, not a
  claim that other releases have been audited.
- Primary decision loop: inspect five public factory offers, a common centre,
  both staged patterns and walls; on an alternating turn draft **all** tiles
  of one colour from **one** source; move factory leftovers to the centre;
  assign the batch to one eligible monochrome pattern line and send excess to
  the penalty floor. Repeat until all offers are empty. Simultaneously settle
  complete lines onto fixed-colour wall cells, score new orthogonal runs and
  floor penalties, then either end on a completed horizontal wall row or
  refill factories from the finite bag and recycled box lid. The first centre
  drafter takes the starting marker, a floor penalty and next-round lead.
- Entry: two empty standard walls and pattern/floor areas, 100 tiles (20 in
  each of five colours), five factory displays each drawn with four tiles, and
  the first-player marker at the centre. The booklet's Portugal-visit method
  chooses an initial starter; the local deterministic illustration sets A as
  starter without claiming a physical visit.
- Positive terminal: after wall-tiling, at least one player has a five-cell
  horizontal wall row. Settle floor penalties, award final +2 per complete
  row, +7 per complete column and +10 per complete colour, then compare scores.
  Higher score wins; equal scores compare completed horizontal rows; a
  remaining tie is shared. This is a competitive rather than solo solved
  configuration.
- Negative terminal: losing the final ranking, including the row-count
  tie-break. An illegal placement is rejected or spills to the floor under
  the documented rules; a failed draft is not a separate game-over state.
- Included: two-player setup, public factories and centre, batch drafting,
  one-line staging, fixed wall layout, adjacency scoring, floor slots, marker,
  refill/recycling, row-triggered end and complete final ranking.
- Excluded: 3–4-player factory counts, gray-side free-form wall variant,
  Azul Mini, expansions, replacement components, optional house rules,
  tournament clocks, digital adaptations, uncertain manufacturing changes and
  visual artwork exactness. They require separate bounded packets.
- Reproducible parameterisation: follow the linked English rulebook; use five
  four-tile displays and standard boards; record factory draws, source/colour,
  one chosen pattern line, floor, wall placement, scores and starter after
  each round until the first row completion. The checked local Python model
  uses seed 304 and a deterministic *example choice policy*, with full
  conservation assertions; its route is a simulation of rule consequences,
  **not a physically played game** or evidence that any particular random
  draw occurred in an actual Azul set.
- Potential later modules: 3–4-player supply geometry, gray-side arrangement,
  official Mini form and physical component/version parity.
- Direct-play status: no physical set or two-person session was available.
  Publisher rules and product description establish the packet; a local model
  exercises the stated rules but does not upgrade the evidence to direct play.
  No third-party audiovisual material was opened or analysed.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `AZU-001` | The original physical set supports 2–4 players and contains 100 tiles, four boards and nine factory displays | Confirmed | Direct | High | P1, P2 |
| `AZU-002` | Two players use five factories and four randomly drawn tiles per factory | Confirmed | Direct | High | P2 |
| `AZU-003` | A draft takes every tile of one colour from one factory or centre; factory leftovers move to the centre | Confirmed | Direct | High | P2 |
| `AZU-004` | One batch enters one eligible pattern line; rows hold 1–5 of one colour and cannot duplicate a colour already on that wall row | Confirmed | Direct | High | P2 |
| `AZU-005` | Excess/rejected tiles and the first-centre marker occupy penalty slots; the first centre drafter starts next round | Confirmed | Direct | High | P2 |
| `AZU-006` | Complete lines transfer one tile to a fixed wall cell; incomplete lines persist; other completed-line tiles go to the lid | Confirmed | Direct | High | P2 |
| `AZU-007` | Wall scoring counts connected horizontal and vertical runs, while seven floor slots debit 1/1/2/2/2/3/3 and never reduce a score below zero | Confirmed | Direct | High | P2 |
| `AZU-008` | Refill draws from a finite bag, recycles lid discards and permits partial displays if both supplies are short | Confirmed | Direct | High | P2 |
| `AZU-009` | A complete horizontal wall row ends the game after the round; +2/+7/+10 bonuses and score/row/shared-tie ranking then apply | Confirmed | Direct | High | P2 |
| `AZU-010` | The seed-304 local two-player model ends after five rounds at 64–52; this is a simulated illustration, not a physical observation | Observation | Direct | High | R1 |
| `AZU-011` | Physical play, print-run parity and reload-like state verification were not performed | Confirmed | Direct | High | R1 |

## Basic data

- Origin/form: Michael Kiesling's Azul, published by Next Move Games; original
  physical base-game boards, tiles, bag and factory displays.
- Mechanical families: matching and combination (`FAM-004`); spatial assembly
  and packing (`FAM-006`). The first captures source/colour grouping and the
  second captures capacity-limited staging and persistent wall geometry.
- **P1**, publisher [Azul product page](https://www.nextmove-games.com/en/azul/azul-game/),
  checked 2026-09-18, establishes physical identity and components.
- **P2**, publisher [English Azul base-game rules PDF](https://cdn.svc.asmodee.net/production-nextmove/uploads/sites/4/2024/06/EN-Azul-Rules-Next-Move-web.pdf),
  checked 2026-09-18, pp. 2–6, establishes every admitted rule and variant
  boundary. Locally reviewed six-page copy:
  `tmp/pdfs/azul-official-rules.pdf` (working evidence, not a corpus asset).
- **R1**, local [deterministic rulebook trace](../../../research/checkpoints/GAME_0304_RULEBOOK_TRACE.py),
  run 2026-09-18, verifies one possible complete route, 100-tile
  conservation and numerical settlement. It is not an independent rule source.

## Mechanical decomposition

### Actions

`ACT-464` owns a visible source-and-colour choice with forced batch size;
`ACT-465` owns the separate one-row-or-floor destination choice. A player
cannot take a handpicked number of tiles or distribute one draft across rows.

### System behaviours and constraints

`SYS-004` selects unseen bag draws. `SYS-880` spills factory leftovers;
`SYS-881` places one tile from each completed line; `SYS-882` scores the
resulting horizontal/vertical runs; `SYS-883` deducts floor costs; `SYS-884`
assigns the marker and next starter; `SYS-885` conserves and recycles tile
supply; `SYS-886` awards final geometric bonuses. `CON-001` captures fixed
addressed wall and staging slots. `CON-640` requires a monochrome staged row;
`CON-641` forbids restaging a wall row's existing colour; `CON-642` bounds
line capacities and overflow; `CON-643` checks the completed-row terminal.

### Information, objective and time

`INF-001` covers public offers, staged rows, walls, floor and score, not the
unseen bag order; `INF-002` captures the unpreviewed next draw. `OBJ-002`
captures accumulating score during the session; `OBJ-177` captures the final
competitive ranking. `TIM-004` gives exclusive alternating drafts, while
`TIM-024` gives the offer-exhaustion/round-settlement cycle.

## Reproducible transitions

| Before | Player action | Deterministic resolution | Claim |
|---|---|---|---|
| Factory has blue ×2, amber ×1, red ×1 | A drafts blue ×2 from that factory | Both blues leave; amber and red enter the centre; A chooses one legal line or floor for the batch | `AZU-003`, `AZU-004` |
| A's length-two line has one blue; corresponding blue wall cell empty | A stages a blue batch of three | One blue completes the line; two enter the floor. A cannot put the two excess tiles in another line | `AZU-004`, `AZU-005` |
| A first drafts from the centre and its marker remains there | A takes one colour | Marker enters A's next free floor slot and A leads next round, despite its current penalty | `AZU-005` |
| Offers are empty; A has a complete length-three blue line | Wall phase begins | One blue fills its fixed wall cell; the other two go to lid; the new tile scores its contiguous horizontal and vertical runs | `AZU-006`, `AZU-007` |
| Bag is empty but lid has discarded tiles | Refill next round | Lid tiles are shuffled into bag; already staged and walled tiles are not recycled | `AZU-008` |
| A finishes one five-cell wall row in wall phase | Finish round | Score floor, then +2/+7/+10 sets; compare scores, then completed rows on score tie | `AZU-009` |

The deterministic model yields five rounds and 54 player turns. Its wall-phase
running scores are A/B `2/3`, `16/8`, `26/16`, `40/29`, `60/50`;
terminal row counts are `2/1`; final bonuses `+4/+2` give `64/52` and A
wins. This is a reproducible *constructed example* under the official rules.
The trace draws all 100 tiles without needing lid recycling, so recycling is
established by P2, not falsely presented as exercised in this trace. A score
crossing both axes, a zero-clamped floor penalty, a partial-refill case and a
remaining shared tie are rulebook-defined edge cases; their occurrence is not
claimed for this seed.

## Strategic and experiential structure

The locally attractive colour is not just a gain: taking it changes a shared
centre offer, commits one staging line and may price unwanted tiles at the
floor. A complete line is only a future wall tile, and the wall's fixed colour
geometry determines both immediate run score and end-game sets. The first
centre draft trades a penalty for next-round initiative. With a rival's wall
visible, players can contest high-value batches or hurry the five-cell row
that ends the whole score race. Exact tile order and opponent choices matter;
no particular winning policy is inferred from the example model.

## Replay and variation

Factory fills, first centre timing, each player's row commitments and the
round that completes the first wall row vary. The finite bag/lid cycle bounds
the material supply, but future draws remain hidden until exposed. Replaying
can explore alternative staging and timing, not a new authored level.

## Adjacent systems and history

2048 also has a fixed tile field and numerical score, but its direction
command shifts all tiles and merges equal values; Azul drafts an entire colour
batch and scores a lasting wall. Qwirkle also scores line placement but freely
positions directly into a shared open table; Azul stages on private rows,
places only at fixed colour addresses and settles after public offers empty.
The gray-side Azul variant relaxes fixed wall-colour geometry and is excluded.

## Normalised genome

| Type | Active gene IDs | Parameters |
|---|---|---|
| Action | `ACT-464`, `ACT-465` | one visible batch, one staging line |
| System Behaviour | `SYS-004`, `SYS-880`–`SYS-886` | bag, offers, wall, scoring, marker, bonuses |
| Constraint | `CON-001`, `CON-640`–`CON-643` | addressed cells, staging legality, terminal row |
| Information | `INF-001`, `INF-002` | public current state, hidden next draw |
| Objective | `OBJ-002`, `OBJ-177` | accumulated points and winner ranking |
| Time | `TIM-004`, `TIM-024` | alternating drafts, delayed settlement |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `303` (`GAME-0001`–`GAME-0303`).
- Exact genome matches: none.
- Tied near matches: `GAME-0001` — 2048 (`5 / 30 = 0.166667`).
- Supported combination subsets: none.
- Scan date: 2026-09-18.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0001` — 2048 | `SYS-004`, `CON-001`, `INF-001`, `INF-002`, `OBJ-002` | Both have fixed addressed cells, visible current tiles, an unseen future random selection and an accumulating score. Azul instead forces a public full-colour draft between two opponents, stages one batch, delays wall placement to round settlement, scores orthogonal runs and ends on a completed row; 2048 moves all board tiles by a direction command and merges equal values. | Near, `5 / 30 = 0.166667` |

## Taxonomy impact

- New: `ACT-464`–`ACT-465`, `SYS-880`–`SYS-886`, `CON-640`–`CON-643`,
  `OBJ-177`, `TIM-024`. The six reused boundaries are `SYS-004`, `CON-001`,
  `INF-001`, `INF-002`, `OBJ-002` and `TIM-004`. Earlier signatures stay
  unchanged; no verified recurring combination is proposed without a second
  independently analysed supporter.

## Negative results

- Do not infer that the gray-side wall may be filled under coloured-side
  placement rules; they are different variants.
- Do not treat the generated seeded trace as a documented physical win or
  claim observed current printing, component condition or random draws.
- Reject generic tile merging and free board painting as Azul draft rules.

## Delta summary

## New facts

- [Confirmed | Direct | High] `AZU-001`–`AZU-009` define the physical base
  game's two-player draft, wall and terminal without extending other variants.
- [Observation | Direct | High] `AZU-010` is a checked simulated route only.

## New genes

- [Confirmed | Direct | High] Fifteen portable boundaries distinguish the
  public batch draft, delayed wall and score system from existing signatures.

## New combinations

- None; a single new game cannot by itself establish recurrence.

## Taxonomy changes

- No existing gene or earlier game signature is changed.

## Inferences

- Staging can trade immediate floor cost against a later higher-value wall
  geometry, but the source model does not establish an optimal policy.

## Open questions

- Directly verify the rulebook account with an original physical set and a
  recorded two-person game, including a lid recycle and an exact tie.

## Contradictions

- None found between the checked publisher product description and rulebook.

## New questions

- Does a separately evidenced later print run change any analysed component or
  coloured-board rule? No such change is inferred here.

## Next recommended game

- `GAME-0305` Sons Of The Forest, the next recorded selection-019 unit.

## Why this game

- It adds a physical, two-player public-draft and delayed-scoring structure to
  a corpus dominated by digital systems, under the amended platform allocation.

## Confidence and unresolved questions

- Publisher rules directly support the game mechanics and terminal; the
  complete local route is a transparent simulation, not direct physical play.
