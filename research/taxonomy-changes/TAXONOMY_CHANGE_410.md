# Taxonomy Change 410 — Dicey Dungeons dice-to-equipment combat

- Proposal status: Accepted
- Claim status: Observation
- Evidence quality: Corroborated
- Confidence: High
- Date: 2026-11-23.
- Scope: [Dicey Dungeons](../../knowledge/games/a-f/dicey-dungeons.md),
  GAME-0664, the commercial Android base rules for the normal first-episode
  Marshmallow fight through the level reward.
- Decision: admit eleven boundaries and reuse ACT-126, SYS-004, SYS-299,
  SYS-362, INF-002 and OBJ-029. No existing signature or gene definition
  changes.

| Gene | Accepted boundary | Nearest rejected equivalence |
| --- | --- | --- |
| ACT-881 | Allocate a specific free die to an eligible equipment socket | ACT-019 independently selects an ability and combat target |
| ACT-882 | Take one level reward into carried equipment storage | ACT-128 adds one card to a persistent deck or skips |
| SYS-1907 | Spend the die and resolve the target card's formula | SYS-801 compares a rolled check rather than converting a chosen die to effect |
| SYS-1908 | Return an incremented die for a second allocation this turn | SYS-357 renews aggregate action points at a turn boundary |
| SYS-1909 | Reroll one existing die against its own capped and renewed allowance | SYS-004 describes random selection; it does not preserve the rest of a current pool or count individual rerolls |
| SYS-1910 | Attach a later die mark that can be cleared with health | SYS-1527 repeats poison damage without returning a marked action input |
| SYS-1911 | Set one upcoming die to a fixed face without removing it | Deleting a die or disabling equipment changes different resources |
| CON-878 | Test that die's face against an equipment-specific predicate | CON-094 uses aggregate spendable budget regardless of individual token faces |
| CON-879 | Exhaust and restore uses independently per piece of equipment | A shared budget or elapsed cooldown has a different owner and refresh |
| INF-612 | Reveal the live faces, sockets, current terms, health and statuses together | INF-152 describes a difficulty and modifiers for a single explicit check |
| TIM-047 | Opponents take serial phases with fresh rolls and immediate actions | TIM-005 resolves attacks already committed before the handoff |

Reused encounter rewards, experience levels and defeat are separate
boundaries. Dice values, card names, limits and observed reduction values
are parameters. No verified combination applies. No universal novelty,
Android binary parity or exact RNG distribution is asserted.
