# Mechanical family registry

The family registry is a controlled navigation and analysis layer over complete
game genomes. It does not replace genes, combinations or full-genome Jaccard
comparison.

## Data model

- `profile`: one short description of the bounded packet analysed for a game;
  profiles remain game-specific and are stored in
  `knowledge/games/index-metadata.json`.
- `family`: a reusable, deliberately broader mechanical lineage recorded in
  `registry.json`.
- One game must belong to at least one family and may belong to several.
- Every family must have at least two independently analysed game supporters.

Membership means that the family's defining intervention-response structure is
material to the analysed boundary. Genre, theme, camera, platform and generic
genes such as visible state or self-paced play are insufficient on their own.

## Maintenance

When adding or normalising a game:

1. preserve its specific profile;
2. test every existing family boundary before proposing another family;
3. add all materially supported memberships, not only one primary label;
4. keep each family populated by at least two games;
5. run repository validation and the web corpus tests.

The registry is reviewed metadata. It is not a claim that all members are
equally similar or that family membership proves historical influence.

## Review status

`FAMILY_TAXONOMY_REVIEW_001` checked all 17 bilingual boundaries and all 108
memberships. Four broad associations were removed because the analysed packet
did not contain the family's stated causal intervention:

- visible SET cards are matching, not hidden-state inference;
- FreeCell reserve cells are board capacity, not delivered inventory;
- Echochrome changes projected adjacency but does not construct a route;
- the Stardew Valley bundle packet fills typed slots but is not spatial packing.

The review also replaced three research-heavy public labels with shorter
equivalents. Stable family IDs and slugs did not change.
