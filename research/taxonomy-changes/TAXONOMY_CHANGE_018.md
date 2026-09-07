# Taxonomy Change 018: Merge the earned driving burst into the stored vehicle reserve spend

## Status

- Proposal status: `Accepted`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Date: 2026-09-06
- Trigger: card `C-01` of
  [`FULL_TAXONOMY_DUPLICATE_AUDIT_001`](../normalisation/FULL_TAXONOMY_DUPLICATE_AUDIT_001.md),
  disposition `CONFIRMED`

## Current classification

- Exact wording or stable IDs: `ACT-309` — Spend stored boost for directed
  vehicle thrust; `ACT-357` — Spend an earned driving burst.
- Files and entries affected: Action registry, Ukrainian gene localisation,
  `GAME-0199` signature and prose, `COMB-0197`, the generated game and
  combination indexes, gene salience, plain-language presentation, stale
  rejection statements in `GAME-0208`, `GAME-0242` and `GAME-0244`, the
  candidate-term disposition, `GAME-0208`'s selected-neighbour comparison, the
  deterministic research artifacts and the web contract tests.
- Original evidence or rationale: `ACT-309` was isolated for `GAME-0177` Rocket
  League, where the reserve is collected from spatial pads. `ACT-357` was
  isolated for `GAME-0199` Need for Speed Unbound on the stated ground that
  "the reserve is earned by live driving technique rather than collected as a
  fixed world object".

## Detected problem

- What is incorrect: the two records describe one player command — activate a
  finite vehicle acceleration reserve to obtain directed thrust — and are
  separated only by the rule that fills the reserve. Filling is not part of the
  command, and the corpus already carries it as System Behaviour: `SYS-540`
  (spatial pad refill), `SYS-691` (ordinary gauge), `SYS-765`
  (manoeuvre-refilled gauge) and `SYS-641` (technique-earned burst). Encoding
  the fill rule a second time inside an Action ID duplicates a rule that is
  independently represented, which is the defect
  [`TAXONOMY_CHANGE_012`](TAXONOMY_CHANGE_012.md) merged.
- How the problem was found: the full taxonomy duplicate audit's mandatory
  control pair, confirmed by independent review.
- Why this changes decision structure rather than terminology: the player's
  decision in both records is when and how much of a finite reserve to spend.
  Neither record exposes a state transition the other lacks, so keeping two IDs
  asserts a decision difference that no carrier evidences.

## Evidence

- Primary sources: the reviewed `GAME-0177`, `GAME-0199`, `GAME-0208`,
  `GAME-0226`, `GAME-0235` and `GAME-0242` records and their source ledgers.
- Reproducible transitions: in every carrier the player activates, holds or
  releases the reserve; the system debits it and applies directed acceleration;
  releasing or exhausting it ends the effect. The transition is identical after
  the reserve's identity and cap are substituted.
- Analysed games checked: all five `ACT-309` carriers and the single `ACT-357`
  carrier, plus every Active Action gene in a fresh same-type transfer scan.
  Only `ACT-309`, `ACT-321` and `ACT-357` mention a vehicle together with a
  reserve, thrust or nitrous; `ACT-321` is fixed-wing piloting and does not
  spend a reserve. `ACT-229` was checked and rejected as a survivor: it is a
  protagonist's special combat or driving form, and `GAME-0226` already carries
  `ACT-229` and `ACT-309` together, which proves the corpus distinguishes them.
- External systems or literature checked: none required; the change narrows an
  abstraction to mechanics already evidenced in the accepted corpus.
- Counterevidence: `ACT-357`'s definition adds "activates some or all of it"
  and "short tactical acceleration increase". Both fail the two-way test.
  `ACT-309`'s "holds or releases" is already a duration-proportional partial
  spend, and its "thrust along the vehicle's facing in ground or aerial motion"
  is strictly broader than a short acceleration increase, so it cannot exclude
  the Unbound case.
