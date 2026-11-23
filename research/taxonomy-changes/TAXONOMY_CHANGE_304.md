# Taxonomy Change 304 — Tracked scenery intervention beside a directly steered avatar

- Proposal status: Accepted
- Claim status: Observation
- Evidence quality: Corroborated
- Confidence: High
- Date: 2026-11-19.
- Trigger: [GAME-0558](../../knowledge/games/m-r/moss.md), original standalone
  Quest Moss, complete The Clearing through home arrival and book closeout.

| Addition | Reviewed boundary | Rejected reuse or counterexample |
|---|---|---|
| ACT-758 | Position and hold a tracked Reader grip independently of Quill. | ACT-114 grips with the climbing ragdoll's own articulated hands. ACT-048 takes a free rigid object into an avatar-relative carry; ACT-706 moves a fixture with the locally controlled body. None describes the separate tracked control channel. |
| ACT-759 | Direct shimmy, pull-up or drop after an automatic eligible ledge catch. | ACT-596 requires holding the attachment input; Quill retains her automatic catch without it. ACT-362 requires an explicit grip request; its associated surface-climbing stamina system is not inherited. |
| ACT-760 | Physically shift the tracked head within an anchored scene while Quill remains in world position. | ACT-610 reframes a following camera by a camera command; ACT-748 requests ball-relative viewing teleport; ACT-095 changes legal continuation by projected geometry. No such route law or teleport exists here. |
| SYS-1623 | Map accepted grip displacement to a fixture's authored translation, retaining an admitted release pose. | SYS-705 pulls a loose physics body into a view-relative attachment. ACT-009 is a one-position push. These stones keep their authored track and do not become freely carried bodies. |
| SYS-1624 | Sustain local braking of an otherwise driven wheel. | SYS-065 uses a linked switch to start, stop or reverse traversal; this grip slows rather than completely stops the wheel. SYS-1363 is already reused for carrying supported Quill and does not describe the separately commanded speed modifier. |
| CON-824 | Admit authored scenery targets and their particular motion envelopes. | CON-556 describes remote loose-physics eligibility, traces, mass and body classes. CON-165 requires articulated-body leverage. Neither permits an inference that the Reader can lift Quill or every solid surface. |
| INF-535 | Read a tracked local diorama, occluded geometry, authored affordance cues and companion advice. | INF-001 would overstate whole-state visibility; INF-192 is a scrolling side view; INF-317 requires instructions fixed to world positions. INF-271 separately and unchanged describes the visible grip response, not the whole local inspection/advice surface. |

Eleven unchanged genes cover direct movement/jumping, breakable strikes and
contextual levers; live gravity/support, fragment contact, container destruction,
local checkpoint retry and autonomous paddle transport; grip feedback, home
arrival and live time. The automatic ledge command is not a new force solver.
A moving wheel remains a supported platform whether its local rate is reduced
or ordinary. Seven additions do not create seven platform-specific variants.

The named GAME-0558 salience review partitions all eighteen admitted genes
without weights. It is a bounded extension of the reviewed salience pilot,
not automatic classification. Existing signatures, definitions, family labels,
release mapping and historical receipts are unchanged. No combination is
created merely from two generic controls: the exhaustive proper-subset scan
owns support. The standing singleton advisory is retained as comparative-review
risk, not an automatic taxonomy merge or expansion freeze.
