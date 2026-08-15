# Game Genomes

Each game file contains a complete evidence-backed decomposition and a typed
genome. The generated [index](INDEX.md) is the corpus lookup; game records own
the canonical stored genomes.

## Required contents

- stable `GAME-xxxx` ID and path slug;
- sources and claim ledger;
- player actions and automatic behaviours;
- constraints, information, objectives and time;
- strategy, replay, failure and adjacent systems;
- active gene IDs;
- full-corpus comparison using the
  [canonical signature rules](../../docs/ARCHITECTURE.md#genome-signature);
- mathematically selected near matches;
- combination result and explicit negative findings.

## Path rule

Use one non-semantic slug shard:

- `0-9/`
- `a-f/`
- `g-l/`
- `m-r/`
- `s-z/`

Do not organise canonical files by puzzle family. Family classifications may
change; stable paths should not. Reusable many-to-many classifications live in
the controlled [mechanical-family registry](../families/README.md); the Game
Index's short profile remains a game-specific navigation summary.

## Completed

<!-- BEGIN GENERATED: COMPLETED_GAMES -->
- [`GAME-0001` — 2048](0-9/2048.md)
- [`GAME-0002` — Rubik’s Cube](m-r/rubiks-cube.md)
- [`GAME-0003` — Minesweeper](m-r/minesweeper.md)
- [`GAME-0004` — Tetris](s-z/tetris.md)
- [`GAME-0005` — Sudoku](s-z/sudoku.md)
- [`GAME-0006` — Sokoban](s-z/sokoban.md)
- [`GAME-0007` — FreeCell](a-f/freecell.md)
- [`GAME-0008` — Nonogram](m-r/nonogram.md)
- [`GAME-0009` — Royal Match](m-r/royal-match.md)
- [`GAME-0010` — Water Sort](s-z/water-sort.md)
- [`GAME-0011` — Chess](a-f/chess.md)
- [`GAME-0012` — Flow Free](a-f/flow-free.md)
- [`GAME-0013` — Baba Is You](a-f/baba-is-you.md)
- [`GAME-0014` — Into the Breach](g-l/into-the-breach.md)
- [`GAME-0015` — Threes](s-z/threes.md)
- [`GAME-0016` — Pipe Mania / Pipe Dream](m-r/pipe-mania.md)
- [`GAME-0017` — Balatro](a-f/balatro.md)
- [`GAME-0018` — Mini Metro](m-r/mini-metro.md)
- [`GAME-0019` — Peg Solitaire](m-r/peg-solitaire.md)
- [`GAME-0020` — Dorfromantik](a-f/dorfromantik.md)
- [`GAME-0021` — Cut the Rope](a-f/cut-the-rope.md)
- [`GAME-0022` — Opus Magnum](m-r/opus-magnum.md)
- [`GAME-0023` — Return of the Obra Dinn](m-r/return-of-the-obra-dinn.md)
- [`GAME-0024` — Gorogoa](g-l/gorogoa.md)
- [`GAME-0025` — Lemmings](g-l/lemmings.md)
- [`GAME-0026` — World of Goo](s-z/world-of-goo.md)
- [`GAME-0027` — Bad North: Jotunn Edition](a-f/bad-north.md)
- [`GAME-0028` — Loop Hero](g-l/loop-hero.md)
- [`GAME-0029` — HUMANITY](g-l/humanity.md)
- [`GAME-0030` — Tin Hearts](s-z/tin-hearts.md)
- [`GAME-0031` — Timelie](s-z/timelie.md)
- [`GAME-0032` — SpaceChem](s-z/spacechem.md)
- [`GAME-0033` — Portal](m-r/portal.md)
- [`GAME-0034` — Braid, Anniversary Edition](a-f/braid.md)
- [`GAME-0035` — Pikmin 4](m-r/pikmin-4.md)
- [`GAME-0036` — Patrick’s Parabox](m-r/patricks-parabox.md)
- [`GAME-0037` — Cosmic Express](a-f/cosmic-express.md)
- [`GAME-0038` — The Swapper](s-z/the-swapper.md)
- [`GAME-0039` — The Witness](s-z/the-witness.md)
- [`GAME-0040` — Carto](a-f/carto.md)
- [`GAME-0041` — Viewfinder](s-z/viewfinder.md)
- [`GAME-0042` — Infinifactory](g-l/infinifactory.md)
- [`GAME-0043` — Stephen’s Sausage Roll](s-z/stephens-sausage-roll.md)
- [`GAME-0044` — A Good Snowman Is Hard to Build](a-f/a-good-snowman-is-hard-to-build.md)
- [`GAME-0045` — Snakebird](s-z/snakebird.md)
- [`GAME-0046` — The Case of the Golden Idol](s-z/the-case-of-the-golden-idol.md)
- [`GAME-0047` — Fights in Tight Spaces](a-f/fights-in-tight-spaces.md)
- [`GAME-0048` — Tactical Breach Wizards](s-z/tactical-breach-wizards.md)
- [`GAME-0049` — Hexcells Infinite](g-l/hexcells-infinite.md)
- [`GAME-0050` — Shogun Showdown](s-z/shogun-showdown.md)
- [`GAME-0051` — Mini Motorways](m-r/mini-motorways.md)
- [`GAME-0052` — Freeways](a-f/freeways.md)
- [`GAME-0053` — Can of Wormholes](a-f/can-of-wormholes.md)
- [`GAME-0054` — A Monster’s Expedition](a-f/a-monsters-expedition.md)
- [`GAME-0055` — Bonfire Peaks](a-f/bonfire-peaks.md)
- [`GAME-0056` — Railbound](m-r/railbound.md)
- [`GAME-0057` — Golf Peaks](g-l/golf-peaks.md)
- [`GAME-0058` — inbento](g-l/inbento.md)
- [`GAME-0059` — KAMI](g-l/kami.md)
- [`GAME-0060` — HOOK](g-l/hook.md)
- [`GAME-0061` — LYNE](g-l/lyne.md)
- [`GAME-0062` — Hexologic](g-l/hexologic.md)
- [`GAME-0063` — Rush Hour](m-r/rush-hour.md)
- [`GAME-0064` — SET](s-z/set.md)
- [`GAME-0065` — Mastermind](m-r/mastermind.md)
- [`GAME-0066` — Black Box](a-f/black-box.md)
- [`GAME-0067` — Simon](s-z/simon.md)
- [`GAME-0068` — Wordle](s-z/wordle.md)
- [`GAME-0069` — Lights Out](g-l/lights-out.md)
- [`GAME-0070` — Inertia](g-l/inertia.md)
- [`GAME-0071` — Slant](s-z/slant.md)
- [`GAME-0072` — Tents](s-z/tents.md)
- [`GAME-0073` — Dominosa](a-f/dominosa.md)
- [`GAME-0074` — Bridges](a-f/bridges.md)
- [`GAME-0075` — Light Up](g-l/light-up.md)
- [`GAME-0076` — Loopy](g-l/loopy.md)
- [`GAME-0077` — Map](m-r/map.md)
- [`GAME-0078` — Galaxies](g-l/galaxies.md)
- [`GAME-0079` — Filling](a-f/filling.md)
- [`GAME-0080` — Keen](g-l/keen.md)
- [`GAME-0081` — Pearl](m-r/pearl.md)
- [`GAME-0082` — Signpost](s-z/signpost.md)
- [`GAME-0083` — Net](m-r/net.md)
- [`GAME-0084` — Netslide](m-r/netslide.md)
- [`GAME-0085` — The Room](s-z/the-room.md)
- [`GAME-0086` — Machinarium](m-r/machinarium.md)
- [`GAME-0087` — The Longest Journey](s-z/the-longest-journey.md)
- [`GAME-0088` — Day of the Tentacle](a-f/day-of-the-tentacle.md)
- [`GAME-0089` — Stardew Valley](s-z/stardew-valley.md)
- [`GAME-0090` — The Talos Principle](s-z/the-talos-principle.md)
- [`GAME-0091` — Fez](a-f/fez.md)
- [`GAME-0092` — Echochrome](a-f/echochrome.md)
- [`GAME-0093` — Monument Valley](m-r/monument-valley.md)
- [`GAME-0094` — Superliminal](s-z/superliminal.md)
- [`GAME-0095` — Manifold Garden](m-r/manifold-garden.md)
- [`GAME-0096` — Maquette](m-r/maquette.md)
- [`GAME-0097` — Antichamber](a-f/antichamber.md)
- [`GAME-0098` — Hyperbolica](g-l/hyperbolica.md)
- [`GAME-0099` — HyperRogue](g-l/hyperrogue.md)
- [`GAME-0100` — Keep Talking and Nobody Explodes](g-l/keep-talking-and-nobody-explodes.md)
- [`GAME-0101` — Chants of Sennaar](a-f/chants-of-sennaar.md)
- [`GAME-0102` — The Password Game](s-z/the-password-game.md)
- [`GAME-0103` — Papers, Please](m-r/papers-please.md)
- [`GAME-0104` — TUNIC](s-z/tunic.md)
- [`GAME-0105` — Outer Wilds](m-r/outer-wilds.md)
- [`GAME-0106` — Her Story](g-l/her-story.md)
- [`GAME-0107` — The Pedestrian](s-z/the-pedestrian.md)
- [`GAME-0108` — Cocoon](a-f/cocoon.md)
<!-- END GENERATED: COMPLETED_GAMES -->

Use the [game-analysis template](../../templates/GAME_ANALYSIS_TEMPLATE.md) and
the public [evidence model](../../docs/EVIDENCE_MODEL.md). Subject selection remains in
the private working repository.