- Stale justification, provable from Git history: at commit `83771a03`, which
  introduced `ACT-357`, `ACT-309`'s `Includes` named only Rocket League's
  pad-fed boost, but its *definition* never required a pad. The `GAME-0199`
  rejection therefore reasoned from a carrier parameter rather than from the
  gene boundary. At commit `49d40cbe` (`GAME-0208`), `ACT-309` was extended to
  "Need for Speed Payback conventional nitrous acceleration", a gauge-fed
  reserve, and three further non-pad carriers followed. The premise of the
  original split was removed by later corpus growth and was never revisited.

## Proposed change

- Old classification: two Action genes separated by the reserve's acquisition
  route.
- Proposed classification: one Action gene for spending a finite vehicle
  acceleration reserve, with the acquisition route as a parameter carried by
  the relevant System Behaviour gene.
- Definitions and boundaries: `ACT-309` becomes "Spend a finite vehicle reserve
  for directed acceleration" and states explicitly that the command does not
  own the rule by which the reserve is filled, capped or recovered. Its
  `Excludes` now names that System Behaviour and a protagonist's special form.
  Ground and aerial breadth is preserved verbatim.
- Lifecycle effects: `ACT-357` becomes `Merged` and is preserved as an
  auditable alias pointing to `ACT-309`. Its stable ID is never reused.
- What does not change: `SYS-641`, `SYS-691`, `SYS-765` and `SYS-540` are
  untouched and keep their distinct filling rules, including the standing
  `Excludes` between them. `SYS-641`'s compound structure remains an open,
  conditional audit finding and is out of scope here. `INF-255` keeps the Burst
  disclosure. No other game signature changes.

## Genome and combination impact

- Genes added, deprecated, merged or split: `ACT-357` merged into `ACT-309`.
  Active genes fall from 2,355 to 2,354; `Merged` records rise from 31 to 32;
  the 2,387 total definitions are unchanged because no ID is deleted.
- Games requiring annotation: `GAME-0199` (signature, decomposition, normalised
  genome, preserved notes, taxonomy impact and negative results); `GAME-0208`,
  `GAME-0242` and `GAME-0244` (stale statements that rejected `ACT-357`).
- Combinations affected: `COMB-0197` substitutes `ACT-309` for `ACT-357`. Its
  size stays at eighteen genes and it remains a strict proper subset of the
  twenty-four-gene `GAME-0199` genome. A global scan found no exact combination
  collision and no additional game whose genome now contains `COMB-0197`.
- Novelty claims affected: `ACT-309`'s novelty note records the generalisation.
  `GAME-0199` no longer claims `ACT-357` as a new gene; it now records five new
  genes and nineteen reused records.
- Comparison impact: `GAME-0208`'s selected near neighbour moves from
  `GAME-0171` Forza Horizon 6 (`12 / 35 = 0.342857`) to `GAME-0199` Need for
  Speed Unbound (`12 / 33 = 0.363636`), because the shared `ACT-309` raises the
  intersection. No exact genome match is created. The pre-existing
  `GAME-0009`/`GAME-0109` exact match is unrelated and unchanged.

## Decision

- Decision: `Accepted`.
- Decided by: confirmed audit card `C-01` plus a fresh unit-level two-way
  transfer test over all 438 Active Action genes.
- Rationale: the surviving Action accepts the same direct command from every
  carrier once the reserve's acquisition route is supplied as a parameter, and
  that route is already represented by type-correct System Behaviour genes.
- Implementation links: `ACT-309`, `ACT-357`, `GAME-0199`, `COMB-0197`,
  `SYS-641`, `SYS-691`, `SYS-765`, `SYS-540`.

## Change history

- 2026-09-06 — created and accepted as the first implementation unit of the
  confirmed taxonomy normalisation derived from
  `FULL_TAXONOMY_DUPLICATE_AUDIT_001`.
