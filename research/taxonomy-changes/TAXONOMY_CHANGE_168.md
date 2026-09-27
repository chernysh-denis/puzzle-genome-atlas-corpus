# Taxonomy Change 168: Bash, chosen checkpoints and restoration flood

## Status

- Proposal status: Accepted
- Claim status: Confirmed
- Evidence quality: Corroborated
- Confidence: High
- Date: 2026-09-27
- Trigger: `GAME-0431` *Ori and the Blind Forest*, original 2015 Xbox One Ginso Tree packet.
- Scope: admit `ACT-569`, `ACT-570`, `SYS-1131`, `SYS-1132`, `SYS-1133` and `CON-708` as Active. No earlier signature, definition or verified combination changes.

## Problem and accepted change

Bash is not an ordinary jump: the player selects an eligible enemy, projectile or lantern and an angle, while the system launches Ori in that direction and a contacted projectile oppositely. Soul Link is not the sequel's automatic checkpoint: the player chooses a safe position and spends energy to create a retry point. Clearing the Ginso heart then triggers a continuously rising lethal waterline. One generic movement, save or hazard label would erase these decision boundaries.

## Transfer and rejection tests

- Reuse `ACT-008`, `SYS-398`, `CON-349` and `TIM-003` for directly controlled movement, retained Bash capability, gated route edges and live time. The player aim and the dual-body outcome remain distinct.
- Reuse `ACT-341`, `CON-621` and `SYS-973` for the fixed Spirit Well, not for player-placed Soul Link. `SYS-369` is authored automatic restoration; it cannot explain the choice and resource price of the new anchor.
- Reject `SYS-994` shield reflection: Bash deliberately sets Ori and projectile on opposing trajectories from a chosen target, not a passive frontal guard returning a shot to its owner.
- Reject `SYS-1032`: Ginso flooding is triggered by heart restoration, not expiration of a Worms round into Sudden Death.
- Do not invent an energy price for Bash, exact water speed, mandatory mid-escape checkpoint, or a unique path through the tree.

## Evidence and limits

[The original Xbox manual](https://dlassets-ssl.xboxlive.com/public/content/0bb3a78d-ea8a-48e2-9049-eec15e61c078/GameManual/6e3e9527-b705-4c19-926f-8ef24bf1f5a5/en-SG/index.html) separates Soul Link and Bash inputs. [Xbox's creator-led Ginso demonstration](https://news.xbox.com/en-us/2014/08/14/gamescom-ori-preview/) states the opposed projectile motion, player-placed Soul Link and restoration-triggered escape. [Xbox's launch description](https://news.xbox.com/en-us/2015/03/12/games-ori-and-the-blind-forest-is-a-sight-to-behold/) states the safe-location and energy limits; two written retail guides bound the later keys, well and heart. No original executable, save, direct-play trace or audiovisual source was inspected.

## Decision

Accept six new boundaries with reviewed Ukrainian wording, deterministic corpus comparison, original rule-valid artwork and complete repository/browser gates. This local unit authorises one local commit only; no push, public corpus publication or deployment.
