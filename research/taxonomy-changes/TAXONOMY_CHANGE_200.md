# Taxonomy Change 200: original Gold clock eligibility and held Berry

## Status

- Proposal status: Accepted
- Claim status: Confirmed
- Evidence quality: Direct
- Confidence: High
- Date: 2026-10-01.
- Trigger: `GAME-0463`, original Game Boy Color Pokémon Gold Version, Route 29 night through first retained badge.
- Scope: one new Active gene, `SYS-1213`; two generalised definitions, `SYS-921` and `TIM-025`. No earlier signature, verified combination or published corpus revision changes.

## Evidence and boundaries

The [game ledger](../../knowledge/games/m-r/pokemon-gold-version.md) uses the original North American manual and pinned exact-Gold source. Its battery-backed cartridge clock is a real-world civil-time source, not an accelerated game timer. `TIM-025` previously named only the host clock; the source can also be the cartridge's clock without changing the external-calendar boundary. A clock setting made by the player at new-game setup is entry context here, not an in-packet time-travel action.

`SYS-921` filters possible wild species by time and habitat; it was first isolated for Animal Crossing fish/bugs. In original Gold, Route 29's night slots include Hoothoot where day slots do not. This eligibility does not guarantee the next encounter: `SYS-954` independently tests terrain rate and selects a weighted slot, while `SYS-004` represents the accepted random sampling.

`SYS-1213` separately resolves a held ordinary Berry automatically when a living holder falls below half HP, restores its declared ten HP up to maximum and consumes the item. It is not a player-commanded PACK heal (`ACT-199` only equips it), permanent regeneration, or party-wide Center recovery (`SYS-956`). The prior twenty-eight uses fit existing boundaries. Earlier Animal Crossing and Pokémon Red signatures remain unchanged.

## Reuse and disposition

The two generalisations are reviewed in both languages. The new Berry gene receives a complete Ukrainian definition and named role explanation inside the same unit. No exact Gold/Red match or verified combination is asserted before the deterministic corpus scan.
