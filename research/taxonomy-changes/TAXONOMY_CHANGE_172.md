# Taxonomy Change 172: Rolling HP and first sanctuary progress in EarthBound

## Status

- Proposal status: Accepted
- Claim status: Confirmed
- Evidence quality: Direct
- Confidence: High
- Date: 2026-09-27
- Trigger: `GAME-0435` *EarthBound*, original 1995 North American Super Nintendo first Giant Step sanctuary.
- Scope: admit `SYS-1139`, `SYS-1140`, `SYS-1141` and `OBJ-250` as Active. No earlier game signature, gene definition or verified combination changes.

## Problem and accepted change

Nintendo's original Player's Guide describes field contact, menu commands and the gradually decreasing HP readout, explicitly observing that a victory before the visible count reaches zero averts unconsciousness. A separate authored guardian and site visit record the first melody in the carried Sound Stone. The command-response loop, damage-display settlement, retained melody and guarded-site objective are different causal boundaries; merely marking the cave as turn-based combat would omit the intervention window and the post-battle endpoint.

## Transfer and rejection tests

- Reuse `ACT-008`, `ACT-019`, `ACT-131`, `SYS-355`, `SYS-362`, `SYS-380`, `CON-269`, `CON-282`, `INF-119` and `TIM-003` for movement, command choice, a carried recovery item, field contact, combat experience, PSI effect, PP legality, story gates, visible status and the live HP counter.
- Reject `SYS-955` because its paired Pokémon move commitments, priority and Speed scheduler do not describe Ness's menu and hostile group. Do not infer exact EarthBound initiative from this packet.
- Reject `TIM-026` because an ATB readiness gauge is not the rolling HP display. Reject `TIM-001` because health may keep changing while the next input remains possible.
- Reject `OBJ-191` because a Triforce fragment is not the separately recorded first sanctuary melody. Reject `SYS-1137` because Ecco's learned acoustic barrier key is not a Sound Stone record.
- A hypothetical healing action's exact cancellation of every lethal countdown and a fixed HP tick rate are not claimed.

## Evidence and limits

[Nintendo of America's original 1995 Player's Guide](https://www.nintendo.co.jp/clvs/manuals/common/pdf/CLV-P-SAAJE.pdf), pp. 9–12 and 22–23, directly establishes the battle choices, gradual HP fall, cabin access, Titanic Ant with two Black Antoids and first Sound Stone melody. The hosted PDF is image-only; the cited pages were visually rendered and inspected. [Nintendo's later digital manual](https://www.nintendo.com/es-es/games/oms/snes-classic/manuals/earthbound/manual.pdf) corroborates controls and resources, but its Wii U wrapper is excluded. [A first-hand original-SNES written route](https://gamefaqs.gamespot.com/snes/588301-earthbound/faqs/14736) independently supports the guardian and first melody. No original cartridge, direct play, input trace, screenshot, video or audio was inspected, so exact battle timing and cartridge revision remain unknown.

## Decision

Accept four narrowly typed boundaries, reviewed Ukrainian copy, the complete lower-ID comparison, original mechanics-led artwork and repository/browser gates. This unit authorises one local commit only; no push, public corpus publication or deployment.
