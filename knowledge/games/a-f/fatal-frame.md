---
game_id: GAME-0591
slug: fatal-frame
game_title: Fatal Frame
analysis_status: reviewed
reviewed: 2026-11-21
combination_ids: []
gene_ids:
  action:
    - ACT-008
    - ACT-341
    - ACT-502
    - ACT-789
  system:
    - SYS-045
    - SYS-215
    - SYS-1740
    - SYS-1741
  constraint:
    - CON-402
    - CON-578
  information:
    - INF-142
    - INF-557
    - INF-558
  objective:
    - OBJ-080
  time:
    - TIM-003
---

# Game: Fatal Frame

Use the [canonical vocabulary](../../../docs/ARCHITECTURE.md#canonical-vocabulary).
Investigate Himuro Mansion as Mafuyu. Frame the ghost that attacks
after you find the notebook, then return through the cleared doorway.

## Analysis scope

- Version / ruleset: English North American PlayStation 2 base retail
  `SLUS-20388`, first issue dated 4 March 2002. Start a fresh ordinary
  Normal game, with the introductory camera and Type-14 film. Exact
  disc revision and hardware or emulator parity for recorded traces
  are unverified.
- Structured analysis target: PLAT-PLAYSTATION-2.
  See [platform coverage](../../platforms/games.json).
- Entry: first direct control of Mafuyu Hinasaki at the Entrance in the
  black-and-white Himuro intro, before entering Rope Hallway.
- Primary decision loop: follow the accessible rooms to the Fireplace
  Room balcony and examine the notebook. When Bound Man approaches,
  raise Camera Obscura to Finder View, align the Capture Circle and
  keep the ghost inside it to accumulate power. Decide between an
  earlier shot and the riskier approach window. Each shutter uses film.
  Lower the finder and move if the ghost closes in without a safe shot.
- Positive exit: defeat Bound Man, descend to the reopened Rope Hallway
  door, cross and follow the hall until the automatic interlude. Confirm
  control of Miku at the beginning of the first night, then stop.
- Negative exit: a missed or weak exposure can waste finite film and leave
  Bound Man active. The spirit can reach attacking distance. The manual
  documents a zero-strength game over for Miku; the precise terminal and
  recovery behavior for failure in Mafuyu's intro were not independently
  verified. The automatic story handoff is part of the successful route.
- Included: ordinary movement, room actions and notebook trigger,
  entering and leaving the finder, finite Type-14 film, proximity
  feedback, framing, charge and decay, ordinary and timed shots, hostile
  response and the cleared return route. Optional spirits are contrasted
  only to distinguish a detection cue from required combat.
- Excluded: scoring and completing the Ghost List, pursuing all optional
  spirit photos, using save or film restock fixtures, upgrade and bonus
  abilities, exact frame/charge/damage coefficients, later nights,
  postgame modes, the Xbox edition, other regions and the sequels.
- Potential scoped module: Miku's first-night screen and hidden doorway
  investigation with photo clues and mandatory combat.
- Direct-play status: no native input or game execution. Tecmo's
  English booklet and in-game tutorial establish the camera rules.
  Two NTSC-U-attributed PlayStation 2 captures and written play
  accounts establish the complete introductory route. User presses
  and transient attack frames between sampled stills remain
  unverified. Video and audio were not played.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
| --- | --- | --- | --- | --- | --- |
| FF-001 | The first North American Tecmo retail game is PS2 NTSC-U/C, SLUS-20388, released March 2002. The English intro starts with Mafuyu inside Himuro Mansion and hands off to Miku in the first night. | Confirmed | Direct | High | P1, P2, R1, R2; W1 0:10/2:10/8:10/8:50 |
| FF-002 | Mafuyu proceeds through the Entrance and Rope Hallway into the Fireplace Room. Examining the notebook on the balcony triggers Bound Man and the shooting tutorial. Earlier non-hostile spirits do not substitute for the required battle. | Observation | Corroborated | High | R1, R2; W1 3:10/3:30/4:10/5:40; W2 4:40/8:10/9:40 |
| FF-003 | The Filament reacts in exploration or the finder. A hidden spirit or clue can produce blue; a moving spirit can produce amber. Strength helps locate the stimulus; amber alone does not distinguish a fleeting ghost from an attacker. | Observation | Corroborated | High | P1 pp. 8–10; R1, R2; W1 3:40 and 5:50 |
| FF-004 | The camera button switches between ordinary field movement and first-person finder aim. The shutter exposes the currently framed scene using available film; an off-target exposure does not produce the charged hit. Type-14 is the introductory film and stock is shown. | Observation | Corroborated | High | P1 pp. 5, 8–10, 28–29; R1, R3; W1 5:40/5:50; W2 10:00/10:10 |
| FF-005 | Framing a spirit inside the Capture Circle charges power. When the spirit is out, charge falls rather than continuing automatically. Shutter damage on a valid subject depends on accumulated charge. The finder shows target, charge, player and ghost condition and film. | Confirmed | Direct | High | P1 pp. 8–10; W1 5:40/5:50 |
| FF-006 | When Bound Man lunges, the camera offers a short attack window. A correctly framed, fully charged shutter during the amber window can damage, interrupt and knock the ghost back. A normal shot or missed window can leave another approach to manage. Neither recording isolates the required inputs at frame precision. | Observation | Corroborated | Medium | R1 Intro and Finder guide; R2 Prologue; R3 shot descriptions; W1 5:50/6:00 |
| FF-007 | Defeating Bound Man reopens the return door. Mafuyu descends, re-enters Rope Hallway and triggers the transition to Miku's first night. The interlude is not evidence of a combat failure. | Observation | Corroborated | High | R1, R2; W1 6:10–6:50/8:10/8:50; W2 10:20/11:20/11:30 |
| FF-008 | Remaining film and an active ghost constrain retrying a shot. The booklet gives Miku's zero-strength game over and recovery from a prior save, but the prologue sources do not isolate Mafuyu's equivalent exit or a zero-film recovery on this route. | Observation | Limited | Medium | P1 pp. 6–10 and 18–19; R1, R3; W1/W2 successful routes |

## Basic data

- Tecmo. FAM-010 applies because the threat moves during aiming and the
  useful exposure depends on charge and hostile timing. Longer waiting can
  make the shot stronger or leave too little time to retreat.
- P1: [Tecmo's original English PlayStation 2 booklet](https://manualmachine.com/gamesps2/fatalframe/1116589-user-manual/),
  cover and controller chart, startup and game-over descriptions,
  finder HUD, battle rules, film glossary. The battle pages describe
  both gain and decay of charge. The game-over passage names Miku.
- P2: [First-issue North American disc and packaging scans](https://crimson-ceremony.net/lostreleases/item.php?id=pzgame_pz1-ps2-usa1).
  The disc carries SLUS 20388. The catalogue distinguishes the first
  issue from the later package. See also the
  [North American release record](https://gamefaqs.gamespot.com/ps2/529305-fatal-frame/data).
- R1: [Chozo Abigaba's original-game guide](https://gamefaqs.gamespot.com/ps2/529305-fatal-frame/faqs/21774),
  Intro, finder cues, shot timing and difference between ghost classes.
- R2: [J. Williams's PlayStation 2 walkthrough](https://gamefaqs.gamespot.com/ps2/529305-fatal-frame/faqs/16695),
  Prologue. The notebook, confrontation, switch back to the field
  to regain space and reopened door corroborate the route. The guide's
  colour descriptions are read alongside the manual, not promoted to
  numerical timing.
- R3: [NuConcept's May 2002 Camera FAQ](https://gamefaqs.gamespot.com/ps2/529305-fatal-frame/faqs/17028),
  typed film and charge, common full-charge timing and special shot
  vocabulary. The guide calls the counter a Zero Shot. The scoped
  claim is the condition and interruption rather than a universal label.
- W1: [Spazbo4's US PS2 route](https://www.youtube.com/watch?v=sMldob3s3To).
  Stills show opening title at 0:10, room sequence at 2:10–3:30,
  notebook at 4:10, tutorial at 5:40, blue Capture Circle and ghost
  at 5:50, ordinary movement after the encounter at 6:10–6:50,
  first-night chapter card at 8:10 and Miku moving at 8:50–9:00.
- W2: [TurkishBullet19's English US Normal route](https://www.youtube.com/watch?v=B6nyZq8yR7E).
  The 4:40 Child Behind photograph and continued movement contrast
  non-hostile capture with the notebook at 8:10, tutorial at 9:40,
  timed samples in the finder at 10:00–10:10 and walking away
  after clearing the confrontation at 10:20. The two captures
  corroborate the sequence without fixing the number of exposures.
- Sources accessed 2026-11-21.

## Mechanical decomposition

### Action Genes

- ACT-008 moves Mafuyu through the Entrance, hallway and balcony and
  helps him regain space between shots. ACT-341 opens the reached doors
  and inspects the notebook to trigger the confrontation (FF-002).
- ACT-789 enters or leaves the first-person optical control state.
  ACT-502 spends a separate shutter action on the current frame
  (FF-004, FF-005).

### System Behaviour Genes

- SYS-045 advances Bound Man toward Mafuyu while the encounter runs.
  SYS-215 resolves the real-time exchange of in-range attacks and
  directed camera hits (FF-005, FF-006).
- SYS-1740 charges only while the ghost stays framed and loses charge
  when framing is broken. Its output is read when a valid shutter
  exposes the subject (FF-005).
- SYS-1741 adds a counter branch for a fully charged shot on the
  approaching ghost during the lunge cue. Disruption can return
  breathing room. Full charge and the moment of vulnerability are
  distinct prerequisites (FF-006).

### Constraint Genes

- CON-402 closes the return route during the mandatory ghost encounter.
  Clearing Bound Man permits the same authored doorway again (FF-007).
- CON-578 represents the finite compatible film paid to expose the
  frame. There is an early Type-14 pickup, but save-point restocking
  and exact supply ceilings are outside the packet (FF-004, FF-008).

### Information Genes

- INF-142 conveys the lunge timing through the ghost and the short
  special-shot prompt (FF-006).
- INF-557 gives a qualitative direction and stimulus-class cue even
  before successful framing. It is not a target lock (FF-003).
- INF-558 exposes charge, target framing, bodies' remaining condition
  and film in the live finder. A visual aiming opportunity and a
  sufficient amount of charge are separate readouts (FF-005, FF-006).

### Objective Genes

- OBJ-080 requires defeating Bound Man and crossing the restored exit
  to settle the intro. Defeat alone is not the handoff to Miku (FF-007).

### Time Genes

- TIM-003 captures the live approach and decision pressure in the
  finder: the spirit continues moving while the player aims or waits
  for power and a vulnerable moment (FF-005, FF-006).

## Reproducible transitions

| Initial state | Intervention | Discriminating result | Evidence |
| --- | --- | --- | --- |
| Control of Mafuyu at the Entrance | Take the accessible passage through Rope Hallway toward the Fireplace Room | The introductory route is navigable without photographing every optional apparition. | FF-001, FF-002 |
| A clue or roaming spirit provokes the Filament | Turn toward the stronger cue and raise the finder | The direction and class cue precede capture eligibility. An optional subject can be photographed without initiating the guardian fight. | FF-002, FF-003, FF-004 |
| The fireplace balcony notebook is within reach | Examine it | The cutscene leads to Bound Man and the shooting tutorial. | FF-002 |
| Bound Man approaches out of shot | Raise the finder and bring him into the Capture Circle | The camera gains power while the spirit stays framed. Letting it leave drains the charge. | FF-004, FF-005 |
| A valid target is framed during the approach | Take a standard shutter or wait for a fully charged lunge opportunity | A valid exposure costs film and does damage. The specially timed hit can push the spirit back. If the opportunity is lost, dropping the finder gives room to move and try again. | FF-004–FF-006 |
| Bound Man is still active | Use another valid exposure if necessary, avoiding another approach | Defeat ends the encounter. Door access returns; shot count depends on timing and damage. | FF-006, FF-007 |
| The balcony fight has ended | Descend and cross into Rope Hallway; follow the passage until the interlude | The first-night card and ordinary Miku control follow. Stop at that handoff. | FF-007 |

## Strategic and experiential structure

The direction cue is useful before the camera can deal damage. Keeping
the spirit framed makes the future shot stronger, but staying aligned
costs time while it closes in. The player can take the shot sooner,
risk the closer counter window or lower the camera and set a new angle
before the next exposure. The finite film makes a photograph of empty
space mechanically different from waiting or moving.

## Replay and variation

The two captures take different optional photography paths and spend
different amounts of time exploring. Both reach the notebook encounter,
cleared exit and scripted continuation. The examples establish neither
an exact shot count nor identical control timing on every disc revision.
No optional spirits, scores, retries or postgame modes are required
for acceptance.

## Adjacent systems and history

Luigi's Mansion also turns near-ghost perception and timing into
a defensive action, but commits to counter-steered suction after exposing
a vulnerable heart. Here the shutter converts charge accumulated by
framing into immediate damage. Pokémon Snap concerns framed photos and
finite film but evaluates captured scenes after a moving excursion; its
subjects do not force the same live approach-versus-charge decision.

## Normalised genome

| Type | Active gene IDs | Carrier parameters |
| --- | --- | --- |
| Action | ACT-008, ACT-341, ACT-502, ACT-789 | locomotion, local interaction, optical mode switch and shutter |
| System Behaviour | SYS-045, SYS-215, SYS-1740, SYS-1741 | autonomous approach, live exchange, in-frame charge and lunge counter |
| Constraint | CON-402, CON-578 | sealed return doorway and finite compatible exposures |
| Information | INF-142, INF-557, INF-558 | lunge timing, Filament and finder readouts |
| Objective | OBJ-080 | Bound Man clearance and opened return route |
| Time | TIM-003 | real-time movement during framing and combat |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `590` (`GAME-0001`–`GAME-0590`).
- Exact genome matches: none.
- Tied near matches: `GAME-0532` — Hades II (`7 / 31 = 0.225806`).
- Supported combination subsets: none.
- Scan date: 2026-11-21.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
| --- | --- | --- | --- |
| Hades II (GAME-0532) | ACT-008, ACT-341, CON-402, INF-142, OBJ-080, SYS-215, TIM-003 | Both read live attack cues, clear a mandatory hostile and traverse the opened next passage. Hades II spends Magick on channeled staff actions and resolves Hecate’s phases; Fatal Frame accumulates power by framing a moving ghost and spends film per exposure. | 7 shared of 31 in union, 0.225806 (22.58%) |

### Preserved research notes

- New genes: ACT-789, SYS-1740, SYS-1741, INF-557 and INF-558.
- Classification result: New gene.

## Taxonomy impact

- [TAXONOMY_CHANGE_337](../../../research/taxonomy-changes/TAXONOMY_CHANGE_337.md)
  distinguishes optical stance, charge, counter timing and two feedback
  layers. No earlier definitions are revised.

## Negative results

- A detected presence does not mean the ghost is an attacker, already
  framed or captured.
- Holding the finder with a ghost outside the Capture Circle does not
  maintain its charge. A shutter can spend film without solving the
  encounter.
- The scripted disappearance of Mafuyu at the chapter transition is
  not a player defeat, a save checkpoint or a health-based terminal.
- No exact initial film count, damage multiplier, attack frame duration
  or required shot count is inferred. Options such as automatic tracking,
  endless film and bonus camera functions are outside this base route.

## Delta summary

## New facts

- [Observation | Corroborated | High] The mandatory notebook
  confrontation is completed by a live optical hit loop and a
  traversable reopened route.

## New genes

- [Observation | Corroborated | Medium] Five additions in
  TAXONOMY_CHANGE_337.

## New combinations

- [Observation | Corroborated | High] No new verified combination
  proposed. Existing subsets are recorded above.

## Taxonomy changes

- [Observation | Corroborated | Medium] The original labels for earlier
  photographic, visibility and ghost-capture genes are retained.

## New questions

- A controlled retail-disc run could isolate an early miss, a timed
  counter, an empty roll and failure behavior without inferring Miku's
  rules for Mafuyu.

## Next recommended game

- [Hypothesis | Limited | Medium] GAME-0592, Dungeons of Hinterberg on
  Xbox Series X|S. Reproduce an entire early dungeon with local magic.
- Optimisation criterion: contrast temporarily exposing a live target
  with changing the traversal geometry through authored magical rules.

## Why this game

- [Hypothesis | Limited | Medium] The intro puts a time-risk tradeoff
  inside the very act of looking at the danger.
