# Taxonomy Change 116: Numbered production and negotiated construction

## Status

- Proposal status: Accepted
- Claim status: Confirmed
- Evidence quality: Direct
- Confidence: High
- Date: 2026-09-23
- Trigger: `GAME-0377` CATAN, four-player fixed-beginner-setup base game under
  the CATAN-hosted 2020 English rulebook.
- Scope: sixteen additive Active genes; no earlier signature, lifecycle or
  verified combination changes.

## Problem

The shared die roll pays resources to every building adjacent to a matching
numbered hex. An active player can negotiate resource transfers or take a
spatially priced bank exchange, then spend exact resource types on connected
roads and spaced settlements. Seven interrupts production and moves a robber;
development cards are acquired hidden and played later. Public bonus points
can change hands before the first own-turn ten-point claim. Existing digital
city production and market trading genes do not preserve this physical board,
private-hand and voluntary-deal structure.

## Accepted change

- `ACT-513`–`ACT-518` distinguish peer exchange, bank conversion, legal
  construction, concealed development purchase, development play and robber
  destination/victim choice.
- `SYS-1024`–`SYS-1027` distinguish shared numbered production, seven
  interruption, development effects and transferable public bonuses.
- `CON-681`–`CON-684` retain spatial topology, exact costs and finite supply,
  harbour eligibility and development timing.
- `INF-384` separates the public production map from private hands;
  `OBJ-219` retains the own-turn point threshold.

## Lower-ID transfer and rejection test

- `SYS-004` transfers random selection, `INF-002` unknown next events,
  `INF-003` concealed current cards and `TIM-004` alternating turns.
- `SYS-484` advances a selected digital city production target rather than
  paying every neighbouring owner from one shared die total. `SYS-490`
  resolves automated empire routes, not an accepted bilateral card bargain.
- `ACT-503` places a follower to claim a Carcassonne feature, not a paid
  road/settlement/city on connected hex vertices. `OBJ-002` compares final
  score, not an immediate own-turn point race. No previous gene is broadened
  merely to make this game look similar.
- Complete lower-ID signatures and verified proper-subset combinations are
  decided by the deterministic validator, not by the CATAN theme.

## Evidence and limits

The [official CATAN base-game rules and almanac](https://www.catan.com/sites/default/files/2021-06/catan_base_rules_2020_200707.pdf)
directly specify setup, production, trades, construction, robber, development
cards, public bonuses and victory. No boxed printing or four-person match
was directly inspected. Variable setup, expanded player counts, optional
combined phases and later rulebook editions are excluded.
