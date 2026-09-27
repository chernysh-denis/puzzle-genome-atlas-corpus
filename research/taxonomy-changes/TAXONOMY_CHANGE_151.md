# Taxonomy Change 151: Reusable net contact and first-visit monkey quota

## Status

- Proposal status: Accepted
- Claim status: Observation
- Evidence quality: Corroborated
- Confidence: High
- Date: 2026-09-26
- Trigger: `GAME-0413` *Ape Escape*, original PlayStation first Fossil Field visit.
- Scope: broaden `ACT-477`'s target from insect to reachable creature; admit `SYS-1099`, `SYS-1100`, `INF-406` and `OBJ-242` as Active. No earlier signature or verified combination is changed.

## Problem and accepted change

The previous `ACT-477` description made the net's collision geometry specific to an insect, despite the action being a short player-aimed swing through a reachable world volume. Ape Escape uses that same decision and contact test against a moving monkey. Target species is a parameter; the difference is what the system does with an accepted catch. Animal Crossing creates a carried specimen and catalogue credit, whereas Ape Escape removes an individual monkey from a first-stage chase and advances a three-of-four quota. Broadening the action avoids a synonym gene while distinct system, information and terminal boundaries retain the divergent consequences.

## Transfer and rejection tests

- `ACT-477` still requires a directly steered transient held-net sweep and a currently reachable living target. It excludes automatic pickups, autonomous traps and consumed thrown capture devices (`ACT-194`). The Animal Crossing signature is unchanged.
- `SYS-1099` is local evasion by an uncaught capture target, not hostile pursuit toward the player (`SYS-057`) or decorative animal movement. Its exact alert radius and route policy remain unknown.
- `SYS-1100` writes a retained individual caught flag and quota increment after an accepted Time Net contact. `SYS-922` additionally creates a carried specimen and species catalogue; `SYS-307` resolves a probability check into companion ownership. Neither is implied here.
- Duplicate queue `272` flags `SYS-1099/SYS-1100` because both involve the same monkeys. Reviewed disposition: retain both. `SYS-1099` updates the position of a **still-uncaught** target after approach or a miss; `SYS-1100` removes that target and advances a retained count **only after accepted net contact**. They have different triggers, state transitions and counterfactuals; merging would erase the reason a miss differs from a catch.
- `INF-406` exposes minimum, total and accepted stage-capture counts, not the full future position of every monkey or Animal Crossing's species catalogue (`INF-352`).
- `OBJ-242` closes the visit at a minimum distinct-creature count while an optional fourth remains. `OBJ-019` requires escort through a fixed exit, and `OBJ-018` counts staged tokens rather than living capture targets.
- Right-stick direction and left-stick movement are controller parameters of `ACT-477` and `ACT-008`, not separate genes merely because a hardware input is distinctive. The starting Stun Club and optional orange-enemy combat do not change the selected net-only three-catch route.

## Evidence and limits

- [Sony PlayStation history](https://www.playstation.com/uk-ua/playstation-history/1994-ps-one/) identifies the original game as a twin-analog gadget-capture design; [Sony's Ape Escape listing](https://store.playstation.com/en-us/product/UP9000-PPSA06319_00-SCUS944230000000/) confirms the original title and Time Net, but the listing's present-day conversion features are excluded.
- Original-PlayStation player walkthroughs by [AmericanArsenal](https://gamefaqs.gamespot.com/ps/196614-ape-escape/faqs/26743), [CHyde](https://gamefaqs.gamespot.com/ps/196614-ape-escape/faqs/8940), [CaptainCAWisma](https://gamefaqs.gamespot.com/ps/196614-ape-escape/faqs/32849) and [Gbness](https://gamefaqs.gamespot.com/ps/196614-ape-escape/faqs/25865) corroborate control mapping, Fossil Field's three-needed/four-total boundary and later reach to the remaining monkey. They are player-authored, not a substitute for an inspected original manual or a direct play trace.
- No disc, executable or gameplay trace was inspected. Exact numeric movement, alert, collision, health and same-frame resolution values are not claimed.

## Decision

Accept the target-neutral net-contact wording and the four typed first-visit boundaries only for `GAME-0413`. Retain all earlier signatures and run deterministic comparison, subset and localisation checks before acceptance. The change does not assert that Ape Escape invented net capture or creature evasion.
