# Ukrainian localisation layer

This directory contains reviewed Ukrainian presentation translations of the
canonical English research corpus. Translation records never replace gene IDs,
English definitions, evidence fields or taxonomy boundaries.

`genes.json` is organised by stable gene ID. Every record must contain a
Ukrainian label, operational definition, inclusion boundary, exclusion
boundary, review date and the game batch that introduced it. A batch covers the
union of genes used by up to five consecutive games; shared genes are translated
once and reused by later batches.

`games.json` and `combinations.json` contain reviewed presentation layers keyed
by stable corpus ID. Combination records translate the canonical label,
decision structure and novelty-assessment boundary one combination at a time.
Original game titles and all canonical English research records remain intact.

Translation review checks semantic equivalence against the canonical registry,
consistent terminology across gene types and preservation of examples and
negative boundaries. The web application uses the English record as fallback
until a reviewed Ukrainian entry exists.
