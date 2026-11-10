# Taxonomy Change 259 Country capitulation and later war settlement

## Status

- Proposal status: `Accepted`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Date: 2026-10-14
- Scope: existing `CON-484` in `GAME-0182` and `COMB-0180`; no carrier or lifecycle change.

## Decision

`CON-484` tests country-level surrender progress. Loss of weighted
victory-point control, with applicable modifiers, must cross the country's
current surrender threshold before it capitulates. A subsequent peace
conference or settlement belongs to the war-level sequence, not to this
country-level predicate.

The earlier English definition required a legal terminal war settlement
*before* country capitulation. The
[Paradox-hosted strategy guide](https://forumcontent.paradoxplaza.com/public/paradox/banners/HoI_IV_Strategy_Guide.pdf#page=56)
places peace-treaty demands after enemy capitulation. The
[official tutorial diary](https://store.steampowered.com/news/posts/?appids=394360&enddate=1464622058)
places Italy in the Ethiopian war and says the same save can continue after
the tutorial. These sources distinguish the transitions; they do not
establish every patch-1.19.2 faction or peace-conference eligibility rule.

The scoped Hearts of Iron IV packet still ends after the Ethiopian war's
immediate settlement, and `COMB-0180` still describes production and supplied
fronts leading to that bounded endpoint. The P1 Ukrainian definition already
named country capitulation correctly; it is retained. Its exclusions and
both plain-language explanations now state the distinction explicitly.
`GAME-0182` remains the sole carrier and `COMB-0180` the sole verified
combination containing `CON-484`. The gene set, signatures and pair scores
do not change. Exact field snapshots and checks are in the
[canonical audit](../normalisation/P2_CANONICAL_SOURCE_REVIEW_011.json).
