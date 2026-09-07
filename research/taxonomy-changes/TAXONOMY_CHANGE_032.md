# Taxonomy Change 032: Remove the unevidenced CON-062 reuse from Kerbal Space Program

## Status

- Proposal status: `Accepted`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Date: 2026-09-07
- Trigger: finding `R-08` of
  [`BATCH_015_GENE_CORRECTION_FOLLOWUP_REVIEW_002`](../normalisation/BATCH_015_GENE_CORRECTION_FOLLOWUP_REVIEW_002.md),
  priority `P0`, following `A-02` of
  [`BATCH_015_GENE_AUDIT_001`](../normalisation/BATCH_015_GENE_AUDIT_001.md) and
  `R-03` of
  [`BATCH_015_GENE_CORRECTION_REVIEW_001`](../normalisation/BATCH_015_GENE_CORRECTION_REVIEW_001.md)
- Supersedes: the retention decided in commit `7d74ec0e`, which rested on
  classifying a community wiki tutorial as the product's own Game Manual.

## Current classification

- Exact wording or stable IDs: `CON-062` — Static facility-footprint placement
  compatibility. Its canonical record names Opus Magnum, Infinifactory, Factorio
  and Frostpunk in `Includes` and Bloons TD 6 and Kerbal Space Program in
  `Additional support`, but those are the cited evidence records, not the
  carrier set: twenty game signatures held the gene before this change and
  nineteen hold it after.
- Files and entries affected: the Constraint registry's `Additional support`
  line, Ukrainian gene localisation, the `GAME-0267` record and its signature,
  `COMB-0265`'s prose, gene salience, plain-language presentation, the generated
  indexes, the `GAME-0267` comparison artefacts and the web contract tests.
- Original evidence or rationale: the reuse was accepted with the record and
  re-verified twice, most recently on a passage attributed to the product's own
  manual.

## Detected problem

- What is incorrect: the packet has never evidenced the gene's boundary. The
  gene requires a placement refused when a declared static footprint overlaps an
  incompatible placed component, terrain locus or fixed port. For the declared
  stock assembly building, the record's support was, in turn: an inference from
  attachment topology (`A-02`), one player discussion thread (`R-03`), and then
  a wiki tutorial described as the product's manual (`R-08`).
- Why the last support fails: `Tutorial:Game Manual` is a user-editable article
  in the community wiki's `Tutorial:` namespace, last edited in 2016 and
  carrying that wiki's `Outdated` template. The official site links to the wiki
  as a community destination, which does not make its articles publisher
  documentation, and a page from that host is in the same corroborating family
  as `S2`–`S6` rather than independent of them.
- How the problem was found: independent review finding `R-08`.

## Evidence

- Primary sources: the `GAME-0267` claim ledger and the canonical `CON-062`,
  `ACT-028` and `CON-610` records.
- Search for publisher documentation, 2026-09-07: the publisher's own site links
  a wiki and a forum and hosts no downloadable PC manual; KSPedia ships inside
  the application and cannot be read without direct play, which this packet
  declares it did not conduct; no KSPedia export of publisher provenance is
  retrievable. `store.steampowered.com/manual/220200` exposes no manual.
- Publisher patch notes were retrieved in full and admitted as `KSP-016`: the
  `1.12.2` notes record "Fix parts being able to attach in construction mode
  when colliding with ground" and "Non-surface placeable items can no longer be
  dropped or placed while intersecting other parts". Both describe EVA
  construction mode, which this packet excludes, so they establish a
  differently scoped mechanic rather than the assembly building's rule.
- Direct verification: silent visual verification of the current unmodified
  Windows editor was not available in this environment, and no audio was ever
  played, heard or analysed.
- Counterevidence, and how it is handled: the mechanic very probably exists —
  two community sources describe it consistently. That is a reason to keep the
  research task open, not a reason for a canonical record to assert it. The
  corpus's evidence model does not admit a gene on player discussion plus an
  outdated wiki tutorial from a single family.

## Proposed change

- Old classification: `GAME-0267` reuses `CON-062`; `KSP-014` is graded
  `Corroborated` / `High` on a source called the product's manual.
- Proposed classification: `GAME-0267` carries no placement-legality Constraint.
  `KSP-014` states only what its sources support and is graded `Limited` /
  `Low`; `S8` is reclassified as a community wiki tutorial; `KSP-016` records
  the publisher patch-note evidence and its different scope.
- Lifecycle effects: none. `CON-062` stays `Active`, keeps its definition and
  its nineteen other carriers, and loses one `Additional support` clause.
- What does not change: `GAME-0265`'s reuse of `CON-062`, which rests on
  `BTD-005` and the record's own refusal transition; `ACT-028`, which continues
  to carry the assembly placement itself; `CON-610`, `COMB-0265`'s gene set, and
  every other signature in the corpus.

## Genome and combination impact

- Genes added, deprecated, merged or split: none. Totals stay at 2,387
  definitions, 2,342 `Active`, 43 `Merged` and 2 `Deprecated`. `CON-062` falls
  from twenty carriers to nineteen.
- Games requiring annotation: `GAME-0267` — front matter, claim ledger, sources,
  direct-play status, constraint prose, normalised genome, preserved notes,
  taxonomy impact, negative results and delta summary, plus its salience
  partition and plain-language cards.
- Combinations affected: `COMB-0265` keeps its ten genes and remains a strict
  proper subset of the now eleven-gene genome; only its prose about what remains
  outside the interaction changed.
- Novelty claims affected: none.
- Comparison impact: `GAME-0267`'s genome falls from twelve genes to eleven, so
  its `genome-jaccard-v1` scores are recomputed. The selected near neighbour
  stays `GAME-0112` Human: Fall Flat and its score moves from
  `2 / 18 = 0.111111` to `2 / 17 = 0.117647`.

## Decision

- Decision: `Accepted`.
- Decided by: review finding `R-08`, a documented search for publisher
  documentation, and the corpus's own evidence model.
- Rationale: a canonical record may not assert a rule it cannot source, and a
  community wiki page is not a manual however plausible its content. Removing
  the gene costs the packet nothing it evidenced.
- Implementation links: `CON-062`, `ACT-028`, `CON-610`, `GAME-0267`,
  `GAME-0265`, `COMB-0265`.

## Change history

- 2026-09-07 — created and accepted as unit 1 of batch-015 gene correction
  follow-up 002.

## Correction

- 2026-09-07 — this record originally described `CON-062` as carried by six
  games and falling to five. That was the set of games its canonical record
  *cites*, not the set whose signatures contain it. The gene is carried by
  twenty game signatures before this change and nineteen after; the decision,
  the removal and every other statement are unaffected. Found by the unit 2
  verification of follow-up 002, which recomputes carrier sets from the
  signatures rather than from the registry's prose.
