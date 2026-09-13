# Taxonomy Change 042: Generalise typed special-item slots to declared counts per class

## Status

- Proposal status: `Accepted`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Date: 2026-09-08
- Trigger: Claude transfer-test corrective pass 02 for `GAME-0282` Dead
  Cells, resolving finding `P1-01` of
  `research/checkpoints/GAME_0282_CODEX_TRANSFER_AUDIT_01.md`, under the
  authority granted by `docs/CLAUDE_GAME_ANALYST_QUALITY_PROTOCOL_V2.md`.

## Current classification

- Exact wording or stable IDs: `CON-404` — Special carried items occupy
  bounded typed slots, whose definition read "the current character can
  normally carry at most one active item, one trinket and one pocket card,
  rune or pill; accepting another member of a full typed slot requires
  leaving or replacing the prior occupant".
- Files and entries affected: the Constraint registry; the Ukrainian gene
  localisation for `CON-404`; the draft `GAME-0282` decomposition; generated
  indexes and research artifacts.
- Original evidence or rationale: the gene was first isolated for `GAME-0164`
  The Binding of Isaac: Rebirth, whose clean-save character holds one active
  item, one trinket and one pocket item. The wording encoded that carrier's
  slot classes and counts as the boundary, although its parameters already
  listed slot type, capacity, occupant, replacement and drop eligibility.

## Detected problem

- What is incorrect, ambiguous or at the wrong type: the draft `GAME-0282`
  unit allocated `CON-623` for a loadout of two weapon slots, two skill
  slots and one amulet slot with forced replacement, without testing the
  lower-ID `CON-404`. The Dead Cells decision — a pickup whose class is full
  can only replace a held occupant — is the same decision as Isaac's, and
  the counts and classes are parameters. Under the old wording a second
  carrier of the same mechanism needed a duplicate gene.
- How the problem was found: the Codex transfer audit 01 (`P1-01`), then the
  corrective pass's ID-by-ID comparison of the draft with `CON-404`,
  `CON-284`, `CON-485`, `CON-353` and `CON-210`.
- Why this changes decision structure rather than terminology or theme: in
  both carriers the player's decision when a full typed slot meets another
  item is which occupant to keep; the number of slots per class and the
  item classes only size that decision.

## Evidence

- Primary sources: the Isaac evidence already cited by `GAME-0164`; for Dead
  Cells, the official wiki's Gear, Rusty Sword, Beginner's Bow and Old Wooden
  Shield pages (`DC-006b`, `Limited | Medium`) for the two weapon slots, the
  starter slot restriction and the replacement on pickup, and Motion Twin's
  2020-12-21 Update 21 announcement for the two weapon slots and the backpack
  as a later meta upgrade (`DC-006a`, `Corroborated | Medium`). The packet
  exercises only the weapon-class pair: a fresh profile has no skill or
  amulet before the terminal, so the skill and amulet counts are recorded
  as parameters and are not asserted as exercised; the two-handed occupant
  and the keep-or-drop menu on a third skill are product facts outside the
  packet and enter no parameter of this boundary.
- Reproducible transitions: the `GAME-0164` pedestal-replacement rows and the
  `GAME-0282` rows for taking a starter item and for a sampled chest or shop
  weapon meeting two held weapons.
- Analysed games checked: `GAME-0164` and `GAME-0282`; `GAME-0281` keeps
  `CON-284`-style capacity out of scope; no other carrier of `CON-404`
  exists.
- External systems or literature checked: none beyond the two carriers; no
  third carrier is asserted.
- Counterevidence: Isaac holds one item per class and drops the replaced
  item on the pedestal; Dead Cells holds two per weapon class and offers a
  keep-or-drop menu. Both are recorded as the capacity and replacement
  parameters.

## Proposed change

- Old classification: at most one active item, one trinket and one pocket
  card, rune or pill.
- Proposed classification: `CON-404` — the current character carries at
  most a declared small count of items in each typed special-item slot
  class; accepting another member of a full typed slot requires leaving or
  replacing the prior occupant.
- Definitions and boundaries: label unchanged; the includes list names both
  carriers' instances; the excludes list gains bulk or weight capacity
  (`CON-284`) and a storage upgrade bought after the scoped run; the
  parameter list is unchanged, because no admitted carrier exercises a
  multi-slot occupant inside its scoped packet.
- Lifecycle effects: none. The uncommitted draft `CON-623` of pass 01 is
  withdrawn before any commit, so no ID is deprecated or merged; the ID
  `CON-623` is reallocated within the same unstaged unit.
- What does not change: the `GAME-0164` signature, every earlier reviewed
  signature, every lifecycle state and every stable committed ID.

## Genome and combination impact

- Genes added, deprecated, merged or split: none by this record; `GAME-0282`
  separately adds new genes whose boundaries this record does not touch.
- Games requiring annotation: `GAME-0282` reuses the generalised ID;
  `GAME-0164` remains a carrier with its wording valid under the wider
  boundary.
- Combinations affected: `COMB-0162` keeps the same gene set and its sole
  carrier `GAME-0164`; `GAME-0282` is not a superset of it.
- Novelty claims affected: the `GAME-0164` novelty note remains true; the
  first isolation is unchanged.

## Decision

- Decision: `Accepted`.
- Definitions and boundaries carrier audit: for Isaac the slot classes
  (active, trinket, pocket), the counts (one each), the trigger (another
  member of a full class is accepted) and the resolution (leave or replace
  the prior occupant) remain true sentence by sentence under the new
  wording. For Dead Cells the weapon class holds two, the trigger and the
  resolution are the same, and the replacement is chosen in a menu.
- Decided by: the reuse-first comparison recorded in the `GAME-0282` record
  and corrective-pass checkpoint.
- Rationale: substituting "two weapons, menu choice" for "one active item,
  pedestal swap" in either direction leaves the trigger and the resolution
  unchanged; counts, classes and the replacement form are parameters.
- Implementation links: `CON-404`, `GAME-0164`, `GAME-0282`.

## Ukrainian review

- `CON-404` receives a corrected Ukrainian definition, inclusion and
  exclusion for the widened boundary in the same unit; the `GAME-0164`
  plain-language card keeps its Isaac instance.

## Change history

- 2026-09-08 — created and accepted during Claude transfer-test corrective
  pass 02 for `GAME-0282`, before that draft's next independent audit.
- 2026-09-08 — corrective pass 03: the `multi-slot occupants` parameter was
  removed after Codex audit 02 (`P2-03`), because neither admitted carrier
  exercises it inside its scoped packet; boundary and decision unchanged.
