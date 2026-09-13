# Taxonomy Change 049: Generalise the municipal milestone gate to any declared settlement progression measure

## Status

- Proposal status: `Rejected`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Date: 2026-09-09
- Trigger: Codex final acceptance audit of `GAME-0284` Cities: Skylines II,
  after Claude transfer passes supplied a research candidate.

## Current classification

- Exact wording or stable IDs: `CON-179` — Municipal tools and land purchases
  require population milestone, whose definition read "a declared service,
  zone, policy, finance option or additional map-area purchase cannot be used
  until the current city has reached its associated population milestone".
- Files and entries affected: the Constraint registry; the Ukrainian gene
  localisation for `CON-179`; the `GAME-0284` decomposition; generated indexes
  and research artifacts.
- Original evidence or rationale: the gene was first isolated for `GAME-0121`
  Cities: Skylines as the legality gate of its milestone-withheld catalogue and
  reused by `GAME-0132` Anno 1800 for its population-tier gates. Its
  parameters already listed the threshold schedule, affected catalogue entries
  and area-purchase count.

## Detected problem

- What is incorrect, ambiguous or at the wrong type: Cities: Skylines II
  withholds taxation, the City Budget and City Statistics panels, service
  budgets, map-tile purchase, four-lane roads, higher zone densities and every
  civic service other than electricity and water until the corresponding
  Expansion Point milestone settles. The legality test — a declared catalogue
  entry is illegal until the settlement's milestone is reached — is the test
  `CON-179` isolates; population is one carrier's measure.
- How the problem was found: the mandatory complete same-series delta of
  `GAME-0121` for `GAME-0284`, run gene by gene before any ID was allocated,
  paired with the milestone unlock table that dates each withheld entry.
- Why this changes decision structure rather than terminology or theme: in all
  three carriers the player must raise one settlement-wide quantity before a
  named command becomes legal, and the planning problem is identical whichever
  quantity that is.

## Evidence

- Primary sources: the Cities: Skylines and Anno 1800 evidence already cited
  by `GAME-0121` and `GAME-0132`; for Cities: Skylines II, Paradox's official
  Feature Highlight #10 statement that each milestone gives "access to new City
  Services, Policies, and Management Options" (`CS2-006a`,
  `Confirmed | Direct | High`) and the community wiki's per-milestone unlock
  table (`CS2-006b`, `CS2-006c`, `Observation | Limited | Medium`).
- Reproducible transitions: the `GAME-0121` locked-option row, the `GAME-0132`
  population-tier gates and the `GAME-0284` milestone settlement row, whose
  entire excluded catalogue is dated to the terminal milestone or later.
- Analysed games checked: `GAME-0121`, `GAME-0132` and `GAME-0284`. No other
  reviewed game carries `CON-179`.
- External systems or literature checked: none beyond the three carriers.
- Counterevidence: none. The two existing carriers remain true, because their
  population thresholds are one value of the widened measure, and the excludes
  list still separates an unlocked-but-unaffordable tool and a research-funded
  technology from a milestone gate.

## Proposed change

- Old classification: a catalogue entry illegal until the city reaches its
  associated population milestone.
- Proposed classification: `CON-179` — Municipal tools and land purchases
  require a progression milestone: a declared service, zone, policy, finance
  option or additional map-area purchase cannot be used until the settlement's
  declared progression measure has reached the milestone associated with it.
- Definitions and boundaries: the label is widened from `require population
  milestone`; the includes list names all three carriers' instances; the
  excludes list keeps insufficient treasury and research-funded technology and
  generalises the unrelated-scenario-flag exclusion to any flag unrelated to
  the settlement's progression measure; the parameters name the gating measure
  and generalise permanence after a fall in that measure.
- Lifecycle effects: none.
- What does not change: the `GAME-0121` and `GAME-0132` signatures, every
  earlier reviewed signature, every lifecycle state and every stable ID.

## Genome and combination impact

- Genes added, deprecated, merged or split: none by this record.
- Games requiring annotation: `GAME-0284` reuses the generalised ID;
  `GAME-0121` and `GAME-0132` remain carriers with their wording valid under
  the wider boundary and gain an explicit support line.
- Combinations affected: none. `CON-179` is not a member of `COMB-0117` or of
  any other verified combination set.
- Novelty claims affected: the `GAME-0121` first-isolation note remains true.

## Decision

- Decision: `Rejected` (corrective pass 02).
- Definitions and boundaries carrier audit: the generalisation was withdrawn
  because it created a duplicate boundary rather than closing a gap. Once
  `CON-179` is widened from a population milestone to any declared settlement
  progression measure, it states the same predicate as the Active lower-ID
  `CON-440` — an authored successor stays unavailable until qualifying results
  have accumulated the declared total in one retained progression measure —
  for exactly the carrier that motivated the widening. Pass 01 did not
  disposition `CON-440` at all.
- Decided by: Codex's reuse-first re-audit of the `GAME-0284` gate against
  every Active Constraint, prompted by the observation that `COMB-0269`
  (`SYS-517 + CON-440 + INF-207`) missed being a strict proper subset of the
  pass-01 signature by `CON-440` alone.
- Rationale: `CON-179` keeps its committed population wording and its two
  existing carriers, `GAME-0121` and `GAME-0132`, whose gates really are
  population thresholds rather than accumulated qualifying results.
  `GAME-0284` instead reuses `CON-440`, whose measure is credited by the
  generalised `SYS-517` and disclosed by `INF-207`, so the sequel joins the
  existing progression corridor and `COMB-0269` becomes a strict proper subset
  with a third carrier. `CON-179` is byte-identical to `HEAD` again and
  `GAME-0284` does not carry it. No committed wording, carrier, lifecycle or
  ID changed.
- Implementation links: `CON-179`, `CON-440`, `COMB-0269`, `GAME-0121`,
  `GAME-0132`, `GAME-0284`, `TAXONOMY_CHANGE_048`, `TAXONOMY_CHANGE_050`.
- Superseded pass-01 rationale (history only): the proposal argued that the
  municipal milestone gate stayed true with the measure as a parameter value.
  That is true in isolation but redundant, because the corpus already owns the
  measure-generic gate as `CON-440`; the reasoning is withdrawn.

## Ukrainian review

- The pass-01 draft that gave `CON-179` corrected Ukrainian wording for the
  widened boundary under the range batch `UK-GAME-0121-0284` was withdrawn
  with this rejection: the committed Ukrainian entry (`UK-GAME-0121-0121`) is
  restored byte-for-byte and remains unchanged.

## Change history

- 2026-09-09 — proposed during the Claude transfer-test initial pass for
  `GAME-0284`; not yet accepted at that stage.
- 2026-09-09 — corrective pass 02: rejected. The widened gate duplicated the
  Active lower-ID `CON-440`, which `GAME-0284` now reuses. `CON-179` and its
  Ukrainian entry are restored to their committed wording and `GAME-0284` does
  not carry it.
- 2026-09-09 — rejection confirmed by Codex during final acceptance under
  selection amendment 001.
