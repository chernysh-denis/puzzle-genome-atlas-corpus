# Taxonomy Change 025: Subsume three product-specific crafting-legality constraints into CON-297

## Status

- Proposal status: `Accepted`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Date: 2026-09-06
- Trigger: card `C-13` of
  [`FULL_TAXONOMY_DUPLICATE_AUDIT_001`](../normalisation/FULL_TAXONOMY_DUPLICATE_AUDIT_001.md),
  disposition `CONFIRMED`, routed as implementation target `T-07`

## Current classification

- Exact wording or stable IDs: `CON-297` — Crafting requires ingredients,
  knowledge and station context; `CON-320` — Workshop output requires station,
  recipe and retained ingredients; `CON-366` — Crafting requires recipe inputs
  and reachable station context; `CON-462` — Crafting requires recipe,
  ingredients, capacity and station.
- Files and entries affected: the Constraint registry, Ukrainian gene
  localisation, the `GAME-0143`, `GAME-0153`, `GAME-0178` and `GAME-0186`
  signatures and prose, `COMB-0141`, `COMB-0151`, `COMB-0176`, `COMB-0184`, the
  generated game and combination indexes, gene salience, plain-language
  presentation, the deterministic research artifacts and the web contract tests.
- Original evidence or rationale: `CON-297` was isolated for `GAME-0141` Rust
  and reused by six later games. The three specific records were each isolated
  in their own game unit — `CON-320` for `GAME-0143` ARC Raiders, `CON-366` for
  `GAME-0153` Terraria and reused by `GAME-0186` Don't Starve Together, and
  `CON-462` for `GAME-0178` Subnautica.

## Detected problem

- What is incorrect: this is a subsumption rather than a pairwise duplicate.
  Every clause of the three specific records is already inside `CON-297`, whose
  definition covers ingredient ownership, recipe knowledge, "every station tier,
  proximity or operating condition required by that recipe" and output capacity,
  and which explicitly admits that "a recipe may declare no station requirement".
  - `CON-320` = unlocked station and tier + known recipe + ingredients in
    persistent inventory. "Persistent inventory" is the ingredient-source
    parameter.
  - `CON-366` = input quantities available in carried, opened or nearby
    inventory + within range of every required station or environmental source.
    Source priority and "environmental source" are parameters.
  - `CON-462` = recipe known + ingredients + station can operate + output
    collectable. Almost verbatim inside `CON-297`, including the operating
    condition and the output-capacity clause.
- How the problem was found: the full taxonomy duplicate audit, card `C-13`,
  confirmed by independent review.
- Why this changes decision structure rather than terminology: none of the
  residual distinctions changes what the player may do, when, with what
  information, or how the request is settled. Where ingredients may come from,
  what class or tier of station is needed, whether it needs power, reach or an
  operating state, and whether a station is required at all are all values the
  same legality predicate takes.

## Evidence

- Primary sources: the reviewed `GAME-0141`, `GAME-0143`, `GAME-0153`,
  `GAME-0178`, `GAME-0186`, `GAME-0197`, `GAME-0229`, `GAME-0233`, `GAME-0240`,
  `GAME-0257` and `GAME-0261` records.
- Reproducible transitions: in all eleven packets a craft request is refused
  when the recipe is unknown, when a required ingredient quantity is not
  available from an admitted source, when a declared station condition is
  unsatisfied, or when the output cannot be received; and is accepted when all
  four hold.
- Analysed games checked: a fresh unit-level scan over all 606 Active Constraint
  genes. `CON-297` is the nearest Constraint to `CON-320` at 0.208 and to
  `CON-462` at 0.192. **It is not the nearest to `CON-366`**, which ranks
  `CON-207` first at 0.203 and `CON-297` only fourth at 0.136. That is recorded
  here rather than smoothed over: `CON-366`'s wording shares vocabulary with
  Minecraft's spatial-grid record, which `CON-366` itself explicitly excludes.
  The subsumption argument for `CON-366` is therefore clause containment, not
  lexical proximity, and the survivor now inherits the spatial-arrangement
  exclusion that made `CON-366` distinct from `CON-207`.
