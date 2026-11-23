---
game_id: GAME-0658
slug: unicorn-overlord
game_title: "Unicorn Overlord"
analysis_status: reviewed
reviewed: 2026-11-23
combination_ids: []
gene_ids:
  action:
    - ACT-189
    - ACT-870
    - ACT-871
  system:
    - SYS-1896
    - SYS-1897
    - SYS-1898
  constraint:
    - CON-068
  information:
    - INF-607
  objective:
    - OBJ-329
  time:
    - TIM-003
---

# Game: Unicorn Overlord

This analysis uses the [canonical vocabulary](../../../docs/ARCHITECTURE.md#canonical-vocabulary).

## Analysis scope

- Version / ruleset: English commercial base game on Nintendo Switch,
  released on 8 March 2024. Scope is the authored Call to Action battle
  stage in Cornia. The recordings are attributed Switch captures. The
  capture build, difficulty and exact retail bytes are unverified.
- Entry: the first Call to Action stage offers unit organization and
  shows the home command post and objective. Three early units have
  two available member slots each in the principal recording.
- Primary decision loop: assign named fighters to front or back slots,
  deploy from the friendly command post using Valor, and send the
  units along the road. Use the harbor as a friendly staging point
  after taking it. Compare predicted damage before engaging, with a
  nearby eligible ally available as an alternate combatant when the
  rules permit. Let the separate automatic encounter settle and
  decide which unit should move or recover next.
- Exit: Aubin's defeat triggers Stage Clear and the separate Stage
  Results screen. The principal trace shows 78,882 before score
  conversion, followed by awards and a post-battle scene. The second
  trace corroborates the clear and returns to controllable travel in
  Cornia after the post-battle exchanges and tutorial.
- Included: the observed formation change, live field orders, Valor
  as a field budget, use of friendly positions, the damage forecast,
  proximity-gated engagement substitution, automatic skills, stamina
  attrition, the stage deadline and the single commander objective.
- Excluded: other stages, demo continuity, post-clear Fort Soligie
  expansion, later unit capacities, optional items as required
  objectives, edit-control claims for Tactics in the recorded run,
  exact tie and random-number behavior, rescue items after defeat,
  score formulas, reload persistence and other platform editions.
- Suggested later scope: compare two configurations of the same
  unit against one enemy formation and observe how editing one
  specific Tactics row changes the forecast and resulting exchange.

## Direct-play status

No direct play was performed. Nintendo supplies the commercial release
identity. ATLUS and SEGA explain the formation, field and encounter
rules. The JRPG Millennial recording supplies the principal observed
route and its results. Handheld Players provides a separately
attributed Switch clear and successor. Still frames and on-screen
captions were reviewed in the background without audio. Exact
hardware inputs, version bytes, difficulty and save reloading were
not verified. An available command in the rules is not a claim
that either player invoked it.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
| --- | --- | --- | --- | --- | --- |
| UO-001 | The release target is the English Nintendo Switch base game. The first deployment in the scoped stage follows a unit-organization tutorial. | Observation | Corroborated | High | P1, P2, R1; W1 4:35–5:29 and W2 41:35–52:30. The recordings do not identify an exact build. |
| UO-002 | Assigning members puts named combatants into specific front and back positions. In W1 Alain's unit advances from one occupied slot out of two to a full pair, and the other two available units are also filled. | Observation | Corroborated | High | P2 printed leaf 2 and formation guide, P3 formation section, W1 5:07–5:28. Hodrick is visible in Alain’s newly full pair at 5:16. Subsequent capacity upgrades are outside the stage. |
| UO-003 | A friendly deployment post spends Valor to put a unit on the live field. The same reserve funds class-specific field skills. Victories replenish Valor; the organizer describes a leader bonus for Alain. | Observation | Corroborated | High | P2 basic tips 3 and 4, P4 deployment and Valor, W1 5:28–5:42 and 18:44–18:53, 20:19. The tutorial describes Valorous Order; it does not prove the player cast it. |
| UO-004 | Orders give deployed units map destinations. Field movement, position ownership and elapsed time matter independently of the automatic encounters. A captured port becomes a friendly facility. | Observation | Corroborated | High | P4 movement and stage rules, R1/R2; W1 7:20–8:00 and 10:35–11:11, W2 53:00–63:30. The harbor banner changes to blue and lists its own garrison effects at 7:53. Capturing every facility is not required by the stated objective. |
| UO-005 | The game shows predicted damage for both sides of a proposed clash before confirmation. If a nearby ally is eligible, the game allows switching the opposing matchup before it settles. | Observation | Corroborated | High | P2 basic tip 6, P4 encounter/switch, W1 11:11 and W2 around 65:00. W1's bridge preview shows 21 and 1 damage. The alternative action is documented without asserting that it was used in this particular confrontation. |
| UO-006 | An encounter runs automatically. When a fighter's turn comes, active skills consume their AP; eligible event reactions spend separate PP. An ordered list of applicable Tactics conditions supplies choices and targets. | Observation | Corroborated | High | P2, P3 formation and Tactics examples, P4 battle skills and priorities; W1 10:44–10:50 and 19:05–19:17 show resolving encounters. Player changes to individual Tactics rows were not established. |
| UO-007 | Field stamina is charged by battles. The rule blocks movement at zero and offers stationary Rest, which exposes a resting unit to attacks. A friendly command post lists no stamina consumption and steady stamina recovery for its garrison. | Observation | Corroborated | High | P4 stamina, R1/R2, W1 10:35–11:11 displays stamina and facility effects. The zero-stamina and vulnerable Rest endpoints are documentary, not a deliberately failed route in W1. |
| UO-008 | Defeating Aubin ends Call to Action without a separate exit pickup or all-enemy requirement. Exceeding the limit or losing the allied command post is a failure route. | Observation | Corroborated | High | P4 stage and failure rules, R1/R2, W1 20:10–20:42 and W2 65:00–65:30. W1 shows 78,882 before conversion; both runs continue after defeating Aubin. |

## Basic data

- Analysis target: `PLAT-NINTENDO-SWITCH`, native retail Nintendo
  Switch release, English, 8 March 2024.
- Developer: Vanillaware. Publisher on the US listing: SEGA.
- Mechanical families: `FAM-009`, tactical forecast and counterplay;
  `FAM-015`, agent routing and coordination.
- Checked: 2026-11-23.
- P1: [Nintendo commercial product listing](https://www.nintendo.com/us/store/products/unicorn-overlord-switch/).
  Product, availability, supported English language and release date.
- P2: [ATLUS official Basic Tips booklet](https://unicornoverlord.atlus.com/media/pdf/unicorn_overlord_tips.pdf).
  Basic Tips 2–7 and the formation leaves cover leader effects, Valor,
  skill differences, previews, exchanges with nearby allies and rows.
- P3: [ATLUS official Advanced Tactics booklet](https://unicornoverlord.atlus.com/media/pdf/unicorn_overlord_tips_v2.pdf).
  Ordered activation examples distinguish a required full column from
  a target preference and fallback.
- P4: [SEGA official stage and combat system](https://asia.sega.com/unicorn-overlord/kr/system/stage-battle/),
  Korean page. The documented field, encounter, resource and priority
  rules were cross-checked against the English booklet and interface.
- R1: [NightlyGamingBinge Call to Action guide](https://nightlygamingbinge.com/unicorn-overlord-call-to-action-walkthrough/).
  Mission conditions, route via the harbor and final encounter.
- R2: [Neoseeker Call to Action route](https://www.neoseeker.com/unicorn-overlord/Call_to_Action).
  Independent stage order, route alternatives, harbor and Aubin.
- W1: [JRPG Millennial's attributed Nintendo Switch run](https://www.youtube.com/watch?v=aomECnM5sXM&t=275s),
  16 August 2024. Main formation, field, damage and clear evidence.
- W2: [Handheld Players' attributed Nintendo Switch launch run](https://www.youtube.com/watch?v=mNc0qfqPbHA&t=2495s),
  8 March 2024. Separate commercial route, clear at about 65:30 and
  Cornia travel by 74:30; post-clear unit expansion is outside the scope.

## Mechanical decomposition

### Action Genes

- ACT-189: select a deployed unit and send it to a point, facility or
  enemy through continued autonomous field movement.
- ACT-870: assign individual members to a unit's front and back
  slots before it fights as one field agent.
- ACT-871: choose an eligible nearby allied unit to fight a contact
  in place of the unit that initiated it, before confirming combat.

### System Behaviour Genes

- SYS-1896: share battle-stage Valor between deployment from a
  friendly position and class-provided field skills. Success in
  battle adds to the pool.
- SYS-1897: run the automatic encounter in action order, applying
  the combatant's preset tactics. Active choices and triggered
  responses use separate per-character stocks.
- SYS-1898: spend field stamina on encounters outside protected
  positions, restrict movement when it is exhausted and restore it
  by resting or at a suitable garrison. Vulnerable Rest is distinct
  from the protection of a friendly command post.

### Constraint Genes

- CON-068: finish the required fight before the stage
  countdown expires. Loss of the allied command post can independently
  end the attempt even before the time limit.

### Information Genes

- INF-607: show projected damage for a whole proposed automatic
  exchange before the selected pairing is committed.

### Objective Genes

- OBJ-329: defeat the named commander to trigger Stage Clear, with
  no extra exit token. The commander is one required target identity;
  his squadmates and other field contacts are part of the route.

### Time Genes

- TIM-003: issue map orders while march, contact and elapsed stage
  time continue. The real-time field includes a pausable command
  state; the inside of a contact is a separate automatic sequence.

## Reproducible transitions

| State | Action or event | Result | Evidence |
| --- | --- | --- | --- |
| Call to Action setup with three eligible units | Inspect the unit-organization prompt, then fill the second slot of Alain's unit and prepare the other pairs | The unit view displays 2/2 for Alain, Lex and Josef's units in W1 | UO-001, UO-002 |
| Friendly home post and available Valor | Deploy from that position and give the unit a destination along the coastal road | The stage reserve is debited and the selected agents travel separately on the live map | UO-003, UO-004 |
| Road to the harbor and hostile facility | Move toward the port and resolve the local opposition | The facility appears friendly. The force can operate from a second nearby position | UO-004, UO-007 |
| An enemy on the bridge road and more than one unit nearby | Inspect the proposed damage. Keep the original matchup or consider an eligible substitute | The preview changes with the chosen pairing by the documented rule. W1's shown bridge matchup forecasts 21 versus 1 damage | UO-005 |
| The fight is confirmed | Let the encounter run | Ordered active actions and qualifying reactions settle automatically. The field returns with changed HP and stamina | UO-006, UO-007 |
| Aubin's position is still hostile and the allied post survives | Reach and defeat the commander before time expires | Stage Clear appears, followed by the score-to-award settlement and post-battle handoff | UO-008 |

## Strategic and experiential structure

The field and the encounter expose different control surfaces. Move
the prepared whole unit into a position where it can make contact,
protect a friendly point or become an alternate attacker. Read the
whole-exchange forecast while a different pairing is still possible.
After committing, individual skill choices come from each fighter's
preset conditions rather than real-time button inputs. That makes
the arrangement of two early fighters and the routing of their shared
field position different decisions.

## Replay and variation

The two recordings agree on the mission goal and settlement and
differ in local movements and fights. A long route or repeated narrow
wins can reduce the field margin even while the commander survives.
The observation establishes a completed representative route, not a
required clear of both bridges or every enemy. The exact clock
duration, pause duration, damage margin and award count are not
promoted to invariants.

## Adjacent systems and history

Fort Soligie introduces an expansion to three members after the scope.
Optional items and later classes alter the available pairings and add
field commands. The retained story world after the clear is evidenced
in W2, but neither later fights nor save/reload are evaluated here.

## Normalised genome

| Type | Stable genes | Role |
| --- | --- | --- |
| Action | ACT-189, ACT-870, ACT-871 | Order a field destination, compose a row formation and select an eligible substitute |
| System Behaviour | SYS-1896, SYS-1897, SYS-1898 | Allocate Valor, run the autonomous encounter and account for field stamina |
| Constraint | CON-068 | Lose at terminal expiry before the mission finishes |
| Information | INF-607 | Inspect a projected exchange before battle |
| Objective | OBJ-329 | Defeat Aubin and receive the clear |
| Time | TIM-003 | Issue field orders during ongoing real-time progress |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `657` (`GAME-0001`–`GAME-0657`).
- Exact genome matches: none.
- Tied near matches: `GAME-0376` — Katamari Damacy REROLL (`2 / 16 = 0.125000`).
- Supported combination subsets: none.
- Scan date: 2026-11-23.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
| --- | --- | --- | --- |
| [Katamari Damacy REROLL (GAME-0376)](../g-l/katamari-damacy-reroll.md) | CON-068, TIM-003 | Both accept live decisions before a terminal deadline. Katamari rolls one directly controlled body and gains access through size. Unicorn Overlord gives separate orders to composed units and confirms an automatic exchange before defeating a named commander. | Near, `0.125000` |

Bad North is a design comparison for commanding autonomous squads
on a clock. An order brings units to contact in both games. The
scoped Unicorn Overlord stage additionally exposes the damage
forecast and the option to change which nearby formation fights.

## Taxonomy impact

ACT-870 assigns individual fighters to persistent positional slots
inside one field entity. ACT-317 applies a geometry and stance to a
selected field group and ACT-651 deploys roster members on starting
panels. ACT-871 replaces the whole attacking unit at a pending
contact, rather than issuing a fresh march order about the map or
rotating a character within the unit. INF-607 supports that choice
but does not execute it. INF-190 and INF-473 respectively accompany
a Civilization VI unit's field commands and forecast the effect of an
addressed shot, not the entire automated matchup.

SYS-1896 changes the stage reserve across field actions, SYS-1897
runs the separate engagement and its AP/PP budgets, and SYS-1898
changes the returning unit's ability to keep moving. SYS-388's
randomized initiative and per-turn refresh are not asserted. CON-068
captures the deadline while OBJ-329 captures the commander objective.
The single worm in Mischief Makers and Aubin's field unit differ
in presentation, but both stages settle on defeat of the designated
adversary without collecting an exit token.

## Negative results

- Winning one exchange need not defeat Aubin or clear the stage.
- The visible Valor Skill tutorial does not prove a cast in W1, and
  the Switch command's availability is distinct from its use.
- No numerical threshold for nearby substitution, random-stream
  model, score formula or evidence of identical Switch builds is
  claimed. Two fighters per unit applies to the observed start only.

## Delta summary

Ten scoped genes, including six additions and four reused definitions.

## New facts

- A unit's two rows have individually addressable slots before it
  moves and fights as one map entity.
- A nearby eligible alternate can replace the initiator of a contact
  after discovery and before the fight commits.
- A unit may still have AP in its next battle but lack the field
  stamina to continue marching from its current position.

## Principles and design implications

Give players one decision about which soldiers belong together and a
later decision about which entire group engages. Expose the latter
outcome while switching is still possible. Budget the next field
movement separately from the ability to act once combat has begun.

## Puzzle or game generation potential

Offer two prebuilt pairs, one defended bridge and a captured rest
point. Preview the damage for each eligible pair. Ask the player to
finish the command objective with enough stamina to reach it before
the stage timer expires.

## New genes

- ACT-870
- ACT-871
- SYS-1896
- SYS-1897
- SYS-1898
- INF-607

## New combinations

None. The full signature satisfies none of the 274 verified combinations.
No existing support list changes.

## Taxonomy changes

[TAXONOMY_CHANGE_404](../../../research/taxonomy-changes/TAXONOMY_CHANGE_404.md).

## New questions

What exact position makes a substitution eligible? Which off-map
edits are permitted before contact and which are allowed from a
garrison? How do different priority and targeting edits change an
otherwise identical forecast?

## Next recommended game

Ristar on the English North American commercial Sega Genesis
cartridge. Trace one complete early Flora act through an arm grab,
a verified release or throw and the playable boundary after the clear.

## Why this game

The same fight links preassembled rows, a live field with finite
stamina, forecast-led choice of who fights, and a separate automatic
resolution. Each can be isolated on the way to one visible result.
