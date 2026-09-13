# Taxonomy Change 050: Generalise the retained progression measure and its gate to any declared qualifying result

## Status

- Proposal status: `Accepted`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Date: 2026-09-09
- Trigger: Codex final acceptance audit of `GAME-0284` Cities: Skylines II,
  after Claude Opus corrective passes supplied a research candidate.

## Current classification

- Exact wording or stable IDs: `SYS-517` — Credit one retained progression
  measure from qualifying activity results, whose definition read "every
  completed result that a bounded ruleset declares eligible adds its configured
  amount to one retained progression measure, so different qualifying
  activities can substitute for one another on the way to a later gate"; and
  `CON-440` — A successor gate requires its accumulated progression threshold,
  whose definition read "an authored successor remains unavailable until
  qualifying completed work has accumulated the declared total in one retained
  progression measure".
- Files and entries affected: the System Behaviour and Constraint registries;
  the Ukrainian gene localisations for `SYS-517` and `CON-440`; the
  `GAME-0284` decomposition; `COMB-0269`; generated indexes and research
  artifacts.
- Original evidence or rationale: both genes were first isolated for
  `GAME-0171` Forza Horizon 6 and generalised for `GAME-0271` Far Cry 5 under
  [`TAXONOMY_CHANGE_033`](TAXONOMY_CHANGE_033.md). In both carriers every
  contribution to the measure is a completed player activity, so the wording
  named completed activity results as the eligible source.

## Detected problem

- What is incorrect, ambiguous or at the wrong type: Cities: Skylines II
  credits the same kind of measure from two declared sources. Paradox states
  that "Passive Expansion Points are awarded 16 times throughout an in-game day
  as a result of increases in both Population and Happiness, while active
  Expansion Points are granted immediately as a result of actions you take,
  such as placing or upgrading a service building, constructing a signature
  building, or expanding the city's road network." The active half is a
  completed activity result and already fits; the passive half credits a
  declared change in a quantity the ruleset already tracks, which the old
  wording cannot express. The decision the pair isolates — accumulate one
  substitutable measure until a declared threshold releases a successor — is
  unchanged.
- How the problem was found: the pass-02 reuse-first re-audit required by the
  corrective prompt, which asked whether a safe minimal generalisation of
  `SYS-517` covers Cities: Skylines II. The combination scan gave the same
  signal independently: `COMB-0269` missed being a strict proper subset of the
  pass-01 signature by `CON-440` alone.
- Why this changes decision structure rather than terminology or theme: in all
  three carriers the player chooses among substitutable ways of raising one
  number toward one disclosed gate. Whether a particular contribution is
  booked when an activity completes or when a tracked quantity rises only
  changes which actions are worth taking, not the structure of the decision.

## Evidence

