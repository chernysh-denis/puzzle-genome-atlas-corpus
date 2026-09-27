# Taxonomy Change 162: Wingmate-qualified route in bounded rail flight

## Status

- Proposal status: Accepted
- Claim status: Confirmed
- Evidence quality: Direct
- Confidence: High
- Date: 2026-09-27
- Trigger: `GAME-0424` *Star Fox 64*, original Nintendo 64 Main Game Corneria stage.
- Scope: admit `ACT-562`, `SYS-1119`, `SYS-1120`, `CON-706`, `INF-416` and `OBJ-245` as Active. Reuse direct hostile attack, authored craft manoeuvre, live combat and real-time progression. No earlier signature or verified combination changes.

## Problem and accepted change

The original Nintendo manual distinguishes 3D Scroll Mode from All-Range Mode: the Arwing can be steered in the screen's directions within bounds as the authored stage advances. The first-stage alternate route is also not a freely selected map destination. Falco must remain available and Fox must fly through seven stone arches; that joint in-stage condition changes both the encountered boss and the next map edge from ordinary Meteo to Sector Y. The new action, corridor law, branch law, eligibility constraint, route-relevant interface and terminal objective preserve these distinct decision boundaries without making seven separate arch genes or claiming a complete campaign model.

## Transfer and rejection tests

- Reuse `ACT-161` and `SYS-215` for directly aimed shots and live target damage; optional Smart Bomb and laser lock-on are scoped parameters.
- Reuse `ACT-496` for a player-triggered authored craft manoeuvre such as roll or boost, and `TIM-003` for live overlap among progress, fire and rescue timing.
- Reject `ACT-392`/`SYS-723`: unrestricted six-degree craft travel would misstate bounded Corneria 3D Scroll. Reject `SYS-496`: Geometry Dash's side-view single-control music clock is not Arwing combat.
- Reject `CON-168` and `INF-062`: the alternate boss requires an ally and traversal set in live flight, not a narrative threshold or preflight node menu.
- Do not add score, medal, later-stage, All-Range Mode or exact boss-pattern mechanics to this first-stage signature.

## Evidence and limits

The [original Nintendo 64 instruction booklet transcription](https://world-of-nintendo.com/manuals/nintendo_64/star_fox_64.shtml) directly identifies the Main Game's Corneria/Meteo/Sector Y results (pp. 12–13), 3D Scroll and checkpoint (p. 14), combat controls (pp. 8–9, 21), wingmate distress and status (pp. 18–19), and Corneria's exact Falco-plus-seven-arch condition (p. 24). The HTML copy is hosted by a third party; no original page image, executable, audiovisual trace or input timing was inspected. These omissions forbid frame-precise arch detection and boss-phase claims.

## Decision

Accept the six bounded new genes only with deterministic comparison, complete Ukrainian translation and presentation, valid original illustration and all repository/browser gates before the authorised one local commit. No push or publication is authorised by this record.
