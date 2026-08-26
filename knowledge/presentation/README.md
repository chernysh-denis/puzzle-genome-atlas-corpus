# Game presentation registry

`games.json` is the versioned canonical boundary for reviewed bilingual game
summaries, Ukrainian display-title additions and external presentation links.
Canonical game identities and genomes remain in `knowledge/games/`; this
registry may not add or omit a game.

## Schema contract

- Root fields are exactly `version` and `games`.
- The current version is `GAME_PRESENTATION_V1`.
- `games` contains one entry for every parsed canonical `GAME-NNNN` record, in
  canonical game-ID order, with no surplus entries.
- Every entry requires non-empty `summaryUk`, `summaryEn`, `playUrl`,
  `linkLabelUk` and `linkLabelEn` strings.
- `titleUk` is the only optional field. Its absence means that the canonical
  English title is also used in Ukrainian presentation.
- `playUrl` must be an absolute, credential-free HTTPS URL.

Both the dependency-free repository validator and the Astro corpus parser
enforce this contract. Editorial changes require normal review; the web layer
must consume the parsed `Game.presentation` record rather than introduce a
second data island.

## Unit 9 migration proof

The migration from `web/src/lib/game-presentation.ts` reconstructed the old
title map and presentation map from the JSON and compared both structures for
deep equality. The normalized before-and-after SHA-256 was
`9bd69f90d9edeef7c24e21440df24f3ca2e3f2543a083cc630e7602f9baeea30`.
No reviewed UA or EN string was changed.
