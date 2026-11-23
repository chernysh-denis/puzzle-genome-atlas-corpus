# Taxonomy Change 330 — Saturn Bomberman battle round

- Proposal status: Accepted
- Claim status: Observation
- Evidence quality: Corroborated
- Confidence: Medium
- Date: 2026-11-20.
- Scope: `GAME-0584`, original English North American Sega Saturn
  commercial disc, the first local free-for-all on Path to Glory with
  No Draw on and Mad Bomber off.
- Source: [Saturn Bomberman](../../knowledge/games/s-z/saturn-bomberman.md).
  The original English manual and sampled North American and
  separately labelled Japanese frames support the defined progression.

| Addition | Boundary | Closest rejected substitute |
| --- | --- | --- |
| SYS-1723 | Land solid late-round pressure blocks in playable lanes while the bout is live. | CON-068 ends an attempt on expiry, without changing traversable cells during play. SYS-1045 computes a blast ray, not a lasting occupied pressure cell. |
| SYS-1724 | Apply capped cumulative changes on separately typed capability axes after pickup. | SYS-037 acquires the pickup. The separate improvement may affect range, count or speed. SYS-911 spends a finite life and restores a body. |
| CON-842 | Deploy only below the owner's concurrent active bomb cap; space becomes available when one resolves. | ACT-270 is the decision to place an available timed bomb. CON-694 consumes an arcade bomb stock for an emergency clear. |
| INF-555 | Display both round clock and individual accumulated win counts during a live multi-contestant bout. | INF-210 describes paired fighting-game vitality and shared-resource state with its clock and score. INF-179 is the visible field rather than the match tally. |
| OBJ-320 | Credit one win to the last eligible individual in the arena. | SYS-423 awards the last surviving squad under squad rules. OBJ-071 settles an asymmetric defusal match from cumulative scores. |

Ten definitions are reused without alteration, including the Super Bomberman
boundaries for blast geometry, fuse resolution and destruction of compatible
terrain. CON-263 applies here because Mad Bomber is off. The full-match
target is an explicit parameter. Neither a post-match bonus nor an
unsupported special item gets a gene in this bout. No existing ID,
definition, signature, combination or release mapping changes.
