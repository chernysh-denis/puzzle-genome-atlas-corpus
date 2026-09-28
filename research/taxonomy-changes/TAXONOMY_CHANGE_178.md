# Taxonomy Change 178: Location-led wild capture in launch Pokémon GO

## Status

- Proposal status: Accepted
- Claim status: Observation
- Evidence quality: Corroborated
- Confidence: High
- Date: 2026-09-28
- Trigger: `GAME-0441` *Pokémon GO*, original July 2016 US Android ordinary wild encounter.
- Scope: admit `ACT-577`, `SYS-1156`, `CON-715`, `INF-426`, `INF-427` and `OBJ-252` as Active. No earlier signature or verified combination changes.

## Problem and accepted change

The original product's location-based search leads to a map-visible wild target, then a separate touchscreen capture encounter. The player's actual walking is the input, while the app's device-position projection and local target display are the response. In the encounter, a thrown Ball must contact the target before the uncertain capture result. Map disclosure and changing ring feedback are distinct information surfaces; retaining one catch is the analytic terminal, not the game's global victory. These boundaries are more transferable than GPS coordinates, species identity, Ball colour or numeric catch rates.

## Transfer and rejection tests

- Reuse `ACT-194` for the committed Ball, `SYS-307` for uncertain capture and `CON-276` for eligible wild target plus device supply. An existing gene need not be rewritten for this narrower carrier.
- Reject `ACT-008`: physical walking with a location-aware device is not a virtual avatar command. Reject `SYS-954`: its terrain step samples a hidden battle directly, whereas this target appears on a map before a separate touch-opened encounter.
- Reject `INF-144`: it exposes authored driving-route guidance, not nearby wild creatures around the phone's current position.
- Do not infer a universal 2016 capture percentage, a deterministic effect of each ring diameter, a fixed encounter timer or exact server spawn table. August 2016 publisher notices document temporary throw/XP defects, not timeless launch constants.

## Evidence and limits

[Niantic's dated launch announcement](https://pokemongo.com/news/launch) establishes real-world location exploration and catch play. The [contemporary first-hand catch guide](https://www.nintendolife.com/news/2016/07/guide_advanced_pokemon_go_capture_tips_and_how_to_get_better_pokeballs) supports the ring and aimed Ball procedure; the [official catch help](https://niantic.helpshift.com/hc/en/6-pokemon-go/faq/102-finding-catching-wild-pokemon/) corroborates only the continuing basic sequence and includes later features excluded here. Niantic's [accuracy-bug notice](https://pokemongo.com/news/encounter-update) and [August release notes](https://pokemongo.com/news/update-080816) mark historical rule drift. No original binary, server or direct play was inspected.

## Decision

Accept the six boundaries with reviewed Ukrainian copy, mechanically plausible original art and full repository/browser gates. This final Goal unit permits one local commit only, without push, public corpus publication or deployment.

## Advisory health review

`BASELINE_441.json` reports 2,297 single-carrier Active genes of 3,097 (74.1686%), above the advisory 70% review threshold. These six new boundaries survive the concrete transfer tests above; their source-specific distinctions are not repaired by renaming a generic capture gene. The latest nine-game window adds 43 new genes, 4.777778 per game, below the separate 12-gene advisory. Retain these accepted boundaries and route the cumulative singleton signal to the next maintainer taxonomy review. Neither threshold authorises a merge or corpus freeze.
