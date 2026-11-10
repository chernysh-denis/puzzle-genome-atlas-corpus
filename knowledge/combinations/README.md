# Combination Registry

A combination record identifies a verified interaction between genes. It is not
an empty matrix cell, a game pitch or a novelty claim.

The canonical definition is in
[`docs/ARCHITECTURE.md`](../../docs/ARCHITECTURE.md#canonical-vocabulary). In
particular, a combination gene set is a proper subset of each supporting game
genome; it must not duplicate a full genome.

Each record requires:

- a stable `COMB-xxxx` ID;
- a gene set containing at least two IDs from at least two types;
- at least one analysed game;
- decision-structure notes;
- a match boundary and explicit novelty conclusion;
- evidence and confidence.

The first paragraph of `## Combination gene set` is the authoritative
membership block: either a backtick-wrapped `ID + ID` formula (which may wrap
across lines), or a contiguous bullet list of backtick-wrapped IDs. Legacy
typed rows such as `- Actions: ID, ID` also remain supported, with each ID
individually backtick-wrapped. A blank line ends this block. Later explanatory
paragraphs may reference member or excluded genes without adding membership.
Missing, malformed or repeated IDs in the membership block are errors; readers
must not silently deduplicate an invalid formula.

The [index](INDEX.md) supports corpus-wide subset scanning. Exact and near
genome matching uses the separate game index. Exploratory combinations remain in the private working repository until
they are supported by a complete analysis.

Every complete game genome that contains a combination as a proper subset must
be listed reciprocally in the combination record, the game front matter and
both indexes. Repository validation enforces this exhaustive support set.

A recurring shared-core combination may be nested inside a more specific
combination without replacing or weakening it. The smaller set still requires
an independently stated decision structure and match boundary; a mathematical
intersection alone is not sufficient evidence for a new record.
