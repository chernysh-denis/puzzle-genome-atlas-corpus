# Taxonomy Change 203: proximity hold, health-priced Special and section-clock loss

## Status

- Proposal status: Accepted
- Claim status: Confirmed
- Evidence quality: Direct
- Confidence: High
- Date: 2026-10-01.
- Trigger: `GAME-0466`, original Genesis *Streets of Rage 2* Stage 1 with Axel.
- Scope: three new Active System Behaviour genes, `SYS-1216`–`SYS-1218`; no earlier signature, verified combination or public-corpus revision changes.

## Evidence and lower-ID transfer test

The [game ledger](../../knowledge/games/s-z/streets-of-rage-2.md) uses SEGA's preserved scanned original manual. Its printed close-attack pages distinguish an approach-triggered hold from pressing a dedicated grab input. `ACT-295` still represents the chosen follow-up attack, while `CON-442` checks the temporary held state; neither describes creating that state automatically. `SYS-1216` isolates the transition. `ACT-611` deliberately carries a held opponent and does not substitute for this proximity event.

The same manual distinguishes stationary A costing Axel health only when it connects from direction+A costing health on use. Ordinary `SYS-578` records the resulting health change but not the mode-dependent self-cost predicate; `SYS-1217` isolates that rule without claiming an additional special-energy meter. The printed 99-second section rule clears the next view or Go arrow and resets the clock; Time Over spends a Fighter. `SYS-915` covers hostile-gated scroll and `SYS-911` covers replacement after life loss, but neither couples a renewable section deadline to that loss. `SYS-1218` does; immediate whole-run timeout is rejected.

The first-stage Barbon terminal, temporary weapons, breakable receptacles, score-earned Fighters and visible state reuse established boundaries. Four playable fighters, later stages, co-op, Duel, Continue and collection-wrapper conveniences are excluded from this one-Axel Stage 1 packet.

## Disposition

Add `SYS-1216`–`SYS-1218` with reviewed Ukrainian definitions in this unit. Preserve every previous game signature and all verified combinations.
