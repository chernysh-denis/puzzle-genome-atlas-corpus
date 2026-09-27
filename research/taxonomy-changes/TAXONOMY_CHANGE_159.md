# Taxonomy Change 159: Contact-triggered belt drive in an editable contraption

## Status

- Proposal status: Accepted
- Claim status: Confirmed
- Evidence quality: Direct
- Confidence: High
- Date: 2026-09-27
- Trigger: `GAME-0421` *The Incredible Machine*, original DOS manual's basketball worked example.
- Scope: admit `SYS-1115` as Active; reuse spatial machine editing, continuous body dynamics, visible state, fixed receiver and resettable run genes without altering earlier signatures.

## Problem and accepted change

The worked example requires more than a ball colliding with a static conveyor. A falling bowling ball starts a mouse motor, and only an attached belt transfers that motor's rotation to the conveyor that moves the basketball. Neither generic gravity/collision (`SYS-036`) nor a perpetually running belt describes the conditional power path. `SYS-1115` records the linked physical trigger and drive; motor count, belt endpoints and ball types are parameters.

## Transfer and rejection tests

- Reuse `ACT-028` for motors, ramp and belt endpoints arranged in the editable machine design; do not create a second Action for attaching a belt.
- Reject `SYS-077`'s discrete conveyor transport and `SYS-157`'s live factory logistics. Both lack this per-run, contact-triggered motor-to-belt activation.
- Reject `SYS-192`'s programmable sensor/logic graph. The manual's trigger is physical contact, not a logic wire or player-authored Boolean program.
- Do not infer precise motor torque, belt speed, collision timing or the uniqueness of the manual solution.

## Evidence and limits

The [original Sierra/Dynamix DOS manual scan](https://www.retrogames.cz/manualy/DOS/The_Incredible_Machine_-_DOS_-_Manual.pdf), printed p. 16, depicts and explains bowling balls striking mouse motors linked by belts to conveyors; printed pp. 8–11 cover edit/run controls. The [Sierra Help walkthrough](https://sierrahelp.com/Walkthroughs/TheIncredibleMachineWalkthrough.html) independently corroborates the mechanism but conflicts with the manual's numbered puzzle label. No executable or direct play was inspected, so this taxonomy boundary does not depend on a verified in-game puzzle number.

## Decision

Accept one typed physical power-transition gene, retain earlier genomes and verified combinations, and require deterministic comparison, reviewed Ukrainian localisation, rule-valid original artwork and repository/browser gates before the authorised local commit.