- Counterevidence, and how it is handled:
  - **`CON-310` remains distinct, as the audit required.** Project Zomboid's
    record additionally requires a character skill level, a specific tool and a
    compatible construction placement state; it therefore admits construction
    requests that this crafting predicate does not describe and refuses crafting
    requests that satisfy every clause of `CON-297`. It is named in the
    survivor's `Excludes`, `GAME-0142` is unchanged, and the
    `REGISTRY_NORMALISATION` decision that retained the `CON-297`/`CON-310`
    split stands.
  - `CON-207` (spatial ingredient arrangement is itself the recipe), `CON-172`
    (an autonomous entity's continuous production state), `CON-498` (a
    science-tier proximity requirement that lapses after a personal prototype)
    and `CON-581` (an output grade determined by retained process history) are
    all real siblings and are now named in the survivor's `Excludes`. None is
    touched. `CON-498` and `CON-297` continue to co-occur in `GAME-0186`, which
    is the clearest demonstration that they are different rules.
  - `CON-320`'s `Excludes` named "Field Crafting recipes that need no Workshop
    station". That contradicted `CON-297`'s explicit admission of stationless
    recipes; the conflict is removed rather than inherited.
- External systems or literature checked: none beyond the products' own
  published material.

## Proposed change

- Old classification: one broad Constraint plus three product-specific
  narrowings of it.
- Proposed classification: one Constraint for crafting legality, carrying the
  ingredient source, station class and output capacity as parameters.
- Definitions and boundaries: `CON-297` becomes "Crafting requires a known
  recipe, sourced ingredients, station context and output capacity". Recipe or
  blueprint knowledge, ingredients and quantities, the admitted ingredient
  sources and their priority, station class, tier, proximity or reach,
  environmental source, power and operating state, whether a station is declared
  at all, queue, output, output capacity or footprint and blocked feedback are
  parameters.
- Lifecycle effects: `CON-320`, `CON-366` and `CON-462` become `Merged` aliases
  pointing to `CON-297`. None of the three stable IDs is ever reused.
- What does not change: `CON-310`, `CON-207`, `CON-172`, `CON-498` and `CON-581`
  keep their boundaries and lifecycles. The `GAME-0141`, `GAME-0142`,
  `GAME-0197`, `GAME-0229`, `GAME-0233`, `GAME-0240`, `GAME-0257` and
  `GAME-0261` signatures are unchanged. Each carrier's product-specific
  ingredient-source and station detail is preserved in that game's own record
  rather than in the gene.

## Genome and combination impact

- Genes added, deprecated, merged or split: three Constraints merged into
  `CON-297`. Active genes fall from 2,346 to 2,343; `Merged` records rise from
  40 to 43; the 2,387 total definitions are unchanged. This is the largest
  single unit of the run and the only one with more than one merged record and
  more than two affected carriers.
- Games requiring annotation: `GAME-0143`, `GAME-0153`, `GAME-0178` and
  `GAME-0186` (signature, constraint prose, normalised genome, preserved notes,
  taxonomy impact and delta summary in each).
- Combinations affected: `COMB-0141`, `COMB-0151`, `COMB-0176` and `COMB-0184`
  each substitute `CON-297`. All four keep their size and remain strict proper
  subsets of their supporting genomes. A global recomputation confirms that
  every combination's declared supporters still equal the set of games whose
  genome contains it; this merge creates no new containment.
- Novelty claims affected: `CON-297` records the subsumption. `GAME-0143` now
  claims 25 new genes rather than 26, `GAME-0153` 12 new rather than 13,
  `GAME-0178` 18 new rather than 19, and `GAME-0186` reuses `CON-297` in place
  of `CON-366` without changing its new-gene count.
- Comparison impact: `CON-297` is now shared by eleven signatures instead of
  seven, so the recomputed `genome-jaccard-v1` scores between crafting games
  rise where both carry it. The comparison migration check confirms every
  recorded exact and near selection stays current, and no exact genome or
  combination collision is created.

## Decision

- Decision: `Accepted`.
- Decided by: confirmed audit card `C-13` plus a fresh unit-level scan over the
  complete Constraint registry and a clause-by-clause containment check.
- Rationale: the surviving Constraint already stated every clause of the three
  specific records; keeping them asserted that an ingredient's source and a
  station's class were boundaries when the broad record had classified them as
  parameters of itself.
- Implementation links: `CON-297`, `CON-320`, `CON-366`, `CON-462`, `CON-310`,
  `CON-207`, `CON-172`, `CON-498`, `CON-581`, `GAME-0143`, `GAME-0153`,
  `GAME-0178`, `GAME-0186`, `COMB-0141`, `COMB-0151`, `COMB-0176`, `COMB-0184`.

## Change history

- 2026-09-06 — created and accepted as unit 8 of the confirmed taxonomy
  normalisation derived from `FULL_TAXONOMY_DUPLICATE_AUDIT_001`.
