---
game_id: GAME-0625
slug: ninja-gaiden-dragon-sword
game_title: "Ninja Gaiden Dragon Sword"
analysis_status: reviewed
reviewed: 2026-11-21
combination_ids: []
gene_ids:
  action:
    - ACT-008
    - ACT-437
    - ACT-831
  system:
    - SYS-1826
  constraint: []
  information:
    - INF-179
  objective:
    - OBJ-336
  time:
    - TIM-003
---

# Game: Ninja Gaiden Dragon Sword

This analysis uses the [canonical vocabulary](../../../docs/ARCHITECTURE.md#canonical-vocabulary).

## Analysis scope

- Version / ruleset: English North American commercial Nintendo DS release,
  shipped March 25, 2008. The retail product is NTR-YNGE-USA. The reference
  recording identifies the US version. The specific cartridge revision and
  the recording's input hardware are unverified.
- Primary decision loop: steer Momiji around the arena with the stylus, cross
  the opponent's screen position with a stroke to request a slash, and use a
  held guard or local movement to manage incoming attacks. Continue until the
  exercise closes and returns ordinary forest control.
- Entry: the first controllable practice bout with Ryu in the shallow pool at
  the waterfall, as confirmed by the live playfield beside the map.
- Exit: the authored interruption after the spar, followed by Momiji standing
  alone on the forest path under ordinary control before the first hostile
  group. An adjacent tutorial prompt corroborates the slash control.
- Included: paired screen information, local movement, grounded slashing,
  physical-button guard, real-time sparring and its automatic story transition.
- Excluded: the later hostile route as its own loop, ranged attacks, named
  aerial techniques, saving, essence economy, the dragon encounter, Ninpo,
  later difficulties and all other Ninja Gaiden releases.
- Suggested later scope: follow the first separately entered hostile group
  through its own combat and continued path access, or isolate the first
  documented Ninpo unlock and use in a later chapter.

## Direct-play status

No direct play was performed. Tecmo's shipping notice and original printed
manual establish the platform and controls. The US-version recording was
reviewed through static storyboard frames. Two independent commercial-era
written routes describe the opening exercise and the subsequent handoff.
The frames establish the progression and visible feedback. They do not show
physical input, exact attack geometry, frame timing, or every exit predicate.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
| --- | --- | --- | --- | --- | --- |
| NGD-001 | The analysed product is the North American Nintendo DS retail game, shipped March 25, 2008. Capture metadata identifies the USA version, without exposing an exact program revision. | Confirmed | Corroborated | High | P1; P2; R1; W1 recording description. |
| NGD-002 | The rotated DS pairs a touch playfield with the Forest of Shadows map. Touching a point in the live scene away from the opponent directs local movement. The two combatants are visible together during the bout. | Observation | Corroborated | High | P1; P2, Action section, printed pp. 15–16; W1 3:10–3:50. Frames do not reveal the physical contact. |
| NGD-003 | A stylus stroke across an opponent on the touch playfield requests a sword slash. Point contact elsewhere on the same playfield can direct movement. The first subsequent forest prompt independently displays the slash gesture. | Observation | Corroborated | High | P2, printed pp. 15–16; W1 5:00–5:20; W2, Basic Controls and Forest of Shadow. |
| NGD-004 | The button-held guard is a distinct input from stylus steering and slashing. During practice it provides a defensive response to eligible attacks. The exact list of blocked moves in this bout was not isolated. | Observation | Corroborated | High | P2, printed pp. 15–16; W2, opening practice explanation; W1 6:30 displays the related subsequent guard prompt. |
| NGD-005 | The opening exercise accepts live actions without requiring Ryu to be defeated. Both firsthand routes describe the opponent as unhurtable during practice and a transition after a short period. Their reports do not establish a universal exact timeout or rule for every difficulty. | Observation | Corroborated | Medium | W2 and W3 describe practice, no ordinary opponent defeat and automatic progression. W1 3:10–4:10 shows the live bout ending in a scene with both fighters still present. |
| NGD-006 | The authored interruption closes the exercise. The recorded route restores ordinary Momiji control on the forest path, with Ryu absent and no opponent victory claim or retry. | Observation | Corroborated | High | W1 4:00–4:50; W2 and W3 place forest movement after the practice and narrative transition. |

## Basic data

- Analysis target: `PLAT-NINTENDO-DS`.
- Developer: Team Ninja. Publisher: Tecmo.
- Mechanical family: `FAM-010`, real-time system pressure.
- Checked: 2026-11-21.
- P1: [Tecmo's North American shipping announcement](https://www.nintendoworldreport.com/pr/15608/tecmo-ships-ninja-gaiden-dragon-sword-for-ds), reproduced as a publisher press release.
- P2: [Scan of the original English instruction booklet](https://romtail.net/wp-content/uploads/2025/06/nintendo-ds-manual-Ninja-Gaiden-Dragon-Sword.pdf), Action, printed pp. 15–16. The document describes the ordinary input scheme using Ryu.
- R1: [North American retail product listing](https://gamefaqs.gamespot.com/ds/938848-ninja-gaiden-dragon-sword/data), corroborates the region, date and NTR-YNGE-USA identifier.
- W1: [KAGE-008's recorded USA-version opening](https://www.youtube.com/watch?v=lMDjZTDYBC4&t=190s), hosted by LongplayArchive. Static frames show the active spar, its closure and resumed movement at 3:10–4:50. The 5:00 still corroborates the slash prompt outside the bout.
- W2: [Sephirosuy's DS route](https://gamefaqs.gamespot.com/ds/938848-ninja-gaiden-dragon-sword/faqs/52309), Basic Controls and the lead-in to Chapter 1.
- W3: [VampireHorde's DS route](https://gamefaqs.gamespot.com/ds/938848-ninja-gaiden-dragon-sword/faqs/52270), opening practice and Chapter 1.

## Mechanical decomposition

### Action Genes

- ACT-008: direct Momiji within the active scene through the contact location.
- ACT-437: hold a physical control for a sustained guard during the bout.
- ACT-831: cross the visible opponent with the stylus to request a sword slash.

### System Behaviour Genes

- SYS-1826: close a live practice encounter by script while the opponent
  stays ineligible for ordinary defeat, then return ordinary route control.

### Constraint Genes

No separate constraint is added. The special defeat boundary belongs to
SYS-1826 and is not claimed for later hostiles.

### Information Genes

- INF-179: the side-by-side presentation exposes the current encounter and
  local field, with a separate mapped route as the exercise ends.

### Objective Genes

- OBJ-336: reach the accepted handoff from practice to the ordinary route
  without needing to defeat the scripted instructor.

### Time Genes

- TIM-003: actions and the practice opponent run in live time within the
  bounded bout. Its exact time threshold is not asserted.

## Reproducible transitions

| State | Input or event | Result | Evidence |
| --- | --- | --- | --- |
| Opening pool encounter | Direct local stylus contact away from the opponent | Momiji changes position while the opponent remains active | NGD-002 |
| Opponent visible in the local playfield | Cross the opponent with a stylus stroke | The game requests a sword slash, without making the practice opponent ordinarily defeatable | NGD-003, NGD-005 |
| Opponent threatens a strike | Hold a physical guard control | An eligible strike can be guarded without using a slash gesture | NGD-004 |
| Practice exchange is live | Let the authored encounter transition occur | A scene interrupts play with both fighters still present | NGD-005, NGD-006 |
| The scene ends | Resume local movement | Momiji proceeds on the forest route under ordinary control | NGD-006 |

## Strategic and experiential structure

Local position matters in two ways. It changes distance from the practice
opponent and changes where the player must draw the slash on the touch
playfield. Holding guard is a different request from making that stroke.
Staying active through the exercise leads to a story handoff. Taking the
successor path is possible even though the practice opponent was never
defeated. This remains distinct from the later tutorial fights and their
normal hostile damage.

## Replay and variation

Both firsthand routes end the exercise without claiming a victory over
Ryu. They describe elapsed play qualitatively. The US recording shows
Momiji changing position and the same onward story handoff. Starting
another slot, deliberately losing all health and pausing during the
exercise were not reproduced. No replay, exact timeout or defeat
semantics are inferred for those unmeasured branches.

## Adjacent systems and history

The original booklet's paired-screen layout and native controls describe
this Nintendo DS release. The later forest section introduces ranged and
aerial actions in its own context, and the booklet explains Ninpo for
eligible later use. This early spar does not establish any of those
progression conditions. The ordinary route resumes before the first
hostile tutorial group.

## Normalised genome

| Type | Stable genes | Role |
| --- | --- | --- |
| Action | ACT-008, ACT-437, ACT-831 | Steer locally, hold guard or cross the opponent to slash |
| System Behaviour | SYS-1826 | Automatically end the non-victory practice bout |
| Constraint | None | The instructor's defeat rule is part of the authored handoff |
| Information | INF-179 | See both fighters, the local field and the route map |
| Objective | OBJ-336 | Reach resumed control on the ordinary forest route |
| Time | TIM-003 | Respond in live time before the encounter closes |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `624` (`GAME-0001`–`GAME-0624`).
- Exact genome matches: none.
- Tied near matches: `GAME-0550` — Ghost of Yōtei (`3 / 13 = 0.230769`); `GAME-0615` — Skate Story (`3 / 13 = 0.230769`).
- Supported combination subsets: none.
- Scan date: 2026-11-21.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
| --- | --- | --- | --- |
| [Ghost of Yōtei (GAME-0550)](../g-l/ghost-of-yotei.md) | ACT-008, ACT-437, TIM-003 | Both support live movement and sustained guard. The Ghost of Yōtei packet answers real hostile pressure and moves into the next story beat after combat. The DS spar lets the player trace an attack through the visible opponent and continues without requiring an ordinary defeat. | Near, `0.230769` |
| [Skate Story (GAME-0615)](../s-z/skate-story.md) | ACT-008, INF-179, TIM-003 | Both use local movement and visible feedback while a scene continues to run. Skate Story checks the taught Ollie at four marked crests before opening the portal. The spar uses the crossing gesture to attack and advances through an authored interruption without a target quota. | Near, `0.230769` |

## Taxonomy impact

[TAXONOMY_CHANGE_371](../../../research/taxonomy-changes/TAXONOMY_CHANGE_371.md)
records the slash input and non-victory training handoff separately.

## Negative results

- ACT-019 requires selecting an actor and a separately declared ability.
  The crossing gesture directly requests a live attack.
- SYS-1455 repeats a narrowly scripted tutorial action after a mistake.
  The spar instead accepts live exchanges and closes into the forest route.
- OBJ-256 requires an accepted knockout or boxing decision. No such verdict
  is the practice objective.
- Later printed Ninpo controls do not establish its use within this bout.

## Delta summary

Adds the first controllable exercise in the US retail Nintendo DS release
through its observed transition to the ordinary Forest of Shadows path.

## New facts

- The native input scheme separates a target-crossing sword stroke from
  held local movement and button-held guard.
- The first live practice bout resolves into an authored interruption without
  an ordinary opponent defeat. Local path control visibly resumes afterward.

## New genes

ACT-831, SYS-1826 and OBJ-336.

## New combinations

None.

## Taxonomy changes

[TAXONOMY_CHANGE_371](../../../research/taxonomy-changes/TAXONOMY_CHANGE_371.md).

## New questions

Which first hostile group admits ranged throws and the same grounded slash
before releasing the route? Its settlement needs an independent scope.

## Next recommended game

Continue with Fuga: Melodies of Steel on Xbox Series X|S and its first
verified complete tank battle.

## Why this game

The combat tutorial makes the input gesture and accepted progression condition
especially clear. The player can practise a real attack without a victory
over the instructor being the route's acceptance condition.
