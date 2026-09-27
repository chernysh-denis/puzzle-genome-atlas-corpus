# Taxonomy Change 155: Sly Cooper's local spotlight alarm

## Status

- Proposal status: Accepted
- Claim status: Observation
- Evidence quality: Corroborated
- Confidence: High
- Date: 2026-09-27
- Trigger: `GAME-0417` *Sly Cooper and the Thievius Raccoonus*, original PlayStation 2 `A Stealthy Approach`.
- Scope: admit `SYS-1106` and `INF-410` as Active. No earlier game signature or verified combination changes.

## Problem and accepted change

The first swamp approach presents two local moving-searchlight passages with visible scan footprints and red sirens. Crossing an active footprint sounds the alarm; a cane strike destroys the linked siren and deactivates the local security system. The current footprint and controller must be read before choosing a crossing interval. Existing guard-suspicion, lighting-weighted acquisition and irreversible loud-heist genes do not fit this local binary fixture relationship. The new system boundary owns the scan-to-alarm-to-disable transition, while the information boundary owns the present visible footprint and alarm feedback. The exact sweep geometry is a parameter, not another gene.

## Transfer and rejection tests

- `SYS-1106` applies when a visible security scan detects crossing and an eligible linked controller can be destroyed to remove that local scan risk. It does not imply reinforcement, a world-wide wanted state or an irreversible mission phase.
- `INF-410` applies when the player can see current scanning coverage and the local controller or alarm state but not an exact future schedule. It is not an avatar-centred suspicion meter or an omniscient stage map.
- Reuse `ACT-008`, `ACT-161`, `SYS-063`, `SYS-755`, `SYS-911`, `SYS-933`, `CON-183`, `OBJ-026` and `TIM-003` for movement, strikes, key-gate access, breakage, finite-life checkpoint return, place objective and live timing.
- Reject `SYS-373`, `SYS-645`, `SYS-888` and `INF-298` for this packet: no progressive guard suspicion, permanent loud conversion, alarm-preemption countdown or directional avatar-centred awareness display is established.
- The optional clue-bottle vault and ability page are not made necessary for the selected key-gated exit.

## Evidence and limits

- The [original US PlayStation 2 booklet scan](https://www.videogamemanual.com/PS2/Sly%20Cooper%20and%20the%20Thievius%20Raccoonus%20%28USA%29.pdf), printed pp. 4, 10–18, describes controls, alarm traps, finite lives, keys and signal repeaters. Relevant scans were visually reviewed; SHA-256 is in the [game analysis](../../knowledge/games/s-z/sly-cooper-and-the-thievius-raccoonus.md).
- An [original PlayStation 2 route](https://gamefaqs.gamespot.com/ps2/561378-sly-cooper-and-the-thievius-raccoonus/faqs/20764) and [independent first-stage route](https://strategywiki.org/wiki/Sly_Cooper_and_the_Thievius_Raccoonus/A_Stealthy_Approach) agree on spotlight passages, siren destruction, water wheels, checkpoint, cased key and exit. They are secondary route descriptions, not direct play by the Atlas.
- No disc or executable was inspected. Frame-level hitboxes, guard timing and the transient state restored at each checkpoint are not claimed.

## Decision

Accept two typed genes for `GAME-0417` only, preserve earlier signatures, regenerate deterministic neighbour and combination checks, and require reviewed Ukrainian copy and original mechanically plausible artwork before the local commit.
