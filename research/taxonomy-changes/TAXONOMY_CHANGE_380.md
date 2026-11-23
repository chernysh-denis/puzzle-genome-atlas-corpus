# Taxonomy Change 380 — Position-sensitive rhythm input and live ranks

- Proposal status: Accepted
- Claim status: Observation
- Evidence quality: Corroborated
- Confidence: High
- Date: 2026-11-22.
- Scope: [Samba de Amigo](../../knowledge/games/s-z/samba-de-amigo.md),
  GAME-0634. First chart of the North American Dreamcast original,
  Arcade Normal with Maracas input.
- Decision: add ACT-844, ACT-845, CON-865, INF-588, OBJ-341, SYS-1835
  and SYS-1836 as Active. Reuse INF-299 and TIM-003. Preserve earlier
  signatures and combinations.

## Boundaries

- ACT-844 requires a timed motion in an indicated spatial band.
  ACT-545 requires physical foot-panel inputs, and ACT-682 recognises
  a continuous body trajectory. ACT-845 is a separate action that
  maintains both shaker positions without a shake impulse. The
  position reference from the player's height belongs to CON-865.
- INF-588 provides the outward destinations and different cue classes
  during play. INF-379 and INF-402 describe fret or arrow lanes with
  different target semantics. The settled report uses INF-299.
- SYS-1835 resolves a local event from timing and shaker configuration.
  SYS-1836 raises and lowers the gauge and live ordinal rank.
  SYS-1059 instead evaluates response to alternating authored phrases
  and uses different failure states.
- OBJ-341 requires a passing live rank and an ordinary song successor.
  OBJ-215 scopes survival to a song report, OBJ-239 a dance chart
  ending at nonzero gauge, and OBJ-258 a passing terminal quality
  grade without a live song survival gauge.

See SAM-001 through SAM-006 in the bounded analysis.
