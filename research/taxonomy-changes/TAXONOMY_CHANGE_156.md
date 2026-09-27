# Taxonomy Change 156: FTL's room-level ship command and charged retreat

## Status

- Proposal status: Accepted
- Claim status: Observation
- Evidence quality: Corroborated
- Confidence: High
- Date: 2026-09-27
- Trigger: `GAME-0418` *FTL: Faster Than Light*, original Windows Kestrel Type A first-sector conditional hostile beacon.
- Scope: admit `ACT-555`, `ACT-556`, `SYS-1107`–`SYS-1110`, `CON-703`, `CON-704`, `INF-411`, `OBJ-243` and `TIM-030` as Active. No prior signature or verified combination changes.

## Problem and accepted change

Existing craft-power and starmap actions transfer, but a live FTL encounter is not direct cockpit piloting. The player assigns personnel to rooms, aims separately charging armaments at enemy system rooms and reallocates discrete reactor bars. A fired shot resolves evasion, shield eligibility and room/hull effects; a damaged room needs crew labour while fire and oxygen remain hazardous. The selected node yields a variable event, and combat may end in either destruction of the hostile or a charged FTL escape. The entire ship command surface can be paused while several kinds of order are issued. Those typed transitions are distinct from existing fighter emphasis, unconditional shield-to-hull damage, one-target personal attacks, radial squad powers and fixed authored encounters.

## Transfer and rejection tests

- Reuse `ACT-393`, `ACT-482`, `SYS-724`, `CON-578` and `TIM-003` for live power routing, addressed star-map travel, subsystem response, finite compatible ammunition and a running combat clock. Their definitions fit without changing prior signatures.
- `ACT-555` requires an addressed reachable ship room and physically assigned crew labour; `ACT-556` requires a powered, charged ship weapon and an enemy system-room target.
- `SYS-1107` requires weapon-specific shield interaction and room consequences, not every hit bypassing or every hit being intercepted. `SYS-1108` requires repair work by present crew under ongoing hazards. `SYS-1109` requires a viable charging escape drive. `SYS-1110` requires a variable beacon result after a committed discrete jump, not a grass-step encounter check.
- `CON-703` binds independently powered room systems to finite reactor bars; `CON-704` jointly binds graph reachability, fuel and live drive readiness. `INF-411` describes a shipwide current-state overview without future event certainty. `OBJ-243` permits living victory or living charged retreat. `TIM-030` accepts crew, power and target orders while the general combat simulation is reversibly paused.
- Reject `CON-565`'s starfighter-only three-channel emphasis, `SYS-940`'s unconditional shield-first damage, `INF-277`'s direct-control cockpit and `TIM-027`'s held radial squad wheel for this ship-command packet.
- No exact enemy, fuel stock, damage formula, event reward, repair tick or Advanced Edition subsystem is promoted to a gene.

## Evidence and limits

- [Subset Games' product description](https://store.steampowered.com/app/212680/FTL_Faster_Than_Light/) states crew orders, ship-power distribution, target choice, mid-combat pause, variable encounters and fight-or-escape choices, and explicitly identifies Advanced Edition as later content.
- Launch-era firsthand accounts on the [developer's strategy forum](https://www.subsetgames.com/forum/viewtopic.php?t=1887) discuss charged escape and reallocating ship power; [2012 Kestrel accounts](https://subsetgames.com/forum/viewtopic.php?t=2332) identify initial Burst Laser II and Artemis; [room repair](https://subsetgames.com/forum/viewtopic.php?t=2197), [fuel-paid jump](https://www.subsetgames.com/forum/viewtopic.php?t=2269), [missile shield bypass](https://subsetgames.com/forum/viewtopic.php?p=7048) and [hull repair separation](https://subsetgames.com/forum/viewtopic.php?t=1923) bound the causal edges.
- No executable, original binary checksum, footage or input trace was inspected. The packet is conditional on a hostile beacon event; it does not claim a scripted first-jump opponent or quantitative hidden rule.

## Decision

Accept eleven new typed boundaries for `GAME-0418` and reuse five existing genes. Preserve all earlier signatures; regenerate deterministic comparison and combination results and require reviewed Ukrainian copy, plausible original artwork and full repository/browser gates before the authorised local commit.
