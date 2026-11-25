# Information Genes

## INF-666 — Preview the accepted surface landing separately from raw aim

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: While the player aims a leap, the interface displays the accepted direction to the current landing point on an eligible surface. That guide can differ from the raw input line before the leap is committed.
- Includes: In Dandara’s opening, the bright direction line and arrow indicate the point on the salt band while the fainter input line can point slightly aside.
- Excludes: An unconditional steering arrow, a route through every later landing, a target marker for the shot and feedback shown only after landing.
- Parameters: Aim input, raw heading, accepted landing, guide direction and pre-release display
- Evidence: [Dandara: Trials of Fear Edition decomposition](../games/a-f/dandara-trials-of-fear-edition.md), DF-003. The official release documentation and the attributed opening captures delimit this rule.
- Novelty: first isolated for `GAME-0738`. See [TAXONOMY_CHANGE_484](../../research/taxonomy-changes/TAXONOMY_CHANGE_484.md). No external novelty claim.

## INF-665 — Pair visible extrusion depth with a fixed face map and target markers

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: One view renders the manipulable wall at its current depths. A separate face map preserves the authored planar layout and marks the goal and local character position. Use the terrain view to read changed treads and the face map to locate the target within the layout.
- Includes: The upper screen in Pullblox Lesson 3 shows the exposed rows. Its lower screen keeps the three-stripe layout, the goal flag and a separate Mallo marker.
- Excludes: A map that encodes the exact volume of every extension, a route overlay predicting correct moves, a camera mode that changes the terrain and a purely decorative preview with no position or goal indication.
- Parameters: Terrain view, planar layout, live position marker, goal marker, top and lower presentation
- Evidence: [Pullblox decomposition](../games/m-r/pullblox.md), PB-002, PB-004, PB-005. The original game manual, attributed Lesson 3 captures and paired release documentation support the bounded behaviour.
- Novelty: first isolated for `GAME-0737`. See [TAXONOMY_CHANGE_483](../../research/taxonomy-changes/TAXONOMY_CHANGE_483.md). No external novelty claim.

## INF-664 — Expose graffiti interaction and distinguish claimed trace nodes

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: A nearby paintable surface shows an interaction cue. In its active trace, the interface distinguishes directional nodes already visited from available nodes and shows the connected trace and the local allowance indicator.
- Includes: Approach the Versum Hill mural until the spray and RB cue appears. During the trace, yellow marks and connecting segments record visited directions and dark nodes remain available.
- Excludes: A full route showing one required command sequence, a fixed view of a finished design, a global list of all district surfaces and an inventory or currency readout.
- Parameters: Surface interaction cue, directional nodes, visited state, connecting trace and allowance display
- Evidence: [Bomb Rush Cyberfunk decomposition](../games/a-f/bomb-rush-cyberfunk.md), BRC-003, BRC-004. The attributed Xbox Series X and PC captures and product documentation support the bounded behaviour.
- Novelty: first isolated for `GAME-0736`. See [TAXONOMY_CHANGE_482](../../research/taxonomy-changes/TAXONOMY_CHANGE_482.md). No external novelty claim.

## INF-663 — Show selected tool uses, remaining pickups and time on the live field

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: The current attempt display identifies the selected limited tool and its remaining uses while separately showing the outstanding collectible count and live time allowance. Switching tools changes which use count is visible without changing the remaining objective.
- Includes: On Toki Tori Forest Falls Level 5, read the selected bridge count or teleport count in the upper left. Read the remaining eggs and countdown separately at the bottom.
- Excludes: An aggregate count of all tools, a count of collected rather than outstanding targets, an inventory-only display and an after-the-fact result screen.
- Parameters: Selected tool, per-tool count, outstanding required pickups, remaining time and live display
- Evidence: [Toki Tori decomposition](../games/s-z/toki-tori.md), TT-002, TT-004–TT-006. The original US cartridge replay and original-version guides support the bounded behaviour.
- Novelty: first isolated for `GAME-0735`. See [TAXONOMY_CHANGE_481](../../research/taxonomy-changes/TAXONOMY_CHANGE_481.md). No external novelty claim.

## INF-662 — Mark the final required hostile before its defeat closes the arena

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: When one required hostile remains, the active arena applies a distinguishable marker to that individual. The cue identifies the target whose removal will trigger the clear, while local optional actions are still available.
- Includes: The last robot in Nex Machina Techno Forest 1-1 gains a magenta highlight before being eliminated and triggering the transition.
- Excludes: A general threat outline on every enemy, an enemy count without identifying the remaining actor and a post-clear banner.
- Parameters: Required hostile set, last remaining member, visual marker, pre-clear interval and outgoing transition
- Evidence: [Nex Machina decomposition](../games/m-r/nex-machina.md), NM-004. Housemarque’s published v1.05 rules and annotated opening captures establish the bounded behaviour.
- Novelty: first isolated for `GAME-0734`. See [TAXONOMY_CHANGE_480](../../research/taxonomy-changes/TAXONOMY_CHANGE_480.md). No external novelty claim.

## INF-661 — Show one local stamp tally against both task supply and the ride requirement

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: The card displays the same credited local count against the total number of stamp opportunities and against a separate smaller travel requirement. The player can tell when departure is eligible while some opportunities remain.
- Includes: The TOEM Homelanda card shows one of three available stamps and one of one required for the bus after Nana’s request.
- Excludes: A sole mandatory mission quota, unrelated resource counters, enumerating every uncompleted task and displaying a travel option without revealing its threshold.
- Parameters: Region, credited stamp count, available count, travel requirement and update after settlement
- Evidence: [TOEM decomposition](../games/s-z/toem.md), TE-002, TE-005, TE-006. The developer’s account and recorded PS5 play establish the scoped sequence.
- Novelty: first isolated for `GAME-0732`. See [TAXONOMY_CHANGE_478](../../research/taxonomy-changes/TAXONOMY_CHANGE_478.md). No external novelty claim.

## INF-660 — Reveal reserve-host identities by a brief flash in the active maze

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: The game transiently singles out reserve-bearing objects among ordinary-looking terrain. The marked objects can be targeted while they still hold the reserve, but their marker can disappear before the player acts.
- Includes: Opening flashes identify those blocks that contain Sno-Bee eggs in the Pengo maze. The player can remember their locations and aim to break them before hatching.
- Excludes: Permanently different art for all destructible terrain, a total remaining-enemy counter without location, seeing only the already spawned actor and a cue showing every future hatch time.
- Parameters: Reserve-bearing subject, flash phase, visibility window, location memory and hatching boundary
- Evidence: [Pengo decomposition](../games/m-r/pengo.md), PE-005. SEGA’s cabinet manual and recorded arcade play constrain the accepted rules. Exact capture hardware and revision are unverified.
- Novelty: first isolated for `GAME-0731`. See [TAXONOMY_CHANGE_477](../../research/taxonomy-changes/TAXONOMY_CHANGE_477.md). No external novelty claim.

## INF-659 — Read controlled chassis damage from its visible body instead of a life bar

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: The driven chassis changes its persistent appearance as it is damaged. Colour, visible dents or sparks communicate worsening condition directly on the body instead of a scalar health bar.
- Includes: The Nitro chassis in the first Metal Warriors sortie grows darker while its trajectory remains under player control. The original instructions describe visible dents and sparking as damage cues.
- Excludes: Momentary hit flashes alone, a numerical reserve gauge, separately displayed enemy anatomy by region, and assuming an exact invisible damage counter from one colour.
- Parameters: Controlled chassis, damage stages, colour, dent, spark, persistence beyond each hit and absence of a life bar
- Evidence: [Metal Warriors decomposition](../games/m-r/metal-warriors.md), MW-004. Konami’s original booklet and the documented rescue route corroborate the bounded effects. Hardware and exact cartridge bytes are unverified.
- Novelty: first isolated for `GAME-0728`. See [TAXONOMY_CHANGE_474](../../research/taxonomy-changes/TAXONOMY_CHANGE_474.md). No external novelty claim.

## INF-658 — Point to the next compatible placement with a depicted collaborator’s hand

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: In a local parts task, a depicted collaborator points at a relevant object or receiver while the world remains at the current work step. The indication directs the player’s next placement or correction without putting the part away for them.
- Includes: One of the extra hands points toward a jar while the loose hardware is still available in Familiar. Another points to one of the held interlocking panels during their fitting scene.
- Excludes: An external hint, a permanently drawn outline with no collaborator, spoken commentary with no actionable cue and a collaborator automatically placing the item.
- Parameters: Current work step, indicating actor, indicated object or receiver and unresolved player placement
- Evidence: [Miniatures decomposition](../games/m-r/miniatures.md), MT-002 and MT-005. Released gameplay records support the local interactions. Capture host and executable revision are unverified.
- Novelty: first isolated for `GAME-0727`. See [TAXONOMY_CHANGE_473](../../research/taxonomy-changes/TAXONOMY_CHANGE_473.md). No external novelty claim.

## INF-657 — Show a growing route map and let touch recenter the view independently of the payload

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: The map remains visible alongside the current action view and exposes surveyed passages and the local position. Temporarily moving it to the touch surface lets the player choose a viewport location without steering the carried payload there.
- Includes: The Nintendo DS map marks the explored corridor while the spirit bubble moves. Holding Map in Soul Bubbles permits inspection at a selected map location, then local control returns.
- Excludes: Clicking a minimap to order the carrier to move, a permanently complete floor plan, or a second map that cannot address a view position.
- Parameters: Surveyed route, current position, map mode, addressed point, camera displacement and retained payload pose
- Evidence: [Soul Bubbles decomposition](../games/s-z/soul-bubbles.md), SB-007. The official booklet and recorded Nintendo DS route support the stated boundary. The captured cartridge region and revision are unverified.
- Novelty: first isolated for `GAME-0726`. See [TAXONOMY_CHANGE_472](../../research/taxonomy-changes/TAXONOMY_CHANGE_472.md). No external novelty claim.

## INF-656 — Expose a visibly cracked route obstruction and teach the compatible tool at acquisition

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: An eligible solid route prop shows damage markings before the player can remove it. A separate acquisition prompt identifies the new tool and its usable input, letting the earlier visible affordance be acted upon on return.
- Includes: In the Crypt Custodian opening, cracked statues mark breakable scenery before the broom is available. The pickup panel later identifies the broom and its swing command.
- Excludes: A door shown as locked without a compatible action, a purely cosmetic crack, an explicit solved path, or a tool tutorial with no previously visible obstruction.
- Parameters: Visible breakability cue, obstructed route, later tool acquisition, prompted input and new use
- Evidence: [Crypt Custodian decomposition](../games/a-f/crypt-custodian.md), CC-003 and CC-004. Xbox-attributed footage and the written opening account support the stated boundary. The exact installed build and broader path variants are unverified.
- Novelty: first isolated for `GAME-0725`. See [TAXONOMY_CHANGE_471](../../research/taxonomy-changes/TAXONOMY_CHANGE_471.md). No external novelty claim.

## INF-655 — Show the next eligible phrase beside current track, song position and energy

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: The live view identifies the selected instrument track, shows upcoming note positions and marks the next still-eligible pair of bars. Separate indicators disclose remaining song energy, current song section, score and the stored item.
- Includes: In Frequency, after a miss makes two bars inactive, find a later green active pair or switch to another track. Read the Energy Meter separately from the song position marker.
- Excludes: A preview revealing the whole chart, a post-play accuracy report, a beat with no visible current track, and a local cue that reports no remaining survival budget.
- Parameters: Selected track, upcoming note positions, eligible phrase styling, energy, song position, score and inventory
- Evidence: [Frequency decomposition](../games/a-f/frequency.md), FQ-003, FQ-004 and FQ-006. The North American instruction booklet and silent PS2 frame evidence support the stated boundary. Executable revision and exact judgement windows are unverified.
- Novelty: first isolated for `GAME-0724`. See [TAXONOMY_CHANGE_470](../../research/taxonomy-changes/TAXONOMY_CHANGE_470.md). No external novelty claim.

## INF-654 — Show aim line, numbered block resistance and distinct shot and ball tallies

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: The shaft exposes the current aim line during direction selection and displays the remaining counted impacts on each visible numbered obstacle. Separate shot and ball tallies distinguish remaining launches from the available payload per launch.
- Includes: Before a holedown shot, compare the aim line with the lower edge of an exposed block. Its printed number and the two launch-related tallies tell different parts of the decision.
- Excludes: A guaranteed preview of every bounce, a radar bearing without projected aim, or a single ammo tally that cannot distinguish the launch allowance from its payload.
- Parameters: Current aim line, sampled opening path, block hit value, remaining shots and balls per shot
- Evidence: [holedown decomposition](../games/g-l/holedown.md), HD-002, HD-003, HD-005. Developer material, original Android reporting and silent frame review support the stated boundary. Exact Android build and numerical physics are unverified.
- Novelty: first isolated for `GAME-0723`. See [TAXONOMY_CHANGE_469](../../research/taxonomy-changes/TAXONOMY_CHANGE_469.md). No external novelty claim.

## INF-653 — Signal local transport availability near the active marker

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: A live indicator beside ordinary play status signals that the current position is within the reached travel marker’s call range. It identifies a present affordance before the player opens the travel command.
- Includes: QuackShot’s Flag Signal flashes near a checkpoint from which the player can call the airplane in the item menu.
- Excludes: A destination pin on a world map, a save icon, ordinary item count, and a destination-selection cursor.
- Parameters: Reached travel marker, current avatar position, live indicator and call availability
- Evidence: [QuackShot Starring Donald Duck decomposition](../games/m-r/quackshot-starring-donald-duck.md), QS-003 and QS-004. The North American retail instructions and two Genesis route recordings support the stated boundary. Exact cartridge revision and numerical timing are unverified.
- Novelty: first isolated for `GAME-0722`. See [TAXONOMY_CHANGE_468](../../research/taxonomy-changes/TAXONOMY_CHANGE_468.md). No external novelty claim.

## INF-652 — Show current collection count and separate clear credits

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: The live route displays a running ordinary-pickup count and reveals letter acquisition separately. The clear and level-selection views expose distinct credit for the full letter set, bonus collection and the pickup threshold.
- Includes: Bean Bay displays a red crystal counter in play and separate letter, emerald and red-crystal results after the goal portal.
- Excludes: One cumulative score, a single medal that hides the collection categories, a stopwatch result, or a claim about persistence across a full application restart.
- Parameters: Live count, visible letter pickup, level result, three independent collection categories and selected stage
- Evidence: [Kaze and the Wild Masks decomposition](../games/g-l/kaze-and-the-wild-masks.md), KZ-005 through KZ-007. The Xbox-labelled recording, launch sources and the independent route or documentation support the bounded rule. Exact rates and Xbox build were unverified.
- Novelty: first isolated for `GAME-0720`. See [TAXONOMY_CHANGE_466](../../research/taxonomy-changes/TAXONOMY_CHANGE_466.md). No external novelty claim.

## INF-651 — Show the player and active helper’s health, level and attack reserves separately

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: The combat view identifies the selected helper and exposes individual health, level and attack-power progress for the primary body and that helper. The primary reserve also signals when the surrounding sweep is available.
- Includes: Alisia Dragoon shows independent status panels with the player and selected helper portraits, HP, levels and gauges. The player’s full Thunder Power can flash before casting.
- Excludes: One shared health or casting pool for both actors, an enemy target lock, an equipment-only stat screen or an undisclosed special-attack threshold.
- Parameters: Player health, player attack level and reserve, full cue, active helper identity and independent helper status
- Evidence: [Alisia Dragoon decomposition](../games/a-f/alisia-dragoon.md), AD-004 and AD-006. The retail instruction booklets and two attributed Genesis recordings corroborate the boundary. Exact ranges, rates and ROM revision were not measured.
- Novelty: first isolated for `GAME-0719`. See [TAXONOMY_CHANGE_465](../../research/taxonomy-changes/TAXONOMY_CHANGE_465.md). No external novelty claim.

## INF-650 — Compare a route sketch with a surveyable landscape and read its verification state

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: The interface keeps the selected sketch and its drawn landmarks visible alongside a traversable-world panorama that can be panned and zoomed. It distinguishes a proposed point in that view from the later confirmed sketch.
- Includes: The east-loch sketch depicts the Giant’s Tooth. A question-mark pin is visible during the survey, and a green check appears on the sketch after the shoreline verification.
- Excludes: An automatically solved minimap objective, a seamless exact map overlay showing all routes, a terrain mask that changes physical geometry, and real-world geolocation.
- Parameters: Selected sketch, visible geographic features, survey framing, mark feedback and later confirmation state
- Evidence: [A Highland Song decomposition](../games/a-f/a-highland-song.md), AHS-003, AHS-004, AHS-006. The inkle navigation notes and two commercial release-window records corroborate the boundary. Exact builds and confirmation radius were not measured.
- Novelty: first isolated for `GAME-0718`. See [TAXONOMY_CHANGE_464](../../research/taxonomy-changes/TAXONOMY_CHANGE_464.md). No external novelty claim.

## INF-649 — Show arriving chorus notes and a visible reply cue

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: In the local chorus view, moving note symbols present upcoming response opportunities and a visibly distinct cue indicates when to answer. The same view can show the note output without exposing exact timing tolerances.
- Includes: Franzea 1 keeps the traversal scene in view while note outlines circulate and a coloured cue approaches the input moment.
- Excludes: An audio-only instruction, a static collection tally, a fixed multicolumn instrumental chart, or a terminal accuracy summary.
- Parameters: Local chorus view, moving symbols, differentiated reply cue and visible note output
- Evidence: [LocoRoco 2 decomposition](../games/g-l/locoroco-2.md), LR2-006. The original publisher overview, Franzea 1 route and scoped English PSP frames corroborate the result. Exact judgment windows were not measured.
- Novelty: first isolated for `GAME-0717`. See [TAXONOMY_CHANGE_463](../../research/taxonomy-changes/TAXONOMY_CHANGE_463.md). No external novelty claim.

## INF-648 — Preview the effective tile mask and resource return of a pending terrain conversion

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: A pending facility placement outlines which tiles can be affected and reports the projected resource delta before commitment. Moving or rotating the candidate can change the mask and return independently of the listed construction price.
- Includes: In Terra Nil the Irrigator preview distinguishes eligible green cells from excluded red-marked cells and gives the projected leaf gain beside the building.
- Excludes: A generic range circle without local clipping, an after-action reward message, a static recipe list, or a preview that only reports whether placement is legal.
- Parameters: Pending placement, candidate orientation, eligible tiles, excluded terrain, predicted delta and base price
- Evidence: [Terra Nil decomposition](../games/s-z/terra-nil.md), TN-004 and TN-005. The release listing, in-game handbook and two post-release recordings are delimited in the claim ledger.
- Novelty: first isolated for `GAME-0716`. See [TAXONOMY_CHANGE_462](../../research/taxonomy-changes/TAXONOMY_CHANGE_462.md). No external novelty claim.

## INF-647 — Show the active rival mood and matching skill effectiveness before commitment

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: The battle view exposes the target’s active mood and remaining turns. While previewing a skill, the interface marks a match between that skill and the active mood before the player confirms the target.
- Includes: In Thirsty Suitors the rival panel shows Thirsty and three turns while Suitor Slam and its selected target carry a visible effectiveness marker.
- Excludes: A guessed hidden affinity alone, an outcome label after damage, a permanent character trait, or a skill description with no current target indication.
- Parameters: Selected target, active mood, turns remaining, skill preview and effectiveness marker
- Evidence: [Thirsty Suitors decomposition](../games/s-z/thirsty-suitors.md), TS-005. The PlayStation release listing and corroborating traces are delimited in the claim ledger.
- Novelty: first isolated for `GAME-0714`. See [TAXONOMY_CHANGE_460](../../research/taxonomy-changes/TAXONOMY_CHANGE_460.md). No external novelty claim.

## INF-646 — Expose live projectile bounces, receiver hits and ready continuation separately

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: A routing board shows successive projectile motion and separate reactions at the contacted deflector and the receiving object. The board exposes a distinct control when the route has qualified for continuation.
- Includes: In ELOH a percussion block animates at any eligible impact. A correct rebound reaches the receiver, which pulses, and successful delivery exposes a bottom arrow.
- Excludes: A predicted line without live contact feedback, a block reaction treated as a hit at the goal, an inferred audio-only cue or an automatic board transition without a continuation choice.
- Parameters: Visible projectile path, block reaction, receiver hit cue and ready control
- Evidence: [ELOH decomposition](../games/a-f/eloh.md), ELH-005–ELH-006. The Google Play video and Android-attributed footage are delimited in the claim ledger.
- Novelty: first isolated for `GAME-0711`. See [TAXONOMY_CHANGE_457](../../research/taxonomy-changes/TAXONOMY_CHANGE_457.md). No external novelty claim.

## INF-645 — Show credited interior and remaining time during perimeter repair

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: While a perimeter can still be edited, the board distinguishes a credited enclosure from an open wall using its visible gaps and the state of the enclosed ground. A live repair clock shows how much longer the player can change that classification.
- Includes: In Rampart a breached perimeter leaves the main castle interior green. Closing it turns the interior blue while the repair countdown continues.
- Excludes: A generic timer without any enclosure feedback, a placement cursor that shows only whether a piece fits, or an ownership result first shown after the player loses input.
- Parameters: Visible gaps, open and credited ground states, remaining time and available repair input
- Evidence: [Rampart decomposition](../games/m-r/rampart.md), RAM-004–RAM-007. The Atari operator manual and attributed trackball-ruleset captures are delimited in the claim ledger.
- Novelty: first isolated for `GAME-0708`. See [TAXONOMY_CHANGE_454](../../research/taxonomy-changes/TAXONOMY_CHANGE_454.md). No external novelty claim.

## INF-644 — Show engaged suction separately from the remaining attached deposit

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: During aimed environmental suction, local material stretching or particles visibly connect the engaged portion to the tool intake, while unengaged attached residue remains distinguishable on the target. This lets the player adjust aim before the entire deposit clears.
- Includes: In The Gunk a bright strand and particles lead into the gauntlet from the current target while dark red-veined material remains attached around the ridge opening.
- Excludes: A generic crosshair with no current contact feedback, an exact numeric range display, a stored-goods count, or a restoration animation only after the deposit has cleared.
- Parameters: Suction contact signal, tool intake, target area, residual material and direction of re-aim
- Evidence: [The Gunk decomposition](../games/s-z/the-gunk.md), TG-003–TG-005. The Xbox listing, publisher account and two attributed Series captures are delimited in the claim ledger.
- Novelty: first isolated for `GAME-0707`. See [TAXONOMY_CHANGE_453](../../research/taxonomy-changes/TAXONOMY_CHANGE_453.md). No external novelty claim.

## INF-643 — Show required key progress and the keyed exit’s readiness separately

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: While a level is live, the interface shows the current required key progress, and the fixed exit has a separate visibly distinguishable locked or eligible marker. A visible live clock indicates that the route must still be completed within the attempt.
- Includes: In Kula World Level 3 the gray key slot fills in gold, the red exit switches to green and the hourglass remains visible until the attempt closes.
- Excludes: An optional collectible count, a clock with no key or exit status, an exit that is never visible until after completion, or guidance promising the whole route to every required item.
- Parameters: Required key slots, credit colour, separate exit marker, eligibility and live timer cue
- Evidence: [Kula World decomposition](../games/g-l/kula-world.md), KW-004–KW-006. The museum record, disc-derived reference and two attributed PlayStation witnesses are delimited in the claim ledger.
- Novelty: first isolated for `GAME-0706`. See [TAXONOMY_CHANGE_452](../../research/taxonomy-changes/TAXONOMY_CHANGE_452.md). No external novelty claim.

## INF-642 — Expose rollover qualification, lock state and pending award separately from the running score

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: A physical table shows the individual rollover indicators, the local receiver presentation and the pending award separately from the accumulated score. The player can distinguish a completed route requirement from readiness to capture and from an already credited tally.
- Includes: In Alien Crush the four upper lamps, the visible Tentacloid Lock state and the upper bonus counter are separate cues. The bonus overlay retains a distinct local value and changing run total.
- Excludes: Only a final total, a single generic bonus-ready lamp with no separate rollover states, or a results screen reporting only a bonus-room clear and perfect award.
- Parameters: Lamp identity and state, lock presentation, pending value, multiplier and running total
- Evidence: [Alien Crush decomposition](../games/a-f/alien-crush.md), ALC-004–ALC-006. The original English booklet and the two attributed TurboGrafx-16 witnesses are delimited in the claim ledger.
- Novelty: first isolated for `GAME-0704`. See [TAXONOMY_CHANGE_450](../../research/taxonomy-changes/TAXONOMY_CHANGE_450.md). No external novelty claim.

## INF-641 — Distinguish marked required cargo, its remaining quota and the live reward clock

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: In one physical loading task, mark which loose objects can satisfy its required quota and show the remaining count separately from the live time available for a higher payout. Unmarked freight remains movable without satisfying the quota.
- Includes: In Part Time UFO the first farm shows blinking orange crates, a two-crate counter and a separate countdown. The basket can yield pay while one required crate is still missing.
- Excludes: An undifferentiated total of loaded objects, only the required final shape, or a bonus clock with no independent cargo-requirement cues.
- Parameters: Marked object roles, remaining required count, live time display and optional cargo credit
- Evidence: [Part Time UFO decomposition](../games/m-r/part-time-ufo.md), PTU-003–PTU-005. The retail materials and the two timed Nintendo Switch witnesses are delimited in the claim ledger.
- Novelty: first isolated for `GAME-0703`. See [TAXONOMY_CHANGE_449](../../research/taxonomy-changes/TAXONOMY_CHANGE_449.md). No external novelty claim.

## INF-640 — Show pipe-pair identity and partial repair through local marks and gauges

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: The player can inspect the marks that associate the exposed terminals of a repair circuit and read its local gauge. Its indicator can change to a success sector while unfinished circuits elsewhere leave the larger task unresolved.
- Includes: In Escaping Wonderland the blue-striped seam and its needle in the green sector identify one restored route before the other panel connections are finished.
- Excludes: A global completion message alone, an unlabeled decorative gauge, a pressure simulation whose values are hidden, or a clue locating only the room entrance.
- Parameters: Terminal color and markings, visible pair, gauge position, successful sector and independent unresolved routes
- Evidence: [Escaping Wonderland decomposition](../games/a-f/escaping-wonderland.md), EW-003–EW-004. The retail materials and the two timed Quest route witnesses are delimited in the claim ledger.
- Novelty: first isolated for `GAME-0702`. See [TAXONOMY_CHANGE_448](../../research/taxonomy-changes/TAXONOMY_CHANGE_448.md). No external novelty claim.

## INF-639 — Distinguish companion stay and follow through paired press and hold cues

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: The live view presents two orders for the same companion on one control: a short press requests staying at the current position, while a hold requests following the player. The cue shows both alternatives before the player chooses one.
- Includes: In Planet of Lana II’s first cooperative plate room on Switch 2, the cue pairs A for Stay with holding A for Follow.
- Excludes: Displaying only one contextual action at a time, issuing a remote destination, showing an already chosen follow state without instructions, or an instruction requiring unrelated buttons for the two orders.
- Parameters: Current companion, shared control, press and hold presentation, wait order, follow order and visible cue context
- Evidence: [Planet of Lana II decomposition](../games/m-r/planet-of-lana-ii.md), LANA2-002. The release materials and the timed witnesses are delimited in the claim ledger.
- Novelty: first isolated for `GAME-0700`. See [TAXONOMY_CHANGE_446](../../research/taxonomy-changes/TAXONOMY_CHANGE_446.md). No external novelty claim.

## INF-638 — Show a candidate’s carried kit and reveal proficiencies before commitment

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: The candidate-specific preview shows assigned equipment and current and maximum resource values. A separate request within that preview discloses proficiencies and attributes while the player can still leave without admitting the candidate.
- Includes: A Dungeon Master mirror review shows equipment and health, stamina and mana. Holding the eye with an empty hand shows proficiencies and attributes before choosing a mode.
- Excludes: Only showing the portrait, a readout available solely after accepting the candidate, or a live roster summary without the distinct pre-admission view.
- Parameters: Candidate, equipment, resource pairs, inspect affordance, proficiencies, attributes and commitment state
- Evidence: [Dungeon Master decomposition](../games/a-f/dungeon-master.md), DM-002. The manual, contemporary account and Atari ST witnesses are delimited in the claim ledger.
- Novelty: first isolated for `GAME-0699`. See [TAXONOMY_CHANGE_445](../../research/taxonomy-changes/TAXONOMY_CHANGE_445.md). No external novelty claim.

## INF-637 — Show a reference motif with the relative mark to apply elsewhere

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: A clue combines a recognizable reference image and a distinguishable overlay. Its motif identifies another eligible view, while the overlay shows the shape and position of the modification relative to that motif.
- Includes: Song of Bloom shows a red ring on the summit of a white mountain in the bud cue and presents the same feature without a ring in the chalk narrative.
- Excludes: A written answer without a location, an exact absolute-coordinate instruction, an outline on the actual target canvas, or an unmarked example with no demonstrated action.
- Parameters: Reference motif, overlay, target view correspondence, stroke geometry, relative placement and availability
- Evidence: [Song of Bloom decomposition](../games/s-z/song-of-bloom.md), BLM-002–BLM-003. The developer materials and iPhone witnesses are delimited in the claim ledger.
- Novelty: first isolated for `GAME-0698`. See [TAXONOMY_CHANGE_444](../../research/taxonomy-changes/TAXONOMY_CHANGE_444.md). No external novelty claim.

## INF-636 — Distinguish local kill awards, sustained weapon state and flight stock

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: Visible destruction awards identify the local scoring event while a separate status area continues to show accumulated score, weapon level, charged attack reserve and replacement craft.
- Includes: In Radiant Silvergun the chain or secret popup is near the affected target. Score and weapon level, the sword gauge and remaining ship marks remain in the upper display.
- Excludes: A hidden accumulation with no event cue, a single opaque total, show-only ammunition, or a report first displayed after the encounter.
- Parameters: Local award, running score, weapon level, charge, replacement stock and display location
- Evidence: [Radiant Silvergun decomposition](../games/m-r/radiant-silvergun.md), RSG-004–RSG-006. The Saturn booklet and recorded witnesses are delimited in the claim ledger.
- Novelty: first isolated for `GAME-0697`. See [TAXONOMY_CHANGE_443](../../research/taxonomy-changes/TAXONOMY_CHANGE_443.md). No external novelty claim.

## INF-635 — Mark the selected predecessor’s reply among current choices

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: The current response list separately marks the eligible choice previously taken in the selected external play record. The marking shows a witnessed decision while leaving the current selection independently available.
- Includes: On Nahe’s boat in Tides of Tomorrow the prior-player symbol accompanies the leave response while the current player can take the dose.
- Excludes: The current pointer or default choice, an indicator that guarantees a trait outcome, the current player’s past dialogue history, or a forced repetition of the branch.
- Parameters: earlier record, earlier response, current candidate, distinct marker and current selection
- Evidence: [Tides of Tomorrow decomposition](../games/s-z/tides-of-tomorrow.md), TOT-002–TOT-003. The PS5 Pro traces and developer evidence are delimited in the claim ledger.
- Novelty: first isolated for `GAME-0696`. See [TAXONOMY_CHANGE_442](../../research/taxonomy-changes/TAXONOMY_CHANGE_442.md). No external novelty claim.

## INF-634 — Distinguish defensive responses by the incoming attack marker

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: A transient marker on the attacking character identifies both the source of a live attack and its defence class. Separate marker classes advertise a required avoidance response or eligibility for a reactive counter.
- Includes: REPLACED’s early red dodge and yellow counter-eligible marks during the first Termite Dale fight.
- Excludes: A single generic warning with no alternative response classes; a permanent vulnerability outline; the tutorial sentence that explains a symbol; or an exact attack timeline.
- Parameters: attacking character, cue class, cue appearance and expiry, allowed response, defence timing and interruption
- Evidence: [REPLACED decomposition](../games/m-r/replaced.md), claims RPL-002–RPL-004. The launch capture and supplementary trace show the cue and its taught response.
- Novelty: first isolated for `GAME-0691`. See [TAXONOMY_CHANGE_437](../../research/taxonomy-changes/TAXONOMY_CHANGE_437.md). No external novelty claim.

## INF-633 — Show the target contour, current cast shadow and accepted panel indication in place

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: A receiving panel exposes authored target marks and the different live silhouette cast by the held prop on that same surface. An accepted fit gets its own change in the panel, so the player can distinguish partial alignment from credit already granted.
- Includes: Compare the dark shadow with the first square outline, then note the bright target patch or frame after acceptance, even when the prop moves.
- Excludes: Giving exact distance or angle values, showing a preview of a future placed solid, exposing the solution gesture directly, or interpreting the unmarked edges of a target as hidden objects.
- Parameters: Target marks, live silhouette, position difference and accepted-panel feedback.
- Evidence: [Shadow Point decomposition](../games/s-z/shadow-point.md), SP-002, SP-003. The attributed original Quest captures and the original launch materials support the scoped rules.
- Novelty: first isolated for `GAME-0689`. See [TAXONOMY_CHANGE_435](../../research/taxonomy-changes/TAXONOMY_CHANGE_435.md). No external novelty claim.

## INF-632 — Show elapsed trip time, credited points and the pending trick chain separately

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: During an authored moving course, show the elapsed run time and already credited score independently of the pending trick additions, current multiplier marker and recent trick names. Local task feedback may report progress without ending the attempt.
- Includes: Read the zero white total beside the yellow pending amount while the chain grows, and read the Perfect Drift dare counter on the same run.
- Excludes: A countdown-only park timer, a score capped to an unstated formula, an already settled result card, or foreknowledge of hidden track branches.
- Parameters: Elapsed time, credited score, pending points, current chain marker, recent tricks and local dare counter.
- Evidence: [Denshattack! decomposition](../games/a-f/denshattack.md), DA-002, DA-004. The attributed PlayStation captures and the platform release materials support the scoped rules.
- Novelty: first isolated for `GAME-0687`. See [TAXONOMY_CHANGE_433](../../research/taxonomy-changes/TAXONOMY_CHANGE_433.md). No external novelty claim.

## INF-631 — Display the assembled command and its missing argument before dispatch

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: A dedicated command line shows the selected verb and addressed operands as words. For a command that needs a second object, the displayed connective shows that another operand is still required. An execution response may be reported on a separate message line.
- Includes: Read the unfinished front-door unlock sentence before owning a key, then read the complete line after selecting the key name in inventory. A separate message reports the locked door on an earlier attempt.
- Excludes: An icon carried at the pointer with no editable sentence, an invisible input buffer, a menu listing legal actions without a pending command, or a guarantee that a complete sentence will succeed.
- Parameters: Persistent verb list, pending sentence line, addressed nouns, missing operand cue, supplied connective and separate result message.
- Evidence: [Maniac Mansion decomposition](../games/m-r/maniac-mansion.md), MM-002–MM-003, MM-005. The Lucasfilm manual and retail floppy capture corroborate the scoped rules.
- Novelty: first isolated for `GAME-0686`. See [TAXONOMY_CHANGE_432](../../research/taxonomy-changes/TAXONOMY_CHANGE_432.md). No external novelty claim.

## INF-630 — Expose the companion interaction command at an eligible control

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: A local control context displays the input for asking an autonomous companion to operate the addressed fixture. The prompt distinguishes delegation from the controlled actor using the fixture directly.
- Includes: At the tube stop lever, read the cue to call the other character to interact before leaving for the tube.
- Excludes: General movement instructions, a tutorial objective checklist, automatic delegation without an available cue, or a full route description.
- Parameters: Local cue trigger, addressed fixture, companion, input label, delegation and player context.
- Evidence: [REANIMAL decomposition](../games/m-r/reanimal.md), RA-002. Release-window PC footage and independent route descriptions corroborate the scoped rules.
- Novelty: first isolated for `GAME-0684`. See [TAXONOMY_CHANGE_430](../../research/taxonomy-changes/TAXONOMY_CHANGE_430.md). No external novelty claim.

## INF-629 — Show each target mark and its travel direction in an inspectable instruction

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: An inspectable authored note pairs each successive target mark with a turn direction for a rotary control. It preserves repeated marks as separate instructions, so the sequence discloses the required travel as well as the destinations.
- Includes: Read the final notebook page beside the mailbox dial. It pairs each of the two sevens with a left arrow and the one with a right arrow.
- Excludes: A plain list of digits, an external walkthrough, navigation directions through several world locations, or automatically entering the combination.
- Parameters: Authored note, ordered mark, direction symbol, repeated target, close-view access and interpretation.
- Evidence: [Last Window decomposition](../games/g-l/last-window-the-secret-of-cape-west.md), LW-003. Nintendo’s Chapter 1 guide and the two recorded English routes support the scoped rules.
- Novelty: first isolated for `GAME-0683`. See [TAXONOMY_CHANGE_429](../../research/taxonomy-changes/TAXONOMY_CHANGE_429.md). No external novelty claim.

## INF-628 — Expose each contestant’s vitality, stone or power state and elimination in a separate panel

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: A multiplayer arena assigns each fighter a distinct display slot. Its vitality remains visible throughout the fight. A stone display is replaced by a power gauge in the active form, and a definite elimination mark identifies a fighter who has left play.
- Includes: Read all four named panels when the fighters enter freefall. On landing and further combat, Pete’s portrait receives a red cross and Falcon’s filled stone slots become the powered gauge.
- Excludes: A single global health or survivor total, a two-player round score alone, an on-field object locator or an interface that reveals no contestant-specific resources.
- Parameters: Fighter identity, vitality, stone holdings, powered form, gauge and confirmed exclusion.
- Evidence: [Power Stone 2 decomposition](../games/m-r/power-stone-2.md), PS2-003, PS2-005–PS2-006. The original Dreamcast manual and the two recorded Arcade runs support the scoped rule.
- Novelty: first isolated for `GAME-0681`. See [TAXONOMY_CHANGE_427](../../research/taxonomy-changes/TAXONOMY_CHANGE_427.md). No external novelty claim.

## INF-627 — Show remaining height during a playable arena descent

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: An active falling arena displays the distance remaining to its landing transition while the player can still steer and contest pickups. The displayed distance falls independently of the fighters’ vitality.
- Includes: In Blue Sky Area, watch the metre count decrease as the contestants approach the courtyard and decide whether there is still room to reach an umbrella.
- Excludes: An elapsed round clock, a generic altitude instrument without a landing decision, a cinematic label or a prediction of the exact landing position.
- Parameters: Live fall, remaining metres, reachable airborne items, valid landing and display lifetime.
- Evidence: [Power Stone 2 decomposition](../games/m-r/power-stone-2.md), PS2-003–PS2-004. The original Dreamcast manual and the two recorded Arcade runs support the scoped rule.
- Novelty: first isolated for `GAME-0681`. See [TAXONOMY_CHANGE_427](../../research/taxonomy-changes/TAXONOMY_CHANGE_427.md). No external novelty claim.

## INF-626 — Expose the current readiness of each machine prerequisite on its own indicator

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: An addressed machine panel separately reports the current pass or fail state of named setup or component prerequisites, allowing the player to locate the remaining issue before operating the final control.
- Includes: Read the three lighthouse rows for engaged rotation, raised housing and the bulb check. A green housing row can coexist with a red bulb check.
- Excludes: One aggregate power light, an inventory checklist of completed quests, the actual final output or a meter for allocating a finite pool of power.
- Parameters: Machine, named prerequisites, per-row red or green state, local changes and separate final control.
- Evidence: [Ghost Town decomposition](../games/g-l/ghost-town.md), GHT-002, GHT-005. The native Quest walkthrough and independent released-game capture show the fixture state.
- Novelty: first isolated for `GAME-0680`. See [TAXONOMY_CHANGE_426](../../research/taxonomy-changes/TAXONOMY_CHANGE_426.md). No external novelty claim.

## INF-625 — Preview an attack and its possible counter separately

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: Before confirming an eligible tactical attack, the interface shows predicted attack damage and hit chance and separately previews the defender’s possible counter damage and chance, alongside both actors’ current resources.
- Includes: Read the two directional rows in the PSP forecast when Jeanne or Roger targets the English Officer. Choose a different eligible attacking position and compare the exchange.
- Excludes: A fixed damage number without likelihood, a post-hit result, a one-sided hit preview or an independently chosen response by the defender.
- Parameters: Attacking actor, target, approach, attack strength and chance, counter strength and chance, current resources and confirmation.
- Evidence: [Jeanne d'Arc decomposition](../games/g-l/jeanne-darc.md), JDA-003. The released PSP recordings and the contemporary rules sources support the scoped boundary.
- Novelty: first isolated for `GAME-0679`. See [TAXONOMY_CHANGE_425](../../research/taxonomy-changes/TAXONOMY_CHANGE_425.md). No external novelty claim.

## INF-624 — Show the local race gap and both lap clocks alongside the vehicle state

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: The live cockpit shows lap and remaining boost, signed separation from one rival, speed, current and fastest-lap time, separate lead indicators and the chassis condition.
- Includes: Read whether the rival is ahead or behind, which driver owns the best lap and how much boost and chassis margin remain before a ramp.
- Excludes: The post-race result screen, a countdown until failure, a course minimap alone or an absolute position measure without this comparison.
- Parameters: Lap, reserve, rival separation sign, speed, current time, best time, lead indicators and damage display.
- Evidence: [Stunt Car Racer decomposition](../games/s-z/stunt-car-racer.md), SCR-005, SCR-006. The Amiga-attributed trace and original operating instructions support the scoped boundary.
- Novelty: first isolated for `GAME-0677`. See [TAXONOMY_CHANGE_423](../../research/taxonomy-changes/TAXONOMY_CHANGE_423.md). No external novelty claim.

## INF-623 — Introduce successive control cues inside a moving ride

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: The live view shows distinct pairs of applicable inputs in succession as the same traversable segment keeps advancing.
- Includes: Read Push and Ollie first, then Flip Trick and Grab Trick farther along the road.
- Excludes: A static control list, a paused tutorial menu, an aiming reticle or a quick-time sequence with an assessed deadline.
- Parameters: Active segment, input group, readable button labels and present progress.
- Evidence: [Mixtape decomposition](../games/m-r/mixtape.md), MX-003. The launch-window Xbox trace and the applicable author and player evidence support the scoped boundary.
- Novelty: first isolated for `GAME-0676`. See [TAXONOMY_CHANGE_422](../../research/taxonomy-changes/TAXONOMY_CHANGE_422.md). No external novelty claim.

## INF-622 — Expose the journey benchmark, running count and final ticket

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: The level exposes a journey benchmark while planning. During traversal it displays the accrued count. On completion it shows the settled total and earned ticket.
- Includes: Read Journey 28 on the empty board, watch the value count upward during the run, then verify 28 beside the gold ticket.
- Excludes: A stopwatch alone, a track piece inventory or a result that hides the counted journey.
- Parameters: Benchmark, planning state, current count, terminal count and ticket.
- Evidence: [Teeny Tiny Trains decomposition](../games/s-z/teeny-tiny-trains.md), TTT-006–TTT-008. The launch-window iOS trace, in-game tutorial and creator sources support the scoped boundaries.
- Novelty: first isolated for `GAME-0675`. See [TAXONOMY_CHANGE_421](../../research/taxonomy-changes/TAXONOMY_CHANGE_421.md). No external novelty claim.

## INF-621 — Expose live ring, stunt and checkpoint-time event credits

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: While the craft moves, the interface exposes speed, remaining block time and the running score. Individual ring passes, stunts and timed checkpoints show their separate awarded credits.
- Includes: Read a 50-point ring, then the credited stunt and a distinct time-extension award against the changing score and timer.
- Excludes: A result table alone, a binary stunt-pass threshold or a checkpoint notification that does not expose the earned amount.
- Parameters: Speed, timer, current total, event source, displayed credit and gate renewal cue.
- Evidence: [Wave Race: Blue Storm decomposition](../games/s-z/wave-race-blue-storm.md), WBS-003–WBS-007. The North American booklet and the two scoped attempt traces support the boundary described in the game record.
- Novelty: first isolated for `GAME-0674`. See [TAXONOMY_CHANGE_420](../../research/taxonomy-changes/TAXONOMY_CHANGE_420.md). No external novelty claim.

## INF-620 — Expose actor dice, skill fit, forecast and resolved clock feedback

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: The action view shows whose current dice can be placed, how the actor fits the required skill, the forecast result classes and the current progress or pressure. Resolution identifies its actual effect.
- Includes: Compare the Sleeper’s and Serafin’s dice for the hatch, then check progress or Drone Stress after committing a die.
- Excludes: A generic difficulty label without the actor’s spendable dice, a hidden result class or a progress bar without action context.
- Parameters: Actor, known die, action skill, forecast classes, tracks and outcome feedback.
- Evidence: [Citizen Sleeper 2 decomposition](../games/a-f/citizen-sleeper-2-starward-vector.md), CS2-003–CS2-007. The official product documentation and recorded contract traces support the boundary described in the game record.
- Novelty: first isolated for `GAME-0673`. See [TAXONOMY_CHANGE_419](../../research/taxonomy-changes/TAXONOMY_CHANGE_419.md). No external novelty claim.

## INF-619 — Show local bonus credit and a separate perfect award alongside the continuing score

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: Bonus settlement separately displays the local earned tally and the extra perfect-clear award, with the running parent score and remaining ball stock readable during settlement.
- Includes: Read the bonus credit first, the perfect special points next and the main-table score after both awards have been added.
- Excludes: A single opaque total, a high-score table without the earned components or a live score indicator with no separate perfect result.
- Parameters: Local tally, perfect award, display order, current parent score, reserve indicator and credit timing.
- Evidence: [Devil's Crush decomposition](../games/a-f/devils-crush.md), DCR-005, DCR-007. The original booklet or the cross-checked retail-rules traces support the boundary described in the game record.
- Novelty: first isolated for `GAME-0672`. See [TAXONOMY_CHANGE_418](../../research/taxonomy-changes/TAXONOMY_CHANGE_418.md). No external novelty claim.

## INF-618 — Show a tested creature property in live feedback and a readable retained entry

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: When a creature property is recorded, the interface identifies the specific result at the scene and exposes a readable entry for the same property under that creature after the notice disappears.
- Includes: The apple bubble triggers an immediate discovery placard and a later illustrated one-star note under Glubbit.
- Excludes: Showing only a star count, showing only live speech with no readable entry, disclosing all properties as an up-front list or exposing only the creature name.
- Parameters: Creature, result identity, live notice, recorded description, entry grouping and displayed credit.
- Evidence: [Yoshi and the Mysterious Book decomposition](../games/s-z/yoshi-and-the-mysterious-book.md), YMB-004, YMB-005. Nintendo's action guide and multiple retail traces support the scoped boundaries. Exact thresholds and restore behaviour remain unmeasured.
- Novelty: first isolated for `GAME-0671`. See [TAXONOMY_CHANGE_417](../../research/taxonomy-changes/TAXONOMY_CHANGE_417.md). No external novelty claim.

## INF-617 — Preview the reachable capsule’s skill before binding it

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: Approaching a reachable skill capsule exposes its class and an inspectable card with identity, price of use, effect strength, range and remaining-use type before the player chooses whether or where to bind it.
- Includes: Read the blue Flash Barrier or attack-coloured Laser and Vacuum Slash details before capture on the Highway.
- Excludes: A tooltip shown only after equipping, an unrevealed next draw, or a simple icon with no pre-capture skill information.
- Parameters: Capsule, approach range, skill class, cost, strength, effective range and use type.
- Evidence: [Phantom Dust decomposition](../games/m-r/phantom-dust.md), PHD-002, PHD-003. The English Xbox manual and original-rules recordings support the stated boundaries. Exact runtime hit and refill timings remain unmeasured.
- Novelty: first isolated for `GAME-0670`. See [TAXONOMY_CHANGE_416](../../research/taxonomy-changes/TAXONOMY_CHANGE_416.md). No external novelty claim.

## INF-616 — Mark a locked target with the current distance band

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: While a hostile is locked, the reticle changes colour or shape to indicate its current distance band. The player can compare that band with the preferred range of the bound attack.
- Includes: A green distant Ommato reticle cues Laser while an orange close reticle cues Vacuum Slash in Phantom Dust.
- Excludes: An identity-only target marker, a fixed accuracy indicator, or range inferred solely from the enemy’s apparent size.
- Parameters: Locked actor, distance band, reticle appearance and preferred attack range.
- Evidence: [Phantom Dust decomposition](../games/m-r/phantom-dust.md), PHD-004. The English Xbox manual and original-rules recordings support the stated boundaries. Exact runtime hit and refill timings remain unmeasured.
- Novelty: first isolated for `GAME-0670`. See [TAXONOMY_CHANGE_416](../../research/taxonomy-changes/TAXONOMY_CHANGE_416.md). No external novelty claim.

## INF-615 — Expose mixed square tile faces without a target picture preview

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: The player can inspect the visible artwork on the current mixed square fragments. Their common geometric shape does not identify the contributing picture and the complete target image is withheld during ordinary assembly.
- Includes: Separating the visible orange, yellow and green fragments of Braeburn from similarly sized and coloured fragments on the same floor.
- Excludes: A printed solution image, shape-keyed connector tabs, a fixed silhouette to fill and a random-next-item preview.
- Parameters: Visible artwork, uniform square shape, mixed ownership and hidden assembled preview.
- Evidence: [Wilmot Works It Out decomposition](../games/s-z/wilmot-works-it-out.md), WWO-002, WWO-004. Publisher documentation, the creator interview and the released-game traces support the stated boundaries. The traces are cross-platform corroboration for the macOS target.
- Novelty: first isolated for `GAME-0669`. See [TAXONOMY_CHANGE_415](../../research/taxonomy-changes/TAXONOMY_CHANGE_415.md). No external novelty claim.

## INF-614 — Show discovery and completion as distinct states of the same named event

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: The interface discloses the identity and clue of a discovered authored event, distinguishes its unresolved and completed states and exposes the corresponding state transition feedback.
- Includes: The Clear the Fog discovery and CLEAR result in Tomba!, with separate Adventure Point receipts and an Events screen that distinguishes the two states.
- Excludes: A static hint, a simple current-target marker, a count without event identity and a claimable reward list that shows no discovered unresolved state.
- Parameters: Event identity, clue, unresolved marker, completion marker and feedback on each transition.
- Evidence: [Tomba! decomposition](../games/s-z/tomba.md), TOM-003, TOM-006. The North American manual and recorded retail play support the boundary in the claim ledger. Physical button telemetry and flags in executable memory were unavailable.
- Novelty: first isolated for `GAME-0668`. See [TAXONOMY_CHANGE_414](../../research/taxonomy-changes/TAXONOMY_CHANGE_414.md). No external novelty claim.

## INF-613 — Read projectile response classes and the guardian’s current damage eligibility

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: Distinct visible projectile classes indicate different defensive choices while a separate boss cue shows whether direct damage is accepted. Read these cues together before choosing to absorb, evade or attack.
- Includes: Read the blue volley and yellow waves alongside Prophet’s closed eye and segmented bar, then recognise the exposed eye and ordinary bar.
- Excludes: Inferring attack eligibility only from numeric damage, a same-colour only hit rule, a combined vitality gauge with no eligibility cue, or an invariant health bar.
- Parameters: Projectile appearance, impact response class, core appearance, segmented protection and live attack window.
- Evidence: [SAROS decomposition](../games/s-z/saros.md), SAR-003, SAR-005, SAR-006. Housemarque’s control notes and the PS5-attributed combat traces support the scope indicated in the ledger. Exact runtime coefficients were not measured.
- Novelty: first isolated for `GAME-0667`. See [TAXONOMY_CHANGE_413](../../research/taxonomy-changes/TAXONOMY_CHANGE_413.md). No external novelty claim.

## INF-612 — Expose current dice, equipment predicates and live combat states

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: Present the available rolled faces beside socket predicates, effects and remaining uses, and show current health and status on each side to inform the next allocation.
- Includes: Reading the current even and upper-bound requirements, remaining rerolls, the marked die and the two health indicators.
- Excludes: Previewing unknown future rolls, exposing a guaranteed enemy command before its roll, and showing a final numeric combat report alone.
- Parameters: exposed faces, visible card predicates and counts, marked dice, both health readings and device layout.
- Evidence: [Dicey Dungeons decomposition](../games/a-f/dicey-dungeons.md), DD-002–DD-005. Mobile reference footage and the cited equipment, status or progression evidence support this boundary. The exact Android executable was not measured.
- Novelty: first isolated for `GAME-0664`. See [TAXONOMY_CHANGE_410](../../research/taxonomy-changes/TAXONOMY_CHANGE_410.md). No external novelty claim.

## INF-611 — Show a shared timing point with phase-specific angular and symbolic cues

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: One interface marks the current chart role and a common judgement point. Phrase play exposes an analog sector and trace with timed bars, while Guard exposes distinct approaching symbols. Two gauges show current player and opponent power.
- Includes: Read the central blue point, angular sector and phrase bars in Charge, then the converging face-button symbols in Guard without losing sight of the two gauges.
- Excludes: A fixed set of parallel fret lanes, an audio-only beat cue, a tutorial disconnected from live events, or a terminal accuracy summary.
- Parameters: Current role indicator, judgement point, trace, analog sector, guard symbols, approach directions and two gauges.
- Evidence: [Gitaroo Man decomposition](../games/g-l/gitaroo-man.md), GM-002, GM-003, GM-005. The printed North American booklet and two recorded PS2 routes support this boundary. Exact controller sampling and executable revision were not measured.
- Novelty: first isolated for `GAME-0663`. See [TAXONOMY_CHANGE_409](../../research/taxonomy-changes/TAXONOMY_CHANGE_409.md). No external novelty claim.

## INF-610 — Show the required next strike pattern on the active opponent

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: The in-world cue marks the active opponent with a direction or remaining count for the next part of a gesture string. Updating the cue makes accepted local progress visible without identifying future threats outside the current target.
- Includes: Follow the chevrons or the numbered circles over a sewer opponent. A remaining count can decrement as strikes are accepted.
- Excludes: A global longest-combo counter, a counter warning from another attacker, an unlinked tutorial instruction or a permanent target tag.
- Parameters: Active opponent, displayed direction or count, cue location, acceptance and visual update.
- Evidence: [Batman: Arkham Shadow decomposition](../games/a-f/batman-arkham-shadow.md), AS-004, AS-005. The attributed commercial recordings and Camouflaj design material support the recorded boundary. The headset binaries and exact controller telemetry were not verified.
- Novelty: first isolated for `GAME-0662`. See [TAXONOMY_CHANGE_408](../../research/taxonomy-changes/TAXONOMY_CHANGE_408.md). No external novelty claim.

## INF-609 — Show a world-space glide path and enlarge the final height scale

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: The approach view marks a suggested descent toward the runway in world space. As the aircraft gets low, a ground-relative height scale appears and changes magnification near touchdown without controlling the aircraft.
- Includes: Follow the green guide in Flight Area 1. Below the documented display thresholds, check first the ordinary and then the enlarged scale at the right edge.
- Excludes: A compulsory ring sequence, a landing radar without suggested approach geometry, a fixed altitude readout and an automatic glide-slope controller.
- Parameters: Suggested path, world-space marker, runway, scale visibility threshold, scale change threshold and aircraft height.
- Evidence: [Pilotwings decomposition](../games/m-r/pilotwings.md), PL-003, PL-005. The original US booklet and two attributed traces support the rule. Neither recorded cartridge was independently matched to a revision.
- Novelty: first isolated for `GAME-0661`. See [TAXONOMY_CHANGE_407](../../research/taxonomy-changes/TAXONOMY_CHANGE_407.md). No external novelty claim.

## INF-608 — Expose sibling birth rank before sibling identities are established

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: Display sibling slots in a declared oldest-to-youngest order while their occupants remain to be identified. Position contributes a relation that evidence can constrain without disclosing a name or portrait for that position.
- Includes: The opening board labels the three unidentified Roottree sisters’ positions from oldest on the left to youngest on the right.
- Excludes: Alphabetically sorted named records, a chart that already links each name to a portrait, a chronological result list or unrestricted placement on a blank canvas.
- Parameters: Sibling group, slot order, age comparison, unknown occupant and evidence clue.
- Evidence: [The Roottrees are Dead decomposition](../games/s-z/the-roottrees-are-dead.md), RT-003, RT-004. The commercial listing, publisher context and attributed recordings support the bounded route. The exact installed depot was unverified.
- Novelty: first isolated for `GAME-0660`. See [TAXONOMY_CHANGE_406](../../research/taxonomy-changes/TAXONOMY_CHANGE_406.md). No external novelty claim.

## INF-607 — Preview both sides’ damage before an automatic exchange

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: Identify one prospective matchup and expose predicted damage for both sides of its full automatic exchange while the player can still reconsider the order or the eligible combatant.
- Includes: The proposed bridge contact in Call to Action shows 21 damage on one side and 1 on the other before combat.
- Excludes: A single strike’s hit chance, remaining health alone, predictions visible only after commitment, an exact random-state promise or the action of replacing one party.
- Parameters: Prospective pairing, predicted damage per side, time of disclosure and commitment.
- Evidence: [Unicorn Overlord decomposition](../games/s-z/unicorn-overlord.md), UO-005. ATLUS and SEGA supply the rules, and attributed Switch footage supports the route. The exact capture binaries were unverified.
- Novelty: first isolated for `GAME-0658`. See [TAXONOMY_CHANGE_404](../../research/taxonomy-changes/TAXONOMY_CHANGE_404.md). No external novelty claim.

## INF-606 — Pair the current world view with a touch map and replace the pair for local interaction

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: During exploration two adjacent views simultaneously expose the current visible surroundings and a touch-sensitive local map with the avatar’s position and heading. A contextual interaction hands the display pair over to the conversation or object task instead.
- Includes: Guide Kyle by the plan while watching the staircase. In the right-handed arrangement, the selected jigsaw is operated on the right while Kyle is shown on the left.
- Excludes: An overview map that replaces the world view, two independently controlled avatars, or duplicating the same view on two displays.
- Parameters: Display pair, layout, surroundings, local pose, active touch surface and interaction state.
- Evidence: [Hotel Dusk: Room 215 decomposition](../games/g-l/hotel-dusk-room-215.md), HD-002, HD-004, HD-005. The original Nintendo documentation and two attributed DS recordings corroborate this scope. Physical inputs and binary identity were unverified.
- Novelty: first isolated for `GAME-0654`. See [TAXONOMY_CHANGE_400](../../research/taxonomy-changes/TAXONOMY_CHANGE_400.md). No external novelty claim.

## INF-605 — Compare emitted sound and ambient sound in a handheld display

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: Two contemporaneous readings on one carried tool expose the amount of nearby ambient sound and the sound the controlled actor is making. Their relative heights indicate an opportunity to act with less acoustic exposure.
- Includes: Read the environment on the left phonometer column and Alex’s current sound on the right. Watch the two while changing pace or picking a route.
- Excludes: A single suspicion indicator, a map of hostile positions, a raw display of any one audio amplitude, or a numerical distance or immunity guarantee.
- Parameters: Tool, current background, current emission, two simultaneous readings and relative height.
- Evidence: [A Quiet Place: The Road Ahead decomposition](../games/a-f/a-quiet-place-the-road-ahead.md), AQP-003. The Xbox Series X capture, publisher captioned diaries and the independent garage capture support the scoped rules. Exact sound coefficients are unmeasured.
- Novelty: first isolated for `GAME-0653`. See [TAXONOMY_CHANGE_399](../../research/taxonomy-changes/TAXONOMY_CHANGE_399.md). No external novelty claim.

## INF-604 — Expose chip compatibility and the active queue head in distinct combat views

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: The preparation view shows the visible offer and selected order with item codes or names. During live action the interface shows the ready item, remaining entries, recharge status and combatants’ current health and positions.
- Includes: Read ten options with codes and their current selection in the paused view. After transmission read MiniBomb at the head, then watch its indicator disappear on use.
- Excludes: Showing only a trait catalogue outside combat, listing every future draw or displaying a readiness meter without its paired preparation or live item status.
- Parameters: Offered names and codes, selection order, next usable item, remaining count, recharge, health and field position.
- Evidence: [Mega Man Battle Network decomposition](../games/m-r/mega-man-battle-network.md), BN1-002, BN1-005, BN1-006. The original Game Boy Advance manual and attributed cartridge-era recordings support the scoped sequence.
- Novelty: first isolated for `GAME-0652`. See [TAXONOMY_CHANGE_398](../../research/taxonomy-changes/TAXONOMY_CHANGE_398.md). No external novelty claim.

## INF-603 — Distinguish movable story words, vacant slots and nearby portal actions in place

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: The scene keeps sentence wording at its local referent and distinguishes editable words or vacant positions. The held word remains identifiable, and a visible spiral and contextual prompt mark an available page transfer.
- Includes: Read FULL at its source, see the vacancy left there, carry the word to the moat sentence and use the green spiral prompts to change plane.
- Excludes: An abstract vocabulary list without spatial referents, decorative printed flavour text alone or a portal preview of an otherwise unseen destination.
- Parameters: Sentence text, editable marking, vacancy, held word, portal mark and prompt.
- Evidence: [The Plucky Squire decomposition](../games/s-z/the-plucky-squire.md), PLUCK-002, PLUCK-003, PLUCK-004. The developer material and attributed PS5 footage support the scoped sequence.
- Novelty: first isolated for `GAME-0651`. See [TAXONOMY_CHANGE_397](../../research/taxonomy-changes/TAXONOMY_CHANGE_397.md). No external novelty claim.

## INF-602 — Expose individual mounted weapon readiness and the hit gauge

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: The live view identifies available enemy weapon salvage and each fitted weapon type, reserve and damage condition. It also reports the current hit gauge, multiplier and score while the player can still act.
- Includes: Read Vulcan over the disabled carrier and then inspect its type, ammo and colour in the weapon window.
- Excludes: A shop-only weapon catalogue, unlabelled scenery effects, a single unstated shared weapon reserve or a result with no live feedback.
- Parameters: Salvage label, mounted type, reserve, condition, hit gauge, multiplier and score.
- Evidence: [Einhänder decomposition](../games/a-f/einhander.md), EIN-003, EIN-005, EIN-006. The printed manual and attributed PlayStation footage support the scoped sequence.
- Novelty: first isolated for `GAME-0650`. See [TAXONOMY_CHANGE_396](../../research/taxonomy-changes/TAXONOMY_CHANGE_396.md). No external novelty claim.

## INF-601 — Show work progress through relative depth and visible instrument scale

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: The work scene keeps its target visible while showing successive paths at changing depths. The implement grows in apparent size as it approaches the target, communicating practical proximity to the terminal interaction.
- Includes: See the mower small against the skyline on an early pass and large next to the two foreground flowers near the end.
- Excludes: A numerical progress bar, a cosmetic camera zoom with no corresponding effective approach, or an exact hidden pass counter inferred from apparent size.
- Parameters: Fixed target view, visible work path, implement scale and approximate relative depth.
- Evidence: [Thank Goodness You're Here! decomposition](../games/s-z/thank-goodness-youre-here.md), TGY-004, TGY-005. The Nintendo Switch store and two attributed captures support the scoped encounter.
- Novelty: first isolated for `GAME-0648`. See [TAXONOMY_CHANGE_394](../../research/taxonomy-changes/TAXONOMY_CHANGE_394.md). No external novelty claim.

## INF-600 — Show enemy-relative sector danger and the combatant’s current quadrant

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: A four-sector battle indicator displays the combatant’s position about the enemy formation and labels the sectors by their current threat, so a player can choose where to wait or attack.
- Includes: Read the dragon marker against the green safe sector, neutral ordinary sector and red high-danger sector.
- Excludes: An exploration radar for the chance of starting a battle, a reticle displaying pending locks, fixed direction markers with no danger classification or exact damage estimates.
- Parameters: Enemy formation, combatant position, four sectors, danger classes and current attack potential.
- Evidence: [Panzer Dragoon Saga decomposition](../games/m-r/panzer-dragoon-saga.md), PDS-003 and PDS-005. The original Sega booklet and attributed disc 1 recordings delimit the scope.
- Novelty: first isolated for `GAME-0647`. See [TAXONOMY_CHANGE_393](../../research/taxonomy-changes/TAXONOMY_CHANGE_393.md). No external novelty claim.

## INF-599 — Highlight and name each newly opened world-map destination

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: When an event opens map nodes, the display temporarily singles out their positions and names before returning the player to node selection.
- Includes: Read the title of the newly opened village and then the title of the newly opened plain on the same map.
- Excludes: A generic success message without destination positions, revealing one mandatory next objective, or assuming every hidden destination is disclosed.
- Parameters: Opened node position, title label, highlight cue and return to map selection.
- Evidence: [Wario Land 3 decomposition](../games/s-z/wario-land-3.md), WL-005 and WL-006. The original Nintendo booklet and both attributed cartridge-era traces delimit the scope.
- Novelty: first isolated for `GAME-0645`. See [TAXONOMY_CHANGE_391](../../research/taxonomy-changes/TAXONOMY_CHANGE_391.md). No external novelty claim.

## INF-598 — Expose the spring state separately from the elapsed result and crown bands

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: A live spring control and its nearby filling indicator show a varying local action state. Once the finish is settled, a distinct gauge shows elapsed time, its rating bands and the resulting crown.
- Includes: Watch the spring indicator while approaching a gap and read the displayed time and crown after the checkered finish.
- Excludes: Treating the spring indicator as an elapsed timer, displaying only a leaderboard placement, or claiming a precise spring refill rate from sampled video.
- Parameters: On-course spring cue, local action indicator, finished elapsed time, labelled crown and rating bands.
- Evidence: [WHAT THE CAR? decomposition](../games/s-z/what-the-car.md), WC-003 and WC-006. The Apple and Triband sources and attributed touch captures delimit the scope.
- Novelty: first isolated for `GAME-0644`. See [TAXONOMY_CHANGE_390](../../research/taxonomy-changes/TAXONOMY_CHANGE_390.md). No external novelty claim.

## INF-597 — Display rocket readiness beside present vitality and run stock

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: The play view shows a visibly filling rocket-energy gauge apart from current vitality, score and remaining player stock. The charge display lets the player choose when to release while live terrain and threats remain in view.
- Includes: Read the changing charge indicator before the vertical castle passage and distinguish it from the red vitality icons and REST counter.
- Excludes: Inferring charge solely from elapsed time, a score bar masquerading as readiness, a single shared depletion pool or a paired fighter HUD with a round timer.
- Parameters: Charge fill, full cue, vitality icons, score, stock and simultaneous play view.
- Evidence: [Rocket Knight Adventures decomposition](../games/m-r/rocket-knight-adventures.md), RK-003 and RK-005. The North American manual and attributed captures delimit the scope.
- Novelty: first isolated for `GAME-0643`. See [TAXONOMY_CHANGE_389](../../research/taxonomy-changes/TAXONOMY_CHANGE_389.md). No external novelty claim.

## INF-596 — Consult a damaged recipe with partial text and geometric instructions

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: Open an authored recipe at the workstation. It exposes tools, ingredients and spatial diagrams while damaged text leaves at least one preparation or arrangement relationship to infer.
- Includes: The idli recipe shows the perforated plates and an illustrated path for steam. A damaged part of the text leaves the player to interpret how the plate is lined and stacked.
- Excludes: A complete menu-selected recipe, a generated dependency tree, a fully hidden rule with no symbolic clue or entering a recovered written answer as a key.
- Parameters: Recipe page, damaged span, visible supplies, spatial diagram and remaining inference.
- Evidence: [Venba decomposition](../games/s-z/venba.md), VB-002. The Xbox release listing, developer interview and attributed captures delimit the scope.
- Novelty: first isolated for `GAME-0642`. See [TAXONOMY_CHANGE_388](../../research/taxonomy-changes/TAXONOMY_CHANGE_388.md). No external novelty claim.

## INF-595 — Read live weapon contact and body outcomes through distinct flashes and poses

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: Weapon and body feedback distinguish defence, weapon collision, nonterminal injury and decisive contact through local visual effects and body posture. The live duel has no displayed health bar or round timer.
- Includes: The booklet distinguishes the contact colours. The combat view shows differing weapon heights and a flash before both participants continue; the terminal effect leads into a fall and replay.
- Excludes: An external split timer, a numerical health estimate, proof of a particular input from a pose, or a scored match statistics screen.
- Parameters: Contact cue, stance, animation, incapacitation, terminal cue and visible HUD.
- Evidence: [Bushido Blade decomposition](../games/a-f/bushido-blade.md), BB-004 through BB-007. The North American disc material and attributed captures delimit the scope.
- Novelty: first isolated for `GAME-0641`. See [TAXONOMY_CHANGE_387](../../research/taxonomy-changes/TAXONOMY_CHANGE_387.md). No external novelty claim.

## INF-594 — Show live points and rank beside the combo and conditional escape clock

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: The running interface displays accumulated points and their current letter tier separately from the current combo indicator. It adds a remaining-time display when the escape phase begins.
- Includes: In John Gutter, the upper HUD shows points, tier and combo. After Pillar John breaks, a separate clock appears below the route.
- Excludes: A results-only leaderboard, a timer that starts with the first step, complete point-formula disclosure or a combo counter treated as the final rank.
- Parameters: Current points, letter tier, combo count and meter, return phase and remaining time.
- Evidence: [Pizza Tower decomposition](../games/m-r/pizza-tower.md), PT-004 through PT-006. The Steam listing and attributed release-era recordings delimit the scope.
- Novelty: first isolated for `GAME-0640`. See [TAXONOMY_CHANGE_386](../../research/taxonomy-changes/TAXONOMY_CHANGE_386.md). No external novelty claim.

## INF-593 — Expose ammunition, vitality, elapsed time and the live score chain

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: During the arena, separate displays disclose current ammunition and its warning, player vitality, elapsed time and the active score-chain multiplier and value.
- Includes: The Rollerdrome Matterhorn Arena display, with Dual Pistols changing between an empty warning and usable rounds, a separate health panel and live combo feedback.
- Excludes: Only a settled rank or score, an invisible enemy wave count, an exact predictive damage report or a time display that alone establishes a terminal deadline.
- Parameters: Ammunition count and warning, vitality, elapsed time, live multiplier and chain value.
- Evidence: [Rollerdrome decomposition](../games/m-r/rollerdrome.md), DROME-003 and DROME-005. The Roll7 description and attributed PS4 captures delimit the scope.
- Novelty: first isolated for `GAME-0639`. See [TAXONOMY_CHANGE_385](../../research/taxonomy-changes/TAXONOMY_CHANGE_385.md). No external novelty claim.

## INF-592 — Separate rescue accounting, time and per-skill stock in a live panel

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: While a population rescue runs, a control panel shows the surviving tribe headcount and the credited rescued subset separately, along with the remaining level time and uses of each local skill.
- Includes: The original Amiga Lemmings 2 Beach 1 panel with a retained tribe count, an increasing rescue count, a decreasing clock and separately decrementing role stocks.
- Excludes: A single kill or progress total, end-of-level results only, level-wide terrain visibility, and an undisclosed exact medal threshold.
- Parameters: Population counters, remaining time, discrete skill types, per-skill remaining uses and refresh after events.
- Evidence: [Lemmings 2: The Tribes decomposition](../games/g-l/lemmings-2-the-tribes.md), TRIBES-002 and TRIBES-005. The Amiga manual and attributed gameplay delimit the scope.
- Novelty: first isolated for `GAME-0638`. See [TAXONOMY_CHANGE_384](../../research/taxonomy-changes/TAXONOMY_CHANGE_384.md). No external novelty claim.

## INF-591 — Show the active surface brush footprint on the terrain

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: A cursor-local outline drawn on the edit surface shows the reach of the currently selected adjustable brush before or during its stroke, letting the player target the covered area.
- Includes: The circle projected onto the glade while the path tool is aimed and dragged in Tiny Glade.
- Excludes: A point cursor without size information, a preview of the exact finished arch, a combat reticle or a whole-level placement legality map.
- Parameters: Active brush, centre, displayed footprint, size adjustment and world surface.
- Evidence: [Tiny Glade decomposition](../games/s-z/tiny-glade.md), GLADE-003 and GLADE-004. The release-window play trace and illustrated player guide define the observed scope.
- Novelty: first isolated for `GAME-0637`. See [TAXONOMY_CHANGE_383](../../research/taxonomy-changes/TAXONOMY_CHANGE_383.md). No external novelty claim.

## INF-590 — Show the addressed hotspot and pending inventory-to-target command

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: When the pointer addresses an interactive object, show its label. While an inventory item is selected, represent it at the cursor and display the proposed item-to-target command before it resolves.
- Includes: The Dig labels for the asteroid sites and the pending Use command joining a carried item and a world target.
- Excludes: A guarantee that the proposed pairing will succeed, an all-hotspots minimap, an already settled operation and a permanent general interaction hint.
- Parameters: Cursor context, target label, selected item, pending pair description and resolution timing.
- Evidence: [The Dig decomposition](../games/s-z/the-dig.md), DIG-002–DIG-004. The LucasArts documentation and attributed DOS captures support the scoped behavior as specified in the claim ledger.
- Novelty: first isolated for `GAME-0636`. See [TAXONOMY_CHANGE_382](../../research/taxonomy-changes/TAXONOMY_CHANGE_382.md). No external novelty claim.

## INF-589 — Expose the current remembered period and the direction of a possible jump

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: Identify the active memory with its period number and label, distinguish another available period, and expose the directional hold prompt. The player can read which school manifestation is active and which chronological jump is offered.
- Includes: The numbered Temperature Days and Day of the Dance view and the past or future prompts once both are available.
- Excludes: A linear level number, complete knowledge of all periods, an exact route map and a replay menu used outside Communion.
- Parameters: Current period index, descriptive label, displayed date where known, neighbouring period and jump prompt.
- Evidence: [1000xRESIST decomposition](../games/0-9/1000xresist.md), RES-004–RES-006. The publisher, developer and two attributed Nintendo Switch recordings support the scoped behavior as specified in the claim ledger.
- Novelty: first isolated for `GAME-0635`. See [TAXONOMY_CHANGE_381](../../research/taxonomy-changes/TAXONOMY_CHANGE_381.md). No external novelty claim.

## INF-588 — Show outward-moving cues and their position or pose target

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: Show incoming cues travelling from the centre to a fixed array of paired coloured targets, with an explicit prompt for rapid shakes or a pose silhouette. Show the immediate judgement alongside the live rank and gauge.
- Includes: The six-circle playfield, ordinary Rhythm Balls, rapid-shake prompts, Pose Marks and the local result or performance display.
- Excludes: A full track chart available before play, measured sensor altitude, scrolling fret lanes or direction-only dance arrows.
- Parameters: Visible cue horizon, circle colour and height, silhouette, judgement, live rank and gauge.
- Evidence: [Samba de Amigo decomposition](../games/s-z/samba-de-amigo.md), SAM-003–SAM-005. The Sega Dreamcast manual and attributed maraca footage support the scoped behavior as specified in the claim ledger.
- Novelty: first isolated for `GAME-0634`. See [TAXONOMY_CHANGE_380](../../research/taxonomy-changes/TAXONOMY_CHANGE_380.md). No external novelty claim.

## INF-587 — Show target charm distance, own live range and progress separately

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: During charm the display exposes a target’s reference pair of wave brackets, a second pair that changes with the player’s relative position, and a separate charm progress indication. The player can adjust alignment before singing and read feedback after.
- Includes: The fixed and moving wave markers, graded label and vertical charm marker over a Basking Bewl in Flock.
- Excludes: A single proximity button without spatial feedback, an authored musical timeline independent of flight, or exact numeric thresholds that the interface does not reveal.
- Parameters: Target wave marks, own wave marks, relative distance, per-attempt feedback and charm progress.
- Evidence: [Flock decomposition](../games/a-f/flock.md), FLK-004, FLK-005. The documented Xbox release and its attributed gameplay traces support the scoped behavior as specified in the claim ledger.
- Novelty: first isolated for `GAME-0633`. See [TAXONOMY_CHANGE_379](../../research/taxonomy-changes/TAXONOMY_CHANGE_379.md). No external novelty claim.

## INF-586 — Read recurring boost readiness alongside separate engine warnings and condition

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: The live view displays recurring thrust readiness and active boost near speed, separately from a temperature warning and damage condition on the vehicle. The player can distinguish preparing or using boost from a reason to cancel it, and can read whether vehicle repair is needed.
- Includes: Reading the thrust lamp, heat warning and two engine condition diagrams during the first Nintendo 64 race in Star Wars Episode I: Racer.
- Excludes: A visible stored fuel gauge, a single meter used for both vehicle vitality and boost, a one-off start warm-up, or exact hidden temperature values.
- Parameters: Current speed, thrust readiness, active boost, temperature warning and per-engine condition.
- Evidence: [Star Wars Episode I: Racer decomposition](../games/s-z/star-wars-episode-i-racer.md), RAC-003, RAC-004. The PAL manual and attributed Nintendo 64 gameplay support the scoped behavior as specified in the claim ledger.
- Novelty: first isolated for `GAME-0632`. See [TAXONOMY_CHANGE_378](../../research/taxonomy-changes/TAXONOMY_CHANGE_378.md). No external novelty claim.

## INF-585 — Expose participation before settlement and reveal true roles in the result

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: During the scenario the player sees their own assigned role and a named roster with participation state, without a complete true allegiance mapping. Public statements and recorded ballots can inform inference. The terminal report discloses the actual roles of the full original roster, including removed participants.
- Includes: The crew player and five profiles during Gnosia’s opening, then the final report showing which one was really Gnosia.
- Excludes: Showing every true role during discussion, treating allegations or tallies as proven allegiance, or an unknown identity pool that only appears at settlement.
- Parameters: Own role, known participant identity, current availability, visible statements and votes, and terminal role reveal.
- Evidence: [Gnosia decomposition](../games/g-l/gnosia.md), GN-002, GN-004–GN-006. The launch notices and attributed Japanese PlayStation Vita traces support the scoped behavior as specified in the claim ledger.
- Novelty: first isolated for `GAME-0630`. See [TAXONOMY_CHANGE_376](../../research/taxonomy-changes/TAXONOMY_CHANGE_376.md). No external novelty claim.

## INF-584 — Show recovered structures and loose parts with resident-revealed slot identities

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: The part panel distinguishes recovered foundations, their placement and installed state, and the available loose components. Some required sockets remain unknown until the relevant resident reveals the kind of part required.
- Includes: Paige’s House has an unknown slot before Pike describes the wheel, and its revealed slot can be inspected separately from the loose wheel in Dark Cloud.
- Excludes: A full recipe list known from the start, knowledge inferred solely by trying every part, current placement geometry alone, or treating spoken wishes as already installed parts.
- Parameters: Foundation entry, available component stock, slot identity, information source and installed state.
- Evidence: [Dark Cloud decomposition](../games/a-f/dark-cloud.md), DCL-004–DCL-007. The original manual and US PlayStation 2 trace support the scoped behavior as specified in the claim ledger.
- Novelty: first isolated for `GAME-0629`. See [TAXONOMY_CHANGE_375](../../research/taxonomy-changes/TAXONOMY_CHANGE_375.md). No external novelty claim.

## INF-583 — Expose an ordered threat strip alongside pending warnings and usable skill patterns

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `Medium`
- Definition: The road-event display pairs a fixed-order line of resource threat icons with pending attack warnings, and shows the ordered pattern, remaining uses and applicable costs of each visible skill. The player can assess a placement and its likely resource trade before applying it.
- Includes: Reading the durability icon under the gap of Relax and the one-Energy Have a Go in the first Keep Driving Tractor event.
- Excludes: A general hazard warning, an enemy damage number with no placement strip, a resource gauge alone, or a guarantee that all future threats are visible.
- Parameters: Threat order and types, warning state, displayed pattern, remaining uses, activation cost and relevant resource stock.
- Evidence: [Keep Driving decomposition](../games/g-l/keep-driving.md), KD-002–KD-004. The retail-period Windows openings support the scoped behavior as specified in the claim ledger.
- Novelty: first isolated for `GAME-0628`. See [TAXONOMY_CHANGE_374](../../research/taxonomy-changes/TAXONOMY_CHANGE_374.md). No external novelty claim.

## INF-582 — Signal a nearby concealed hostile with its characteristic sound before revelation

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `Medium`
- Definition: A nearby concealed opponent emits a recognisable sound during ordinary traversal. The cue is actionable evidence that a threat is present before the player can see its full body or choose a precise aim point.
- Includes: The reported Heaven Smile laugh cues a player to stop and reveal the nearby hostile in Killer7.
- Excludes: A persistent exact enemy icon, a graded suspicion display, a sound-only input test, a musical hit cue, or assuming the warning discloses exact position or a weak point.
- Parameters: Eligible concealed hostile, recognisable cue, current vicinity, ordinary traversal and information absent before the reveal.
- Evidence: [Killer7 decomposition](../games/g-l/killer7.md), K7-004. The original manual and GameCube opening traces support the scoped behavior as specified in the claim ledger.
- Novelty: first isolated for `GAME-0627`; see [TAXONOMY_CHANGE_373](../../research/taxonomy-changes/TAXONOMY_CHANGE_373.md). No external novelty claim.

## INF-581 — Show the active weapon category and the target’s exposed weakness marker before commitment

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `Medium`
- Definition: Before the player commits an attack, the combat view identifies the current operator’s weapon class and presents an exposed target weakness as a typed marker separate from health. The player can compare these presented classes without first spending a scan or an attack.
- Includes: The opening Taranis battle in Fuga: Melodies of Steel presents the acting gunner’s category and the enemy’s yellow weakness marker before the matching attack.
- Excludes: A weakness inferred only from previous damage, paid or learned scan results, a forecast showing turn order without weapon compatibility, or a single health bar whose colour indicates only depletion.
- Parameters: Acting operator, weapon category, visible target, weakness class and exposure state, health display and pre-commit availability.
- Evidence: [Fuga: Melodies of Steel decomposition](../games/a-f/fuga-melodies-of-steel.md), FUG-002, FUG-003. The Xbox opening traces and developer battle guide support the scoped behavior as specified in the claim ledger.
- Novelty: first isolated for `GAME-0626`; see [TAXONOMY_CHANGE_372](../../research/taxonomy-changes/TAXONOMY_CHANGE_372.md). No external novelty claim.

## INF-580 — Expose aerial acquisition and flight readiness beside separate finite stocks

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `Medium`
- Definition: A pursuit view marks an acquired aircraft and changes the cue when a missile obtains its lock. A separate boost lamp shows current readiness or activity, distinct from the remaining guided shots, replacement craft and score.
- Includes: Blue Lightning’s targeting square and red lock indication alongside afterburner lamp, missile stock, remaining jets and points.
- Excludes: A radar map of all contacts, a timed acquisition-progress bar, a cockpit power-allocation interface or progress inferred solely from points.
- Parameters: Labeled target, acquisition and missile-lock cues, ready and active lamp, missile count, reserve aircraft and score.
- Evidence: [Blue Lightning decomposition](../games/a-f/blue-lightning.md), BL-003, BL-004. The Atari instructions and Lynx traces support the scoped behavior as specified in the claim ledger.
- Novelty: first isolated for `GAME-0623`; see [TAXONOMY_CHANGE_369](../../research/taxonomy-changes/TAXONOMY_CHANGE_369.md). No external novelty claim.

## INF-579 — Preview candidate routes and mark the committed shared gateway

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `Medium`
- Definition: At a live shared-course decision, the road-visible gates supply a preview or identity cue for the offered route. After commitment, the selected gateway visibly indicates the path the remaining racers can use.
- Includes: The candidate imagery and chosen Travel Ring into Dinosaur Jungle in Sonic Racing: CrossWorlds.
- Excludes: An item-slot icon, a fully exposed future track map, a menu outside the race or a promise that every candidate exposes its exact destination.
- Parameters: Gate cue, candidate route, preview coverage, visibility after commitment and follower view.
- Evidence: [Sonic Racing: CrossWorlds decomposition](../games/s-z/sonic-racing-crossworlds.md), SRC-003, SRC-004. The Sega rules and the post-launch race traces support the scoped behavior as specified in the claim ledger.
- Novelty: first isolated for `GAME-0621`; see [TAXONOMY_CHANGE_367](../../research/taxonomy-changes/TAXONOMY_CHANGE_367.md). No external novelty claim.

## INF-578 — Reveal a boss weak-point reticle subject to firing and weapon state

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `Medium`
- Definition: A weak-point reticle marks a local boss target after sufficient time without firing for eligible weapons. A homing weapon can keep the cue visible while attacking, while specified other types suppress the ordinary cue.
- Includes: Eagle Eye in Alien Soldier marks a boss target when firing stops or Homing Force sustains the cue. Sword Force and Lancer Force are the documented exceptions.
- Excludes: A universal health bar, a start-of-fight reveal for every weapon, a target lock that guarantees a hit, a revealed hitbox formula, or a permanent learned target record.
- Parameters: Boss part, idle period, selected weapon, visibility exception and marker appearance.
- Evidence: [Alien Soldier decomposition](../games/a-f/alien-soldier.md), ALS-007. The Japanese Sega manual and the opening combat traces support the scoped behavior as specified in the claim ledger.
- Novelty: first isolated for `GAME-0620`; see [TAXONOMY_CHANGE_366](../../research/taxonomy-changes/TAXONOMY_CHANGE_366.md). No external novelty claim.

## INF-577 — Expose active-unit reach and local target properties before committing its command

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `Medium`
- Definition: The tactical display identifies the current unit and highlights currently reachable cells. A field cursor reveals an addressed unit and its known local statistics; the battle display separates the current cell’s defensive terrain value and a favourable weapon relation from eligibility to attack.
- Includes: In Saraband, the active panel shows name, class, HP, MP and LE; the target panel shows the addressed monk, and the North American booklet explains the cursor and exclamation cue.
- Excludes: An authored future hostile move, a complete visible initiative sequence, movement highlights guaranteeing attack range, or inferring a nonzero terrain bonus from a city reading of zero.
- Parameters: Active actor, highlighted cells, cursor target, local statistics, terrain value and weapon relation cue.
- Evidence: [Shining Force III decomposition](../games/s-z/shining-force-iii.md), SF3-003, SF3-005. The North American Sega manual and the English battle traces support the scoped behavior as specified in the claim ledger.
- Novelty: first isolated for `GAME-0618`; see [TAXONOMY_CHANGE_364](../../research/taxonomy-changes/TAXONOMY_CHANGE_364.md). No external novelty claim.

## INF-576 — Expose different authored artefact traits by inspection channel alongside a reference entry

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `Medium`
- Definition: An authored reference supplies name and property clues for the requested identity. A selected artefact exposes different fixed readouts through separately selected sensory channels. The player connects the clues and readouts without receiving a validated name from a single inspection.
- Includes: The Hunter’s Boon entry describes a predator trophy. In the tooth’s inspection, appearance and Inner Perception offer distinct evidence channels. The accepted name appears after the offer, not on opening inspection.
- Excludes: One unchanging detail panel, a literal reference picture of every specimen, a tracking signal that conveys proximity alone, or a handwritten label treated as identification evidence.
- Parameters: Identity entry, diagnostic channels, fixed readouts, visible shape and withheld confirmed name.
- Evidence: [Strange Antiquities decomposition](../games/s-z/strange-antiquities.md), SAQ-003, SAQ-004. The Switch captures and contemporary route support the scoped behavior as specified in the claim ledger.
- Novelty: first isolated for `GAME-0617`; see [TAXONOMY_CHANGE_363](../../research/taxonomy-changes/TAXONOMY_CHANGE_363.md). No external novelty claim.

## INF-575 — Mark required targets and expose their resolved count while control continues

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `Medium`
- Definition: The live view identifies visible members of the required target set as such and reports the number resolved against the fixed total. It does not reveal the positions of all remaining objects.
- Includes: Silent Bomber Mission 01 shows TARGET tags on the marked fixtures and a live count out of eleven. An ordinary enemy without the mark need not increment it.
- Excludes: A list of all hidden target coordinates, a counter of physical proof items collected after a defeat, an ordinary score total or one guardian’s remaining health.
- Parameters: Visible target identity, finite required set, resolved count and total count.
- Evidence: [Silent Bomber decomposition](../games/s-z/silent-bomber.md), SBOM-005. The North American manual and game traces support the scoped behavior as specified in the claim ledger.
- Novelty: first isolated for `GAME-0616`; see [TAXONOMY_CHANGE_362](../../research/taxonomy-changes/TAXONOMY_CHANGE_362.md). No external novelty claim.

## INF-574 — Expose owned plot data and current match ledgers alongside inspected card and combat totals

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `Medium`
- Definition: The interface provides the current spendable and qualifying totals, position and checkpoint state, and allows inspection of plot ownership, attribute, level and toll. The current cards and proposed combat contributions can be inspected before commitment.
- Includes: Dunnan separates both G values, exposes land data and displays attainable combat strength and vitality before paid item selection.
- Excludes: Showing only final rank, exposing a future random draw or roll, or promising the predicted combat outcome regardless of the opponent’s item.
- Parameters: Spendable and qualifying total, route position, checkpoint, inspectable land and cards, pre-commit combat contributions.
- Evidence: [Culdcept decomposition](../games/a-f/culdcept.md), CUL-002, CUL-003, CUL-007, CUL-008. The North American instructions, English commercial match frames and firsthand route evidence support the scoped rules as specified in the claim ledger.
- Novelty: first isolated for `GAME-0611`; see [TAXONOMY_CHANGE_357](../../research/taxonomy-changes/TAXONOMY_CHANGE_357.md). No external novelty claim.

## INF-573 — Show known and unknown cravings beside the remaining enemy shield

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `Medium`
- Definition: The encounter display puts a target’s remaining shield near type clues for its vulnerabilities. The display distinguishes known types from unconfirmed slots and signals when the shielded state changes.
- Includes: Dosa Divas shows flavour symbols, question marks and remaining shield values beneath goons, and exposes the Stuffed state after a shield break.
- Excludes: A separate scan action as the only means of viewing the target, exact next enemy commands or displaying health alone.
- Parameters: Target, remaining shield, known flavour, unknown slot and incapacitation indicator.
- Evidence: [Dosa Divas decomposition](../games/a-f/dosa-divas.md), DD-003, DD-004. The PlayStation listing, commercial PS5 frames and firsthand PS5 route report support the scoped rules as specified in the claim ledger.
- Novelty: first isolated for `GAME-0608`; see [TAXONOMY_CHANGE_354](../../research/taxonomy-changes/TAXONOMY_CHANGE_354.md). No external novelty claim.

## INF-572 — Show a stage letter grade and elapsed result beside the earlier time

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `Medium`
- Definition: After clearing an authored stage, the result view exposes the letter grade, the completed elapsed time and a separately identified previous time when one exists.
- Includes: Mischief Makers reports rank, current time and the earlier stage time in the console result view; cleared stages also have rank marks in stage selection.
- Excludes: A live stamina or timer gauge, a single race leaderboard placement, undisclosed grade thresholds, automatic retention of every secondary pickup.
- Parameters: Stage, grade, current elapsed time, previous time or empty placeholder, result display.
- Evidence: [Mischief Makers decomposition](../games/m-r/mischief-makers.md), MM-006, MM-007. The Nintendo booklet, commercial N64 frames and firsthand route reports support the scoped rules as specified in the claim ledger.
- Novelty: first isolated for `GAME-0607`; see [TAXONOMY_CHANGE_353](../../research/taxonomy-changes/TAXONOMY_CHANGE_353.md). No external novelty claim.

## INF-571 — Show an authored investigation graph with recorded evidence and unresolved lead nodes

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `Medium`
- Definition: the open case displays a connected map of named leads, people and evidence traces. Recorded and unfinished entries are visually distinguishable, and relevant evidence can be inspected again before synthesis.
- Includes: Follow Miss Deane’s Departure from the reception lead to the registered document comparison on its mind map.
- Excludes: A fully populated answer key, an unstructured note list, an external guide or a physical map of the building alone.
- Parameters: Case, named node, authored dependency links, known status, revisitable evidence and hypothesis readiness.
- Evidence: [The Séance of Blake Manor decomposition](../games/s-z/the-seance-of-blake-manor.md), BM-002, BM-003, BM-007, BM-008. The commercial Steam capture and firsthand route report support the scoped rules as specified in the claim ledger.
- Novelty: first isolated for `GAME-0606`; see [TAXONOMY_CHANGE_352](../../research/taxonomy-changes/TAXONOMY_CHANGE_352.md). No external novelty claim.

## INF-570 — Separate attempt scoring from the selected challenge’s retained completion mark

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `Medium`
- Definition: a settled attempt exposes distinguishable stage and remaining-time score components, and the challenge selection shows a separate completion mark on the corresponding challenge. A score display therefore does not substitute for checking which challenge is recorded as cleared.
- Includes: Read Stage Score and Time Bonus for Novice Mission 1, then return to the grid and locate the emblem under 1.
- Excludes: An in-progress counter, a single badge that encodes undisclosed scoring factors or a save/reload claim inferred from visiting the selection screen.
- Parameters: Challenge identity, score components, terminal result, completion mark and selection screen.
- Evidence: [Outtrigger decomposition](../games/m-r/outtrigger.md), OT-006, OT-007. The original US manual and independently recorded Dreamcast frames support the scoped rules as specified in the claim ledger.
- Novelty: first isolated for `GAME-0605`; see [TAXONOMY_CHANGE_351](../../research/taxonomy-changes/TAXONOMY_CHANGE_351.md). No external novelty claim.

## INF-569 — Expose timed full-collection instructions with a live clock and local pickup guidance

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `Medium`
- Definition: the challenge discloses that all designated pickups are required and shows the remaining time during the attempt, along with a local visible cue at an eligible pickup.
- Includes: Follow the Get it! cue to a medal while the separate countdown is still running. Follow the cue to the pickup rather than treating it as a completion signal.
- Excludes: A static full route, a total shown only on the result screen, an enemy-count signal or an exact catalogue of every off-screen position.
- Parameters: Briefed collection objective, local cue, current allowance and refresh point.
- Evidence: [Outtrigger decomposition](../games/m-r/outtrigger.md), OT-002–OT-004. The original US manual and independently recorded Dreamcast frames support the scoped rules as specified in the claim ledger.
- Novelty: first isolated for `GAME-0605`; see [TAXONOMY_CHANGE_351](../../research/taxonomy-changes/TAXONOMY_CHANGE_351.md). No external novelty claim.

## INF-568 — Expose stocked departure fuel alongside the current mass-derived requirement

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `Medium`
- Definition: the base and departure interfaces distinguish usable fuel stock, current assembled mass and the journey’s required cost before commitment, allowing the player to detect a shortfall independently of the repair objective.
- Includes: On the command terminal, compare the current Organics with the Journey Cost before starting the first Journey.
- Excludes: A distance-only route preview, a generic ready light, the tutorial collection target by itself or the entire future cost schedule.
- Parameters: Current mass, displayed cost, stored fuel and departure confirmation state.
- Evidence: [The Alters decomposition](../games/s-z/the-alters.md), TA-006–TA-008. The publisher account, walkthroughs and static commercial Xbox frames support these boundaries as specified in the claim ledger.
- Novelty: first isolated for `GAME-0604`; see [TAXONOMY_CHANGE_350](../../research/taxonomy-changes/TAXONOMY_CHANGE_350.md). No external novelty claim.

## INF-567 — Preview past decision alternatives with their crew-role consequences

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `Medium`
- Definition: the timeline exposes a character’s recorded life path and an actionable supplied alternative together with the prospective crew role before the player confirms the branch.
- Includes: Read the original Going Away line and inspect Staying Behind with the Technician role.
- Excludes: A calendar, a future travel map, a generic party class menu with no link to an earlier life decision or discovering the role only after waking the crew member.
- Parameters: Life timeline, historical decision, available alternative, role disclosure and confirmation surface.
- Evidence: [The Alters decomposition](../games/s-z/the-alters.md), TA-004, TA-005. The publisher account, walkthroughs and static commercial Xbox frames support these boundaries as specified in the claim ledger.
- Novelty: first isolated for `GAME-0604`; see [TAXONOMY_CHANGE_350](../../research/taxonomy-changes/TAXONOMY_CHANGE_350.md). No external novelty claim.

## INF-566 — Distinguish stored cycling boost from its active spending

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `Medium`
- Definition: the riding interface displays the current acceleration reserve and visibly indicates when the rider is actively spending it for a boost. The information is available during the same steering decisions that use it.
- Includes: Read the segmented reserve, then notice the active indication when Kat accelerates along the first lap.
- Excludes: The current place alone, a physical speed pickup, shared vehicle survival energy or an exact future boost duration.
- Parameters: Available reserve, charge display, current spend indication, riding state and tutorial briefing.
- Evidence: [Wheel World decomposition](../games/s-z/wheel-world.md), WW-005, WW-006. The creative director’s notes and still frames from the two early PC traces support these boundaries.
- Novelty: first isolated for `GAME-0603`; see [TAXONOMY_CHANGE_349](../../research/taxonomy-changes/TAXONOMY_CHANGE_349.md). No external novelty claim.

## INF-565 — Expose local flight energy and target bearing on live instruments

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `Medium`
- Definition: the flight interface shows current speed and height beside a radar that reports target directions and relative target height. It identifies areas of local lift and acknowledges eligible ring passage.
- Includes: Check speed before flaring, compare the glider height with target markers, and use the orange thermal region alongside the world view.
- Excludes: An out-of-game annotated map, a guarantee that a marked thermal is reachable at the current height or a scripted future route that steers the craft.
- Parameters: Speed, altitude indicators, relative bearings and height, thermal locations and ring-clear notification.
- Evidence: [Pilotwings 64 decomposition](../games/m-r/pilotwings-64.md), PW-004, PW-005. The original manual, flight stills and independent player accounts support the boundaries. The record distinguishes observed results from supplementary code paths.
- Novelty: first isolated for `GAME-0602`; see [TAXONOMY_CHANGE_348](../../research/taxonomy-changes/TAXONOMY_CHANGE_348.md). No external novelty claim.

## INF-564 — Expose active body health, personal move points and tape move details in combat

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `Medium`
- Definition: the turn-combat interface shows participants, current body or tape condition, personal action-resource markers and each inspected sticker move’s price and action details, so the player can judge an affordable command before commitment.
- Includes: Read the different health states while one actor is human, the orange action-point markers and the price and range on the sticker card.
- Excludes: A visible future enemy command, an explicit initiative forecast, a use counter separately tracked for each move or an out-of-game form reference.
- Parameters: Active people and forms, health, current reserve, selectable move, price and target details.
- Evidence: [Cassette Beasts decomposition](../games/a-f/cassette-beasts.md), CB-002, CB-004, CB-007. Developer-authored rules, in-game tutorial stills and independent mobile traces support the boundaries. Unobserved edge cases are identified in the record.
- Novelty: first isolated for `GAME-0601`; see [TAXONOMY_CHANGE_347](../../research/taxonomy-changes/TAXONOMY_CHANGE_347.md). No external novelty claim.

## INF-563 — Expose the live recording link, changing odds and settlement

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `Medium`
- Definition: while a creature’s form is being recorded, the screen identifies the active recorder and target via a visible link, shows the current chance of creating a record and then communicates the outcome through results or new tape state.
- Includes: Read the percentage over the wild Dominoth while the human holds the cassette player, then check the new recording and its bestiary entry.
- Excludes: Only a probability before a turn, a hidden future random number, a health bar without recording state or a notification that the creature has been removed.
- Parameters: Recording actor, target, visible link, current probability and successful or failed settlement.
- Evidence: [Cassette Beasts decomposition](../games/a-f/cassette-beasts.md), CB-004, CB-005. Developer-authored rules, in-game tutorial stills and independent mobile traces support the boundaries. Unobserved edge cases are identified in the record.
- Novelty: first isolated for `GAME-0601`; see [TAXONOMY_CHANGE_347](../../research/taxonomy-changes/TAXONOMY_CHANGE_347.md). No external novelty claim.

## INF-562 — Expose scoring, team style readiness and personal boost as distinct signals

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `Medium`
- Definition: the live interface exposes ordinary match score, separate style points, the team’s filling or ready special meter and its stored-charge indication, and the eligible player’s boost. Readiness and storage are distinguishable from scoring a basket.
- Includes: Read the score, Trick Points, the Gamebreaker indicator and Turbo reserve separately before deciding to shoot, pocket or wait.
- Excludes: A score-only scoreboard, one undifferentiated progress gauge, or hidden readiness without a visible signal.
- Parameters: Match score, style points, team gauge and stored state, personal gauge and current possession.
- Evidence: [NBA Street Vol. 2 decomposition](../games/m-r/nba-street-vol-2.md), NS-004, NS-005, NS-006. Printed PlayStation 2 instructions and independent captures or firsthand accounts support the rule boundaries. Not every branch was visible in the sampled frames.
- Novelty: first isolated for `GAME-0600`; see [TAXONOMY_CHANGE_346](../../research/taxonomy-changes/TAXONOMY_CHANGE_346.md). No external novelty claim.

## INF-561 — Expose line out and recoverable strain separately during tethered retrieval

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `Medium`
- Definition: the interface distinguishes a line-length reading from a live strain indicator, shows the moving hooked target and signals when steering or reel intervention is needed. This makes shortening the line legible separately from keeping it intact.
- Includes: The Lodge display shows Line Out in feet, a hooked bass in the water and the right-side line-tension bar, with a red danger state and contextual rod-direction commands.
- Excludes: A lone progress bar, an undisclosed native threshold, a whole-lake fish locator or one shared bar that sums all catches.
- Parameters: Payout distance, strain channel, target motion, danger display and contextual commands.
- Evidence: [Sega Bass Fishing decomposition](../games/s-z/sega-bass-fishing.md), BF-002, BF-005. The 1999 Sega Dreamcast booklet and independent Dreamcast captures support the described rule. Internal coefficients and native input were not tested.
- Novelty: first isolated for `GAME-0598`; see [TAXONOMY_CHANGE_344](../../research/taxonomy-changes/TAXONOMY_CHANGE_344.md). No external novelty claim.

## INF-560 — Expose the staged launch and both combatants’ health and knockdown state

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `Medium`
- Definition: the live arena presents the scheduled launch and each landed body’s unfolding countdown. During combat it presents the shared match clock and both participants’ remaining vitality and knockdown readiness or condition separately.
- Includes: The launch and cube indicators, paired HP and knockdown gauges and condition labels of the first Basic Arena duel.
- Excludes: Round wins tallied across a set, hidden bot choices, exact unmeasured hit values, or preview of an unchosen later loadout.
- Parameters: Launch cue, unfolding timer, match clock, participant, HP, knockdown bar and status.
- Evidence: [Custom Robo decomposition](../games/a-f/custom-robo.md), CR-004, CR-007, CR-008. The North American Nintendo booklet and independent English GameCube route traces support these boundaries. Exact hit and timing coefficients remain unknown.
- Novelty: first isolated for `GAME-0596`; see [TAXONOMY_CHANGE_342](../../research/taxonomy-changes/TAXONOMY_CHANGE_342.md). No external novelty claim.

## INF-559 — Cue a beat group and show its local treatment result

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `Medium`
- Definition: rhythmic lead pulses and a moving trace along a row identify the current group and its target. The interface distinguishes the outcome of the local response, with explicit counting help available in the guided introduction and removed before ordinary performance.
- Includes: The seven-beat teaching row and the solo Samurai Techno heart row, with a visible timing flash and a changing heart response.
- Excludes: A full preview chart, a stream of individually playable fret notes, instructor alternation with copied inputs, an independent survival reserve or exact cutoff values presented by the interface.
- Parameters: Cue channels, target row and rhythm, instruction state, feedback signal and target appearance.
- Evidence: [Rhythm Doctor decomposition](../games/m-r/rhythm-doctor.md), RD-003–RD-005. Xbox product and controller evidence plus independent first-case release-window traces support these boundaries. Exact console timing windows remain unknown.
- Novelty: first isolated for `GAME-0595`; see [TAXONOMY_CHANGE_341](../../research/taxonomy-changes/TAXONOMY_CHANGE_341.md). No external novelty claim.

## INF-558 — Expose framing, held charge, remaining film and both sides’ condition in a battle finder

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `Medium`
- Definition: an active photographic battle finder shows a subject acquisition opportunity and current shot charge together with the available film and remaining physical condition of the player and currently fought spirit. These readouts allow the player to distinguish a viable frame from enough charge to commit the exposure.
- Includes: the Fatal Frame finder pairing Capture Circle and Lock Circle with current Spirit Power, film, Mafuyu’s strength and Bound Man’s remaining power.
- Excludes: photo subject identification and roll count without combat state (INF-378); a rechargeable battery and post-processing indicator (INF-376); predicting exact future attack frames or damage before all conditions are known.
- Parameters: capture region, target acquisition, charge gauge, exposures, player vitality and target vitality
- Evidence: [Fatal Frame decomposition](../games/a-f/fatal-frame.md), FF-005 and FF-006. Tecmo’s booklet, the introductory tutorial and written and visual records of the PlayStation 2 route establish these boundaries. Exact timing and coefficients are unmeasured.
- Novelty: first isolated for `GAME-0591`; see [TAXONOMY_CHANGE_337](../../research/taxonomy-changes/TAXONOMY_CHANGE_337.md). No external novelty claim.

## INF-557 — Indicate nearby supernatural stimulus type and bearing before framing

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `Medium`
- Definition: a qualitative detector reacts to nearby supernatural subjects or clues during ordinary movement or finder use. Signal class distinguishes broad stimulus types and strength responds to proximity or facing. The cue alone does not resolve exact identity, intent or a valid exposure.
- Includes: the Filament glowing blue toward a clue or hidden spirit, or amber near a moving ghost, before the spirit enters the capture circle.
- Excludes: a target already acquired in the viewfinder; precise world coordinates; an exact hostile-intent preview; assuming every amber cue means an ongoing attack.
- Parameters: stimulus type, proximity, heading, relative cue strength, field mode and finder mode
- Evidence: [Fatal Frame decomposition](../games/a-f/fatal-frame.md), FF-003. Tecmo’s booklet, the introductory tutorial and written and visual records of the PlayStation 2 route establish these boundaries. Exact timing and coefficients are unmeasured.
- Novelty: first isolated for `GAME-0591`; see [TAXONOMY_CHANGE_337](../../research/taxonomy-changes/TAXONOMY_CHANGE_337.md). No external novelty claim.

## INF-556 — Show both drivers’ remaining duel reserves and relative separation

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `Medium`
- Definition: show the two competitors’ current remaining reserves together with an identified relative gap or lead cue during a live driving duel, so current attrition can be read separately from speed, gear and course progress.
- Includes: the two Spirit Point bars, Timid Challenger marker and relative distance cue during an active SP Battle.
- Excludes: a race place and lap counter with no remaining duel reserve; a single player health bar; an end-of-bout score screen; a hidden exact coefficient for applying damage.
- Parameters: reserve display for each competitor, identity, separation cue, current duel and refresh
- Evidence: [Tokyo Xtreme Racer decomposition](../games/s-z/tokyo-xtreme-racer.md), TXR-006. Genki and dated 1.0.0 stills establish the scoped released behavior, with corroborating independent play accounts. Exact coefficients are unmeasured.
- Novelty: first isolated for `GAME-0590`; see [TAXONOMY_CHANGE_336](../../research/taxonomy-changes/TAXONOMY_CHANGE_336.md). No external novelty claim.

## INF-555 — Expose the live round clock and individual bout tally

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `Medium`
- Definition: show remaining round time and a separate accumulated bout-win count for each contestant during the current match so the time pressure and progress toward overall victory are jointly readable.
- Includes: the Battle Game header pairing the practical countdown with each visible character’s wins.
- Excludes: a post-match-only scoreboard; a feed that reports recent knockouts without standings; a single overall progress bar; complete knowledge of hidden pickup locations or fuse lengths.
- Parameters: visible clock, participant identification, individual win tally and display interval
- Evidence: [Saturn Bomberman decomposition](../games/s-z/saturn-bomberman.md), SB-002 and SB-007. The English Sega manual and static original-release battle captures establish the scoped rule. Exact timings and internal values are not measured.
- Novelty: first isolated for `GAME-0584`; see [TAXONOMY_CHANGE_330](../../research/taxonomy-changes/TAXONOMY_CHANGE_330.md). No external novelty claim.

## INF-554 — Show the day-to-night gauge and whether the route can reach the gate in time

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `Medium`
- Definition: The display shows current time until a phase change and marks the prepared route tip according to whether the protected follower can currently reach the final gate for purification before nightfall.
- Includes: Read the water-basin display and the white or blue spirit image at the Spirit Path tip.
- Excludes: Only showing direction to the gate, disclosing the full future spawn sequence, or guaranteeing survival along a route.
- Parameters: Remaining time, current phase, guide position, route tip, terminal reachability and cue state.
- Evidence: [Kunitsu-Gami decomposition](../games/g-l/kunitsu-gami-path-of-the-goddess.md), KG-003, KG-005. The full-release Capcom manual and corroborating PS5 and release-game evidence establish the conditional transition. Exact timings and internal values are not measured.
- Novelty: first isolated for `GAME-0583`; see [TAXONOMY_CHANGE_329](../../research/taxonomy-changes/TAXONOMY_CHANGE_329.md). No external novelty claim.

## INF-553 — Indicate a nearby interaction target through the avatar’s head direction

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `Medium`
- Definition: A controllable character turns the head toward a noticed person or object before the player confirms an interaction. Moving or turning can change which target is indicated without adding a cursor or disclosing the effect of using an item.
- Includes: Look for Manny’s head movement as he approaches the cards, Eva or an interactable tube fixture.
- Excludes: A verb wheel that names the action, a mouse hotspot cursor, a target marker shown after confirmation, or revealing the hidden prerequisite.
- Parameters: Avatar position and facing, noticed target, cue direction, contextual reach and target change.
- Evidence: [Grim Fandango decomposition](../games/g-l/grim-fandango.md), GF-002. The LucasArts manual and corroborating original-release walkthroughs and frames establish the conditional transition. Exact timings and internal values are not measured.
- Novelty: first isolated for `GAME-0582`; see [TAXONOMY_CHANGE_328](../../research/taxonomy-changes/TAXONOMY_CHANGE_328.md). No external novelty claim.

## INF-552 — Show recovered and lost ship value against ordered salvage milestones

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `Medium`
- Definition: A live work indicator presents credited recovery, recorded losses and milestone positions on the same ship-scale progress display. The shift-end report presents the settled results without requiring the worker to infer them from remaining geometry.
- Includes: Compare the yellow accepted share and red losses against the next target marker above the Mackerel, then read the shift summary.
- Excludes: An unlabelled count of loose pieces, a single score that hides losses, or displaying an exact route for all remaining material.
- Parameters: Current ship, credited amount, lost amount, milestone positions and settlement report.
- Evidence: [Hardspace: Shipbreaker decomposition](../games/g-l/hardspace-shipbreaker.md), HS-005, HS-006. Blackbird’s Xbox guide and corroborating released-game evidence establish the conditional transition. Exact timings and internal values are not measured.
- Novelty: first isolated for `GAME-0581`; see [TAXONOMY_CHANGE_327](../../research/taxonomy-changes/TAXONOMY_CHANGE_327.md). No external novelty claim.

## INF-551 — Expose hidden structural cut points and the targeted salvage destination

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `Medium`
- Definition: The worker can inspect a ship to see structural cut points obscured by its casing. When aiming at a part, tool feedback identifies its material or assigned destination, informing the choice to cut, detach or route it.
- Includes: Highlight the yellow joints through the Mackerel with the scanner and check the selected panel’s Processor destination before moving it.
- Excludes: A prediction of the exact resulting trajectory, automatic salvage credit, and binding one fixed destination to an entire hull.
- Parameters: Scan mode, view, highlighted link, targeted object and destination indication.
- Evidence: [Hardspace: Shipbreaker decomposition](../games/g-l/hardspace-shipbreaker.md), HS-003, HS-005. Blackbird’s Xbox guide and corroborating released-game evidence establish the conditional transition. Exact timings and internal values are not measured.
- Novelty: first isolated for `GAME-0581`; see [TAXONOMY_CHANGE_327](../../research/taxonomy-changes/TAXONOMY_CHANGE_327.md). No external novelty claim.

## INF-550 — Expose both sides’ measures, scheduled hostile actions and a visible escalation meter

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `Medium`
- Definition: A pre-command combat score shows the current action allocations and the relative placement of upcoming opposing moves. A visible escalation meter shows how far the current boss has progressed toward further power.
- Includes: Inspect the staff before selecting Cadence or Cerrin. Read the separate Crescendo meter when deciding how long to spend preparing.
- Excludes: A hidden enemy queue, promising exact damage and target for every future enemy action or using the musical score purely as decoration.
- Parameters: Allied measure count, hostile measure count, forecast action indicator, current position and visible escalation.
- Evidence: [People of Note decomposition](../games/m-r/people-of-note.md), PON-002, PON-007. Developer accounts, Switch 2 release reviews and source-attributed battle stills establish the scoped transitions. Exact console build and timing limits are qualified in the game record.
- Novelty: first isolated for `GAME-0577`; see [TAXONOMY_CHANGE_323](../../research/taxonomy-changes/TAXONOMY_CHANGE_323.md). No external novelty claim.

## INF-549 — Expose an authored lead and request current route guidance from it

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `Medium`
- Definition: The journal records an authored lead and lets the player select it for destination guidance. Requesting help shows a route cue toward the currently available objective or escape destination without completing the step.
- Includes: Track Dying Gasp to find the required contacts. After the violation, request the butterfly guidance toward the return shrine.
- Excludes: Revealing an entire solution, following a permanent out-of-game route or automatically moving the avatar to the tracked destination.
- Parameters: Lead identity, journal, tracking option, current route and guidance request.
- Evidence: [The Forgotten City decomposition](../games/s-z/the-forgotten-city.md), TFC-003, TFC-004, TFC-007. Creator interviews and independently documented title-release play establish the scoped transitions. Console build limits are qualified in the game record.
- Novelty: first isolated for `GAME-0576`; see [TAXONOMY_CHANGE_322](../../research/taxonomy-changes/TAXONOMY_CHANGE_322.md). No external novelty claim.

## INF-548 — Expose current card legality, remaining slots and relative turn readiness

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `Medium`
- Definition: Expose the available hand and command details with the actor’s remaining slots and relative turn order on the current map. Inspection can show legal reach and directed hostile vision before committing.
- Includes: Read REST and Cost separately, inspect highlighted cells and facing in Aerial view, and check the action order before confirming a card.
- Excludes: Revealing the future draw order, authoring a guaranteed replay of every guard decision, or allowing the camera to change the rules of reach.
- Parameters: Hand, card details, movement shading, sight region, remaining slots and readiness order.
- Evidence: [Metal Gear Acid decomposition](../games/m-r/metal-gear-acid.md), MGA-003, MGA-004, MGA-006. The original manual and launch-period PSP play accounts establish the scoped transitions. Region and runtime limits are qualified in the game record.
- Novelty: first isolated for `GAME-0575`; see [TAXONOMY_CHANGE_321](../../research/taxonomy-changes/TAXONOMY_CHANGE_321.md). No external novelty claim.

## INF-547 — Show the visible reply outline, loose fragments and the speaker transition

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `Medium`
- Definition: The current vignette visibly distinguishes the other character’s authored speech from the reply the player can assemble, exposes the target outline and outstanding fragments, and signals the completed reply by its visual presentation.
- Includes: See Krish’s balloon and match Florence’s visible fragments to the indicated reply contour without reading words.
- Excludes: Choosing from a written list of topics, matching an invisible receptacle, or relying on hidden relationship scores.
- Parameters: Speaker, current speech balloon, loose fragments, visible boundary, placed coverage and completion feedback.
- Evidence: [Florence decomposition](../games/a-f/florence.md), FLO-002, FLO-003. Launch-period touch accounts and attributed chapter walkthroughs establish the scoped transitions. Later figure analysis and original-runtime limits are qualified in the game record.
- Novelty: first isolated for `GAME-0574`; see [TAXONOMY_CHANGE_320](../../research/taxonomy-changes/TAXONOMY_CHANGE_320.md). No external novelty claim.

## INF-546 — Show milestone notices, room service state and live creature encounters

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `Medium`
- Definition: The dungeon interface discloses new orders and capabilities as scenario states change, presents visible gold, room capacity and efficiency, and signals active encounters and creature status without exposing the complete hidden map.
- Includes: Use Eversmile’s objective marker, flashing room or spell button, overhead map and battle view to adjust construction or creature placement.
- Excludes: A complete enemy map before exploration, a purely cosmetic room label or silent automatic advancement with no current cue.
- Parameters: Objective notice, availability cue, gold, room indicators, revealed map and battle status.
- Evidence: [Dungeon Keeper decomposition](../games/a-f/dungeon-keeper.md), DKE-003, DKE-009. The PC CD-ROM manual and attributed full-campaign play accounts establish the scoped transitions. Exact script constants from secondary sources are qualified in the game record.
- Novelty: first isolated for `GAME-0573`; see [TAXONOMY_CHANGE_319](../../research/taxonomy-changes/TAXONOMY_CHANGE_319.md). No external novelty claim.

## INF-545 — Expose live weapon-card availability, remaining enemies and elapsed time

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `Medium`
- Definition: The active run view communicates the held weapon-card state and firing stock alongside remaining required enemies and elapsed time. This allows the player to plan a spend before reaching the finish.
- Includes: Read the current card and ammunition alongside the demon counter and timer while crossing Elevate.
- Excludes: An advance prediction of optimal route, hidden later pickups, or displaying only the final medal.
- Parameters: Held cards, firing stock, live enemy count and run timer.
- Evidence: [Neon White decomposition](../games/m-r/neon-white.md), NW-005, NW-007. Director descriptions and contemporary Switch and stage accounts support the scoped transitions. The specific demon count uses the attributed later stage inventory.
- Novelty: first isolated for `GAME-0572`; see [TAXONOMY_CHANGE_318](../../research/taxonomy-changes/TAXONOMY_CHANGE_318.md). No external novelty claim.

## INF-544 — Show the service timing gauge and separate fault, point and game feedback

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `Medium`
- Definition: The court view exposes the current ball and opponents. During service it presents a live timing gauge and distinguishes the attempt. A completed delivery or resolution can disclose speed, fault state and point and game scores at their respective stages.
- Includes: The Virtua Tennis Serve Gauge, serve count, speed, point score and games in the Dreamcast display.
- Excludes: An exact advance prediction of every rally bounce; hidden CPU preferences; showing only the terminal winner.
- Parameters: Ball and athlete view, server, gauge, attempt, speed, adjudication and current scores.
- Evidence: [Virtua Tennis decomposition](../games/s-z/virtua-tennis.md), VT-003, VT-008. The original booklet and attributed contemporary play accounts support the controls and settings. Implementation-only branches are qualified to the pinned reconstruction.
- Novelty: first isolated for `GAME-0571`; see [TAXONOMY_CHANGE_317](../../research/taxonomy-changes/TAXONOMY_CHANGE_317.md). No external novelty claim.

## INF-543 — Read embodied combat state from coloured bodies, visible trajectories and hand readiness

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `Medium`
- Definition: The scene distinguishes hostile bodies, usable objects and architecture through contrasting visual classes and shows local attack motion, bullets and the player’s hands in spatial relation. A glitched hand signals unavailable defence. These cues reveal immediate geometry and readiness without disclosing a complete future spawn script, exact ammunition counter or numeric recovery timer.
- Includes: SUPERHOT VR red hostiles, dark interactive props, pale environment, visible bullet paths and hand glitch; occluded threats remain occluded.
- Excludes: An omniscient whole-board state; a numeric health or reload HUD; assuming colour alone guarantees every object’s material rule; exposing all later scenes.
- Parameters: Visible body classes, local geometry, trajectory, occlusion, held object, hand state and feedback.
- Evidence: [SUPERHOT VR decomposition](../games/s-z/superhot-vr.md), SHV-002, SHV-006. Official Quest launch material, developer statements and qualified released-version accounts support the common rules; no native Quest binary, exact time floor or recovery coefficient was measured.
- Novelty: first isolated for `GAME-0567`; see [TAXONOMY_CHANGE_313](../../research/taxonomy-changes/TAXONOMY_CHANGE_313.md). No external novelty claim.

## INF-542 — Expose local numbered approach cues and distinct song-survival and spin meters

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `Medium`
- Definition: The live interface reveals the currently approaching numbered and coloured touch targets, shrinking timing rings, phrase route/ball and any reversal cue, together with current score, combo and the song performance reserve. During a spin event its local fill meter is separately readable; story O/X feedback does not replace either meter or disclose the complete future chart.
- Includes: Elite Beat Agents lower-screen chart and Elite-o-Meter, local spinner fill and upper-screen section outcome. Exact hidden hit windows, drain coefficients and the whole future chart are not revealed.
- Excludes: An omniscient chart before play; instructor/player turn ownership; conflating spinner fill with the remaining song reserve; a terminal category report being the live preview.
- Parameters: Visible targets, number, colour, ring phase, phrase geometry, ball, reversal, score, combo, reserve, spin fill and section outcome.
- Evidence: [Elite Beat Agents decomposition](../games/a-f/elite-beat-agents.md), EBA-002, EBA-003, EBA-004, EBA-007. Official documentation and qualified first-hand accounts support the common rules; no native European cartridge, exact hit window or scoring coefficient was measured.
- Novelty: first isolated for `GAME-0566`; see [TAXONOMY_CHANGE_312](../../research/taxonomy-changes/TAXONOMY_CHANGE_312.md). No external novelty claim.

## INF-541 — Reveal live dome-cycle measurements through their separately purchased instruments

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `Medium`
- Definition: Each acquired basic instrument adds its declared persistent measurement to the live display, such as dome integrity, banked resources or remaining mining time before the next assault. The underlying dome, stock and wave clock already exist before the corresponding instrument is bought; buying one does not reveal every other measurement.
- Includes: The original Dome Keeper console offers separate health, inventory and hostile-proximity instruments. Their presence is not presumed at fresh landing, and the ordinary warning cue is not an exact future spawn/composition list.
- Excludes: Treating every readout as free starting information; changing the underlying countdown by displaying it; exact future hostile health, composition or arrival frames; a later early-warning/exit-route upgrade being assumed in 2022.
- Parameters: Instrument node, acquired state, measurement kind, live value, visibility, basic warning and run persistence.
- Evidence: [Dome Keeper decomposition](../games/a-f/dome-keeper.md), DK-009. No direct play, executable checksum or frame-perfect native reproduction is claimed; the launch-era source and observation limits remain in the game record.
- Novelty: first isolated for `GAME-0565`; see [TAXONOMY_CHANGE_311](../../research/taxonomy-changes/TAXONOMY_CHANGE_311.md). No external novelty claim.

## INF-540 — Expose the locally revealed mine and material cues without the whole hidden map

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `Medium`
- Definition: The mining view exposes nearby excavated passages, the keeper, loose bodies and locally revealed rock/resource cues, while deeper unobserved terrain and chambers remain undisclosed. Visible mineral-bearing rock can guide a drilling choice before its material becomes a delivered bank resource.
- Includes: Dome Keeper reveals short-range rock hardness and exposed iron, water or cobalt cues along the excavation frontier; the opening route is not an omniscient world map.
- Excludes: A purchased prospecting gadget locating resources at distance; a fully visible random board; an acquired authored floor plan; the dome battle view proving the locations of hidden underground chambers.
- Parameters: Keeper position, camera, local reveal range, remembered excavation, hardness cue, material cue, loose body and hidden terrain.
- Evidence: [Dome Keeper decomposition](../games/a-f/dome-keeper.md), DK-002. No direct play, executable checksum or frame-perfect native reproduction is claimed; the launch-era source and observation limits remain in the game record.
- Novelty: first isolated for `GAME-0565`; see [TAXONOMY_CHANGE_311](../../research/taxonomy-changes/TAXONOMY_CHANGE_311.md). No external novelty claim.

## INF-539 — Mark an airborne contest disc’s landing opportunity and temporary receiver charge

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `Medium`
- Definition: While a contest disc is aloft, a visible ground marker discloses its current intended landing opportunity, and the athlete’s local pose or charge cue distinguishes preparation from sufficient powered readiness before reception. The display supports positioning without certifying an exact future opponent response or native frame count.
- Includes: Windjammers marks the landing point after a toss or lob and shows the receiver concentrating or surrounded by a ready-charge ring.
- Excludes: A complete predicted shot route; hidden opponent inputs; an independently spendable permanent super meter; merely showing the present disc position with no landing marker.
- Parameters: Airborne state, current landing marker, receiver position, preparation pose, ready cue, display timing and remaining uncertainty.
- Evidence: [Windjammers decomposition](../games/s-z/windjammers.md), WJ-005. No native MVS execution, exact timing windows, threshold-margin rule or complete per-frame contact audit is claimed; source limits remain in the game record.
- Novelty: first isolated for `GAME-0564`; see [TAXONOMY_CHANGE_310](../../research/taxonomy-changes/TAXONOMY_CHANGE_310.md). No external novelty claim.

## INF-538 — Reveal a selected enemy’s available health and weakness information through a learned scan

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `Medium`
- Definition: A legal learned scan command reveals the addressed enemy’s disclosed HP and weakness information where that target permits it; the information is earned by the selected ability rather than assumed present in every ordinary battle view.
- Includes: After the early level unlock, Aya may spend the ready command and required PE on Scan to inspect a compatible enemy before choosing later attacks.
- Excludes: A complete omniscient enemy ledger; guaranteed disclosure for every boss; a quickhack installation menu; a passive range globe; a held visor scan that requires a separate exploration mode.
- Parameters: Learned ability, command readiness, energy cost, selected target, disclosed HP, weakness and disclosure exception.
- Evidence: [Parasite Eve decomposition](../games/m-r/parasite-eve.md), PEV-006. No native PlayStation execution, exact hit formula, status duration or complete save-field audit is claimed; source limits remain in the game record.
- Novelty: first isolated for `GAME-0562`; see [TAXONOMY_CHANGE_308](../../research/taxonomy-changes/TAXONOMY_CHANGE_308.md). No external novelty claim.

## INF-537 — Display the current weapon’s effective volume and selected command target

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `Medium`
- Definition: Attack selection exposes a spatial wireframe of the current weapon’s effective range around the controlled actor, its loaded ammunition and selected enemy or target part; this information supports positioning and selection but does not guarantee a hit or reveal every hidden combat value.
- Includes: Aya checks the range globe and changes the selected alligator target between tail and head before committing a ready command.
- Excludes: A hard prohibition on every out-of-range target; an exact probabilistic damage forecast; a complete enemy-health display without Scan; an omniscient world map.
- Parameters: Weapon range, actor position, wireframe volume, loaded bullets, selected enemy/part and commitment.
- Evidence: [Parasite Eve decomposition](../games/m-r/parasite-eve.md), PEV-003. No native PlayStation execution, exact hit formula, status duration or complete save-field audit is claimed; source limits remain in the game record.
- Novelty: first isolated for `GAME-0562`; see [TAXONOMY_CHANGE_308](../../research/taxonomy-changes/TAXONOMY_CHANGE_308.md). No external novelty claim.

## INF-536 — Read companion attention and readiness from nonverbal local behaviour

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: The companion’s gaze, eye appearance, posture, approach, refusal and feeding response disclose its current attention and readiness without exposing a numerical obedience score, a complete future route or a guarantee that repeating the same request will be accepted immediately.
- Includes: Trico looks toward food, initially refuses close feeding, rests and changes posture before helping the boy reach a ledge.
- Excludes: A full solved route overlay; a visible exact trust meter; reading hidden AI variables; treating every animation as a new command or a fixed response deadline.
- Parameters: Companion, visible cue, local stimulus, attention, readiness and unresolved response delay.
- Evidence: [The Last Guardian decomposition](../games/s-z/the-last-guardian.md), TLG-004, TLG-005. Native execution, exact AI timing, installed patch and checkpoint fields are unverified; source limits remain in the game record.
- Novelty: first isolated for `GAME-0559`; see [TAXONOMY_CHANGE_305](../../research/taxonomy-changes/TAXONOMY_CHANGE_305.md). No external novelty claim.

## INF-535 — Inspect a locally occluded diorama with authored traversal cues and companion advice

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: The current scene exposes Quill, local supports, fixture markings and motion feedback from the Reader’s tracked viewpoint; occluded details can be inspected by changing that viewpoint, and authored companion gestures or local instructions can suggest the next operation without revealing all later rooms or an exact future trajectory.
- Includes: Clearing scratch-marked edges, patterned interactive stones, visible wheel phase, contextual prompts and Quill’s authored communicative response.
- Excludes: Simultaneous omniscience of the whole chapter; a solved-route overlay; a guaranteed future landing preview; every friendly gesture being a progress requirement.
- Parameters: Scene boundary, occlusion, head pose, visible edge and fixture cues, authored prompts and advice availability.
- Evidence: [Moss decomposition](../games/m-r/moss.md), MOS-002, MOS-007. Native tracking, exact rates and field-by-field checkpoint persistence are not reproduced; source limits remain in the game record.
- Novelty: first isolated for `GAME-0558`; see [TAXONOMY_CHANGE_304](../../research/taxonomy-changes/TAXONOMY_CHANGE_304.md). No external novelty claim.

## INF-534 — Distinguish live solar input from stored gun energy and purification resistance

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: The interface separately shows current sensed sunlight, the weapon’s remaining energy, life, eligible item effects and an overheat warning, while purification exposes the captive’s Darkness Gauge and beam weakening; settlement discloses time, discoveries, continues, charged energy and rank without exposing exact hidden scoring or lens-experience formulas.
- Includes: The Solar Gauge and Gun Gauge in Fog Castle, two generator beams and the post-purification results screen.
- Excludes: One merged sun/ammunition meter; a visible exact lens EXP counter; certifying every hidden coefficient from a coarse recording.
- Parameters: Sensor gauge, stored energy, life, item effect, darkness, beam appearance and graded result.
- Evidence: [Boktai decomposition](../games/a-f/boktai-the-sun-is-in-your-hand.md), BOK-002, BOK-007, BOK-008, BOK-010, BOK-013. Native sensor, exact coefficients and field-by-field persistence are not reproduced; source limits remain in the game record.
- Novelty: first isolated for `GAME-0557`; see [TAXONOMY_CHANGE_303](../../research/taxonomy-changes/TAXONOMY_CHANGE_303.md). No external novelty claim.

## INF-533 — Expose song score, style feedback and retained rank without a full multiplier readout

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `Medium`
- Definition: The running presentation shows accumulated points and immediate named style feedback, while the song card exposes best score, rank and credited square coins. The hidden per-class pickup counters are not thereby revealed as a complete explicit multiplier HUD.
- Includes: Read Slide or Risky feedback during Doki Doki Rush, then distinguish its final grade from the persistent square-coin row.
- Excludes: A declared x-multiplier display inferred from score changes; a health gauge; per-note timing grades during a stage with no such prompts; a preview of every future collectible.
- Parameters: Live score, feedback event, song card, rank, best score, square row and undisclosed counters.
- Evidence: [Sayonara Wild Hearts decomposition](../games/s-z/sayonara-wild-hearts.md), SWH-005, SWH-007, SWH-008.
- Novelty: first isolated for `GAME-0556`; see [TAXONOMY_CHANGE_302](../../research/taxonomy-changes/TAXONOMY_CHANGE_302.md).

## INF-532 — Distinguish live battery, household period, happiness and money before the next chore

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: The interface separately discloses current personal charge, the day/night period clock, earned happiness and money, while the base exposes robot rank. These measures serve different decisions and are not interchangeable currencies or a single completion percentage.
- Includes: Read low charge before another toothbrush pass; compare remaining night time with a nearby outlet and later inspect the home rank.
- Excludes: A hidden exact drain equation; a whole-house cleanliness percentage; cash substituting for battery; a complete advance schedule of every toy quest.
- Parameters: Charge, clock and phase icon, happiness, money, base rank and update timing.
- Evidence: [Chibi-Robo! decomposition](../games/a-f/chibi-robo.md), CHR-004, CHR-007, CHR-008.
- Novelty: first isolated for `GAME-0555`; see [TAXONOMY_CHANGE_301](../../research/taxonomy-changes/TAXONOMY_CHANGE_301.md).

## INF-531 — Read named grid topography alongside retained relational location clues

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: The map exposes labelled places, terrain features and row-column addresses; retained correspondence supplies absolute or relative location clues. Selecting a square reveals its authored encounter rather than guaranteeing a useful new specimen at every named place.
- Includes: Use Ambleside’s town label, Backbarrow’s northeast hills and the wood south of Gosforth to locate C20, M21 and G5.
- Excludes: An automatically plotted optimal route; a fully revealed plant-location catalogue; a physical walkable world whose navigation topology changes when the paper is rearranged.
- Parameters: Named place, grid address, woodland or hill geometry, retained letter, relative relation and encounter text.
- Evidence: [Strange Horticulture decomposition](../games/s-z/strange-horticulture.md), SH-005, SH-006.
- Novelty: first isolated for `GAME-0554`; see [TAXONOMY_CHANGE_300](../../research/taxonomy-changes/TAXONOMY_CHANGE_300.md).

## INF-530 — Cross-read a growing botanical reference against inspected specimen traits

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: An inspectable botanical reference retains acquired entries with names, partial illustrations and properties, while close inspection exposes the selected specimen’s authored visual and descriptive traits. The player must reconcile these sources; having an entry does not grant the specimen or automatically identify every shelf object.
- Includes: Ambleside adds Gilded Dendra and Wandering Bue entries; inspect a shelf specimen’s texture, scent or shape against the relevant entry rather than matching only an incomplete sketch.
- Excludes: INF-054’s fixed page-pair manual boundary; a complete authoritative shelf-name overlay; labels being validated as evidence; copying botanical effects into real-world advice.
- Parameters: Acquired entry, fictional name, illustration crop, property text, specimen focus, inspection description and ownership separation.
- Evidence: [Strange Horticulture decomposition](../games/s-z/strange-horticulture.md), SH-001, SH-002, SH-004.
- Novelty: first isolated for `GAME-0554`; see [TAXONOMY_CHANGE_300](../../research/taxonomy-changes/TAXONOMY_CHANGE_300.md).

## INF-529 — Expose host identity, condition, skill readiness and mission credits

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: The current host presentation and information surfaces expose body identity, controlled condition, opponent energy, separate active-skill readiness and the current mission’s objective credits. Briefing or terminal data explain the body and tasks without revealing a guaranteed future route.
- Includes: Read the dog or sheep, green condition, blue opponent bar, A/B power and the first level’s energy and occupation objectives before using its exit.
- Excludes: An exact future trajectory, a new permission to occupy an otherwise ineligible body, merging optional Power Cells with healing energy, and a complete unseen world-state disclosure.
- Parameters: Host identity, controlled condition, opponent energy, skill channels, briefing, terminal, objective credit and display state.
- Evidence: [Space Station Silicon Valley decomposition](../games/s-z/space-station-silicon-valley.md), SSV-006, SSV-007.
- Novelty: first isolated for `GAME-0548`; see [TAXONOMY_CHANGE_295](../../research/taxonomy-changes/TAXONOMY_CHANGE_295.md).

## INF-528 — Expose tracked putting geometry together with hole and stroke feedback

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: The player can inspect the current club head, ball lie, course banks and cup in spatial perspective, while wrist or scorecard fields expose the current hole, counted strokes and par-relative result. This supports alignment and pace choice without forecasting an exact future path.
- Includes: Inspect Tourist Trap’s narrow neck and wider cup area, align the visible putter face, and read the par-two hole’s retained stroke result.
- Excludes: A recommended disc or wind readout, an exact predicted trajectory, hidden sensor coefficients and treating par as a required maximum.
- Parameters: Head pose, ball lie, banks, cup, current hole, par, counted strokes, signed result and display surface.
- Evidence: [Walkabout Mini Golf decomposition](../games/s-z/walkabout-mini-golf.md), WMG-003, WMG-004, WMG-006.
- Novelty: first isolated for `GAME-0547`; see [TAXONOMY_CHANGE_294](../../research/taxonomy-changes/TAXONOMY_CHANGE_294.md).

## INF-527 — Expose protection stock, shot charge, local danger interval and voiced guidance without a full map

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: The mission surface exposes held crystalline protection, shot charge, current location, applicable ID-card state and separate overall-danger and next-burst indicators. Automatic or requested voice navigation supplies local directions without a complete persistent map.
- Includes: Read the crystal count and charge gauge, distinguish the danger percentage from the shrinking next-boundary bar, and ask Chris for the current route in Burning Rangers.
- Excludes: A health bar independent of the shared crystals, complete map omniscience, and confusing a grade at settlement with current danger.
- Parameters: Held crystals, charge gauge, room name, ID-card icon, danger graph, interval bar, voice instruction and concealed routes.
- Evidence: [Burning Rangers decomposition](../games/a-f/burning-rangers.md), BR-008.
- Novelty: first isolated for `GAME-0546`; see [TAXONOMY_CHANGE_293](../../research/taxonomy-changes/TAXONOMY_CHANGE_293.md).

## INF-526 — Show live incidents and proposed attribute fit alongside responder availability

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: The dispatch surface exposes current incident markers, call details, allowed team slots and a five-axis comparison of the proposed group against call needs, while roster cards distinguish available, busy, returning and resting responders. It does not expose all future calls or the exact hidden outcome formula.
- Includes: Inspect a Dispatch call and its proposed suitability while noticing that an otherwise suitable hero is still Resting.
- Excludes: An omniscient future schedule, a guaranteed success promise from a chart, and a world map with no assignment or readiness information.
- Parameters: Map marker, current call, slot count, five attributes, proposed group, readiness label and outcome feedback.
- Evidence: [Dispatch decomposition](../games/a-f/dispatch.md), DIS-002, DIS-003, DIS-009.
- Novelty: first isolated for `GAME-0545`; see [TAXONOMY_CHANGE_292](../../research/taxonomy-changes/TAXONOMY_CHANGE_292.md).

## INF-525 — Expose call ownership, target identity, numeric ratings and local mistake hearts

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: The presentation distinguishes demonstration from the player’s response, reveals dance directions or target appearance order and human/enemy identity, and exposes the live audience percentage and applicable local mistake hearts.
- Includes: Use the turn marker and spoken/animated call, distinguish people from Morolians, and inspect the rating and boss hearts.
- Excludes: A persistent full-song note highway, an omniscient future chart, ordinal rap grades alone, and disclosed exact timing thresholds.
- Parameters: Turn icon, audiovisual cue, target type and direction, current percentage, heart display and feedback.
- Evidence: [Space Channel 5 decomposition](../games/s-z/space-channel-5.md), SC-002–SC-004, SC-007.
- Novelty: first isolated for `GAME-0544`; see [TAXONOMY_CHANGE_291](../../research/taxonomy-changes/TAXONOMY_CHANGE_291.md).

## INF-524 — Expose live stunt credit, passing-star target and engine temperature

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: The racing display separates the stars already earned, the course passing target, current feat credit and current engine temperature so a player can weigh scoring opportunities against boost heat.
- Includes: Read the earned-star and required-star values alongside the temporary stunt counter and temperature gauge.
- Excludes: A hidden cumulative vehicle-unlock tally, future stunt credit, and a nitro fuel reserve.
- Parameters: Earned stars, target, live stunt credit, temperature and warning.
- Evidence: [Excite Truck decomposition](../games/a-f/excite-truck.md), ET-009.
- Novelty: first isolated for `GAME-0542`; see [TAXONOMY_CHANGE_289](../../research/taxonomy-changes/TAXONOMY_CHANGE_289.md).

## INF-523 — Mark obstructions that intersect the protected actor’s route

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: Local world markers identify still-relevant obstacles because their obstruction lies in a protected unit’s authored travel corridor. Eligible objects elsewhere can remain unmarked and can still matter for a separate cleanup.
- Includes: Prioritise the Simian Acres sheds with flashing route arrows and leave remote demolition targets for a later visit.
- Excludes: Marking an exit bearing, showing every destructible target regardless of route, or a complete prospective simulation of mutable paths.
- Parameters: Route intersection, eligible obstructions, marker, outstanding obstruction state and optional targets.
- Evidence: [Blast Corps decomposition](../games/a-f/blast-corps.md), BC-003, BC-005.
- Novelty: first isolated for `GAME-0539`; see [TAXONOMY_CHANGE_286](../../research/taxonomy-changes/TAXONOMY_CHANGE_286.md).

## INF-522 — Show separate coverage for discovered evidence spots and case words

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: The interface reports visited evidence spots and collected vocabulary terms in two separate found-over-total counts for the same case. Neither count reports correctness of an answer.
- Includes: Use the Constriction toolbar to read 9 evidence spots and 25 words as separate totals and find which discovery track remains incomplete.
- Excludes: A single clue tally, an answer correctness indicator, a required number of solutions or a combined progress percentage.
- Parameters: Spot tally and authored total, term tally and authored total.
- Evidence: [The Rise of the Golden Idol decomposition](../games/s-z/the-rise-of-the-golden-idol.md), RGI-002, RGI-007.
- Novelty: first isolated for `GAME-0538`; see [TAXONOMY_CHANGE_285](../../research/taxonomy-changes/TAXONOMY_CHANGE_285.md).

## INF-521 — Pan the rolling course separately from steering and inspect live course resources

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: The live view shows nearby supports and hazards, with score, vitality, ordinary pickup tally and the attempt clock. Separate directional inputs pan the map without changing the steering command.
- Includes: Use the Control Pad to look beyond the rolling view, then read time and vitality before the next crossing.
- Excludes: The Control Pad moving the avatar, a solved route overlay, a final-only result or a claim that every hidden course object is revealed.
- Parameters: Panned area, avatar view, geometry, score, vitality, pickup tally and running time.
- Evidence: [Kirby Tilt 'n' Tumble decomposition](../games/g-l/kirby-tilt-n-tumble.md), KTT-002, KTT-006.
- Novelty: first isolated for `GAME-0537`; see [TAXONOMY_CHANGE_284](../../research/taxonomy-changes/TAXONOMY_CHANGE_284.md).

## INF-520 — Expose the aimed hack route, predicted result and active armor opening

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: A target-linked grid displays the current ordered trace, terminal and typed cells alongside projected hack damage. An independent enemy indicator and exposed component mark the resolved temporary Open state.
- Includes: Check the path and projected damage while aiming, then recognize the active opening at the enemy.
- Excludes: A static route diagram without draft feedback, a boss health bar alone, unconditional firing permission, or an exact preview of damage from later free aim.
- Parameters: Target, grid, draft, node markers, projected harm and resolved window cue.
- Evidence: [PRAGMATA decomposition](../games/m-r/pragmata.md), PRA-002, PRA-003, PRA-005.
- Novelty: first isolated for `GAME-0536`; see [TAXONOMY_CHANGE_283](../../research/taxonomy-changes/TAXONOMY_CHANGE_283.md).

## INF-519 — Expose shared reserve and drafted spend alongside hull state

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: The combat planner shows the shared reserve available before resolution and the amount assigned to costs by the current draft, together with vessel hull information for evaluating attack and recovery options.
- Includes: Read the available and assigned Spirit in the top gauge while checking the Little Jack’s hull before adding another command.
- Excludes: A personal MP meter only, a single remaining value with no draft commitment, or a result score after all commands resolve.
- Parameters: Shared reserve, assigned cost, current draft, own and opposing hull status.
- Evidence: [Skies of Arcadia decomposition](../games/s-z/skies-of-arcadia.md), SOA-003, SOA-007.
- Novelty: first isolated for `GAME-0535`; see [TAXONOMY_CHANGE_282](../../research/taxonomy-changes/TAXONOMY_CHANGE_282.md).

## INF-518 — Preview danger and a separate attack opportunity for each time slot

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: A timeline marks upcoming time slots with categorical incoming danger and separate favourable attack openings. A provisional next-turn forecast can change when the current plan or an authored tactical branch changes the encounter.
- Includes: Read the coloured band above the Little Jack’s slots and compare its independent Chance markers before and after the maneuver.
- Excludes: A complete preview of exact damage, a committed attack icon with no time slot, a guarantee of a hit, or colour as an unconditional action permission.
- Parameters: Current slots, categorical danger, chance marker, provisional future and branch.
- Evidence: [Skies of Arcadia decomposition](../games/s-z/skies-of-arcadia.md), SOA-004, SOA-005.
- Novelty: first isolated for `GAME-0535`; see [TAXONOMY_CHANGE_282](../../research/taxonomy-changes/TAXONOMY_CHANGE_282.md).

## INF-517 — Mark possessable cores and disclose the occupied host’s command status separately

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: The stopped traversal view marks cores that can host the spirit. The display identifies the currently occupied object and gives separate feedback about whether a live command is available on it.
- Includes: Follow the cores toward the crane and use the interface to distinguish the ball as a relay from the operable claw.
- Excludes: A general scenery outline, a highlight that grants a trick to every marked prop, or a full preview of the solved chain.
- Parameters: World mode, visible core, current host, interaction label and command availability.
- Evidence: [Ghost Trick decomposition](../games/g-l/ghost-trick-phantom-detective.md), GT-003, GT-007.
- Novelty: first isolated for `GAME-0533`; see [TAXONOMY_CHANGE_280](../../research/taxonomy-changes/TAXONOMY_CHANGE_280.md).

## INF-516 — Replace ordinary sight with focused local sound and proximity cues

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: While the avatar’s eyes are closed, ordinary visual access is withheld. Relevant nearby sounds become easier to notice, and compatible controller feedback can indicate proximity to specified nearby objects.
- Includes: On flat-screen PS5, close the eyes to emphasise local sound and use the applicable DualSense vibration without seeing an ordinary scene.
- Excludes: An overlay preserving full sight, an omniscient position list, or a marked barrier changing state by itself.
- Parameters: Eye state, local audio source, salience, controller proximity feedback and loss of ordinary view.
- Evidence: [The Midnight Walk decomposition](../games/s-z/the-midnight-walk.md), MW-005.
- Novelty: first isolated for `GAME-0531`; see [TAXONOMY_CHANGE_278](../../research/taxonomy-changes/TAXONOMY_CHANGE_278.md).

## INF-515 — Expose formation guard and the remaining committed action order

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: A dedicated guard meter shows formation protection separately from personal HP. The execution view reveals the remaining committed action order and pending casts’ time in turns after the party batch starts, without specifying the next enemy command during planning.
- Includes: Read party Guard Condition separately from each member’s health and watch the execution icons after locking in the Grilgan round.
- Excludes: A pre-commit forecast of all enemy abilities, an exact personal HP bar in lieu of a guard reserve or a real-time action-readiness meter.
- Parameters: Displayed guard, personal HP, committed resolution phase, remaining order and pending-cast counter.
- Evidence: [Lost Odyssey decomposition](../games/g-l/lost-odyssey.md), LO-002, LO-004, LO-006.
- Novelty: first isolated for `GAME-0530`; see [TAXONOMY_CHANGE_277](../../research/taxonomy-changes/TAXONOMY_CHANGE_277.md).

## INF-514 — Project the last legal straight-drop pose of the active piece

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: A nonoccupying outline shows the last reachable pose along the active piece’s gravity axis at its current lateral position and orientation. It updates with the pose or blocking occupancy.
- Includes: Move a horizontal I piece and use its landing outline to see which columns will be occupied after a hard drop.
- Excludes: An ordered successor preview, a prediction of a sequence of placements, or an already landed piece with occupancy.
- Parameters: Active pose, collision geometry, descent axis and displayed target footprint.
- Evidence: [Tetris Effect decomposition](../games/s-z/tetris-effect.md), TE-002, TE-003.
- Novelty: first isolated for `GAME-0529`; see [TAXONOMY_CHANGE_276](../../research/taxonomy-changes/TAXONOMY_CHANGE_276.md).

## INF-513 — Play reference tones and current indexed responses in the same order

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: An addressed playback action exposes the target sequence and current response sequence in matching position order. The sound of each current position corresponds to that position’s set state and can guide correction.
- Includes: Listen to the reference five-pipe series and then the pitches produced by the entered levels.
- Excludes: A written password, a song that only accompanies play, or a hidden evaluation that discloses neither indexed sequence.
- Parameters: Reference tones, current tones, playback order, indexed positions and pitch mapping.
- Evidence: [The Neverhood decomposition](../games/s-z/the-neverhood.md), NH-007.
- Novelty: first isolated for `GAME-0528`; see [TAXONOMY_CHANGE_275](../../research/taxonomy-changes/TAXONOMY_CHANGE_275.md).

## INF-512 — Distinguish recoverable internal damage from lasting health loss on the same bar

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `Medium`
- Definition: The health surface separately exposes provisional internal damage and already lost health. The difference lets the player judge whether to wait for recovery or finish an eligible damage conversion.
- Includes: Read the recoverable segment on Yi’s health bar after an early parry and the provisional segment on the enemy bar after marking it.
- Excludes: A single undifferentiated health reading, a separate resource gauge, or an exact future recovery time inferred from the overlay alone.
- Parameters: Health bar, recoverable segment, lasting loss and visible change at recovery or conversion.
- Evidence: [Nine Sols decomposition](../games/m-r/nine-sols.md), NS-006, NS-009.
- Novelty: first isolated for `GAME-0527`; see [TAXONOMY_CHANGE_274](../../research/taxonomy-changes/TAXONOMY_CHANGE_274.md).

## INF-511 — Report three separate layer, destruction and support coverage proportions

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: The area result displays separate proportions for opened layers, destroyed counted threats and collected support items. Improving one measure does not make the other measures complete.
- Includes: Read Analyzation, Shot Down and Support Item on the subsystem screen after an Area 1 clear.
- Excludes: An optional points score, a single undifferentiated grade, or estimates of hidden future targets.
- Parameters: Layer total, counted enemies, support items, individual result ratios and presentation.
- Evidence: [Rez decomposition](../games/m-r/rez.md), RZ-009.
- Novelty: first isolated for `GAME-0526`; see [TAXONOMY_CHANGE_273](../../research/taxonomy-changes/TAXONOMY_CHANGE_273.md).

## INF-510 — Disclose pending locks, evolution progress and special charges independently

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: The live display distinguishes the shots queued on the current reticle from progress toward the next form and from available special-attack charges.
- Includes: Read a pending lock count at the reticle, and consult two separate gauges before deciding whether to use Overdrive.
- Excludes: A threat-bearing radar, a single health number, or post-stage completion ratios.
- Parameters: Pending lock count, progress gauge, visible avatar form and charge gauge.
- Evidence: [Rez decomposition](../games/m-r/rez.md), RZ-009.
- Novelty: first isolated for `GAME-0526`; see [TAXONOMY_CHANGE_273](../../research/taxonomy-changes/TAXONOMY_CHANGE_273.md).

## INF-509 — Display need-category readiness separately from individual attribute effects

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: The residence panel exposes current fulfilment under each category, the upgrade minima, and optional or individual attribute gains. A player can distinguish an unfilled category from a supplied alternative with a different return.
- Includes: Inspect a Latium home’s Food, Public Service and Fashion bars and hover over sardines and porridge to compare their effects.
- Excludes: A single happiness score, recipe ratios without residence state or an undisclosed eligibility threshold.
- Parameters: Residence, supply bars, categories, selected need, attributes and upgrade cue.
- Evidence: [Anno 117: Pax Romana decomposition](../games/a-f/anno-117-pax-romana.md), A117-005, A117-006, A117-010.
- Novelty: first isolated for `GAME-0525`; see [TAXONOMY_CHANGE_272](../../research/taxonomy-changes/TAXONOMY_CHANGE_272.md).

## INF-508 — Expose independent engine tier and race-miss count

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: Two race displays reveal the current cumulative engine tier and race-wide recorded mistakes independently, so a rise in one does not imply recovery of the other.
- Includes: Watch the power arrows rise again after a correct buoy while the earlier miss cross remains.
- Excludes: A single boost gauge, inferred previous mistakes, or a shared meter that fills by consuming penalty charges.
- Parameters: Power arrows, cap signal, miss marks and concurrent presentation.
- Evidence: [Wave Race 64 decomposition](../games/s-z/wave-race-64.md), WR-004, WR-005, WR-008.
- Novelty: first isolated for `GAME-0524`; see [TAXONOMY_CHANGE_271](../../research/taxonomy-changes/TAXONOMY_CHANGE_271.md).

## INF-507 — Show the required passing side separately from the perimeter return cue

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: Visible route markers distinguish the required passing side for individual encounters. Outer perimeter markers and a directional warning communicate returning to the course as a separate navigation problem.
- Includes: Pass to the right of a red route buoy. Read the pink perimeter and the return arrow when approaching the outer edge.
- Excludes: A neutral marker valid from either side, a single GPS route recommendation, or inferring the correct side only from a failure message.
- Parameters: Marker meaning, visible side, boundary, warning direction and player view.
- Evidence: [Wave Race 64 decomposition](../games/s-z/wave-race-64.md), WR-004, WR-006, WR-008.
- Novelty: first isolated for `GAME-0524`; see [TAXONOMY_CHANGE_271](../../research/taxonomy-changes/TAXONOMY_CHANGE_271.md).

## INF-506 — Show the current calendar phase and warn before spending it

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: The interface identifies the current named time phase and signals before commitment that an offered activity will consume time. The warning lets the player distinguish a phase-spending choice from free movement and inspection.
- Includes: Read the named hour and an investigation warning before committing to Florian’s substantial examination.
- Excludes: An uninterrupted countdown, an exact future verdict forecast, or performing the phase advance itself.
- Parameters: Named phase, date, offered activity, spending signal and free-action contrast.
- Evidence: [Pentiment decomposition](../games/m-r/pentiment.md), PEN-002, PEN-003.
- Novelty: first isolated for `GAME-0523`; see [TAXONOMY_CHANGE_270](../../research/taxonomy-changes/TAXONOMY_CHANGE_270.md).

## INF-505 — Expose current lie, throw direction, wind, disc recommendation and count

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `Medium`
- Definition: Before delivery the player can see the current lie and route, directional aim, prevailing wind, suggested disc and current count. The displayed information helps prepare a shot without promising its exact landing.
- Includes: Read the wind and recommendation before choosing a disc for a shorter approach to the glowing goal.
- Excludes: An exact future trajectory, undisclosed wind generation, a swing algorithm or an enforced disc assignment.
- Parameters: Lie, aim, wind, suggested class, counted deliveries and feedback.
- Evidence: [Wii Sports Resort decomposition](../games/s-z/wii-sports-resort.md), WSR-002, WSR-009.
- Novelty: first isolated for `GAME-0521`; see [TAXONOMY_CHANGE_268](../../research/taxonomy-changes/TAXONOMY_CHANGE_268.md).

## INF-504 — Indicate the approximate region of a loose contested resource

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: A locator shows the broad arena region of a loose resource as it appears or returns. The cue supports routing without disclosing an exact traversal path.
- Includes: Read the bottom locator when a Power Stone appears on the arena floor.
- Excludes: Only showing the stone count, an exact shortest-path preview, or showing only an already visible pickup in the world.
- Parameters: Resource, loose position, locator region, display timing and route uncertainty.
- Evidence: [Power Stone decomposition](../games/m-r/power-stone.md), PS-009.
- Novelty: first isolated for `GAME-0519`; see [TAXONOMY_CHANGE_266](../../research/taxonomy-changes/TAXONOMY_CHANGE_266.md).

## INF-503 — Expose a local disturbance for a pending habitat encounter

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: A local visible disturbance marks the habitat whose pending arrival can be investigated. It directs the player to the site before the encounter is revealed in the world.
- Includes: Notice shaking tall grass and inspect it to meet the waiting Pokémon.
- Excludes: A fully visible wandering actor, a generic quest marker with no site-specific arrival, or battle telegraph timing.
- Parameters: Marked habitat, visible disturbance, pending encounter and inspection prompt.
- Evidence: [Pokémon Pokopia decomposition](../games/m-r/pokemon-pokopia.md), PP-002, PP-004, PP-007.
- Novelty: first isolated for `GAME-0518`; see [TAXONOMY_CHANGE_265](../../research/taxonomy-changes/TAXONOMY_CHANGE_265.md).

## INF-502 — Disclose coarse and detailed regions in a sensor overview

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: An overview distinguishes locations where current sensor coverage supports detailed information from regions represented coarsely. It can mark scripted objectives outside the selected local view.
- Includes: Switch to the Homeworld sensor view to see objective pings and distinguish areas with current fleet sensor coverage.
- Excludes: A uniformly detailed world map, a local-only unit pane, or the simulation rule deciding what is observable irrespective of this view.
- Parameters: Overview scale, coverage-dependent detail and objective markers.
- Evidence: [Homeworld decomposition](../games/g-l/homeworld.md), HW-002.
- Novelty: first isolated for `GAME-0517`; see [TAXONOMY_CHANGE_264](../../research/taxonomy-changes/TAXONOMY_CHANGE_264.md).

## INF-501 — Expose the beat phase used by freely selected live actions

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: Sound or synchronized visual motion discloses the recurring phase shared by multiple optional live actions. The player can consult that phase when choosing and timing a command without being given an authored list of required next notes.
- Includes: Track the musical pulse, motion and optional beat guide while freely choosing attacks in Hi-Fi RUSH.
- Excludes: An authored sequence of notes to match, a telegraph only for one incoming strike, a purely cosmetic loop with no command relation, or reporting timing only after the attempt.
- Parameters: Beat reference, visible or audible channel, timing phase and aligned action classes.
- Evidence: [Hi-Fi RUSH decomposition](../games/g-l/hi-fi-rush.md), HR-008.
- Novelty: first isolated for `GAME-0516`; see [TAXONOMY_CHANGE_263](../../research/taxonomy-changes/TAXONOMY_CHANGE_263.md).

## INF-500 — Read injury and bleeding from body feedback without a numeric meter

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: Current injury severity is disclosed through changes in the controlled avatar’s posture, gait or animation. A distinct visible bodily sign discloses ongoing bleeding without giving a numeric health value.
- Includes: Regina guards an injured arm or struggles to walk. A blood trail identifies ongoing bleeding and the need to stop it.
- Excludes: Numerical health bars, a body-part treatment selection panel, a cosmetic stain that does not disclose current injury, or a prompt that reports an exact depletion rate.
- Parameters: Current injury, condition animation, distinct ongoing bleed cue and unavailable exact numeric health.
- Evidence: [Original Dino Crisis route](../games/a-f/dino-crisis.md), DC-005. Documentary evidence from the scoped North American release.
- Novelty: first isolated for `GAME-0515`; see [TAXONOMY_CHANGE_262](../../research/taxonomy-changes/TAXONOMY_CHANGE_262.md).

## INF-499 — Show the basic attack footprint while choosing movement

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: When the active combatant is choosing an ordinary move, the interface distinguishes the displayed reach of its ordinary attack from the set of available movement destinations. The attack footprint helps the player judge whether positional movement will enable a strike.
- Includes: The ranged cat’s movement interface shows attack reach in red as the player decides how to approach Tom Tom.
- Excludes: A list of movement destinations alone, an identified next enemy action, a guarantee of hitting the shown cell or a predicted random result.
- Parameters: Active actor, move selection, reachable tiles, basic attack footprint and highlight.
- Evidence: [Mewgenics first battle](../games/m-r/mewgenics.md), MG-003/008. Documentary launch-day scope; no direct play or exact binary.
- Novelty: first isolated for `GAME-0514`; see [TAXONOMY_CHANGE_261](../../research/taxonomy-changes/TAXONOMY_CHANGE_261.md). No external novelty claim.

## INF-498 — Consult an incomplete authored map with independent compass orientation

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the interface exposes an authored, potentially incomplete spatial plan and an independent compass direction for orientation, without guaranteeing the exact current player position, every connected route or every undiscovered feature; the player must relate current local observations to that partial plan.
- Includes: The original Thief mission map is explicitly imperfect; the carried compass points north while the player locates the current corridor from observed landmarks.
- Excludes: INF-496 an acquired floorplan that also discloses current position; explored-terrain painting; an omniscient future patrol map; inferring exact coordinates from a drawn floorplan.
- Parameters: Authored plan, omissions, compass orientation, local landmarks, current observation and unknown player position.
- Evidence: [Original Bafford Expert decomposition](../games/s-z/thief-the-dark-project.md), TH-009; P1 map and compass instructions; P2 Bafford authored maps; S1 north-pointing compass route. Native executable, coefficients, animal/failure timing and saved-state fidelity remain unverified; documentary qualifications stay explicit.
- Novelty: first isolated for `GAME-0513`; operational counterexamples reviewed in [`TAXONOMY_CHANGE_250`](../../research/taxonomy-changes/TAXONOMY_CHANGE_250.md). No external novelty claim.

## INF-497 — Inspect retained public specimens separately from personal catch knowledge

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the museum’s collection and exhibited specimens disclose which eligible species have already been contributed to the shared public collection, separately from a player’s encyclopedia of caught species; current donation selection and refusal provide collection eligibility feedback without forecasting an uncaught future specimen.
- Includes: Inspecting New Leaf aquarium exhibits and the collection list, then choosing an eligible Blathers donation rather than treating encyclopedia credit as museum credit.
- Excludes: INF-352 current fish shadow, bite and caught-species cue; an external complete fishing timetable; a future spawn prediction; claiming New Leaf displays the New Horizons Critterpedia donation icon.
- Parameters: Public collection, exhibited species, inspection, personal caught set, current eligible donation and refusal.
- Evidence: [Original New Leaf fishing decomposition](../games/a-f/animal-crossing-new-leaf.md), NL-007; P1 section 11; S2 museum; S8 original New Leaf museum collection description. Exact native coefficients, installed regional/build parity and controlled save/reload remain unverified. Later community documentation remains qualified corroboration.
- Novelty: first isolated for `GAME-0511`; operational counterexamples reviewed in [`TAXONOMY_CHANGE_248`](../../research/taxonomy-changes/TAXONOMY_CHANGE_248.md). No external novelty claim.

## INF-496 — Expose an acquired authored floor plan with current position rather than explored-terrain growth

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Limited`
- Confidence: `Medium`
- Definition: acquiring and opening an in-world plan makes its pre-authored local floors and the controlled actor’s current position inspectable; the disclosed plan does not need to be painted by visiting each corridor and does not reveal every future story location or hidden collectible.
- Includes: Marshall College Campus Overview, a carried two-floor plan with the current-position arrow.
- Excludes: INF-125 visited-terrain and travel-point map growth; INF-195 partial mission-route HUD markers; SYS-931 paired dungeon map and compass acquisition; an external guide map.
- Parameters: World plan, acquisition, authored floors, current position, viewing control, disclosed topology and absent future information.
- Evidence: [Indiana Jones complete-opening decomposition](../games/g-l/indiana-jones-and-the-great-circle.md), IJ-008; R3 50/385/405; S1 campus-map location. Installed binary, captured presets, native coefficients and save/reload sets remain unverified; premium-access and later documentary sources retain their dates.
- Novelty: first isolated for `GAME-0510`; operational counterexamples reviewed in [`TAXONOMY_CHANGE_247`](../../research/taxonomy-changes/TAXONOMY_CHANGE_247.md). No external novelty claim.

## INF-495 — Expose class-filtered local sensor contacts and an in-range or edge objective bearing

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: a local sensor surface discloses only eligible nearby hostile classes and the current objective’s position within sensor range or its bearing at the range boundary; deliberately omitted hostile classes remain discoverable through ordinary local perception rather than an omniscient terrain map.
- Includes: MechAssault sensor: ground vehicles and airborne threats have classified marks, foot soldiers are omitted, and the yellow objective changes between an outside-range edge arrow and an in-range mark. No enemy BattleMech occurs in the admitted first mission.
- Excludes: INF-364 hostile perception cones and alert-suppressed radar; INF-195 explored terrain-map disclosure; an external strategy map; revealing every foot soldier or future spawn; importing later enemy-mech contacts into the first mission.
- Parameters: Sensor range, eligible/omitted class, classified contact, current objective, range membership, edge bearing and information horizon.
- Evidence: [MechAssault first-sortie decomposition](../games/m-r/mechassault.md), MA-010; P1 p3 sensor legend; R1 210/265/350/470/525. Original disc, captured difficulty, exact coefficients and native timing remain unverified; dated qualifications are retained in the game ledger.
- Novelty: first isolated for `GAME-0509`; operational counterexamples reviewed in [`TAXONOMY_CHANGE_246`](../../research/taxonomy-changes/TAXONOMY_CHANGE_246.md). No external novelty claim.

## INF-492 — Expose partial police briefing knowledge separately from current contact discovery

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the mission preparation surface offers its authored situation, known person profiles, threat images and available floor-plan material, but this prior knowledge is not an omniscient live disclosure of every current contact position or hidden optional report.
- Includes: Ready or Not 1.0 tablet briefing and LSPD-supplied maps/person material for the selected mission.
- Excludes: INF-388 the required objective checklist alone; a real-time full enemy map; requiring the player to hear briefing audio; inventing current positions from a known-person portrait.
- Parameters: Selected mission, situation, known actor, image, available plan, annotation, discovery limit and source age.
- Evidence: [Ready or Not decomposition](../games/m-r/ready-or-not.md), RON-011; P1 New Tablet System; R1 initial briefing/mission preparation. No native execution, exact coefficients, original-launch binary checksum or bug-free implementation is claimed; dated source qualifications remain in the game ledger.
- Novelty: first isolated for `GAME-0508`; operational counterexamples reviewed in [`TAXONOMY_CHANGE_245`](../../research/taxonomy-changes/TAXONOMY_CHANGE_245.md). No external novelty claim.

## INF-493 — Expose a limited live scene through a selected tactical camera viewpoint

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `Medium`
- Definition: a selected tactical camera feed reveals the scene visible from that device current placement and viewing angle, adding a mediated observation point without exposing all occluded contacts or replacing the officer own embodied state.
- Includes: Ready or Not Mirror Gun view under an addressed door and preview of an officer-carried headcam.
- Excludes: INF-115 only the current avatar-centered scene; immutable briefing photographs; replay time scrubbing; full-map enemy disclosure; control transfer to the camera carrier.
- Parameters: Camera, placement, viewing angle, aperture, current visible scene, feed selection and occlusion.
- Evidence: [Ready or Not decomposition](../games/m-r/ready-or-not.md), RON-010/011; P1 team-camera preview; S4 Mirror Gun written operation, launch sensor geometry not natively measured. No native execution, exact coefficients, original-launch binary checksum or bug-free implementation is claimed; dated source qualifications remain in the game ledger.
- Novelty: first isolated for `GAME-0508`; operational counterexamples reviewed in [`TAXONOMY_CHANGE_245`](../../research/taxonomy-changes/TAXONOMY_CHANGE_245.md). No external novelty claim.

## INF-494 — Expose current officer assignment, command and retained personnel readiness

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the tactical and personnel interfaces identify assigned officers and their current command/health state, then expose retained roster availability, stress labels, treatment controls and locked trait status so squad readiness is distinguishable from mission score.
- Includes: Ready or Not red/blue squad labels, Fall In/entry orders, injured/healthy officers and first HQ roster with Anxious/Content and trait padlocks.
- Excludes: Omniscient suspect health; unlocked trait effects before their experience gate; INF-299 aggregate mission evaluation alone; numerical stress or exact therapy-duration prediction not exposed by the inspected interface.
- Parameters: Officer identity, subgroup, active assignment, current order, health label, retained stress, treatment, reserve and trait lock.
- Evidence: [Ready or Not decomposition](../games/m-r/ready-or-not.md), RON-002/005/014; R1 180/220/850/1450/1500/1585/1600/1650; P1 Commander. No native execution, exact coefficients, original-launch binary checksum or bug-free implementation is claimed; dated source qualifications remain in the game ledger.
- Novelty: first isolated for `GAME-0508`; operational counterexamples reviewed in [`TAXONOMY_CHANGE_245`](../../research/taxonomy-changes/TAXONOMY_CHANGE_245.md). No external novelty claim.

## INF-491 — Expose initial boost readiness and accumulating destructive engine heat

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: the driving interface discloses initial boost charging and the current engine-heat warning state so the player can distinguish unavailable boost from a ready but thermally dangerous request without exposing a safe future driving line.
- Includes: Original MotorStorm Boost charging indication and cool-to-critical warning gauge during the first race.
- Excludes: A stored fuel or nitro quantity; a weapon-temperature display; omniscient future collision prediction; exact undocumented heat units.
- Parameters: Initial charging, remaining readiness indication, current heat phase, visual warning and live race view.
- Evidence: [MotorStorm decomposition](../games/m-r/motorstorm.md), MS-004; P1 HUD/control printed pp. 6–7 and 12–13; R1 290/495. No native execution, exact coefficients, captured patch/region or cross-save terrain history is claimed; documentary qualifications remain in the game ledger.
- Novelty: first isolated for `GAME-0507`; operational counterexamples reviewed in [`TAXONOMY_CHANGE_244`](../../research/taxonomy-changes/TAXONOMY_CHANGE_244.md). No external novelty claim.

## INF-489 — Expose current flight threat sectors and pending target marks

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `Medium`
- Definition: the current flight display exposes threat bearings relative to the active attack view together with the aiming reticle and acquired-target marks, supporting sector selection and pending-volley decisions without revealing the entire future route.
- Includes: Original Panzer Dragoon sector radar, rotating aim box and acquired target crosshairs.
- Excludes: A complete future enemy schedule; every hidden enemy being globally visible; an exact lock range or timing formula inferred from a mark alone.
- Parameters: Current sector, relative threat marks, reticle and pending acquisition feedback.
- Evidence: [Panzer Dragoon decomposition](../games/m-r/panzer-dragoon.md), PD-003/009; P2 printed p. 8; R1 555/645/695/740; R2 670/730. Native execution, exact coefficients and disc parity are not claimed.
- Novelty: first isolated for `GAME-0505`; operational counterexamples reviewed in [`TAXONOMY_CHANGE_242`](../../research/taxonomy-changes/TAXONOMY_CHANGE_242.md). No external novelty claim.

## INF-490 — Separate current flight vitality from credited episode closeout

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `Medium`
- Definition: the flight interface distinguishes the controlled body’s current energy and the terminal opponent’s current vitality, while closeout separately exposes destruction proportion, missed enemies, awarded retry credits and the resulting total stock.
- Includes: Original Panzer Dragoon blue energy, red boss health and Episode 1 shot-down/credit display.
- Excludes: Treating current energy and continue credits as the same meter; universal award thresholds inferred from two results; a displayed credit proving a saved disk state.
- Parameters: Body energy, opponent vitality, destruction proportion, missed count, awarded and total credits.
- Evidence: [Panzer Dragoon decomposition](../games/m-r/panzer-dragoon.md), PD-005/007/009; P2 printed p. 8; R1 695/785/820; R2 730/850. Native execution, exact coefficients and disc parity are not claimed.
- Novelty: first isolated for `GAME-0505`; operational counterexamples reviewed in [`TAXONOMY_CHANGE_242`](../../research/taxonomy-changes/TAXONOMY_CHANGE_242.md). No external novelty claim.

## INF-486 — Expose generator heat fulfillment, fuel balance and Overdrive stress

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `Medium`
- Definition: the generator interface separates current city heat fulfillment and fuel availability from the active operating mode and accumulating Overdrive stress, making efficiency benefits and approaching accident risk inspectable before further live progression.
- Includes: Reading New London’s heat-demand bar and generator Overdrive gauge in the original Frostpunk 2 ruleset.
- Excludes: A precise unpublished fuel or accident formula; a universal per-building radial temperature map; later heat-level displays inferred from this original interface.
- Parameters: Current demand/fulfillment, available fuel, operating mode and visible stress.
- Evidence: [Frostpunk 2 decomposition](../games/a-f/frostpunk-2.md), FP2-005/015; P1 2:36–3:43; S3. Native execution, exact coefficients and current binary parity are not claimed.
- Novelty: first isolated for `GAME-0504`; operational counterexamples reviewed in [`TAXONOMY_CHANGE_241`](../../research/taxonomy-changes/TAXONOMY_CHANGE_241.md). No external novelty claim.

## INF-487 — Disclose regional activity cost, risk, discoveries and connections

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `Medium`
- Definition: the revealed regional map exposes known activities, team requirements, exploration duration and difficulty or risk, discovered resource sites and the current connection state without revealing every undiscovered region’s contents.
- Includes: Inspecting a western exploration region before reserving Frostland Teams and then reading its revealed Old Dreadnought site in Frostpunk 2.
- Excludes: Complete omniscience of unexplored Frostland; individually tracked carried scout cargo; a displayed risk label exposing an exact random distribution.
- Parameters: Revealed regions, known sites, team cost, duration, risk and trail state.
- Evidence: [Frostpunk 2 decomposition](../games/a-f/frostpunk-2.md), FP2-010/011; P1 15:52–18:38. Native execution, exact coefficients and current binary parity are not claimed.
- Novelty: first isolated for `GAME-0504`; operational counterexamples reviewed in [`TAXONOMY_CHANGE_241`](../../research/taxonomy-changes/TAXONOMY_CHANGE_241.md). No external novelty claim.

## INF-488 — Separate city ideology, group relations, trust and tension displays

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `Medium`
- Definition: political and city panels separately disclose current opposing ideological directions, each group’s relationship to the government, aggregate governing trust and city tension, so support is not mistaken for general material welfare.
- Includes: Inspecting Frostpunk 2’s three Zeitgeist axes, group portraits, trust and tension indicators.
- Excludes: One interchangeable popularity meter; exact undisclosed future protest timing; flavour ideology with no current relation information.
- Parameters: Ideological axes, group identity/relations, aggregate trust and distinct tension.
- Evidence: [Frostpunk 2 decomposition](../games/a-f/frostpunk-2.md), FP2-007/008; P1 5:10–7:58. Native execution, exact coefficients and current binary parity are not claimed.
- Novelty: first isolated for `GAME-0504`; operational counterexamples reviewed in [`TAXONOMY_CHANGE_241`](../../research/taxonomy-changes/TAXONOMY_CHANGE_241.md). No external novelty claim.

## INF-483 — Preview current and upcoming authored bodily dance moves

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `Medium`
- Definition: a demonstrated dancer and ordered named silhouette cards disclose the current authored bodily move and upcoming changes before they become the scoring target, including explicitly marked repeat-side variants.
- Includes: Original Dance Central’s current and upcoming Flashcards and double-up D marking while Flashcards remain enabled.
- Excludes: A full note-lane fretboard; a call-response instructor turn; an unseen randomly generated next move; treating the demonstrator as a mirror of the player’s actual errors.
- Parameters: Current demonstration, future move order, silhouette, literal move name, double-up marking and preview setting.
- Evidence: [Dance Central decomposition](../games/a-f/dance-central.md), DC-002; P1 printed pp. 6–9; S2; R1 82–214 seconds. Native execution, exact tracking coefficients and current binary parity are not claimed.
- Novelty: first isolated for `GAME-0503`; operational counterexamples reviewed in [`TAXONOMY_CHANGE_240`](../../research/taxonomy-changes/TAXONOMY_CHANGE_240.md). No external novelty claim.

## INF-484 — Expose tracked-player identity and limb-local dance mismatch

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `Medium`
- Definition: a camera-helper silhouette identifies the currently tracked active body, while feedback on the demonstrated dancer localises bodily parts whose movement is not matching the current choreography; this informs correction without revealing an exact detector formula.
- Includes: The white active helper silhouette, gray inactive people and red limb outlines in original Dance Central.
- Excludes: A binary hit marker with no body localisation; a guarantee of perfect real-world anatomical measurement; exact undisclosed joint tolerances; a full recording of physical button input.
- Parameters: Tracked identity, helper visibility, problematic limb, feedback timing and undisclosed recognition tolerance.
- Evidence: [Dance Central decomposition](../games/a-f/dance-central.md), DC-002/006; P1; S1/S2. Native execution, exact tracking coefficients and current binary parity are not claimed.
- Novelty: first isolated for `GAME-0503`; operational counterexamples reviewed in [`TAXONOMY_CHANGE_240`](../../research/taxonomy-changes/TAXONOMY_CHANGE_240.md). No external novelty claim.

## INF-485 — Show ongoing bodily dance quality and cumulative scoring state

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `Medium`
- Definition: during evaluated bodily dance, colour and quality text expose the current movement’s assessment separately from the accumulated numerical score, earned stars and current score multiplier.
- Includes: Original Dance Central’s coloured Spotlight, Flawless text and Boombox score, stars and multiplier.
- Excludes: A terminal-only results report; a life meter that stops this song when emptied; treating current movement quality as the total star grade; disclosed exact scoring source code.
- Parameters: Current quality, colour scale, grade text, accumulated score, stars and multiplier.
- Evidence: [Dance Central decomposition](../games/a-f/dance-central.md), DC-003/004; P1; R1 82–214 seconds. Native execution, exact tracking coefficients and current binary parity are not claimed.
- Novelty: first isolated for `GAME-0503`; operational counterexamples reviewed in [`TAXONOMY_CHANGE_240`](../../research/taxonomy-changes/TAXONOMY_CHANGE_240.md). No external novelty claim.

## INF-481 — Disclose the current story route through requested local guiding threads

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `Medium`
- Definition: a requested local visual guidance effect points along the currently assigned authored route without revealing a terrain map or enumerating the optional branches and rewards beside that route.
- Includes: Hazel requesting the Guiding Strand to the current Chapter 3 objective.
- Excludes: A thrown consumable locator; a full minimap; a guarantee that all side collectibles lie on the indicated path; an external walkthrough.
- Parameters: Current assignment, guidance request, locally shown path and undisclosed side branches.
- Evidence: [South of Midnight decomposition](../games/s-z/south-of-midnight.md), P2 Guiding Strand; R1 current local threads. Exact installed build, captured preset, native input and current binary parity are not established.
- Novelty: first isolated for `GAME-0502`; operational counterexamples reviewed in [`TAXONOMY_CHANGE_239`](../../research/taxonomy-changes/TAXONOMY_CHANGE_239.md). No external novelty claim.

## INF-482 — Expose an optional expiring interaction on an already defeated hostile

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `Medium`
- Definition: after hostile defeat, a contextual visible prompt discloses that the retained body currently permits a distinct optional interaction before disappearing; this is not a living enemy’s stagger or future attack cue.
- Includes: The visible Y Unravel prompt on a defeated Haint.
- Excludes: A living stagger opportunity; an exact numerical remaining timer; the defeat damage itself; a permanently available loot label.
- Parameters: Defeated target, contextual prompt, current interaction availability and disappearance.
- Evidence: [South of Midnight decomposition](../games/s-z/south-of-midnight.md), R1 44:20 visible prompt; S1 state distinction. Exact installed build, captured preset, native input and current binary parity are not established.
- Novelty: first isolated for `GAME-0502`; operational counterexamples reviewed in [`TAXONOMY_CHANGE_239`](../../research/taxonomy-changes/TAXONOMY_CHANGE_239.md). No external novelty claim.

## INF-479 — Expose current firearm dispersion through a weapon-, posture- and movement-sensitive crosshair

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: the active firearm’s crosshair changes its visible spread with equipped weapon, current body posture and movement speed, indicating relative shot precision without revealing the next shot’s exact impact.
- Includes: Original F.E.A.R.’s dynamically resized crosshair, whose smaller size indicates greater precision before firing.
- Excludes: A decorative fixed crosshair; a held-aim focus charge alone; scope magnification itself; a computed exact hit probability; guaranteeing a headshot.
- Parameters: Weapon, posture, movement speed, spread treatment, relative precision and shot uncertainty.
- Evidence: [F.E.A.R. decomposition](../games/a-f/fear.md), M1 base HUD Crosshair paragraph. No native input, exact patch or current-executable parity is claimed.
- Novelty: first isolated for `GAME-0501`; counterexamples reviewed in [`TAXONOMY_CHANGE_238`](../../research/taxonomy-changes/TAXONOMY_CHANGE_238.md). No external novelty claim.

## INF-480 — Expose the current authored mission requirements without a terrain map or prospective reward

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: an inspectable mission-status surface states the currently assigned authored requirements before the player chooses the next local intervention, without requiring a terrain map, a prospective reward offer or a full future mission chain.
- Includes: F.E.A.R.’s Mission Status command and First Encounter’s current gate-control and team-rendezvous assignments.
- Excludes: An external walkthrough; omniscient terrain; a promised-reward task contract; a removable gathering checklist; a dialogue line with no current actionable assignment.
- Parameters: Current mission, assigned requirements, availability of inspection, update boundary and local completion state.
- Evidence: [F.E.A.R. decomposition](../games/a-f/fear.md), M1 base default key chart, Mission Status; S1 First Encounter current ordered objectives. No native input, exact patch or current-executable parity is claimed.
- Novelty: first isolated for `GAME-0501`; counterexamples reviewed in [`TAXONOMY_CHANGE_238`](../../research/taxonomy-changes/TAXONOMY_CHANGE_238.md). No external novelty claim.

## INF-476 — Expose vehicle component faults and separate operating reserves

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: the current vehicle inspection and driving surfaces distinguish installed or missing parts, local condition and eligible fault remedies while exposing separate fuel, electrical charge and environmental exposure needed to judge maintenance and escape readiness.
- Includes: Pacific Drive's wagon part diagram, Flat versus Loose Wheel remedies, headlight charge specification and cockpit fuel, battery and radiation displays.
- Excludes: A single aggregate racing health bar; hidden future failure or quirk diagnosis; a remaining storm countdown inferred from the time-of-day clock; claiming displayed consumption is an independently measured rate.
- Parameters: Part, mount, local condition, fault, remedy, installed comparison, fuel, battery, radiation, selected inspection and current driving state.
- Evidence: [Pacific Drive decomposition](../games/m-r/pacific-drive.md), R1 940/1320/1340/2510/4140/4160/4480; declared interface numbers are not native performance measurements. Source-specific limits remain in the claim ledger; no native execution or current-binary parity.
- Novelty: first isolated for `GAME-0500`; counterexamples reviewed in [`TAXONOMY_CHANGE_237`](../../research/taxonomy-changes/TAXONOMY_CHANGE_237.md). No external novelty claim.

## INF-477 — Disclose travel conditions and local energy-gated escape choices

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: the route-planning surface exposes known destination conditions before departure, and the local navigation surface exposes topography, current position, disclosed anchor sites, receiver energy and currently eligible escape candidates without calculating a safe travel path or revealing all container contents.
- Includes: Pacific Drive's Radio Station route preview with Perpetual Stability and 1 kLIM requirement, followed by the ARC map's anchors, free waypoint, exclusion circle and Link Gateway candidates.
- Excludes: Automatic road guidance; all future junction conditions; an explored room-cell graph; claiming the first stable destination has an entry-triggered countdown; undisclosed container or material contents.
- Parameters: Known destination, conditions, topography, current location, anchors, receiver energy, candidate sites, exclusion region and activation phase.
- Evidence: [Pacific Drive decomposition](../games/m-r/pacific-drive.md), R1 1580/4140/4160/4320/4340/4345/4360. Source-specific limits remain in the claim ledger; no native execution or current-binary parity.
- Novelty: first isolated for `GAME-0500`; counterexamples reviewed in [`TAXONOMY_CHANGE_237`](../../research/taxonomy-changes/TAXONOMY_CHANGE_237.md). No external novelty claim.

## INF-478 — Expose current ordered task steps and pinned gathering deficits

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: the live requirement surface distinguishes the currently disclosed ordered mission step from player-pinned recipe requirements and updates their completion or owned-versus-required counts as eligible state changes, without revealing every later objective or promising that gathering alone completes fabrication.
- Includes: Pacific Drive's first repair, plasma quota, radio transmitter and return instructions alongside the independently pinned replacement-parts checklist.
- Excludes: A fixed all-mission briefing; a reward-and-deadline task offer; hidden future instructions; ingredients reserved by pinning; acquisition equated with crafting or installation.
- Parameters: Current task, ordered step, completion predicate, recipe pin, owned quantity, required quantity, output quantity and disclosed successor.
- Evidence: [Pacific Drive decomposition](../games/m-r/pacific-drive.md), R1 940/1120/1205/1223/2030/2420/2440/2450/3330/4270/4280/4360. Source-specific limits remain in the claim ledger; no native execution or current-binary parity.
- Novelty: first isolated for `GAME-0500`; counterexamples reviewed in [`TAXONOMY_CHANGE_237`](../../research/taxonomy-changes/TAXONOMY_CHANGE_237.md). No external novelty claim.

## INF-473 — Forecast an addressed body target's hit and effect without full enemy omniscience

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: before committing an eligible body-targeted command, selection exposes estimated damage, hit probability and declared attack/target type, affinity, class or secondary effect, without thereby revealing every exact enemy parameter.
- Includes: Wine Cellar targeting-sphere readout and the distinction from exact Status parameters gated by the later unavailable Analysis spell.
- Excludes: Guaranteed future damage; disclosure of every concealed enemy statistic; a turn-order/AP queue; unreadable recording pixels treated as known values.
- Parameters: Selected part, estimated damage, hit chance, declared class/type/affinity and disclosure limit.
- Evidence: [Vagrant Story decomposition](../games/s-z/vagrant-story.md), M1 pp11/17; P1 pp4/5. Source limitations are retained in its claim ledger; no native execution.
- Novelty: first isolated for `GAME-0499`; counterexamples reviewed in [`TAXONOMY_CHANGE_236`](../../research/taxonomy-changes/TAXONOMY_CHANGE_236.md). No external novelty claim.

## INF-474 — Distinguish original item properties from combined current combat statistics

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: inspection exposes an item's original properties and the current combined item/character combat values, including retained durability, charge and declared class/type/affinity effectiveness, so the player can distinguish item development from the presently equipped result.
- Includes: Wine Cellar ORG/EQP status, DP/PP and class/type/affinity panels with optional item-change notices.
- Excludes: Only item identity/quantity; a mandated capacity/polarity/Mod-drain calculation; hidden exact hit formulas; a cosmetic equipment comparison.
- Parameters: Original item properties, combined statistics, durability, charge and class/type/affinity.
- Evidence: [Vagrant Story decomposition](../games/s-z/vagrant-story.md), M1 pp10-12/20; P1 p5. Source limitations are retained in its claim ledger; no native execution.
- Novelty: first isolated for `GAME-0499`; counterexamples reviewed in [`TAXONOMY_CHANGE_236`](../../research/taxonomy-changes/TAXONOMY_CHANGE_236.md). No external novelty claim.

## INF-475 — Reveal concealed local floor panels through contact or eligible detection

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: a concealed authored floor panel's position becomes disclosed when it is triggered or an eligible detection effect marks it; contact-discovered marks remain until room exit, while other detection retains only its declared local and temporary reach.
- Includes: Wine Cellar floor-panel discovery and the eligible carried Eye of Argon room reveal, without borrowing the later Eureka spell.
- Excludes: Every trap visible from initial entry; a complete future-area map; the health/status transition itself; an invented detection duration or permanent global trap knowledge.
- Parameters: Concealed panel, contact, detector, local reveal, temporary duration and room exit.
- Evidence: [Vagrant Story decomposition](../games/s-z/vagrant-story.md), M1 pp15/20; P1 p22 Heal Panel and detector item table. Source limitations are retained in its claim ledger; no native execution.
- Novelty: first isolated for `GAME-0499`; counterexamples reviewed in [`TAXONOMY_CHANGE_236`](../../research/taxonomy-changes/TAXONOMY_CHANGE_236.md). No external novelty claim.

## INF-471 — Expose prospective transport placement and purchase feasibility

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: before committing an eligible transport build or train purchase, the interface exposes its current cost and relevant facility reach or proposed vehicle capability, capacity and length, permitting rejection or revision without claiming hidden future demand.
- Includes: Station industry highlights, track/build price previews and train purchase composition feedback in launch-day Transport Fever 2.
- Excludes: A circular service area assumed from another game; settled arrival counters; undisclosed future production; a corporate income ledger alone.
- Parameters: Proposed facility, access highlight, cost, track proposal, vehicle type, capacity, length and performance.
- Evidence: [Transport Fever 2 decomposition](../games/s-z/transport-fever-2.md),
  complete dated Mining Miracle source/transition ledger; no native execution.
- Novelty: first isolated for `GAME-0498`; no external novelty claim.

## INF-472 — Distinguish current transport demand, load and credited arrival progress

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the current transport surface exposes relevant city needs, ordered service stops, assigned vehicle destination, onboard load and capacity, while authored arrival counters show credited progress separately for each required receiver rather than equating capacity or boarded passengers with completed delivery.
- Includes: City needs overlay, vehicle/line panels and separate Carson City/Reno arrival counters in launch-day Transport Fever 2 Mining Miracle.
- Excludes: Future passenger schedules; one pooled city-arrival quota; treating onboard load as arrival credit; a results-only score report.
- Parameters: Current demand, line, stops, vehicle, destination, load, capacity, receiver-specific counter and required quota.
- Evidence: [Transport Fever 2 decomposition](../games/s-z/transport-fever-2.md),
  complete dated Mining Miracle source/transition ledger; no native execution.
- Novelty: first isolated for `GAME-0498`; no external novelty claim.

## INF-470 — Show current stage collections, money and return phase without finite lives

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the live interface exposes current stage money, independent acquired treasure and successor-key indicators, main and auxiliary health and the switch-triggered return clock, without asserting a finite-life stock or complete future route.
- Includes: Original Normal Wario Land 4 stage HUD and collection feedback.
- Excludes: A finite-lives platform HUD; undisclosed future rooms or enemy outcomes; a results-only collection table.
- Parameters: Money, collected pieces, CD, key, main health, filling gauge, return phase and current local view.
- Evidence: [Wario Land 4 decomposition](../games/s-z/wario-land-4.md),
  preserved Nintendo booklet and bounded written/source ledger; no native play.
- Novelty: first isolated for `GAME-0497`; no external novelty claim.

## INF-468 — Disclose chart distance and system economy while withholding future local markets

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: navigation charts and selected-system reports expose system
  position, measured distance, economy, government and technology so a trader
  can choose a feasible risk-priced destination; they do not reveal its next
  sampled market quotation or exact future local encounters.
- Includes: Original BBC Micro Elite short/long charts, distance query and
  planetary data.
- Excludes: A preview of each next enemy move; all future commodity quotes;
  fog exploration whose systems do not exist until discovered; a guaranteed
  optimal route recommendation.
- Parameters: current system, cursor, selected system, distance, economy,
  government, technology and concealed visit state
- Evidence: [Elite decomposition](../games/a-f/elite.md),
  claims EL-003; pinned original _IB_DISC source reconstruction.
- Novelty: first isolated for `GAME-0491`; disclose chart distance and system economy while withholding future local markets.

## INF-467 — Reveal presently available panel exits and authored situational advice

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: the interface marks a conquered panel’s currently available outgoing directions and presents authored local advice, letting the player distinguish an open successor or obstacle response without disclosing every future panel or the contents of a hidden pickup.
- Includes: Original Comix Zone flashing Attack Arrows, alternative right/down exits and Alissa’s local reports and obstacle advice.
- Excludes: A complete level map; disclosure of every hidden item; a promised optimal route; an exact future enemy command or landing prediction.
- Parameters: current panel, conquered state, outgoing directions, arrow cue, local report and hidden information.
- Evidence: [Comix Zone decomposition](../games/a-f/comix-zone.md), original SEGA booklet and written original-Genesis accounts; CZ-010.
- Novelty: first isolated for `GAME-0490`; transfer tests in `TAXONOMY_CHANGE_227`.

## INF-466 — Preview attached-spirit build changes and shared invocation availability

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `Medium`
- Definition: the interface distinguishes each spirit’s attached, standby and recovering state, shows shared standby counts by element, and previews the class, attribute and ability changes of a requested attachment-state change before commitment.
- Includes: original Golden Sun’s Djinn state colours, change confirmation and elemental summon counts.
- Excludes: an exact future enemy choice; exact future turn order; an unlabelled decorative spirit; a guaranteed successful invocation despite later loss of availability.
- Parameters: owner, state, elemental count, proposed attachment and before/after build.
- Evidence: [Golden Sun decomposition](../games/g-l/golden-sun.md), original Nintendo booklet pp. 16–21 and 39–43; GS-010.
- Novelty: first isolated for `GAME-0489`; configuration consequences and shared paid availability are visible before choice.

## INF-465 — Expose current craft speed, ready function and local targeting cue

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `Medium`
- Definition: the live vehicle interface exposes current speed, the enabled weapon or power-up identity and any currently applicable local targeting cue, without revealing a guaranteed future hit, exact effect expiry or the next grid's selection.
- Includes: original PlayStation wipEout Single Race. The speed bar and weapon icon show current control state; a local marker can identify a target.
- Excludes: A two-slot item queue and coin counter; vehicle health or lives inferred from the speed bar; omniscient future trajectories; exact hidden selection probabilities.
- Parameters: speed indicator, enabled function, local target, cue visibility and information horizon.
- Evidence: [wipEout decomposition](../games/s-z/wipeout.md), original US longbox booklet and contemporary first-hand account; claim WO-006. No original program or direct play inspected.
- Novelty: first isolated for `GAME-0488`; reviewed transfer tests in `TAXONOMY_CHANGE_225` preserve other boundaries.

## INF-463 — Expose current vessel condition and loaded broadside readiness

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `Medium`
- Definition: the sea-combat view displays both vessels’ current condition statistics and the controlled vessel’s loaded-gun readiness alongside visible positions and trajectories, without guaranteeing future impact components or hidden damage rolls.
- Includes: original Windows Sid Meier's Pirates! ordinary sea encounter. Current ship statistics and gun readiness support the next turn or broadside.
- Excludes: A perfect forecast of component damage; a ground-vehicle instrument panel; hidden future rolls; automatic target selection authored by the display alone.
- Parameters: vessel statistics, current component condition, loaded guns, positions, trajectories and visible update.
- Evidence: [Sid Meier's Pirates! decomposition](../games/s-z/sid-meiers-pirates.md), publisher PC manual; claim PIR-012. Exact executable revision, timings and direct play remain uninspected.
- Novelty: first isolated for `GAME-0487`; transfer tests in `TAXONOMY_CHANGE_224` preserve prior boundaries.

## INF-464 — Expose duel advantage, crew counts and live positional danger

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `Medium`
- Definition: the boarding view shows the two captains’ positions, their current crew counts, the tempo-advantage bar and visible disorientation, so an approaching boundary and next-hit surrender risk can be read without an exact future casualty forecast.
- Includes: original Windows Sid Meier's Pirates! ordinary sea encounter. The crew counts and advantage bar explain current pressure, not guaranteed future losses.
- Excludes: A duelist health bar inferred from crew; hidden future attack choices; exact future casualty counts; a cosmetic initiative display with no timing role.
- Parameters: captain positions, stage boundary, crew counts, advantage, disorientation and current cue.
- Evidence: [Sid Meier's Pirates! decomposition](../games/s-z/sid-meiers-pirates.md), publisher PC manual; claim PIR-012. Exact executable revision, timings and direct play remain uninspected.
- Novelty: first isolated for `GAME-0487`; transfer tests in `TAXONOMY_CHANGE_224` preserve prior boundaries.

## INF-462 — Disclose tactical height, individual readiness, facing, reach and fallen count

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `Medium`
- Definition: the battlefield interface exposes addressed vertical panels and selected height, current actor and CT, facing, legal movement and target choices and falling-unit countdown without promising exact future random outcomes or a complete future turn simulation.
- Includes: Original Final Fantasy Tactics battle/status and fallen-unit display.
- Excludes: quantity-bearing hex stacks; an omniscient random-result preview; an asserted exact damage forecast; externally calculated schedule.
- Parameters: panel, altitude, current actor, CT, facing, legal reach, eligible target, count and hidden roll.
- Evidence: [Final Fantasy Tactics decomposition](../games/a-f/final-fantasy-tactics.md), original Square/Sony booklet and original-PS1 written evidence; claims FFT-001–FFT-010. No native executable or direct play was inspected; indexed-source limits remain explicit.
- Novelty: first isolated for `GAME-0486`; transfer tests in `TAXONOMY_CHANGE_223` preserve all earlier boundaries.

## INF-461 — Expose the current town date and hour for clocked visits

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `Medium`
- Definition: the player's watch and calendar disclose the current game hour and date needed to plan time-dependent town visits, without listing every actor's future routine or an exact future event countdown.
- Includes: original Shenmue's inspectable watch/calendar during the sailors inquiry.
- Excludes: an omniscient daily routine table; a discrete-only day-period label; a campaign-deadline countdown; the command that advances a day.
- Parameters: current date, current hour, inspection access and display state.
- Evidence: [Shenmue decomposition](../games/s-z/shenmue.md), original Sega booklet and Dreamcast menu account; claims SH-002 and SH-008.
- Novelty: first isolated for `GAME-0485`; current clock disclosure is independent of service admission and notebook facts.

## INF-460 — Expose contextual search, explored map and password-computer feedback

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `Medium`
- Definition: the current interface reveals local search progress and result or the retained visited-room/tunnel map, utility-code counts, editable acquired fragments, recognised letters and mission clock; optional paid help additionally marks corrected orientation or reports companion-fragment availability.
- Includes: Impossible Mission search bar and contextual pocket-computer views.
- Excludes: all unvisited-room contents; exact guard-program forecasts; a fully solved password disclosed before card recognition.
- Parameters: view context, visited graph, search state, codes, fragments, letters and clock.
- Evidence: [Impossible Mission decomposition](../games/g-l/impossible-mission.md), licensed original-rule reproduction and written original-C64 play; claims IM-001–IM-010. No original executable or direct play was inspected.
- Novelty: first isolated for `GAME-0484`; lower-ID transfer tests in `TAXONOMY_CHANGE_221` preserve earlier boundaries.

## INF-458 — Disclose nearby classified actors, facing, attention and diversion radius

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `Medium`
- Definition: a local radar exposes nearby actor classes and their current facing/attention, mission interest and placed diversion radius, allowing local planning without exposing the entire future route or requiring alert-state radar suppression.
- Includes: original Stranger's Wrath coloured radar and Chippunk radius.
- Excludes: an omniscient whole-world map; Metal Gear Solid's suppressed alert radar; exact future hostile intents.
- Parameters: local range, actor class, facing, attention, mission interest and lure area.
- Evidence: [Oddworld: Stranger's Wrath decomposition](../games/m-r/oddworld-strangers-wrath.md), original EA Xbox booklet and independently authored original-Xbox routes; claims SW-001–SW-012. No direct play, measured timing or exact executable is claimed.
- Novelty: first isolated for `GAME-0483`; lower-ID transfer tests in `TAXONOMY_CHANGE_220` preserve earlier boundaries.

## INF-459 — Disclose incapacitation, capture progress and deferred bounty state

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `Medium`
- Definition: visible hostile damage/incapacitation cues, held collection progress and inspectable recorded bounty state distinguish an eligible live/dead body, a completed capture and pending payment before settlement.
- Includes: original Stranger's Wrath hostile stars/boss bars, bounty meter and inventory.
- Excludes: a probabilistic catch estimate; payment assumed from defeat alone; a hidden future reward forecast.
- Parameters: hostile condition, body status, collection progress, captures and payment state.
- Evidence: [Oddworld: Stranger's Wrath decomposition](../games/m-r/oddworld-strangers-wrath.md), original EA Xbox booklet and independently authored original-Xbox routes; claims SW-001–SW-012. No direct play, measured timing or exact executable is claimed.
- Novelty: first isolated for `GAME-0483`; lower-ID transfer tests in `TAXONOMY_CHANGE_220` preserve earlier boundaries.

## INF-457 — Show current population, collection and settled stage results

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `Medium`
- Definition: the interface reports the current living population and collected optional value, then settles the stage result, without revealing every secret route or imposing an ordinary completion deadline.
- Includes: LocoRoco population/Pickory feedback and Stage Clear result.
- Excludes: a complete hidden-item map; a compulsory deadline inferred from an optional elapsed-time result.
- Parameters: population, collection counters, stage settlement and revealed result.
- Evidence: [LocoRoco decomposition](../games/g-l/locoroco.md), original Sony PSP booklet, Sony launch announcement/creator interview and source-limited contemporary first-stage routes; claims LR-001–LR-009. No direct play or exact geometry is claimed.
- Novelty: first isolated for `GAME-0482`; lower-ID transfer boundaries in `TAXONOMY_CHANGE_219` preserve previous definitions.

## INF-456 — Expose driving-credit deadline, score, stage and route feedback

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Limited`
- Confidence: `Medium`
- Definition: the driving credit presents its remaining countdown, accumulated score, current section and route-progress/result feedback without claiming ranked rivals, finite lives or fully exposed future traffic.
- Includes: Out Run original-mode timer, score, stage, minimap and selected-route result.
- Excludes: complete hidden state; a competitive place among traffic cars; a life stock; future traffic preview; exact internal timer bits from its displayed digits.
- Parameters: countdown display, score, stage, current route, final route result and hidden future.
- Evidence: [Out Run decomposition](../games/m-r/out-run.md), original Sega upright manual and official retrospective, plus original-mode source at Cannonball commit `27493ebf62be3498dff93ed6a45e8e2db819bae1`; claims OR-001–OR-009. Rewrite transfer is not original-binary verification.
- Novelty: first isolated for `GAME-0481`; lower-ID transfer tests in `TAXONOMY_CHANGE_218` preserve earlier definitions.

## INF-454 — Show live population terrain and divine-power availability across two scales

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: a live world map exposes current terrain and faction population/settlement markers while a local close-up exposes actionable geometry; population gauges and a shared divine-resource marker expose relative development and currently available intervention thresholds without revealing the opponent's cursor or future policy.
- Includes: Populous Book of Worlds, Closeup Map, population gauges and Manna Bar.
- Excludes: complete exposure of every decision-relevant state (`INF-001`); exact future AI commands; a static non-updating map.
- Parameters: world/local scale, terrain, faction markers, population, resource and power thresholds.
- Evidence: [Populous decomposition](../games/m-r/populous.md), original 1989 Electronic Arts / Bullfrog manual, printed rules and inspected Amiga diagrams; claims POP-001–POP-010.
- Novelty: first isolated for `GAME-0480`; the lower-ID boundary tests and carrier parameters are recorded in `TAXONOMY_CHANGE_217`.

## INF-455 — Follow a queried population subject with transient zoom information

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: a query tag exposes one population subject's faction, advancement, type and strength or settlement growth, follows documented actor/settlement transfers and surviving combat successor, and disappears without a successor; a zoom command temporarily substitutes its subject's information before the display returns to the tagged subject or becomes blank when none exists.
- Includes: Populous shield quadrants, query transfers and roughly three-second zoom-subject information before the shield restores its bearer.
- Excludes: a permanent omniscient inspector; altering the subject by viewing it; implying exact numeric formulas from a relative bar.
- Parameters: subject, tag, faction, advancement, class, strength/growth, transfer, successor and transient information display.
- Evidence: [Populous decomposition](../games/m-r/populous.md), original 1989 Electronic Arts / Bullfrog manual, printed rules and inspected Amiga diagrams; claims POP-001–POP-010.
- Novelty: first isolated for `GAME-0480`; the lower-ID boundary tests and carrier parameters are recorded in `TAXONOMY_CHANGE_217`.

## INF-453 — Show adventure score, remaining time and replacement-life marks

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: the current adventure display exposes accumulated score, remaining time and finite replacement-life marks alongside the local scene, allowing score exposure and lethal retry risk to be compared without a separate collectible inventory or full-world map.
- Includes: original Pitfall!'s score, twenty-minute clock and spare-Harry marks in the booklet's composite interface diagram.
- Excludes: a separate route-resource count, stage number or combat-capability meter (`INF-347`); a map of all scene indices; inferring that every object in a composite diagram belongs to one playable room.
- Parameters: score, remaining time, replacement count, display marks, local scene and update.
- Evidence: [Pitfall! decomposition](../games/m-r/pitfall.md), original Activision Atari 2600 booklet AX-018-03, controls, score, hazards, composite HUD and David Crane's route advice.
- Novelty: first isolated for `GAME-0479`; the verified HUD exposes a score attempt's three reserves without inventing a collectible tally.

## INF-452 — Show current-city connections without revealing the full itinerary

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `Medium`
- Definition: at the current city, a map and travel view expose known outgoing services, their usable timing and cost implications and the current journey clock, but not every future connection or all authored consequences of travel.
- Includes: planning the next offered journey from Paris in the original iOS *80 Days*.
- Excludes: a fully revealed Slay the Spire act with encounter-category nodes (`INF-062`); an exact prediction of a future story incident; importing later-version route counts into launch iOS.
- Parameters: current city, known routes, offered services, departure state, fare, duration, day and undiscovered successor information.
- Evidence: [80 Days decomposition](../games/0-9/80-days.md), inkle's globe, timing and route-planning descriptions, corroborated by a launch-era iOS account.
- Novelty: first isolated for `GAME-0478`; the player weighs partial intercity knowledge against a running clock.

## INF-451 — Expose local block support and receding tower danger

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the live Nightmare view discloses the nearby block arrangement, current climber position, visible topward goal and the lower tower's loss, so the next push, pull or climb can be planned without revealing a complete future removal schedule.
- Includes: original *Catherine* Underground Cemetery tower and its nearby progress/danger cues.
- Excludes: a whole-stage solved path, exact hidden row-removal interval or unobserved PS3-specific HUD typography; a static Sokoban board with no advancing danger.
- Parameters: visible tower region, block class, support edge, avatar, goal cue, lower frontier and update timing.
- Evidence: [Catherine decomposition](../games/a-f/catherine.md), Atlus's contemporary manual and corroborated original-PS3 stage descriptions.
- Novelty: first isolated for `GAME-0477`; spatial support cues and an independently receding danger frontier jointly inform the next climb move.

## INF-450 — Guide current exercise form and report its combat grade

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: during a selected Fit Skill, show a model of the current required body movement and give immediate grade feedback for the sensed performance so the player can adjust form before later repetitions or turns.
- Includes: Tipp's on-screen demonstration, `Great` or `Good` message, associated glow, sound and controller vibration during early *Ring Fit Adventure* battles.
- Excludes: disclosing hidden exact sensor thresholds or future enemy actions; an end-only fitness estimate; a medical measurement of exercise quality.
- Parameters: selected exercise, displayed pose, sensed form, grade and feedback channels.
- Evidence: [Ring Fit Adventure decomposition](../games/m-r/ring-fit-adventure.md), Nintendo's Adventure Mode guidance.
- Novelty: first isolated for `GAME-0476`; live body-form feedback informs the next physical repetition while also explaining battle damage.

## INF-449 — Expose local affordances through potentially unreliable perception

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `Medium`
- Definition: the local scene exposes reachable foes, contrasting hazard tiles and authored fixture states, but a separately changing perception resource may add audiovisual events that do not reliably report persistent physical state, requiring comparison with stable room and inventory outcomes.
- Includes: Ellia reading tomb traps, candles, a statue and undead while low-sanity effects can mislead in original GameCube Eternal Darkness.
- Excludes: an omniscient map; every visual event being an actual world entity; a health or sanity HUD alone (`INF-119`); undisclosed exact candle solutions.
- Parameters: local view, object affordance, hazard cue, perception resource, misleading event, persistence check and inventory/fixture feedback.
- Evidence: [Eternal Darkness decomposition](../games/a-f/eternal-darkness-sanitys-requiem.md), Nintendo's overview and corroborated contemporary Ellia routes.
- Novelty: first isolated for `GAME-0473`; unreliable presentation does not automatically change the set of physically hostile entities.

## INF-448 — Show a local 3D speed-stage route and live attempt state

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: a following three-dimensional stage view shows Sonic's immediately reachable route and visible local enemies, while the live display exposes elapsed time, collected-ring reserve and remaining lives; the view can be reframed within authored camera limits but does not disclose unseen later geometry.
- Includes: Sonic's first original Dreamcast Emerald Coast camera and Action Stage display.
- Excludes: fixed side-scrolling lookahead (`INF-192`); a full solved route map; guaranteed homing-target disclosure before input; a fixed deadline merely because elapsed time appears.
- Parameters: camera follow, permitted pan, occlusion, local path, enemy visibility, elapsed time, rings, lives and update timing.
- Evidence: [Sonic Adventure decomposition](../games/s-z/sonic-adventure.md), original Dreamcast instruction manual, printed pp. 2 and 18–19.
- Novelty: first isolated for `GAME-0472`; the player reads a reframable 3D path together with the ring/life/time attempt state, without inheriting the side-view Sonic HUD boundary.

## INF-447 — Show active surgical field, tools, vitals and clock

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `Medium`
- Definition: present the currently exposed patient field and instrument choices alongside patient-condition and remaining-time feedback so the next local treatment can be selected without revealing the full future case.
- Includes: first original-DS Trauma Center operation's wounds, shards, incision guide, tool palette, vital display and time.
- Excludes: disclosure of unseen inner shards before incision; exact hidden error penalties; later-operation diagnoses.
- Parameters: exposed field, target positions, tool icons, vitals, clock, guidance and update timing.
- Evidence: [Trauma Center: Under the Knife decomposition](../games/s-z/trauma-center-under-the-knife.md), Nintendo DS overview and corroborated first-operation routes.
- Novelty: first isolated for `GAME-0471`; surgical field and patient viability are live decision information.

## INF-446 — Show segmented racing Boost and immediate crash feedback

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `Medium`
- Definition: the live racing interface exposes stored Boost and its currently available segments, with immediate feedback when a Takedown or crash changes that reserve; it does not reveal future traffic or the precise collision outcome before impact.
- Includes: original Burnout 3: Takedown's first Silver Lake Race Boost bar and Takedown/crash feedback.
- Excludes: place and lap progress alone (`INF-205`); route terms before race entry (`INF-206`); a vehicle's hidden future damage or a guaranteed Aftertouch success.
- Parameters: charge, segment count, cap, gain/loss indication, qualifying event and display update.
- Evidence: [Burnout 3: Takedown decomposition](../games/a-f/burnout-3-takedown.md), original PS2 manual and contemporary route.
- Novelty: first isolated for `GAME-0470`; live temporary capacity is visible separately from the race's ordinal place.

## INF-445 — Show the aimed gravity-fall direction and landing target

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `Medium`
- Definition: while the player aims a gravity shift, a visible targeting cue and the scene's surfaces disclose the current directed-fall target before commitment, without guaranteeing a safe landing or successful attack.
- Includes: Kat's gravity-aim reticle and visible tower or Nevi approach line in original PS Vita Gravity Rush.
- Excludes: an omniscient future collision path; a map waypoint (`INF-125`); a numeric promise of attack damage; a cue for world-global gravity colour (`INF-045`).
- Parameters: aim reticle, current direction, visible target, occlusion and camera orientation.
- Evidence: [Gravity Rush decomposition](../games/g-l/gravity-rush.md), PlayStation's original traversal description and contemporary Vita guide.
- Novelty: first isolated for `GAME-0468`; the cue is for an avatar-local fall that can become traversal or a kick approach.

## INF-444 — Show ribbon-shape input cues and current survival form

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `Medium`
- Definition: the approaching ribbon's visible obstacle shape identifies the next single or composite response, while the controlled character's visible form and local pass/mistake feedback disclose its present survival condition; music supplies timing cues but not an omniscient future course.
- Includes: original PlayStation Vib-Ribbon's block, pit, loop, wave and paired visual shapes, visible rabbit/frog/worm/Queen form, and response feedback during a selected audio-CD track.
- Excludes: the entire future obstacle sequence; a fixed authored soundtrack that signals known geometry (`INF-194`); fretboard lanes and Rock Meter (`INF-379`); exact hidden thresholds.
- Parameters: visible shape, pair markings, lookahead distance, music cue, current form, local feedback and display latency.
- Evidence: [Vib-Ribbon decomposition](../games/s-z/vib-ribbon.md), contemporary PAL guide and original-disc shape enum documentation.
- Novelty: first isolated for `GAME-0467`; shape coding and the character's own evolving body jointly inform the next rhythmic traversal response.

## INF-440 — An acquired dungeon compass audibly flags local key or chest presence

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: after acquisition of the dungeon compass, entering an eligible room produces an audible cue for the presence of a key or treasure chest in that room, without disclosing its exact concealed position, acquisition method or future enemy behaviour.
- Includes: Original Link’s Awakening compass tone on entry to a room containing a key or treasure chest.
- Excludes: an omniscient future map; ordinary environmental sound; a rhythm beat; the compass boss marker alone; claiming this research heard a game recording.
- Parameters: dungeon, compass ownership, entered room, key or chest presence, sound trigger and concealed details.
- Evidence: [Link's Awakening decomposition](../games/s-z/the-legend-of-zelda-links-awakening.md), original Nintendo DMG manual and Nintendo Player's Guide, printed pp. 12–16 and 26–29, documentary reconstruction rather than direct play.
- Novelty: first isolated for `GAME-0458`; no external novelty claim or earlier signature change.

## INF-439 — Expose current road contact through physical steering feedback

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: the cabinet supplies tactile steering resistance or vibration responsive to current road surface and vehicle motion, supplementing visual driving information without revealing an exact future physical trajectory.
- Includes: Original Sega Rally Championship’s documented wheel reaction to road and car movement; no measured force curve.
- Excludes: a static decorative wheel; a HUD icon alone; an omniscient future handling preview; assuming the same force calibration across cabinet editions.
- Parameters: steering mechanism, current contact, vehicle motion, tactile response and calibration.
- Evidence: [Sega Rally Championship decomposition](../games/s-z/sega-rally-championship.md), visually inspected original 1995 Sega twin manual, printed pp. 14–16 and 28; source reconstruction, not cabinet execution.
- Novelty: first isolated for `GAME-0457`; no external novelty claim or earlier definition rewrite.

## INF-438 — Expose current carried-item operations and selected action mode

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: an options surface shows retained item identities, the selected item's usable quantities and eligible operations, and the currently selected character or item action before the shared world input executes it.
- Includes: Alone in the Dark Options inventory, selected weapon quantity and available-versus-chosen action display.
- Excludes: a quick-slot bar alone; future hidden contents; an exhaustive future enemy plan; a displayed hidden weight total.
- Parameters: inventory identities, selected item, quantity, available operations, active verb and display state.
- Evidence: [Alone in the Dark decomposition](../games/a-f/alone-in-the-dark.md), its original DOS CD manual and bounded first-hand written mechanics ledger; reconstruction, not local execution.
- Novelty: first isolated for `GAME-0456`; no external novelty claim or earlier boundary rewrite.

## INF-437 — Cue rhythmic alignment and reveal local assembly outcomes and final grade

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the interface combines musical approach cues with moving target alignment to disclose a response moment, communicates each assembly outcome and exposes a terminal performance grade; an authored phase may reduce visual approach preview without removing musical timing cues.
- Includes: Original DS Built to Scale's musical approach, holed plates, connected or missed rod and final Try Again/OK/Superb result.
- Excludes: Complete omniscient state visibility; an obstacle-traversal soundtrack without graded beat input; instructor button-symbol reproduction; a category-by-category numerical report; disclosure of exact hidden grade thresholds.
- Parameters: Audio phrases, target motion, preview visibility, local feedback, final grade labels and undisclosed evaluation thresholds.
- Evidence: [Rhythm Heaven decomposition](../games/m-r/rhythm-heaven.md), its original-manual and bounded first-hand source ledger.
- Novelty: first isolated for `GAME-0454`; no external novelty or direct-play claim.

## INF-001 — Fully visible current state

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: every decision-relevant element of the current board is visible
  before the player acts.
- Includes: the complete tile layout and values on the standard 2048 board; all
  Rubik's Cube stickers, inspectable by changing viewpoint before a move; the
  settled field and active tetromino in NES Tetris; every given, empty cell and
  player assignment in a printed Sudoku; all walls, goals, crates and the
  keeper in a Sokoban level; every card and its current zone in FreeCell; every
  Nonogram clue and current cell assignment; the current Royal Match board,
  level targets and remaining move count; every visible Water Sort layer and
  empty tube slot; current Into the Breach units, terrain, health and markers;
  every current card and empty cell on the Threes board; Dorfromantik's placed
  landscape, current tile, visible preview and remaining stack count; every
  rope, anchor, star, the candy and Om Nom in a Cut the Rope level; Opus
  Magnum's placed components, instruction rows, atoms, bonds and mechanism
  poses during editing and testing; World of Goo's terrain, hazards, pipe,
  loose population, connected structure and extraction count; Bad North's
  current island terrain, squads, enemies, houses and incoming longships; Loop
  Hero's current route, hero state, known enemies, held cards, equipment
  inventory and accumulated resources; HUMANITY's trial geometry, crowd,
  placed commands, enabled commands and goal fill; Tin Hearts' room geometry,
  soldiers, routing devices, hazards, exit and rescued progress; Timelie's
  current maze, actors, robots, doors and scheduled command state; SpaceChem's
  routes, symbols, waldos, atoms, bonds, ports and current fault state;
  Portal's chamber, cubes, buttons, hazards and apertures; Braid's current Tim,
  enemy, platform, key, gate, switch and puzzle-piece state; Pikmin 4's current
  leaders, followers, targets, routes, tasks and day clock; Patrick's Parabox's
  inspectable current grids, occupants, goals and containment relations;
  Cosmic Express's fixed grid, route, passengers, homes and carriage capacity;
  The Swapper's room geometry, bodies, coloured fields, mechanisms and orb;
  Carto's acquired map fragments, terrain edges, current arrangement, avatar
  location and corresponding traversable world regions; Viewfinder's current
  world geometry, held source image, placement plane, avatar and teleporter;
  Fights in Tight Spaces' current arena, occupants, health, hand, momentum and
  primed hostile indicators; A
  Good Snowman Is Hard to Build's monster, walls, remaining snow, ball sizes
  and ordered stacks; Snakebird's fixed terrain, fruit, exit state and ordered
  body segments; The Case of the Golden Idol's inspectable tableau, extracted
  terms and current Thinking-panel assignments; every platform, barrier, target
  cell and ordered body segment in a scoped Can of Wormholes stage; the local
  A Monster's Expedition land, water, stopper, log pose and target shore; every
  current trigger, line, hook, crossing and linkage in scoped HOOK levels; all
  LYNE endpoints, typed waypoints, nexus capacities and current route segments;
  all 25 current lit or unlit states on a Lights Out field; every Slant clue,
  empty cell and assigned diagonal; every Tents tree, side quota and current
  tent or non-tent assignment; every Dominosa digit and current selected or
  rejected pair; every Bridges island clue and current single or double bridge;
  every Light Up wall, clue, bulb and currently illuminated white cell; every
  Loopy dot, face clue and current edge mark; every Map boundary, immutable
  colour and current editable-region assignment; every Galaxies cell, centre
  dot and current boundary mark; every Filling cell, immutable digit and
  current editable-cell assignment; every Keen cage, operation, target and
  current digit; every Pearl clue and selected link; every Signpost arrow,
  immutable number, current successor link and derived chain label; every Net
  tile shape, orientation, lock and centre-connected component highlight; every
  Netslide tile mask, current position, fixed barrier and connected highlight;
  Machinarium's currently exposed scrapyard objects, Josef configuration,
  acquired inventory and prepared pole state; The Longest Journey's current
  constituent or composite inventory identities, exposed ducky subpart and
  visible track-key target; Day of the Tentacle's current held ingredients and
  constructed battery on Red Edison's shelf; Monument Valley's current Ida
  position, fixed route surfaces, rotating bridge pose and final pedestal;
  Maquette's current model, corresponding courtyards, key pose, gaps, doors and
  house state; Factorio's explored terrain, placed entities, inventories,
  moving items, active recipes, power state and visible hostile units; each
  Split Fiction player's local Chapter 1 geometry, hazards and prompts.
- Excludes: knowledge of future random events.
- Parameters: simultaneous display versus sequential inspection.
- Evidence: [2048 decomposition](../games/0-9/2048.md) and
  [Rubik's Cube decomposition](../games/m-r/rubiks-cube.md), and
  [Tetris decomposition](../games/s-z/tetris.md), and
  [Sudoku decomposition](../games/s-z/sudoku.md), and
  [Sokoban decomposition](../games/s-z/sokoban.md), and
  [FreeCell decomposition](../games/a-f/freecell.md), and
  [Nonogram decomposition](../games/m-r/nonogram.md), and
  [Royal Match decomposition](../games/m-r/royal-match.md), and
  [Water Sort decomposition](../games/s-z/water-sort.md), and
  [Chess decomposition](../games/a-f/chess.md), and
  [Flow Free decomposition](../games/a-f/flow-free.md), and
  [Baba Is You decomposition](../games/a-f/baba-is-you.md), and
  [Lights Out decomposition](../games/g-l/lights-out.md), and
  [Into the Breach decomposition](../games/g-l/into-the-breach.md), and
  [Threes decomposition](../games/s-z/threes.md), and
  [Mini Metro decomposition](../games/m-r/mini-metro.md), and
  [Peg Solitaire decomposition](../games/m-r/peg-solitaire.md), and
  [Dorfromantik decomposition](../games/a-f/dorfromantik.md), and
  [Cut the Rope decomposition](../games/a-f/cut-the-rope.md), and
  [Opus Magnum decomposition](../games/m-r/opus-magnum.md), and
  [Lemmings decomposition](../games/g-l/lemmings.md), and
  [World of Goo decomposition](../games/s-z/world-of-goo.md), and
  [Bad North decomposition](../games/a-f/bad-north.md), and
  [Loop Hero decomposition](../games/g-l/loop-hero.md), and
  [HUMANITY decomposition](../games/g-l/humanity.md), and
  [Tin Hearts decomposition](../games/s-z/tin-hearts.md), and
  [Timelie decomposition](../games/s-z/timelie.md), and
  [SpaceChem decomposition](../games/s-z/spacechem.md),
  [Portal decomposition](../games/m-r/portal.md), and
  [Braid decomposition](../games/a-f/braid.md), and
  [Pikmin 4 decomposition](../games/m-r/pikmin-4.md), and
  [Patrick's Parabox decomposition](../games/m-r/patricks-parabox.md), and
  [Cosmic Express decomposition](../games/a-f/cosmic-express.md), and
  [The Swapper decomposition](../games/s-z/the-swapper.md),
  [Carto decomposition](../games/a-f/carto.md), and
  [Viewfinder decomposition](../games/s-z/viewfinder.md), and
  [A Good Snowman Is Hard to Build decomposition](../games/a-f/a-good-snowman-is-hard-to-build.md),
  [Snakebird decomposition](../games/s-z/snakebird.md), and
  [The Case of the Golden Idol decomposition](../games/s-z/the-case-of-the-golden-idol.md),
  [Can of Wormholes decomposition](../games/a-f/can-of-wormholes.md), and
  [A Monster's Expedition decomposition](../games/a-f/a-monsters-expedition.md),
  and [Tactical Breach Wizards decomposition](../games/s-z/tactical-breach-wizards.md),
  and [KAMI decomposition](../games/g-l/kami.md), and
  [HOOK decomposition](../games/g-l/hook.md),
  [LYNE decomposition](../games/g-l/lyne.md), and
  [Hexologic decomposition](../games/g-l/hexologic.md), and
  [Rush Hour decomposition](../games/m-r/rush-hour.md), and
  [SET decomposition](../games/s-z/set.md), and
  [Slant decomposition](../games/s-z/slant.md), and
  [Tents decomposition](../games/s-z/tents.md), and
  [Dominosa decomposition](../games/a-f/dominosa.md), and
  [Bridges decomposition](../games/a-f/bridges.md), and
  [Light Up decomposition](../games/g-l/light-up.md), and
  [Loopy decomposition](../games/g-l/loopy.md), and
  [Map decomposition](../games/m-r/map.md), and
  [Galaxies decomposition](../games/g-l/galaxies.md), and
  [Filling decomposition](../games/a-f/filling.md), and
  [Keen decomposition](../games/g-l/keen.md), and
  [Pearl decomposition](../games/m-r/pearl.md), and
  [Signpost decomposition](../games/s-z/signpost.md), and
  [Net decomposition](../games/m-r/net.md), and
  [Netslide decomposition](../games/m-r/netslide.md),
  [Machinarium decomposition](../games/m-r/machinarium.md), and
  [The Longest Journey decomposition](../games/s-z/the-longest-journey.md), and
  [Day of the Tentacle decomposition](../games/a-f/day-of-the-tentacle.md), and
  [Stardew Valley decomposition](../games/s-z/stardew-valley.md), and
  [The Talos Principle decomposition](../games/s-z/the-talos-principle.md),
  [Fez decomposition](../games/a-f/fez.md),
  [Echochrome decomposition](../games/a-f/echochrome.md),
  [Monument Valley decomposition](../games/m-r/monument-valley.md), and
  [Superliminal decomposition](../games/s-z/superliminal.md), and
  [Manifold Garden decomposition](../games/m-r/manifold-garden.md), and
  [Maquette decomposition](../games/m-r/maquette.md),
  [Antichamber decomposition](../games/a-f/antichamber.md), and
  [Factorio decomposition](../games/a-f/factorio.md), and
  [Split Fiction decomposition](../games/s-z/split-fiction.md).
- Additional support: [Space Invaders decomposition](../games/s-z/space-invaders.md),
  for the visible current rack, base, fortress masks, projectiles, score and
  remaining base stock, with undisclosed future shot timing and UFO value.
- Novelty: not assessed.

## INF-002 — Unpreviewed random future event

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: the next random state change is not revealed before the action
  that triggers it.
- Includes: both the value and position of the next 2048 tile; the types of
  Royal Match items that will refill vacated board cells; Mini Metro's next
  station opening and passenger arrival before the system selects them; Loop
  Hero's next random dawn spawn, card reward opportunity and loot identity;
  Slay the Spire's unrevealed encounter identity, card offer and relic or
  potion result before the run seed resolves that future node.
- Excludes: a preview queue or deterministic future state.
- Evidence: [2048 decomposition](../games/0-9/2048.md) and
  [Royal Match decomposition](../games/m-r/royal-match.md), and
  [Mini Metro decomposition](../games/m-r/mini-metro.md),
  [Loop Hero decomposition](../games/g-l/loop-hero.md), and
  [Slay the Spire decomposition](../games/s-z/slay-the-spire.md), and
  [The Binding of Isaac: Rebirth decomposition](../games/s-z/the-binding-of-isaac-rebirth.md).
- Additional support: [Darkest Dungeon decomposition](../games/a-f/darkest-dungeon.md),
  for the hidden per-round initiative roll and each brigand's undisclosed skill selection.
- Additional support: [Dead Cells decomposition](../games/a-f/dead-cells.md),
  for the unpreviewed next room, drop and blueprint assignment.
- Novelty: not assessed; this is part of the baseline genome.

## INF-003 — Fixed concealed current state

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: decision-relevant contents already exist in the current state but
  remain inaccessible until an information-revealing action occurs.
- Includes: fixed mine locations under covered Minesweeper cells; a fixed
  concealed Mastermind code or Wordle answer tested by successive guesses; the current concealed
  order of Balatro's remaining draw pile while the hand and remaining deck
  composition are inspectable; the current concealed order of Fights in Tight
  Spaces' draw pile while the visible hand and deck contents constrain future
  card availability; The Room's authored items and mechanisms behind unopened
  covers, plates and locks; the concealed order of a Slay the Spire combat
  draw pile while the deck list and visible hand remain inspectable.
- Excludes: a future random event not yet selected; an inspectable element that
  is merely offscreen; information the player once saw and forgot.
- Parameters: setup distribution, known global content count, first-action
  conditioning and reveal permanence.
- Evidence: [Minesweeper decomposition](../games/m-r/minesweeper.md),
  [Mastermind decomposition](../games/m-r/mastermind.md),
  [Wordle decomposition](../games/s-z/wordle.md), and
  [Balatro decomposition](../games/a-f/balatro.md), and
  [Fights in Tight Spaces decomposition](../games/a-f/fights-in-tight-spaces.md),
  [The Room decomposition](../games/s-z/the-room.md), and
  [Slay the Spire decomposition](../games/s-z/slay-the-spire.md), and
  [Strands decomposition](../games/s-z/strands.md), and
  [Magic: The Gathering Arena decomposition](../games/m-r/magic-the-gathering-arena.md),
  and [Yu-Gi-Oh! Master Duel decomposition](../games/s-z/yu-gi-oh-master-duel.md).
- Additional support: [Darkest Dungeon decomposition](../games/a-f/darkest-dungeon.md),
  for corridor tile contents that exist at generation but are exposed only on entry or by a scouting roll.
- Novelty: not assessed.

## INF-004 — Exact local aggregate clue

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: a visible clue position reports the exact aggregate count of
  positions belonging to one fixed concealed target class in its declared
  local neighbourhood.
- Includes: Minesweeper mine clues from 0 through 8 on a square grid; Hexcells
  Infinite black clues counting adjacent blue cells on a hex grid.
- Excludes: approximate hints; the global remaining-hazard count alone; direct
  identification of which neighbouring position belongs to the target class;
  a whole-line ordered run description.
- Parameters: target class, neighbourhood topology, clue range and display
  convention.
- Evidence: [Minesweeper decomposition](../games/m-r/minesweeper.md) and
  [Hexcells Infinite decomposition](../games/g-l/hexcells-infinite.md).
- Novelty: not assessed.

## INF-005 — Exact ordered successor preview

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the player is shown the exact identities and order of one or more
  elements already scheduled to become available next.
- Includes: the enabled-by-default one-piece `NEXT` tetromino display in NES
  Tetris; the ordered five-piece pipe dispenser in Pipe Dream; Dorfromantik's
  visible current tile and ordered successor preview.
- Excludes: showing only a probability distribution or category; revealing no
  future element; an unordered set that does not identify which element is
  next.
- Parameters: preview depth, visibility control and displayed attributes.
- Evidence: [Tetris decomposition](../games/s-z/tetris.md) and
  [Pipe Mania decomposition](../games/m-r/pipe-mania.md), and
  [Dorfromantik decomposition](../games/a-f/dorfromantik.md).
- Novelty: not assessed.

## INF-006 — Visible ordered run-length description

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: each declared line exposes the exact ordered sequence of lengths
  of its filled contiguous runs while withholding the runs' absolute positions.
- Includes: a Nonogram row clue `3 1 2`, meaning a run of three, then one, then
  two in that order with separation.
- Excludes: an unordered total of filled cells; exact local hazard counts; a
  fully specified target image; clues concealed until later play.
- Parameters: line orientation, run count, run lengths and whether colours are
  encoded.
- Evidence: [Nonogram decomposition](../games/m-r/nonogram.md).
- Novelty: not assessed.

## INF-007 — Public action-history state

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: every participant observes the action sequence, and retained
  facts from that public history remain decision-relevant even when the current
  spatial arrangement does not encode them.
- Includes: knowing chess castling and en-passant rights, repetition history and
  the sequence relevant to automatic draw counters.
- Excludes: concealed actions; private hands; future random events; information
  derivable entirely from the visible current arrangement.
- Parameters: record persistence, remembered event classes and whether a formal
  move record is available.
- Evidence: [Chess decomposition](../games/a-f/chess.md).
- Novelty: not assessed.

## INF-008 — Visible executable rule syntax

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the current mechanical rules are disclosed through visible,
  spatially arranged symbols whose syntactic configuration determines which
  rules are active.
- Includes: visible noun, `IS` and property word blocks in Baba Is You.
- Excludes: static instructional prose; hidden rules learned only by trial;
  visible objects whose arrangement changes state but not rule syntax.
- Parameters: symbol language, reading directions, grammar and separate active
  rule display.
- Evidence: [Baba Is You decomposition](../games/a-f/baba-is-you.md).
- Novelty: not assessed.

## INF-009 — Exact committed hostile-intent preview

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: before the player acts, every hostile unit's already committed
  action exposes its acting unit, target positions, effect and relative
  execution order.
- Includes: Into the Breach attack arrows, damage indicators and attack-order
  display; Fights in Tight Spaces primed-attack ranges, effects and displayed
  enemy order.
- Excludes: predicting an opponent's not-yet-chosen move; a probability
  distribution over possible attacks; previewing only the next falling piece.
- Parameters: preview horizon, displayed effect attributes, order display and
  cancellation visibility.
- Evidence: [Into the Breach decomposition](../games/g-l/into-the-breach.md)
  and [Fights in Tight Spaces decomposition](../games/a-f/fights-in-tight-spaces.md).
- Novelty: not assessed.

## INF-010 — Category-bounded next-element preview

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: before the next action, the player sees a category that contains
  the successor element but may withhold its exact identity and insertion
  position.
- Includes: Threes showing an exact coloured base card or a white / `+`
  high-card category while leaving the eligible entry lane unresolved.
- Excludes: an exact successor identity (`INF-005`); no preview of the next
  random event (`INF-002`); a probability distribution with no guaranteed
  category.
- Parameters: category vocabulary, exact base-card exceptions, candidate value
  range and whether position is disclosed.
- Evidence: [Threes decomposition](../games/s-z/threes.md).
- Novelty: not assessed.

## INF-011 — Exact visible input-output assembly schema

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: before construction begins, the puzzle discloses the exact
  identities, relations and acceptance-relevant geometry of every supplied
  input assembly and required output product, whether the transformation is
  performed directly or through an executing machine.
- Includes: Opus Magnum's visible input and output molecular diagrams;
  SpaceChem's visible reagent and required product bond structures, with screen
  orientation ignored where acceptance uses graph equivalence; Infinifactory's
  visible input and target voxel arrangements with required output orientation;
  inbento's complete typed piece footprints and per-cell recipe.
- Excludes: revealing only a target score or category; hidden transformation
  rules; visibility of material currently moving through the machine.
- Parameters: input and output count, identity vocabulary, relation or bond
  representation, spatial geometry, orientation and equivalence rule.
- Evidence: [Opus Magnum decomposition](../games/m-r/opus-magnum.md) and
  [SpaceChem decomposition](../games/s-z/spacechem.md), and
  [Infinifactory decomposition](../games/g-l/infinifactory.md), and
  [inbento decomposition](../games/g-l/inbento.md).
- Novelty: not assessed.

## INF-012 — Scene-indexed revisitable fixed evidence

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: decision-relevant facts are distributed across a finite set of
  named, immutable scenes that become selectively accessible, remain stable
  across visits and can be cross-referenced after discovery.
- Includes: Return of the Obra Dinn death memories, their transcripts, depicted
  participants and book links between a person and scenes where they appear.
- Excludes: concealed contents revealed permanently by one action; a random
  future event; every relevant fact being simultaneously visible in the
  current scene.
- Parameters: scene-discovery order, indexing metadata, transcript availability,
  bookmarks and revisit path.
- Evidence: [Return of the Obra Dinn decomposition](../games/m-r/return-of-the-obra-dinn.md)
  and [Blue Prince decomposition](../games/a-f/blue-prince.md).
- Novelty: not assessed.

## INF-013 — Finite identity roster with disclosed role metadata

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the puzzle exposes a complete finite list of candidate identities
  and structured attributes while withholding the mapping from those labels to
  the subjects observed in evidence.
- Includes: the Obra Dinn manifest listing names, occupations and nationalities
  alongside an illustration containing the sixty faces.
- Excludes: an unknown population whose candidate names emerge gradually; a
  complete disclosed identity-to-face mapping; an unlabelled set of hazards.
- Parameters: roster size, metadata fields, portrait grouping and whether
  confirmed identities are eliminated from unresolved choices.
- Evidence: [Return of the Obra Dinn decomposition](../games/m-r/return-of-the-obra-dinn.md).
- Novelty: not assessed.

## INF-014 — Navigable nested panel scene graph

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: each visible panel is one node in a deterministic illustrated
  scene graph; visible focus or navigation affordances disclose routes to other
  views, but only the current node per panel is displayed at once.
- Includes: Gorogoa hiding deeper pictures, rooms, frames and alternate crops
  behind zoom-in, zoom-out and pan transitions in each of four panels.
- Excludes: a finite set of separately indexed evidence scenes; exact successor
  preview; concealed content exposed permanently by one reveal.
- Parameters: graph depth, branching, affordance visibility, backtracking and
  simultaneous panel count.
- Evidence: [Gorogoa decomposition](../games/g-l/gorogoa.md).
- Novelty: not assessed.

## INF-015 — Prospective structural-link preview

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: before a held live structural node is committed, the interface
  shows the exact connection topology that the current position would create
  while leaving later force response or operational load unresolved.
- Includes: World of Goo guidelines displaying prospective strands from a held
  Goo Ball to nearby structural nodes.
- Excludes: previewing a supplied successor element; displaying only generic
  placement validity; predicting the complete physical deformation after
  commitment.
- Parameters: previewed neighbour set, link count, validity colour and whether
  geometry updates continuously during drag.
- Evidence: [World of Goo decomposition](../games/s-z/world-of-goo.md).
- Novelty: not assessed.

## INF-016 — Visible carrier-arrival telegraph

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: a currently visible in-world carrier and its approach disclose a
  future boundary region where a transported group will enter active play,
  while leaving those occupants' later targets and effects unresolved.
- Includes: an approaching Bad North Viking longship giving advance warning of
  the shore region at which its group will land.
- Excludes: an exact committed action for every hostile unit; an abstract spawn
  marker with no carrier transit; an unpreviewed random insertion.
- Parameters: visible approach horizon, landing-region precision, payload
  visibility, speed readability and route variability.
- Evidence: [Bad North decomposition](../games/a-f/bad-north.md).
- Novelty: not assessed.

## INF-017 — Prospective autonomous-route projection

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: before paused autonomous traversal resumes, the interface draws
  the predicted route through the current routing surfaces or devices.
- Includes: Tin Hearts' projected soldier path updating after a prism block is
  repositioned or rotated while time is frozen.
- Excludes: prospective structural links alone; a carrier-arrival region; a
  guarantee of the complete future state of multiple colliding bodies.
- Parameters: projection horizon, device classes represented, collision detail,
  update latency and whether uncertainty is displayed.
- Evidence: [Tin Hearts decomposition](../games/s-z/tin-hearts.md).
- Novelty: not assessed.

## INF-018 — Exact scrubbed future-state preview

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: moving a time cursor forward exposes the complete deterministic
  world states that the current command schedule would produce, including
  actor, hostile and interactive-object consequences up to a terminal boundary.
- Includes: seeking forward in Timelie to observe patrol positions, character
  paths, door states, pursuit and capture under the current plan.
- Excludes: a drawn route without resolved world consequences; one committed
  hostile action preview; a prerecorded replay that cannot inform revision.
- Parameters: preview horizon, state fidelity, seek granularity, failure cutoff,
  hidden variables and update behaviour after plan edits.
- Evidence: [Timelie decomposition](../games/s-z/timelie.md).
- Novelty: not assessed.

## INF-019 — Live cross-portal scene view

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: an active portal surface continuously displays the scene visible
  from its paired endpoint under the corresponding transformed viewpoint,
  before the player or an object crosses it.
- Includes: looking through a Portal aperture to inspect its exit side, hazards
  or the player character from the remote viewpoint.
- Excludes: a symbolic destination label; a route-only future projection; a
  prerecorded camera view that does not update with the current world.
- Parameters: recursion depth, field of view, occlusion, update latency,
  displayed body classes and incomplete-pair presentation.
- Evidence: [Portal decomposition](../games/m-r/portal.md).
- Novelty: not assessed.

## INF-020 — Visible rewind-affinity marking

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: before temporal manipulation, a persistent visual treatment
  identifies which current entities will not restore with ordinary world state
  when the player rewinds.
- Includes: Braid's green glow on time-immune keys, doors, switches, platforms
  or enemies.
- Excludes: discovering immunity only after testing; an exact preview of every
  future state; colour that has no rule consequence.
- Parameters: marked affinity classes, animation, visibility range, inheritance
  by carried objects and mixed-affinity composite mechanisms.
- Evidence: [Braid decomposition](../games/a-f/braid.md).
- Novelty: not assessed.

## INF-021 — Visible cooperative-work capacity state

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: before and during cooperative work, the interface exposes the
  target's required capacity and the currently committed workers or strength,
  making the threshold for starting and accelerating the task inspectable.
- Includes: Pikmin 4 showing a treasure's carrying requirement and the current
  Pikmin / Oatchi carrying strength assigned to it.
- Excludes: an undisclosed capacity learned only by failed assignment; generic
  follower headcount; a prospective route projection after work begins.
- Parameters: unit count versus weighted strength, maximum assignment, speed
  indication, target lock display and mixed-worker contribution.
- Evidence: [Pikmin 4 decomposition](../games/m-r/pikmin-4.md).
- Novelty: not assessed.

## INF-022 — Nested-space view with parent-boundary context

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: while one contained space is expanded as the active local view,
  the interface simultaneously retains the relevant surrounding parent
  geometry and boundary correspondence needed to judge whether outward transfer
  is currently possible.
- Includes: Patrick's Parabox enlarging a box interior while leaving its parent
  context visible around the box, including walls that block a proposed exit.
- Excludes: a view showing only the active interior; selectable hidden nodes of
  an illustrated scene graph; a live view through a paired portal endpoint.
- Parameters: parent depth shown, scale, occlusion, boundary highlights,
  recursive rendering depth and focus transition.
- Evidence: [Patrick's Parabox decomposition](../games/m-r/patricks-parabox.md).
- Novelty: not assessed.

## INF-023 — Post-commit violated-clue indication

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: after a submitted complete answer is rejected, the interface
  identifies at least one currently violated clue instance or rule location
  without displaying a corrected answer.
- Includes: an invalid The Witness panel submission blinking implicated square
  clues red while leaving the player to infer a valid partition.
- Excludes: a generic failure sound with no located cause; highlighting illegal
  geometry continuously before submission; revealing the complete solution;
  merely keeping all current clues visible.
- Parameters: indicated violation subset, delay, duration, ordering, ambiguous
  responsibility, repeated submissions and accessibility channel.
- Evidence: [The Witness decomposition](../games/s-z/the-witness.md).
- Novelty: not assessed.

## INF-024 — Persistent extracted phrase bank with answer scaffold

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: terms explicitly collected from distributed case evidence remain
  visible as a reusable hypothesis vocabulary alongside a partially written
  structured answer whose fixed text signals possible semantic roles.
- Includes: The Case of the Golden Idol retaining names and place words at the
  bottom of its Thinking screen while the event Scroll supplies grammatical
  context around blank slots.
- Excludes: a complete candidate identity roster disclosed before exploration;
  unstructured personal notes; clues that remain only at their original scene
  locations; feedback identifying a violated answer slot.
- Parameters: bank grouping, found / missing indicator, fixed scaffold text,
  phrase categories, sorting and cross-panel availability.
- Evidence: [The Case of the Golden Idol decomposition](../games/s-z/the-case-of-the-golden-idol.md).
- Novelty: not assessed.

## INF-025 — Exact reactive hostile-consequence preview

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: before tactical commit, the interface exposes the exact hostile
  attacks and immediate resulting state computed from the player's current
  tentative actions, and updates that disclosure when the draft changes.
- Includes: Tactical Breach Wizards Foresee showing who current enemies will
  attack and the damage / displacement outcome of the current turn draft.
- Excludes: hostile actions already committed before the player acts; a
  probability distribution; a route-only projection; random-access scrubbing
  across a multi-time deterministic world trajectory.
- Parameters: displayed actors, targets and effects, simulation depth, target-
  update timing, order display and failure-state detail.
- Evidence: [Tactical Breach Wizards decomposition](../games/s-z/tactical-breach-wizards.md).
- Novelty: not assessed.

## INF-026 — Visible local target-contiguity qualifier

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: a visible qualifier on an exact local target-count clue states
  that all counted target-class neighbours form one contiguous run in the
  clue's declared neighbourhood order.
- Includes: braces around a Hexcells Infinite black clue stating that its
  counted adjacent blue cells are consecutive around the hexagonal ring.
- Excludes: an unqualified exact local count; ordered run lengths spanning a
  complete row or column; a qualifier stating that target neighbours are
  separated rather than contiguous.
- Parameters: neighbourhood order, cyclic-versus-linear adjacency, target
  class, run count and notation.
- Evidence: [Hexcells Infinite decomposition](../games/g-l/hexcells-infinite.md).
- Novelty: not assessed.

## INF-027 — Exact next hostile-step preview

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: before the next player action, the interface identifies each
  hostile unit's exact next automatic behavioural step and the attack geometry
  when that step is an attack.
- Includes: Shogun Showdown showing whether an enemy will move, prepare an
  attack or execute its currently queued attack after the player's turn.
- Excludes: a complete hostile attack committed before a multi-action planning
  phase; a learned but undisplayed later behaviour pattern; a probability over
  possible responses.
- Parameters: preview horizon, displayed movement direction, attack footprint,
  damage, response order and update timing after displacement.
- Evidence: [Shogun Showdown decomposition](../games/s-z/shogun-showdown.md).
- Novelty: not assessed.

## INF-028 — Visible weighted origin-destination demand

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: before network construction or evaluation, the interface exposes
  which authored entrances require routes to which exits and visibly encodes
  their relative traffic frequencies.
- Includes: selecting a Freeways road sign or building to inspect its required
  destination arrows and their relative sizes.
- Excludes: unpreviewed demand generated during play; destination identity
  inferred only after a vehicle moves; exact future vehicle spawn times.
- Parameters: endpoint classes, direction convention, weight granularity and
  whether reciprocal demand is shown separately.
- Evidence: [Freeways decomposition](../games/a-f/freeways.md).
- Novelty: not assessed.

## INF-029 — Visible exact directional line-sum clue

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: a visible clue identifies one fixed directional line of
  assignable positions and discloses the exact arithmetic sum their completed
  numeric values must equal without disclosing each individual value.
- Includes: a Hexologic edge number and arrow identifying one horizontal or
  diagonal line whose one-to-three-pip cells must add to that number.
- Excludes: an exact count of concealed members of one class in a local
  neighbourhood; ordered run lengths; a fully specified per-position target;
  an inequality or approximate total; score accumulated from past actions.
- Parameters: line orientation, member positions, target range, arrow notation,
  clue visibility and whether every geometric line is clued.
- Evidence: [Hexologic decomposition](../games/g-l/hexologic.md).
- Novelty: not assessed.

## INF-031 — Persistent partitioned hypothesis-match counts

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: after each complete ordered hypothesis, the interface retains
  that proposal with two exact aggregate counts: symbols matched at the same
  position and additional symbols matched only by identity, without revealing
  which positions produced the second count.
- Includes: Mastermind retaining every four-peg guess beside unordered exact-
  position and wrong-position indicator totals.
- Excludes: revealing the target symbols or their positions; one undivided
  similarity score; identifying a specific violated clue; feedback that
  disappears before the next hypothesis can be compared with it.
- Parameters: history depth, count notation, exact / residual labels, indicator
  ordering, accessibility channel and whether zero counts use blanks.
- Evidence: [Mastermind decomposition](../games/m-r/mastermind.md).
- Novelty: not assessed.

## INF-032 — Persistent indirect probe outcome

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: after a probe into a concealed spatial system, the interface
  permanently labels its boundary entry with the exact categorical result and,
  when the probe exits elsewhere, links both boundary positions as one paired
  observation without exposing the internal route.
- Includes: Black Box retaining `H`, `R` or a matching numbered entry / exit
  pair around the arena.
- Excludes: revealing the concealed cells traversed; a local count attached to
  one interior cell; feedback that disappears before the next query; a score
  with no identified probe origin.
- Parameters: outcome vocabulary, pair notation, persistence, accessibility
  channel and whether already used exits may be selected.
- Evidence: [Black Box decomposition](../games/a-f/black-box.md).
- Novelty: not assessed.

## INF-030 — Live exact-subconstraint satisfaction indication

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: before full answer submission, the interface continuously marks
  one declared local constraint as currently satisfied exactly while making no
  claim that its internal assignments are compatible with all other
  constraints or belong to the final solution.
- Includes: Hexologic turning one arrow-line border green when its current pip
  total equals the displayed target even though an intersecting line may force
  those values to be rearranged.
- Excludes: marking a violated clue only after a rejected complete submission;
  revealing corrected values; generic success feedback; highlighting a legal
  action whose local completion predicate is still false.
- Parameters: predicate type, update timing, satisfied-state notation,
  persistence, animation and accessibility channel.
- Evidence: [Hexologic decomposition](../games/g-l/hexologic.md).
- Novelty: not assessed.

## INF-033 — Transient ordered-cue presentation

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: the system exposes a complete target sequence one cue at a time
  in ordinal order, but does not leave a persistent symbolic record of earlier
  cues available during the subsequent reproduction decision.
- Includes: Simon flashing the current light sequence serially before the
  player echoes it from memory; sound may redundantly identify the same pads.
- Excludes: a persistent preview queue; simultaneously visible target symbols;
  a concealed sequence known only through aggregate query feedback; an
  unpreviewed future event.
- Parameters: cue channels, presentation duration, inter-cue interval,
  persistence, replay count and accessibility redundancy.
- Evidence: [Simon decomposition](../games/s-z/simon.md).
- Novelty: not assessed.

## INF-034 — Persistent position-addressed ternary hypothesis feedback

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: after each accepted complete sequence query, the interface
  retains the proposal and labels every guessed position as an exact-position
  match, a duplicate-limited identity match elsewhere, or absent after all
  target occurrences have been consumed.
- Includes: Wordle keeping every guessed word as green, yellow and grey tiles,
  including grey excess copies of a letter that has already received all
  available exact or residual credit.
- Excludes: two aggregate exact / misplaced counts; a transient correctness
  signal; per-position equality only with no present-elsewhere category; full
  target reveal.
- Parameters: category labels, colour-independent accessibility channel,
  history depth, duplicate notation and whether absent and exhausted share one
  visible class.
- Evidence: [Wordle decomposition](../games/s-z/wordle.md).
- Novelty: not assessed.

## INF-035 — Instrument-gated alternate visual layer

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: decision-relevant markings over one persistent mechanism state
  are unavailable in ordinary view and become visible only while an acquired
  inspection instrument is active, without that viewing mode itself changing
  the underlying mechanism.
- Includes: The Room's completed eyepiece revealing the hidden alignment trace
  over the exposed front rings.
- Excludes: an inspectable object merely being offscreen; permanent compartment
  opening; random information generated by inspection; cosmetic colour grading
  with no rule consequence; a preview of future system motion.
- Parameters: required instrument and assembly state, target region, overlay
  persistence, toggle behaviour, simultaneous manipulation and reset scope.
- Evidence: [The Room decomposition](../games/s-z/the-room.md).
- Novelty: not assessed.

## INF-036 — Pictorial requested-item disclosure

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: interacting with one addressed character exposes a persistent or
  repeatable non-verbal depiction of the exact item identity that character
  currently accepts, without revealing the full downstream solution chain.
- Includes: Machinarium's small scrapyard robot showing the high doll in its
  request bubble before the player retrieves and gives that item.
- Excludes: spoken flavour dialogue; a generic interaction icon; a complete
  walkthrough hint; an item–fixture match inferred only from shape; a reward
  shown only after the exchange.
- Parameters: requester, depicted item identity, display duration, repeatability,
  accessibility channel, request-state changes and ambiguity.
- Evidence: [Machinarium decomposition](../games/m-r/machinarium.md).
- Novelty: not assessed.

## INF-037 — Close inspection exposes manipulable held-item subpart

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: opening a dedicated close-up view of one acquired item reveals a
  previously unavailable addressed component whose direct manipulation changes
  that item's later mechanical compatibility.
- Includes: close inspection of The Longest Journey's rubber ducky exposing
  the removable Band-Aid that covers its leak.
- Excludes: enlarging artwork with no new action; viewing an already available
  mechanism from another angle; an inspection instrument revealing a separate
  world overlay; receiving a complete text hint.
- Parameters: item identity, inspection mode, exposed hotspot, manipulation,
  resulting state, persistence and accessibility alternative.
- Evidence: [The Longest Journey decomposition](../games/s-z/the-longest-journey.md).
- Novelty: not assessed.

## INF-038 — Addressed recipient discloses exact multi-item commission

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: after one initiating interaction with an addressed recipient,
  the game explicitly names every distinct item type in the finite set that the
  recipient will accept to produce the declared result.
- Includes: Red Edison responding to Day of the Tentacle's patent application
  by requesting oil, vinegar and gold for the super-battery.
- Excludes: a picture of one requested item; an undisclosed recipe inferred by
  trial and error; vague flavour dialogue; a full walkthrough of how to acquire
  each ingredient; a numeric currency price.
- Parameters: recipient, initiating state, item labels, set cardinality,
  persistence or repeatability, accepted synonyms and accessibility channel.
- Evidence: [Day of the Tentacle decomposition](../games/a-f/day-of-the-tentacle.md).
- Novelty: not assessed.

## INF-039 — Visible typed collection schema and retained slot progress

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: before each contribution, the interface displays the collection's
  eligible item identities, required quantities, quality thresholds, slot quota
  and which requirements have already been persistently filled.
- Includes: Stardew Valley's readable Boiler Room scrolls showing three bar
  slots, four mineral slots and two slots chosen from four monster-drop options,
  together with retained bundle progress.
- Excludes: a character verbally requesting one exact set; a crafting recipe
  with no persistent partial contribution state; acquisition-route guidance;
  an undisclosed target inferred only from rejected items.
- Parameters: collection hierarchy, item labels, quantities, quality markers,
  alternative quota, filled-state marker, remote progress access and
  accessibility representation.
- Evidence: [Stardew Valley decomposition](../games/s-z/stardew-valley.md).
- Novelty: not assessed.

## INF-040 — Visible gate-specific shape roster and arranger occupancy

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: an addressed access barrier displays the exact coloured rigid
  piece identities it still requires, and its arranger exposes the complete
  finite piece inventory, board boundary, current orientations, occupied cells
  and remaining gaps before each placement decision.
- Includes: The Talos Principle's first A1 lock showing its green `L`, `J` and
  `Z` requirements and the 4 × 3 arranger showing every live placement.
- Excludes: a scalar key count with no identities; hidden target geometry;
  acquisition-route hints; a crafting recipe with no addressed spatial board.
- Parameters: roster identity, missing-state marker, board topology, footprint
  preview, occupancy display, invalid-placement feedback and accessibility form.
- Evidence: [The Talos Principle decomposition](../games/s-z/the-talos-principle.md).
- Novelty: not assessed.

## INF-041 — Rotation reveals depth between flattened traversal views

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the animated transition between two settled orthographic views
  temporarily exposes the relative depth and side arrangement that each flat
  endpoint collapses, then presents the new front-layer collision slice as the
  visible basis for the next movement decision.
- Includes: a Fez quarter-turn showing that two apparently aligned platforms
  occupy different world depths before the adjacent settled view exposes a new
  continuation.
- Excludes: free-camera inspection with no rule consequence; a static cutaway;
  hidden-state revelation unrelated to projection; an exact preview of every
  future movement outcome.
- Parameters: transition duration, intermediate layers, occlusion, silhouette,
  depth cues, reduced-motion alternative and settled-state indicator.
- Evidence: [Fez decomposition](../games/a-f/fez.md).
- Novelty: not assessed.

## INF-042 — Live projected path authority is visually disclosed

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the continuously updated screen image itself exposes the
  currently authoritative path joins and occlusions: apparent contact is shown
  as contact, while a discontinuity hidden by nearer geometry is absent from
  the traversal image used for the next decision.
- Includes: Echochrome showing when remote walkway ends line up and when a
  nearer element covers a gap before the Walker reaches that relation.
- Excludes: a hidden numeric topology table; a route forecast drawn ahead of
  an autonomous agent; a four-state transition animation; cosmetic perspective
  whose apparent joins have no rule consequence.
- Parameters: line clarity, depth cues, silhouette contrast, occlusion edge,
  alignment snap, reduced-motion presentation and update latency.
- Evidence: [Echochrome decomposition](../games/a-f/echochrome.md).
- Novelty: not assessed.

## INF-043 — Current reachable destinations are visibly marked

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: the current navigation state visibly distinguishes the nodes or
  surfaces that can accept a movement destination or attachment command, and
  that marking updates whenever local reachability changes.
- Includes: Monument Valley highlighting currently reachable nodes after
  geometry moves; Sekiro turning eligible grappling anchors green.
- Excludes: a complete future-route overlay; decoration with no input meaning;
  hidden reachability discovered only after rejection; showing the current
  avatar location without marking selectable destinations.
- Parameters: marker form, contrast, focus state, path-versus-node scope,
  update latency, invalid-target feedback and reduced-motion presentation.
- Evidence: [Monument Valley decomposition](../games/m-r/monument-valley.md) and
  [Sekiro decomposition](../games/s-z/sekiro-shadows-die-twice.md).
- Novelty: not assessed.

## INF-044 — Live perspective-held physical placement preview

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: before release, the rendered held object continuously shows the
  exact current collision-bounded world position, orientation and scale that
  will become physical if committed, even though its projected screen extent
  remains stable while camera depth changes.
- Includes: Superliminal showing the Induction chess piece grow in world scale
  as it is aimed toward a distant wall and showing its current plate-relative
  pose before it is dropped.
- Excludes: a cursor with no object pose; a numeric size label; an image plane
  that will create different geometry; a route forecast; discovering scale or
  collision only after release.
- Parameters: silhouette, depth cues, contact shadow, target overlap, update
  latency, invalid-placement feedback, rotation preview and accessibility form.
- Evidence: [Superliminal decomposition](../games/s-z/superliminal.md).
- Novelty: not assessed.

## INF-045 — Gravity-frame colour and eligibility encoding

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: the scene continuously uses one stable colour mapping to expose
  the currently selected orthogonal gravity frame, the colour a faced surface
  would acquire as floor, and which coloured portable bodies and fixtures are
  eligible in that frame.
- Includes: Manifold Garden tinting the current floor by gravity direction,
  showing the aimed wall's colour at the crosshair and matching red, blue or
  other cubes and switches to those directional frames.
- Excludes: colour used only for decoration; a hidden gravity vector; a numeric
  direction label with no object eligibility; colour identifying teams or
  score; a portal surface class unrelated to global down.
- Parameters: six-direction palette, current-frame indicator, aimed-surface
  preview, object and fixture marking, colour-blind alternative, contrast and
  transition timing.
- Evidence: [Manifold Garden decomposition](../games/m-r/manifold-garden.md).
- Novelty: not assessed.

## INF-046 — Simultaneous nested-scale correspondence display

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: the current view exposes at least two recognisable nested scale
  instances of one world together, using homologous architecture and object
  silhouettes so the player can identify which locations and bodies share
  authoritative state across scale.
- Includes: Maquette showing the central model inside the normal courtyard and
  distinctive matching buildings, gaps, red block and golden key
  representations at different sizes.
- Excludes: a minimap whose symbols do not physically exist; sequential views
  with no retained parent context; identical decoration without causal linkage;
  a numeric scale label; periodic same-scale copies.
- Parameters: visible recursion depth, landmark distinctiveness, scale ratio,
  occlusion, correspondence highlight, update latency and reduced-detail
  rendering.
- Evidence: [Maquette decomposition](../games/m-r/maquette.md).
- Novelty: not assessed.

## INF-047 — Stable local threshold with concealed remote destination

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the current doorway, window or corridor mouth is visibly stable,
  but the identity of the remote room presently connected beyond it is not
  disclosed as a persistent map relation and must be revealed by a viewpoint
  change or traversal.
- Includes: Antichamber showing the same local `Now You See It` doorway before
  and after the off-screen change while withholding which authored room it now
  reaches until the player returns to inspect or cross it.
- Excludes: a live cross-portal view; a simultaneously visible recursive
  counterpart; a periodic copy whose translation is already legible; a hidden
  random outcome; a locked door whose fixed destination is known.
- Parameters: local threshold cues, destination disclosure moment, map support,
  preview depth, persistence, change feedback and accessibility alternative.
- Evidence: [Antichamber decomposition](../games/a-f/antichamber.md).
- Novelty: not assessed.

## INF-048 — Continuous curvature-rendered distance and direction cues

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the live first-person scene renders landmarks, horizons and
  route directions through the same curved metric that resolves traversal, so
  apparent spacing, angular spread and accumulated orientation continuously
  expose consequences of curvature rather than a hidden graph label.
- Includes: Hyperbolica showing curved horizons, rapidly multiplying visible
  surroundings and route directions that shift while the avatar walks through
  the Maze of Apeirogon.
- Excludes: a flat minimap alone; cosmetic lens distortion over Euclidean
  collision; a live portal endpoint; an off-screen room remap; a static
  diagram of hyperbolic tiling outside play.
- Parameters: projection model, field of view, landmark density, horizon form,
  depth cue, distortion strength, motion smoothing and accessibility overlay.
- Evidence: [Hyperbolica decomposition](../games/g-l/hyperbolica.md).
- Novelty: not assessed.

## INF-049 — Player-centred finite projection of an unbounded tiling

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: play displays a finite projected neighbourhood around the
  player's current cell, shrinking more distant tiles toward the view boundary
  and allowing the view to recenter on the player while the underlying world
  continues beyond the generated radius.
- Includes: HyperRogue's standard Poincare-disc presentation and explicit view
  recentering over a lazily generated hyperbolic cell field.
- Excludes: a finite minimap; continuous first-person curved collision cues; a
  camera zoom over a flat finite board; decorative radial distortion; complete
  disclosure of an unbounded graph.
- Parameters: projection model, generated radius, visible radius, view centre,
  cell scaling, rotation, pan limit, recenter control and edge highlighting.
- Evidence: [HyperRogue decomposition](../games/g-l/hyperrogue.md).
- Novelty: not assessed.

## INF-050 — Complementary role-partitioned rules and live state

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the complete decision procedure is split between human roles:
  one role can inspect the changing live object but lacks the authoritative
  rule reference, while another can inspect that reference but cannot see the
  object's current instance; only communicated descriptions combine them.
- Includes: Keep Talking and Nobody Explodes Defusers seeing bomb modules,
  timer, strikes and casing facts while Experts read the separate Bomb Defusal
  Manual without seeing the bomb.
- Excludes: one player switching between board and help screen; concealed state
  unknown to every role; optional secret information in an adversarial game;
  all collaborators seeing the same interface.
- Parameters: role count, state fields, rule pages, communication channel,
  persistent shared notes and whether any role may change between attempts.
- Evidence: [Keep Talking and Nobody Explodes decomposition](../games/g-l/keep-talking-and-nobody-explodes.md).
- Novelty: not assessed.

## INF-051 — Stable unknown glyph identity across contextual occurrences

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the same visually distinct but initially untranslated glyph
  recurs across world labels, dialogue or instructions with one stable semantic
  identity, letting separate contexts constrain a shared hypothesis.
- Includes: recurring Devotee signs for open, closed and door across the first
  lever, doorway and six-valve instruction in Chants of Sennaar.
- Excludes: a fresh random cipher each occurrence; translated text; ornamental
  marks with no stable meaning; information split between human roles.
- Parameters: glyph inventory, occurrence contexts, visual variants, language,
  morphology and when canonical translation becomes visible.
- Evidence: [Chants of Sennaar decomposition](../games/a-f/chants-of-sennaar.md).
- Novelty: not assessed.

## INF-052 — Persistent provisional glossary with illustrated validation cues

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: a persistent player-facing notebook stores editable hypotheses
  beside discovered glyphs and later presents authored nonverbal illustrations
  that disclose the candidate semantic slots used to verify a bounded group.
- Includes: Chants of Sennaar's first journal page retaining notes and showing
  pictures for opening, closing and a door before the three-glyph match.
- Excludes: an external manual; a second player's private interface; automatic
  translation with no hypothesis state; a static glossary already solved.
- Parameters: retained annotations, illustration set, discovery threshold,
  page grouping, reveal timing, incorrect feedback and solved-state display.
- Evidence: [Chants of Sennaar decomposition](../games/a-f/chants-of-sennaar.md).
- Novelty: not assessed.

## INF-053 — Visible current-day policy with persistent reference detail

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: before timed case processing begins, the interface explicitly
  discloses the current workday's new or repealed rules and keeps an inspectable
  authoritative reference for document requirements and validation details.
- Includes: Papers, Please showing the daily official bulletin alongside the
  rulebook's basic rules, issuing cities and valid document seals.
- Excludes: a second human's private manual; rules inferred only from penalties;
  one static clue sheet that never changes across days; automatic pass/fail
  feedback without the governing reference.
- Parameters: amendment source, persistent reference sections, rule hierarchy,
  bookmark upgrades, setup-time pause and whether old rules remain listed.
- Evidence: [Papers, Please decomposition](../games/m-r/papers-please.md).
- Novelty: not assessed.

## INF-054 — Collectible diegetic manual progressively expands persistent reference

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: individually collected page pairs permanently expand one
  inspectable in-world manual whose authored diagrams, maps and annotations can
  communicate controls or secrets that were mechanically possible beforehand.
- Includes: collecting TUNIC pages 42–43 at the fountain, then reading page 43
  to identify the Holy Cross as directional input and infer a nearby door code.
- Excludes: an editable player glossary; an external second-role manual; a
  tutorial that grants the control it describes; transient pickup flavour text.
- Parameters: page-pair locations, collection prerequisites, page order,
  inspect-anywhere access, zoom, encoded language and knowledge-only secrets.
- Evidence: [TUNIC decomposition](../games/s-z/tunic.md).
- Novelty: not assessed.

## INF-055 — Retained fact is explicitly available after world reset

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: after a world-reset boundary, the interface or authored dialogue
  exposes that one previously acquired operational fact remains available to
  the player even though the source encounter and surrounding world state reset.
- Includes: Outer Wilds continuing to display the launch-code marks and offering
  a reply to Slate that the Hatchling already obtained them from the observatory.
- Excludes: the human player remembering an undisplayed solution; a retained
  inventory object; a complete public action history; a fact reacquired anew.
- Parameters: fact identity, display channel, dialogue acknowledgement, reset
  boundary, persistence duration and accessibility alternative.
- Evidence: [Outer Wilds decomposition](../games/m-r/outer-wilds.md).
- Novelty: not assessed.

## INF-056 — Game-authored clue is visible in an external interface

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: a decision-relevant clue is fully observable in a file, desktop
  layer or mock operating-system surface outside the ordinary game-world view.
- Includes: the intended external clue channel in OneShot and its World Machine
  Edition equivalent.
- Excludes: information hidden in executable code; a normal pause menu; an
  in-world computer terminal rendered inside the same scene.
- Parameters: interface surface, file format, persistence, update signal and
  accessibility equivalent.
- Evidence: [OneShot decomposition](../games/m-r/oneshot.md).
- Novelty: not assessed.

## INF-057 — RCI demand and spatial diagnostic overlays are visible

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the interface exposes current sector demand plus selectable maps
  for coverage, traffic, pollution, desirability and other spatial city conditions.
- Includes: SimCity 4 and Cities: Skylines RCI bars, information views and
  building or location query inspection.
- Excludes: a fully revealed internal demand formula; decorative map colouring;
  post-hoc score only.
- Parameters: demand sectors, overlay layers, spatial resolution, refresh cadence and query detail.
- Evidence: [SimCity 4 Deluxe Edition decomposition](../games/s-z/simcity-4-deluxe-edition.md)
  and [Cities: Skylines decomposition](../games/a-f/cities-skylines.md).
- Additional support: [Cities: Skylines II decomposition](../games/a-f/cities-skylines-ii.md),
  for the residential, commercial, industrial and office demand bars and the
  selectable electricity and water info views the route reads before extending
  supply.
- Novelty: not assessed.

## INF-058 — Itemised managed-domain budget ledger is visible

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the interface itemises recurring income, expenditure and the
  managed treasury or stockpile balance before the player commits further
  construction or fiscal changes.
- Includes: SimCity 4 and Cities: Skylines economy, budget and tax panels;
  RollerCoaster Tycoon Deluxe monthly income/expenditure, cash-minus-loan,
  Park Value, weekly profit and ride-level financial reports.
- Excludes: one undifferentiated currency total; hidden future random expenses;
  private household accounts outside the managed domain.
- Parameters: managed domain, categories, period, projected versus realised
  totals, taxes or prices, debt and deal terms.
- Evidence: [SimCity 4 Deluxe Edition decomposition](../games/s-z/simcity-4-deluxe-edition.md)
  and [Cities: Skylines decomposition](../games/a-f/cities-skylines.md).
- Additional support: [RollerCoaster Tycoon Deluxe decomposition](../games/m-r/rollercoaster-tycoon-deluxe.md).
- Novelty: carrier wording generalised by
  [`TAXONOMY_CHANGE_078`](../../research/taxonomy-changes/TAXONOMY_CHANGE_078.md).

## INF-059 — Recipe and technology dependency reference is visible

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the interface exposes known production recipes and the reachable
  technology prerequisite graph, including required inputs, products and
  unlock relationships, before the player commits the next factory expansion.
- Includes: Factorio recipe tooltips, crafting menus and technology screen with
  science-pack costs, prerequisites and unlock effects.
- Excludes: a hidden recipe inferred only by experiment; one current inventory
  count; a static external manual with no in-game reference.
- Parameters: known recipe set, ingredient quantities, machine category,
  technology prerequisites, science costs, queue state and search filters.
- Evidence: [Factorio decomposition](../games/a-f/factorio.md) and
  [Age of Empires II: Definitive Edition decomposition](../games/a-f/age-of-empires-ii-definitive-edition.md).
- Novelty: not assessed.

## INF-060 — Live factory-network diagnostics are visible

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: inspectable panels and overlays expose current production flow,
  network satisfaction and spatial externalities so the player can locate a
  running factory's bottleneck or risk without seeing every future event.
- Includes: Factorio production and consumption statistics, electric-network
  satisfaction, logistic-network contents, train state, machine status icons
  and the pollution map overlay.
- Excludes: the recipe dependency reference itself; a post-level score only;
  full disclosure of future enemy attack timing or unexplored terrain.
- Parameters: metric, interval, network scope, spatial layer, update cadence,
  historical window, status icon and aggregation.
- Evidence: [Factorio decomposition](../games/a-f/factorio.md).
- Novelty: not assessed.

## INF-061 — Category-and-magnitude hostile intent preview

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: before the player commits a combat phase, each hostile actor
  discloses its next action category and any declared attack magnitude while
  some buff, debuff or special-effect details may remain categorical.
- Includes: Slay the Spire intent icons showing attack damage and whether an
  enemy plans to attack, defend, buff, debuff, sleep or use an unknown action.
- Excludes: an exact spatial target-and-effect preview; no forecast of the next
  hostile action; a probability distribution over uncommitted actions.
- Parameters: category vocabulary, damage count, multi-hit display, hidden
  special details and intent-suppression effects.
- Evidence: [Slay the Spire decomposition](../games/s-z/slay-the-spire.md).
- Novelty: not assessed.

## INF-062 — Revealed branching route categories and connections

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the player can inspect the current act's directed route,
  successor connections and node categories before choosing the next node,
  while encounter-specific contents may remain unknown.
- Includes: Slay the Spire maps exposing combat, elite, unknown, rest, shop,
  treasure and boss icons plus their connecting paths.
- Excludes: a hidden map revealed only after travel; exact contents of an
  unknown event; a route authored directly by the player.
- Parameters: visible horizon, node categories, boss disclosure, connection
  graph and hidden encounter identity.
- Evidence: [Slay the Spire decomposition](../games/s-z/slay-the-spire.md).
- Novelty: not assessed.

## INF-063 — Visible exact delivery shape, quota and progression reward

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the progression interface discloses the exact structured shape
  currently accepted, the remaining delivery quantity and the mechanics or
  resources awarded when that quota completes.
- Includes: shapez 2 milestone diagrams, live Vortex progress and listed
  machine, floor, platform, blueprint-point or research-point rewards.
- Excludes: the full hidden algorithm of later random Operator shapes; a recipe
  list with no current quota; a receiver whose required object must be inferred.
- Parameters: shape code or diagram, delivered count, target quantity, reward
  list, locked-successor visibility and difficulty scaling.
- Evidence: [shapez 2 decomposition](../games/s-z/shapez-2.md).
- Novelty: not assessed.

## INF-064 — Visible season, hostility and mystery activation forecast

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the interface exposes the current and next ordered weather phase,
  the settlement's hostility tier and which declared phase effects are active or
  will activate at the current tier.
- Includes: Against the Storm's season timeline, Hostility meter and forest
  mystery thresholds.
- Excludes: hidden weather; an unlabeled difficulty number; exact future random
  offers.
- Parameters: phase horizon, time remaining, hostility sources, tier thresholds
  and mystery descriptions.
- Evidence: [Against the Storm decomposition](../games/a-f/against-the-storm.md).
- Novelty: not assessed.

## INF-065 — Visible population-group resolve trajectory and need state

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: for each population group the interface exposes current Resolve,
  its direction of change, threshold relations and the satisfied or unsatisfied
  contributors that explain the value.
- Includes: Against the Storm species portraits and need panels.
- Excludes: one opaque happiness icon; exact hidden future newcomers; individual
  cosmetic mood animation.
- Parameters: group, value, trend, departure threshold, reputation threshold,
  needs and modifiers.
- Evidence: [Against the Storm decomposition](../games/a-f/against-the-storm.md).
- Novelty: not assessed.

## INF-066 — Visible paired reputation and impatience progress

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the interface simultaneously exposes the settlement success track
  and opposed failure track, their terminal thresholds and current progress.
- Includes: Against the Storm Reputation and Queen's Impatience bars.
- Excludes: one hidden failure timer; a final score shown only after play; two
  unrelated currencies.
- Parameters: current values, maxima, passive rate, milestone markers and active
  modifiers.
- Evidence: [Against the Storm decomposition](../games/a-f/against-the-storm.md).
- Novelty: not assessed.

## INF-067 — Visible task requirements, deadline and rewards

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: before or during commitment, the interface discloses a task's
  required state or payment, remaining time where applicable, promised reward
  and declared failure or threat consequence.
- Includes: Against the Storm Orders and Glade Event resolution panels; The
  Sims 4 scenario stage checklist and declared branch rewards.
- Excludes: hidden quest requirements; a generic recipe with no task reward; a
  surprise failure effect disclosed only after expiry.
- Parameters: requirements, alternatives, deadline, progress, reward and threat.
- Evidence: [Against the Storm decomposition](../games/a-f/against-the-storm.md)
  and [The Sims 4 decomposition](../games/s-z/the-sims-4.md).
- Additional support: [The Long Dark decomposition](../games/s-z/the-long-dark.md),
  for the ordered `Hopeless Rescue` objectives, remaining allowance, completion
  badge and declared failure boundary.
- Novelty: not assessed.

## INF-068 — Visible world-map range, biome and modifier state

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: before embarking, the persistent map exposes which tiles are
  reachable and the known biome, difficulty or modifier properties attached to
  candidate destinations.
- Includes: the Against the Storm world-map embarkation preview.
- Excludes: concealed settlement glade contents; an unrestricted level-select
  list; a destination whose rules appear only after starting the run.
- Parameters: origin, range, biome, difficulty, map modifier, reward and cycle.
- Evidence: [Against the Storm decomposition](../games/a-f/against-the-storm.md).
- Novelty: not assessed.

## INF-069 — Material and infrastructure overlays are visible

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: selectable spatial overlays expose elements, oxygen, temperature,
  germs, rooms, power, plumbing, ventilation, shipping and automation.
- Includes: Oxygen Not Included overlays and inspectable cell values.
- Excludes: unexplored contents; one nonspatial tooltip; future random offers.
- Parameters: layer, legend, resolution, topology, colouring, cadence and detail.
- Evidence: [Oxygen Not Included decomposition](../games/m-r/oxygen-not-included.md).
- Novelty: not assessed.

## INF-070 — Agent needs, errands and stress causes are visible

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the interface exposes each agent's needs, traits, skills, morale,
  stress modifiers, schedule and ranked eligible errands.
- Includes: Oxygen Not Included Duplicant details and building Errands tabs.
- Excludes: hidden final tie-break logic; aggregate totals only; cosmetic animation.
- Parameters: agent, need, trait, skill, morale, stress, schedule, errand and eligibility reason.
- Evidence: [Oxygen Not Included decomposition](../games/m-r/oxygen-not-included.md).
- Novelty: not assessed.

## INF-071 — Colony production and survival reports are visible

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: current and historical panels expose colony-wide oxygen, food,
  power, material, labour and population changes plus actionable shortage warnings.
- Includes: Oxygen Not Included cycle reports, resource lists, diagnostics and notifications.
- Excludes: exact future outcomes; a single score; hidden asteroid resources.
- Parameters: metric, cycle, production, consumption, reserve, warning, population and labour.
- Evidence: [Oxygen Not Included decomposition](../games/m-r/oxygen-not-included.md).
- Novelty: not assessed.

## INF-072 — Autonomous-person profile exposes activity, needs and thoughts

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the interface exposes one autonomous person's current activity,
  relevant capabilities or preferences, bodily or social needs, recent
  thoughts and mood or stress state for causal inspection.
- Includes: Dwarf Fortress creature, labour, thoughts and preferences panels;
  The Sims 4 active-Sim needs, skills, work and relationship panels;
  RollerCoaster Tycoon Deluxe guest activity, spending, carried items,
  happiness, nausea, intensity preference and recent thoughts.
- Excludes: hidden future events; one aggregate settlement or park happiness
  number; anonymous movement with no inspectable personal state.
- Parameters: person, activity, capabilities or preferences, work details,
  needs, thoughts, memories, relationships, mood or stress and health.
- Evidence: [Dwarf Fortress decomposition](../games/a-f/dwarf-fortress.md) and
  [The Sims 4 decomposition](../games/s-z/the-sims-4.md).
- Additional support: [RollerCoaster Tycoon Deluxe decomposition](../games/m-r/rollercoaster-tycoon-deluxe.md).
- Novelty: resident-only wording generalised by
  [`TAXONOMY_CHANGE_078`](../../research/taxonomy-changes/TAXONOMY_CHANGE_078.md).

## INF-073 — Carried hotbar and active equipment state are visible

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the interface exposes carried quick slots, their stack contents
  and the currently active hand or equipped item before a local world action.
- Includes: Minecraft Survival hotbar and selected held item; Counter-Strike 2
  carried weapon/utility icons, active item and ammunition state; Cyberpunk
  2077 weapon slots, active weapon and ammunition HUD; Hollow Knight: Silksong
  equipped Crest, Tool slots and Tool charge state; Helldivers 2 current
  firearm, magazine/reserve ammunition, grenade and support-weapon state;
  Rainbow Six Siege operator weapons, gadgets, ammunition and charges.
- Excludes: a complete future terrain map; a hidden recipe discovered only by
  external knowledge; a colony-wide production report.
- Parameters: slots, stacks, selected item, hand and equipment state.
- Evidence: [Minecraft decomposition](../games/m-r/minecraft.md) and
  [Counter-Strike 2 decomposition](../games/a-f/counter-strike-2.md), and
  [Cyberpunk 2077 decomposition](../games/a-f/cyberpunk-2077.md), and
  [Hollow Knight: Silksong decomposition](../games/g-l/hollow-knight-silksong.md), and
  [Helldivers 2 decomposition](../games/g-l/helldivers-2.md),
  [Pokémon Legends: Z-A decomposition](../games/m-r/pokemon-legends-z-a.md) and
  [Rainbow Six Siege decomposition](../games/s-z/tom-clancys-rainbow-six-siege.md).
- Evidence: [Terraria decomposition](../games/s-z/terraria.md).
- Additional support: [Don't Starve Together decomposition](../games/a-f/dont-starve-together.md),
  for visible carried stacks and equipped hand/body items.
- Additional support: [The Binding of Isaac: Rebirth decomposition](../games/s-z/the-binding-of-isaac-rebirth.md),
  for the visible active, trinket and pocket slots plus pickup counters.
- Additional support: [Team Fortress 2 decomposition](../games/s-z/team-fortress-2.md),
  for visible active stock weapon and ammunition state.
- Additional support: [Left 4 Dead 2 decomposition](../games/g-l/left-4-dead-2.md),
  for current weapon, ammunition and typed support-item slots.
- Additional support: [Destiny 2 decomposition](../games/a-f/destiny-2.md),
  for current weapon-slot and ammunition HUD state.
- Additional support: [Resident Evil 2 (2019 remake) decomposition](../games/m-r/resident-evil-2-2019.md),
  for shortcut slots plus loaded and remaining ammunition shown while the weapon is readied.
- Additional support: [Resident Evil: Director's Cut decomposition](../games/m-r/resident-evil-directors-cut.md),
  for status-screen disclosure of the equipped handgun and carried ammunition state before the next room action.
- Additional support: [The Long Dark decomposition](../games/s-z/the-long-dark.md),
  for the selected carried survival item and loaded Distress Pistol state.
- Additional support: [Halo 3 decomposition](../games/g-l/halo-3.md),
  for active and reserve weapons, ammunition or charge and grenade state.
- Additional support: [Super Metroid decomposition](../games/s-z/super-metroid.md),
  for selected special equipment and its current missile reserve on the HUD.
- Novelty: not assessed.

## INF-074 — Crafting grid and available recipe state are visible

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: the crafting interface exposes the current grid contents,
  matching output and recipe-book entries currently available to the player.
- Includes: Minecraft 2×2 and 3×3 crafting UI with recipe-book autofill.
- Excludes: hidden future recipes; an autonomous machine production report.
- Parameters: grid, cells, ingredients, matched output and recipe-book entries.
- Evidence: [Minecraft decomposition](../games/m-r/minecraft.md).
- Novelty: not assessed.

## INF-075 — Personal survival capacity and equipment wear are visible

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the interface exposes the avatar's current survival meters,
  temporary capacity modifiers and carried tool wear sufficiently to judge
  food, combat, recovery and replacement needs.
- Includes: Minecraft hearts, hunger drumsticks, armour icons and durability
  bars; Rainbow Six Siege health and eligible injured state.
- Includes: Valheim health, stamina, active-food durations/status and durability.
- Excludes: exact hidden saturation; a predicted future damage outcome; remote
  world state unrelated to personal survival.
- Parameters: health, hunger, stamina, active food, duration, armour, breath,
  recovery status and durability.
- Evidence: [Minecraft decomposition](../games/m-r/minecraft.md) and
  [Rainbow Six Siege decomposition](../games/s-z/tom-clancys-rainbow-six-siege.md), and
  [Don't Starve Together decomposition](../games/a-f/dont-starve-together.md),
  and [Valheim decomposition](../games/s-z/valheim.md).
- Additional support: [Resident Evil 2 (2019 remake) decomposition](../games/m-r/resident-evil-2-2019.md),
  for the Fine, Caution and Danger condition and damage effect.
- Additional support: [Resident Evil: Director's Cut decomposition](../games/m-r/resident-evil-directors-cut.md),
  for Chris's visible condition monitor and lethal-state warning.
- Additional support: [The Long Dark decomposition](../games/s-z/the-long-dark.md),
  for Warmth, Fatigue, Thirst, Hunger, Condition, Stamina and relevant clothing
  state during the timed Challenge route.
- Additional support: [DEATH STRANDING DIRECTOR'S CUT decomposition](../games/a-f/death-stranding-directors-cut.md),
  for visible stamina during the opening body-load traversal.
- Novelty: not assessed.

## INF-076 — A thrown locator reveals a temporary bearing to a hidden target

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: the visible flight path of a used locator discloses a temporary
  directional observation toward an otherwise undisclosed world target.
- Includes: watching a thrown Minecraft Eye of Ender point toward a stronghold.
- Excludes: revealing exact coordinates; a permanently updating compass needle.
- Parameters: bearing, flight path, observation position and target class.
- Evidence: [Minecraft decomposition](../games/m-r/minecraft.md).
- Novelty: not assessed.

## INF-077 — Weather timeline and city heat conditions are visible

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: the interface exposes current and forecast ambient temperature
  changes together with inspectable heat categories for occupied buildings.
- Includes: Frostpunk weather bar, temperature forecast and heat view.
- Excludes: exact future dilemmas; material-cell thermal simulation; decorative snow.
- Parameters: current temperature, forecast horizon, change time, building heat,
  category legend and illness risk.
- Evidence: [Frostpunk decomposition](../games/a-f/frostpunk.md).
- Novelty: not assessed.

## INF-078 — Hope, Discontent and promise causes are visible

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: the interface exposes current Hope and Discontent, active positive
  and negative causes, crisis thresholds and timed promises affecting them.
- Includes: Frostpunk welfare bars, modifier lists and promise deadlines.
- Excludes: one citizen mood; hidden event outcomes; resource stockpiles.
- Parameters: track values, trends, modifiers, promise, deadline, recovery target
  and purpose replacement.
- Evidence: [Frostpunk decomposition](../games/a-f/frostpunk.md).
- Novelty: not assessed.

## INF-079 — Generator fuel, heat-output and stress diagnostics are visible

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: generator controls expose current coal reserve and consumption,
  configured power and range, heat output, Overdrive state and stress.
- Includes: Frostpunk generator panel and coal-depletion forecast.
- Excludes: city-wide production history; hidden explosion chance; technology tree.
- Parameters: coal, burn rate, remaining duration, power, range, overdrive,
  stress and warning threshold.
- Evidence: [Frostpunk decomposition](../games/a-f/frostpunk.md).
- Novelty: not assessed.

## INF-080 — Frostland destinations, travel time and scout cargo are visible

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the world map exposes revealed scout destinations and route-time
  estimates together with each team's current position, status and carried
  resources or escorted people.
- Includes: A New Home Frostland map and approaching Great Storm coverage.
- Excludes: concealed successors before exploration; street routing; fast travel.
- Parameters: node, route, estimated time, team, cargo, survivors, storm reach
  and destination state.
- Evidence: [Frostpunk decomposition](../games/a-f/frostpunk.md).
- Novelty: not assessed.

## INF-081 — Star map, planet properties and known resource reserves are visible

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the navigation views expose discovered stars, planetary orbits,
  distances and available planet properties, with researched exploration levels
  revealing aggregate resource types and remaining reserves.
- Includes: Dyson Sphere Program planet view, star map and universe-exploration
  resource summaries.
- Excludes: deposits on unscanned distant systems; factory production rates;
  hidden future Dark Fog wave composition.
- Parameters: exploration level, star, planet, orbit, distance, resource type,
  reserve estimate, rare resource and hostile presence.
- Evidence: [Dyson Sphere Program decomposition](../games/a-f/dyson-sphere-program.md).
- Novelty: not assessed.

## INF-082 — Mecha energy, flight state and navigation target are visible

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the interface exposes current mecha-core energy and fuel state,
  active movement regime, speed, target bearing and distance needed to judge a
  surface, sail or warp journey.
- Includes: Dyson Sphere Program Icarus core meter and space-navigation HUD.
- Excludes: factory electric-grid satisfaction; autonomous vessel cargo;
  exact undiscovered planet resources.
- Parameters: core energy, generation, fuel, mode, speed, heading, target,
  distance and estimated approach.
- Evidence: [Dyson Sphere Program decomposition](../games/a-f/dyson-sphere-program.md).
- Novelty: not assessed.

## INF-083 — Logistics-station slot and carrier state are visible

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: each logistics station exposes its typed stored quantities, local
  and remote slot modes, carrier inventory, charge, range, load thresholds,
  warper policy and active trips.
- Includes: Dyson Sphere Program Planetary and Interstellar Logistics Station panels.
- Excludes: belt-lane contents outside the station; hidden route-selection
  internals; general recipe reference.
- Parameters: item slot, storage, supply, demand, current quantity, carrier,
  energy, range, minimum load, warper and trip.
- Evidence: [Dyson Sphere Program decomposition](../games/a-f/dyson-sphere-program.md).
- Novelty: not assessed.

## INF-084 — Dyson plan, construction progress and stellar output are visible

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the orbital editor and receiver panels expose configured orbits
  and sphere layers, planned and built elements, sail and rocket progress,
  generated output, receiver demand and continuous-receiving state.
- Includes: Dyson Sphere Program Dyson editor, swarm/sphere statistics and Ray
  Receiver diagnostics.
- Excludes: ordinary factory production statistics; unexplored star resources;
  future shell elements not placed by the player.
- Parameters: orbit, layer, node, frame, shell cell, sail count, rocket points,
  generation, requested power, efficiency and receiver mode.
- Evidence: [Dyson Sphere Program decomposition](../games/a-f/dyson-sphere-program.md).
- Novelty: not assessed.

## INF-085 — Dark Fog threat, wave and combat state are visible

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: combat overlays expose known hostile bases and units, current
  planetary threat progress, incoming-wave warning and the mecha or defence
  state needed to respond.
- Includes: default Regular Dark Fog threat meter, attack warning and targeting.
- Excludes: exact future wave composition before dispatch; ordinary factory
  bottlenecks; a hidden random event.
- Parameters: base, level, threat value, threshold, wave warning, target,
  hostile health, ammunition, shield and defence coverage.
- Evidence: [Dyson Sphere Program decomposition](../games/a-f/dyson-sphere-program.md).
- Novelty: not assessed.

## INF-086 — Settlement population, needs and workforce state are visible

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: inspectable settlement panels expose population groups, housing, needs or well-being, employment, vacancies and available versus required workforce.
- Includes: Anno 1800 residence/workforce, Timberborn population/well-being, Workers & Resources citizen/labour and Surviving Mars population/work-allocation interfaces.
- Excludes: hidden future births or exact death time; production throughput without population state; aggregate score alone.
- Parameters: species or citizen groups, age, tier, housing, need schema, education, health, happiness, loyalty and work priorities.
- Evidence: [Anno 1800 decomposition](../games/a-f/anno-1800.md), [Timberborn decomposition](../games/s-z/timberborn.md), [Workers & Resources: Soviet Republic decomposition](../games/s-z/workers-resources-soviet-republic.md) and [Surviving Mars: Relaunched decomposition](../games/s-z/surviving-mars.md).
- Novelty: not assessed.

## INF-087 — Island storage and trade-route orders are visible

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: storage and route interfaces expose island quantities, capacity,
  selected ports, assigned ships, cargo-slot orders and current route progress.
- Includes: Anno 1800 trading post, warehouse and trade-route panels.
- Excludes: local cart paths in transit; unknown competitor cargo; recipe reference.
- Parameters: island, good, quantity, capacity, port, ship, slot, order,
  minimum stock and route state.
- Evidence: [Anno 1800 decomposition](../games/a-f/anno-1800.md).
- Novelty: not assessed.

## INF-088 — Influence allocation and current newspaper issue are visible

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the interface exposes available and committed influence by
  category together with the current newspaper's articles, replacement costs
  and published effects.
- Includes: Anno 1800 influence overview and newspaper editor.
- Excludes: hidden future issue composition; treasury budget; AI reputation.
- Parameters: influence pool, category, investment, article, propaganda,
  replacement cost, effect and publication time.
- Evidence: [Anno 1800 decomposition](../games/a-f/anno-1800.md).
- Novelty: not assessed.

## INF-089 — Regional map exposes islands, fertilities and expedition state

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: discovered regional and expedition views expose island locations,
  known crop fertilities and deposits, ship positions, voyage morale and the
  declared skill or supply consequences of current expedition choices.
- Includes: Anno 1800 Old/New World maps and discovery expedition interface.
- Excludes: undiscovered island details; exact hidden event rolls; local factory flow.
- Parameters: region, island, fertility, deposit, ship, destination, morale,
  skill chance, cargo and event option.
- Evidence: [Anno 1800 decomposition](../games/a-f/anno-1800.md).
- Novelty: not assessed.

## INF-090 — World’s Fair phase and exhibition supply are visible

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the monument interface exposes its current construction or
  exhibition phase, required and delivered inputs, remaining preparation time,
  achieved supply tier and associated reward pool.
- Includes: Anno 1800 World’s Fair construction and exhibition panels.
- Excludes: hidden reward identity where only a pool is declared; ordinary
  factory diagnostics; campaign quest text outside the monument.
- Parameters: phase, input, delivered quantity, workforce, electricity, time,
  supply tier, exhibition and reward pool.
- Evidence: [Anno 1800 decomposition](../games/a-f/anno-1800.md).
- Novelty: not assessed.

## INF-091 — Current and forecast weather event is visible

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the interface identifies the current weather, remaining duration
  and next forecast when advance warning is available.
- Includes: Timberborn temperate, drought and badtide displays.
- Excludes: hidden future draws; cosmetic seasons.
- Parameters: event, remaining days, forecast, lead time and cycle.
- Evidence: [Timberborn decomposition](../games/s-z/timberborn.md).
- Novelty: not assessed.

## INF-092 — Water, irrigation and contamination state is inspectable

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: rendering, overlays and panels expose depth, flow, contamination
  and affected irrigation or plant state at relevant locations.
- Includes: Timberborn water, badwater, pumps, barriers and soil effects.
- Excludes: exact future source output; world visibility alone.
- Parameters: location, depth, flow, contamination, irrigation and opening.
- Evidence: [Timberborn decomposition](../games/s-z/timberborn.md).
- Novelty: not assessed.

## INF-093 — Population, well-being and work allocation are visible

- Lifecycle: `Merged`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: historical game-specific duplicate now represented by the
  parameterised active boundary `INF-086`.
- Includes: historical references that used `INF-093` before registry
  normalisation 006.
- Excludes: new game signatures; use `INF-086` with the scoped parameters and
  any retained companion Constraints or System behaviours.
- Parameters: none; preserved as a lifecycle alias.
- Evidence: [Timberborn decomposition](../games/s-z/timberborn.md).
- Merged into: `INF-086` by
  [`TAXONOMY_CHANGE_014`](../../research/taxonomy-changes/TAXONOMY_CHANGE_014.md).

## INF-094 — Goods, production and power-network state are visible

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: panels disclose stored goods, recipe flow, operating reason and
  connected power generation, demand, satisfaction and storage.
- Includes: Timberborn stock, workplace and mechanical-power interfaces.
- Excludes: recipe reference without live quantities; future wind output.
- Parameters: goods, capacity, inputs, outputs, status, generation and demand.
- Evidence: [Timberborn decomposition](../games/s-z/timberborn.md).
- Novelty: not assessed.

## INF-095 — Automation measurement, logic and target state are visible

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: automation interfaces disclose connections, sampled values,
  thresholds or logic, current signals and resulting target state.
- Includes: Timberborn 1.0 sensors, relays, logic and controlled buildings.
- Excludes: hidden scripts; manual state without a signal rule.
- Parameters: connection, measurement, predicate, signal and target response.
- Evidence: [Timberborn decomposition](../games/s-z/timberborn.md).
- Novelty: not assessed.

## INF-096 — Wonder unlock, build and activation progress is visible

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: the interface itemises the wonder's science gate, build
  deliveries and progress, then separate activation supplies and eligibility.
- Includes: Timberborn Earth Recultivator panel and first-launch state.
- Excludes: one-step ordinary building costs; hidden victory rules.
- Parameters: science, delivered goods, progress, launch supply and win state.
- Evidence: [Timberborn decomposition](../games/s-z/timberborn.md).
- Novelty: not assessed.

## INF-097 — Citizen welfare, education and labour state is visible

- Lifecycle: `Merged`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: historical game-specific duplicate now represented by the
  parameterised active boundary `INF-086`.
- Includes: historical references that used `INF-097` before registry
  normalisation 006.
- Excludes: new game signatures; use `INF-086` with the scoped parameters and
  any retained companion Constraints or System behaviours.
- Parameters: none; preserved as a lifecycle alias.
- Evidence: [Workers & Resources: Soviet Republic decomposition](../games/s-z/workers-resources-soviet-republic.md).
- Merged into: `INF-086` by
  [`TAXONOMY_CHANGE_014`](../../research/taxonomy-changes/TAXONOMY_CHANGE_014.md).

## INF-098 — Lines, passengers, vehicles and traffic state are visible

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: transport panels expose stops, line orders, waiting passengers,
  vehicle cargo, fuel, delay, reachability and network traffic.
- Includes: Workers & Resources passenger and cargo transport.
- Excludes: hidden future pathfinder choices.
- Parameters: line, stop, passenger, vehicle, cargo, fuel, route and delay.
- Evidence: [Workers & Resources: Soviet Republic decomposition](../games/s-z/workers-resources-soviet-republic.md).
- Novelty: not assessed.

## INF-099 — Construction assignments and phase progress are visible

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: site and office panels itemise sources, vehicles, current phase,
  required and delivered materials, workers, mechanisms and work progress.
- Includes: Workers & Resources realistic construction UI.
- Excludes: hidden delivery timing or instant-money completion.
- Parameters: site, source, phase, material, vehicle, labour and progress.
- Evidence: [Workers & Resources: Soviet Republic decomposition](../games/s-z/workers-resources-soviet-republic.md).
- Novelty: not assessed.

## INF-100 — Dual-currency trade prices and flows are visible

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: economy panels expose ruble and dollar balances, current import
  and export prices, traded volumes and income or expenditure by commodity.
- Includes: Workers & Resources economy and customs panels.
- Excludes: fully disclosed future world-event price changes.
- Parameters: bloc, currency, resource, direction, price, volume and period.
- Evidence: [Workers & Resources: Soviet Republic decomposition](../games/s-z/workers-resources-soviet-republic.md).
- Novelty: not assessed.

## INF-101 — Utility and environmental diagnostics are visible

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: overlays expose connected power, heat, water and sewage capacity
  plus temperature, pollution, fire, waste and maintenance state.
- Includes: Workers & Resources infrastructure overlays.
- Excludes: exact future failures or cosmetic network rendering only.
- Parameters: network, supply, demand, loss, environment, risk and outage.
- Evidence: [Workers & Resources: Soviet Republic decomposition](../games/s-z/workers-resources-soviet-republic.md).
- Novelty: not assessed.

## INF-102 — Research and nuclear-chain state are visible

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: panels expose research prerequisites and workdays, uranium and
  fuel inventories, reactor staff, cooling, output, waste and radiation.
- Includes: Workers & Resources nuclear route.
- Excludes: hidden future accidents.
- Parameters: project, progress, material, staff, cooling, output, waste and risk.
- Evidence: [Workers & Resources: Soviet Republic decomposition](../games/s-z/workers-resources-soviet-republic.md).
- Novelty: not assessed.

## INF-103 — Campaign branches and measured objectives are visible

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: campaign UI exposes active and completed branches, required
  construction or traded totals and the next available task.
- Includes: both released Workers & Resources base campaigns.
- Excludes: platform achievements or hidden sandbox goals.
- Parameters: campaign, branch, objective, target, current total and completion.
- Evidence: [Workers & Resources: Soviet Republic decomposition](../games/s-z/workers-resources-soviet-republic.md).
- Novelty: not assessed.

## INF-104 — Terrain layers, designations and mine remit are visible

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: overlays expose typed underground material, surface height,
  mining and dumping target volumes and the selected tower's operating area.
- Includes: Captain of Industry resource layers, terrain grid, designations and
  Mine Control Tower area display.
- Excludes: concealed ore with no preview; factory recipe diagnostics; a
  decorative contour map.
- Parameters: material, depth, height, designation type, target plane, tower
  area, vehicle access and mixed-load warning.
- Evidence: [Captain of Industry decomposition](../games/a-f/captain-of-industry.md).
- Novelty: not assessed.

## INF-105 — Vehicle jobs, buffers and reachability state are visible

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: entity and vehicle panels expose current cargo requests,
  reservations, import or export rules, assignments, fuel, maintenance and
  unreachable destinations.
- Includes: Captain of Industry truck statistics, storage sliders, dedicated
  routes, mine assignments and navigation warnings.
- Excludes: hidden future jobs; belt-only throughput graphs; world-map trade offers.
- Parameters: vehicle, product, source, destination, request, reservation,
  buffer, assignment, route, fuel and maintenance.
- Evidence: [Captain of Industry decomposition](../games/a-f/captain-of-industry.md).
- Novelty: not assessed.

## INF-106 — Settlement, Unity, health and maintenance state are visible

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: population and statistics panels expose housing, workers, food
  and service fulfilment, Unity income and expenses, health modifiers,
  pollution and maintenance supply and demand.
- Includes: Captain of Industry population overview and product statistics.
- Excludes: individual citizen routes; undisclosed future disease timing;
  municipal cash in multiple currencies.
- Parameters: population, jobs, housing, service, Unity, health, pollution,
  maintenance tier, production and consumption.
- Evidence: [Captain of Industry decomposition](../games/a-f/captain-of-industry.md).
- Novelty: not assessed.

## INF-107 — World nodes, ship state and island offers are visible

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the world map and trading interface expose revealed routes,
  destinations, enemy strength, ship fuel and damage, outpost requirements,
  village reputation and available exchange terms.
- Includes: Captain of Industry exploration map, villages, contracts and resource nodes.
- Excludes: unrevealed node identity; home-island terrain layers; train schedules.
- Parameters: node, edge, distance, fuel, strength, damage, loot, reputation,
  offer ratio, Unity cost and cargo capacity.
- Evidence: [Captain of Industry decomposition](../games/a-f/captain-of-industry.md).
- Novelty: not assessed.

## INF-108 — Rocket assembly, transfer and launch readiness are visible

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: assembly and launch panels expose rocket component progress,
  transporter or pad availability, connected propellant and water and the
  first-launch state.
- Includes: Captain of Industry Rocket Assembly Depot and Rocket Launch Pad.
- Excludes: hidden launch prerequisites; space-station upkeep after the first
  launch; generic factory output statistics alone.
- Parameters: rocket tier, components, assembly progress, transporter route,
  pad, fuel, oxidiser, water, payload and launch status.
- Evidence: [Captain of Industry decomposition](../games/a-f/captain-of-industry.md).
- Novelty: not assessed.

## INF-109 — Mars sectors, deposits and anomaly progress are visible

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: map overlays expose sector scan progress and revealed deposits,
  anomalies, entrances and explorer-analysis state while unrevealed contents
  remain unknown.
- Includes: Surviving Mars: Relaunched surface scanning and RC Explorer pins.
- Excludes: exact contents of unscanned sectors; production diagnostics;
  cosmetic terrain rendering.
- Parameters: sector, progress, queue, deposit, grade, anomaly, explorer and
  analysis status.
- Evidence: [Surviving Mars: Relaunched decomposition](../games/s-z/surviving-mars.md).
- Novelty: not assessed.

## INF-110 — Drone command areas, errands and resource access are visible

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: commander and work panels expose service-area coverage, assigned
  drones, pending construction, hauling or repair errands, required resources
  and unreachable or unpowered causes.
- Includes: Surviving Mars: Relaunched rockets, RC Commanders, Drone Hubs and
  controlled drones.
- Excludes: hidden pathfinder tie-breaks; human workplace staffing; shuttle-only
  global transport.
- Parameters: commander, range, drone, errand, priority, resource, route,
  power and failure reason.
- Evidence: [Surviving Mars: Relaunched decomposition](../games/s-z/surviving-mars.md).
- Novelty: not assessed.

## INF-111 — Mars rocket manifests, flights and landing state are visible

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: resupply and rocket panels expose cargo or passenger capacity,
  selected manifest, fuel, origin, destination, travel progress, landing-site
  compatibility, automation and expected export or project result.
- Includes: Surviving Mars: Relaunched patch 1.0.7 universal rockets.
- Excludes: hidden future expedition events; local shuttle routes; generic
  inventory lists with no flight state.
- Parameters: rocket, capacity, manifest, passenger, fuel, route, travel time,
  landing site, automation, export and reward.
- Evidence: [Surviving Mars: Relaunched decomposition](../games/s-z/surviving-mars.md).
- Novelty: not assessed.

## INF-112 — Dome life support and local maintenance are visible

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: network and building panels expose each dome's current power,
  water, oxygen, food and storage coverage plus leaks, dust, required repair
  resources, malfunction and estimated reserve duration.
- Includes: Surviving Mars: Relaunched dome, pipe, tank, grid and maintenance
  diagnostics.
- Excludes: undisclosed disaster timing; colonist comfort causes unrelated to
  survival; one aggregate resource total without topology.
- Parameters: dome, network, supply, demand, storage, reserve duration, leak,
  dust, maintenance threshold, repair resource and malfunction.
- Evidence: [Surviving Mars: Relaunched decomposition](../games/s-z/surviving-mars.md).
- Novelty: not assessed.

## INF-113 — Martian laws, factions, seats and tension are visible

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: political panels expose prepared and locked laws, option effects
  and upkeep, faction agendas and support, Assembly seats, promises, vote state,
  global tension and crisis causes.
- Includes: Surviving Mars: Relaunched Earth Council and Martian Assembly UI.
- Excludes: hidden future faction events; flavour biographies; research costs
  unrelated to law upkeep.
- Parameters: law, option, prerequisite, preparation, effect, upkeep, faction,
  agenda, seats, support, promise, vote, tension and crisis.
- Evidence: [Surviving Mars: Relaunched decomposition](../games/s-z/surviving-mars.md).
- Novelty: not assessed.

## INF-114 — Independence gates, penalties, contributions and price are visible

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the independence interface exposes required colony and mission
  goals, declaration state, sponsor penalties, sponsor-colony contributions,
  current price reduction, remaining payment and achieved free status.
- Includes: Surviving Mars: Relaunched purchased-independence sequence.
- Excludes: optional post-independence mission goals; platform achievements;
  hidden future sponsor events.
- Parameters: goal, progress, declaration, penalty, sponsor colony, resource,
  contribution, base price, reduction, balance and completion.
- Evidence: [Surviving Mars: Relaunched decomposition](../games/s-z/surviving-mars.md).
- Novelty: not assessed.

## INF-115 — Local sight and sound expose partial opponent state

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: a player directly learns opponents and their actions only through
  current avatar-centred visibility, spatial sound or effects that penetrate the
  local occlusion state.
- Includes: Counter-Strike 2 sightlines, footsteps, shots, reloads, utility and
  bomb interaction audio; Cyberpunk 2077 local sight, footsteps, speech,
  gunfire and scanner-assisted currently exposed hostile state; Marvel Rivals
  third-person sightlines, effects, silhouettes and spatial combat audio;
  Helldivers 2 local patrol silhouettes, movement, calls, shots and effects;
  Rainbow Six Siege avatar sightlines, penetrable occlusion and spatial action audio.
- Excludes: omniscient enemy positions; an authored hidden solution inferred
  from static clues; teammate-transmitted knowledge itself.
- Parameters: view, occlusion, distance, material, sound event and effect state.
- Evidence: [Counter-Strike 2 decomposition](../games/a-f/counter-strike-2.md) and
  [Cyberpunk 2077 decomposition](../games/a-f/cyberpunk-2077.md), and
  [Marvel Rivals decomposition](../games/m-r/marvel-rivals.md), and
  [Helldivers 2 decomposition](../games/g-l/helldivers-2.md) and
  [Pokémon Legends: Z-A decomposition](../games/m-r/pokemon-legends-z-a.md) and
  [Dead by Daylight decomposition](../games/a-f/dead-by-daylight.md), and
  [The Binding of Isaac: Rebirth decomposition](../games/s-z/the-binding-of-isaac-rebirth.md), and
  [Rainbow Six Siege decomposition](../games/s-z/tom-clancys-rainbow-six-siege.md), and
  [War Thunder decomposition](../games/s-z/war-thunder.md), and
  [Team Fortress 2 decomposition](../games/s-z/team-fortress-2.md).
- Additional support: [Left 4 Dead 2 decomposition](../games/g-l/left-4-dead-2.md),
  for local Infected silhouettes, vocalisations, movement and attack sounds.
- Additional support: [Destiny 2 decomposition](../games/a-f/destiny-2.md),
  for local hostile sight, spatial audio and combat effects.
- Additional support: [Cuphead decomposition](../games/a-f/cuphead.md),
  for visual-only local projectile paths and beam wind-ups; this carrier makes
  no audio claim.
- Additional support: [Resident Evil 2 (2019 remake) decomposition](../games/m-r/resident-evil-2-2019.md),
  for visual-only local zombie sight and approach cues; this carrier makes no audio claim.
- Additional support: [Resident Evil: Director's Cut decomposition](../games/m-r/resident-evil-directors-cut.md),
  for fixed-camera local sight plus spatial hostile sounds without an omniscient enemy map.
- Additional support: [Halo 3 decomposition](../games/g-l/halo-3.md),
  for local hostile sight, spatial sound and combat effects.
- Novelty: not assessed.

## INF-116 — Live team, score and shared-objective state are visible

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the live team interface exposes eligible allied status, match clock or score and current shared-objective ownership, progress or phase state.
- Includes: Counter-Strike 2, Dota 2, Marvel Rivals, Battlefield 6 and
  Helldivers 2 team HUD, radar or minimap and objective state, including
  Reinforce stock and mission time where applicable; EA SPORTS FC 26 match
  score, clock, side identity and restart state; Rainbow Six Siege team health,
  score, phase clock, bomb sites and defuser state; Football Manager 26 score,
  clock, team condition and live match phase; Rocket League team labels, score,
  regulation clock and overtime state.
- Excludes: permanent omniscient enemy tracking; post-match analytics; account rank.
- Parameters: team frames, allied state, radar or minimap, shared sightings, clock, score, objective schema, phase and respawn notice.
- Evidence: [Counter-Strike 2 decomposition](../games/a-f/counter-strike-2.md),
  [Dota 2 decomposition](../games/a-f/dota-2.md),
  [Marvel Rivals decomposition](../games/m-r/marvel-rivals.md),
  [Battlefield 6 decomposition](../games/a-f/battlefield-6.md) and
  [Helldivers 2 decomposition](../games/g-l/helldivers-2.md) and
  [Dead by Daylight decomposition](../games/a-f/dead-by-daylight.md), and
  [EA SPORTS FC 26 decomposition](../games/a-f/ea-sports-fc-26.md) and
  [Rainbow Six Siege decomposition](../games/s-z/tom-clancys-rainbow-six-siege.md),
  [Football Manager 26 decomposition](../games/a-f/football-manager-26.md), and
  [Rocket League decomposition](../games/m-r/rocket-league.md), and
  [War Thunder decomposition](../games/s-z/war-thunder.md), and
  [Team Fortress 2 decomposition](../games/s-z/team-fortress-2.md).
- Additional support: [Left 4 Dead 2 decomposition](../games/g-l/left-4-dead-2.md),
  for Survivor health/status frames and shared checkpoint state.
- Additional support: [Destiny 2 decomposition](../games/a-f/destiny-2.md),
  for live activity score and objective/phase state.
- Novelty: not assessed.

## INF-117 — Personal economy and transaction offers are visible

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: the player can inspect current money, offered buy or sell prices,
  relevant owned stock and the availability or value of a transaction before
  committing a purchase, sale or service-menu allocation.
- Includes: Counter-Strike 2 Competitive money display and buy menu; Grand Theft
  Auto V Story Mode character balances and shop offers; Cyberpunk 2077 eurodollar
  balance, vendor prices and purchase eligibility; the Fishmonger's offered
  catch prices in DREDGE; DAVE THE DIVER's visible dish prices, supported
  servings and retained balance before its bounded first service.
- Excludes: opponents' exact hidden balances; cosmetic marketplace prices; a
  hidden future demand distribution; a terminal report that shows revenue only
  after every transactional decision has ended.
- Parameters: balance, price, role, owned stock, buy, sell or menu-offer state,
  availability and refund state.
- Evidence: [Counter-Strike 2 decomposition](../games/a-f/counter-strike-2.md)
  [Grand Theft Auto V decomposition](../games/g-l/grand-theft-auto-v.md), and
  [Cyberpunk 2077 decomposition](../games/a-f/cyberpunk-2077.md),
  [DREDGE decomposition](../games/a-f/dredge.md) and
  [DAVE THE DIVER decomposition](../games/a-f/dave-the-diver.md).
- Additional support: [Dead Cells decomposition](../games/a-f/dead-cells.md),
  for shop prices shown against the gold balance before purchase.
- Novelty: not assessed.
- Change note: wording generalised by
  [`TAXONOMY_CHANGE_038`](../../research/taxonomy-changes/TAXONOMY_CHANGE_038.md)
  to make the already-reviewed sell-side carrier explicit and admit a service
  offer whose price and supported stock are visible before allocation.

## INF-118 — Team-shared fog-limited world and minimap state

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the player sees current terrain, allied entities and hostiles
  revealed by any eligible allied vision source, with the same bounded state
  summarised on a team minimap.
- Includes: Dota 2 shared unit/ward vision, fog and minimap sightings.
- Excludes: omniscient spectator view; voluntary team chat content.
- Parameters: allied source, radius, terrain, hostile visibility and minimap marker.
- Evidence: [Dota 2 decomposition](../games/a-f/dota-2.md).
- Novelty: not assessed.

## INF-119 — Personal character resources and build are visible

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the interface exposes a controlled character's health, action or
  casting resources, experience, attributes, learned build, status effects and
  ability readiness.
- Includes: Dota 2 hero HUD and ability/talent panels; Clair Obscur: Expedition
  33 character menus and combat resources; Grand Theft Auto V Story Mode health,
  armour, special meter and character-stat panels; Cyberpunk 2077 health, RAM,
  level, attributes, perks, skills and cooldown displays; Marvel Rivals hero
  health, ultimate meter, ability readiness, status and selected Team-Up state;
  Hollow Knight: Silksong health, Silk, equipped Crest and Tool state.
  Hollow Knight health Masks and SOUL reserve; Helldivers 2 health,
  injury/status and selected stratagem charge or cooldown state.
- Excludes: hidden enemy cooldowns; account statistics; exact future turn order.
- Parameters: health, resource, experience, level, attributes, skill, status,
  cooldown and persistence.
- Evidence: [Dota 2 decomposition](../games/a-f/dota-2.md),
  [Clair Obscur: Expedition 33 decomposition](../games/a-f/clair-obscur-expedition-33.md),
  [Grand Theft Auto V decomposition](../games/g-l/grand-theft-auto-v.md), and
  [Cyberpunk 2077 decomposition](../games/a-f/cyberpunk-2077.md), and
  [Marvel Rivals decomposition](../games/m-r/marvel-rivals.md), and
  [Hollow Knight: Silksong decomposition](../games/g-l/hollow-knight-silksong.md), and
  [Monster Hunter Wilds decomposition](../games/m-r/monster-hunter-wilds.md), and
  [Hollow Knight decomposition](../games/g-l/hollow-knight.md).
- Evidence: [Terraria decomposition](../games/s-z/terraria.md).
- Evidence: [Helldivers 2 decomposition](../games/g-l/helldivers-2.md) and
  [Pokémon Legends: Z-A decomposition](../games/m-r/pokemon-legends-z-a.md) and
  [Dead by Daylight decomposition](../games/a-f/dead-by-daylight.md), and
  [Team Fortress 2 decomposition](../games/s-z/team-fortress-2.md).
- Additional support: [Warcraft III: Reign of Chaos decomposition](../games/s-z/warcraft-iii-reign-of-chaos.md),
  for Thrall's health, mana, experience, level, learned Chain Lightning and
  readiness state.
- Additional support: [Left 4 Dead 2 decomposition](../games/g-l/left-4-dead-2.md),
  for controlled-Survivor health, temporary health and status feedback.
- Additional support: [Destiny 2 decomposition](../games/a-f/destiny-2.md),
  for Titan shield/health, fixed build and ability readiness.
- Additional support: [Cuphead decomposition](../games/a-f/cuphead.md),
  for the visible remaining-HP allowance and charged Super Meter cards.
- Additional support: [Darkest Dungeon decomposition](../games/a-f/darkest-dungeon.md),
  for each hero's health, stress, stats, resistances, status icons and the four equipped skills with their accuracy, damage and critical values.
- Additional support: [Dead Cells decomposition](../games/a-f/dead-cells.md),
  for the HUD's health bar with its orange portion, gold, cells, equipped gear and stats.
- Additional support: [Halo 3 decomposition](../games/g-l/halo-3.md),
  for visible personal shield and underlying health readiness.
- Additional support: [Battletoads decomposition](../games/a-f/battletoads.md),
  for the visible current energy segments before damage, healing or life loss.
- Additional support: [Super Metroid decomposition](../games/s-z/super-metroid.md),
  for visible Energy, missile reserve and inspectable retained suit abilities.
- Additional support: [Chrono Trigger decomposition](../games/a-f/chrono-trigger.md),
  for visible party HP/MP, personal Battle Gauges, learned commands, item stock
  and fair/general currency state.
- Novelty: not assessed.

## INF-120 — Match economy, item logistics and buyback are visible

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the player can inspect current gold, shop prices and access,
  hero/backpack/stash/courier items, recipe dependencies and buyback state.
- Includes: Dota 2 shop, inventory, courier and buyback panels.
- Excludes: opponents' hidden gold; cosmetic inventory value.
- Parameters: gold, price, shop, recipe, slot, courier, cost and cooldown.
- Evidence: [Dota 2 decomposition](../games/a-f/dota-2.md).
- Novelty: not assessed.

## INF-121 — Team clock, score, structures and objectives are visible

- Lifecycle: `Merged`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: historical game-specific duplicate now represented by the
  parameterised active boundary `INF-116`.
- Includes: historical references that used `INF-121` before registry
  normalisation 006.
- Excludes: new game signatures; use `INF-116` with the scoped parameters and
  any retained companion Constraints or System behaviours.
- Parameters: none; preserved as a lifecycle alias.
- Evidence: [Dota 2 decomposition](../games/a-f/dota-2.md).
- Merged into: `INF-116` by
  [`TAXONOMY_CHANGE_014`](../../research/taxonomy-changes/TAXONOMY_CHANGE_014.md).

## INF-122 — Capture probability and attempt state are visible

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: before and during an eligible capture, the interface exposes the
  target and device's current success estimate plus the progress or failure of
  the committed checks.
- Includes: Palworld capture percentage and Sphere attempt feedback; Pokémon
  Legends: Z-A capture arrows and committed throw feedback.
- Excludes: a guaranteed hidden recruitment roll; exact future random sample;
  creature combat damage alone.
- Parameters: target, device, estimated chance, check progress, success and failure.
- Evidence: [Palworld decomposition](../games/m-r/palworld.md) and
  [Pokémon Legends: Z-A decomposition](../games/m-r/pokemon-legends-z-a.md).
- Novelty: not assessed.

## INF-123 — Companion profile exposes combat and assignment capabilities

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the player can inspect an owned companion's identity, level,
  stats, type or element, health/status, learned skills or moves, passives and
  ruleset-specific capabilities before a party, roster or assignment decision.
- Includes: Palworld Pal detail and Palbox management panels; Pokémon Legends:
  Z-A Pokémon summaries exposing level, stats, type and learned moves.
  It also includes Pokémon Red Version party summaries before switching or
  route planning.
- Excludes: undiscovered wild-creature identity; cosmetic-only appearance;
  hidden random future mutation.
- Parameters: identity, level, stats, type or element, skills, passives,
  partner interaction and assignment capability.
- Evidence: [Palworld decomposition](../games/m-r/palworld.md) and
  [Pokémon Legends: Z-A decomposition](../games/m-r/pokemon-legends-z-a.md).
- Additional support: [Pokémon Red Version decomposition](../games/m-r/pokemon-red-version.md).
- Novelty: not assessed.

## INF-124 — Avatar and active-party survival state are visible

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the HUD exposes the avatar's health, hunger, stamina, temperature
  and equipped state together with active-party companion health and readiness.
- Includes: Palworld exploration and combat HUD.
- Excludes: base-wide task detail; hidden wild-creature stats; post-run analytics.
- Parameters: health, hunger, stamina, temperature, armour, durability, party,
  active companion and cooldown.
- Evidence: [Palworld decomposition](../games/m-r/palworld.md).
- Novelty: not assessed.

## INF-125 — Explored map and authored mission gates are visible

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: discovered terrain, travel points, mission markers and current
  main-mission requirements are inspectable before route choice.
- Includes: Palworld map, Watchtower reveal, mission list and World Tree markers;
  Grand Theft Auto V Story Mode map icons and critical-path mission prompts;
  Cyberpunk 2077 map, journal, tracked job and fast-travel points; Hollow
  Knight: Silksong explored map, pins and current route gates.
- Excludes: undiscovered map contents; optional external interactive maps;
  custom server navigation aids.
- Parameters: discovered region, marker, fast travel, objective, prerequisite
  and completion.
- Evidence: [Palworld decomposition](../games/m-r/palworld.md) and
  [Grand Theft Auto V decomposition](../games/g-l/grand-theft-auto-v.md), and
  [Cyberpunk 2077 decomposition](../games/a-f/cyberpunk-2077.md), and
  [Hollow Knight: Silksong decomposition](../games/g-l/hollow-knight-silksong.md), and
  [Monster Hunter Wilds decomposition](../games/m-r/monster-hunter-wilds.md) and
  [Pokémon Legends: Z-A decomposition](../games/m-r/pokemon-legends-z-a.md).
- Evidence: [Terraria decomposition](../games/s-z/terraria.md).
- Additional support: [Resident Evil 2 (2019 remake) decomposition](../games/m-r/resident-evil-2-2019.md),
  for the visited-places map and the objective list with its sub-objectives.
- Additional support: [Resident Evil: Director's Cut decomposition](../games/m-r/resident-evil-directors-cut.md),
  for the status map retaining visited mansion rooms and Chris's current position.
- Additional support: [Halo 3 decomposition](../games/g-l/halo-3.md),
  for current mission waypoints and authored route gates.
- Additional support: [StarCraft II decomposition](../games/s-z/starcraft-ii.md),
  for the visible `Liberation Day` objective and designated Headquarters target.
- Additional support: [Warcraft III: Reign of Chaos decomposition](../games/s-z/warcraft-iii-reign-of-chaos.md),
  for current chapter objectives, route beacons and the final Prophet
  rendezvous.
- Additional support: [Super Metroid decomposition](../games/s-z/super-metroid.md),
  for the HUD minimap and pause map exposing Samus's visited rooms and current
  position before the next route choice.
- Novelty: not assessed.

## INF-126 — Base assignments, resources and worker condition are visible

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: base interfaces expose assigned companions, fixed jobs and
  priorities, available shared materials, facility task state and worker
  hunger, sanity, health or illness.
- Includes: Palworld Palbox, Monitoring Stand, storage and base status displays.
- Excludes: remote multiplayer guild administration; hidden future production;
  active-party combat HUD.
- Parameters: base, worker, assignment, priority, inventory, facility, task,
  hunger, sanity and ailment.
- Evidence: [Palworld decomposition](../games/m-r/palworld.md).
- Novelty: not assessed.

## INF-127 — Match map exposes current insertion and zone timing

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the world map and HUD expose the participant's current position,
  visible aircraft state, present safe-area and Blue/Red Zone boundaries, and
  the warning or contraction timing needed for the next route decision.
- Includes: PUBG Normal Match map, minimap, plane, white circle, Blue Zone,
  Red Zone and phase countdowns.
- Excludes: exact future safe-circle centres; hidden opponents; external map tools.
- Parameters: player, aircraft, safe circle, damaging boundary, hazard region,
  phase, warning and contraction timer.
- Evidence: [PUBG: BATTLEGROUNDS decomposition](../games/m-r/pubg-battlegrounds.md).
- Novelty: not assessed.

## INF-130 — Map exposes self, landmarks and wipe horizon

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the map and server interface expose the player's current island
  position, visible biomes or monuments and the declared next wipe horizon
  without revealing ordinary opponent positions or unopened loot.
- Includes: Rust world map, monument labels and server wipe timer.
- Excludes: omniscient player tracking; future loot contents; hidden base
  interiors.
- Parameters: player position, terrain, biome, monument, safe zone, marker,
  server and wipe time.
- Evidence: [Rust decomposition](../games/m-r/rust.md).
- Novelty: not assessed.

## INF-131 — Building interface exposes placement legality and operation state

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: placement previews and building feedback expose whether the
  current operation is geometrically legal, supported and authorised, while
  relevant fixture feedback exposes the local conditions governing building or
  station operation.
- Includes: Rust placement colour, BUILDING PRIVILEGE/BLOCKED, stability and
  TC cost per 24 hours; Valheim support colour, shelter/cover and covered-
  Workbench operation feedback.
- Additional support: [Bloons TD 6 decomposition](../games/a-f/bloons-td-6.md),
  for the placement preview that reports whether the candidate position is
  geometrically legal before a defender is committed; and
  [Command & Conquer Remastered Collection decomposition](../games/a-f/command-and-conquer-remastered-collection.md),
  for mobile-construction and completed-building placement feedback.
- Excludes: hidden enemy TC inventory; future raid damage; exact remote base
  layout.
- Parameters: preview, socket, stability/support, shelter/cover, privilege,
  blocked reason, station state, upkeep, stored material and protected duration.
- Evidence: [Rust decomposition](../games/m-r/rust.md) and
  [Valheim decomposition](../games/s-z/valheim.md).
- Novelty: not assessed.

## INF-132 — Research and crafting dependencies are visible

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: the crafting, Research Table and Workbench interfaces expose
  known status, prerequisites, ingredients, scrap or fragment costs, required
  tier, queue progress and declared output before commitment.
- Includes: Rust blueprint, tech-tree, Workbench and crafting-queue panels.
  Cyberpunk 2077 crafting specifications expose components and output tier.
- Excludes: unrevealed world-loot rolls; other players' blueprint knowledge;
  hidden future server balance changes.
- Parameters: recipe, learned state, prerequisite, cost, ingredient, workbench,
  duration, queue and output.
- Evidence: [Rust decomposition](../games/m-r/rust.md) and
  [Cyberpunk 2077 decomposition](../games/a-f/cyberpunk-2077.md).
- Evidence: [Terraria decomposition](../games/s-z/terraria.md).
- Additional support: [Don't Starve Together decomposition](../games/a-f/dont-starve-together.md),
  for visible crafting ingredients, prototype state and required science tier.
- Additional support: [Animal Crossing: New Horizons decomposition](../games/a-f/animal-crossing-new-horizons.md),
  for visible DIY recipe knowledge, branch cost, workbench context and tool output.
- Novelty: not assessed.

## INF-128 — Ground loot and inventory compatibility are visible

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: reachable world items and the inventory interface expose item
  identity, quantity, equipment or attachment compatibility and remaining
  carrying state before the player transfers or replaces loot.
- Includes: PUBG ground labels, inventory stacks, weapon and attachment slots,
  backpack load and equipment comparison; Cyberpunk 2077 loot labels,
  inventory comparisons, weapon slots and carry weight.
- Excludes: contents of unopened remote death crates; future loot spawns;
  opponents' carried inventories.
- Parameters: item, quantity, slot, weapon compatibility, capacity, equipped
  state, replacement and reach.
- Evidence: [PUBG: BATTLEGROUNDS decomposition](../games/m-r/pubg-battlegrounds.md) and
  [Cyberpunk 2077 decomposition](../games/a-f/cyberpunk-2077.md), and
  [Monster Hunter Wilds decomposition](../games/m-r/monster-hunter-wilds.md), and
  [Don't Starve Together decomposition](../games/a-f/dont-starve-together.md).
- Additional support: [Resident Evil 2 (2019 remake) decomposition](../games/m-r/resident-evil-2-2019.md),
  for the interact icon, item name and slot state before a pickup.
- Additional support: [Resident Evil: Director's Cut decomposition](../games/m-r/resident-evil-directors-cut.md),
  for item identity, quantity, equip state and remaining six-slot capacity in the status inventory.
- Additional support: [Darkest Dungeon decomposition](../games/a-f/darkest-dungeon.md),
  for the loot window and inventory slots that expose item identity, stack state and free capacity before a pickup.
- Additional support: [The Long Dark decomposition](../games/s-z/the-long-dark.md),
  for searched supplies, clothing or weapon compatibility, carried weight and
  the choice to take or leave route loot.
- Additional support: [Animal Crossing: New Horizons decomposition](../games/a-f/animal-crossing-new-horizons.md),
  for visible branches, capture tools, specimen identity and free inventory state.
- Novelty: not assessed.

## INF-129 — Survivor count and elimination feed are visible

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the interface exposes the current number of living participants,
  public elimination events and the terminal placement or victory result
  without revealing every survivor's location or loadout.
- Includes: PUBG alive counter, kill feed, death result and chicken-dinner state.
- Excludes: omniscient spectator positions; hidden player inventory; post-match
  progression rewards.
- Parameters: alive count, event participants, event cause, placement, personal
  kills and terminal result.
- Evidence: [PUBG: BATTLEGROUNDS decomposition](../games/m-r/pubg-battlegrounds.md).
- Novelty: not assessed.

## INF-133 — Graded moodles expose embodied pressure categories

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the interface names current hunger, thirst, fatigue, exertion,
  panic, stress, pain, sickness, temperature, encumbrance and related categories
  at graded severity while leaving complete internal numeric state hidden.
- Includes: Project Zomboid moodle stack and tooltips.
- Excludes: exact health-panel wounds; cosmetic facial emotion; one visible
  undifferentiated health bar.
- Parameters: category, grade, icon, tooltip, threshold, modifier and hidden value.
- Evidence: [Project Zomboid decomposition](../games/m-r/project-zomboid.md).
- Novelty: not assessed.

## INF-134 — Body health panel exposes wounds and applied treatments

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: an inspectable body diagram identifies affected regions, visible
  wound classes, bleeding and current treatment so the player can select a
  compatible care action, without revealing a concealed Knox Infection flag.
- Includes: Project Zomboid Health panel.
- Excludes: exact future recovery time; omniscient infection diagnosis; moodle
  summaries without body location.
- Parameters: region, wound, bleeding, treatment, bandage state, pain, visible
  infection and concealed transmission state.
- Evidence: [Project Zomboid decomposition](../games/m-r/project-zomboid.md).
- Novelty: not assessed.

## INF-135 — Isometric cutaway reveals only locally perceived space

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: the world view cuts away obstructing architecture around the
  survivor and renders only terrain, interiors, items and creatures currently
  available through local vision, hearing or remembered exploration.
- Includes: Project Zomboid's Sims-style cutaway vision and local sound cues.
- Excludes: an omniscient top-down map; hidden container contents; exact zombie
  positions beyond perception.
- Parameters: camera, floor, wall cutaway, line of sight, lighting, hearing,
  explored memory and occlusion.
- Evidence: [Project Zomboid decomposition](../games/m-r/project-zomboid.md).
- Novelty: not assessed.

## INF-136 — Calendar and survival infrastructure state are inspectable

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: clocks, weather cues, container and appliance state, crop panels
  and item tooltips expose the current date, accessible reserves, power or water
  availability, freshness and crop condition without revealing every future
  cutoff or weather sample.
- Includes: Project Zomboid long-horizon shelter and farming inspection.
- Excludes: exact hidden utility shutoff date; undiscovered loot; a global
  forecast of all future seasons.
- Parameters: date, time, weather, service state, container, reserve, item age,
  crop phase, water and disease.
- Evidence: [Project Zomboid decomposition](../games/m-r/project-zomboid.md) and
  [Don't Starve Together decomposition](../games/a-f/dont-starve-together.md).
- Additional support: [Animal Crossing: New Horizons decomposition](../games/a-f/animal-crossing-new-horizons.md),
  for the NookPhone and world cues exposing current date, hour, weather and season.
- Novelty: not assessed.

## INF-137 — Raid map exposes condition, extraction and remaining time

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the mission or raid interface identifies the current map and
  condition, shows known objectives, points of interest and eligible extraction
  fixtures, and exposes remaining session or departure timing needed to route risk.
- Includes: ARC Raiders Topside map, regional condition and extraction state;
  Helldivers 2 mission map, main objective, extraction location and mission time.
- Excludes: exact hidden loot rolls; omniscient Raider positions; future Map
  Condition schedules outside the current raid.
- Parameters: map, condition, point of interest, endpoint, endpoint state,
  Raider position, route marker and clock.
- Evidence: [ARC Raiders decomposition](../games/a-f/arc-raiders.md) and
  [Helldivers 2 decomposition](../games/g-l/helldivers-2.md).
- Novelty: not assessed.

## INF-138 — Inventory marks value, compatibility and defeat protection

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: item and inventory panels expose identity, rarity, stack,
  durability, compatible slot, sale or recycle value and whether current
  placement protects the item from knockout loss.
- Includes: ARC Raiders backpack, loadout, Safe Pocket and stash tooltips.
- Excludes: unopened-container contents; hidden future market rotation;
  another Raider's complete inventory.
- Parameters: item, rarity, quantity, durability, slot, compatibility, value,
  protected state and capacity.
- Evidence: [ARC Raiders decomposition](../games/a-f/arc-raiders.md).
- Novelty: not assessed.

## INF-139 — ARC cues disclose type, attention and vulnerable components

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: visible form, lights, movement, emitted sound and attack windups
  let the player identify an ARC machine's type, current attention, imminent
  attack and externally vulnerable or destructible components without exposing
  its complete hidden controller state.
- Includes: ARC Raiders machine audio, target-switch cues, telegraphs, armour
  and weak-point feedback.
- Excludes: exact internal AI probabilities; other Raiders' intentions; a
  permanent omniscient target marker through cover.
- Parameters: machine type, cue, alert, target switch, windup, attack, armour,
  component, hit feedback and destroyed state.
- Evidence: [ARC Raiders decomposition](../games/a-f/arc-raiders.md).
- Novelty: not assessed.

## INF-140 — Raid settlement exposes retained loss and persistent rewards

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: after the raid ends, the result presentation distinguishes
  extraction from knockout, item retention from forfeiture and awarded
  experience, level or quest progress before the next loadout is prepared.
- Includes: ARC Raiders End of Round and return-to-Speranza result state.
- Excludes: hidden loot that was never searched; future Expedition rewards;
  another squad's private progression.
- Parameters: terminal result, extracted items, protected items, lost items,
  XP, level, skill point, quest progress and next hub state.
- Evidence: [ARC Raiders decomposition](../games/a-f/arc-raiders.md).
- Novelty: not assessed.

## INF-141 — Combat HUD exposes turn order, AP, party and target state

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: during battle the interface exposes upcoming combatant order,
  current character AP, party health and status plus the selected enemy's
  health, Break and condition state before command commitment.
- Includes: Clair Obscur: Expedition 33 reactive turn-based combat HUD.
- Excludes: exact future enemy move contents; offscreen exploration secrets;
  post-battle statistics alone.
- Parameters: queue horizon, AP, health, status, target and Break gauge.
- Evidence: [Clair Obscur: Expedition 33 decomposition](../games/a-f/clair-obscur-expedition-33.md).
- Novelty: not assessed.

## INF-142 — Attack motion, sound and prompts cue reactive timing

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: animation, sound and optional prompt elements disclose enough of
  an executing attack's rhythm for the player to time its offensive or
  defensive real-time input without revealing the exact timing numerically.
- Includes: Clair Obscur: Expedition 33 skill prompts and Nevron attack cues;
  Street Fighter 6 attack animation, contact effects, sound and Counter Hit,
  Throw Escape or Reversal notices.
- Excludes: a static turn-order preview; hidden untelegraphed damage; a
  persistent countdown that reveals an exact future event time.
- Parameters: cue channel, attack member, rhythm, prompt visibility and assist.
- Evidence: [Clair Obscur: Expedition 33 decomposition](../games/a-f/clair-obscur-expedition-33.md)
  and [Street Fighter 6 decomposition](../games/s-z/street-fighter-6.md).
- Additional support: [Brawlhalla decomposition](../games/a-f/brawlhalla.md),
  for attack motion, impact effects and recovery poses that cue live dodge and
  counterattack timing.
- Additional support: [Dead Cells decomposition](../games/a-f/dead-cells.md),
  for enemy wind-ups and attack prompts that cue roll, parry and strike timing.
- Additional support: [TEKKEN 8 decomposition](../games/s-z/tekken-8.md),
  for attack start-up animation that lets a slow low or mid be guarded
  before it lands and the throw animation's extended hand that selects the
  break button inside the response window; no sound channel is asserted, and
  the post-contact PUNISH, CLEAN, COUNTER and TORNADO notices are outcome
  feedback recorded under `INF-210`.
- Novelty: not assessed.

## INF-143 — Build interface exposes Picto mastery and Lumina cost

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the party build interface exposes acquired Pictos, equipped stat
  effects, battle-mastery progress, learned Luminas, their costs and each
  character's remaining activation capacity before configuration.
- Includes: Clair Obscur: Expedition 33 Pictos and Lumina menus in version 1.5.6.
- Excludes: concealed future loot; skill timing prompts; exact enemy build state.
- Parameters: Picto, mastery count, passive, cost, capacity and equipped state.
- Evidence: [Clair Obscur: Expedition 33 decomposition](../games/a-f/clair-obscur-expedition-33.md).
- Novelty: not assessed.

## INF-144 — Navigation view exposes GPS route and wanted search

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the map and minimap expose the controlled protagonist, chosen or
  authored destination, calculated road route and current police search state
  needed to choose travel and evasion paths.
- Includes: Grand Theft Auto V Story Mode GPS line, waypoint, wanted stars,
  police markers and search cones; Cyberpunk 2077 route guidance, waypoint,
  minimap and NCPD Heat/search state; Need for Speed Unbound LPD pursuit and
  garage-route guidance.
- Excludes: undiscovered optional content; exact future traffic positions;
  omniscient hostile tracking outside the wanted search.
- Parameters: protagonist, destination, route, recalculation, stars, police
  marker, cone and minimap scale.
- Evidence: [Grand Theft Auto V decomposition](../games/g-l/grand-theft-auto-v.md) and
  [Cyberpunk 2077 decomposition](../games/a-f/cyberpunk-2077.md).
- Novelty: not assessed.

## INF-145 — Character wheel exposes protagonist availability and context

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: before a control transfer, the character interface identifies
  unlocked protagonists, marks unavailable choices and previews the selected
  character whose current world activity will receive control.
- Includes: Grand Theft Auto V Story Mode character wheel and switch transition.
- Excludes: hidden off-screen future missions; turn-order panels; multiplayer
  player lists.
- Parameters: protagonist, availability, portrait, current activity, mission
  restriction and transition.
- Evidence: [Grand Theft Auto V decomposition](../games/g-l/grand-theft-auto-v.md).
- Novelty: not assessed.

## INF-146 — Heist board exposes approach, roles, skill and cut

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the planning interface discloses available approaches, required
  specialist roles and each unlocked candidate's competence and percentage cut
  before the player commits the operation plan.
- Includes: Grand Theft Auto V Story Mode major-heist planning boards.
- Excludes: exact concealed future mistakes; GTA Online lobby readiness;
  post-heist payout only.
- Parameters: approach, preparation, role, candidate, skill, cut, availability
  and confirmed plan.
- Evidence: [Grand Theft Auto V decomposition](../games/g-l/grand-theft-auto-v.md).
- Novelty: not assessed.

## INF-147 — Scanner exposes target state and available quickhacks

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: scanner focus reveals an eligible actor or device's disclosed
  identity, affiliation, vulnerabilities and current hackable functions, plus
  each installed quickhack's RAM cost, upload state and availability.
- Includes: Cyberpunk 2077 base-game Kiroshi scanning and quickhack selection.
- Excludes: future patrol paths; concealed loot; information available only
  after an unselected dialogue branch.
- Parameters: target, identity, affiliation, level, vulnerability, device
  function, quickhack, RAM cost, upload, cooldown and trace.
- Evidence: [Cyberpunk 2077 decomposition](../games/a-f/cyberpunk-2077.md).
- Novelty: not assessed.

## INF-148 — Dialogue interface exposes contextual response gates

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the conversation interface presents currently available
  responses and marks their timing, lifepath or attribute context before the
  player commits, without disclosing all downstream quest consequences.
- Includes: Cyberpunk 2077 dialogue, timed response, lifepath and attribute
  options.
- Excludes: hidden future branch flags; subtitles with no choice; an external
  walkthrough revealing consequences.
- Parameters: option, speaker, timer, lifepath, attribute, threshold,
  availability, styling and concealed consequence.
- Evidence: [Cyberpunk 2077 decomposition](../games/a-f/cyberpunk-2077.md).
- Novelty: not assessed.

## INF-149 — Cyberware interface exposes capacity and implant effects

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the ripperdoc and character interfaces expose current cyberware
  capacity, compatible body slots, installed and offered implants, armour,
  attunement, tier, price and declared ability effects before configuration.
- Includes: Cyberpunk 2077 Update 2.0+ cyberware menus.
- Excludes: concealed vendor-stock changes at future levels; cosmetic body
  appearance; hidden enemy implants outside scanner disclosure.
- Parameters: capacity, slot, implant, tier, armour, attunement, effect, price,
  components and compatibility.
- Evidence: [Cyberpunk 2077 decomposition](../games/a-f/cyberpunk-2077.md).
- Novelty: not assessed.

## INF-150 — Character roster exposes roles, kits and composition alternatives

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the match selection interface exposes currently available
  characters, their role or class, ability kit, allied occupancy and any
  offered composition alternatives before confirmation.
- Includes: Marvel Rivals Season 9.5 hero and Team-Up selection state; Apex
  Legends Legend classes, kits and current squad occupancy; Rainbow Six Siege
  attacker/defender operator kits, team occupancy and current bans.
- Excludes: hidden opponent selection before disclosure; cosmetic skin details;
  external tier-list recommendations.
- Parameters: character, role or class, team occupancy, ability, composition
  option, base effect, enhanced effect and selection state.
- Evidence: [Marvel Rivals decomposition](../games/m-r/marvel-rivals.md),
  [Apex Legends decomposition](../games/a-f/apex-legends.md) and
  [Rainbow Six Siege decomposition](../games/s-z/tom-clancys-rainbow-six-siege.md), and
  [Team Fortress 2 decomposition](../games/s-z/team-fortress-2.md).
- Novelty: not assessed.

## INF-151 — Match HUD exposes team, phase and live objective state

- Lifecycle: `Merged`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: historical game-specific duplicate now represented by the
  parameterised active boundary `INF-116`.
- Includes: historical references that used `INF-151` before registry
  normalisation 006.
- Excludes: new game signatures; use `INF-116` with the scoped parameters and
  any retained companion Constraints or System behaviours.
- Parameters: none; preserved as a lifecycle alias.
- Evidence: [Marvel Rivals decomposition](../games/m-r/marvel-rivals.md).
- Merged into: `INF-116` by
  [`TAXONOMY_CHANGE_014`](../../research/taxonomy-changes/TAXONOMY_CHANGE_014.md).

## INF-152 — Dice interface exposes difficulty, modifiers and reroll state

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: before and during an eligible explicit check, the interface
  exposes its difficulty, governing skill, current modifiers, available bonus
  sources, advantage or disadvantage and remaining Inspiration rerolls without
  revealing every downstream narrative consequence.
- Includes: Baldur's Gate 3 dialogue and explicit ability-check dice interface.
- Excludes: automatic passive checks; hidden future quest branches; damage dice.
- Parameters: difficulty, skill, modifier, proficiency, bonus, advantage,
  disadvantage, rolled total, success, failure and Inspiration.
- Evidence: [Baldur's Gate 3 decomposition](../games/a-f/baldurs-gate-3.md).
- Novelty: not assessed.

## INF-153 — Party interface exposes active members, condition and approval

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: party frames and character sheets identify the current active
  members and expose their health, conditions, concentration, equipment and
  inspectable approval state before control, treatment or formation changes.
- Includes: Baldur's Gate 3 single-player party HUD and companion sheets.
- Excludes: exact concealed approval triggers; inactive strangers; romance state.
- Parameters: member, active slot, health, condition, concentration, equipment,
  approval value or category and selected control.
- Evidence: [Baldur's Gate 3 decomposition](../games/a-f/baldurs-gate-3.md).
- Novelty: not assessed.

## INF-154 — Rest interface exposes recovery and camp-supply commitment

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: before committing a short or long rest, the interface identifies
  the rest type, remaining short-rest opportunities, required and selected camp
  supplies and whether the resulting long rest will be full or partial.
- Includes: Baldur's Gate 3 Balanced rest and camp-supply interfaces.
- Excludes: concealed future camp scenes; external inventory calculators;
  restoration from a spell or potion.
- Parameters: rest type, remaining uses, required supplies, selected supplies,
  full-rest state, partial-rest state and declared recovery.
- Evidence: [Baldur's Gate 3 decomposition](../games/a-f/baldurs-gate-3.md).
- Novelty: not assessed.

## INF-155 — Deployment map exposes objectives and legal team sources

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: before redeployment, the team map identifies current objective
  ownership, squad positions, active beacons, available vehicles and whether
  each candidate source can presently accept the configured combatant.
- Includes: Battlefield 6 Conquest deployment interface and source icons.
- Excludes: omniscient enemy positions; ordinary first-person minimap use after
  deployment; external voice coordination.
- Parameters: objective, owner, squad source, combat state, beacon, vehicle,
  seat, timer, availability and selection focus.
- Evidence: [Battlefield 6 decomposition](../games/a-f/battlefield-6.md).
- Novelty: not assessed.

## INF-156 — Focus Mode highlights wounds and breakable monster parts

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: while Focus Mode is held, the view marks open localized wounds
  and compatible breakable body regions before the player aims a Focus Strike.
- Includes: Monster Hunter Wilds Focus Mode wound and weak-part highlights.
- Excludes: exact hidden monster health; a damage number alone; an external
  weakness guide.
- Parameters: focus state, body region, wound state, breakable state, highlight
  and occlusion.
- Evidence: [Monster Hunter Wilds decomposition](../games/m-r/monster-hunter-wilds.md).
- Novelty: not assessed.

## INF-157 — Hunt HUD exposes target, clock, faint allowance and monster condition

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the quest interface identifies the active target, remaining
  attempt conditions and observable monster status needed to judge pursuit,
  success or failure without exposing exact hidden health.
- Includes: Monster Hunter Wilds assignment target, timer, faint state and
  visible monster condition or minimap state.
- Excludes: exact internal health values; future drop rolls; external overlays.
- Parameters: target, timer, faint allowance, engagement, condition, zone and
  completion state.
- Evidence: [Monster Hunter Wilds decomposition](../games/m-r/monster-hunter-wilds.md)
  and [Monster Hunter: World decomposition](../games/m-r/monster-hunter-world.md).
- Novelty: not assessed.

## INF-158 — Scoutflies expose a selected target route or last known position

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the navigation layer marks the current route toward a selected
  objective, resource or tracked monster and updates to its current or last
  known field position as evidence changes.
- Includes: Monster Hunter Wilds scoutflies and target map route.
- Excludes: omniscient disclosure of every monster; direct automatic movement;
  an external map guide.
- Parameters: selected target, evidence, current position, last known position,
  route segment, update and lost state.
- Evidence: [Monster Hunter Wilds decomposition](../games/m-r/monster-hunter-wilds.md)
  and [Monster Hunter: World decomposition](../games/m-r/monster-hunter-world.md).
- Novelty: not assessed.

## INF-159 — Combat HUD exposes resources, equipment and carried runes

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: the live HUD discloses HP, FP, stamina, statuses, equipped
  armaments, selected actions and the current carried-rune count.
- Includes: Elden Ring base combat HUD and compass.
- Excludes: hidden stance values; undiscovered loot; future boss phases.
- Parameters: gauges, status, slots, skill, item, runes and target health.
- Evidence: [Elden Ring decomposition](../games/a-f/elden-ring.md).
- Novelty: not assessed.

## INF-160 — Map exposes fragments, Grace, guidance and the rune mark

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: the world map reveals acquired regional detail, discovered Grace,
  advisory guidance, placed markers and the active dropped-rune location.
- Includes: scoped Elden Ring Limgrave map information.
- Excludes: undiscovered exact terrain; forced routing; enemy omniscience.
- Parameters: fragment, region, Grace, guidance, marker and rune mark.
- Evidence: [Elden Ring decomposition](../games/a-f/elden-ring.md).
- Novelty: not assessed.

## INF-161 — Equipment panels expose requirements, scaling and load tier

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: equipment interfaces disclose armament requirements and scaling,
  attack or defence values, weight, capacity and resulting load tier.
- Includes: Elden Ring early equipment and status panels.
- Excludes: hidden enemy stance; undiscovered upgrade results; cosmetic preview.
- Parameters: item, requirements, scaling, values, weight, capacity and tier.
- Evidence: [Elden Ring decomposition](../games/a-f/elden-ring.md).
- Novelty: not assessed.

## INF-162 — Grace menus expose level price, flask split and reset choices

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: an eligible Grace menu shows available rest functions, next level
  cost, attribute preview and current flask allocation before commitment.
- Includes: Elden Ring early Grace levelling and flask menus.
- Excludes: concealed later menu unlocks; live combat HUD; merchant stock.
- Parameters: menu unlock, level price, preview, charges, allocation and time.
- Evidence: [Elden Ring decomposition](../games/a-f/elden-ring.md).
- Novelty: not assessed.

## INF-163 — Explored minimap retains lit terrain and world-state icons

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the character-bound minimap retains the brightest explored tile
  state, updates later visible terrain mutations and marks known spawn points,
  town NPCs, bosses and the most recent death location.
- Includes: Terraria 1.4.5.8 portrait, overlay and full-screen minimap modes.
- Excludes: unreached dark terrain; another character's map history; exact
  future spawns or hidden chest contents.
- Parameters: explored brightness, tile update, character map, icon class,
  zoom, mode and death position.
- Evidence: [Terraria decomposition](../games/s-z/terraria.md).
- Novelty: not assessed.

## INF-164 — Housing query exposes room validity and NPC assignment

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the housing interface identifies available town NPCs and assigned
  rooms, and an addressed-room query reports suitability or a prioritised
  missing frame, wall, furniture, occupancy or home-tile condition.
- Includes: Terraria housing menu, NPC flags and question-mark validation tool.
- Excludes: hidden exact arrival time; biome-happiness optimisation not shown by
  the query; visual decoration with no housing consequence.
- Parameters: NPC flag, room, assignment, validity, failed category and message.
- Evidence: [Terraria decomposition](../games/s-z/terraria.md).
- Novelty: not assessed.

## INF-165 — World and boss cues expose night risk and Eye state

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: environmental light and celestial motion, status messages, enemy
  appearance, boss bar, sprite transformation and minimap icon disclose the
  current day-night risk and live Eye encounter state without revealing its AI rolls.
- Includes: Terraria dusk/night cues, evil-presence warning and first Eye fight.
- Excludes: exact hidden natural-spawn roll; future attack coordinates; external clocks.
- Parameters: phase of day, warning, boss health, phase cue, target icon and dawn.
- Evidence: [Terraria decomposition](../games/s-z/terraria.md).
- Novelty: not assessed.

## INF-166 — Progressive themed-path discovery and earned route disclosure

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the interface begins with one broad semantic clue and a visible
  letter field, retains every accepted answer as an addressed path, reports
  assistance progress, and can progressively disclose an unresolved answer's
  cell set and then its traversal order after earned requests.
- Includes: Strands' Today's Theme clue, retained theme-word and spangram paths,
  Hint meter, highlighted answer letters and subsequent ordered-letter hint.
- Excludes: exposing the complete hidden answer partition at entry; feedback
  about only positional similarity to a guessed word; an unearned walkthrough;
  a clue whose text itself is the answer.
- Parameters: clue specificity, path colours or labels, retained word list,
  progress display, hinted target choice, cell highlight and order notation.
- Evidence: [Strands decomposition](../games/s-z/strands.md).
- Novelty: not assessed.

## INF-167 — Concurrent partner viewport exposes live cooperative state

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: while each human controls one actor, the interface concurrently
  renders the partner's live viewpoint alongside the local viewpoint so that
  both positions, hazards, prompts and interaction progress can inform current
  coordination without changing control ownership.
- Includes: Split Fiction's persistent split-screen presentation in local and
  online cooperative play.
- Excludes: a minimap icon without the partner's view; switching a single
  camera between actors; an external streamed screen; hidden role-exclusive
  information that must be communicated verbally.
- Parameters: pane count, layout, local-player emphasis, online rendering,
  shared overlays, prompt duplication and cutscene behaviour.
- Evidence: [Split Fiction decomposition](../games/s-z/split-fiction.md).
- Novelty: not assessed.

## INF-168 — Active-resident panel exposes motives, mood and action queue

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the live interface exposes the active resident's current motive
  levels, mood or emotional state and ordered or executing interactions so the player
  can attribute behaviour and revise near-term direction.
- Includes: The Sims 4 Live Mode needs panel, emotional state and visible
  interaction queue for Farrah Nouvel; The Sims 2 motive, mood and queued
  interaction display for the selected household resident.
- Excludes: a colony aggregate; a biography-only profile; hidden exact future
  autonomy choices or relationship outcomes.
- Parameters: motive categories, value resolution, mood label, contributing
  modifiers, queue order, cancellation affordance and failed-action feedback.
- Evidence: [The Sims 4 decomposition](../games/s-z/the-sims-4.md) and
  [The Sims 2: Legacy Collection decomposition](../games/s-z/the-sims-2-legacy-collection.md).
- Novelty: not assessed.

## INF-169 — Debrief separates mission, extraction and shared-war results

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the post-mission presentation separately exposes whether the
  required objective succeeded, which participants and carried shared assets
  departed, and what operation-level contribution entered the shared campaign.
- Includes: Helldivers 2 mission debrief separating objective success,
  extracted Helldivers, recovered samples and Galactic War impact.
- Excludes: a single undifferentiated score; live tactical HUD; private account
  experience without any operation or shared-campaign result.
- Parameters: mission result, survivor count, asset types/counts, operation
  status, contribution components, planet and campaign progress.
- Evidence: [Helldivers 2 decomposition](../games/g-l/helldivers-2.md).
- Novelty: not assessed.

## INF-170 — Battle HUD exposes partner, target, health, moves and cooldowns

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the live battle interface identifies the sole active companion
  and current target while exposing health plus the bounded assigned move set
  and each move's current readiness.
- Includes: Pokémon Legends: Z-A partner/target health and four move-button
  cooldown displays.
- Excludes: a storage-only profile; hidden opponent future decisions; an
  unlabelled animation with no readiness feedback.
- Parameters: active partner, target, health, move slots, input mapping,
  cooldown, range feedback and status.
- Evidence: [Pokémon Legends: Z-A decomposition](../games/m-r/pokemon-legends-z-a.md).
- Novelty: not assessed.

## INF-171 — Royale interface exposes rank, points, ticket and promotion target

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the progression interface exposes the current tournament rank,
  accumulated qualification points and threshold, ticket possession and the
  designated opponent for the next promotion.
- Includes: Rank Z, 1,000 Ticket Point threshold, Challenger's Ticket and Zach
  promotion state in Pokémon Legends: Z-A.
- Excludes: hidden matchmaking rating; battle experience; a generic quest title
  without qualification state.
- Parameters: rank, points, threshold, ticket, opponent and promotion status.
- Evidence: [Pokémon Legends: Z-A decomposition](../games/m-r/pokemon-legends-z-a.md).
- Novelty: not assessed.

## INF-172 — Terror Radius encodes approximate Killer proximity

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: survivor audio layers intensify as the Killer enters nearer bands
  and change for an active chase, communicating approximate threat proximity
  without revealing the Killer's exact coordinate or route.
- Includes: Dead by Daylight heartbeat, Terror Radius music and chase layer in
  the blank-loadout standard Trial.
- Excludes: Killer-specific Undetectable or Lullaby exceptions; exact aura
  reading; ordinary spatial footsteps already covered by local sound.
- Parameters: source, radius, proximity bands, audio layers, chase state,
  listener role and suppression exceptions.
- Evidence: [Dead by Daylight decomposition](../games/a-f/dead-by-daylight.md).
- Novelty: not assessed.

## INF-173 — Killer-only transient tracks expose recent Survivor routes

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: recent running and injury leave spatial track cues visible to the
  Killer role but ordinarily hidden from Survivors, disclosing a fading route
  rather than the tracked Survivor's current exact position.
- Includes: Dead by Daylight Scratch Marks and Pools of Blood.
- Excludes: audible footsteps; public teammate HUD state; exact temporary aura
  revelation from a Perk.
- Parameters: cue class, source state, location, direction quality, role
  visibility, intensity, duration and decay.
- Evidence: [Dead by Daylight decomposition](../games/a-f/dead-by-daylight.md).
- Novelty: not assessed.

## INF-174 — Work progress and Skill Check window are visible

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: while a Survivor performs eligible work, the interface exposes
  current progress and, when sampled, a moving timing pointer with graded
  response zones plus immediate success or failure feedback.
- Includes: Dead by Daylight repair, healing, recovery, unhook and gate progress
  bars together with Good/Great Skill Check intervals.
- Excludes: hidden future prompt location; post-match score events; attack-
  timing cues without a continuing work bar.
- Parameters: interaction, progress, efficiency colour, pointer, success zones,
  warning, response grade and failure feedback.
- Evidence: [Dead by Daylight decomposition](../games/a-f/dead-by-daylight.md).
- Novelty: not assessed.

## INF-175 — Item panels expose rarity, affixes, requirements and comparison

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: inspecting ground, carried or equipped gear exposes its base and
  rarity, explicit modifiers, sockets and unmet requirements, with the relevant
  equipped alternative available for comparison.
- Includes: Path of Exile 2 equipment tooltips and comparison panels.
- Excludes: hidden future affix rolls; external trade valuation; an unlabelled
  item model with no statistics.
- Parameters: item identity, rarity, modifiers, sockets, requirements,
  comparison slot, deltas and unusable warning.
- Evidence: [Path of Exile 2 decomposition](../games/m-r/path-of-exile-2.md).
- Novelty: not assessed.

## INF-176 — Skill panels expose sockets, compatibility, cost and effect

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the Skills interface exposes each active Skill's assigned input,
  Support sockets and occupants, compatibility feedback, resource cost and the
  effect produced by the current composed Gem state.
- Includes: Path of Exile 2 active Skill and Support management.
- Excludes: hidden exact future damage outcomes; passive-tree topology; item
  affixes unrelated to the selected Skill.
- Parameters: Skill, input, sockets, Supports, tags, cost, damage or utility
  summary, warnings and resulting changes.
- Evidence: [Path of Exile 2 decomposition](../games/m-r/path-of-exile-2.md).
- Novelty: not assessed.

## INF-177 — Passive tree exposes connections, effects and available points

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the character-development view exposes current allocated nodes,
  adjacent reachable nodes, each inspected node's effect, unspent points and
  the declared refund cost so the next connected allocation is attributable.
- Includes: Path of Exile 2 Passive Skill Tree in the scoped campaign.
- Excludes: hidden optimal builds; the active Skill socket panel; account-wide
  Atlas progression.
- Parameters: root, allocated and adjacent nodes, effect text, point count,
  refund currency and confirmation.
- Evidence: [Path of Exile 2 decomposition](../games/m-r/path-of-exile-2.md).
- Novelty: not assessed.

## INF-178 — Broadcast play view identifies ball, control and local team shape

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the live broadcast-style play view keeps the shared ball, the
  current direct-control marker, the nearby members of both sides, the playing
  surface's decision-relevant markings and fixtures, and the context for the
  next eligible control or ball action readable before that action is taken.
- Includes: broadcast camera, player indicator and local formation shape in EA
  SPORTS FC 26; NBA 2K26's scoped Play Now court, players, ball, baskets,
  boundaries and control marker.
- Excludes: permanent omniscient member attributes; a manager-only or external
  tactical board; post-match heat maps; omniscient future routes; broadcast
  decoration that carries no state.
- Parameters: sport and playing surface, camera and zoom, region, markings,
  scoring fixtures, boundaries, ball state, controlled actor and marker,
  teammates and opponents, radar availability, labels, occlusion and any
  suggested-switch cue.
- Evidence: [EA SPORTS FC 26 decomposition](../games/a-f/ea-sports-fc-26.md).
- Additional support: [NBA 2K26 decomposition](../games/m-r/nba-2k26.md), for a
  two-basket court whose ball alternates between carried and free states.
- Novelty: first isolated for `GAME-0163`; generalised by
  [`TAXONOMY_CHANGE_019`](../../research/taxonomy-changes/TAXONOMY_CHANGE_019.md)
  — the disclosure is the live readable relation between ball, control locus
  and local team shape, and the playing surface is a parameter.

## INF-179 — Current field or room exposes threats, interactables and exits

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the current field or room view exposes the controlled actor,
  visible threats, hazards, obstacles, interactables, pickups and exit states
  needed to choose the next movement, interaction, attack or resource action.
- Includes: ordinary base-Rebirth room play and boss encounters; Final Fantasy
  VII's current pre-rendered field with the optional position/exit pointers,
  nearby actors, fixtures, ladders and pickups.
- Excludes: concealed adjacent-room contents; exact hidden drop rolls; an
  external item-description overlay.
- Parameters: field or room bounds, actor, projectile, hazard, obstacle,
  interactable, pickup, exit or door, pointer, boss bar and visual effect.
- Evidence: [The Binding of Isaac: Rebirth decomposition](../games/s-z/the-binding-of-isaac-rebirth.md).
- Additional support: [Final Fantasy VII decomposition](../games/a-f/final-fantasy-vii.md),
  using the original PlayStation manual's field-control and exit-indicator rules.
- Additional support: [Chrono Trigger decomposition](../games/a-f/chrono-trigger.md),
  for the current field exposing party members, Gato, booths, pickups, Telepods
  and the exits required by the scoped fair route.
- Novelty: first isolated for `GAME-0164`; existing partial-opponent sight genes
  do not expose a complete bounded room's shared projectile field and exits.

## INF-180 — Explored map retains room graph and disclosed room roles

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the minimap retains every discovered room cell and connection on
  the current floor and marks the identity of eligible disclosed special rooms
  without revealing all unexplored contents.
- Includes: base-Rebirth explored ordinary, Treasure, Shop and boss room map
  state; Blue Prince's current drafted manor rooms and doorway graph.
- Excludes: a fully revealed future floor; a non-spatial branching act-node
  chart; secret rooms not yet disclosed by an eligible effect or entry.
- Parameters: cell, adjacency, explored state, current room, room-role icon,
  concealment and map-reveal effect.
- Evidence: [The Binding of Isaac: Rebirth decomposition](../games/s-z/the-binding-of-isaac-rebirth.md)
  and [Blue Prince decomposition](../games/a-f/blue-prince.md).
- Additional support: [Dead Cells decomposition](../games/a-f/dead-cells.md),
  for the explored biome map with shop, treasure and teleporter marks.
- Novelty: first isolated for `GAME-0164`.

## INF-181 — Horse interface exposes bond, condition and saddle cargo

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: horse HUD, wheel and management views expose the current horse's
  identity, health, stamina, bond, active saddle and accessible weapon, outfit
  or carcass cargo before a riding or transfer decision.
- Includes: Arthur's current horse during the scoped Chapter 2 route.
- Excludes: hidden wild-horse traits before inspection; motor-vehicle state;
  cosmetic horse appearance with no mechanical value.
- Parameters: horse, health, stamina, core, bond, saddle, cargo slot, carried
  weapon, outfit and call state.
- Evidence: [Red Dead Redemption 2 decomposition](../games/m-r/red-dead-redemption-2.md).
- Novelty: first isolated for `GAME-0165`.

## INF-182 — Legal and honour interface exposes report and consequence state

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: contextual prompts, minimap marks and status displays disclose
  an active witness and identification state, reported crime, law search,
  regional bounty and current honour movement or band before the next response.
- Includes: scoped Chapter 2 witness, wanted, bounty and honour feedback.
- Excludes: exact hidden future witness compliance; undisclosed law spawns;
  companion-specific affinity.
- Parameters: witness marker, identity, report phase, search area, bounty,
  jurisdiction, honour change, band and contextual prompt.
- Evidence: [Red Dead Redemption 2 decomposition](../games/m-r/red-dead-redemption-2.md).
- Novelty: first isolated for `GAME-0165`.

## INF-183 — Camp ledger exposes shared funds, supplies and upgrades

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the donation ledger and camp status icons expose recent
  contributions, shared balance, medicine, ammunition and food supply state,
  offered restocks, upgrade prerequisites, prices and purchased effects.
- Includes: the unlocked Horseshoe Overlook camp ledger during Chapter 2.
- Excludes: Arthur's private wallet alone; hidden future gang donations;
  flavour-only camp decoration with no registered effect.
- Parameters: contribution, balance, category, stock band, offer, predecessor,
  price, purchase and service effect.
- Evidence: [Red Dead Redemption 2 decomposition](../games/m-r/red-dead-redemption-2.md).
- Novelty: first isolated for `GAME-0165`.

## INF-184 — Explored hex map retains terrain, resources and borders

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: the world view retains every explored hex's known terrain,
  features, disclosed resources, improvements, districts, roads and borders
  while distinguishing current visibility from remembered fog.
- Includes: the scoped seeded Pangaea map in Civilization VI.
- Excludes: exact contents of never-seen fog; hidden rival orders; a room minimap.
- Parameters: hex, exploration, visibility, terrain, feature, resource,
  improvement, road, district and owner.
- Evidence: [Sid Meier's Civilization VI decomposition](../games/s-z/sid-meiers-civilization-vi.md).
- Novelty: first isolated for `GAME-0166`.

## INF-198 — Quick-job market exposes supplied contract terms

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: before acceptance, the market exposes each current offer's cargo,
  origin, destination, route distance, deadline, advertised income and supplied
  vehicle needed to compare one employer job with another.
- Includes: Euro Truck Simulator 2 Quick Jobs.
- Excludes: owned-truck Freight Market costs; undisclosed future offers; an
  autonomous employee's completed-job log.
- Parameters: offer, cargo, weight, origin, destination, distance, deadline,
  income, truck, trailer and expiration.
- Evidence: [Euro Truck Simulator 2 decomposition](../games/a-f/euro-truck-simulator-2.md).
- Novelty: first isolated for `GAME-0169`; earlier job displays do not expose a
  complete supplied direct-drive cargo contract.

## INF-199 — Driving widgets expose vehicle, damage and rest state

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: the live driving interface exposes current speed, selected gear,
  fuel, Rest State, time until Mandatory Break and separate truck, trailer and
  cargo damage needed to decide whether and how to continue the haul.
- Includes: Euro Truck Simulator 2 update 1.60 widgets and Quick Info.
- Excludes: exact future traffic; hidden internal component values below the
  interface boundary; post-delivery reward settlement.
- Parameters: speed, gear, fuel, rest state, break time, truck damage, trailer
  damage, cargo damage, malfunction and widget visibility.
- Evidence: [Euro Truck Simulator 2 decomposition](../games/a-f/euro-truck-simulator-2.md).
- Novelty: first isolated for `GAME-0169`; earlier vehicle HUD genes do not join
  articulated cargo condition to separate physiological and legal rest clocks.

## INF-200 — Job and GPS widgets expose delivery progress

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: during an active delivery, the interface exposes cargo type and
  weight, destination, advertised income, remaining completion time, estimated
  arrival, remaining travel time and route distance.
- Includes: Euro Truck Simulator 2 update 1.60 Job Details and GPS widgets.
- Excludes: exact future traffic delay; a job-market offer not yet accepted;
  final deductions and experience after delivery.
- Parameters: cargo, weight, destination, income, deadline remainder, arrival
  day and time, travel time, distance and route recalculation.
- Evidence: [Euro Truck Simulator 2 decomposition](../games/a-f/euro-truck-simulator-2.md).
- Novelty: first isolated for `GAME-0169`; earlier route views do not combine a
  live cargo contract's economic terms with ETA and deadline slack.

## INF-201 — Delivery results expose one-job settlement

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `Medium`
- Definition: after delivery, the results interface exposes the completed job's
  evaluation, settled income, eligible time or damage adjustments, parking
  experience and resulting profile credit.
- Includes: Euro Truck Simulator 2 Quick Job result screen.
- Excludes: live GPS state before drop-off; recurring company profit; a traffic
  fine notification already applied on the road.
- Parameters: evaluation, base income, adjustments, paid income, base
  experience, parking experience and profile totals.
- Evidence: [Euro Truck Simulator 2 decomposition](../games/a-f/euro-truck-simulator-2.md).
- Novelty: first isolated for `GAME-0169`; earlier summaries do not expose the
  economic and experience settlement of one directly driven cargo contract.

## INF-202 — HUD exposes survival pressure and quick-use state

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: the live interface exposes health, stamina, bleeding, hunger,
  overload and radiation pressure together with selected weapon ammunition and
  four assigned quick-use slots.
- Includes: the scoped S.T.A.L.K.E.R. 2 HUD and inventory weight indication.
- Excludes: hidden future damage; undiscovered loot; all downstream consequences
  of a dialogue choice.
- Parameters: health, stamina, effect icon, radiation meter, load colour,
  quick slot, weapon, magazine, reserve and fire mode.
- Evidence: [S.T.A.L.K.E.R. 2 decomposition](../games/s-z/stalker-2-heart-of-chornobyl.md).
- Novelty: first isolated for `GAME-0170`; it joins radiation and overload with
  the immediate first-person treatment and ammunition interface.

## INF-203 — Detector signal exposes artifact proximity

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: an active detector communicates changing direction or distance to
  a nearby hidden artifact and marks the critical range at which it can appear.
- Includes: Echo Detector signal cadence during both scoped artifact searches.
- Excludes: revealing the artifact's future sampled identity; showing ordinary
  ground loot; an external walkthrough coordinate.
- Parameters: detector model, direction, distance, signal cadence, critical
  range, artifact class and manifestation state.
- Evidence: [S.T.A.L.K.E.R. 2 decomposition](../games/s-z/stalker-2-heart-of-chornobyl.md).
- Novelty: first isolated for `GAME-0170`; the signal is a continuous local
  measurement that precedes visual access to its target.

## INF-195 — Expose the partial mission route through map and markers

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: the live HUD shows the locally revealed portion of the assembled
  mission map, the player, nearby contacts and the current objective or
  extraction marker without revealing every unopened branch.
- Includes: minimap and white/yellow objective guidance in Awakening and Vor's
  Prize.
- Excludes: the full future tile graph; Navigation's planetary node selection;
  an external walkthrough route.
- Parameters: revealed tiles, player position, contacts, objective, extraction,
  marker colour, distance and occlusion.
- Evidence: [Warframe decomposition](../games/s-z/warframe.md).
- Novelty: first isolated for `GAME-0168`; existing maps do not expose a
  progressively revealed generated route plus its current mission endpoint.

## INF-196 — Expose equipment ranks, Mod slots and resulting statistics

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: the Arsenal and upgrade interface show selected equipment,
  separate ranks, compatible Mod slots, capacity, polarities, drain and the
  resulting statistic changes before live play resumes.
- Includes: starter Warframe and weapon configuration in Vor's Prize.
- Excludes: hidden damage formulas; unidentified future drops; cosmetic-only
  appearance editing.
- Parameters: item, rank, statistics, slots, compatibility, capacity, polarity,
  drain, preview and validation feedback.
- Evidence: [Warframe decomposition](../games/s-z/warframe.md).
- Novelty: first isolated for `GAME-0168`; earlier equipment views do not expose
  this capacity-and-polarity modifier calculation.

## INF-197 — Expose mission rewards, Affinity changes and next quest state

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: mission completion and the returning Orbiter state show retained
  rewards, equipment Affinity/rank changes, restored functions and the next
  available opening-quest step.
- Includes: the Vor's Prize settlement loop from extraction back to Navigation,
  Arsenal, Foundry or Mod Station.
- Excludes: temporary ammunition; later quest spoilers; undisclosed random
  reward outcomes before extraction.
- Parameters: mission, pickups, reward, Affinity, ranks, segment, quest step,
  next mission and presentation timing.
- Evidence: [Warframe decomposition](../games/s-z/warframe.md).
- Novelty: first isolated for `GAME-0168`; earlier result screens do not combine
  retained equipment growth with restoration of a persistent tutorial hub.

## INF-192 — Side-scrolling viewport exposes local obstacle lookahead

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the running side view exposes the controlled body, current
  support and a bounded forward slice of blocks, gaps, hazards, transitions
  and optional routes, while later authored geometry remains outside the
  viewport.
- Includes: the moving Stereo Madness playfield in cube and ship sections;
  the directly steered World 1-1 viewport in original Super Mario Bros.
- Excludes: simultaneous disclosure of the full level; editor view; hidden
  collision objects; a minimap that reveals the entire future route.
- Parameters: camera anchor, automatic or commanded horizontal travel, forward
  margin, viewport width, scroll speed, object classes, occlusion and contrast.
- Evidence: [Geometry Dash decomposition](../games/g-l/geometry-dash.md) and
  [Super Mario Bros. decomposition](../games/s-z/super-mario-bros.md).
- Additional support: [Battletoads decomposition](../games/a-f/battletoads.md),
  for the bounded side-view canyon slice, support, gap and forward threat
  lookahead rather than disclosure of the complete stage.
- Novelty: first isolated for `GAME-0167`; `INF-001` requires every
  decision-relevant current-board element to be inspectable, whereas this
  auto-run deliberately reveals only a live local horizon.

## INF-193 — Attempt, current progress, best percentage and Secret Coin state are visible

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the level interface identifies the current attempt, exposes
  proportional current route progress and the retained best reached percentage,
  and reports contacted or persistently credited Secret Coins and completion
  feedback without revealing future geometry.
- Includes: Stereo Madness attempt counter, current progress percentage/bar,
  retained best percentage, coin feedback and 100% completion presentation
  under the scoped UI settings.
- Excludes: an external speedrun overlay; user-level leaderboards; exact future
  obstacle timing; account-wide achievement statistics.
- Parameters: attempt number, current percentage, retained best percentage,
  percentage precision, bar visibility, coin slots, pending versus credited
  state and completion banner.
- Evidence: [Geometry Dash decomposition](../games/g-l/geometry-dash.md).
- Novelty: first isolated for `GAME-0167`; earlier progress interfaces report
  work, mission or tournament state rather than clean-retry route execution.

## INF-194 — Soundtrack and pulses cue the authored obstacle cadence

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the fixed soundtrack and synchronised visual pulses provide
  recurring temporal cues for the authored obstacle sequence, letting learned
  input timing be aligned before the corresponding geometry reaches the icon.
- Includes: Stereo Madness's fixed music, colour pulses and repeated route timing.
- Excludes: a song selected independently of level geometry; metronome scoring
  that grades presses against beats; music muted as a parameter.
- Parameters: song, offset, cue events, obstacle positions, audio latency,
  visual pulse, mute state and learned timing.
- Evidence: [Geometry Dash decomposition](../games/g-l/geometry-dash.md).
- Novelty: first isolated for `GAME-0167`; earlier audio-timing genes telegraph
  hostile attacks rather than one replayed platform route.

## INF-185 — City panel exposes yields, growth, production and citizens

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: the city interface shows population, worked tiles and specialists,
  Food and growth, Housing, Amenities, current Production target/progress and
  the city's other yield contributions before reassignment.
- Includes: each Roman city in the scoped Civilization VI route.
- Excludes: hidden rival city values; empire diplomacy; district placement preview.
- Parameters: city, population, assignments, yields, food, growth, Housing,
  Amenities, production target and progress.
- Evidence: [Sid Meier's Civilization VI decomposition](../games/s-z/sid-meiers-civilization-vi.md).
- Novelty: first isolated for `GAME-0166`.

## INF-186 — District lens exposes legal hexes and adjacency preview

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: before placement, the map marks district-eligible and ineligible
  city hexes and exposes the adjacency yield predicted for each legal choice.
- Includes: Campus, Industrial Zone and Spaceport placement in Civilization VI.
- Excludes: hidden future resource spawns; citizen tile assignment; wonder animation.
- Parameters: city, district, hex, legality, terrain, occupancy, neighbours and adjacency.
- Evidence: [Sid Meier's Civilization VI decomposition](../games/s-z/sid-meiers-civilization-vi.md).
- Novelty: first isolated for `GAME-0166`.

## INF-187 — Government view exposes typed slots and policy effects

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: the government interface exposes available governments, their
  inherent effects and typed slot frames, plus unlocked policy cards, card
  effects, current assignments and incompatibility feedback.
- Includes: base-game policy configuration in Civilization VI.
- Excludes: hidden AI policies; expansion Governor promotions; civic-tree progress.
- Parameters: government, effects, slot types, cards, assignments, unlocks and warnings.
- Evidence: [Sid Meier's Civilization VI decomposition](../games/s-z/sid-meiers-civilization-vi.md).
- Novelty: first isolated for `GAME-0166`.

## INF-188 — Diplomacy view exposes relationships, agreements and war state

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: contacted-civilization views expose current relationship cues,
  available deal terms, active agreements, war/peace state, treaty gates and
  disclosed warmonger consequences before a diplomatic action.
- Includes: Greece, Egypt and Germany in the scoped game.
- Excludes: exact hidden future acceptance calculations; city-state envoy state;
  multiplayer chat.
- Parameters: rival, relationship, agenda feedback, deal terms, agreement,
  war, peace, timer and warmonger value.
- Evidence: [Sid Meier's Civilization VI decomposition](../games/s-z/sid-meiers-civilization-vi.md).
- Novelty: first isolated for `GAME-0166`.

## INF-189 — Trade view exposes capacity, destinations and route yields

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: trader selection shows used and available route capacity,
  eligible origin/destination pairs, predicted yields, duration and route state
  before the player commits a destination.
- Includes: domestic and international base-game trade routes.
- Excludes: diplomatic lump-sum trades; hidden hostile routes; manual road planning.
- Parameters: capacity, trader, origin, destination, path, yields, duration and trading post.
- Evidence: [Sid Meier's Civilization VI decomposition](../games/s-z/sid-meiers-civilization-vi.md).
- Novelty: first isolated for `GAME-0166`.

## INF-190 — Unit interface exposes movement, actions and combat forecast

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: selecting a unit exposes remaining movement, health, strength,
  available commands, reachable hexes and the declared forecast for an eligible
  attack before commitment.
- Includes: Roman civilian, melee and ranged units in Civilization VI.
- Excludes: exact hidden random damage; city production choices; rival future orders.
- Parameters: unit, movement, health, strength, commands, range, target and forecast.
- Evidence: [Sid Meier's Civilization VI decomposition](../games/s-z/sid-meiers-civilization-vi.md).
- Novelty: first isolated for `GAME-0166`.

## INF-191 — Victory view exposes science milestones and rival progress

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: the victory interface shows Rome's completed and outstanding
  Science milestones and disclosed progress by each rival toward the enabled
  terminal, allowing the remaining launch race to be compared.
- Includes: Satellite, Moon Landing and three Mars modules in the scoped route.
- Excludes: disabled victory conditions; exact future completion turns;
  Gathering Storm exoplanet speed.
- Parameters: civilization, enabled victory, milestone, completion, rival
  comparison and terminal state.
- Evidence: [Sid Meier's Civilization VI decomposition](../games/s-z/sid-meiers-civilization-vi.md).
- Novelty: first isolated for `GAME-0166`.

## INF-204 — Driving HUD exposes speed, gear and route guidance

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the live driving view exposes current speed and gear together
  with the authored or waypoint route cues needed to judge braking and steering.
- Includes: Forza Horizon 6 speedometer, gear, minimap/GPS and configurable
  driving line in the scoped opening; Need for Speed Unbound speed, gear and
  `Shopping Spree` route cues; Need for Speed Payback speed, gear, minimap and
  Highway Heist route cues; Trackmania `Summer 2026 - 01` speed, gear and
  authored road/waypoint guidance; Need for Speed Underground's opening
  Circuit speed, gear, road shape and route arrows.
- Excludes: event eligibility before entry; hidden future traffic; post-event
  settlement.
- Parameters: speed, gear, route, minimap, driving line, braking cue, waypoint
  and camera.
- Evidence: [Forza Horizon 6 decomposition](../games/a-f/forza-horizon-6.md) and
  [Need for Speed Payback decomposition](../games/m-r/need-for-speed-payback.md),
  [Trackmania decomposition](../games/s-z/trackmania.md), and
  [Need for Speed Underground decomposition](../games/m-r/need-for-speed-underground.md).
- Additional support: [Forza Horizon 5 decomposition](../games/a-f/forza-horizon-5.md),
  for the live speed, gear and driving-line surface in a fixed Solo circuit.
- Additional support: [Mario Kart 8 Deluxe decomposition](../games/m-r/mario-kart-8-deluxe.md),
  for course geometry and speed feedback across road, glider and anti-gravity
  sections.
- Additional support: [Gran Turismo decomposition](../games/g-l/gran-turismo.md),
  for speed, gear and stopping-area cues in original licence B-1.
- Novelty: first isolated for `GAME-0171`; cargo-driving widgets join speed to
  fuel, rest and damage rather than a race-oriented guidance layer.

## INF-205 — Race HUD exposes position, course progress and nearby rivals

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: during a driving event, the interface exposes current place or
  timed target, lap/checkpoint progress, elapsed or remaining time and locally
  sensed rival vehicles needed to revise the racing line.
- Includes: Forza Horizon 6 Festival races and Time Attack in the scoped route,
  including configurable Proximity Radar; Need for Speed Unbound place,
  progress and seven-rival race surface; Trackmania `Summer 2026 - 01`
  checkpoint/course progress, running time and fixed timed target without
  rivals; Need for Speed Underground's place, four-car field, lap, elapsed
  time and nearby rivals in the opening Circuit.
- Excludes: omniscient future rival paths; free-roam traffic with no event
  result; the final reward panel.
- Parameters: position, participant count, lap, checkpoint, time, split,
  proximity direction, distance and audio cue.
- Evidence: [Forza Horizon 6 decomposition](../games/a-f/forza-horizon-6.md),
  [Trackmania decomposition](../games/s-z/trackmania.md), and
  [Need for Speed Underground decomposition](../games/m-r/need-for-speed-underground.md).
- Additional support: [Forza Horizon 5 decomposition](../games/a-f/forza-horizon-5.md),
  for live place, lap/checkpoint progress, time and nearby Drivatars.
- Additional support: [Mario Kart 8 Deluxe decomposition](../games/m-r/mario-kart-8-deluxe.md),
  for current place, lap, course progress and nearby CPU karts.
- Additional support: [Gran Turismo decomposition](../games/g-l/gran-turismo.md),
  for the running clock and fixed test target without a rival field.
- Novelty: first isolated for `GAME-0171`; prior opponent HUD genes do not join
  course progress to vehicle proximity and race position.

## INF-206 — Map and event card expose driving-event terms

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: the world map and selected event panel disclose its location,
  type, route form, current unlock, vehicle eligibility and available reward or
  campaign contribution before entry.
- Includes: the six exposed Horizon Qualifiers and first Horizon Invitational;
  Need for Speed Unbound's A+ `Shopping Spree` class, `$0` buy-in, payout table,
  displayed reward and Heat gain; Need for Speed Payback's Story mission, Race
  class and displayed `LV180` entry terms; Need for Speed Underground's Race 1
  Circuit, Olympic Square, two-lap, difficulty and Bank terms; Mario Kart 8
  Deluxe's 150 cc Mushroom Cup, fixed course set, vehicle packet and assistance
  state.
- Excludes: undiscovered optional content; live race position; post-completion
  Race Customizer options unavailable on first play.
- Parameters: marker, location, event type, route, car theme, class, unlock,
  progress value and reward.
- Evidence: [Forza Horizon 6 decomposition](../games/a-f/forza-horizon-6.md),
  [Need for Speed Payback decomposition](../games/m-r/need-for-speed-payback.md),
  and [Need for Speed Underground decomposition](../games/m-r/need-for-speed-underground.md).
- Novelty: first isolated for `GAME-0171`; generic mission maps do not expose
  one driving event's course and car-entry contract.

## INF-207 — Expose retained progression and its next threshold-gated successor

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: before the next commitment, the interface exposes one retained
  progression measure, its required threshold and whether the corresponding
  authored successor is still locked or now available.
- Includes: the Qualifier meter and first Horizon Invitational state in Forza
  Horizon 6; the Resistance Point meter and successor-region state in Far Cry
  5's scoped tutorial-island route.
- Excludes: a personal experience bar; a mission list with no shared measure; a
  score shown only after settlement; a hidden threshold; reward rolls whose
  gate state is not disclosed.
- Parameters: current amount, exact or proportional presentation, threshold,
  remaining amount, successor identity, lock state and interface styling.
- Evidence: [Forza Horizon 6 decomposition](../games/a-f/forza-horizon-6.md)
  and [Far Cry 5 decomposition](../games/a-f/far-cry-5.md).
- Additional support: [Cities: Skylines II decomposition](../games/a-f/cities-skylines-ii.md),
  for the milestone bar that exposes the city's current progression measure,
  the requirement for the next milestone and what that milestone will release.
- Novelty: first isolated for `GAME-0171`; generalised and given a second
  mechanically distinct carrier under
  [`TAXONOMY_CHANGE_033`](../../research/taxonomy-changes/TAXONOMY_CHANGE_033.md).

## INF-208 — Driving-event results expose performance and retained rewards

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: after a valid finish and any declared post-result settlement, the
  results transition exposes place, time or rating, earned progress and any
  credits, experience, vehicles or campaign unlocks retained from that event.
- Includes: Forza Horizon 6 Qualifier and first-Wristband settlement panels;
  Need for Speed Unbound's classified finish and post-pursuit garage result;
  Need for Speed Payback's retained mission and Chapter 2 completion result;
  Need for Speed Underground's first-place result, credited Bank and retained
  Race 1 completion.
- Excludes: live HUD values before the finish; an unclaimed Playlist reward;
  hidden future Wheelspin outcomes.
- Parameters: event, position, time, stars, points, credits, experience, vehicle
  and unlock.
- Evidence: [Forza Horizon 6 decomposition](../games/a-f/forza-horizon-6.md),
  [Need for Speed Payback decomposition](../games/m-r/need-for-speed-payback.md),
  and [Need for Speed Underground decomposition](../games/m-r/need-for-speed-underground.md).
- Additional support: [Forza Horizon 5 decomposition](../games/a-f/forza-horizon-5.md),
  for the classified result and retained ordinary-race reward transition.
- Additional support: [Mario Kart 8 Deluxe decomposition](../games/m-r/mario-kart-8-deluxe.md),
  for per-race points, cumulative standings, trophy and star class.
- Novelty: first isolated for `GAME-0171`; delivery results expose contract
  damage and pay, not competitive driving performance and festival progress.

## INF-209 — Side-view fighters expose spacing and live combat state

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the shared side view keeps both combatant bodies, their relative
  distance, facing, pose and current hit, guard, armour, airborne, knockdown or
  wake-up state perceptible during the live exchange.
- Includes: Ryu and Luke in the scoped Street Fighter 6 Versus arena.
- Excludes: exact hidden frame numbers; an off-screen opponent; only a roster
  portrait or post-round result; a team minimap.
- Parameters: camera framing, body pose, facing, distance, contact effect,
  airborne state, knockdown and wake-up animation.
- Evidence: [Street Fighter 6 decomposition](../games/s-z/street-fighter-6.md).
- Additional support: [Brawlhalla decomposition](../games/a-f/brawlhalla.md),
  for two continuously framed fighters, their spacing, pose, facing, airborne
  state and live contact trajectory.
- Additional support: [TEKKEN 8 decomposition](../games/s-z/tekken-8.md),
  for the side view that keeps both fighters' bodies, distance, facing and
  pose in frame (a community wiki's perspective field and one inspected
  official static Game Screen frame) with the current hit state readable
  through attack start-up and the publisher's post-contact indicators;
  guard, armour, airborne, wall, knockdown and wake-up visibility is not
  separately evidenced and is not asserted for this carrier, and continuity
  between frames is inferred rather than observed, so the instance is
  graded `Limited`.
- Novelty: first isolated for `GAME-0172`; existing combat information genes
  expose party panels, target resources or telegraphs without making the whole
  fixed-opponent spacing state continuously visible in one shared plane.

## INF-210 — Duel HUD exposes paired vitality, shared-resource state, clock and round score

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: one live fighting HUD simultaneously exposes each participant's
  vitality, including any declared recoverable or temporary overlay, and the
  state of each shared combat resource, together with the shared round timer
  and accumulated round markers.
- Includes: the ordinary Street Fighter 6 Fighting Ground HUD with vitality,
  Drive state and Super Art stock; the TEKKEN 8 battle screen with each
  Health Gauge and its Recoverable Gauge, each Heat gauge and Heat Timer,
  Rage indication, the Time Limit and the Rounds Won markers.
- Excludes: hidden frame data; ranked points; a team-objective scoreboard;
  post-match progression or lobby profile information.
- Parameters: participants, vitality, recoverable or temporary overlay,
  shared resource gauges, states and timers, round timer, round markers, hit
  notices and current control-type icon.
- Evidence: [Street Fighter 6 decomposition](../games/s-z/street-fighter-6.md).
- Additional support: [TEKKEN 8 decomposition](../games/s-z/tekken-8.md),
  for paired Health Gauges with Recoverable Gauges, Heat gauges and timers,
  Rage indication, the Time Limit and the Rounds Won markers, plus the
  post-contact PUNISH, CLEAN, COUNTER and TORNADO notices and combo count as
  the hit-notice parameter.
- Novelty: first isolated for `GAME-0172`; generalised by
  [`TAXONOMY_CHANGE_046`](../../research/taxonomy-changes/TAXONOMY_CHANGE_046.md)
  so that the displayed shared resources are parameters; earlier match HUD genes aggregate
  teams and shared objectives rather than two opposed fighter resources and
  short-round progress.

## INF-211 — Room draft exposes topology, type, cost and effect

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: before one room-plan commitment, every offered card discloses
  enough of its doorway topology, room identity or type, current cost and
  declared effect for the player to compare the alternatives.
- Includes: Blue Prince's three-plan doorway offer.
- Excludes: hidden future room contents not stated by the card; the explored
  manor map; a shop item offer unrelated to topology.
- Parameters: offer member, room name/type, doorway diagram, cost, rarity,
  effect text and placement warning.
- Evidence: [Blue Prince decomposition](../games/a-f/blue-prince.md).
- Novelty: first isolated for `GAME-0173`; one interface jointly previews a
  candidate's graph shape and rule/economy effect before spatial instantiation.

## INF-212 — Manor HUD exposes daily resources and held items

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the persistent exploration interface exposes current remaining
  steps, keys, gems, coins and eligible held-item state before a route, draft,
  purchase or fixture decision.
- Includes: the scoped Blue Prince manor HUD.
- Excludes: permanent clues visible only in their rooms; undisclosed future
  offers; a generic health-only HUD.
- Parameters: steps, keys, gems, coins, item slots, modifiers and day.
- Evidence: [Blue Prince decomposition](../games/a-f/blue-prince.md).
- Novelty: first isolated for `GAME-0173`; it exposes the coupled route and
  room-draft economy in one daily-state panel.

## INF-213 — Current drafted room exposes doors, interactables and clues

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the current instantiated room makes its available exits,
  addressed fixtures, collectible or purchasable items, room effects and
  discoverable clue surfaces perceptible before interaction.
- Includes: ordinary explored rooms in Blue Prince.
- Excludes: every hidden manor secret; future room offers; only the abstract map
  icon without the room scene.
- Parameters: room, doors, lock state, fixture, item, shop offer, clue surface,
  effect and inspection state.
- Evidence: [Blue Prince decomposition](../games/a-f/blue-prince.md).
- Novelty: first isolated for `GAME-0173`; the scene view connects one drafted
  graph node to its local route, economy and evidence affordances.

## INF-214 — Observation network exposes device-bounded team intelligence

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: each surviving observation device exposes only its current field,
  motion and supported markings to eligible teammates, with feed availability
  and loss visible before an information decision.
- Includes: Rainbow Six Siege attacker drone and defender camera feeds, scans
  and pings.
- Excludes: omniscient enemy positions; direct avatar sight; post-match replay.
- Parameters: device, field, movement, observed entity, scan, ping, recipients,
  signal and destruction state.
- Evidence: [Rainbow Six Siege decomposition](../games/s-z/tom-clancys-rainbow-six-siege.md).
- Novelty: first isolated for `GAME-0174`; the shared information boundary is
  indexed by a controllable, destructible network node.

## INF-215 — Local surfaces expose material, fortification and breach state

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: visible geometry and feedback distinguish relevant soft,
  barricaded, reinforced, damaged and opened states sufficiently to choose a
  compatible line of fire, fortification or breach action.
- Includes: Rainbow Six Siege walls, hatches, doors, windows and their current
  reinforcement or opening state.
- Excludes: a complete hidden structural map; cosmetic damage that cannot alter
  sight, cover, penetration or access.
- Parameters: surface, material, layer, damage, opening, penetration, side,
  sound and compatible tool cue.
- Evidence: [Rainbow Six Siege decomposition](../games/s-z/tom-clancys-rainbow-six-siege.md).
- Novelty: first isolated for `GAME-0174`; mutable material state is itself a
  decision-visible tactical information surface.

## INF-216 — Squad view exposes availability, condition, attributes and role suitability

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: before lineup confirmation, the squad interface exposes each
  candidate's availability, current condition, relevant attributes and
  assessed suitability for positions and roles.
- Includes: Football Manager 26 squad selection and role star ratings.
- Excludes: hidden future development; scouting an unowned player; live match
  analytics after kick-off.
- Parameters: player, registration, injury, suspension, condition, attributes,
  position, role and suitability rating.
- Evidence: [Football Manager 26 decomposition](../games/a-f/football-manager-26.md).
- Novelty: first isolated for `GAME-0175`; it is the pre-commit evidence surface
  for assigning autonomous football agents.

## INF-217 — Tactical visualizer exposes possession shapes, roles and instructions

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: the tactics interface previews the team's distinct in-possession
  and out-of-possession formations, assigned roles and active instructions
  before the manager confirms them.
- Includes: Football Manager 26 dual-formation tactics visualizer.
- Excludes: a single decorative lineup image; hidden match-engine weights;
  direct player movement.
- Parameters: phase, formation, player positions, roles, duties, instructions,
  warnings and confirmation state.
- Evidence: [Football Manager 26 decomposition](../games/a-f/football-manager-26.md).
- Novelty: first isolated for `GAME-0175`; one planning surface exposes two
  coupled autonomous team states rather than one static formation.

## INF-218 — Manager match overview exposes live performance, analytics and advice

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: while the fixture runs, the management interface exposes score,
  clock, player condition and performance, event or spatial analytics and
  contextual staff recommendations before an intervention.
- Includes: Football Manager 26 Match Overview, xG and staff advice.
- Excludes: omniscient future events; direct avatar sight as the only evidence;
  post-season statistics.
- Parameters: score, clock, rating, condition, events, xG, spatial view,
  recommendation, urgency and match phase.
- Evidence: [Football Manager 26 decomposition](../games/a-f/football-manager-26.md).
- Novelty: first isolated for `GAME-0175`; it joins autonomous simulation
  evidence to a bounded live policy-revision interface.

## INF-219 — Fixture and competition table expose the recorded result

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: after settlement, the career interface exposes the fixture's
  final score and outcome together with the resulting competition-table state.
- Includes: Football Manager 26 match result and Premier League table.
- Excludes: an in-match provisional score; predicted standings; hidden future
  fixtures.
- Parameters: fixture, score, result, points, played, goal difference, rank and
  saved competition state.
- Evidence: [Football Manager 26 decomposition](../games/a-f/football-manager-26.md).
- Novelty: first isolated for `GAME-0175`; the information confirms that one
  autonomous match has entered a persistent competition ledger.

## INF-220 — Tactical HUD exposes soldier authority, cover and attack odds

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: for the selected soldier the tactical interface exposes health,
  remaining action authority, reachable movement bands, cover relationships,
  available commands and the displayed hit, damage and critical information
  for an eligible attack before commitment.
- Includes: XCOM 2 tactical soldier HUD and attack preview.
- Excludes: the hidden future random result; exact hostile policy weights;
  campaign-management panels.
- Parameters: selected soldier, health, Action Points, cells, cover, commands,
  target, hit chance, damage range and critical chance.
- Evidence: [XCOM 2 decomposition](../games/s-z/xcom-2.md).
- Novelty: first isolated for `GAME-0176`; one preview joins spatial defence,
  personal action budget and probabilistic attack consequence.

## INF-221 — Concealment and mission view expose detection risk and objective state

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: the tactical view marks squad concealment, currently observable
  hostile and detection information, the mission fixture and whether the
  sabotage and hostile-clearance requirements remain incomplete.
- Includes: XCOM 2 concealment indicators, detection tiles and Gatecrasher
  objective display.
- Excludes: hidden enemies outside current information; exact future pod path;
  strategy-layer objectives.
- Parameters: concealment, detection boundary, visible hostiles, objective
  marker, charge state, clearance state and mission result.
- Evidence: [XCOM 2 decomposition](../games/s-z/xcom-2.md).
- Novelty: first isolated for `GAME-0176`; it combines approach risk with a
  conjunctive mission terminal rather than exposing either alone.

## INF-222 — Car view exposes ball, field, boost and aerial state

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the live vehicle view exposes the controlled car, shared ball,
  nearby cars, arena markings, goal direction, current boost reserve and
  eligible aerial-state feedback sufficiently to choose the next movement or
  contact attempt.
- Includes: Rocket League car/ball camera, boost meter, teammate nameplates,
  ball indicator, field markings and optional flip-reset indicator.
- Excludes: hidden opponent inputs; guaranteed future ball trajectory;
  post-match replay analysis.
- Parameters: camera mode, car, ball, nameplate, goal direction, boost meter,
  velocity display, reset indicator and visible arena region.
- Evidence: [Rocket League decomposition](../games/m-r/rocket-league.md).
- Novelty: first isolated for `GAME-0177`; one view joins free ball geometry to
  vehicle orientation, finite thrust and resettable aerial authority.

## INF-223 — Interfaces expose scan, habitat and submersible safety state

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: contextual interfaces expose held scan progress and fragment count, current depth, habitat power and integrity, and occupied submersible energy, health and crush-depth warning before continued commitment.
- Includes: Subnautica Scanner ring and blueprint counter, Builder integrity feedback, Seabase power display and Seamoth HUD.
- Excludes: undiscovered fragment locations; exact future solar yield; hidden fauna paths.
- Parameters: target, scan progress, fragment count, depth, integrity, power, vehicle energy, vehicle health and crush warning.
- Evidence: [Subnautica decomposition](../games/s-z/subnautica.md).
- Novelty: first isolated for `GAME-0178`; observation, refuge and vehicle interfaces expose one continuous underwater safety chain.

## INF-224 — Strategic command view exposes economy, selection and production state

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: the live interface exposes the relevant owner stockpiles,
  capacity or technology tier where present, selected entities, their commands,
  health and active production or research progress before the next order.
- Includes: the Age of Empires II: Definitive Edition command panel and HUD;
  Command & Conquer credits, power, selection, health and production state;
  Stellaris empire resources, selected ships, orders, research and production.
- Excludes: hidden enemy stockpiles and queues; post-match statistics; a city turn's aggregate yield panel.
- Parameters: resource totals, capacity, technology tier, selection, hit points,
  command, production item, progress and availability state.
- Evidence: [Age of Empires II: Definitive Edition decomposition](../games/a-f/age-of-empires-ii-definitive-edition.md)
  [Command & Conquer Remastered Collection decomposition](../games/a-f/command-and-conquer-remastered-collection.md),
  and [Stellaris decomposition](../games/s-z/stellaris.md).
- Additional support: [StarCraft II decomposition](../games/s-z/starcraft-ii.md),
  for the command view exposing selection, health and available commands even
  though the scoped mission has no player economy or production.
- Additional support: [Warcraft III: Reign of Chaos decomposition](../games/s-z/warcraft-iii-reign-of-chaos.md),
  for the command view exposing selected-unit health and available orders in a
  scoped chapter without player economy or production.
- Novelty: first isolated for `GAME-0179` and generalised by
  `TAXONOMY_CHANGE_036`; a fixed number of stockpiles, population and an Age
  label are carrier parameters rather than the information boundary;
  `TAXONOMY_CHANGE_055` later removed the RTS-only genre label.

## INF-225 — Explored RTS terrain persists under current fog of war

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: explored terrain and last-known static geography remain visible on the world view and minimap, while current enemy units and changed hostile state are disclosed only inside active allied line of sight.
- Includes: normal reveal-map and fog-of-war state in Age of Empires II: Definitive Edition.
- Excludes: unexplored black map; omniscient spectator vision; invisibility detection layers; a hex-only turn-based map.
- Parameters: explored area, current visibility, terrain, resource memory, structure memory, enemy unit, vision source and minimap.
- Evidence: [Age of Empires II: Definitive Edition decomposition](../games/a-f/age-of-empires-ii-definitive-edition.md).
- Rejected carrier: [Command & Conquer Remastered Collection decomposition](../games/a-f/command-and-conquer-remastered-collection.md);
  its cumulative shroud discovery does not establish this current-sight boundary.
  See [the pinned source audit](../../research/normalisation/P2_CNC_VISIBILITY_SOURCE_AUDIT_001.json).
- Additional support: [StarCraft II decomposition](../games/s-z/starcraft-ii.md),
  for explored mission terrain persisting while hostile state outside current
  allied sight returns to fog.
- Additional support: [Warcraft III: Reign of Chaos decomposition](../games/s-z/warcraft-iii-reign-of-chaos.md),
  for explored prologue terrain persisting while live hostile occupancy beyond
  current allied sight returns to fog.
- Novelty: first isolated for `GAME-0179`; remembered generated terrain is separated from live enemy occupancy in a command-scale RTS view.

## INF-226 — Cockpit instruments expose flight and engine state

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: powered cockpit instruments expose current attitude, airspeed,
  altitude, heading, vertical speed, power, engine, fuel and warning state
  before the next manual control or configuration change.
- Includes: the scoped Microsoft Flight Simulator 2024 Cessna 172 G1000 PFD,
  engine display and cockpit annunciations.
- Excludes: exact future trajectory; external cinematic camera alone; route
  planning that omits current aircraft and engine state.
- Parameters: attitude, airspeed, altitude, heading, vertical speed, RPM,
  fuel, electrical status, flap/trim state, warning and update cadence.
- Evidence: [Microsoft Flight Simulator 2024 decomposition](../games/m-r/microsoft-flight-simulator-2024.md).
- Novelty: first isolated for `GAME-0180`; one powered cockpit surface joins
  aerodynamic energy, orientation and propulsion health for live correction.

## INF-227 — Avionics and EFB expose plan progress and conditions

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: compatible avionics and the electronic flight bag expose the
  selected aeronautical route, present aircraft position, active waypoint or
  leg, desired track, deviation, distance and declared flight conditions.
- Includes: the scoped Microsoft Flight Simulator 2024 Free Flight plan shared
  with the Cessna 172 G1000 and EFB.
- Excludes: automatic flight-control output; hidden future weather; a road-only
  GPS path or authored objective arrow without a flight plan.
- Parameters: origin, destination, waypoint, active leg, map, position, track,
  deviation, distance, weather, time and airport information.
- Evidence: [Microsoft Flight Simulator 2024 decomposition](../games/m-r/microsoft-flight-simulator-2024.md).
- Novelty: first isolated for `GAME-0180`; planning and cockpit navigation share
  a route state that informs but does not execute the manual flight.

## INF-228 — Map ballot exposes candidates, modes and vote state

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: the pre-match interface exposes three candidate maps with their
  game modes, the Random Map alternative and the player's current selectable
  vote before ballot settlement.
- Includes: current Overwatch Quick Play map-voting screen and Control label.
- Excludes: the hidden exact random roll; future ballot candidates; external
  map guides; hero-selection information.
- Parameters: map, mode, new/reworked tag, side icon, random option, own vote
  and ballot deadline.
- Evidence: [Overwatch decomposition](../games/m-r/overwatch.md).
- Novelty: first isolated for `GAME-0181`; the arena's mode is readable before
  a collective, partially probabilistic commitment.

## INF-229 — National focus, research and resource state are visible

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the national interface exposes the active focus, occupied and free
  research slots, progress, prerequisite access and top-level manpower,
  factories, fuel and political-resource state before time advances.
- Includes: the Italian national overview during the Hearts of Iron IV tutorial.
- Excludes: detailed equipment flow; map-local army state; hidden AI priorities.
- Parameters: focus, slot, technology, progress, manpower, factory counts, fuel,
  political resource, alert and tooltip.
- Evidence: [Hearts of Iron IV decomposition](../games/g-l/hearts-of-iron-iv.md).
- Novelty: first isolated for `GAME-0182`; several parallel national commitments
  share one visible strategic readiness layer.

## INF-230 — Construction, production and equipment flow are visible

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: inspectable industry panels expose construction priority and
  progress, production-line allocation, resource satisfaction, efficiency,
  output and national equipment surplus or deficit.
- Includes: Italian civilian construction, military production and logistics
  equipment views in the tutorial.
- Excludes: rail/hub supply reach; one division's combat bubble; external build
  guides.
- Parameters: project, factories, progress, line, equipment, resource, shortage,
  efficiency, daily output, stockpile and deficit.
- Evidence: [Hearts of Iron IV decomposition](../games/g-l/hearts-of-iron-iv.md).
- Novelty: first isolated for `GAME-0182`; national projects and portfolio lines
  expose both capacity assignment and downstream readiness consequences.

## INF-231 — Strategic map exposes armies, fronts and combat state

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the strategic map and army interface expose selected divisions,
  commanders, front and offensive lines, plan assignment/readiness, province
  control and current combat indicators.
- Includes: northern and southern Italian armies in the Ethiopian war.
- Excludes: current supply-network detail; exact concealed enemy composition;
  post-war map history.
- Parameters: division, army, commander, front, offensive line, assignment,
  planning, execution, province control, combat bubble and tooltip.
- Evidence: [Hearts of Iron IV decomposition](../games/g-l/hearts-of-iron-iv.md).
- Novelty: first isolated for `GAME-0182`; hierarchical agents and player-drawn
  persistent instruction geometry are readable in one live territorial view.

## INF-232 — Supply map exposes routes, reach and deficits

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: the logistics map exposes supply-capital routes, railway levels,
  hubs, motorisation, local reach, bottlenecks, demand and undersupplied fielded
  units before the player revises the theatre.
- Includes: Italian East African supply diagnosis in the tutorial war.
- Excludes: equipment production-line efficiency; hidden future sabotage;
  ordinary terrain vision alone.
- Parameters: capital, rail segment, level, hub, connection, motorisation,
  transport, reach, demand, delivered amount, bottleneck and deficit.
- Evidence: [Hearts of Iron IV decomposition](../games/g-l/hearts-of-iron-iv.md).
- Novelty: first isolated for `GAME-0182`; a multi-stage strategic delivery
  network is inspectable from national origin to local field penalty.

## INF-233 — Air-region interface exposes coverage and mission state

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `Medium`
- Definition: the air interface exposes wing composition, base, assigned region,
  range/coverage, enabled missions, efficiency, fuel-relevant readiness and
  current regional air result.
- Includes: Italian fighters and close air support assigned over Ethiopia.
- Excludes: directly piloted cockpit instruments; aircraft production output;
  hidden future enemy transfers.
- Parameters: wing, aircraft, base, region, range, coverage, mission, efficiency,
  fuel state, opposition and result.
- Evidence: [Hearts of Iron IV decomposition](../games/g-l/hearts-of-iron-iv.md).
- Novelty: first isolated for `GAME-0182`; a scheduled regional agent pool shows
  spatial eligibility and cross-system contribution without individual routing.

## INF-234 — War interface exposes surrender and settlement progress

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: map and war interfaces expose controlled victory points, country
  surrender progress, capitulation state and the immediate settlement that
  determines whether the bounded war has concluded.
- Includes: Ethiopian surrender and war conclusion in the official tutorial.
- Excludes: occupation resistance after annexation; hidden AI willingness;
  platform achievements.
- Parameters: participant, control, victory point, surrender limit, progress,
  capitulation, war status, settlement and outcome.
- Evidence: [Hearts of Iron IV decomposition](../games/g-l/hearts-of-iron-iv.md).
- Novelty: first isolated for `GAME-0182`; distributed territorial state is
  visibly aggregated into a country-level terminal meter and settlement.

## INF-235 — Live stage view exposes nearby threats, pickups and weapon effects

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: the playfield exposes the avatar, currently rendered enemies,
  boss chests, experience gems, stage items and active weapon effects within the
  camera region so movement can respond to local openings and hazards.
- Includes: normal Mad Forest play in Vampire Survivors.
- Excludes: exact off-screen enemy count; a complete future wave schedule;
  account collection menus.
- Parameters: camera region, avatar, enemy, pickup, chest, stage item, effect,
  damage feedback and occlusion.
- Evidence: [Vampire Survivors decomposition](../games/s-z/vampire-survivors.md).
- Additional support: [Battletoads decomposition](../games/a-f/battletoads.md),
  for visible local enemies, flies, Walker parts, Dragon ride state and boss
  rocks that support the next combat decision.
- Novelty: first isolated for `GAME-0183`; local spatial legibility is central
  even though attacks execute without aim or fire commands.

## INF-236 — Survival HUD exposes clock, level and run-build progression

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: the stage interface exposes the current survival clock, kill
  count, level and experience progress together with the retained weapon and
  passive-item build and any item levels available for inspection.
- Includes: the Vampire Survivors Mad Forest HUD and paused level-up/build views.
- Excludes: exact future level-up offers; concealed later waves; persistent
  collection unlocks outside the current run.
- Parameters: clock, kills, level, experience bar, health, weapon, passive,
  item level, pause screen and result.
- Evidence: [Vampire Survivors decomposition](../games/s-z/vampire-survivors.md).
- Novelty: first isolated for `GAME-0183`; one compact display joins fixed-time
  survival progress with a repeatedly drafted automatic-combat build.

## INF-237 — Arcade markers and aim aid expose a provisional firing solution

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: the Ground Arcade interface marks currently spotted enemy
  vehicles on the world view and minimap with identity and distance, predicts
  the shot's approximate impact point and colours the aimed armour location by
  estimated penetration chance without revealing a guaranteed outcome.
- Includes: visible ground-target markers and red, yellow or green penetration
  assistance in the scoped War Thunder match.
- Excludes: omniscient tracking of every enemy; the Realistic or Simulator
  interface; exact future dispersion, ricochet or internal damage.
- Parameters: spotting source, target, marker, minimap, identity, distance,
  predicted impact, armour point, penetration colour and uncertainty.
- Evidence: [War Thunder decomposition](../games/s-z/war-thunder.md).
- Novelty: first isolated for `GAME-0184`; shared detection and a local armour
  forecast jointly inform a shot while the true ballistic resolution remains
  partly hidden.

## INF-238 — Vehicle HUD exposes ammunition, reload and internal damage state

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the live ground-vehicle interface exposes the selected weapon and
  ammunition, current reload readiness and a damage panel for the active crew
  and functional modules so the player can adapt movement and firing authority.
- Includes: current ammunition/reload and crew, engine, gun or aiming damage in
  the scoped War Thunder Ground Arcade vehicle.
- Excludes: hidden opponent internals before a hit; hangar modification research;
  post-match economy and repair cost.
- Parameters: weapon, ammunition type, remaining rounds, reload, crew roles,
  module states, impairment, repair state and vehicle-loss warning.
- Evidence: [War Thunder decomposition](../games/s-z/war-thunder.md).
- Novelty: first isolated for `GAME-0184`; one directly controlled vehicle's
  combat authority is legible as several independently damaged internal parts
  rather than a single health meter.

## INF-239 — Card interface exposes hand, public zones and current rule objects

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the interface exposes the player's hand, both life totals,
  battlefield permanents, graveyards, current phase, priority prompts and the
  ordered stack, while card inspection reveals the full current rules text of
  visible objects and Arena highlights currently legal interactions.
- Includes: the scoped MTG Arena Arcane Aerialists match, including visible mana
  sources, attackers, blockers, targets and response stops.
- Excludes: opponent hand identities; concealed library order; unpublished
  matchmaking or opening-hand probabilities; collection and rank panels.
- Parameters: hand, life, battlefield, graveyard, exile, stack, phase, priority,
  card text, legal highlight and mana preview.
- Evidence: [Magic: The Gathering Arena decomposition](../games/m-r/magic-the-gathering-arena.md).
- Novelty: first isolated for `GAME-0185`; one digital rules interface exposes
  both public card zones and the currently unresolved rule queue without
  revealing the opponent's private resources.

## INF-240 — Survival HUD exposes sanity, thermal, light and partner danger

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: the live interface and world feedback expose personal health, hunger and sanity, current clock and season, thermal and darkness warnings, carried survival state and the nearby partner's embodied, injured or ghost condition.
- Includes: status icons, gain/loss arrows, screen and audio distortion, freezing warning, clock segments and visible partner ghost in scoped Don't Starve Together.
- Excludes: exact future weather or spawn outcomes; remote omniscient partner inventory; hidden world-generation seed.
- Parameters: health, hunger, sanity, temperature warning, light warning, clock, season, inventory, partner position, partner life state and ghost aura.
- Evidence: [Don't Starve Together decomposition](../games/a-f/dont-starve-together.md).
- Novelty: first isolated for `GAME-0186`; personal survival pressures and asymmetric cooperative life state are exposed together while future ecology remains uncertain.

## INF-241 — Personal explored map retains discovered procedural geography

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: each survivor's map records only geography, biomes, paths and marked fixtures discovered through that survivor's exploration and retains those observations for later route and rendezvous decisions.
- Includes: locating the Florid Postern, resources and the shared camp in the scoped generated Forest world.
- Excludes: revealing undiscovered terrain; a shared omniscient team map; caves or remote shards; exact future resource return.
- Parameters: survivor, explored region, terrain, biome, road, icon, fixture, camp, map view and retained observation.
- Evidence: [Don't Starve Together decomposition](../games/a-f/dont-starve-together.md).
- Novelty: first isolated for `GAME-0186`; cooperative routing begins from separately accumulated partial maps of one shared generated world.

## INF-242 — Duty HUD exposes party, enmity, casts and local danger

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: the live duty interface exposes party members and their health or
  statuses, the controlled player's relative enmity, selected-target health and
  cast progress, and authored local cues for imminent affected ground.
- Includes: the Sastasha Duty Support party list, enmity indicators, target cast
  bar, visible boss windups and affected-ground markers.
- Excludes: exact hidden enemy controller state; undisclosed future reward
  rolls; a complete walkthrough shown in the HUD; offscreen optional rooms.
- Parameters: party member, role, health, status, enmity rank, target, target
  health, cast, progress, ground region, cue channel and resolution time.
- Evidence: [FINAL FANTASY XIV Online decomposition](../games/a-f/final-fantasy-xiv-online.md).
- Novelty: first isolated for `GAME-0188`; one party-combat display connects
  ally survival, threat authority and spatially avoidable hostile timing.

## INF-243 — Lock motion and resistance expose angular proximity

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: during a lock attempt, pick pose, cylinder travel, resistance and
  break feedback disclose whether the current angle is nearer the concealed
  opening interval without revealing its exact value in advance.
- Includes: visual, motion and sound feedback from the scoped novice Helgen
  prison-cell lock in Skyrim Special Edition.
- Excludes: displaying the exact sweet-spot angle; a carried key label; a binary
  success/failure result with no intermediate feedback.
- Parameters: pick pose, cylinder travel, resistance, sound, vibration,
  break event, inferred direction and hidden interval.
- Evidence: [The Elder Scrolls V: Skyrim Special Edition decomposition](../games/s-z/the-elder-scrolls-v-skyrim-special-edition.md).
- Novelty: first isolated for `GAME-0190`; a consumable analog probe reveals
  graded proximity through the same motion that risks destroying it.

## INF-244 — Strategic view exposes force, settlement and objective state

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the strategic interface exposes the selected force's route and
  remaining movement, known terrain and fog, date, treasury/resources, owned
  settlement buildings or capacity, recruit stock, army composition, progression
  and current objective.
- Includes: the scoped campaign surfaces of Total War: WARHAMMER III and Heroes
  of Might and Magic III: Complete.
- Excludes: exact hidden hostile positions beyond current vision; battle-unit
  morale; an external walkthrough.
- Parameters: army, route, movement, map, fog, settlement, building, timer,
  treasury, mission, marker and known encounter.
- Evidence: [Total War: WARHAMMER III decomposition](../games/s-z/total-war-warhammer-iii.md).
- Novelty: first isolated for `GAME-0191`; one strategic display joins a
  persistent army allowance, slot-bound settlement queue and authored tutorial
  route before the battle instance exists.

## INF-245 — Battle view exposes formations, combat and morale

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the battle interface and world cues expose controlled unit
  positions, facing and formation, health or model loss, current orders,
  engagement, leadership and routing state, plus visible terrain and hostiles.
- Includes: deployment and live combat information in the first scoped Beacon
  battle of Total War: WARHAMMER III.
- Excludes: hidden enemy reserves; exact future damage; campaign treasury or
  construction state; post-battle statistics alone.
- Parameters: unit card, formation, facing, health, model count, order, target,
  terrain, leadership, routing, visibility and battle result.
- Evidence: [Total War: WARHAMMER III decomposition](../games/s-z/total-war-warhammer-iii.md).
- Novelty: first isolated for `GAME-0191`; regiment geometry and loss-sensitive
  morale remain decision-visible within one live command layer.

## INF-246 — Cooperative cues expose teammate danger and imminent pressure

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: teammate outlines, automatic character vocalisations and
  distinctive hostile or adaptive music cues disclose current separation,
  incapacitation, capture, nearby threat identity and short-term encounter
  pressure without revealing the exact future population or route sample.
- Includes: Left 4 Dead 2 Survivor silhouettes and calls for Special Infected,
  incoming mobs, friendly fire and short-term route goals, plus distinctive
  Special/Boss or panic music in the scoped Hotel chapter.
- Excludes: omniscient enemy positions; a complete next-wave roster; manual
  human voice chat; a static external walkthrough.
- Parameters: teammate, outline state, vocalisation, hostile cue, music layer,
  event class, direction, urgency, visibility exception and hidden future.
- Evidence: [Left 4 Dead 2 decomposition](../games/g-l/left-4-dead-2.md).
- Novelty: first isolated for `GAME-0192`; multiple diegetic and overlay channels
  jointly reveal cooperative rescue urgency while the Director's next exact
  population remains concealed.

## INF-247 — Ops interfaces expose projected and settled reward grade

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: the activity interface exposes selected difficulty and projected
  grade before launch, then reports completion score, eligible time
  contribution, final grade, mapped reward tier and chest admission after the
  terminal objective.
- Includes: the scoped Normal Devil's Lair Fireteam Op projecting and settling
  `B` / Tier 1 under current Update 9.7 rules.
- Excludes: hidden future reward item identity; account Power progression; a
  live objective marker without post-activity evaluation; external telemetry.
- Parameters: activity, difficulty, modifiers, projected grade, score, time
  contribution, final grade, reward tier, chest and display timing.
- Evidence: [Destiny 2 decomposition](../games/a-f/destiny-2.md).
- Novelty: first isolated for `GAME-0193`; one interface carries a selectable
  Ops difficulty through a score calculation into a grade-labelled reward
  terminal rather than merely showing a live score or generic results screen.

## INF-248 — Campaign interface exposes persistent party readiness

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the campaign map, party and settlement interfaces expose the
  party's route or position, movement speed, denars, food, recruit offers,
  roster, wounded health, carried equipment and current tutorial objective
  before the player commits travel, time, hiring or purchase.
- Includes: Tevea, the three marked raiders and Radagos-hideout preparation in
  scoped Mount & Blade II: Bannerlord Campaign.
- Excludes: exact hidden enemy composition; future loot; kingdom-wide economy;
  battle formation state after an encounter loads.
- Parameters: party, position, route, speed, denars, food, recruit offer,
  roster, health, inventory, settlement and quest objective.
- Evidence: [Mount & Blade II: Bannerlord decomposition](../games/m-r/mount-and-blade-ii-bannerlord.md).
- Novelty: first isolated for `GAME-0194`; one campaign surface joins a mobile
  recruit roster and provisions to authored contact readiness.

## INF-249 — Battle interface exposes avatar and troop-command state

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the live battle interface and world cues expose avatar health and
  equipment, selected troop group, formation, issued order, living/casualty
  state, visible hostiles and incoming attack direction before the next direct
  or group command.
- Includes: the three tutorial raider battles and Radagos hideout in scoped
  Mount & Blade II: Bannerlord Campaign.
- Excludes: campaign denars and food; concealed hostiles without an eligible
  cue; post-battle loot identity; exact future AI decisions.
- Parameters: avatar, health, equipment, mount state, troop group, formation,
  order, living count, casualty, hostile, attack cue and direction.
- Evidence: [Mount & Blade II: Bannerlord decomposition](../games/m-r/mount-and-blade-ii-bannerlord.md).
- Novelty: first isolated for `GAME-0194`; one player simultaneously reads an
  embodied fighter and a recruited formation under the same live authority.

## INF-250 — Vehicle form and response expose distributed physical damage

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: visible body deformation, broken or detached parts, tyre state
  and changed steering, suspension or traction response expose the current
  distributed condition of a soft-body vehicle during live control.
- Includes: damage feedback from contact in scoped BeamNG.drive Road Master.
- Excludes: one abstract vehicle-health bar; purely decorative dirt; hidden
  future beam failure; a post-combat internal-module diagram.
- Parameters: visible shape, part attachment, tyre, suspension, steering pull,
  traction response, contact history and camera.
- Evidence: [BeamNG.drive decomposition](../games/a-f/beamng-drive.md).
- Novelty: first isolated for `GAME-0195`; earlier vehicle information exposes
  aggregate damage widgets or combat modules rather than world-visible
  distributed form plus the resulting control response.

## INF-251 — Time Trial result exposes elapsed time and retained entry

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: after a valid Time Trial finish, the end transition exposes the
  completed elapsed time and its place in the mission's retained result or
  high-score state separately from the live checkpoint HUD.
- Includes: the scoped BeamNG.drive Road Master completed-time result; the
  Trackmania `Summer 2026 - 01` retained time and fixed medal result.
- Excludes: live elapsed time before finish; Festival progress and reward
  inventory; hidden online ranking; an unfinished attempt.
- Parameters: mission, elapsed time, retained entry, comparison value, display
  timing and retry/continue choice.
- Evidence: [BeamNG.drive decomposition](../games/a-f/beamng-drive.md) and
  [Trackmania decomposition](../games/s-z/trackmania.md).
- Additional support: [Gran Turismo decomposition](../games/g-l/gran-turismo.md),
  for the elapsed result reported after licence B-1 settles.
- Novelty: first isolated for `GAME-0195`; existing driving result information
  is coupled to Festival rewards, while this record is a standalone retained
  timed evaluation.

## INF-252 — Field and machine views expose productive treatment state

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: context, map and vehicle interfaces expose the current field
  owner, crop and growth, fertilized/treatment state, coupled tool controls,
  remaining compatible fill and working-width cues needed to plan productive
  passes.
- Includes: the scoped Farming Simulator 25 field-information, soil-composition
  map layer, Help Window, attachable-object and fill-level displays.
- Excludes: concealed future growth; exact untreated cells below the exposed
  layer; post-contract money settlement; a generic quest checklist with no
  machine or surface state.
- Parameters: owner, crop, growth, treatment percentage, yield state, map layer,
  vehicle, implement, attachment, activation, fill and working width.
- Evidence: [Farming Simulator 25 decomposition](../games/a-f/farming-simulator-25.md).
- Novelty: first isolated for `GAME-0196`; one interface boundary joins a
  persistent productive surface to the moving powered tool that can change it.

## INF-253 — Contract views expose borrowed field-job progress and settlement

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: before acceptance and through completion, contract interfaces
  expose the selected task, farmer, assigned field, promised reward,
  borrowed-item choice or deduction, accepted progress and final collectable
  state needed to decide whether and when to settle.
- Includes: the scoped Farming Simulator 25 Fertilizing offer and completed
  contract state.
- Excludes: generic farm balance without task attribution; undisclosed future
  offers; field treatment visible only in the world; post-settlement spending.
- Parameters: task, farmer, field, reward, borrowing fee, supplied items,
  progress, threshold, completed state, collect action and net result.
- Evidence: [Farming Simulator 25 decomposition](../games/a-f/farming-simulator-25.md).
- Novelty: first isolated for `GAME-0196`; one view carries a temporary machine
  fleet and surface-coverage contract through explicit net-money collection.

## INF-254 — Platform-duel HUD exposes damage, stocks, weapon and clock

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: one live platform-fighter interface exposes each participant's
  damage colour and remaining stock together with current weapon/unarmed cues,
  off-screen direction when applicable and the shared match clock.
- Includes: the scoped Brawlhalla Bödvar mirror Stock HUD and world cues.
- Excludes: hidden exact frame values; ranked rating; account experience and
  missions; a vitality/Drive/Super round HUD; post-match cosmetic rewards.
- Parameters: participants, damage colour, stocks, weapon/unarmed state,
  off-screen indicator, clock, knockout notice and result transition.
- Evidence: [Brawlhalla decomposition](../games/a-f/brawlhalla.md).
- Novelty: first isolated for `GAME-0198`; damage is visible as launch risk
  rather than remaining health and is paired directly with recoverable stock.

## INF-255 — Driving HUD exposes burst, Heat and exposed earnings

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the live driving interface jointly exposes the vehicle's
  temporary burst reserve, current police Heat/perception state and earnings
  that remain exposed before garage settlement.
- Includes: Need for Speed Unbound Burst Nitrous, Heat, police pursuit/search
  and cash state through the scoped race-to-garage trace.
- Excludes: event terms shown only before entry; final retained account balance;
  hidden police routes; cosmetic tachometer effects.
- Parameters: burst reserve, gain cue, activation cue, Heat, police perception,
  search state, exposed cash, bust risk and garage route.
- Evidence: [Need for Speed Unbound decomposition](../games/m-r/need-for-speed-unbound.md).
- Novelty: first isolated for `GAME-0199`; one live risk surface ties the
  earned acceleration resource to the pursuit that delays durable payout.

## INF-256 — Heist cues expose objective, concealment and response phase

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the live heist view exposes current objective text and relevant
  timers, casing or masked state when present, local detection or loud-response
  phase, fixture and escort state, hostage and secured-loot consequences and
  escape availability without revealing future layout samples or exact enemies.
- Includes: PAYDAY 2 Bank Heist detection bars, objective/drill prompts, Police
  Assault banner, custody/hostage cues, bag credit and escape marker; PAYDAY 3
  Road Rage EMP deadline, route prompts, escort circle, drill, bag percentage
  and escape marker.
- Excludes: omniscient guard paths; exact future jam time; account progression
  menus; post-heist payout arithmetic.
- Parameters: objective, timer, casing, detection, alarm, response phase,
  fixture, escort region, route stop, drill, hostage, secured count, escape
  marker and hidden future state.
- Evidence: [PAYDAY 2 decomposition](../games/m-r/payday-2.md) and
  [PAYDAY 3 decomposition](../games/m-r/payday-3.md).
- Novelty: first isolated for `GAME-0201`; one mission interface spans the
  irreversible stealth boundary, interruptible machine work and transported
  objective terminal.

## INF-257 — Heist result exposes secured value and retained payout

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the terminal result identifies contract success and discloses
  the credited contract and secured-loot value together with the retained
  payout partitions produced by that completed heist.
- Includes: the PAYDAY 2 Bank Heist success and payout sequence after escape.
- Excludes: live objective hints; future Crime.net offers; skill, Infamy or
  account-build optimisation beyond the declared result boundary.
- Parameters: success, contract value, secured bags, loot value, spending cash,
  offshore value, experience display and retained timestamp.
- Evidence: [PAYDAY 2 decomposition](../games/m-r/payday-2.md).
- Additional support: [PAYDAY 3 decomposition](../games/m-r/payday-3.md), for
  successful Heist Results, secured rare-earth value and retained payout.
- Novelty: first isolated for `GAME-0201`; the terminal separates transported
  value from the economic partitions retained after the mission closes.

## INF-258 — Body and terrain feedback expose climbing affordance and risk

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: visible surface geometry, hand/body pose, attachment response,
  motion, local hazard effects and landing feedback reveal current reach,
  climbability, rest opportunities and fall risk without exposing a solved route.
- Includes: PEAK free-surface climbing and biome traversal feedback.
- Excludes: a complete route overlay; hidden loot contents; stamina values
  already represented by personal survival information.
- Parameters: surface, reach, pose, grip, motion, hazard cue, rest, fall and injury.
- Evidence: [PEAK decomposition](../games/m-r/peak.md).
- Additional support: [DEATH STRANDING DIRECTOR'S CUT decomposition](../games/a-f/death-stranding-directors-cut.md),
  for surface, body-pose, sway, footing and fall-risk feedback without a solved route.
- Novelty: first isolated for `GAME-0203`; the physical avatar itself is the
  main instrument for reading an unmarked generated climbing route.

## INF-259 — Biome and rescue feedback expose expedition progress

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: biome titles, campfire/gate state, entry into PEAK, Flare response,
  helicopter countdown and Scouting Report disclose ordered run progress and
  whether the positive terminal has settled.
- Includes: the scoped PEAK solo expedition.
- Excludes: achievement hunting; a complete daily route map; hidden future
  luggage; post-result account cosmetics.
- Parameters: biome, campfire, gate, PEAK region, signal, helicopter, countdown,
  report and completed result.
- Evidence: [PEAK decomposition](../games/m-r/peak.md).
- Novelty: first isolated for `GAME-0203`; sparse world-state milestones make a
  continuous vertical survival route and its explicit rescue closure auditable.

## INF-260 — Character view exposes qualities and relationships

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: character panels and tooltips expose identity, traits, skills,
  lifestyle, directed opinions, family and political relationships plus the
  explained modifiers relevant to current interactions.
- Includes: Murchad, marriage candidates, councillors, vassals and commanders
  in the scoped Crusader Kings III tutorial.
- Excludes: hidden future events; an external biography; title geography
  without character state.
- Parameters: character, trait, skill, lifestyle, opinion, relation, modifier,
  tooltip and eligible interaction.
- Evidence: [Crusader Kings III decomposition](../games/a-f/crusader-kings-iii.md).
- Novelty: first isolated for `GAME-0204`; one inspectable actor sheet explains
  social, administrative and military consequences across several systems.

## INF-261 — Title view exposes realm, domain, vassals and claims

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: map modes, title panels and relation tooltips expose direct
  holdings, realm inclusion, de jure hierarchy, holders, lieges, vassals,
  obligations and available title claims or casus belli.
- Includes: Thomond, Ormond, Munster and Desmond in Murchad's tutorial.
- Excludes: exact hidden hostile plans; succession after the tutorial; terrain
  combat detail already shown by army information.
- Parameters: title, rank, holder, de jure relation, domain, realm, liege,
  vassal, obligation, claim and casus belli.
- Evidence: [Crusader Kings III decomposition](../games/a-f/crusader-kings-iii.md).
- Novelty: first isolated for `GAME-0204`; nested legal geography simultaneously
  explains ownership, obligations and a possible war.

## INF-262 — Interaction views expose candidates and expected effects

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: marriage and council interfaces expose eligible people, their
  relevant qualities, acceptance or appointment constraints, predicted
  relationship effects, available tasks, targets and current task progress.
- Includes: the ordinary marriage and council steps in Murchad's tutorial.
- Excludes: hidden AI deliberation; future children; undisclosed random events;
  external candidate rankings.
- Parameters: candidate, office, skill, acceptance, alliance, task, target,
  progress, expected effect and rejection reason.
- Evidence: [Crusader Kings III decomposition](../games/a-f/crusader-kings-iii.md).
- Novelty: first isolated for `GAME-0204`; person selection and office operation
  are made comparable through predicted relational and timed consequences.

## INF-263 — Military view exposes muster, movement, battle and siege

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: military panels and map feedback expose available levies and
  men-at-arms, rally and gathering state, army composition, commander, route,
  supply, battle balance, casualties, retreat and siege progress.
- Includes: Murchad's raised army and the Desmond war route.
- Excludes: direct soldier-level controls; exact future combat rolls; title
  claims and enforce-demand effects.
- Parameters: contribution, rally, gathering, army, commander, route, supply,
  advantage, casualties, retreat, fort and siege progress.
- Evidence: [Crusader Kings III decomposition](../games/a-f/crusader-kings-iii.md).
- Novelty: first isolated for `GAME-0204`; distributed realm capacity and one
  high-level army's battle/siege states remain visible on the same map.

## INF-264 — War and guidance views expose legal progress and completion

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: declaration, war and tutorial interfaces expose the selected
  casus belli, target and objective, score components, settlement eligibility,
  declared effects, current guidance and explicit tutorial completion state.
- Includes: the instructed Desmond war and Murchad tutorial terminal.
- Excludes: forming Ireland; an arbitrary player checklist; post-tutorial
  achievements; exact hidden opponent plans.
- Parameters: casus belli, target, objective, battle score, occupation score,
  prisoner score, total, demand, effect, guidance stage and completion.
- Evidence: [Crusader Kings III decomposition](../games/a-f/crusader-kings-iii.md).
- Novelty: first isolated for `GAME-0204`; one display connects pre-war legal
  authority, live military evaluation, enforceable outcome and authored stop.

## INF-265 — Sensory evidence and learned monster preparation are visible

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: an investigative focus and retained journal expose reachable
  highlighted evidence, a locally followable trace and learned target or
  preparation facts while leaving unexamined future clues undisclosed.
- Includes: Witcher Senses highlights and the quest/journal/bestiary information
  used in The Beast of White Orchard.
- Excludes: a complete external walkthrough; omniscient enemy tracking; ordinary
  combat sight and sound without clue interpretation.
- Parameters: search area, highlight, trace, clue state, journal fact, target
  class, vulnerability, preparation and undiscovered state.
- Evidence: [The Witcher 3: Wild Hunt decomposition](../games/s-z/the-witcher-3-wild-hunt.md).
- Novelty: first isolated for `GAME-0205`; transient local highlighting and
  retained monster knowledge disclose two stages of the same investigation.

## INF-266 — Duel interface exposes public card-rule state

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the interface exposes the player's hand, both Life Point totals,
  public zones and cards, current phase, battle positions, inspected rules
  text, legal prompts and the numbered Chain while concealing the opponent's
  hand, Deck order and face-down identities.
- Includes: the scoped Master Duel Tutorial chapter `10003` interface.
- Excludes: personal collection panels, external deck trackers, CPU intent or
  disclosure of unrevealed cards.
- Parameters: hand, LP, zones, phase, position, card text, prompt, Chain and concealed state.
- Evidence: [Yu-Gi-Oh! Master Duel decomposition](../games/s-z/yu-gi-oh-master-duel.md).
- Novelty: first isolated for `GAME-0206`; one digital surface joins positional
  card state and a whole numbered response chain without revealing fixed secrets.

## INF-267 — Heist HUD exposes carrier relation and active wreck stage

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the live driving view exposes the current carrier-relative
  instruction, eligible hostile markers, accepted wreck count and immediate
  catch-up or delivery pressure without revealing future waves or exact AI
  trajectories.
- Includes: truck target, `2`/`4` House Enforcer quotas, rear/side prompts and
  Airfield 73 route in Need for Speed Payback's `The Highway Heist`.
- Excludes: generic speed/gear display; pre-event car eligibility; police Heat;
  post-result unlocks; an external walkthrough.
- Parameters: objective text, target marker, target distance, wreck quota,
  current count, approach cue, route update, failure warning and destination.
- Evidence: [Need for Speed Payback decomposition](../games/m-r/need-for-speed-payback.md).
- Novelty: first isolated for `GAME-0208`; one HUD surface couples hostile
  contact progress to a moving carrier's changing spatial gate.

## INF-268 — Tutorial adviser exposes the current authored instruction

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the tutorial surface states the current authored objective,
  explains the relevant legal action or risk and reports completion before
  advancing to the next instruction, without disclosing the full future chain.
- Includes: adviser dialogue and current task text throughout Cossacks 3
  `War Ruse — Peace`.
- Excludes: the ordinary RTS resource HUD; an external walkthrough; a complete
  campaign list; dialogue with no mechanically testable instruction.
- Parameters: objective step, instruction, highlighted actor or command,
  completion predicate, warning, acknowledgement and next-step reveal.
- Evidence: [Cossacks 3 decomposition](../games/a-f/cossacks-3.md).
- Additional support: [Halo 3 decomposition](../games/g-l/halo-3.md),
  for contextual control, interaction and objective instructions.
- Additional support: [Warcraft III: Reign of Chaos decomposition](../games/s-z/warcraft-iii-reign-of-chaos.md),
  for the narrator exposing one current movement, grouping, combat or ability
  lesson and acknowledging it before the next step.
- Novelty: first isolated for `GAME-0209`; a staged teaching surface reveals
  one causal RTS dependency and its completion transition at a time.

## INF-269 — Status icons expose categorical body trends, not exact causes

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the survival HUD exposes categorical current health, blood,
  temperature, energy, hydration, bleeding and sickness state plus eligible
  directional trends while withholding exact internal values, pathogen
  identity and future bodily outcome.
- Includes: the DayZ first-person status area during the scoped official
  Chernarus life.
- Excludes: the complete inventory panel; exact debug-monitor statistics;
  external diagnostic tools; a named disease diagnosis before the rules reveal
  enough evidence; remote survivor status.
- Parameters: category, icon, grade, trend, bleeding count, symptom, threshold,
  hidden value, hidden agent and update interval.
- Evidence: [DayZ decomposition](../games/a-f/dayz.md).
- Novelty: first isolated for `GAME-0210`; the interface supports survival
  diagnosis through categorical direction without disclosing the full body model.

## INF-270 — Tank HUD exposes aim uncertainty, durability and component state

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: the active-tank interface exposes ammunition and reload readiness,
  a movement-sensitive aiming circle, vehicle hit points and known crew or
  module impairment without guaranteeing the next shell's exact impact or
  penetration result.
- Includes: Arcade and Sniper aiming views, ammunition, reload, hit points and
  damage indicators for the scoped World of Tanks MS-1.
- Excludes: hidden opponent modules before an observed hit; exact future shell
  dispersion; garage research, economy and service cost.
- Parameters: ammunition, reload, reticle, dispersion, aim time, hit points,
  crew, module, impairment, repair and uncertainty.
- Evidence: [World of Tanks decomposition](../games/s-z/world-of-tanks.md).
- Novelty: first isolated for `GAME-0211`; one combat display couples a
  settling accuracy envelope and aggregate tank durability with distinct
  internal functional warnings.

## INF-271 — Remote manipulation response exposes target and held-object state

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: a remote-manipulation reticle or effect and the visible prop
  response disclose whether the aimed object is reacting to a pull, attached
  in the held pose, released, launched or rejected, while leaving its future
  collision path and damage unresolved.
- Includes: ordinary Gravity Gun targeting, pull, hold, drop, launch and deny
  response during the scoped Half-Life 2 Ravenholm chapter; reticle,
  telekinetic effect and loose-prop response during CONTROL's scoped mission.
- Excludes: exact future impact preview; the general active-weapon/ammunition
  HUD; hidden object mass as a numeric label; supercharged Gravity Gun state;
  audio alone as the only evidence channel.
- Parameters: perspective, aimed target, reticle or effect state, object
  motion, held pose, tool or ability elements, deny response, release state and
  prediction boundary.
- Evidence: [Half-Life 2 decomposition](../games/g-l/half-life-2.md) and
  [CONTROL Ultimate Edition decomposition](../games/a-f/control-ultimate-edition.md).
- Novelty: first isolated for `GAME-0212`; the manipulation tool exposes the
  current physical relation before the launched body's open-ended collision
  result, rather than previewing an exact trajectory or damage value.

## INF-272 — Holographic map colours expose route-edge reachability

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: an inspectable three-dimensional map distinguishes unexplored
  connections, currently openable passages and passages blocked by a missing
  capability through stable colours, without revealing undiscovered contents
  or solving the route automatically.
- Includes: BD-1's Bogano Holomap showing unexplored orange paths, openable
  green gates and unavailable red gates in STAR WARS Jedi: Fallen Order.
- Excludes: an external walkthrough; a flat objective marker with no edge
  state; hidden future collectibles; a guaranteed route chosen by the system.
- Parameters: discovered volume, edge, colour, unexplored state, current
  capability, openable gate, blocked gate and objective marker.
- Evidence: [STAR WARS Jedi: Fallen Order decomposition](../games/s-z/star-wars-jedi-fallen-order.md).
- Novelty: first isolated for `GAME-0213`; the navigational display classifies
  each known connection by present reachability rather than only retaining
  explored geometry or one suggested destination.

## INF-273 — Road HUD exposes offence severity and police pursuit state

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: the live road interface identifies nearby civilian, police and
  pursuing vehicles and distinguishes a payable citation, active arrest demand
  and continuing police search without revealing future patrol paths.
- Includes: Mafia (2002) radar colours, ticket and handcuff icons, wanted bar,
  objective cues and the transition from observed offence to pursuit/search.
- Excludes: a calculated GPS road route; exact hidden police spawn positions;
  an already-debited traffic-fine toast; post-mission statistics.
- Parameters: radar contact, contact class, offence icon, citation, arrest,
  wanted bar, police perception, search state and objective cue.
- Evidence: [Mafia (2002) decomposition](../games/m-r/mafia-2002.md).
- Novelty: first isolated for `GAME-0214`; the same visible law surface tells
  the player whether stopping can still settle the offence or whether evasion
  has become a terminal arrest risk.

## INF-274 — Fortification outlines expose build and damage state

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: local world outlines, geometry and progress feedback distinguish
  an available authored Fortification locus from its building, completed,
  damaged and destroyed states before the next toolbox or route decision.
- Includes: Battlefield V Arras trench, sandbag, barrier and resupply-station
  Fortification feedback.
- Excludes: a complete remote structural map; cosmetic rubble; arbitrary
  terrain with no build authority; hidden future damage.
- Parameters: outline, type, progress, completion, material, damage, function,
  tool prompt and local visibility.
- Evidence: [Battlefield V decomposition](../games/a-f/battlefield-v.md).
- Novelty: first isolated for `GAME-0220`; the missing structure's authored
  silhouette itself discloses a live tactical construction opportunity.

## INF-275 — Squad interface exposes Reinforcement budget and call state

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: the live squad surface exposes the shared Reinforcement-point
  total, current leader, available typed calls, their costs and any selected
  target or pending delivery sufficiently to choose an authorised spend.
- Includes: Battlefield V squad Reinforcement menu and delivery feedback.
- Excludes: private account currency; hidden enemy squad budget; future points
  not yet earned; an automatic effect with no call decision.
- Parameters: squad, leader, points, option, cost, availability, target,
  confirmation, delivery state and recipients.
- Evidence: [Battlefield V decomposition](../games/a-f/battlefield-v.md).
- Novelty: first isolated for `GAME-0220`; one display separates collective
  earning from role-gated spending and previews the currently legal live effect.

## INF-276 — Gunslinger HUD exposes combo, special and duel preparation state

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the first-person interface exposes the current rapid-kill combo
  and experience feedback, Concentration readiness, and—during a duel—the
  opponent-focus and draw-hand-speed values plus visible opponent draw cue,
  without guaranteeing the next shot's hit.
- Includes: the scoped first `Call of Juarez: Gunslinger` Story episode and its
  Pat Garrett duel.
- Excludes: hidden future enemy positions; an external walkthrough; audio as
  the only draw evidence; Arcade leaderboard and Duel Challenge lives.
- Parameters: combo count, continuation cue, award, experience, Concentration,
  focus, speed, opponent hand, draw cue, aim state and result feedback.
- Evidence: [Call of Juarez: Gunslinger decomposition](../games/a-f/call-of-juarez-gunslinger.md).
- Novelty: first isolated for `GAME-0222`; one visible action-game surface joins
  expiring reward pressure with the two independent preparations for a draw.

## INF-277 — Cockpit exposes live systems, target, objective and threats

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: a directly controlled craft's cockpit instruments expose the
  currently applicable power distribution, shield and hull state, weapon or
  auxiliary readiness, selected target, objective direction and visible threat
  warnings without revealing hidden future spawns.
- Includes: the non-VR Standard-instruments presentation in Squadrons Mission 1;
  Frontier power, shield, hull, weapon, target and objective presentation in
  Starfield's `One Small Step`.
- Excludes: an external walkthrough; hidden enemy plans; VR head position;
  multiplayer squad telemetry; purely cinematic information.
- Parameters: power channels, shields, hull, weapons, auxiliaries, countermeasure,
  selected target, lock, objective marker, threat warning and result feedback.
- Evidence: [STAR WARS: Squadrons decomposition](../games/s-z/star-wars-squadrons.md).
- Additional support: [Starfield decomposition](../games/s-z/starfield.md).
- Novelty: first isolated for `GAME-0225`; one diegetic cockpit surface joins
  flight resources, target solution and time-critical defence warnings.
- Change note: wording generalised by
  [`TAXONOMY_CHANGE_075`](../../research/taxonomy-changes/TAXONOMY_CHANGE_075.md).

## INF-278 — Shared-rule claim exposes modifier and claimant consequence

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: live match feedback identifies a claimed shared-rule modifier
  and exposes the claimant's identity or location according to that modifier's
  declared scope, without revealing every other participant.
- Includes: Fortnite `v42.00` claimant name around an Override Console and map
  broadcast for a claimed squad-scoped Override; in Solo, that squad is one
  participant.
- Excludes: an external code list; hidden future console effects; omniscient
  opponent tracking; account profile statistics after the match.
- Parameters: modifier, scope, claimant, name display, map marker, recipients,
  duration, visibility range and removal.
- Evidence: [Fortnite decomposition](../games/a-f/fortnite.md).
- Novelty: first isolated for `GAME-0227`; changing a shared live rule creates
  an explicit information cost tied to the participant who obtained authority.

## INF-279 — Local survey exposes resource identity, bearing and distance

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: a local survey interface exposes which eligible nearby resource
  was revealed, its relative bearing and an approximate distance before the
  player chooses a traversal line.
- Includes: No Man's Sky Scanner markers inspected through the Analysis Visor
  during the scoped Awakenings route.
- Excludes: undiscovered planetary geography; an external resource map;
  catalogue completion; one tracked authored mission destination.
- Parameters: resource class, marker, bearing, approximate distance, survey
  origin, visible duration and current visor state.
- Evidence: [No Man's Sky decomposition](../games/m-r/no-mans-sky.md).
- Novelty: first isolated for `GAME-0229`; temporary pulse-produced resource
  bearings guide collection without exposing the wider generated world.

## INF-280 — Weapon heat and active-cooling timing are visible

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: the combat interface exposes the active weapon's current heat,
  overheat state and authored active-cooling timing band before the player
  decides whether to fire, wait or commit the timed input.
- Includes: reticle heat gauge, overheat lock and active-cooling window in the
  scoped STAR WARS Battlefront II (2017) campaign prologue.
- Excludes: hidden thermal simulation; carried ammunition count; an ability
  cooldown; external weapon statistics with no current readiness state.
- Parameters: heat gauge, capacity, overheat cue, cooling cursor, success band,
  penalty band, ready feedback and selected weapon.
- Evidence: [STAR WARS Battlefront II (2017) decomposition](../games/s-z/star-wars-battlefront-ii-2017.md).
- Novelty: first isolated for `GAME-0230`; the same live display supports burst
  pacing and a timed alternative to passive recovery.

## INF-281 — Initial attribute values and remaining budget are visible

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: before character confirmation, the creation interface exposes
  every current named attribute value and the still-unspent portion of their
  shared distributable point pool.
- Includes: Fallout 4's S.P.E.C.I.A.L. allocation panel showing seven current
  values and remaining points.
- Excludes: hidden derived formulas; later perk charts; cosmetic sliders;
  external build planners; a class list with no shared numeric budget.
- Parameters: attribute labels, current values, minimum, maximum, total pool,
  remaining points, invalid-state feedback and confirmation availability.
- Evidence: [Fallout 4 decomposition](../games/a-f/fallout-4.md).
- Novelty: first isolated for `GAME-0231`; the interface reveals the coupled
  cross-attribute budget before campaign entry.

## INF-282 — Challenge ledger exposes progress, claims and group readiness

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: a tracked-challenge surface exposes each current requirement and
  count, its incomplete, completed or redeemed state, the individual reward and
  whether the encompassing group reward can now be claimed.
- Includes: the current 7 Days to Die `Basics of Survival` challenge window.
- Excludes: an external walkthrough; a one-at-a-time instruction that conceals
  future requirements; hidden reward rolls; the later trader-job catalogue.
- Parameters: group, entry, requirement, current count, target count,
  completion state, redeem state, individual reward and group readiness.
- Evidence: [7 Days to Die decomposition](../games/0-9/7-days-to-die.md).
- Novelty: first isolated for `GAME-0233`; the player can distinguish completed
  work from unclaimed value and inspect the remaining group-wide claim gate.

## INF-283 — Live attachment surface exposes categories and current choices

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: during live control, a bounded weapon surface reveals the
  attachment categories supported by the held weapon, the current option and
  the alternatives presently available before replacement is committed.
- Includes: the Battlefield 2042 Plus Menu for sight, barrel, ammunition and
  underbarrel choices.
- Excludes: an external weapon guide; hidden future unlocks; armour durability;
  the complete pre-deployment loadout.
- Parameters: weapon, categories, current options, alternatives,
  compatibility, selection focus and commit feedback.
- Evidence: [Battlefield 2042 decomposition](../games/a-f/battlefield-2042.md).
- Novelty: first isolated for `GAME-0234`; the immediate weapon mutation is
  previewed without leaving the live combat state.

## INF-284 — Support call surface exposes vehicle availability and placement legality

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: a live support surface reveals the currently requestable vehicle
  classes, availability or shared-capacity rejection, requester cooldown and
  whether the selected world position can accept delivery.
- Includes: the ordinary Battlefield 2042 call-in tablet and delivery target
  feedback.
- Excludes: the deployment map's existing vehicle seats; account unlock
  progress; an external vehicle list; hidden enemy vehicle capacity.
- Parameters: options, availability, shared capacity, cooldown, target cursor,
  surface legality, confirmation and rejection.
- Evidence: [Battlefield 2042 decomposition](../games/a-f/battlefield-2042.md).
- Novelty: first isolated for `GAME-0234`; one interface joins shared asset
  availability with a local spatial delivery check.

## INF-285 — Objective display exposes point-to-sector control and ticket pressure

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the match interface exposes each relevant control point inside
  its sector, local capture or contest state, complete sector ownership, both
  reinforcement pools and the current majority-driven pressure before the
  next strategic choice.
- Includes: Battlefield 2042 Conquest point, sector and ticket feedback.
- Excludes: omniscient enemy positions; personal score as the terminal state;
  an external map; ordered Breakthrough-sector progress.
- Parameters: point, sector, owner, contest, capture progress, majority,
  reinforcement pools, drain state and result feedback.
- Evidence: [Battlefield 2042 decomposition](../games/a-f/battlefield-2042.md).
- Novelty: first isolated for `GAME-0234`; the display makes the two-level
  territorial aggregation and its shared-resource consequence readable.

## INF-286 — Campaign HUD exposes recovery stock and cumulative route rank

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: during and between linked driving events, the interface exposes
  the remaining checkpoint-recovery stock together with the current cumulative
  route rank or pass target, making both local recovery risk and stage progress
  readable before final settlement.
- Includes: Checkpoint Resets, race objective and 211th-to-195th progress in the
  scoped Need for Speed: The Run Stage 1 packet.
- Excludes: speed and gear alone; a one-race live place without cumulative
  progress; hidden recovery stock; external friend rankings or leaderboards.
- Parameters: remaining recovery units, final-unit warning, current rank,
  event pass target, stage target, progress update and settlement display.
- Evidence: [Need for Speed: The Run decomposition](../games/m-r/need-for-speed-the-run.md).
- Novelty: first isolated for `GAME-0235`; one surface connects a finite local
  rollback budget to rank progress carried across several race results.

## INF-287 — Recon view exposes actor marks and directional detection progress

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the live reconnaissance and combat interface distinguishes
  deliberately marked living actors, their retained world or map positions and
  the direction and progress of nearby hostile perception before or as full
  detection occurs.
- Includes: Far Cry 3 camera target markers, map symbols and directional
  detection indicators in the scoped first-outpost mission.
- Excludes: current sight alone; a complete omniscient enemy roster; a static
  objective waypoint; hidden suspicion with no player-readable feedback.
- Parameters: marked actor, type cue, world marker, map marker, observer
  direction, suspicion progress, detected state, colour and display lifetime.
- Evidence: [Far Cry 3 decomposition](../games/a-f/far-cry-3.md).
- Novelty: first isolated for `GAME-0236`; acquired persistent target knowledge
  and incoming local perception risk share one actionable tactical surface.

## INF-288 — Manual-recipe surface exposes apparatus and process state

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: an embodied recipe surface exposes the known operation sequence,
  staged inputs, current batch transformations, apparatus state and visible
  timing instrument needed to choose the next manual step.
- Includes: Kingdom Come: Deliverance II's recipe page, alchemy bench,
  ingredients, grinder, heated cauldron, sandglass and output vessel.
- Excludes: a technology graph; fixed crafting grid; external walkthrough;
  hidden tolerances or future recipes.
- Parameters: recipe, instruction, input, batch, preparation, apparatus, heat,
  timer, vessel, output preview and feedback.
- Evidence: [Kingdom Come: Deliverance II decomposition](../games/g-l/kingdom-come-deliverance-ii.md).
- Novelty: first isolated for `GAME-0240`; recipe knowledge and live apparatus
  state remain jointly visible during stepwise execution.

## INF-289 — Broadcast court view identifies ball, control and local team shape

- Lifecycle: `Merged`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: historical sport-specific duplicate now represented by the
  parameterised active boundary `INF-178`.
- Includes: historical references that used `INF-289` before taxonomy change
  019.
- Excludes: new game signatures; use `INF-178` with the scoped playing-surface
  parameters.
- Parameters: none; preserved as a lifecycle alias.
- Evidence: [NBA 2K26 decomposition](../games/m-r/nba-2k26.md).
- Merged into: `INF-178` by
  [`TAXONOMY_CHANGE_019`](../../research/taxonomy-changes/TAXONOMY_CHANGE_019.md).

## INF-290 — Possession HUD exposes score, game clock and shot clock

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: during live play, the interface jointly exposes both team scores,
  current period, remaining match time, remaining possession time and current
  adjudication feedback needed to choose pace, attempt and defensive risk.
- Includes: NBA 2K26 scorebug, quarter/game clock, shot clock and foul or
  violation feedback in the scoped exhibition.
- Excludes: season standings; hidden opponent ratings; a score-only display;
  an external stopwatch; currency or progression notices.
- Parameters: sides, scores, period, game clock, shot clock, possession,
  offence notice, free-throw state and update cadence.
- Evidence: [NBA 2K26 decomposition](../games/m-r/nba-2k26.md).
- Novelty: first isolated for `GAME-0241`; shared match time and per-possession
  time pressure remain simultaneously visible.

## INF-291 — Final match surface exposes score and box-score settlement

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: after one head-to-head match settles, a terminal surface exposes
  the unequal final score, winning and losing sides and accumulated box-score
  categories sufficient to verify that the contest is complete.
- Includes: NBA 2K26's final Play Now result and team/player box score.
- Excludes: an in-progress scoreboard; season standings; currency rewards;
  account progression; a replay clip without result state.
- Parameters: sides, final score, winner, loser, period totals, team statistics,
  player statistics, completion state and dismissal.
- Evidence: [NBA 2K26 decomposition](../games/m-r/nba-2k26.md).
- Novelty: first isolated for `GAME-0241`; the terminal joins result identity
  with the accumulated event ledger of one disposable exhibition.

## INF-292 — Assisted-driving view exposes live manoeuvre prompts and nitro

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: during forced vehicle progression, the driving view identifies
  the currently available assisted-path or manoeuvre choices together with the
  current ordinary nitro state needed to select and time the next intervention.
- Includes: TouchDrive route/manoeuvre offers and nitro gauge during the scoped
  Asphalt Legends Career race.
- Excludes: static route planning; a manual-steering direction indicator;
  hidden future branches; post-race rewards; a boost gauge with no choices.
- Parameters: vehicle, current path, offered options, availability interval,
  selected state, nitro amount, timing cue and update cadence.
- Evidence: [Asphalt Legends decomposition](../games/a-f/asphalt-legends.md).
- Novelty: first isolated for `GAME-0242`; live discrete path authority is
  readable alongside the resource that changes the assisted trajectory's pace.

## INF-293 — Investigation interfaces expose classified targets and evaluated progress

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: scanner, mission and settlement surfaces expose acquired target
  classifications, analysed evidence, custody outcomes, current investigative
  score or rank and retained episode progress without revealing unexamined
  future targets.
- Includes: Battlefield Hardline scanner colours, evidence and warrant records,
  Expert Score/Rank and Episode progress.
- Excludes: an omniscient suspect roster; generic enemy health; an external
  walkthrough; account rank unrelated to the bounded investigation.
- Parameters: target, classification, evidence state, warrant state, custody
  outcome, score, rank, episode progress, successor and display timing.
- Evidence: [Battlefield Hardline decomposition](../games/a-f/battlefield-hardline.md).
- Novelty: first isolated for `GAME-0243`; live forensic classification and
  post-action custody/evidence evaluation share one bounded progress surface.

## INF-294 — Expose vehicle condition beside session notoriety and unbanked reputation

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: driving and service/encounter interfaces disclose vehicle
  condition, session notoriety, reputation awaiting settlement and available
  recovery or payment feedback so the player can judge return risk.
- Includes: Heat's first-night health, HEAT, REP and contextual repair/bribe
  feedback before safe-house settlement.
- Excludes: Unbound's distinct Burst gauge; hidden future patrol routes; an
  external walkthrough; final retained rewards without live exposure state.
- Parameters: condition, notoriety, reputation, multiplier, service feedback,
  payment offer, currency and update timing.
- Evidence: [Need for Speed Heat decomposition](../games/m-r/need-for-speed-heat.md).
- Novelty: first isolated for `GAME-0244`; current survivability is readable
  alongside the reputation modifier that remains exposed until the night ends.

## INF-295 — Expose a temporary contextual close-action opportunity

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: local visual feedback distinguishes a living hostile's temporary
  stagger state and currently reachable contextual close-action opportunity
  from ordinary damage, recovery and final defeat; the display does not assert
  whether accepting the action will defeat the target.
- Includes: visible close-action opportunities in DOOM (2016), DOOM Eternal,
  Batman: Arkham Asylum, God of War, Resident Evil 4 (2023 remake) and Sekiro.
- Excludes: a persistent enemy-health bar alone; an unaware-target indicator;
  external walkthrough knowledge; a close action whose current legality is not
  disclosed; a promised defeat result not represented by the display.
- Parameters: hostile, stagger state, visual treatment, reach, context,
  opportunity duration, recovery and opportunity-closing state.
- Evidence: [DOOM (2016) decomposition](../games/a-f/doom-2016.md) and
  [Resident Evil 4 decomposition](../games/m-r/resident-evil-4-2023.md).
- Novelty: first isolated for `GAME-0245`; `TAXONOMY_CHANGE_059` removes the
  settlement-specific duplicate while preserving the disclosed opportunity.

## INF-296 — Active capability mode and shared reserve are visible

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the live personal-capability interface identifies the currently
  selected mode and common finite reserve, including visible depletion and
  replenishment, before the player chooses another mode or qualified action.
- Includes: Crysis Remastered Nanosuit mode icon/menu and suit-energy meter
  during Speed, Strength, Armor and Cloak use.
- Excludes: health alone; a permanent skill tree; a hidden cooldown; separate
  weapon ammunition; a vehicle power-allocation diagram; night-vision power.
- Parameters: actor, available modes, selected mode, reserve, capacity,
  depletion, recharge, readiness, icon and display timing.
- Evidence: [Crysis Remastered decomposition](../games/a-f/crysis-remastered.md).
- Novelty: first isolated for `GAME-0246`; one surface joins the selected member
  of an alternative capability set to the shared resource all members consume.

## INF-297 — Aimed relocation preview exposes the accepted world endpoint

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: while a short-range world relocation is aimed, the interface
  distinguishes its current accepted destination from an invalid point before
  the player commits the move.
- Includes: Dishonored's Blink targeting icon and valid floor or ledge preview
  in the scoped mission.
- Excludes: a route marker with no relocation legality; a post-action arrival
  effect; a hidden teleport destination; an ordinary aiming reticle that only
  selects an attack target.
- Parameters: origin, aimed point, range, collision state, accepted endpoint,
  invalid feedback, resource readiness and update timing.
- Evidence: [Dishonored (2012) decomposition](../games/a-f/dishonored-2012.md).
- Novelty: first isolated for `GAME-0247`; the player can inspect the exact
  non-traversed arrival relation before making it irreversible.

## INF-298 — Local awareness cues expose incoming detection and alert state

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: avatar-centred visual cues disclose the direction and current
  escalation of nearby hostile perception while leaving unobserved actors and
  future patrol states unknown.
- Includes: Dishonored's local awareness indicators from suspicion through
  detection during the scoped mission.
- Excludes: an acquired persistent mark on each actor; omniscient enemy
  locations; a binary combat banner with no incoming direction or progression;
  knowledge supplied only by an external walkthrough.
- Parameters: perceiver, direction, suspicion progress, search state, detected
  state, cue timing, occlusion and decay feedback.
- Evidence: [Dishonored (2012) decomposition](../games/a-f/dishonored-2012.md).
- Novelty: first isolated for `GAME-0247`; local perception pressure is exposed
  without requiring the actor-bound reconnaissance marks bundled by
  `INF-287`.

## INF-299 — Results report exposes categories and aggregate evaluation

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: after one bounded mission, level or encounter settles, a terminal
  report exposes recorded conduct or performance categories and the resulting
  aggregate evaluation state sufficient to verify how the attempt was
  classified.
- Includes: Dishonored's end-mission kills, detections, found-body or related
  Stats categories and displayed Chaos state for the scoped mission; Cuphead's
  completed-level time, remaining HP, parry count, Super Meter use, skill level
  and aggregate grade; DAVE THE DIVER's first-service sales categories and
  aggregate performance grade.
- Excludes: live health or ammunition; hidden later narrative consequences; an
  external achievement tracker; a score screen that omits conduct categories.
- Parameters: activity, category labels, category values, aggregate label,
  evaluation state, completion state, display timing and dismissal.
- Evidence: [Dishonored (2012) decomposition](../games/a-f/dishonored-2012.md)
  and [Cuphead decomposition](../games/a-f/cuphead.md), and
  [DAVE THE DIVER decomposition](../games/a-f/dave-the-diver.md).
- Novelty: first isolated for `GAME-0247`; detailed conduct and its aggregate
  classification are jointly readable at the same finite mission terminal.
- Change note: wording generalised by
  [`TAXONOMY_CHANGE_037`](../../research/taxonomy-changes/TAXONOMY_CHANGE_037.md)
  so result categories may describe bounded performance as well as mission
  conduct, and the aggregate may be a grade as well as a classification state.
- Additional support: `TAXONOMY_CHANGE_038` confirms that a finite service
  session is another bounded activity carrier; the report and aggregate
  evaluation boundary is unchanged.

## INF-300 — Situational overlay exposes nearby actors and interactables through occlusion

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: while the player invokes a bounded situational overlay, the view
  distinguishes eligible nearby designated targets, other actors and
  interactable objects through ordinary occlusion while leaving actors beyond
  its coverage and future state unknown.
- Includes: Instinct silhouettes and interactable highlights in HITMAN World
  of Assassination's scoped Paris mission.
- Excludes: persistent acquired marks; a fully revealed tactical map; external
  walkthrough knowledge; ordinary unobstructed sight; decorative colour
  grading without decision state.
- Parameters: observer, coverage, target class, actor class, interactable class,
  occlusion, distinction, update timing and unknown remainder.
- Evidence: [HITMAN World of Assassination decomposition](../games/g-l/hitman-world-of-assassination.md).
- Novelty: first isolated for `GAME-0248`; several local decision classes are
  temporarily revealed through occlusion without being permanently marked.

## INF-301 — Interface exposes presented role and current social legality

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the live interface identifies the controlled actor's currently
  presented role and exposes whether its present area, action or visible item
  is ordinary, suspicious, trespassing or otherwise illegal enough to revise
  the route before completed detection.
- Includes: disguise identity, trespass, suspicious-action and illegal-item
  feedback in HITMAN World of Assassination's scoped Paris mission.
- Excludes: a cosmetic outfit preview; hidden legality learned only after
  failure; a global wanted level; a static mission briefing with no live
  context update.
- Parameters: presented role, area, action, visible item, legality class, live
  label or icon, transition timing and detection relation.
- Evidence: [HITMAN World of Assassination decomposition](../games/g-l/hitman-world-of-assassination.md).
- Novelty: first isolated for `GAME-0248`; one view joins social presentation
  with the legality of current place, behaviour and exposed equipment.

## INF-302 — Carried grid exposes item footprints, orientation and free cells

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: a carried-inventory surface exposes each retained item's current
  rectangular footprint and orientation together with occupied and unoccupied
  cells, so a legal reposition or pickup fit can be judged before commitment.
- Includes: the attaché-case item layout and reorientation surface in Resident
  Evil 4's bounded first chapter.
- Excludes: weight-only capacity; an unlimited item list; a spatial crafting
  recipe; hidden remote loot; cosmetic case decoration with no occupancy
  effect.
- Parameters: grid dimensions, item, footprint, orientation, occupied cells,
  free cells, proposed placement and compatibility feedback.
- Evidence: [Resident Evil 4 decomposition](../games/m-r/resident-evil-4-2023.md).
- Novelty: first isolated for `GAME-0249`; the inventory explains exact spatial
  fit and item reorientation rather than only category, weight or slot count.

## INF-303 — Weapon reticle exposes current aim-focus state

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: while a weapon is readied, the live reticle visibly
  distinguishes its current unfocused or focused aim state before the player
  commits a shot whose declared precision, damage, stagger or critical-result
  relation depends on it.
- Includes: default and focused firearm reticles in Resident Evil 4's bounded
  first chapter; the handgun reticle that shrinks toward its minimum while
  aim is held in Resident Evil 2 (2019 remake)'s scoped Leon opening.
- Excludes: a decorative crosshair with no state change; scope zoom alone;
  hidden accuracy values; an externally calculated hit probability.
- Parameters: weapon, ready state, focus progress, reticle treatment, focused
  state, shot timing and consequence relation.
- Evidence: [Resident Evil 4 decomposition](../games/m-r/resident-evil-4-2023.md)
  and [Resident Evil 2 (2019 remake) decomposition](../games/m-r/resident-evil-2-2019.md).
- Novelty: first isolated for `GAME-0249`; the aiming surface reveals when
  continued readiness changes shot consequences before firing.
- Change note: wording generalised by
  [`TAXONOMY_CHANGE_040`](../../research/taxonomy-changes/TAXONOMY_CHANGE_040.md)
  so the disclosed focus state may govern precision or damage as well as
  stagger or critical relations.

## INF-304 — Expose a temporary contextual close-follow-up opportunity

- Lifecycle: `Merged`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: historical result-specific duplicate now represented by the
  parameterised active boundary `INF-295`.
- Includes: historical references that used `INF-304` before taxonomy change
  059.
- Excludes: current signatures and new analysis; use `INF-295` while keeping
  damage and defeat settlement outside the Information boundary.
- Parameters: none; preserved as a lifecycle alias.
- Evidence: [Resident Evil 4 decomposition](../games/m-r/resident-evil-4-2023.md).
- Merged into: `INF-295` by
  [`TAXONOMY_CHANGE_059`](../../research/taxonomy-changes/TAXONOMY_CHANGE_059.md).

## INF-305 — Successor exits preview reward class and elevated risk

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: before the player commits to one available successor exit, its
  visible marker discloses the class of reward admitted by that branch and any
  declared elevated encounter-risk category without exposing complete future
  contents.
- Includes: Hades chamber doors showing their next reward symbol and skull
  risk marker before Zagreus enters one available branch.
- Excludes: a complete generated route map; a marker shown only after entry;
  exact future enemy composition; external guide knowledge; a cosmetic door.
- Parameters: exit, reward class, risk category, availability, alternatives,
  preview marker, hidden contents and commitment transition.
- Evidence: [Hades decomposition](../games/g-l/hades.md).
- Novelty: first isolated for `GAME-0251`; prior route views either reveal a
  larger node graph or expose local door state without binding each immediate
  exit to a forecast reward and encounter-risk class.

## INF-306 — Run-upgrade offer exposes effect and capability consequence

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: a bounded run-upgrade offer exposes every current option's
  declared effect, rarity or level, affected capability and any replacement
  consequence before the player commits the exclusive choice.
- Includes: Hades Boon offers describing each eligible blessing and the
  Attack, Special, Cast, Dash or other current-build relation it changes.
- Excludes: hidden optimal-build advice; a reward icon with no option text;
  permanent account-upgrade trees; exact future synergy probability.
- Parameters: option, effect text, rarity, level, capability, current modifier,
  replacement, prerequisite feedback and selection count.
- Evidence: [Hades decomposition](../games/g-l/hades.md).
- Additional support: [Dead Cells decomposition](../games/a-f/dead-cells.md),
  for scroll and mutation offers stating each option's effect before the choice.
- Novelty: first isolated for `GAME-0251`; the interface explains one
  temporary capability-build commitment rather than only its reward class or
  the already-equipped build state.

## INF-307 — Negotiation interface exposes current estimated success

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: during one live authored negotiation, the interface displays a
  current estimate of successful resolution and updates it after registered
  evidence, responses or interventions without revealing the exact remaining
  branch sequence or guaranteeing the predicted endpoint.
- Includes: the changing success percentage during Detroit: Become Human's
  opening rooftop negotiation.
- Excludes: exact hit probability for one attack; a hidden relationship value;
  a post-result score; a complete future-state preview; external advice about
  the optimal response.
- Parameters: negotiation, estimate scale, display timing, update trigger,
  evidence, response, intervention, hidden factors and terminal treatment.
- Evidence: [Detroit: Become Human decomposition](../games/a-f/detroit-become-human.md).
- Novelty: first isolated for `GAME-0252`; the forecast summarises accumulated
  authored interaction state while the actual branch remains unresolved.

## INF-308 — Chapter branch map distinguishes traversed and locked paths

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: after an authored chapter settles, its branch-map interface marks
  the nodes and endpoint reached by the current retained path while preserving
  untraversed alternatives as locked, concealed or incomplete.
- Includes: the post-chapter and later revisitable flowchart for Detroit:
  Become Human's opening incident.
- Excludes: a linear objective list; a route map shown before decisions; a
  complete spoiler graph; global player percentages; an external walkthrough;
  branch state that disappears when the result surface closes.
- Parameters: chapter, traversed node, edge, endpoint, locked alternative,
  disclosure depth, completion marker and revisit surface.
- Evidence: [Detroit: Become Human decomposition](../games/a-f/detroit-become-human.md).
- Novelty: first isolated for `GAME-0252`; one retained result surface explains
  the path taken and the existence, but not necessarily identity, of missed
  authored alternatives.

## INF-309 — Focused tactical vision exposes occluded actors and threat classes

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: while a player-controlled tactical vision mode is active, the
  interface classifies nearby actors and relevant evidence through ordinary
  visual occlusion, including the equipment or condition that determines
  immediate threat, without permanently marking them after the mode ends.
- Includes: Detective Mode distinguishing nearby armed and unarmed inmates,
  guards and highlighted evidence during Batman: Arkham Asylum Game of the
  Year Edition's bounded opening Story Mode route.
- Excludes: avatar-centred ordinary sight and sound; an acquired persistent
  mark that survives after scanning; a complete future patrol route; an
  external walkthrough; a cosmetic colour filter with no state disclosure.
- Parameters: mode state, actor, occlusion, classification, equipment, threat
  state, evidence highlight, range, update timing and mode exit.
- Evidence: [Batman: Arkham Asylum Game of the Year Edition
  decomposition](../games/a-f/batman-arkham-asylum-game-of-the-year-edition.md).
- Novelty: first isolated for `GAME-0255`; a reversible focused overlay reveals
  current occluded actor and threat categories rather than storing individual
  reconnaissance marks or merely intensifying local visible clues.

## INF-310 — Incoming close-attack cue exposes a counter opportunity

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: a local visual cue identifies which nearby hostile has committed
  an eligible close attack and exposes the short opportunity for a reactive
  counter without guaranteeing that the response will be timed successfully.
- Includes: the counter icon above an attacking inmate during Batman: Arkham
  Asylum Game of the Year Edition's bounded opening Story Mode route.
- Excludes: a general hostile outline; a permanent enemy mark; an exact future
  attack timeline; a finisher cue on an already staggered target; a tutorial
  sentence that is not tied to the current incoming attack.
- Parameters: attacker, attack class, cue shape, cue onset, response interval,
  reach, overlap, expiry and failed-response feedback.
- Evidence: [Batman: Arkham Asylum Game of the Year Edition
  decomposition](../games/a-f/batman-arkham-asylum-game-of-the-year-edition.md).
- Novelty: first isolated for `GAME-0255`; the interface discloses one current
  reactive combat window rather than an enemy's general alert state or a
  staggered-finisher opportunity.

## INF-311 — Portable motion sensor exposes bounded direction and distance

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: while a portable local-motion sensor is raised, its interface
  exposes the direction sector and approximate distance of the nearest eligible
  moving actor, while withholding identity, stationary actors, exact world
  coordinate, route and future motion.
- Includes: Alien: Isolation's scoped motion tracker front cone, side/rear
  quarters and nearest-moving-actor distance display.
- Excludes: direct local sight; exact actor-bound marking; an omniscient minimap;
  stationary-resource survey; a passive threat-radius layer with no directional
  distance reading; player inference from external media.
- Parameters: observer, sensor, active view, range, eligible movement, nearest
  reading, sector resolution, distance resolution, refresh and concealed state.
- Evidence: [Alien: Isolation decomposition](../games/a-f/alien-isolation.md).
- Novelty: first isolated for `GAME-0257`; partial local movement becomes a
  device-bounded anonymous direction/distance channel without persistent actor
  identity or exact position.

## INF-312 — Ordinary object appearance can conceal current hostile identity

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: local sight can show an actor's current appearance as an ordinary
  eligible object without disclosing that the observed form retains hostile
  identity, so safety remains unresolved until movement, attack, testing or
  reveal provides additional current evidence.
- Includes: uncertainty over which apparently duplicated station prop is a
  concealed Mimic in Prey (2017)'s bounded lobby route.
- Excludes: ordinary line-of-sight occlusion; a known hostile behind cover; a
  purely decorative object; external walkthrough knowledge; a persistent scan
  that already labels the concealed actor; future disguise prediction.
- Parameters: observer, visible appearance, eligible object class, copied
  instance, hidden identity, comparison set, test, reveal event and expiry.
- Evidence: [Prey (2017) decomposition](../games/m-r/prey-2017.md), supported by
  Bethesda's static description of object mimicry and hidden threats.
- Novelty: first isolated for `GAME-0258`; the uncertainty is not where an
  already known hostile is but whether a currently ordinary-looking local
  object is itself the hostile actor.

## INF-313 — Layered body damage exposes regional severance progress

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: the live body itself exposes each eligible region's intact,
  peeled, structurally weakened or detached state and its remaining functional
  contribution, so the player can choose another regional attack without a
  conventional aggregate enemy health bar.
- Includes: visible skin, flesh, bone and intact-limb state during Dead Space
  (2023)'s bounded Chapter 1 combat.
- Excludes: a generic blood effect; a single health bar; hidden internal hit
  points; an external bestiary; a target marker unrelated to regional damage.
- Parameters: actor, region, layer set, degradation state, attachment,
  capability cue, threshold proximity and display persistence.
- Evidence: [Dead Space (2023 remake) decomposition](../games/a-f/dead-space-2023.md).
- Novelty: first isolated for `GAME-0259`; the body's visible layers disclose
  local progress toward a capability-changing detachment rather than aggregate
  survival alone.

## INF-314 — Local circuit panel exposes capacity and branch state

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: one authored control panel reveals its fixed available power,
  the identity and demand of each local fixture branch, and which branches are
  currently powered or unpowered before the next allocation choice.
- Includes: the Maintenance Bay breaker showing office, elevator and lights
  branches and their two-branch capacity in Dead Space (2023) Chapter 1.
- Excludes: a colony-wide economic power report; hidden wiring inferred from an
  external guide; vehicle performance gauges; a binary switch with no competing
  branch; future power demand beyond the panel.
- Parameters: panel, capacity, branch, demand, current state, available state,
  selected relation and rejection feedback.
- Evidence: [Dead Space (2023 remake) decomposition](../games/a-f/dead-space-2023.md).
- Novelty: first isolated for `GAME-0259`; a bounded local supply and every
  competing route/visibility branch are jointly legible at the choice surface.

## INF-315 — Worn equipment exposes remaining protected-breath duration

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: while environmental breathing equipment is relevant, its worn
  state and current filter reserve expose the remaining protected duration and
  replacement warning before exhaustion, without revealing future atmosphere
  boundaries or automatically selecting the next cartridge.
- Includes: the gas mask, wristwatch filter-time reading and replacement prompt
  during Metro Exodus's bounded `Moscow` chapter.
- Excludes: health alone; a hidden oxygen counter; weapon ammunition; an
  external walkthrough estimate; a map that reveals every future toxic region.
- Parameters: equipment, worn state, installed duration, display precision,
  warning threshold, carried replacement availability and update timing.
- Evidence: [Metro Exodus decomposition](../games/m-r/metro-exodus.md).
- Novelty: first isolated for `GAME-0260`; the interface predicts the remaining
  live protection interval of installed breathing equipment rather than only
  reporting accumulated environmental damage.

## INF-316 — Personal indicator exposes current visual illumination

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: an embodied personal indicator exposes whether the controlled
  actor's current position and illumination state place them in a locally
  visible or shadowed category before hostile detection necessarily completes,
  without identifying every observer or predicting future sightlines.
- Includes: the wristwatch visibility light during Metro Exodus's bounded
  `Moscow` infiltration.
- Excludes: an exact directional suspicion meter; a permanent actor mark;
  automatic hostile outlines; an external brightness setting; an indicator
  that reports only whether the player's flashlight is switched on.
- Parameters: actor, position, ambient illumination, carried light, visible or
  shadowed category, indicator state, observer independence and update timing.
- Evidence: [Metro Exodus decomposition](../games/m-r/metro-exodus.md).
- Novelty: first isolated for `GAME-0260`; a body-carried signal reports the
  actor's present light exposure before any particular hostile finishes
  perception, rather than reporting detection progress or lamp state alone.

## INF-317 — Authored placed instructions expose current control affordances

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: instructions authored by the developer and placed at fixed world
  positions disclose the control or risk relevant to that position when the
  player stands on them, without tracking progress, reporting completion or
  advancing an instruction chain.
- Includes: the fixed developer messages read from the ground during DARK
  SOULS III's bounded `Cemetery of Ash` route; the fixed control and Focus
  instruction tablets encountered on Hollow Knight's bounded opening route.
- Excludes: a tutorial adviser that states the current objective and reports
  its completion; a persistent objective or route marker; a message authored by
  another player; an ordinary resource or combat HUD.
- Parameters: placement, trigger radius, disclosed control or hazard, wording
  and whether the message persists after being read.
- Evidence: [DARK SOULS III decomposition](../games/a-f/dark-souls-iii.md)
  and [Hollow Knight decomposition](../games/g-l/hollow-knight.md).
- Novelty: first isolated for `GAME-0262`; instruction is delivered by world
  position alone, so the player learns a control only by reaching the place
  where it matters and never receives a completion signal.

## INF-318 — Sealed encounter exposes the guardian's remaining health

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: while a sealed mandatory encounter is live, a dedicated surface
  identifies the guardian by name or encounter presence and continuously exposes its remaining share of health, so
  the player can judge accumulated progress and approaching thresholds without
  seeing its attack selection.
- Includes: the named guardian bar shown during DARK SOULS III's bounded
  `Cemetery of Ash` encounter; the first colossus's encounter health display in
  Shadow of the Colossus.
- Excludes: ordinary field-enemy health; a hunt interface that withholds exact
  monster health; a preview of the opponent's next committed action; the
  player's own resource display.
- Parameters: guardian name, bar granularity, threshold visibility, appearance
  and dismissal conditions.
- Evidence: [DARK SOULS III decomposition](../games/a-f/dark-souls-iii.md).
- Additional support: [Shadow of the Colossus decomposition](../games/s-z/shadow-of-the-colossus.md),
  where encounter presence rather than an on-screen name identifies the one
  active guardian.
- Novelty: first isolated for `GAME-0262`; the disclosure is bounded to one
  sealed encounter and reports only accumulated damage, leaving the guardian's
  behaviour change to be inferred from that share alone.

## INF-319 — Attack cues distinguish which defensive response is legal

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: a visible cue attached to an incoming attack sorts it into
  declared categories that differ in which defensive response can succeed, so
  the player reads the required response type before choosing when to commit
  it.
- Includes: the distinct cue colours separating a parryable attack from an
  unblockable attack during God of War's bounded opening route.
- Excludes: a cue that only exposes an attack's timing or rhythm; a cue that
  only identifies which hostile is attacking; an exact numeric window; a
  post-hit report of what would have worked.
- Parameters: cue form, category set, mapped legal responses, visibility range
  and lead time before contact.
- Evidence: [God of War decomposition](../games/g-l/god-of-war.md).
- Novelty: first isolated for `GAME-0263`; the disclosure selects the response
  type rather than its instant, so reading it wrong fails even with perfect
  timing.

## INF-320 — The offered check discloses its odds and contributing modifiers

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: before commitment, an option carrying an attribute check exposes
  its declared difficulty, its computed success odds and the individual terms
  that currently raise or lower them, so the player can see what would have to
  change to improve the attempt.
- Includes: the odds and modifier breakdown shown on an active check during
  Disco Elysium - The Final Cut's bounded opening episode.
- Excludes: a post-resolution report of what happened; a bare difficulty label
  with no odds; a hidden probability; a forecast of an already committed
  hostile action.
- Parameters: difficulty label, numeric odds, listed modifier terms, retry
  class indicator and the display's update on state change.
- Evidence: [Disco Elysium - The Final Cut decomposition](../games/a-f/disco-elysium-the-final-cut.md).
- Novelty: first isolated for `GAME-0264`; the interface exposes the
  arithmetic of its own uncertainty, turning preparation into a legible plan
  rather than a guess.

## INF-321 — Commentary is attributed to the named faculty that produced it

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: each line of internally generated commentary is labelled with the
  specific named attribute that generated it, so the player can weigh a
  disclosure against that attribute's known reliability instead of receiving
  one undifferentiated authorial voice.
- Includes: the named skill voices that speak during dialogue and examination
  in Disco Elysium - The Final Cut's bounded opening episode.
- Excludes: an unattributed narrator; a tutorial adviser; subtitles for a
  companion who exists in the world; a log that records events without
  interpreting them.
- Parameters: faculty names, attribution form, reliability implied by the
  attribute's value and whether the disclosure can be contradicted.
- Evidence: [Disco Elysium - The Final Cut decomposition](../games/a-f/disco-elysium-the-final-cut.md).
- Novelty: first isolated for `GAME-0264`; information carries the identity of
  its source inside the character, so the same sentence is trusted differently
  depending on which faculty said it.

## INF-322 — Placement preview exposes the defender's effective coverage

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: while a defender is being positioned, the interface draws the
  exact reach it would have at the current candidate position, so the player
  can see which part of the fixed hostile route the placement would cover
  before committing to it.
- Includes: the reach indicator drawn around a monkey while it is being placed
  and when it is later selected, during Bloons TD 6's bounded Easy standard
  route.
- Excludes: a preview that only reports whether the position is legal; a fog or
  vision overlay derived from allied units; a minimap; a marker showing where a
  hostile currently is.
- Parameters: reach shape and size, candidate position, route overlap, upgrade
  effect on reach and whether the indicator persists after placement.
- Evidence: [Bloons TD 6 decomposition](../games/a-f/bloons-td-6.md).
- Novelty: first isolated for `GAME-0265`; the disclosure is geometric and
  prospective, so the placement decision is made against a drawn intersection
  rather than against an inferred one.

## INF-323 — Defence interface exposes budget, stock and schedule position

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the interface exposes the current spendable budget, the remaining
  shared defence stock and the current index within a finite authored schedule
  at the same time, so any purchase can be priced against both the damage
  already absorbed and the number of scheduled waves still to come.
- Includes: the simultaneous cash, lives and round display during Bloons TD 6's
  bounded Easy standard route.
- Excludes: a controlled character's personal health and resources; an itemised
  recurring budget ledger; a preview of the next wave's exact composition; a
  post-attempt score summary.
- Parameters: budget value, stock value, current and final schedule index and
  the update moment of each.
- Evidence: [Bloons TD 6 decomposition](../games/a-f/bloons-td-6.md).
- Novelty: first isolated for `GAME-0265`; this is the disclosure surface the
  packet's single pricing decision is taken against — the interface exposes the
  balance a commitment must fit, the damage the defence has already absorbed and
  how much of the finite schedule is left to survive, which is what makes a
  purchase, a conceded leak and a deferred upgrade comparable at all.

## INF-324 — The projected path exposes its extreme altitudes before commitment

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Limited`
- Confidence: `Medium`
- Definition: a dedicated view draws the path the craft would follow under its
  current motion alone and labels that path's highest and lowest points, so the
  player can compare both against a declared threshold and decide when and how
  hard to act before the motion carries them past the useful moment.
- Includes: the map view's projected trajectory with its labelled apoapsis and
  periapsis during Kerbal Space Program's bounded Sandbox orbit task.
- Excludes: cockpit instruments reporting only present attitude, speed and
  altitude; a placement preview showing a static reach; a marker showing where
  a hostile currently is; a post-manoeuvre report of what happened.
- Parameters: projection basis, drawn path, labelled extremes, threshold
  comparison, update rate and whether a planned manoeuvre can be previewed.
- Evidence: [Kerbal Space Program decomposition](../games/g-l/kerbal-space-program.md).
- Novelty: first isolated for `GAME-0267`; the disclosure is a prediction of
  the player's own uncorrected future rather than a description of the present,
  so acting on it is what prevents it from coming true.

## INF-325 — The interface marks which opponents may currently be released

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Limited`
- Confidence: `Medium`
- Definition: the encounter interface distinguishes, before the player commits,
  which opponents have satisfied their release condition and which have not,
  by marking the release option or the opponent's own entry differently while
  leaving the condition that produced the change undisclosed.
- Includes: the coloured release option and monster name that signal
  eligibility during Undertale's bounded opening route.
- Excludes: a numeric success chance shown before an attempt; a health bar; an
  exposed stagger or finisher opportunity; a post-attempt report of why an
  option failed.
- Parameters: marker form, what it distinguishes, when it updates and how much
  of the underlying condition it leaves hidden.
- Evidence: [Undertale decomposition](../games/s-z/undertale.md).
- Novelty: first isolated for `GAME-0268`; the disclosure states that mercy is
  now possible without stating why, so the player is told the result of their
  experimentation but not the rule behind it.

## INF-326 — The voyage interface prices another catch against the remaining day

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the interface exposes the current position on the world clock, the
  space the carried grid still has free and the condition of what is already
  carried at the same time, so the player can judge whether one more acquisition
  fits, whether it can be reached and returned before the declared boundary, and
  what the delay costs the cargo already held.
- Includes: the time-dial's day and hour shown beside the hold's free cells and
  each fish's freshness state during DREDGE's bounded first-day route.
- Excludes: a personal health, stamina or sanity readout by itself; a shop's
  prices and current money; a match clock and score; an itemised recurring
  budget; a projected path's extreme values.
- Parameters: clock display, declared boundary, free-space measure, carried
  condition states and the update moment of each.
- Evidence: [DREDGE decomposition](../games/a-f/dredge.md).
- Novelty: first isolated for `GAME-0269`; this is the disclosure surface the
  packet's single gathering decision is taken against — the interface exposes
  how much of the bounded day is left, how much room the hold still has and what
  the delay has already cost the cargo, which is what makes one more acquisition,
  an earlier return and a deferred sale comparable at all.

## INF-327 — The interface names the run's current escalation tier

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the live interface exposes the run's current escalation as a named
  ordered tier alongside the elapsed run clock, so the player can read how far
  the world has already been strengthened, and see it change, without being told
  the value or the formula behind it.
- Includes: the named ordered difficulty bar shown beside the run timer in Risk
  of Rain 2's bounded first-environment route.
- Excludes: a difficulty setting chosen before the attempt; a numeric enemy level
  on one hostile; a match clock and score; a wave or round index; a post-attempt
  result summary.
- Parameters: tier names, ordering, the value bands they cover, update moment and
  how much of the underlying value the display withholds.
- Evidence: [Risk of Rain 2 decomposition](../games/m-r/risk-of-rain-2.md).
- Novelty: first isolated for `GAME-0270`; the disclosure turns a continuously
  rising hidden value into a small number of readable states, so the decision to
  linger is informed without being calculable.

## INF-328 — Region interface exposes accumulated progress and its next gate

- Lifecycle: `Merged`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: historical parameter-specific duplicate now represented by the
  generalised active boundary `INF-207`.
- Includes: historical references that used `INF-328` during the Batch 016
  candidate pass.
- Excludes: current signatures and new analysis; use `INF-207`.
- Parameters: none; retained as an auditable alias.
- Evidence: [Far Cry 5 decomposition](../games/a-f/far-cry-5.md) and
  [`TAXONOMY_CHANGE_033`](../../research/taxonomy-changes/TAXONOMY_CHANGE_033.md).
- Merged into: `INF-207` by
  [`TAXONOMY_CHANGE_033`](../../research/taxonomy-changes/TAXONOMY_CHANGE_033.md).

## INF-329 — Task interface exposes aggregate and per-target completion

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: the interface exposes a bounded task's aggregate completion
  measure and the accepted completion state of its named component targets, so
  the player can identify which target still prevents settlement.
- Includes: PowerWash Simulator's overall job percentage, the Details list of
  vehicle parts and each part's completion percentage during the first Career
  job.
- Excludes: a score shown only after settlement; a checklist without measured
  target state; a minimap of explored space; a quality grade; an on-demand
  world highlight that locates residual state spatially.
- Parameters: aggregate measure, target partition, per-target measure,
  precision, accepted threshold and update timing.
- Evidence: [PowerWash Simulator decomposition](../games/m-r/powerwash-simulator.md).
- Novelty: first isolated for `GAME-0279`; the measure is what converts an
  open-ended activity into a task with a knowable end.

## INF-330 — Live service surface exposes requests and waiting pressure

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: during a live service session, the interface identifies each
  current request and exposes its changing wait state together with enough
  preparation or readiness feedback to decide which compatible delivery should
  be completed next.
- Includes: dish or drink requests above customers, visible impatience progress
  and the current prepared-dish state during DAVE THE DIVER's bounded first
  restaurant service.
- Excludes: one static requested-item picture with no concurrent queue or time
  pressure; a concealed future demand schedule; a post-session sales report; a
  global shift clock that does not distinguish individual requests.
- Parameters: requester, requested item, preparation or ready marker, wait-state
  granularity, urgency cue, compatibility and update timing.
- Evidence: [DAVE THE DIVER decomposition](../games/a-f/dave-the-diver.md).
- Novelty: first isolated for `GAME-0278`; the information surface makes
  parallel expiring requests prioritizable without revealing future arrivals.

## INF-331 — On-demand overlay locates residual target state

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: on request, the interface marks residual eligible state in the
  active world or marks the selected incomplete component as a spatial whole,
  letting the player search its geometry without changing that target state.
- Includes: PowerWash Simulator's Dirt Highlight flash for remaining dirt and
  the Details selection that flashes one incomplete vehicle part.
- Excludes: aggregate or per-target percentages without spatial location; a
  permanent objective waypoint; highlighting a legal attack target; a hint
  that changes or solves the target state.
- Parameters: request control, residual-state predicate, selected component,
  highlight colour, duration, occlusion and refresh timing.
- Evidence: [PowerWash Simulator decomposition](../games/m-r/powerwash-simulator.md).
- Novelty: first isolated for `GAME-0279`; it separates measured incompleteness
  from the optional spatial query used to find the remaining area.

## INF-332 — Shared expedition light meter and its threshold band are visible

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: throughout an expedition a persistent interface element exposes
  the party's shared light meter as its current value and the named threshold
  band that value falls in, together with the band's declared effect icons, so
  the player can read the current danger-and-reward regime before travel,
  battle, loot and any manual change to the meter.
- Includes: the Darkest Dungeon torch meter shown at the top of the screen
  with its band from Radiant Light to Black as Pitch and its effect icons,
  read before each corridor step and before snuffing, in the scoped Old Road
  tutorial.
- Excludes: a personal light or visibility indicator (`INF-316`); a run
  escalation tier that withholds its underlying value (`INF-327`); daily
  spendable resource counts without a modifier band (`INF-212`); the
  controlled hero's own resources (`INF-119`); the meter's decay and band
  effects themselves (`SYS-829`); the snuff command (`ACT-449`).
- Parameters: meter range, band names and thresholds, effect icons shown,
  modifiers withheld from the display and placement of the element.
- Evidence: [Darkest Dungeon decomposition](../games/a-f/darkest-dungeon.md).
- Novelty: first isolated for `GAME-0281`; one always-present element
  discloses a shared, player-depletable meter and the regime it currently
  selects, which no personal-meter or escalation-tier disclosure covers.

## INF-333 — Per-unit remaining-action markers are visible without the resolution order

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: during a combat round every friendly and hostile unit carries a
  marker showing whether it still has an action to take in the current round,
  the marker clearing as the unit acts, while the order in which the remaining
  units will act is not disclosed.
- Includes: the Darkest Dungeon gold pips beside each hero's and brigand's
  health bar, whose tooltip reads as actions remaining, in the scoped Old Road
  tutorial.
- Excludes: an exposed upcoming combatant order (`INF-141`); a telegraphed
  hostile intent (`INF-061`); the selected unit's own remaining action budget
  alone (`INF-220`, `INF-190`); the hidden initiative roll itself (`INF-002`).
- Parameters: marker form, units carrying markers, multi-action units, tooltip
  text and whether corpses or stunned units display a marker.
- Evidence: [Darkest Dungeon decomposition](../games/a-f/darkest-dungeon.md).
- Novelty: first isolated for `GAME-0281`; the disclosure is the set of units
  yet to act, not their sequence, which separates it from every exposed-order
  and personal-action-budget gene.

## INF-334 — An engaged hostile's breakable stability state is visible

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: during a live encounter the interface exposes the selected or
  engaged hostile's current breakable stability state separately from health,
  including its movement toward or recovery away from the break threshold, so
  the player can decide whether to maintain pressure before the state recovers.
- Includes: the enemy Posture display in Sekiro's bounded opening route.
- Excludes: remaining critical-execution requirements (`INF-335`); a health bar
  without a separate stability state (`INF-318`); a brief contextual execution
  opportunity (`INF-295`); visible regional component damage (`INF-313`); the
  stability-break transition itself (`SYS-409`); a post-battle result report.
- Parameters: hostile, stability measure, bar direction, recovery, break
  threshold, visibility conditions, precision and update timing.
- Evidence: [Sekiro decomposition](../games/s-z/sekiro-shadows-die-twice.md),
  using the official PC manual's Posture description.
- Novelty: first isolated for `GAME-0288`; narrowed by
  [`TAXONOMY_CHANGE_066`](../../research/taxonomy-changes/TAXONOMY_CHANGE_066.md)
  to the independently visible stability state after the execution count was
  extracted from the former compound disclosure.

## INF-335 — Remaining critical executions required to defeat a protected hostile are visible

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: during a live encounter the interface exposes a discrete count of
  critical executions still required to settle one protected hostile's final
  defeat; each accepted execution removes one displayed requirement, allowing
  the player to distinguish an intermediate execution from the terminal one.
- Includes: Deathblow markers above the health gauge of a strong enemy in
  Sekiro's bounded opening route, including the two markers removed in sequence
  to defeat the required guardian.
- Excludes: the hostile's breakable stability state (`INF-334`); a temporary
  contextual execution opportunity (`INF-295`); accumulated round wins
  (`INF-210`); remaining participant stocks (`INF-254`); living-participant
  totals (`INF-129`); guardian health alone (`INF-318`); task-component progress
  (`INF-329`); hidden encounter phases; the sequential-execution settlement
  itself (`SYS-847`).
- Parameters: protected hostile, required execution count, marker form,
  decrement timing, intermediate-survival indication, final marker and
  visibility conditions.
- Evidence: [Sekiro decomposition](../games/s-z/sekiro-shadows-die-twice.md),
  using the official PC manual's Deathblow-marker description.
- Novelty: extracted from former compound `INF-334` by
  [`TAXONOMY_CHANGE_066`](../../research/taxonomy-changes/TAXONOMY_CHANGE_066.md);
  the discrete remaining requirement transfers independently of how a critical
  opportunity is created or exposed.

## INF-336 — Calendar date and current day period are visible

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the campaign interface exposes the current calendar date and its
  active authored day period before the player commits the next available
  activity, traversal or story action.
- Includes: Persona 5 Royal's April date, weekday and current school,
  after-school or evening segment during the bounded 9–12 April opening.
- Excludes: a complete future schedule; exact hidden event triggers; a survival
  clock coupled to food, crops, utilities or weather (`INF-136`); an external
  elapsed-time result.
- Parameters: calendar system, date, weekday, period, current activity and
  transition cue.
- Evidence: [Persona 5 Royal decomposition](../games/m-r/persona-5-royal.md).
- Novelty: first isolated for `GAME-0291`; earlier time displays either bundle
  the date with simulation resources or expose deadlines and results rather
  than the authored campaign segment itself.

## INF-337 — Wand inspection exposes spell sequence and casting statistics

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the carried-wand surface shows slot contents and order together
  with shuffle state, spells per cast, mana, cast delay and recharge statistics
  before the player selects or fires that wand.
- Includes: inspecting both starting wands and any replacement during Noita's
  scoped first-Mines descent.
- Excludes: hidden future wand generation; Holy Mountain spell editing; a
  generic weapon damage number without an executable spell composition.
- Parameters: wand, slots, spell order, shuffle, spells per cast, mana maximum,
  mana recharge, cast delay, recharge time, spread and current selection.
- Evidence: [Noita decomposition](../games/m-r/noita.md).
- Novelty: first isolated for `GAME-0296`; one information surface exposes both
  a portable program sequence and the statistics that schedule its execution.

## INF-338 — Local material and current stain state are visible

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the live view identifies aimed or contacted world material and
  exposes the actor's current material-derived stain or status with its visible
  remaining amount before the next movement or application decision.
- Includes: distinguishing water, toxic sludge and burning material and reading
  Wet, toxic or On Fire state during Noita's scoped first-Mines descent.
- Excludes: unrevealed off-screen substances; hidden alchemical recipes; a
  generic health bar; inventory capacity without world-material identity.
- Parameters: cursor or contact target, material name, colour, stain name,
  percentage or duration, status icon and update cadence.
- Evidence: [Noita decomposition](../games/m-r/noita.md).
- Novelty: first isolated for `GAME-0296`; the surface joins world-substance
  identity to the temporary bodily coating created from that substance.

## INF-339 — Current large-monster positions are visible before species identification

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: from quest start the field map exposes the current position of
  each present large monster, using a generic mark until first encounter or
  retained prior knowledge reveals its species-specific icon.
- Includes: MONSTER HUNTER RISE's map during the scoped first Great Izuchi
  Village hunt, where current large-monster position does not require trace
  collection.
- Excludes: evidence-fed scoutfly acquisition and route updates (`INF-158`);
  exact hidden health; small-monster positions; an external map guide; hidden
  species identity before the game reveals it.
- Parameters: quest, large monster, current position, common icon, encounter,
  known identity, specific icon, movement update and map visibility.
- Evidence: [MONSTER HUNTER RISE decomposition](../games/m-r/monster-hunter-rise.md),
  using Capcom's official map support guidance.
- Novelty: first isolated for `GAME-0297`; location is immediately disclosed
  even when identity is not, unlike tracking systems whose position or route
  becomes available only after collected evidence.

## INF-340 — Each shared ability unit's ready or recovering state is visible

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: the live interface separately represents every unit in a small
  shared ability pool and visibly distinguishes ready units from units still
  progressing through their individual recovery.
- Includes: MONSTER HUNTER RISE's Wirebug Gauge during Wiredash, Long Sword
  Silkbind and Wirefall in the scoped first Village hunt.
- Excludes: one undivided stamina bar; hidden cooldowns; ammunition count; an
  ability list that shows only binary global readiness.
- Parameters: pool, unit count, ready state, recovering state, progress,
  temporary extra unit, expiry and display cadence.
- Evidence: [MONSTER HUNTER RISE decomposition](../games/m-r/monster-hunter-rise.md),
  using Capcom's official Wirebug Action and game-screen manual.
- Novelty: first isolated for `GAME-0297`; the display lets the player reserve
  one unit for recovery while another independently recharges after a
  different movement or combat commitment.

## INF-341 — Expose the current zoo task and species-care requirements

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: the current scenario instruction and animal information views
  expose the required action or destination and species-specific welfare,
  habitat and enrichment needs before the next zoo-editing commitment.
- Includes: Goodwin House's active tutorial objective, animal welfare panel
  and Zoopedia requirements for Common Warthogs and Ostriches.
- Excludes: a hidden future task list; a guaranteed prediction of exact
  welfare values after placement; changing the zoo merely by opening a panel.
- Parameters: stage, highlighted destination, species, care category, current
  welfare, suitable fixture and display timing.
- Evidence: [Planet Zoo: Console Edition decomposition](../games/m-r/planet-zoo-console-edition.md),
  using Frontier's beginner and animal guides.
- Novelty: first isolated for `GAME-0298`; scenario guidance and species
  diagnostics jointly inform the next habitat action.

## INF-342 — Expose enemy exertion and a burst-response cue

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: the live encounter displays an opponent's current exertion or
  break state and visibly announces a special incoming attack early enough
  for a player to choose a legal reactive counter.
- Includes: Nioh 2 opponent Ki gauge and red burst-attack flash in the
  first mission, including the Mezuki encounter.
- Excludes: the player's own Ki or Anima gauges; a prediction of every future
  attack; an invisible enemy recovery threshold; the counter action itself.
- Parameters: opponent, Ki bar, break cue, special-attack flash, timing and
  eligible response.
- Evidence: [Nioh 2 decomposition](../games/m-r/nioh-2.md), using Sony's
  opening-hours guide and two written first-mission routes.
- Novelty: first isolated for `GAME-0299`; opponent readiness and the
  particular prompted response are simultaneously decision-visible.

## INF-343 — Expose combat turn order, AP and target health

- Lifecycle: `Active`
- Claim status: `Pattern`
- Evidence quality: `Corroborated`
- Confidence: `Medium`
- Definition: during a turn-based encounter the interface shows the current
  actor, upcoming combat order, that actor's available Action Points and the
  selected target's health before a movement or attack commitment.
- Includes: the two-Voidling main-deck fight in Divinity: Original Sin 2 -
  Definitive Edition on Classic difficulty.
- Excludes: a Break gauge (`INF-141`); exact future enemy actions; later
  physical/magic armour status not exercised by this unarmoured encounter.
- Parameters: actor, queue horizon, current AP, target, health and visibility.
- Evidence: [Divinity: Original Sin 2 - Definitive Edition decomposition](../games/a-f/divinity-original-sin-2-definitive-edition.md),
  supported by the PC Definitive Edition AP guide and written ship route.
- Novelty: first isolated for `GAME-0301`; this opening's actionable combat
  display lacks the Break-state boundary of the nearest existing HUD gene.

## INF-344 — Race HUD exposes item order, coins and incoming threats

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: during a live race, the interface exposes the active held item,
  any reserve item, current course-coin total and warnings for eligible incoming
  threats, while leaving future random item results and rival inputs concealed.
- Includes: Mario Kart 8 Deluxe's two item slots, coin counter and Red/Spiny
  Shell or comparable incoming-attack warnings in the scoped Grand Prix.
- Excludes: current place and lap (`INF-205`); the post-race point table;
  exact hidden item probabilities; an omniscient map of every projectile.
- Parameters: active slot, reserve slot, item identity, coin total, threat
  class, warning direction, urgency, visibility and concealment horizon.
- Evidence: [Mario Kart 8 Deluxe decomposition](../games/m-r/mario-kart-8-deluxe.md),
  using Nintendo's item guidance, update notes and preserved race manual.
- Novelty: first isolated for `GAME-0309`; one racing surface joins an ordered
  transient inventory and capped speed resource to reactive attack warnings.

## INF-345 — Cargo interface exposes load, condition and delivery settlement

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: cargo and result interfaces expose carried package identities,
  body positions, total mass, capacity, centre of gravity, container or cargo
  condition and the accepted order's evaluation sufficiently to audit the
  current load and terminal result.
- Includes: the scoped DEATH STRANDING DIRECTOR'S CUT opening order.
- Excludes: hidden future weather; an external package manifest; a truck-only
  economic settlement; undiscovered cargo outside sensor range.
- Parameters: package, position, mass, limit, centre of gravity, container
  condition, cargo condition, accepted quantity, grade and Likes.
- Evidence: [DEATH STRANDING DIRECTOR'S CUT decomposition](../games/a-f/death-stranding-directors-cut.md).
- Novelty: first isolated for `GAME-0310`; one evidence chain joins spatial
  body-load state to the condition-aware accepted delivery result.

## INF-346 — Scan and map expose terrain risk and an unsolved marked route

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: local scan feedback and a topographic map expose terrain classes,
  elevation, nearby eligible cargo and the player's linked route markers while
  leaving exact traversability and route success unresolved.
- Includes: Odradek terrain/cargo feedback and linked map markers in the scoped
  DEATH STRANDING DIRECTOR'S CUT opening order.
- Excludes: a complete solved path; exact future weather; permanent visibility
  of unscanned cargo; road turn-by-turn navigation.
- Parameters: terrain class, elevation, hazard colour, cargo marker, scan
  lifetime, route marker, line segment and world projection.
- Evidence: [DEATH STRANDING DIRECTOR'S CUT decomposition](../games/a-f/death-stranding-directors-cut.md).
- Novelty: first isolated for `GAME-0310`; transient local survey and authored
  topographic planning share one incomplete route-reading surface.

## INF-347 — Platform stage exposes score, attempt resources, time and lives

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: a live platform-stage interface exposes accumulated score,
  current route-resource count, stage identity when applicable, elapsed or
  remaining attempt time and finite life stock while world or avatar feedback
  discloses relevant temporary capability and checkpoint state.
- Includes: the original Super Mario Bros. World 1-1 HUD plus small, Super,
  Fiery and temporary Star presentation; original Sonic the Hedgehog's score,
  elapsed time, rings, lives, temporary-state feedback, activated lamppost and
  signpost closeout.
- Excludes: hidden future block contents; complete future route geometry; a
  results-only score table; emulator overlays.
- Parameters: score, route resource, area, elapsed or remaining time, lives,
  avatar/world state, checkpoint feedback, temporary-state feedback and update
  timing.
- Evidence: [Super Mario Bros. decomposition](../games/s-z/super-mario-bros.md),
  using Nintendo's preserved manual and pinned original-game disassembly.
- Additional support: [Sonic the Hedgehog decomposition](../games/s-z/sonic-the-hedgehog.md),
  using SEGA's preserved manual and pinned deterministic disassembly.
- Novelty: first isolated for `GAME-0311`; one compact stage surface joins
  route identity and deadline with score economy and capability state.

## INF-348 — Fixed arena and HUD expose assault, base and life state

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: one fixed top-down combat surface exposes the current arena,
  protected base, visible vehicles, projectiles, terrain and created bonus
  together with stage, remaining-hostile and player-life status, while declared
  occluding terrain may conceal bodies and future random results stay unknown.
- Includes: Tank 1990 Stage 1 with its eagle, tanks, bullets, visible bonus,
  vegetation occlusion and stage/enemy/life counters.
- Excludes: a camera showing only a moving local slice; complete knowledge of
  hidden tanks under vegetation; the next random bonus identity; an external
  emulator overlay.
- Parameters: arena extent, visible entities, occluding terrain, stage label,
  hostile reserve display, life display, score and update timing.
- Evidence: [Tank 1990 decomposition](../games/s-z/tank-1990.md), using the
  pinned inherited display logic and corroborating reimplementation.
- Novelty: first isolated for `GAME-0313`; the whole defended arena and its
  finite-assault status share one surface with an explicit occlusion exception.

## INF-349 — Visor motion tracker exposes nearby moving contacts by allegiance

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: a continuously available avatar-centred tracker exposes the
  relative bearing of nearby eligible moving or firing entities and classifies
  friendly versus hostile contacts, while withholding elevation, exact
  identity, route and stationary actors.
- Includes: Halo 3's visor Motion Tracker during the scoped original-Xbox-360
  `Sierra 117` mission.
- Excludes: direct local sight; an omniscient map; a portable sensor that must
  be raised and reports only one anonymous direction/distance reading; a
  teammate-shared spotted-target network; stationary-contact disclosure.
- Parameters: observer, range, eligible motion or fire, relative bearing,
  allegiance class, vehicle-size marker, update interval, stationary state,
  elevation and concealed identity.
- Evidence: [Halo 3 decomposition](../games/g-l/halo-3.md), using the original
  Xbox 360 manual and licensed launch-era HUD guide.
- Novelty: first isolated for `GAME-0315`; the passive visor layer classifies
  multiple current moving contacts by allegiance but deliberately omits their
  elevation and stationary presence.

## INF-350 — Brawler HUD and viewpoint expose life, combat form and boss-counter state

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: a scrolling combat-stage presentation joins current health,
  finite lives and score with the controlled body's visible ordinary, held-tool
  or mounted form; a declared boss may replace that view with its aiming cue
  and cumulative counter-damage state without revealing future trajectories.
- Includes: Ragnarok's Canyon exposing Toad energy, lives and points, the held
  Walker leg or ridden Dragon, then Tall Walker's crosshair, firing cue and
  increasingly cracked boss-view screen.
- Excludes: a platform HUD whose defining route state is coins and a countdown;
  a fixed whole-arena hostile-reserve display; hidden off-screen enemies; exact
  future boss shots or collision results.
- Parameters: health display, life stock, score, combat form, held capability,
  mount state, boss viewpoint, aim cue, cumulative damage and update timing.
- Evidence: [Battletoads decomposition](../games/a-f/battletoads.md), using the
  original manual's scoreboard and independent written Stage 1 boss accounts.
- Novelty: first isolated for `GAME-0318`; one stage surface must survive a
  temporary viewpoint reversal while keeping finite-life and counter progress
  readable.

## INF-351 — Treasure map and ship chart expose an unresolved correspondence

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: one held treasure map exposes an unlabeled destination outline,
  local landmarks and a marked target while a separate ship chart exposes
  named world geography, vessel position and player marks; the player must
  infer the correspondence because neither surface identifies or routes it.
- Includes: matching the Gold Hoarders Tutorial Voyage's X-marks-the-spot map
  to a small island on the Sea of Thieves Sloop chart before sailing and digging.
- Excludes: a quest marker that names the correct destination; automatic GPS
  routing; an explored minimap that already overlays the target; an external map.
- Parameters: treasure-map silhouette, landmark, marked point, chart scale,
  island geometry, names, vessel position, player mark and absent route solution.
- Evidence: [Sea of Thieves decomposition](../games/s-z/sea-of-thieves.md),
  using the official Gold Hoarders guide and corroborated tutorial notifications.
- Novelty: first isolated for `GAME-0319`; the decision depends on comparing
  two incomplete spatial representations rather than reading one disclosed marker.

## INF-352 — Wildlife cues expose target state and caught identity

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: local presentation distinguishes currently targetable wildlife
  through its visible body or water shadow, exposes the active capture cue and
  reports a successful specimen's species plus prior catalogue credit, while
  withholding the identity of an unseen or future instance.
- Includes: fish shadows, bobber nibbles and bite, visible insects, catch reveal
  and Critterpedia credit in Animal Crossing: New Horizons.
- Excludes: a complete future spawn table; hidden exact catch probability;
  museum-completion state; generic world sight with no capture-state cue.
- Parameters: target representation, cue sequence, species reveal, new/known
  catalogue state, habitat, occlusion, despawn and feedback timing.
- Evidence: [Animal Crossing: New Horizons decomposition](../games/a-f/animal-crossing-new-horizons.md),
  using Nintendo's beginner guide and corroborating first-day routes.
- Novelty: first isolated for `GAME-0320`; the same information boundary spans
  pre-capture targeting, action timing and post-capture identity credit.

## INF-353 — Active-reload indicator exposes timing bands and grade

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: during a reload, the combat interface exposes the moving active-
  reload marker and authored success/perfect/failure regions before the optional
  second press, then reports the accepted grade and changed readiness outcome.
- Includes: the original Xbox 360 Gears of War active-reload indicator and its
  success, perfect and failure feedback.
- Excludes: ammunition count alone; a hidden reload-speed modifier; weapon heat
  cooling with no reserve-ammunition transfer; exact future hostile action.
- Parameters: selected weapon, marker, timing track, success region, perfect
  region, failure region, accepted grade and feedback duration.
- Evidence: [Gears of War decomposition](../games/g-l/gears-of-war.md), using
  the original manual's HUD and active-reload pages.
- Novelty: first isolated for `GAME-0321`; the current finite-ammunition reload
  exposes a three-grade intervention surface rather than only remaining stock.

## INF-354 — Late clearance exposes the exact remaining-hostile count

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: once a full-clear objective reaches its declared low remaining
  threshold, the quest surface reports the exact number of required living
  hostiles still preventing settlement without revealing their positions.
- Includes: the five-or-fewer monster counter in Diablo II: Resurrected's
  scoped `Den of Evil` quest.
- Excludes: a permanent marker over every enemy; a boss health bar; the total
  number before the threshold; a counter that ignores reanimated hostiles.
- Parameters: objective, threshold, required hostile set, current living count,
  update timing, concealment and settlement value.
- Evidence: [Diablo II: Resurrected decomposition](../games/a-f/diablo-ii-resurrected.md).
- Novelty: first isolated for `GAME-0322`; exact quantity arrives only for the
  final search and narrows omission without disclosing spatial answers.

## INF-355 — Command surface exposes roster assignment and power-up gauge state

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: the joined stage HUD and paused command surface expose the
  directly controlled roster member and finite life stock, that member's
  ordered power-up gauge and active tier, and every available member's current
  direct-control, unused or autonomous-plan assignment before confirmation.
- Includes: Contra Force's one-player HUD and Command Select surface during the
  scoped first mission.
- Excludes: concealed future enemies; a match-draft interface before play;
  equipment statistics outside the active row; exact future partner pathing or
  attack targets; a life display with no roster or gauge state.
- Parameters: roster, controlled member, life stock, ordered gauge, highlight,
  active tier, assignment, available plans, confirmation and return to play.
- Evidence: [Contra Force decomposition](../games/a-f/contra-force.md), using
  the original North American NES manual's display and command rules.
- Novelty: first isolated for `GAME-0324`; one actionable surface must make a
  character-local upgrade row and mutually exclusive direct/support roster
  roles legible before either selection changes live play.

## INF-356 — Dungeon display joins current room, acquired outline and compass objective

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: the live dungeon information surface distinguishes the actor's
  current room and explored route, the authored room outline supplied by an
  acquired map, and the objective position supplied by an acquired compass,
  alongside the health, currency, key and selected-item state needed for the
  next room decision.
- Includes: The Legend of Zelda's scoped Level-1 Eagle display after collecting
  its map and compass on the original North American NES ruleset.
- Excludes: exact enemy or drop contents of unentered rooms; an external
  walkthrough; a map that automatically moves the actor; future boss attacks;
  an item bar with no dungeon-location state.
- Parameters: current room, explored cells, room outline, objective marker,
  health, currency, key count, selected item, acquisition state and concealment.
- Evidence: [The Legend of Zelda decomposition](../games/s-z/the-legend-of-zelda.md),
  using Nintendo's preserved original manual and corroborating Level-1 route.
- Novelty: first isolated for `GAME-0325`; one compact room-decision surface
  joins the actor's local position with two separately earned layers of
  dungeon navigation disclosure.

## INF-357 — Near-camera platform route exposes typed crates and attempt state

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: a fixed near-camera platform view exposes the controlled body,
  immediate forward/depth support, visible enemies, crate classes and pickups
  together with current fruit, life, protection and destroyed-crate state,
  while later geometry, hidden contents and untriggered linked bodies remain
  concealed.
- Includes: the original Crash Bandicoot `N. Sanity Beach` view and attempt
  presentation during the scoped all-crate run.
- Excludes: a side-view camera whose left edge commits passed terrain; a whole
  level map; exact future enemy motion; showing a linked crate bridge before
  its switch; an external walkthrough overlay.
- Parameters: camera, depth horizon, support, visible actors, crate symbols,
  fruit, lives, masks, destroyed count, checkpoint feedback and concealment.
- Evidence: [Crash Bandicoot decomposition](../games/a-f/crash-bandicoot.md),
  using the original manual and corroborating written first-level route.
- Novelty: first isolated for `GAME-0326`; the decision surface couples a
  forward/depth platform slice to the mutable-object and finite-attempt state
  needed for an optional exhaustive clear.

## INF-358 — Side-view stage and transient counters expose pair and completion state

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the live side-view stage exposes the active and following paired
  bodies, mounted state, immediate terrain, hostiles, portable objects and
  pickups; event-triggered counters and later map feedback expose collectible,
  life, checkpoint, bonus-discovery and stage-completion state while concealed
  entrances and future route geometry remain hidden.
- Includes: original Donkey Kong Country's scoped `Jungle Hijinxs!` view,
  momentary banana, K-O-N-G and life counters, Star Barrel feedback, paired or
  mounted bodies and completed-stage exclamation marker.
- Excludes: a whole-stage map; permanent counters for every hidden object;
  exact future enemy motion; revealing a sensitive wall before interaction; an
  external walkthrough overlay.
- Parameters: viewport, active body, follower, mount, local geometry, visible
  actors and objects, counter trigger, counter duration, checkpoint feedback,
  discovered-bonus set, map marker and concealment.
- Evidence: [Donkey Kong Country decomposition](../games/a-f/donkey-kong-country.md),
  using Nintendo's preserved original manual and corroborating first-stage
  route analysis.
- Novelty: first isolated for `GAME-0329`; one decision surface must relate a
  persistent two-body buffer and optional mounted body to transient counters
  and a later retained completeness marker without disclosing the hidden
  detours in advance.

## INF-359 — Carried radio static warns of an anonymous nearby threat

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: while one portable sensor is carried and enabled, its changing
  static warns that an eligible hostile is nearby without disclosing exact
  bearing, identity, coordinate, route or a named distance band.
- Includes: the radio warning around monsters during Silent Hill 2's scoped
  Eastern South Vale route in the 2024 PlayStation 5 remake.
- Excludes: ordinary spatial footsteps; music with declared proximity bands;
  a tracker that plots relative bearing or allegiance; a detector that gives
  direction or distance to hidden loot; an omniscient enemy marker.
- Parameters: sensor, enabled state, eligible hostile, local range, warning
  intensity, occlusion, suppressed state and withheld fields.
- Evidence: [Silent Hill 2 (2024 remake) decomposition](../games/s-z/silent-hill-2-2024.md),
  using PlayStation's official nearby-monster radio description and
  corroborating written Eastern South Vale routes.
- Novelty: first isolated for `GAME-0330`; existing threat-audio and tracker
  boundaries either encode bands, bearing, allegiance or ordinary spatial
  events, while this carried sensor deliberately reports only anonymous nearby
  presence.

## INF-360 — Hand scanner exposes target eligibility and survey progress

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: while local survey mode is active, the interface distinguishes
  eligible flora, fauna and mineral targets, exposes whether one sample was
  accepted and shows retained survey progress without revealing unobserved
  target locations.
- Includes: Starfield hand-scanner feedback for one Kreet sample during `One
  Small Step`.
- Excludes: a solved external map; Subnautica's held blueprint-fragment ring;
  remote planet resource totals; hostile identity scanning.
- Parameters: scanner mode, target class, eligibility, range, accepted sample,
  class progress, location progress and completion state.
- Evidence: [Starfield decomposition](../games/s-z/starfield.md).
- Novelty: first isolated for `GAME-0331`; one instant local observation advances
  a retained ecological or mineral survey rather than a technology blueprint.

## INF-361 — Battle view exposes active troop, hex reach and stack state

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: the tactical battle view exposes battlefield hexes and obstacles,
  active troop, creature identity, count and health, speed, reachable movement,
  ammunition, legal targets and resolved damage without disclosing the exact
  future random roll.
- Includes: manual Heroes of Might and Magic III: Complete battles.
- Excludes: Adventure Map economy; a complete future initiative simulation;
  exact hidden damage result before commitment; an external calculator.
- Parameters: battlefield, hex, obstacle, active troop, count, health, speed,
  reach, ammunition, target legality, resolved damage and hidden roll.
- Evidence: [Heroes of Might and Magic III: Complete decomposition](../games/g-l/heroes-of-might-and-magic-iii-complete.md).
- Novelty: first isolated for `GAME-0332`; the decision surface joins a
  quantity-bearing troop, its scheduled authority and current hex legality.

## INF-362 — Park and attraction panels expose objective and operating state

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: separate park and attraction views expose the current scenario
  objective, date, guest count and Park Rating; ride status and guest-response
  measures such as popularity and satisfaction; and, in applicable ride tabs,
  waiting guests, admission price and inspection setting. Test measurements
  appear only after a completed run. These observations let the player
  diagnose progress or failure before the deadline settles.
- Includes: RollerCoaster Tycoon Deluxe Park Status, Rides Info and applicable
  Ride-window tabs during the Forest Frontiers scenario.
- Excludes: one guest's personal panel (`INF-072`); the itemised finance ledger
  (`INF-058`); test measurements before a completed run; exact hidden future
  arrivals, breakdowns or scenario result.
- Parameters: objective, date, attendance, rating, ride status, guest response,
  queue, price, inspection setting and completed test data where applicable.
- Evidence: [RollerCoaster Tycoon Deluxe decomposition](../games/m-r/rollercoaster-tycoon-deluxe.md),
  using the official Steam-hosted 2003 manual; [Taxonomy Change 256](../../research/taxonomy-changes/TAXONOMY_CHANGE_256.md).
- Novelty: first isolated for `GAME-0335`; the decision surface joins the
  dated aggregate terminal with inspectable attraction causes.

## INF-363 — Battle menu exposes active creature and move state

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: the battle decision surface exposes both active creature
  identities, levels, health and status, the available command classes, and
  each inspected learned move's type plus current and maximum PP without
  revealing the opponent's next selected command or unresolved random result.
- Includes: Pokémon Red Version's active battle view and FIGHT move panel.
- Excludes: the separate party summary; exact future damage, capture or escape
  rolls; an external reference; hidden opponent move selection.
- Parameters: active creatures, identity, level, health, status, commands,
  learned moves, type, current/max PP and hidden future state.
- Evidence: [Pokémon Red Version decomposition](../games/m-r/pokemon-red-version.md),
  using the original manual and pinned battle interface source.
- Novelty: first isolated for `GAME-0336`; a four-command creature battle menu
  binds persistent per-move attrition to the immediate choice surface.

## INF-364 — Conditional radar shows local actors and directed perception

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: while a declared radar state is available, the interface exposes
  the player's local position, eligible nearby hostile or surveillance actors
  and their directed perception regions, then deliberately removes that layer
  in named alert, search or narrow-space states.
- Includes: Metal Gear Solid's Soliton Radar dots and colour-coded fields of
  vision in Infiltration, with suppression during Alert, Evasion and declared
  narrow-space states.
- Excludes: an always-available world map; a bearing-only threat warning; a
  cosmetic minimap without perception direction; direct world-space vision
  cones that remain visible when the radar is unavailable.
- Parameters: radar availability, player marker, eligible observer, observer
  class, directed region, colour or state coding, local bounds, suppression
  trigger and restored state.
- Evidence: [Metal Gear Solid decomposition](../games/m-r/metal-gear-solid.md),
  using the original English PlayStation manual and Konami's preserved opening
  infiltration guidance.
- Novelty: first isolated for `GAME-0339`; one conditional information layer
  joins actor positions to directed perception geometry and is withdrawn by
  the same awareness states it helps the player avoid.

## INF-365 — Carried clue encodes a fixed ordered traversal route

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: an inspectable carried artefact exposes authored wording or
  symbols whose ordered interpretation identifies each successive local route
  branch, without placing a waypoint or automatically moving the traveller.
- Includes: reading the purchased “dance” map's first word on each line as the
  nine forest directions in the original EGA The Secret of Monkey Island.
- Excludes: a treasure silhouette compared with a separate world chart; a
  single destination marker; an external walkthrough; a code entered into a
  stationary receiver; a map that reveals only explored geometry.
- Parameters: artefact, surface wording, interpretation rule, direction
  alphabet, sequence length, inspection availability and route correspondence.
- Evidence: [The Secret of Monkey Island decomposition](../games/s-z/the-secret-of-monkey-island.md),
  using two independently agreeing written routes; no executable run observed.
- Novelty: first isolated for `GAME-0343`; one inventory clue directly encodes
  the ordered locomotion decisions rather than naming a destination or requiring
  comparison with a second spatial representation.

## INF-366 — Hunting display exposes target, shots, hit row, pass line, round and score

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: the active hunting display exposes the moving target and its
  immediate scene together with remaining shots, the ordered hit/miss row, the
  minimum qualifying boundary, current round and accumulated score before the
  next shot or round settlement.
- Includes: the original Duck Hunt Game A playfield and lower HUD during round
  one.
- Excludes: a software reticle absent from the original NES presentation; a
  hidden target path; the exact remaining flight time; later-round pass-line
  values not yet reached; external strategy tables.
- Parameters: active target, visible flight, shots remaining, target lamps,
  pass line, round number, score and hit feedback.
- Evidence: [Duck Hunt decomposition](../games/a-f/duck-hunt.md), using the
  original English NES manual's labelled screen and Nintendo's rules page.
- Novelty: first isolated for `GAME-0345`; one compact display joins
  target-local opportunity state to round-level qualification progress.

## INF-367 — Street HUD joins tag progress, spray, survival, time and pursuit cues

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: during an active street stage, the interface exposes current
  stamina, score, authoritative time, carried spray frames and the addressed
  graffiti command/progress, while world arrows and the available map identify
  immediate attackers, escape direction and remaining marked points without
  revealing future police spawns.
- Includes: the bounded Xbox 360 Jet Set Radio Shibuya GG HUD, command icons,
  enemy/exit arrows and remaining-point map support.
- Excludes: a complete future route; exact hidden pursuit logic; external
  walkthrough directions; optional leaderboard; graffiti editor; result rank
  after the active stage has already settled.
- Parameters: stamina, score, time, spray stock, point mark/size/state,
  directional command, threat cue, escape cue, map and hidden future state.
- Evidence: [Jet Set Radio decomposition](../games/g-l/jet-set-radio.md), using
  the inherited original instruction booklet and corroborated Xbox 360 route.
- Novelty: first isolated for `GAME-0350`; one live traversal surface joins a
  consumable world-edit command to both survival and territorial progress.

## INF-368 — Scan visor exposes target eligibility, progress and typed result

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: while a dedicated analysis visor or mode is active, the
  interface distinguishes eligible local world targets, exposes held scan
  progress and presents the completed target's authored information, weak
  point or fixture consequence without revealing unscanned target results in
  advance.
- Includes: Metroid Prime's Scan Visor during the bounded Frigate Orpheon
  prologue.
- Excludes: an ordinary combat reticle with no analysis result; Subnautica's
  blueprint-fragment count; a cyberdeck quickhack menu; Starfield's instant
  survey sample; an external walkthrough.
- Parameters: mode, target marker, eligibility, range, lock, progress,
  completion, result class, presented data and persistence.
- Evidence: [Metroid Prime decomposition](../games/m-r/metroid-prime.md), using
  Nintendo's original manual and pinned reverse-engineered scan state.
- Novelty: first isolated for `GAME-0355`; earlier scanner interfaces are tied
  to blueprint, survey or hack state and do not expose one target's typed
  information/control resolution.

## INF-369 — Converging reflected rays expose the current target bearing

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: while the compatible reflective tool is focused in sufficient
  direct light, its initially separated visible rays converge along the
  horizontal bearing toward the current authored world target, without
  revealing a route or distance.
- Includes: the Ancient Sword's guiding light pointing from open terrain toward
  the first colossus in the bounded Shadow of the Colossus opening.
- Excludes: a persistent compass; a complete route line; exact coordinates or
  distance; the map's past journey trace; weak-point disclosure on a guardian.
- Parameters: tool, light eligibility, ray spread, convergence, bearing,
  target, visibility and loss of focus.
- Evidence: [Shadow of the Colossus decomposition](../games/s-z/shadow-of-the-colossus.md),
  using the original North American PlayStation 2 manual.
- Novelty: first isolated for `GAME-0356`; information strength varies with
  player-controlled optical convergence rather than a thrown item, pulse or
  always-present navigation display.

## INF-370 — Equipped sword light reveals eligible guardian wounds and sigils

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: when the designated sword is equipped and an eligible guardian
  body region enters the required visibility relation, a luminous mark exposes
  that region as a wound trigger or major health-bearing sigil without
  revealing an automatic route to it.
- Includes: the first Shadow of the Colossus guardian's rear-left-leg trigger
  mark and the major crown sigil on Normal difficulty.
- Excludes: the guardian health bar (`INF-318`); an externally supplied
  walkthrough; ordinary hit flash; Hard-mode additional sigils; a target lock
  that steers attacks automatically.
- Parameters: equipped tool, guardian, body region, difficulty, visibility,
  mark class, active state, depletion and concealment.
- Evidence: [Shadow of the Colossus decomposition](../games/s-z/shadow-of-the-colossus.md),
  using the original PlayStation 2 manual's sword rule and corroborated
  first-colossus routes.
- Novelty: first isolated for `GAME-0356`; a carried tool conditionally makes
  local parts of a traversable hostile legible as topology-changing or
  health-bearing attack sites.

## INF-371 — Wanted stars expose current police-pressure tier

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: a compact star display exposes the current discrete level of
  ordinary police attention and changes as pursuit enters search or clears,
  without revealing future police positions or an automatic escape route.
- Includes: the wanted-star display during the bounded original PlayStation 2
  Grand Theft Auto: San Andreas opening and duplicate low-tier evasion control.
- Excludes: a calculated GPS route; Mafia's separate citation and handcuff
  classes; hidden patrol spawn locations; mission text that fixes a wanted
  level independently of ordinary police perception.
- Parameters: star count, filled state, flashing/search state, pursuit,
  reacquisition, clearance and mission override.
- Evidence: [Grand Theft Auto: San Andreas decomposition](../games/g-l/grand-theft-auto-san-andreas.md),
  using the original English PlayStation 2 booklet and corroborated opening
  rules guide.
- Novelty: first isolated for `GAME-0357`; prior wanted-state displays are
  inseparable from a calculated route or citation/arrest taxonomy, while this
  boundary admits the compact tier alone.

## INF-372 — Context icon and focus mark disclose the current world action

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: the live interface changes its action icon or focus mark with
  the actor's position and addressed target, showing the currently legal
  contextual command before it is pressed rather than requiring the player
  to memorise a fixed action for every fixture and actor.
- Includes: Ocarina of Time's A-button OPEN, SPEAK and CHECK prompts and Navi's
  target triangle or focus cursor for a nearby actor or relevant object in
  the bounded Kokiri Forest and Great Deku Tree route.
- Excludes: a static inventory item icon; a prompt shown only after an action
  has already resolved; a map revealing unopened rooms; undisclosed future
  actions; the player command that actually opens or speaks.
- Parameters: actor position, target eligibility, focus mark, prompt text,
  current action, occlusion, acquisition and expiry.
- Evidence: [Ocarina of Time decomposition](../games/s-z/the-legend-of-zelda-ocarina-of-time.md),
  using Nintendo's original N64 manual pages 11–18.
- Novelty: first isolated for `GAME-0363`; one live field-facing disclosure
  switches the legal meaning of the same control across actors and fixtures.

## INF-373 — Show pinfall, frame progress and pending bowling score

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `Medium`
- Definition: the bowling display exposes the standing pin field, frame and
  delivery results, and the accumulating score while an unresolved strike or
  spare may still depend on later balls.
- Includes: the original Wii Sports Bowling lane and ten-frame result display
  for one selected Mii.
- Excludes: revealing the future physical path of a ball; displaying the
  hidden exact skill-adjustment formula; an unconditional fully known final
  score before pending bonuses have settled.
- Parameters: visible pins, frame index, delivery mark, strike, spare,
  pending bonus, current score and final score.
- Evidence: [Wii Sports decomposition](../games/s-z/wii-sports.md), using
  Nintendo's Bowling instructions and ten-frame scoring corroboration.
- Novelty: first isolated for `GAME-0364`; frame-indexed pin and bonus state
  is disclosed separately from the later performance skill adjustment.

## INF-374 — Expose a live trick line, balance, clock and park goals

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: the skating interface shows the current trick string and
  provisional score, balance indicators during eligible sustained tricks,
  remaining park-run time and the park's declared goals or their credited
  state, so the player can revise the line and route before settlement.
- Includes: default HUD and Tour park-goal display in Tony Hawk's Pro Skater
  1 + 2 Warehouse.
- Excludes: guaranteeing a successful future landing; an exact predicted
  multiplier for undiscovered gaps; revealing every hidden collectible;
  the option to hide individual HUD elements.
- Parameters: trick string, provisional and banked score, balance meter,
  remaining time, goal list, credited state and display settings.
- Evidence: [Tony Hawk's Pro Skater 1 + 2 decomposition](../games/s-z/tony-hawks-pro-skater-1-plus-2.md),
  using Activision's HUD accessibility settings and Tours park-goal display.
- Novelty: first isolated for `GAME-0365`; it joins unbanked line risk with
  the remaining session window and independently tracked park goals.

## INF-375 — Expose typed target protection before power selection

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: the combat target display separates a selected hostile's
  remaining health from its named shield, armour or barrier resistance,
  allowing the player to judge which current attacks or powers can affect
  the protected target before committing a power.
- Includes: Mass Effect 2's target bar and contextual power-wheel feedback
  during the bounded Lazarus and Freedom's Progress fights.
- Excludes: disclosing exact future enemy actions; an untyped single health
  bar; a power's hidden numerical damage; only learning protection after a
  failed cast.
- Parameters: selected target, protection class, remaining layer, health,
  available power, contextual suitability and display update.
- Evidence: [Mass Effect 2 (Legendary Edition) decomposition](../games/m-r/mass-effect-2-legendary-edition.md),
  using the official Xbox manual's HUD and target-bar rules.
- Novelty: first isolated for `GAME-0367`; the interface discloses the typed
  resistance needed for an ability-legality decision, not merely target health.

## INF-376 — Expose camera readiness and subject-scoring cues before capture

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: the camera view exposes remaining charge, post-shot processing
  readiness and visible target or PP cues for the currently framed scene,
  allowing a player to decide whether and when a shot is worth committing.
- Includes: Dead Rising's battery, processing gauge, target marker and PP
  sensor during a live rooftop photograph opportunity.
- Excludes: revealing exact future subject movement; showing only the final
  score after a photograph; ordinary life or item-slot indicators; photo
  capture and scoring rules themselves.
- Parameters: battery, processing state, target marker, PP sensor, framing,
  subject, feedback cadence and preview uncertainty.
- Evidence: [Dead Rising decomposition](../games/a-f/dead-rising.md), using
  Capcom's original camera-view manual.
- Novelty: first isolated for `GAME-0368`; this is a pre-capture information
  surface for an observation-reward decision, not a combat target bar.

## INF-377 — Expose hospital referrals, queues and quarterly criteria

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: briefing, patient/queue, casebook and status panels disclose
  current diagnosis/referral pressure, service state and progress toward each
  announced quarterly winning or losing criterion before intervention.
- Includes: Theme Hospital's first-level Mission Briefing, room Queue Panel,
  Casebook and five-category Progress Report.
- Excludes: exact unseen patient arrival sequence; complete hidden treatment
  probabilities or reputation weights; the underlying medical resolution.
- Parameters: patient condition, diagnosis state, room, queue length,
  criterion, target, progress bar, quarter and loss warning.
- Evidence: [Theme Hospital decomposition](../games/s-z/theme-hospital.md),
  using the original PC manual's briefing and business/queue panels.
- Novelty: first isolated for `GAME-0370`; the operating display joins
  patient-level referral decisions with the institution's five-way appraisal.

## INF-378 — Viewfinder discloses subject recognition and remaining film

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: during a live photo excursion, the camera display shows the
  remaining exposure allowance and a focus sensor that identifies a
  recognised subject, marks an unreported subject as new, or shows an
  unidentified target without revealing its later appraisal score.
- Includes: original Pokémon Snap's red Focus Sensor, `NEW` and `?` cues
  and remaining-film display during Beach photography.
- Excludes: Dead Rising's battery and processing gauge (`INF-376`); Oak's
  later score breakdown (`INF-299`); an omniscient list of future subjects.
- Parameters: focus state, sensor colour, subject identity, new/unidentified
  cue, remaining exposures and HUD update timing.
- Evidence: [Pokémon Snap decomposition](../games/m-r/pokemon-snap.md), using
  Nintendo's original instruction booklet, pp. 13–15.
- Novelty: first isolated for `GAME-0371`; live capture eligibility and
  subject-recognition uncertainty share one viewfinder surface.

## INF-379 — Show approaching note lanes and live performance gauges

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: a scrolling coloured chart discloses near-future note positions
  and simultaneous or sustained form, while live score, multiplier, Rock Meter
  and Star Power displays expose the state used for timing and survival.
- Includes: Guitar Hero III's fretboard and performance display in a solo song.
- Excludes: showing the entire song chart before play; post-song statistics;
  soundtrack rhythm with no explicit note judgement surface.
- Parameters: scroll horizon, lane colour, chord/sustain marking, score,
  streak multiplier, Rock Meter state and Star Power charge.
- Evidence: [Guitar Hero III decomposition](../games/g-l/guitar-hero-iii-legends-of-rock.md),
  Activision's PlayStation 3 instruction booklet, pp. 8–10.
- Novelty: first isolated for `GAME-0372`; previewed chart events and live
  survival/scoring state jointly guide the next fret-strum commitment.

## INF-380 — Expose cell growth, DNA, health and collected parts

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: a live cell-stage display separates growth progress from
  spendable DNA and current health, while the collection and editor expose
  discovered part availability for the next body revision.
- Includes: Spore's Cell-stage Progress Bar, DNA and Health meter, My
  Collection part list and Cell Creator palette.
- Excludes: exact undisclosed food-to-growth coefficients; a complete view of
  unseen future parts; treating health and DNA as interchangeable resources.
- Parameters: progress, milestones, DNA balance, health, collected part types
  and editor availability.
- Evidence: [Spore decomposition](../games/s-z/spore.md), original EA manual,
  pp. 6–7, 18–19 and 30–31.
- Novelty: first isolated for `GAME-0373`.

## INF-381 — Guide an open-city race by destination bearing and junction cues

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: during a point-to-point race without a mandatory street route,
  the interface exposes the destination bearing, the driven vehicle's current
  heading, remaining distance and suggested turn at an approaching junction
  while leaving alternative legal streets available to the player.
- Includes: Burnout Paradise's original Xbox 360 offline ordinary `Race`
  compass, distance counter, flashing road signs and Paradise City map.
- Excludes: `INF-204` speed-and-gear driving HUD; an imposed checkpoint ribbon;
  a completed result or omniscient rival path; pre-entry event eligibility.
- Parameters: destination, current heading, distance, next junction,
  recommendation, map scale and chosen route.
- Evidence: [Burnout Paradise decomposition](../games/a-f/burnout-paradise.md),
  original Electronic Arts Xbox 360 manual, pp. 2, 4 and 6.
- Novelty: first isolated for `GAME-0374`; a live destination vector in an
  unconstrained street network is not the same boundary as authored driving-
  line guidance coupled to speed and gear (`INF-204`).

## INF-382 — Show a highlighted species' staged garden requirements

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: a highlighted piñata's information view exposes its Condition Status, allowing the player to distinguish what is needed for appearance, visit and residence before choosing a garden edit.
- Includes: pressing Y on a piñata in or around the original Viva Piñata garden and checking the Condition Status tab.
- Excludes: revealing future species before they are available; calculating a guaranteed arrival time; claiming undocumented Whirlm thresholds from the general manual.
- Parameters: highlighted piñata, species, stage, condition display, current satisfaction and unknown requirement.
- Evidence: [Viva Piñata decomposition](../games/s-z/viva-pinata.md), original Xbox 360 booklet pp. 14 and 16–17.
- Novelty: first isolated for `GAME-0375`; it exposes species-specific staged attraction rules, not general resident mood or crop water.

## INF-383 — Show rolling diameter against target and remaining time

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Limited`
- Confidence: `Medium`
- Definition: during a timed rolling-size stage, the interface discloses the
  katamari's current measured size, the stage's required size and the time
  remaining, so the player can judge whether a new object class or final
  target is reachable before expiry.
- Includes: the size and countdown readouts during Katamari Damacy REROLL
  Make a Star 1.
- Excludes: an unshown exact threshold for each individual item; a final
  result screen alone; a generic score without physical size; an asserted
  identical time allowance across the original PS2 and all REROLL releases.
- Parameters: current diameter, target diameter, remaining time and display
  precision.
- Evidence: [Katamari Damacy REROLL decomposition](../games/g-l/katamari-damacy-reroll.md),
  first-hand REROLL stage report and the original publisher's timed-size
  description; exact PS4 display details await direct inspection.
- Novelty: first isolated for `GAME-0376`; two live measurements jointly
  guide size-ordered route choice under a deadline.

## INF-384 — Public production board with private resource hands

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: players can inspect the shared numbered terrain, robber,
  buildings, roads, harbours, piece reserves and disclosed points while the
  identities of opponents' held resource and development cards stay private.
- Includes: CATAN's face-up fixed beginner board and building-cost cards
  alongside concealed player hands and development-card deck.
- Excludes: `INF-001`'s fully visible decision state; revealing every rival
  card merely because its hand count is observable; concealing hex numbers.
- Parameters: public board state, visible card counts, own hand, rival hands,
  hidden point cards and declared cost chart.
- Evidence: [CATAN decomposition](../games/a-f/catan.md), official base rules.
- Novelty: first isolated for `GAME-0377`; an exact public production network
  coexists with changing, player-specific private economic state.

## INF-385 — Show a rolling stage, speed, clock and optional score

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: a live stage interface shows the rolling body and visible
  nearby course together with remaining time, current speed, stage identity,
  score and collectible tally, while leaving the safe future route for the
  player to judge.
- Includes: Super Monkey Ball 2's scoped Story Mode main-game screen with
  the monkey ball, platform, timer, speed, score and bananas.
- Excludes: a full solved path overlay; `INF-347`'s finite-life platform HUD;
  a results-only score report; Challenge Mode's monkeys-remaining count as
  if it were part of this Story attempt.
- Parameters: camera region, stage label, time, speed, score, banana count and
  goal visibility.
- Evidence: [Super Monkey Ball 2 decomposition](../games/s-z/super-monkey-ball-2.md),
  original GameCube manual p. 9.
- Novelty: first isolated for `GAME-0378`; the interface joins a physical
  rolling-state cue with the live goal deadline and optional score economy.

## INF-386 — Show worm energy, terrain, wind and turn time

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: the match display reveals the current worm and altered ground,
  individual and team energy, remaining turn time and current wind direction
  and strength, without promising an exact future impact solution.
- Includes: the battle view in the scoped Worms Armageddon PC match.
- Excludes: an omniscient ballistic trajectory, secret future wind values,
  campaign rank or network chat.
- Parameters: camera region, worm label, energy bars, turn indicator, round
  indicator option and wind bar.
- Evidence: [Worms Armageddon decomposition](../games/s-z/worms-armageddon.md),
  Team17 manual p. 8.
- Novelty: first isolated for `GAME-0379`; public physical firing conditions
  and team survival are shown together under one turn clock.

## INF-387 — Show a puzzle prompt, choices, reward and purchased hints

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Corroborated`
- Confidence: `Medium`
- Definition: an authored puzzle presents its fixed question, visual answer
  candidates and current attainable picarat reward; purchased hints become
  visible in order while the accepted answer remains undisclosed until solved.
- Includes: the opening Professor Layton village map with its question,
  pictured locations and optional hint view.
- Excludes: an omniscient answer highlight before submission; invisible
  future random puzzle selection; scene exploration outside this puzzle.
- Parameters: prompt, picture, candidate count, current reward, hint tier and
  answer-feedback state.
- Evidence: [Professor Layton and the Curious Village
  decomposition](../games/m-r/professor-layton-and-the-curious-village.md),
  Nintendo manual pp. 8–10 and first-puzzle walkthrough.
- Novelty: first isolated for `GAME-0380`; an authored spatial question and
  priced clue layers are disclosed without revealing its fixed answer.

## INF-388 — Mission watch exposes a fixed objective checklist and status

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: pre-mission briefing and an inspectable in-mission status view
  disclose the finite required objectives and their current completion state,
  separately from the local combat scene and personal health/ammunition.
- Includes: GoldenEye 007's original mission briefing and Q Watch objective
  screen for Secret Agent Dam's alarm and bungee tasks.
- Excludes: a live waypoint to every alarm, an omniscient guard map, a hidden
  objective not yet briefed, or life and ammunition meters alone (`INF-119`).
- Parameters: difficulty, objective list, objective state, status-view access
  and completion feedback.
- Evidence: [GoldenEye 007 decomposition](../games/g-l/goldeneye-007.md),
  Nintendo's original instruction booklet and original-N64 Dam guides.
- Novelty: first isolated for `GAME-0381`; a mission contract remains
  inspectable during live play even though its spatial targets require search.

## INF-389 — Display current Wants, Fears and aspiration state

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: a selected resident's interface shows currently offered Wants
  and Fears beside aspiration status and reward feedback, allowing the player
  to choose a visible desire and observe its fulfilled or realised outcome.
- Includes: the scoped The Sims 2: Legacy Collection household resident's
  current desire icons and aspiration meter during one Live Mode day.
- Excludes: motive bars and action queue alone (`INF-168`); a fixed authored
  scenario checklist (`INF-067`); a universal fixed icon count across editions.
- Parameters: resident, displayed Want/Fear set, aspiration meter, reward
  points, icon replacement and visibility of optional locks.
- Evidence: [The Sims 2: Legacy Collection decomposition](../games/s-z/the-sims-2-legacy-collection.md), EA's original PC manual and Maxis' design diary.
- Novelty: first isolated for `GAME-0383`; visible live desires and fears are
  distinct from bodily motives or a staged objective list.

## INF-390 — Display shared racing energy and boost eligibility

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: the live race display exposes the machine's current shared
  energy reserve and a visible first-lap-to-later-lap change that tells the
  driver when manual energy-priced boosting becomes available.
- Includes: F-Zero GX's energy bar changing from red to rainbow after lap one
  in the scoped Twist Road race.
- Excludes: race place and rival proximity alone (`INF-205`); a boost meter
  unrelated to vehicle damage; exact hidden damage coefficients.
- Parameters: energy level, display colour, lap transition, boost eligibility
  and depletion feedback.
- Evidence: [F-Zero GX decomposition](../games/a-f/f-zero-gx.md), Nintendo's
  original instruction booklet, racing HUD section.
- Novelty: first isolated for `GAME-0384`; one display discloses a shared
  survival/acceleration resource and its progress-gated command access.

## INF-391 — Inspect a case-local record of evidence and profiles

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the court interface makes the current case's admitted evidence
  descriptions and participant profiles inspectable and revisitable, while
  authored trial events may add or revise entries before later challenges.
- Includes: the original DS first-case Court Record with autopsy report,
  blackout record, statue-clock, passport and participant profiles as the
  script introduces them.
- Excludes: an immutable scene-indexed memory tableau (`INF-012`); an
  unlimited external document search; proof that every listed item is useful
  against the currently selected testimony line.
- Parameters: case, item roster, item detail, profile roster, scripted
  addition/revision point and current availability.
- Evidence: [Phoenix Wright: Ace Attorney decomposition](../games/m-r/phoenix-wright-ace-attorney.md),
  the contemporary original-DS GameSpot review and first-case written route.
- Novelty: first isolated for `GAME-0385`; case evidence is a growing,
  inspectable challenge inventory rather than free-form investigation memory.

## INF-392 — Display addressable and revisitable testimony lines

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: after a witness gives an authored testimony, court
  cross-examination exposes its individual statements as selectable lines
  the player can revisit in either direction and address with a press or an
  evidence presentation until that testimony version changes.
- Includes: navigating Frank Sahwit's statements in The First Turnabout
  before choosing which line to press or challenge.
- Excludes: one-way passive dialogue; a generated interview transcript;
  treating a revised testimony as though its old lines remained active.
- Parameters: witness, version, ordered lines, selected line, navigation
  direction and replacement event.
- Evidence: [Phoenix Wright: Ace Attorney decomposition](../games/m-r/phoenix-wright-ace-attorney.md),
  the contemporary original-DS GameSpot review and first-case written route.
- Novelty: first isolated for `GAME-0385`; testimony is a line-addressed
  challenge surface rather than merely story text.

## INF-393 — Expose a growing case notebook of clues and leads

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: a case-local notebook makes registered physical clues, persons
  of interest, objectives, interview questions and discovered destinations
  inspectable as the authored investigation reveals them.
- Includes: L.A. Noire's The Driver's Seat notebook recording the car owner,
  relevant objects, witnesses, bar address and later apartment lead.
- Excludes: omniscient disclosure of the whole solution; a courtroom record
  limited to admitted trial items (`INF-391`); immutable death-scene indexing
  (`INF-012`); an external search engine.
- Parameters: current case, clue roster, person record, objective, question,
  address, registration event, current destination and revisit access.
- Evidence: [L.A. Noire decomposition](../games/g-l/la-noire.md), Rockstar's
  PS4 manual notebook section and Prima's remaster case route.
- Novelty: first isolated for `GAME-0388`; one in-world dossier unifies
  evidence and the next navigable lead across multiple physical sites.

## INF-394 — Show the board route, Star site and rival tallies

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: the board presentation exposes the connected route and
  inspectable map together with each competitor's current Stars and Coins,
  allowing a route or spending choice to be made against visible standings.
- Includes: Mario Party 2's inspectable Adventure Board map, Toad's current
  site and the four players' displayed Star and Coin totals during Pirate
  Land.
- Excludes: previewing the next Dice Block result (`INF-002`); revealing a
  later relocated Star site before purchase; the internal rules of a
  not-yet-selected minigame; undisclosed future board events.
- Parameters: route graph, visible fixtures, active Star site, player totals,
  active player and map-inspection control.
- Evidence: [Mario Party 2 decomposition](../games/m-r/mario-party-2.md),
  Nintendo's original Nintendo 64 instruction booklet, pp. 8, 12–15.
- Novelty: first isolated for `GAME-0392`; the public board graph and moving
  scoring site coexist with rival currency and Star standings.

## INF-395 — Show current cycle day and time against a fixed expiry

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: the interface exposes the current day and clock position within
  a fixed, continuously advancing world cycle, allowing the player to compare
  remaining opportunity against a known terminal deadline.
- Includes: the first-to-final-day clock in Majora's Mask's Clock Town
  prologue, where the clock reaches the 72-hour moonfall limit.
- Excludes: a date label for discrete campaign activities (`INF-336`);
  an elapsed post-result timer; disclosure of every future NPC position.
- Parameters: day labels, displayed time, clock rate, pause policy, final
  deadline and accessibility of the display.
- Evidence: [Majora's Mask decomposition](../games/s-z/the-legend-of-zelda-majoras-mask.md),
  Nintendo's original N64 instruction booklet, pp. 10–11.
- Novelty: first isolated for `GAME-0395`; the visible cycle clock is directly
  decision-relevant to the final-night gate and moonfall failure.

## INF-396 — Show the call-response rhythm and live rap rating

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `Medium`
- Definition: disclose the instructor or player turn, ordered beat-aligned
  button symbols and current ordinal performance rating so the player can
  time the next response and observe risk after an answer.
- Includes: the first Normal dojo stage in PaRappa the Rapper Remastered;
  the PS4 enlarged-player-icon option improves visibility of the same cue.
- Excludes: Guitar Hero III's advancing fretboard plus Rock Meter
  (`INF-379`); the whole chart supplied before play; hidden timing thresholds.
- Parameters: turn marker, button symbol, beat position, player icon size,
  rating label and update timing.
- Evidence: [PaRappa Remastered decomposition](../games/m-r/parappa-the-rapper-remastered.md),
  Sony's official feature page and the original-game written guide.
- Novelty: first isolated for `GAME-0396`; turn ownership is visible as well
  as the symbols and graded risk, unlike a single continuous chart lane.

## INF-397 — Show the current short command and course chance state

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: reveal the current microgame's brief imperative and remaining
  countdown together with the course's visible progress and life stock, while
  keeping the identity of a later random ordinary task undisclosed.
- Includes: Wario's introductory task prompt, bomb timer, course-slot
  progress and four life indicators.
- Excludes: a promised reward/task checklist (`INF-067`); previewing the
  exact future ordinary-task order; a completed-course score alone.
- Parameters: instruction, countdown, progress indicator, life display,
  update timing and speed cue.
- Evidence: [WarioWare introductory course](../games/s-z/warioware-inc-mega-microgame.md),
  Nintendo's GBA booklet and two contemporary written guides.
- Novelty: first isolated for `GAME-0398`; the currently operative command
  changes at every microgame boundary while cumulative chance remains shown.

## INF-398 — Show a moving local arena view and run counters

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: a camera-followed viewport exposes the controlled craft,
  current nearby threats and visible score, multiplier and finite stock
  counters, while live enemies beyond the screen edge need not be shown until
  the camera or they move into view.
- Includes: the larger-than-screen Evolved arena and its score/life/bomb
  feedback in original Xbox 360 Geometry Wars: Retro Evolved.
- Excludes: fully visible global board state (`INF-001`); a static
  side-scrolling authored obstacle horizon (`INF-192`); an exact preview of
  future enemy spawn positions; off-screen enemy erasure by a bomb.
- Parameters: camera anchor, viewport bounds, visible actors, score and
  multiplier displays, life and bomb counters, off-screen persistence.
- Evidence: [Geometry Wars: Retro Evolved decomposition](../games/g-l/geometry-wars-retro-evolved.md),
  two contemporary Xbox 360 Evolved guides describing camera-limited bombs
  and score/stock feedback.
- Novelty: first isolated for `GAME-0400`; current live arena state extends
  outside the local view, so the player cannot treat a screen clear as a
  whole-playfield reset.

## INF-399 — Show present airborne objects and score-run miss marks

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: display the fruit and bombs currently traversing the screen,
  together with accumulated score and outstanding missed-fruit marks, but do
  not reveal the class, timing or position of later launches in advance.
- Includes: the original iPhone Fruit Ninja Classic play view and its score
  and missed-fruit feedback.
- Excludes: a fully known fixed board (`INF-001`); a camera moving through a
  larger persistent arena (`INF-398`); a preview of future bomb trajectories;
  a deterministic warning for an occasional critical bonus.
- Parameters: currently visible bodies, motion, score display, miss marks,
  launch visibility boundary and update timing.
- Evidence: [Fruit Ninja decomposition](../games/a-f/fruit-ninja.md),
  original TouchArcade review and Halfbrick's Classic guide.
- Novelty: first isolated for `GAME-0401`; current threats are legible while
  later airborne objects remain unpreviewed in an open score run.

## INF-400 — Show current trail status and measured crossing conditions

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: journey status and map show present date, weather, health, food
  and distance; a reached river shows its width, depth and offered methods
  before the player commits.
- Includes: A-157 status/map and Kansas crossing screens.
- Excludes: foretelling rainfall, illness or accident draws; hiding current
  food; treating traveller advice as guaranteed outcomes.
- Parameters: shown counters, map, water measurements and choices.
- Evidence: [The Oregon Trail decomposition](../games/s-z/the-oregon-trail.md),
  MECC A-157 booklet, Program Preview pp. 8–11.
- Novelty: first isolated for `GAME-0402`; measured present state informs
  policy and river risk while later events stay hidden.

## INF-401 — Show ghost exposure, power and room-survival state

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: a live room view and HUD expose the player's remaining health,
  whether the room is dark or cleared, currently visible hostiles and an
  exposed ghost's heart and remaining power during suction.
- Includes: Luigi's health icon, Parlor illumination, normal ghost hearts
  and power numerals in original GameCube Luigi's Mansion.
- Excludes: a preview of exact next spawn time, hidden Boo location, future
  ghost movement or frame-perfect capture windows.
- Parameters: health, room-light state, ghost position, exposed-heart cue,
  power numeral and display timing.
- Evidence: [Luigi's Mansion decomposition](../games/g-l/luigis-mansion.md),
  Nintendo's original booklet pp. 12–13 and 22–25.
- Novelty: first isolated for `GAME-0403`; current vulnerability and
  resistance are visible while the future encounter timing is not.

## INF-402 — Show approaching step arrows and live Dance Gauge

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: four upward-scrolling directional lanes and fixed step zones
  disclose imminent required foot placements, while each timing judgement,
  Dance Gauge and low-gauge Danger cue expose current performance risk.
- Includes: the single-player `GN845-UC` DanceDanceRevolution song screen.
- Excludes: an entire chart preview; precise unpublished timing windows;
  Guitar Hero III's fret colours, sustain forms, score multiplier and Star
  Power (`INF-379`); the completed-song report (`INF-299`).
- Parameters: visible arrow horizon, lane directions, step zones, displayed
  judgement, current gauge, Danger cue and display timing.
- Evidence: [DanceDanceRevolution decomposition](../games/a-f/dancedancerevolution.md),
  Konami's 1998 `GN845-UC` operator manual, p. 11.
- Novelty: first isolated for `GAME-0406`; the live view links physical
  foot-panel timing and song-survival risk without later-series meters.

## INF-403 — Show sun, seed readiness, lane threat and flagged progress

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: the interface exposes the current sun balance, visible
  seed packets and their grayed-out recharge state, placed plants and
  advancing zombies by row, plus a progress bar whose flags indicate
  larger upcoming waves; the pre-level sweep previews zombie types.
- Includes: the regular first-stage daytime Adventure view in original
  Plants vs. Zombies.
- Excludes: an exact future spawn calendar or lane assignment; Bloons TD 6's
  lives-and-round-stock interface (`INF-323`); all future plant unlocks;
  a numerical combat forecast not shown in the game.
- Parameters: sun balance, packet set, readiness display, visible rows,
  enemy preview, progress fraction and flag positions.
- Evidence: [Plants vs. Zombies decomposition](../games/m-r/plants-vs-zombies.md),
  PopCap's public readme, “The Basics”, “Plants and Planting” and “Zombies”.
- Novelty: first isolated for `GAME-0407`; the player prices a near-term
  plant against current spendability and wave progress without omniscient
  future lane data.

## INF-404 — Expose vitality, lives and the current copied ability

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: a live stage display names the avatar's Normal or copied
  ability state and shows the current vitality and remaining finite lives,
  with a use counter only for an ability type that has one.
- Includes: the bottom-screen Normal/Beam label, six-bar initial vitality
  and remaining-lives number in original NES Kirby's Adventure.
- Excludes: a whole future stage map; exact unseen enemy abilities; a
  countdown stage timer; a HUD where ability ownership is not visible.
- Parameters: form label, vitality maximum/current value, life stock, optional
  ability-use limit, update timing and damage feedback.
- Evidence: [Kirby's Adventure decomposition](../games/g-l/kirbys-adventure.md),
  using Nintendo's preserved original NES manual, pp. 20–21.
- Novelty: first isolated for `GAME-0408`; `INF-347` requires a timed
  platform-stage display, whereas this packet's decision state is the
  inhalation/copy gate and vitality without a stage clock.

## INF-405 — Expose arena opponents and vehicle-combat resources

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: a live vehicle-combat display exposes remaining opponent count
  and radar positions together with the controlled vehicle's health, life
  stock, active weapon/ammunition, machine-gun heat, turbo and energy, so
  movement and fire decisions can use these current states.
- Includes: the original PS2 Twisted Metal: Black arena HUD and opponent
  radar while driving Junkyard Dog in Story Mode.
- Excludes: exact unseen opponent intent; a complete future-stage map;
  spectator-only telemetry; a generic speedometer without combat state.
- Parameters: opponent count and radar markers, health, lives, selected
  weapon, ammunition, heat, turbo, energy and display refresh.
- Evidence: [Twisted Metal: Black decomposition](../games/s-z/twisted-metal-black.md),
  using Sony's original PS2 manual, HUD diagram.
- Novelty: first isolated for `GAME-0409`; positional enemy disclosure and
  multiple independent combat budgets are visible in one arena display.

## INF-406 — Expose a stage's required and caught creature counts

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the stage briefing or status view discloses the minimum
  creature-capture quota and the count already accepted, letting the player
  distinguish sufficient progress from optional uncaught creatures.
- Includes: Fossil Field's three-needed versus four-total monkey information
  and the catch-progress view in original PlayStation Ape Escape.
- Excludes: the position of every unseen monkey; a future gadget route;
  species catalogue credit (`INF-352`); a final score shown only after exit.
- Parameters: required, total, caught, remaining and refresh timing.
- Evidence: [Ape Escape decomposition](../games/a-f/ape-escape.md), with
  original-PlayStation first-stage and controls walkthrough corroboration.
- Novelty: first isolated for `GAME-0413`; a stage can settle before every
  advertised creature is reachable or caught.

## INF-407 — Show live leaks, mirrored pose, score and activity clock

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: the active view exposes the glass holes that can presently be covered, the player's reflected body placement against them and the current activity score and clock, without previewing the exact positions or arrival times of later damage.
- Includes: the 20,000 Leaks activity view pictured in Microsoft's original Kinect Adventures! manual, pp. 18–19.
- Excludes: a full future leak schedule; exact sensor recognition volumes; a multi-activity Adventure goal screen; an unseen timer inferred from another game mode.
- Parameters: visible hole positions, mirrored pose, active contact cue, score, clock and refresh timing.
- Evidence: [Kinect Adventures! decomposition](../games/g-l/kinect-adventures.md), inspected original Microsoft manual PDF pp. 18–19.
- Novelty: first isolated for `GAME-0414`; the present spatial contact targets and bodily alignment are exposed alongside live scored-time feedback.

## INF-408 — Expose taxi customers, assigned route, two clocks and fare feedback

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: a live taxi interface marks available customers with distance-coded icons and difficulty-sized pickup zones; after boarding it displays assigned destination direction and distance, customer and overall timers, current and total fares, manoeuvre combo and any time-bonus cue without revealing a guaranteed fastest street route.
- Includes: Dreamcast Crazy Taxi's Arcade/Original display and customer markers during the scoped Arcade-rule run.
- Excludes: a precomputed shortest-path itinerary; unknown future customer schedule; police Heat or a vehicle resource reserve.
- Parameters: icon colour, stop-zone size, route arrow, distance, clocks, fares, combo, ranking and time-bonus indicator.
- Evidence: [Crazy Taxi decomposition](../games/a-f/crazy-taxi.md), original Sega Dreamcast manual pp. 7, 9–11.
- Novelty: first isolated for `GAME-0415`; available-fare choice and the currently assigned service compete under separate visible deadlines and earnings feedback.

## INF-409 — Expose unit condition, reachable cells and terrain intel

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: the tactical view exposes current unit health and order availability, highlights the selected unit's presently reachable cells under its terrain-cost rules, and allows inspection of terrain type and defensive cover, without revealing the opposing commander's exact future orders or promising numeric cost values on the screen.
- Includes: the movement highlight and R-button terrain or unit information in Advance Wars Field Training `Terrain Intel`.
- Excludes: a guaranteed preview of Olaf's next target; the exact hidden damage or AI formula; fog-of-war revelation in a different mission; a post-battle-only report.
- Parameters: selected unit, current health, spent state, highlighted range, terrain type, cover rating and refresh timing.
- Evidence: [Advance Wars decomposition](../games/a-f/advance-wars.md), Nintendo's original booklet pp. 4–7 and 26 and the mission dialogue transcription.
- Novelty: first isolated for `GAME-0416`; inspection connects a unit-specific reachable route to visible terrain protection before an irreversible order.

## INF-410 — Expose a moving security scan and its local alarm state

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the current view exposes moving spotlight footprints and a linked alarm fixture, with a visible change when a scan detects the avatar, so the player can time passage and identify the local security controller without seeing future sweep positions.
- Includes: the two searchlight passages and red sirens in original PlayStation 2 *Sly Cooper and the Thievius Raccoonus* stage `A Stealthy Approach`.
- Excludes: an omniscient stage map, a numerical guard-suspicion meter, unrevealed traps, an exact preview of future patrol positions and the alarm-triggering rule itself (`SYS-1106`).
- Parameters: footprint visibility, sweep direction, warning colour, fixture location, enabled state, camera occlusion and update timing.
- Evidence: [Sly Cooper and the Thievius Raccoonus decomposition](../games/s-z/sly-cooper-and-the-thievius-raccoonus.md), original PlayStation 2 booklet and corroborated first-stage descriptions.
- Novelty: first isolated for `GAME-0417`; exact local security geometry is readable while its future motion is not precommitted as a tactical intent.

## INF-411 — Expose ship rooms, power and encounter state

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the tactical ship view exposes currently known crew and room conditions, system power and damage, shield and hull state, weapon charge and missile stock, opponent-visible systems and FTL readiness, while the sector map distinguishes reachable beacons without guaranteeing their future events.
- Includes: original FTL Kestrel combat controls and ship/sector displays during one first-sector hostile beacon.
- Excludes: exact hidden enemy intent, a guaranteed future event at every beacon, unobserved internal hit-roll probabilities, and the direct-control cockpit instrumentation of `INF-277`.
- Parameters: ship room, crew, system bars, shield, hull, target, weapon, reserve, jump readiness, beacon graph and fog state.
- Evidence: [FTL: Faster Than Light decomposition](../games/a-f/ftl-faster-than-light.md), official Subset Games materials and contemporary player interface accounts.
- Novelty: first isolated for `GAME-0418`; the player reads simultaneous room, power and route state through a command overview rather than an avatar-centred cockpit.

## INF-412 — Expose a puppy's condition and learned tricks

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: the home interface identifies the current puppy and makes its present condition and list of taught commands inspectable, alongside icons for the menus currently unlocked.
- Includes: opening Dog Status after naming and teaching sit in the original Nintendogs first-home session.
- Excludes: exposing an exact hidden microphone-confidence score; predicting future condition changes; a zoo-wide animal welfare dashboard; treating unavailable menus as already usable.
- Parameters: puppy name, condition, known tricks, active menu icons and current home state.
- Evidence: [Nintendogs decomposition](../games/m-r/nintendogs.md), Nintendo of America's original instruction booklet pp. 16–17.
- Novelty: first isolated for `GAME-0419`; per-puppy condition and learned voice vocabulary are visible before choosing a direct care action.

## INF-413 — Show temporary and banked driving-style score separately

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: the live race interface exposes current Kudos Stash, settled Kudos Bank and combo feedback as distinct fields alongside, but not replacing, current race position.
- Includes: original Project Gotham Racing 2 offline Kudos World Series Street Race screen.
- Excludes: a single total with no temporary state; final post-race breakdown; treating the visible place number as the style score; a multiplayer leaderboard.
- Parameters: stash amount, bank amount, combo state, current position and display update.
- Evidence: [Project Gotham Racing 2 decomposition](../games/m-r/project-gotham-racing-2.md), original Microsoft/Bizarre manual printed pp. 4 and 10–11.
- Novelty: first isolated for `GAME-0420`; the driver can read the unbanked timing-sensitive award separately from both retained style score and race place.

## INF-414 — Expose the drum beat, attack opportunity and formation state

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: during the live mission, pulsing screen edges indicate command cadence while visible formation and prey cues disclose current attack reach, squad health and consecutive rhythm progress needed for the next order.
- Includes: beat pulses, attack-ready eye, health and combo display in the original PSP *Patapon* first hunt.
- Excludes: a fully visible future off-screen route (`INF-001`); an instructor's displayed note chart (`INF-396`); exact input-window boundaries or damage values not shown by the manual.
- Parameters: beat phase, attack cue, visible formation members, health, combo and Fever display.
- Evidence: [Patapon decomposition](../games/m-r/patapon.md), Sony's original PSP manual pp. 2, 6 and 8, plus contemporary first-hunt guide.
- Novelty: first isolated for `GAME-0422`; cadence and tactical reach are disclosed together for a timed army-level order.

## INF-415 — Expose workshop vehicle ratings before challenge selection

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: the vehicle workshop shows current design ratings for speed, fuel, ammunition, weight and number of parts before the player tests, saves or selects the build for a challenge.
- Includes: Mumbo's Motors displaying the five original Xbox 360 Banjo-Kazooie: Nuts & Bolts ratings while a small scoop-equipped vehicle is prepared.
- Excludes: an exact numerical prediction of rock momentum; the live challenge's elapsed-time grade; an undisclosed future part; a general car-selection list without editable construction ratings.
- Parameters: speed, fuel, ammunition, weight, part count, selected design and update timing.
- Evidence: [Banjo-Kazooie: Nuts & Bolts decomposition](../games/a-f/banjo-kazooie-nuts-and-bolts.md), original Xbox 360 manual, Building Vehicles section.
- Novelty: first isolated for `GAME-0423`; the visible multi-axis ratings guide a functional build decision before a vehicle-dependent challenge.

## INF-416 — Show craft status, wingmate distress and settled route

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: a live flight interface displays the player's shield and boost state, aiming cursor and a named ally's distress or damage/down status, while the post-stage map exposes the route reached; it does not fully disclose future threats or an unearned alternative.
- Includes: original Star Fox 64 Corneria shield/boost gauges, cursor, Falco HELP cues, pause-state teammate condition and result map.
- Excludes: an omniscient enemy map; a live exact seven-arch counter not established by the original manual; guaranteed boss-shield display while Slippy is down; a pre-stage menu freely choosing Sector Y.
- Parameters: shield, boost, cursor, ally distress, pause-state damage, down marker, boss-gauge eligibility and settled route colour.
- Evidence: [Star Fox 64 decomposition](../games/s-z/star-fox-64.md), Nintendo's original manual pp. 13, 15, 18–19.
- Novelty: first isolated for `GAME-0424`; player damage, named wingmate survival and route result are exposed across live and settlement views relevant to one compound branch.

## INF-417 — Show village need, belief and creature lesson cues

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: the player can inspect a village's raised need through its store flag and allegiance through Village Center information, while a light bulb above a teaching creature indicates learned observation; these cues do not disclose exact future learning or belief gains.
- Includes: *Black & White* Land 1 Food Desire flag and tooltip, Village Center belief tooltip and creature learning light bulb during a watched Food Miracle demonstration.
- Excludes: an exact numerical learning-per-cast forecast; automatic visibility of all future village desires; an unrelated settlement's group Resolve trajectory (`INF-065`).
- Parameters: village, flag type and height, current belief display, learner feedback and disclosed versus hidden progress.
- Evidence: [Black & White decomposition](../games/a-f/black-and-white.md), original Lionhead manual pp. 11, 18–19.
- Novelty: first isolated for `GAME-0425`; two distinct live recipients of the same divine action have inspectable need/belief and teaching feedback without full hidden-model disclosure.

## INF-418 — Mark peelable paper and rear-touch interaction sites

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `Medium`
- Definition: visible paper tabs or edges identify a layer the player can manipulate from the front, while symbols on a thin or transparent surface identify the corresponding rear-touch interaction site; these affordances disclose input mode but not a guaranteed future landing.
- Includes: early *Tearaway* movable paper tabs and symbol-marked Vita rear-touch drum surfaces.
- Excludes: an exact landing trajectory preview; a universal touch affordance on every paper surface; a map of hidden future chapters; a touchscreen-only decoration prompt.
- Parameters: peel-edge cue, rear-touch marking, eligible surface, cue visibility and undisclosed destination.
- Evidence: [Tearaway decomposition](../games/s-z/tearaway.md), Sony PlayStation Blog hands-on and Pocket Gamer's lead-designer early-level walkthrough.
- Novelty: first isolated for `GAME-0426`; two visibly differentiated physical input affordances govern the same local route.

## INF-419 — Show contracting Taken corona and darkness-break flash

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: the light corona around a darkness-protected hostile visibly contracts under illumination and a bright flash marks complete removal, distinguishing a still-protected target from one that ordinary shots may wound.
- Includes: Taken shroud exposure cue in original Xbox 360 *Alan Wake*.
- Excludes: exact numerical shroud health or remaining exposure time; a guaranteed firearm hit; player flashlight charge HUD (`INF-119`); permanent target markers after the encounter.
- Parameters: target, corona extent, illuminated state, break flash and visible damage-legality cue.
- Evidence: [Alan Wake decomposition](../games/a-f/alan-wake.md), original Microsoft/Remedy Xbox 360 manual p. 12.
- Novelty: first isolated for `GAME-0427`; the target itself reveals the transition from light-dependent protection to conventional vulnerability.

## INF-420 — Display one selected guard's current near and far sight regions

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: inspecting one hostile observer displays that observer's current directed sight region with distinct near and far visibility zones, while other unselected observers continue to perceive without simultaneous displayed cones.
- Includes: selecting one German guard in original *Commandos: Behind Enemy Lines* to see his bright near and dark far sight areas as he patrols.
- Excludes: omniscient simultaneous cones for every guard; exact future patrol positions; a cumulative detection meter; guaranteed safety from an unselected guard; the underlying detection legality (`CON-077`).
- Parameters: selected guard, facing, near and far extents, visual obstruction, current posture and update timing.
- Evidence: [Commandos: Behind Enemy Lines decomposition](../games/a-f/commandos-behind-enemy-lines.md), original Pyro/Eidos manual, enemy-view instructions.
- Novelty: first isolated for `GAME-0429`; visible sight information is explicitly limited to one selected observer despite simultaneous live threats.

## INF-421 — Show current power bars and unsigned response-impact cues

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `Medium`
- Definition: the interface displays the present values of several political power reserves and, while inspecting an offered response before commitment, marks which reserves it may affect without revealing the direction or magnitude of each change.
- Includes: original 2016 Reigns showing church, people, army and treasury bars and tilt-time affected-domain dots.
- Excludes: exact signed delta previews; the hidden next-card identity (`INF-002`); complete disclosure of narrative flags or card weights; certainty that every shown effect is beneficial.
- Parameters: displayed reserves, response side, indicated affected subset, concealed sign and magnitude.
- Evidence: [Reigns decomposition](../games/m-r/reigns.md), François Alliot's four-dimension account and Emily Short's dated firsthand discussion of the tilt cue.
- Novelty: first isolated for `GAME-0432`; a player can see both the current risk position and the domains a contemplated binary response touches without receiving a signed forecast.

## INF-422 — Directional returned echo exposes local undersea features

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: a player-requested song echo discloses Ecco's position and a bounded facing-region map with rock boundaries and distinguishable nearby hazards, glyphs, air pockets or other marked features, without revealing the entire remaining level.
- Includes: the held A-button sonar display used to orient a Bay of Medusa dive in original Genesis *Ecco the Dolphin*.
- Excludes: a permanently revealed global map; a guaranteed route solution; using only the normal visible viewport; an Odradek terrain-and-cargo survey (`ACT-471`).
- Parameters: facing, echo return, shown region, feature categories, map lifetime and current position.
- Evidence: [Ecco the Dolphin decomposition](../games/a-f/ecco-the-dolphin.md), original Sega Genesis manual, pp. 5 and 8.
- Novelty: first isolated for `GAME-0433`; the player deliberately requests an acoustic, direction-bounded spatial view before committing to a breath-limited route.

## INF-423 — Show charged scarf and currently formed bridge spans

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the scarf's visible luminous pattern indicates usable power,
  while nearby raised cloth and absent sections show the current bridge route;
  these local cues do not reveal future online companions or a whole-area map.
- Includes: checking whether the original PS3 *Journey* traveller can jump
  toward a visible raised span or should regain scarf charge first.
- Excludes: a numeric exact energy gauge; omniscient future matchmaking;
  a proof that every remaining gap is currently crossable; an automated route.
- Parameters: scarf glow, local section state, current viewpoint and optional
  companion visibility.
- Evidence: [Journey decomposition](../games/g-l/journey.md), PlayStation's
  first-person retrospective and original-PS3 first-hand walkthrough.
- Novelty: first isolated for `GAME-0436`; the costume itself communicates
  resource readiness beside a visibly changing traversal surface.

## INF-424 — Show live balance steering and immediate gate outcome

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: while a body-steered course advances, display the avatar and
  approaching local gates together with a live balance-position cue, then
  immediately signal whether each crossed gate was passed or missed, so the
  player can correct subsequent physical input.
- Includes: the balance dot, visible skier and flags, and gate success/failure
  feedback in original Wii Fit Beginner Ski Slalom.
- Excludes: an exact future steering trace; full-course route omniscience;
  numeric board-to-avatar sensor coefficients; a result visible only after
  finishing; Wii Fit Body Test's standalone centre-of-balance assessment.
- Parameters: current balance cue, skier position, visible gate, pass/miss
  signal, feedback timing and local camera region.
- Evidence: [Wii Fit decomposition](../games/s-z/wii-fit.md), the first-hand
  original-game guide and Jelsma et al.'s observed on-course feedback.
- Novelty: first isolated for `GAME-0439`; live embodied-control feedback is
  paired with per-gate correctness during one continuous activity.

## INF-425 — Show a contextual need hint without prescribing the object

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: an authored puzzle gives a brief visible instruction about an
  actor's or scene's unmet need, while leaving the compatible object noun
  unstated for the player to infer from the hint and environment.
- Includes: original *Scribblenauts* DS Puzzle 1-5 showing `Refresh Him` for
  a wanderer in the desert without naming lemonade as the required answer.
- Excludes: a list of all accepted nouns; a hidden request with no clue;
  an exact future-state preview; the separate result of delivering an object.
- Parameters: current actor, hint text, visible setting, inferred need and
  undisclosed accepted object classes.
- Evidence: [Scribblenauts decomposition](../games/s-z/scribblenauts.md),
  original Nintendo DS instruction booklet, Puzzle Mode example.
- Novelty: first isolated for `GAME-0440`; the puzzle communicates a need
  without converting its open object choice into a multiple-choice menu.

## INF-426 — Show location-linked map position and nearby wild targets

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the map view exposes the trainer's current device-linked position and currently visible nearby wild creatures, allowing the player to choose a target rather than revealing the exact future spawn schedule.
- Includes: the original Pokémon GO walking map showing a wild Pokémon within touch range before the player opens its catch encounter.
- Excludes: a complete map of every hidden future spawn; a turn-based random battle that begins without a visible map target; the separate ring shown only after entering the catch view.
- Parameters: trainer marker, visible local map, nearby wild marker, contact range and refresh state.
- Evidence: [Pokémon GO decomposition](../games/m-r/pokemon-go.md), Niantic's 2016 launch account, contemporary guidance and official catch help for map visibility.
- Novelty: first isolated for `GAME-0441`; this information makes real location and target selection legible before the catch interface opens.

## INF-427 — Show encounter difficulty and throw timing through a target ring

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: when a capture device is readied against a visible wild creature, a coloured target ring changes size and indicates relative capture difficulty and an aim/timing opportunity, without disclosing an exact or guaranteed catch probability.
- Includes: green-to-red difficulty cue and shrinking ring while holding a Ball in the original Pokémon GO ordinary wild encounter.
- Excludes: a deterministic success promise at any ring size; a full hidden catch-rate formula; the map view before the target is tapped; post-catch XP as a pre-throw forecast.
- Parameters: target, current ring size, ring colour, Ball readiness and visible aim region.
- Evidence: [Pokémon GO decomposition](../games/m-r/pokemon-go.md), contemporary July 2016 first-hand guidance and official catch help for the continuing target-ring affordance.
- Novelty: first isolated for `GAME-0441`; encounter-specific difficulty/timing feedback differs from the map's indication of which wild target is locally available.

## INF-428 — Expose the live gunfight clock, rounds and life stock

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `Medium`
- Definition: the current gunfight interface shows the countdown, available shots and remaining lives alongside visible enemies so the player can decide when to expose, fire or return to cover without seeing hidden successor threats.
- Includes: the original arcade *Time Crisis* Story Game displaying the bounded stage clock, six-shot ammunition cycle and life allowance during an active combat view.
- Excludes: perfect knowledge of future enemy positions; an exact hostile-attack forecast; a score-only clock; the system's actual countdown and shot-consumption rules.
- Parameters: clock, rounds, lives, current view, exposed hostiles and update timing.
- Evidence: [Time Crisis decomposition](../games/s-z/time-crisis.md), Namco operator manual and contemporary first-hand arcade guides.
- Novelty: first isolated for `GAME-0443`; multiple live survival resources are disclosed in the same exposure-and-cover decision window.

## INF-429 — Show Mare time, chip tally, capture state and drill gauge

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: the flight HUD exposes remaining stage time, currently held
  Color Chips, Ideya Capture strength, score and usable Drill Attack gauge,
  without disclosing a solved route or future threat timing.
- Includes: the original-Saturn *NiGHTS* Nightopia screen during the first
  Spring Valley Mare.
- Excludes: the actual countdown and gauge transitions; a later boss HUD;
  perfect knowledge of unseen collectibles.
- Parameters: time, chip count, capture strength, score, gauge and update.
- Evidence: [NiGHTS into Dreams decomposition](../games/m-r/nights-into-dreams.md), original Saturn manual's Nightopia screen diagram.
- Novelty: first isolated for `GAME-0445`; collection, target durability
  and burst capacity are disclosed together inside the live flight loop.

## INF-430 — Preview rail resources, alignment grade and station reach

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: before a railway build decision, current resource supply and demand, prospective track cost/grade and a proposed station's service circle are exposed for spatial planning.
- Includes: Tutorial resource overlay, track drag feedback and station radius in original PC *Railroad Tycoon II*.
- Excludes: a fixed promise about randomly placed future resources; future goods output quantity; the company budget ledger.
- Parameters: resource icons, demand colours, projected route, price, grade and catchment.
- Evidence: [Railroad Tycoon II decomposition](../games/m-r/railroad-tycoon-ii.md), original manual's Tutorial map, track and station instructions.
- Novelty: first isolated for `GAME-0446`; spatial transport feasibility is inspected before committing paid infrastructure.

## INF-431 — Show founder cash, shares and personal net worth separately

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: a personal portfolio view shows the founder's cash and share holdings as personal net worth, distinct from the railroad company's ledger and treasury.
- Includes: Tutorial personal portfolio and $10 million personal-net-worth scenario target in original PC *Railroad Tycoon II*.
- Excludes: treating corporate transport income as instant personal cash; company income and expenditure categories (`INF-058`); a guaranteed future stock price.
- Parameters: cash, shares, valuation, net-worth total and corporate comparison.
- Evidence: [Railroad Tycoon II decomposition](../games/m-r/railroad-tycoon-ii.md), original manual's Tutorial and Finances chapters.
- Novelty: first isolated for `GAME-0446`; dual account visibility prevents a successful paid route from being misread as scenario completion.

## INF-432 — Show boxing stamina, hearts, stars, round, clock and points

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: the live bout display exposes each boxer's stamina and Little Mac's distinct heart and star stocks together with the current round, remaining time and points.
- Includes: the NES *Punch-Out!! Featuring Mr. Dream* in-bout display.
- Excludes: exact future punch timing; opponent move script; a generic paired-health display without the separate heart and star resources.
- Parameters: paired stamina, heart count, star count, round, clock and points.
- Evidence: [Punch-Out!! decomposition](../games/m-r/punch-out.md), official Nintendo NES Classic manual p. 6.
- Novelty: first isolated for `GAME-0447`; the display distinguishes three non-interchangeable boxer stocks and points in one timed bout.

## INF-433 — Show the next corridor bend, obstacle and coin line

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the third-person following view exposes the runner's present path width and a bounded approaching slice of bends, gaps, obstacles and optional coin lines, while the later continuing course remains unseen.
- Includes: reading a left temple-wall corner and side coin row before input during original-iPhone *Temple Run*.
- Excludes: a full future map; an exact forecast of subsequent generated segments; Geometry Dash's side-scrolling authored-level viewport (`INF-192`).
- Parameters: camera position, forward horizon, path width, corner visibility, obstacle and coin contrast, speed.
- Evidence: [Temple Run decomposition](../games/s-z/temple-run.md), Imangi's temple-wall account and contemporary first-hand mobile reviews.
- Novelty: first isolated for `GAME-0448`; an over-the-shoulder changing corridor must be read while forward movement cannot wait.

## INF-434 — Expose partner-battle resources, targets and effect feedback

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: a turn-combat screen presents protagonist HP and FP, current partner, available commands and eligible target selection, then displays damage, recovery and abnormal-condition feedback after resolution.
- Includes: reading Mario's resources, Kooper's command and Fuzzy damage feedback in original-N64 *Paper Mario*.
- Excludes: a future enemy-move forecast, exact Action Command frame windows or an initiative queue with per-character AP (`INF-141`).
- Parameters: health, special-resource balance, active partner, command, target, damage, recovery and condition icon.
- Evidence: [Paper Mario decomposition](../games/m-r/paper-mario.md), Nintendo's N64 manual pp. 8, 14–15 and 20–21.
- Novelty: first isolated for `GAME-0449`; a fixed protagonist and swappable helper share a battle presentation but not an AP queue.

## INF-435 — Show downhill place, speed and trick-boost state

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `Medium`
- Definition: expose current race place and speed, trick score, adrenaline, Uber eligibility and TRICKY-letter progression alongside nearby course and rivals.
- Includes: live Race feedback in original *SSX Tricky*.
- Excludes: a full future-course map; opponent plans; Showoff crystals and timer; motor-racing gear HUD.
- Parameters: place, speed, score, meter, Uber window, letters, terrain and rival proximity.
- Evidence: [SSX Tricky decomposition](../games/s-z/ssx-tricky.md), EA's original booklet and first-hand PS2 guide.
- Novelty: first isolated for `GAME-0450`; the rider reads stunt-earned speed capacity alongside rank.

## INF-436 — Expose a local traversal view, weapon acquisition and carried condition

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: a following or directed local view discloses nearby terrain and hostiles; weapon posture exposes acquisition, while condition, compass and inventory displays disclose current health, facing and carried supplies without revealing the full future route.
- Includes: Original Tomb Raider's local Look, pistol-aim pose, health, compass and inventory-ring disclosure.
- Excludes: A full cave map; exact future trap schedule; enemy plans; precise jump frame windows; a first-person rule-changing gaze.
- Parameters: viewpoint, facing, nearby geometry, visible hostile, aim pose, condition and supplies.
- Evidence: [Tomb Raider (1996) decomposition](../games/s-z/tomb-raider-1996.md), the source ledger and transitions for this scoped packet.
- Novelty: first isolated for `GAME-0451`; no external novelty claim.

## INF-441 — Show the current local proof tally against a stated mission quota

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the mission briefing states a finite required proof quantity and the live interface exposes how many qualifying physical proofs the actor has collected in the current location, allowing a return decision without revealing unseen targets or future route geometry.
- Includes: the Westside Hotel request for 25 Gold Gems and the current-location Metal Bug Gem counter in original PSP Daxter.
- Excludes: counting defeats before their proof is collected; a distinct-creature capture stage (`INF-406`); an omniscient enemy map; a global collectible total detached from the assigned locality; optional Precursor Orb progress.
- Parameters: required quota, credited local proof count, briefing channel, display channel, locality and refresh after collection.
- Evidence: [Daxter decomposition](../games/a-f/daxter.md), original PSP UCES-00044/ANZ manual PDF leaf 6 and independent original-PSP first-hotel routes by Larry Imgrund and Akiro.
- Novelty: first isolated for `GAME-0459`; no claim that the HUD itself always displays the required number.

## INF-442 — Show shared household cash and itemised daily budget

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: the interface exposes one private household's currently spendable shared cash and an itemised recent-day income and expense ledger, letting the player compare a proposed purchase with the household's actual means.
- Includes: original *The Sims* Control Panel Simoleon total and Budget window's current and previous-day credits and debits before buying a chair.
- Excludes: a municipality's tax-and-service treasury (`INF-058`); one undifferentiated score; unseen future bills; a Sim's individual motive bars.
- Parameters: household, cash total, income category, expense category, day and purchase price.
- Evidence: [The Sims (2000) decomposition](../games/s-z/the-sims.md), original Maxis/EA PC manual pp. 15 and 65–67.
- Novelty: first isolated for `GAME-0461`; the existing managed-domain ledger expressly excludes private household accounts.

## INF-443 — Show live street resources and current mapped district targets

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: the active street interface reports stamina, carried spray and completed-versus-required graffiti, while the paused district map locates outstanding graffiti points and the currently disclosed rival position without exposing hidden future encounters.
- Includes: original Xbox Jet Set Radio Future Dogenzaka Hill HUD and pause-map reading before and after Beat appears.
- Excludes: an authoritative story countdown or directional graffiti command from the original Jet Set Radio (`INF-367`); complete future route disclosure; VS-mode Graffiti Wars time; external walkthrough hints.
- Parameters: stamina, spray stock, completed count, quota, map, remaining marks, current rival marker and disclosure timing.
- Evidence: [Jet Set Radio Future decomposition](../games/g-l/jet-set-radio-future.md), original Xbox instruction manual pp. 13–14 and contemporary Dogenzaka route corroboration.
- Novelty: first isolated for `GAME-0464`; the local street map and quota persist into a staged moving-rival task without the predecessor's time or command-trace display.

## INF-469 — Expose current traversal, companion and separate collection state

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `Medium`
- Definition: the current play view and pause or stage summary expose local geometry, actors, companion health, collection counters and independent completion indicators, with local bonus time or a cycling exit symbol when applicable; hidden reward locations and exact internal formulas remain undisclosed.
- Includes: Original Wii live hearts, pause bananas/balloons/coins/letters/pieces, bonus clock, slot display and map collection icons.
- Excludes: Complete secret-location disclosure; future commands; exact hidden physics or reward formulas; only a post-game score.
- Parameters: view, visible range, indicators, counters, local timer and summary.
- Evidence: [Donkey Kong Country Returns decomposition](../games/a-f/donkey-kong-country-returns.md), original USA Wii booklet pp. 9–22 and contemporary written first-stage routes and play testimony; retention limits are attributed separately there. No native execution.
- Novelty: first isolated for `GAME-0495`; boundary counterexamples are reviewed in [`TAXONOMY_CHANGE_232`](../../research/taxonomy-changes/TAXONOMY_CHANGE_232.md). No external novelty claim.
