# Taxonomy Change 057: Separate team coordination from automatic substitution

## Status

- Proposal status: `Accepted`
- Claim status: `Confirmed`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Date: 2026-09-10
- Trigger: card `C-01` of
  [`BATCH_017_FULL_TAXONOMY_AUDIT_001`](../normalisation/BATCH_017_FULL_TAXONOMY_AUDIT_001.md).
- Scope: `SYS-459`, `SYS-759`, one extracted System gene, `GAME-0241` and
  `COMB-0239`; the other two existing `SYS-459` carriers keep their signatures.

## Current classification

- `SYS-459` coordinates off-ball football roles under team AI and is carried by
  `GAME-0163` EA SPORTS FC 26 and `GAME-0175` Football Manager 26.
- `SYS-759` coordinates non-controlled basketball roles under team AI and is
  carried only by `GAME-0241` NBA 2K26.
- The two records share the same continuous state transition: non-controlled
  participants on both sides are repositioned and routed from role or
  formation, possession, shared-ball location, marking and available space.
- `SYS-759` also admits "automatic line-up rotation", which is not continuous
  spatial coordination. It replaces one active participant with a reserve at a
  legal stoppage and therefore needs its own System boundary.

## Evidence and boundary test

- EA SPORTS FC 26 and Football Manager 26 establish the football carriers of
  continuous team-role coordination in their reviewed decompositions.
- The official [NBA 2K26 gameplay Courtside
  Report](https://nba.2k.com/2k26/courtside-report/gameplay/) describes adaptive
  offensive AI, off-ball positioning, help defence, screen navigation and
  transition behaviour. Those clauses transfer directly into `SYS-459` when
  sport, side size, surface and role vocabulary are parameters.
- The current written [NBA 2K26 Coach Settings
  trace](https://www.magicgameworld.com/nba-2k26-how-to-change-substitution-settings-automatic-manual-sub-method-guide/),
  accessed 2026-09-10, separately exposes automatic versus manual substitution
  and rotation logic based on playing time and fatigue.
- Official [NBA Rule
  3](https://official.nba.com/rule-no-3-players-substitutes-and-coaches/)
  establishes five active players, reserve eligibility, outgoing-player
  replacement and the stoppages at which a substitute can enter. It supplies
  the represented law, while the current secondary game trace supplies the
  NBA 2K26 automation setting.

The two-way transfer test passes for the shared core:

1. Every `SYS-459` carrier continuously routes non-controlled members of both
   sides around a live shared ball under role, possession, marking and space.
2. NBA 2K26 does the same with court roles, spacing, screens and help defence.
3. Removing sport nouns changes no player decision, legality predicate or
   state transition.
4. Automatic substitution does not transfer to the football carrier boundary
   and can occur independently of the current spatial coordination state.

## Decision

- Generalise `SYS-459` to **Coordinate non-controlled team roles under live
  AI**. Sport, ruleset, side size, playing surface, formation or role, shared-
  object location, spacing, screening and tactical policy are parameters.
- Change `SYS-759` to `Merged` and point it to `SYS-459`. The stable ID remains
  as a historical alias and may not enter a new signature.
- Add `SYS-850` — **Replace an active team member through automatic coaching**.
  It owns the discrete system transition from one legal active line-up to
  another while preserving active-member capacity.
- Keep player-confirmed live managerial changes outside `SYS-850`; those are
  intentional Action mechanics. Keep pre-match line-up selection, direct-
  control switching, continuous off-ball positioning and persistent roster
  construction outside it as well.

## Genome and combination impact

- `GAME-0241` replaces `SYS-759` with `SYS-459` and adds `SYS-850`; its genome
  grows from 25 to 26 Active genes.
- The current decomposition is 19 game-introduced Active genes plus seven
  reused genes. `SYS-759` is no longer counted as Active or as a current
  game-introduced gene.
- `GAME-0163` and `GAME-0175` retain the same stable `SYS-459` ID and therefore
  require no signature edit.
- `COMB-0239` replaces `SYS-759` with `SYS-459` and remains a strict 21-gene
  subset. `SYS-850` stays outside the distinctive possession-loop core because
  the bounded match still has the same causal possession pattern when a
  particular legal stoppage triggers no substitution.
- A global supporter recomputation is required after migration. No new
  combination is introduced by this decision.
- `GAME-0241` keeps `GAME-0163` as its selected neighbour. Their shared set
  rises from six to seven genes, and the score changes from `6 / 39 = 0.153846`
  to `7 / 39 = 0.179487`; the union remains 39 because the extracted `SYS-850`
  offsets the merged duplicate.

## Corpus accounting

- Canonical definitions: 2,452 → 2,453.
- Active definitions: 2,400 → 2,400.
- Inactive definitions: 52 → 53.
- System definitions: 849 → 850; Active Systems remain 831.
- Games, combinations and families remain 288, 274 and 17.
- Earlier reviewed signatures changed: `0`; only the direct owner `GAME-0241`
  is migrated.

## Localisation disposition

- `SYS-459`: `corrected` — the Ukrainian label and boundary become sport-
  neutral and add NBA 2K26 as a carrier.
- `SYS-759`: removed from the current Ukrainian Active registry because it is
  now a lifecycle alias.
- `SYS-850`: `corrected` — a new reviewed Ukrainian boundary for automatic
  personnel replacement.
- All other `GAME-0241` translations: `verified`; product names, mode names,
  team names, stable IDs and setting labels remain `retained-with-reason`.

## Rejection condition

Reopen the merge only if a later carrier demonstrates that continuous live
coordination has a distinct operation, predicate or settlement that cannot be
expressed through sport, side, surface, role, formation, possession, spacing,
screening or tactical-policy parameters. Reopen `SYS-850` only if automatic
personnel replacement proves to be a player commitment rather than a system
transition, or if its alleged carrier cannot be reproduced under the declared
NBA 2K26 automatic-substitution setting.

## Change history

- 2026-09-10 — accepted as `BATCH_017_TAXONOMY_CORRECTION_001` after the full
  Batch 017 candidate audit and a fresh source and carrier review.
