# Taxonomy Change 167: Selected guard sight, not omniscient patrol vision

## Status

- Proposal status: Accepted
- Claim status: Confirmed
- Evidence quality: Direct
- Confidence: High
- Date: 2026-09-27
- Trigger: `GAME-0429` *Commandos: Behind Enemy Lines*, original 1998 Windows PC first mission.
- Scope: admit `INF-420` as Active; reuse contextual orders, posture, transport, prop placement, live patrol response and the all-survive structure objective. No earlier signature or verified combination changes.

## Problem and accepted change

The original manual allows the player to inspect one guard's moving near/far view, but other guards' sight still operates. Treating this as a complete patrol-map reveal would misstate both information and risk. `INF-420` records the limited current display, while `CON-077` remains the detection rule itself.

## Transfer and rejection tests

- Reuse `CON-077` for directed, occlusion-bounded sight. Distance and crawling alter its current permitted region; they do not create a second detection gene.
- Reject `INF-287`: that gene retains actor marks and shows directional detection progress, neither of which is evidenced here.
- Reject `INF-410`: a moving spotlight footprint plus linked alarm fixture is not a selected human guard's sight.
- Do not add a generic reinforcement gene from later missions to this first mission.

## Evidence and limits

[The original Pyro/Eidos manual](https://cdn.akamai.steamstatic.com/steam/apps/6800/manuals/commandos_manual.pdf) describes the selected enemy's view and warns that all other enemies still observe. [First-mission guide](https://gamefaqs.gamespot.com/pc/63451-commandos-behind-enemy-lines/faqs/81342) locates the bounded boat/relay route. No original executable, direct play or measured cone geometry was inspected.

## Decision

Accept one new information boundary with reviewed Ukrainian wording and repository/browser validation. This local unit does not authorise push, public publication or deployment.