- Primary sources: the Forza Horizon 6 and Far Cry 5 evidence already cited by
  `GAME-0171` and `GAME-0271`; for Cities: Skylines II, Paradox's official
  [Feature Highlight #10: Game Progression](https://www.paradoxinteractive.com/games/cities-skylines-ii/features/game-progression)
  for both award classes and the threshold (`Confirmed | Direct | High`), the
  publisher's dated `Hotfix 1.2.3f1` announcement of 2025-01-22 on its
  [official Steam announcement channel](https://store.steampowered.com/news/app/949230),
  confirming that Expansion Points remain a tracked quantity after Economy 2.0, and the community wiki's per-building `XP` column for the
  configured contribution of each placed service building
  (`Observation | Limited | Medium`).
- Reproducible transitions: the `GAME-0171` Qualifier rows, the `GAME-0271`
  liberation rows and the `GAME-0284` road-commit, facility-commit and
  periodic-award rows.
- Analysed games checked: `GAME-0171`, `GAME-0271` and `GAME-0284`. No other
  reviewed game carries `SYS-517` or `CON-440`.
- External systems or literature checked: none beyond the three carriers.
- Counterevidence: none. Forza Horizon 6 and Far Cry 5 remain true sentence by
  sentence, because a completed activity result is one kind of declared
  qualifying result, and neither carrier gains a source it does not have. The
  excludes lists are unchanged and still reject a score that changes no gate, an
  ordered mission chain with no shared measure, a personal experience pool spent
  on upgrades, a single-shape delivery quota, a mere disclosure, a
  named-mission gate, a personal-level threshold, a timed gate and a price paid
  from a spendable balance.

## Proposed change

- Old classification: a measure credited only by completed activity results,
  and a gate that reads only accumulated completed work.
- Proposed classification: `SYS-517` credits the measure from "every result
  that a bounded ruleset declares eligible — a completed activity, or a
  declared change in a quantity the ruleset already tracks"; `CON-440` reads
  "until qualifying results have accumulated the declared total".
- Definitions and boundaries: `SYS-517`'s label named the narrower source and
  is therefore renamed from `Credit one retained progression measure from
  qualifying activity results` to `Credit one retained progression measure from
  every declared qualifying result`, so that the canonical label carries the
  accepted state-change source rather than contradicting the widened
  definition. Its Ukrainian label is renamed in the same unit from
  `Зараховувати результати допустимих дій до однієї збереженої величини
  поступу` to `Зараховувати кожен допустимий результат до однієї збереженої
  величини поступу`. `CON-440`'s label is unchanged, because it names the
  threshold and the successor rather than the eligible source class. Both
  definitions and both includes lists change, and the includes lists gain the
  Cities: Skylines II instance. `INF-207` needs no change, because it already
  exposes "one retained progression measure, its required threshold and whether
  the corresponding authored successor is still locked or now available".
- Lifecycle effects: none.
- What does not change: the `GAME-0171` and `GAME-0271` signatures, the
  `COMB-0269` gene set, every earlier reviewed signature, every lifecycle state
  and every stable ID. The `SYS-517` rename replaces a label, not an
  identifier, so no carrier's signature membership moves; the renamed label
  propagates to every registry, localisation, game record, salience note, card,
  test and generated artifact that quotes it.

## Genome and combination impact

- Genes added, deprecated, merged or split: one deprecation. The pass-01
  proposal to create a separate new System gene for the Cities: Skylines II
  measure is withdrawn, because the generalised `SYS-517` owns that boundary
  and multiple producers of one measure are parameters rather than a separate
  rule. Its identifier `SYS-839` is registered `Deprecated` with no carrier, so
  that the pass-01 record stays readable and the identifier is never reused; no
  Active gene, carrier or signature depends on it.
- Games requiring annotation: `GAME-0284` reuses both generalised IDs;
  `GAME-0171` and `GAME-0271` remain carriers with their wording valid under
  the wider boundary and gain explicit support lines.
- Combinations affected: `COMB-0269` gains `GAME-0284` as a third supporting
  carrier. Its gene set `SYS-517 + CON-440 + INF-207` is unchanged and is a
  strict proper subset of the new sixteen-gene signature.
- Novelty claims affected: the `GAME-0171` first-isolation notes remain true.

## Decision

- Decision: `Accepted`.
- Decided by: Codex's complete carrier audit recorded in the `GAME-0284` record
  and final acceptance checkpoint, which restates each existing carrier's trigger,
  eligible sources, contribution, threshold, result and exclusions under the
  widened wording.
- Rationale: the boundary survives every carrier, the eligible-source list was
  already parameter-shaped in both genes' own parameter lists, and refusing the
  generalisation would have preserved a duplicate System whose only difference
  from `SYS-517` is that its definition hard-codes two producer classes.
- Implementation links: `SYS-517`, `CON-440`, `INF-207`, `COMB-0269`,
  `GAME-0171`, `GAME-0271`, `GAME-0284`, `TAXONOMY_CHANGE_033`,
  `TAXONOMY_CHANGE_048`, `TAXONOMY_CHANGE_049`.

## Ukrainian review

- `SYS-517` and `CON-440` receive corrected Ukrainian definitions and
  inclusions for the widened boundary in the same unit, under the range batch
  `UK-GAME-0171-0284`. `SYS-517` additionally receives the renamed Ukrainian
  label recorded above, because the old label named the narrower source;
  `CON-440`'s label is retained, because it names the threshold and the
  successor rather than the eligible source class.

## Change history

- 2026-09-09 — proposed during the Claude Opus corrective pass 02 for
  `GAME-0284`; not yet accepted at that stage.
- 2026-09-09 — corrected during the Claude Opus corrective pass 03 for
  `GAME-0284`, after Codex transfer audit 02 finding `P1-02`. The record had
  claimed that both labels were unchanged because neither named the narrower
  source. That was wrong for `SYS-517`, whose English and Ukrainian labels both
  named activity results. The disposition recorded above is now the actual one:
  `SYS-517` is renamed in both languages and the rename is propagated; the
  generalisation itself stands and is not withdrawn.
- 2026-09-09 — accepted by Codex after the final carrier audit under accepted
  selection amendment 001; Claude's passes remain research input, not the
  canonical acceptance authority.
