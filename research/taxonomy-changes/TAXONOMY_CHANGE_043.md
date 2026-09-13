# Taxonomy Change 043: Generalise the aimed strike target to eligible breakable world objects

## Status

- Proposal status: `Accepted`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Date: 2026-09-08
- Trigger: Claude transfer-test corrective pass 03 for `GAME-0282` Dead
  Cells, resolving finding `P1-01` of
  `research/checkpoints/GAME_0282_CODEX_TRANSFER_AUDIT_02.md`, under the
  authority granted by `docs/CLAUDE_GAME_ANALYST_QUALITY_PROTOCOL_V2.md`.

## Current classification

- Exact wording or stable IDs: `ACT-161` — Aim and strike a reachable
  hostile with the current tool, whose definition read "the player aims an
  equipped melee or ranged combat tool at one reachable hostile and commits
  a direct strike or shot rather than assigning an autonomous squad or
  selecting an abstract card target".
- Files and entries affected: the Action registry; the Ukrainian gene
  localisation for `ACT-161`; the draft `GAME-0282` decomposition; generated
  indexes and research artifacts.
- Original evidence or rationale: the gene was first isolated for Minecraft
  and its carriers strike hostiles. The `GAME-0239` Half-Life (1998) carrier
  already maps the crowbar strike on route glass (`HL1-010`, transition row
  "Aim and strike until its threshold is crossed") to `ACT-161`, with the
  pane's durability and removal typed under `SYS-755`; the registry wording
  was narrower than that admitted use.

## Detected problem

- What is incorrect, ambiguous or at the wrong type: the Dead Cells packet
  contains an ordinary branch in which the player strikes the barred
  Collector's room door with the equipped weapon until it breaks. The
  destruction resolution is the lower-ID `SYS-755`; the player's command is
  an aimed, directly committed weapon strike, which is `ACT-161`'s decision,
  but the definition named only a hostile target. Under the old wording a
  second carrier of the same command against an object would need either a
  duplicate Action or a silent parameter stretch.
- How the problem was found: Codex transfer audit 02 (`P1-01`), then the
  corrective pass's command/restriction/resolution mapping of the door
  branch against `ACT-161`, `ACT-341` (which excludes an ordinary weapon
  attack), `ACT-391` (a reward object) and `SYS-755`.
- Why this changes decision structure rather than terminology or theme: the
  player's decision is the same — aim the current combat tool at one
  reachable target and commit the strike — whether the target is a hostile
  or a breakable object; the target class only selects which System resolves
  the hit (`SYS-215` for hostiles, `SYS-755` for objects).

## Evidence

- Primary sources: the ninety existing carriers' hostile-target
  evidence, unchanged; for Half-Life, `HL1-010` (`Confirmed | Direct |
  High`); for Dead Cells, the official wiki's Currency page ("can actually
  be broken") and the 2021-01-25 Steam thread on breaking the door before
  spending cells (`DC-020g`, `Corroborated | Medium`).
- Reproducible transitions: the Half-Life glass row and the `GAME-0282` row
  "Cells are still carried at the room's exit — strike the door until it
  breaks, or invest the rest".
- Analysed games checked: every `ACT-161` carrier keeps a hostile-target
  instance; the widened target class adds no requirement to any of them and
  removes none. `GAME-0239` gains explicit registry coverage for a use its
  record already made. No third object-target carrier is asserted.
- External systems or literature checked: none beyond the carriers.
- Counterevidence: none; a strike at an object that is not eligible for
  `SYS-755` remains outside the boundary because no resolution follows.

## Proposed change

- Old classification: target restricted to one reachable hostile.
- Proposed classification: `ACT-161` — Aim and strike a reachable hostile
  or breakable world object with the current tool; the player aims an
  equipped melee or ranged combat tool at one reachable hostile or one
  eligible breakable world object and commits a direct strike or shot rather
  than assigning an autonomous squad or selecting an abstract card target.
- Definitions and boundaries: the canonical label is widened from `Aim and
  strike a reachable hostile with the current tool` to `Aim and strike a
  reachable hostile or breakable world object with the current tool`, so the
  label states the same target class as the definition; the Ukrainian label
  `Прицілитися й атакувати досяжну ціль поточною зброєю` already covers that
  class and is unchanged; the includes list gains the
  Half-Life crowbar strikes on route glass and the Dead Cells door strikes;
  the excludes list gains the contextual fixture interaction (`ACT-341`)
  and the object's durability and removal (`SYS-755`); parameters gain the
  target class.
- Lifecycle effects: none.
- What does not change: every carrier's signature, every earlier reviewed
  signature, every lifecycle state and every stable ID.

## Genome and combination impact

- Genes added, deprecated, merged or split: none by this record.
- Games requiring annotation: `GAME-0282` reuses the generalised ID for the
  door strike beside its hostile strikes; `GAME-0239` remains a carrier with
  its glass row now covered by the registry wording.
- Combinations affected: none; no combination gene set changes and no
  carrier is added or removed.
- Novelty claims affected: none.

## Decision

- Decision: `Accepted`.
- Definitions and boundaries carrier audit: for every existing carrier the
  trigger (an equipped combat tool aimed at one reachable target), the
  operation (a direct strike or shot committed by the player) and the
  exclusions (autonomous squads, ability cards, group waypoints) remain true
  sentence by sentence; the target class of each existing instance is
  `hostile`. For Half-Life and Dead Cells the same command is committed
  with target class `breakable object`, and the resolution is `SYS-755`.
- Decided by: the command/restriction/resolution mapping recorded in the
  `GAME-0282` record and corrective-pass checkpoint.
- Rationale: substituting a breakable pane or door for a hostile leaves the
  aimed, directly committed strike unchanged; only the resolving System
  differs, and that is already typed separately. The label is a separate
  contract from the definition: a label that still named only a hostile
  would contradict the widened boundary, so it is widened with it.
- Implementation links: `ACT-161`, `SYS-755`, `GAME-0239`, `GAME-0282`.

## Ukrainian review

- `ACT-161` receives a corrected Ukrainian definition, inclusion and
  exclusion for the widened target class in the same unit, under the range
  batch `UK-GAME-0129-0282`.

## Change history

- 2026-09-08 — created and accepted during Claude transfer-test corrective
  pass 03 for `GAME-0282`, before that draft's next independent audit. That
  pass widened the definition but left the canonical English label at the
  hostile-only wording and recorded `label unchanged`.
- 2026-09-08 — corrective pass 04, after Codex audit 03 (`P1-01`): the
  canonical English label is widened to the definition's complete target
  class, the proposed-classification and boundary bullets above record that
  correction, and the web contract asserts the parsed label and definition
  together. No signature, ID, lifecycle or Ukrainian meaning changes.
