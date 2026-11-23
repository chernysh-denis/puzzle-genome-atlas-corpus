# Taxonomy Change 395 — Retained rows and ordered troop settlement

- Proposal status: Accepted
- Claim status: Observation
- Evidence quality: Corroborated
- Confidence: High
- Date: 2026-11-22.
- Scope: [Drop Duchy](../../knowledge/games/a-f/drop-duchy.md), GAME-0649.
  Ordinary Wooded Region in the English Windows launch-period base game.
- Decision: add ACT-861 and SYS-1872 through SYS-1876. Reuse eight
  definitions and preserve earlier signatures.

## Boundaries

- ACT-861 orders both sides' deployed groups before issuing the
  battle command. SYS-019 executes previously committed hostile
  intents and does not give the player the same scheduling authority.
- SYS-1872 credits terrain in completed rows while preserving the
  occupied cells. SYS-008 removes rows. SYS-1521 keeps completed rows
  temporarily and clears them at mode exit.
- SYS-1873 converts eligible adjacent terrain while recruiting.
  SYS-487 applies district yields and does not perform the same
  conversion and immediate troop award.
- SYS-1874 combines friendly groups and reduces the combined force
  to one type. SYS-1875 subtracts opposing strength with a class
  matchup. Their different resolutions apply to the same ordered
  chain. Fractional rounding is outside the observed packet.
- SYS-1876 pays immediately for survivors. The resource receipt
  separates that yield from previously credited terrain.
