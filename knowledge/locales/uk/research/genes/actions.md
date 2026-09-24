# Гени дій

## ACT-001

- Назва: Глобальний напрямлений зсув
- Переглянуто: `2026-08-24`

### Операційне визначення

Гравець обирає напрямок і намагається перемістити кожен рухомий елемент уздовж цього напрямку.

### Включає

Одна команда, глобально пов’язана з кількома рядками або стовпцями.

### Виключає

Вибір одного елемента та його незалежне переміщення; автоматичне ущільнення після вибору напрямку.

### Ігри-носії

- [`GAME-0001` — "2048"](../games/0-9/2048.md)
- [`GAME-0015` — Threes](../games/s-z/threes.md)

## ACT-002

- Назва: Безпосереднє обертання шару
- Переглянуто: `2026-08-24`

### Операційне визначення

Гравець безпосередньо обирає зв’язаний шар елементів і обертає його як єдине жорстке ціле.

### Включає

Поворот зовнішнього шару грані стандартного кубика Рубіка 3 × 3.

### Виключає

Обертання всього об’єкта лише для зміни ракурсу; незалежне обертання одного елемента; автоматичне обертання як наслідок іншої дії.

### Ігри-носії

- [`GAME-0002` — "Rubik’s Cube"](../games/m-r/rubiks-cube.md)

## ACT-003

- Назва: Вибір прихованої клітинки для відкриття
- Переглянуто: `2026-08-24`

### Операційне визначення

Гравець обирає одну приховану позицію та наказує відкрити її заздалегідь визначений внутрішній вміст.

### Включає

Відкриття однієї закритої клітинки у Minesweeper.

### Виключає

Сусідні клітинки, які система відкриває автоматично; вибір уже видимої інформації; створення нового випадкового вмісту після вибору.

### Ігри-носії

- [`GAME-0003` — Minesweeper](../games/m-r/minesweeper.md)

## ACT-004

- Назва: Перемикання захисної позначки-гіпотези
- Переглянуто: `2026-08-24`

### Операційне визначення

Гравець позначає приховану позицію як імовірну небезпеку або знімає з неї позначку, не перевіряючи вміст; доки позначку встановлено, вона блокує звичайне відкриття.

### Включає

Встановлення та зняття прапорця на закритій клітинці Minesweeper.

### Виключає

Небезпека, підтверджена системою; декоративна нотатка без впливу на введення; автоматичне відкриття непозначених сусідів.

### Ігри-носії

- [`GAME-0003` — Minesweeper](../games/m-r/minesweeper.md)

## ACT-005

- Назва: Зміна положення активного елемента, що падає
- Переглянуто: `2026-08-24`

### Операційне визначення

Поки елемент опускається під керуванням системи, гравець безпосередньо змінює його дозволене горизонтальне положення або орієнтацію до моменту фіксації.

### Включає

Переміщення або обертання активного тетроміно в NES Tetris A-Type.

### Виключає

Автоматичне падіння; переміщення вже зафіксованих елементів; обертання зв’язаного шару постійного об’єкта.

### Ігри-носії

- [`GAME-0004` — Tetris](../games/s-z/tetris.md)

## ACT-006

- Назва: Прискорити перебіг симуляції
- Переглянуто: `2026-08-24`

### Операційне визначення

Гравець тимчасово збільшує швидкість автоматичної зміни стану, керованої часом, не змінюючи її напрямку чи умови завершення.

### Включає

Утримання кнопки вниз для швидшого падіння активного тетроміно в NES Tetris; вибір режиму `FAST` для прискорення Flooz у Pipe Dream після розміщення труб; вибір швидшого годинника симуляції Mini Metro, поки тривають автоматичні попит і перевезення; прискорення симуляції натовпу в HUMANITY після підготовки поля команд; прискорення солдатиків Tin Hearts без зміни їхнього фізичного маршруту; утримання регулятора швидкості Echochrome, поки Walker іде тим самим маршрутом, визначеним проєкцією.

### Виключає

Миттєве жорстке падіння; вибір напрямку руху; зміна постійного рівня складності поза грою.

### Ігри-носії

- [`GAME-0124` — Against the Storm](../games/a-f/against-the-storm.md)
- [`GAME-0132` — Anno 1800](../games/a-f/anno-1800.md)
- [`GAME-0135` — "Captain of Industry"](../games/a-f/captain-of-industry.md)
- [`GAME-0284` — "Cities: Skylines II"](../games/a-f/cities-skylines-ii.md)
- [`GAME-0121` — "Cities: Skylines"](../games/a-f/cities-skylines.md)
- [`GAME-0204` — "Crusader Kings III"](../games/a-f/crusader-kings-iii.md)
- [`GAME-0126` — Dwarf Fortress](../games/a-f/dwarf-fortress.md)
- [`GAME-0092` — Echochrome](../games/a-f/echochrome.md)
- [`GAME-0175` — Football Manager 26](../games/a-f/football-manager-26.md)
- [`GAME-0130` — Frostpunk](../games/a-f/frostpunk.md)
- [`GAME-0182` — Hearts of Iron IV](../games/g-l/hearts-of-iron-iv.md)
- [`GAME-0029` — HUMANITY](../games/g-l/humanity.md)
- [`GAME-0018` — Mini Metro](../games/m-r/mini-metro.md)
- [`GAME-0051` — Mini Motorways](../games/m-r/mini-motorways.md)
- [`GAME-0125` — Oxygen Not Included](../games/m-r/oxygen-not-included.md)
- [`GAME-0016` — Pipe Mania / Pipe Dream](../games/m-r/pipe-mania.md)
- [`GAME-0298` — 'Planet Zoo: Console Edition'](../games/m-r/planet-zoo-console-edition.md)
- [`GAME-0142` — Project Zomboid](../games/m-r/project-zomboid.md)
- [`GAME-0127` — RimWorld](../games/m-r/rimworld.md)
- [`GAME-0335` — RollerCoaster Tycoon Deluxe](../games/m-r/rollercoaster-tycoon-deluxe.md)
- [`GAME-0390` — SimCity 2000](../games/s-z/simcity-2000.md)
- [`GAME-0118` — SimCity 4 Deluxe Edition](../games/s-z/simcity-4-deluxe-edition.md)
- [`GAME-0287` — Stellaris](../games/s-z/stellaris.md)
- [`GAME-0136` — "Surviving Mars: Relaunched"](../games/s-z/surviving-mars.md)
- [`GAME-0004` — Tetris](../games/s-z/tetris.md)
- [`GAME-0370` — Theme Hospital](../games/s-z/theme-hospital.md)
- [`GAME-0133` — Timberborn](../games/s-z/timberborn.md)
- [`GAME-0030` — Tin Hearts](../games/s-z/tin-hearts.md)
- [`GAME-0134` — "Workers & Resources: Soviet Republic"](../games/s-z/workers-resources-soviet-republic.md)

## ACT-007

- Назва: Призначення символу вільній позиції
- Переглянуто: `2026-08-24`

### Операційне визначення

Гравець обирає одну позицію, якій зараз можна призначити значення, і записує один символ із дозволеної області як запропоноване значення цієї позиції.

### Включає

Внесення цифри від 1 до 9 у порожню клітинку Sudoku; позначення клітинки Nonogram як заповненої або підтверджено порожньої; натискання редагованої клітинки Hexologic, щоб призначити чи замінити її запропоноване значення з однієї, двох або трьох цяток; призначення символу `/` або зворотної скісної риски одній клітинці Slant; установлення чи вилучення лампи в одній білій клітинці Light Up; призначення одного з чотирьох кольорів палітри одній редагованій області Map; призначення цифри від 1 до 9 одній редагованій клітинці Filling; призначення цифри від 1 до 6 одній клітинці Keen; установлення намету або явної позначки відсутності намету в одній редагованій клітинці Tents.

### Виключає

Відкриття вже наявного прихованого значення; нотування кількох можливих кандидатів без призначення одного; зміна незмінної початкової підказки.

### Ігри-носії

- [`GAME-0066` — Black Box](../games/a-f/black-box.md)
- [`GAME-0079` — Filling](../games/a-f/filling.md)
- [`GAME-0062` — Hexologic](../games/g-l/hexologic.md)
- [`GAME-0080` — Keen](../games/g-l/keen.md)
- [`GAME-0075` — Light Up](../games/g-l/light-up.md)
- [`GAME-0077` — Map](../games/m-r/map.md)
- [`GAME-0008` — Nonogram](../games/m-r/nonogram.md)
- [`GAME-0071` — Slant](../games/s-z/slant.md)
- [`GAME-0005` — Sudoku](../games/s-z/sudoku.md)
- [`GAME-0072` — Tents](../games/s-z/tents.md)

## ACT-008

- Назва: Безпосередньо пересувати керованого персонажа
- Переглянуто: `2026-08-24`

### Операційне визначення

Гравець сам керує рухом одного персонажа крізь прохідну частину рівня, подаючи команди для ходьби, бігу чи стрибка, а не вибираючи віддалене місце для автоматичного пошуку шляху.

### Включає

Переміщення комірника на одну ортогональну клітинку підлоги в Sokoban без руху ящика; біг і стрибки сіба-іну в HUMANITY крізь випробування до позицій командування; ходіння й стрибки Chell камерою Portal і Tim рівнем Braid; навігація активним Rescue Officer або Oatchi поверхнею Pikmin 4; переміщення Patrick на одну кардинально сусідню локальну клітинку вкладеного простору Patrick’s Parabox; ходіння й стрибки активним тілом у кімнаті The Swapper; ходіння Carto поточним з’єднаним ландшафтом фрагментів мапи; ходіння й стрибки поточною тривимірною геометрією Viewfinder; переміщення чудовиська на одну кардинально сусідню клітинку саду в A Good Snowman Is Hard to Build; просування голови Snakebird на одну кардинально сусідню клітинку з автоматичним слідуванням тіла; просування будь-якого поточного кінця Can of Wormholes на одну кардинально сусідню клітинку; ходіння чудовиськом A Monster’s Expedition суходолом або завершеним мостом із колоди; ходіння й стрибки сновидцем Superliminal кімнатою Induction та її відкритим виходом; ходіння, стрибки й керування падінням періодичною архітектурою Part 1 у Manifold Garden; ходіння між центральною моделлю Maquette, пов’язаними масштабом подвір’ями, мостами для ключа та фіксованим виходом із будинку; ходіння, біг, стрибки й присідання Ві в Найт-Сіті та створених для завдань локаціях Cyberpunk 2077; безпосереднє переміщення й стрибки обраним героєм Marvel Rivals живою ареною; біг і стрибки Hornet сполученими кімнатами Pharloom у Hollow Knight: Silksong; дослідження Spring Meadows і Flying Waters вибраним персонажем у Clair Obscur: Expedition 33; дослідження світу вибраним персонажем загону в Baldur’s Gate 3; біг, стрибки й дослідження поверхні та печер персонажем Terraria.

### Виключає

Зміну ракурсу; переміщення сусіднього об’єкта; телепортацію або пошук шляху, що автоматично виконує кілька кроків.

### Ігри-носії

- [`GAME-0233` — 7 Days to Die](../games/0-9/7-days-to-die.md)
- [`GAME-0044` — A Good Snowman Is Hard to Build](../games/a-f/a-good-snowman-is-hard-to-build.md)
- [`GAME-0054` — A Monster’s Expedition](../games/a-f/a-monsters-expedition.md)
- [`GAME-0228` — A Way Out](../games/a-f/a-way-out.md)
- [`GAME-0223` — Aion Classic](../games/a-f/aion-classic.md)
- [`GAME-0257` — "Alien: Isolation"](../games/a-f/alien-isolation.md)
- [`GAME-0320` — "Animal Crossing: New Horizons"](../games/a-f/animal-crossing-new-horizons.md)
- [`GAME-0097` — Antichamber](../games/a-f/antichamber.md)
- [`GAME-0154` — Apex Legends](../games/a-f/apex-legends.md)
- [`GAME-0143` — ARC Raiders](../games/a-f/arc-raiders.md)
- [`GAME-0312` — ASTRO BOT](../games/a-f/astro-bot.md)
- [`GAME-0148` — Baldur’s Gate 3](../games/a-f/baldurs-gate-3.md)
- [`GAME-0386` — Banjo-Kazooie](../games/a-f/banjo-kazooie.md)
- [`GAME-0255` — "Batman: Arkham Asylum Game of the Year Edition"](../games/a-f/batman-arkham-asylum-game-of-the-year-edition.md)
- [`GAME-0234` — Battlefield 2042](../games/a-f/battlefield-2042.md)
- [`GAME-0149` — Battlefield 6](../games/a-f/battlefield-6.md)
- [`GAME-0243` — Battlefield Hardline](../games/a-f/battlefield-hardline.md)
- [`GAME-0220` — Battlefield V](../games/a-f/battlefield-v.md)
- [`GAME-0318` — Battletoads](../games/a-f/battletoads.md)
- [`GAME-0256` — "BioShock™ Remastered"](../games/a-f/bioshock-remastered.md)
- [`GAME-0189` — "Black Myth: Wukong"](../games/a-f/black-myth-wukong.md)
- [`GAME-0308` — Bloodborne™](../games/a-f/bloodborne.md)
- [`GAME-0173` — Blue Prince](../games/a-f/blue-prince.md)
- [`GAME-0055` — Bonfire Peaks](../games/a-f/bonfire-peaks.md)
- [`GAME-0034` — Braid, Anniversary Edition](../games/a-f/braid.md)
- [`GAME-0198` — Brawlhalla](../games/a-f/brawlhalla.md)
- [`GAME-0222` — "Call of Juarez: Gunslinger"](../games/a-f/call-of-juarez-gunslinger.md)
- [`GAME-0053` — Can of Wormholes](../games/a-f/can-of-wormholes.md)
- [`GAME-0302` — "Captain Toad: Treasure Tracker"](../games/a-f/captain-toad-treasure-tracker.md)
- [`GAME-0040` — Carto](../games/a-f/carto.md)
- [`GAME-0347` — "Castlevania: Symphony of the Night"](../games/a-f/castlevania-symphony-of-the-night.md)
- [`GAME-0346` — Chrono Trigger](../games/a-f/chrono-trigger.md)
- [`GAME-0144` — Clair Obscur: Expedition 33](../games/a-f/clair-obscur-expedition-33.md)
- [`GAME-0108` — Cocoon](../games/a-f/cocoon.md)
- [`GAME-0324` — Contra Force](../games/a-f/contra-force.md)
- [`GAME-0254` — CONTROL Ultimate Edition](../games/a-f/control-ultimate-edition.md)
- [`GAME-0137` — Counter-Strike 2](../games/a-f/counter-strike-2.md)
- [`GAME-0218` — Counter-Strike](../games/a-f/counter-strike.md)
- [`GAME-0326` — Crash Bandicoot](../games/a-f/crash-bandicoot.md)
- [`GAME-0246` — Crysis Remastered](../games/a-f/crysis-remastered.md)
- [`GAME-0277` — Cuphead](../games/a-f/cuphead.md)
- [`GAME-0146` — Cyberpunk 2077](../games/a-f/cyberpunk-2077.md)
- [`GAME-0262` — DARK SOULS™ III](../games/a-f/dark-souls-iii.md)
- [`GAME-0295` — DARK SOULS™: REMASTERED](../games/a-f/dark-souls-remastered.md)
- [`GAME-0281` — Darkest Dungeon](../games/a-f/darkest-dungeon.md)
- [`GAME-0278` — DAVE THE DIVER](../games/a-f/dave-the-diver.md)
- [`GAME-0210` — DayZ](../games/a-f/dayz.md)
- [`GAME-0161` — Dead by Daylight](../games/a-f/dead-by-daylight.md)
- [`GAME-0282` — Dead Cells](../games/a-f/dead-cells.md)
- [`GAME-0368` — Dead Rising](../games/a-f/dead-rising.md)
- [`GAME-0259` — "Dead Space (2023 remake)"](../games/a-f/dead-space-2023.md)
- [`GAME-0310` — "DEATH STRANDING DIRECTOR’S CUT"](../games/a-f/death-stranding-directors-cut.md)
- [`GAME-0266` — Deep Rock Galactic](../games/a-f/deep-rock-galactic.md)
- [`GAME-0200` — Delta Force](../games/a-f/delta-force.md)
- [`GAME-0193` — Destiny 2](../games/a-f/destiny-2.md)
- [`GAME-0252` — "Detroit: Become Human"](../games/a-f/detroit-become-human.md)
- [`GAME-0353` — "Deus Ex: Game of the Year Edition"](../games/a-f/deus-ex-game-of-the-year-edition.md)
- [`GAME-0322` — "Diablo II: Resurrected"](../games/a-f/diablo-ii-resurrected.md)
- [`GAME-0247` — Dishonored (2012)](../games/a-f/dishonored-2012.md)
- [`GAME-0329` — "Donkey Kong Country"](../games/a-f/donkey-kong-country.md)
- [`GAME-0186` — "Don’t Starve Together"](../games/a-f/dont-starve-together.md)
- [`GAME-0352` — DOOM (1993)](../games/a-f/doom-1993.md)
- [`GAME-0245` — DOOM (2016)](../games/a-f/doom-2016.md)
- [`GAME-0286` — DOOM Eternal](../games/a-f/doom-eternal.md)
- [`GAME-0269` — DREDGE](../games/a-f/dredge.md)
- [`GAME-0131` — Dyson Sphere Program](../games/a-f/dyson-sphere-program.md)
- [`GAME-0163` — EA SPORTS FC 26](../games/a-f/ea-sports-fc-26.md)
- [`GAME-0152` — Elden Ring](../games/a-f/elden-ring.md)
- [`GAME-0327` — Fable](../games/a-f/fable.md)
- [`GAME-0231` — Fallout 4](../games/a-f/fallout-4.md)
- [`GAME-0361` — Fallout: New Vegas](../games/a-f/fallout-new-vegas.md)
- [`GAME-0236` — Far Cry 3](../games/a-f/far-cry-3.md)
- [`GAME-0271` — Far Cry 5](../games/a-f/far-cry-5.md)
- [`GAME-0091` — Fez](../games/a-f/fez.md)
- [`GAME-0338` — Final Fantasy VII](../games/a-f/final-fantasy-vii.md)
- [`GAME-0188` — FINAL FANTASY XIV Online](../games/a-f/final-fantasy-xiv-online.md)
- [`GAME-0227` — Fortnite](../games/a-f/fortnite.md)
- [`GAME-0321` — Gears of War](../games/g-l/gears-of-war.md)
- [`GAME-0263` — God of War](../games/g-l/god-of-war.md)
- [`GAME-0381` — GoldenEye 007](../games/g-l/goldeneye-007.md)
- [`GAME-0357` — "Grand Theft Auto: San Andreas"](../games/g-l/grand-theft-auto-san-andreas.md)
- [`GAME-0145` — Grand Theft Auto V](../games/g-l/grand-theft-auto-v.md)
- [`GAME-0314` — Grounded](../games/g-l/grounded.md)
- [`GAME-0251` — Hades](../games/g-l/hades.md)
- [`GAME-0239` — Half-Life (1998)](../games/g-l/half-life-1998.md)
- [`GAME-0212` — Half-Life 2](../games/g-l/half-life-2.md)
- [`GAME-0315` — Halo 3](../games/g-l/halo-3.md)
- [`GAME-0340` — "Halo: Combat Evolved Anniversary"](../games/g-l/halo-combat-evolved-anniversary.md)
- [`GAME-0159` — Helldivers 2](../games/g-l/helldivers-2.md)
- [`GAME-0248` — HITMAN World of Assassination](../games/g-l/hitman-world-of-assassination.md)
- [`GAME-0150` — "Hollow Knight: Silksong"](../games/g-l/hollow-knight-silksong.md)
- [`GAME-0274` — Hollow Knight](../games/g-l/hollow-knight.md)
- [`GAME-0112` — Human: Fall Flat](../games/g-l/human-fall-flat.md)
- [`GAME-0029` — HUMANITY](../games/g-l/humanity.md)
- [`GAME-0098` — Hyperbolica](../games/g-l/hyperbolica.md)
- [`GAME-0099` — HyperRogue](../games/g-l/hyperrogue.md)
- [`GAME-0215` — It Takes Two](../games/g-l/it-takes-two.md)
- [`GAME-0350` — "Jet Set Radio"](../games/g-l/jet-set-radio.md)
- [`GAME-0376` — Katamari Damacy REROLL](../games/g-l/katamari-damacy-reroll.md)
- [`GAME-0240` — "Kingdom Come: Deliverance II"](../games/g-l/kingdom-come-deliverance-ii.md)
- [`GAME-0388` — L.A. Noire](../games/g-l/la-noire.md)
- [`GAME-0192` — Left 4 Dead 2](../games/g-l/left-4-dead-2.md)
- [`GAME-0290` — Lies of P](../games/g-l/lies-of-p.md)
- [`GAME-0219` — Lineage II](../games/g-l/lineage-ii.md)
- [`GAME-0394` — LittleBigPlanet 2](../games/g-l/littlebigplanet-2.md)
- [`GAME-0214` — "Mafia (2002)"](../games/m-r/mafia-2002.md)
- [`GAME-0095` — Manifold Garden](../games/m-r/manifold-garden.md)
- [`GAME-0096` — Maquette](../games/m-r/maquette.md)
- [`GAME-0147` — Marvel Rivals](../games/m-r/marvel-rivals.md)
- [`GAME-0323` — "Marvel’s Spider-Man 2"](../games/m-r/marvels-spider-man-2.md)
- [`GAME-0367` — Mass Effect 2 (Legendary Edition)](../games/m-r/mass-effect-2-legendary-edition.md)
- [`GAME-0238` — "Max Payne (2001)"](../games/m-r/max-payne-2001.md)
- [`GAME-0273` — Max Payne 3](../games/m-r/max-payne-3.md)
- [`GAME-0389` — Mega Man 2](../games/m-r/mega-man-2.md)
- [`GAME-0306` — METAL GEAR SOLID V: THE PHANTOM PAIN](../games/m-r/metal-gear-solid-v-the-phantom-pain.md)
- [`GAME-0339` — Metal Gear Solid](../games/m-r/metal-gear-solid.md)
- [`GAME-0260` — Metro Exodus](../games/m-r/metro-exodus.md)
- [`GAME-0355` — Metroid Prime](../games/m-r/metroid-prime.md)
- [`GAME-0129` — Minecraft](../games/m-r/minecraft.md)
- [`GAME-0297` — 'MONSTER HUNTER RISE'](../games/m-r/monster-hunter-rise.md)
- [`GAME-0151` — Monster Hunter Wilds](../games/m-r/monster-hunter-wilds.md)
- [`GAME-0207` — 'Monster Hunter: World'](../games/m-r/monster-hunter-world.md)
- [`GAME-0393` — Mortal Kombat II](../games/m-r/mortal-kombat-ii.md)
- [`GAME-0194` — "Mount & Blade II: Bannerlord"](../games/m-r/mount-and-blade-ii-bannerlord.md)
- [`GAME-0111` — Myst](../games/m-r/myst.md)
- [`GAME-0202` — "NARAKA: BLADEPOINT"](../games/m-r/naraka-bladepoint.md)
- [`GAME-0241` — NBA 2K26](../games/m-r/nba-2k26.md)
- [`GAME-0341` — "Ninja Gaiden Black"](../games/m-r/ninja-gaiden-black.md)
- [`GAME-0299` — Nioh 2](../games/m-r/nioh-2.md)
- [`GAME-0229` — "No Man’s Sky"](../games/m-r/no-mans-sky.md)
- [`GAME-0296` — Noita](../games/m-r/noita.md)
- [`GAME-0382` — Ōkami HD](../games/m-r/okami-hd.md)
- [`GAME-0224` — Once Human](../games/m-r/once-human.md)
- [`GAME-0117` — OneShot](../games/m-r/oneshot.md)
- [`GAME-0293` — Ori and the Will of the Wisps](../games/m-r/ori-and-the-will-of-the-wisps.md)
- [`GAME-0105` — Outer Wilds](../games/m-r/outer-wilds.md)
- [`GAME-0300` — Overcooked! 2](../games/m-r/overcooked-2.md)
- [`GAME-0181` — Overwatch](../games/m-r/overwatch.md)
- [`GAME-0342` — "PAC-MAN"](../games/m-r/pac-man.md)
- [`GAME-0139` — Palworld](../games/m-r/palworld.md)
- [`GAME-0162` — Path of Exile 2](../games/m-r/path-of-exile-2.md)
- [`GAME-0036` — "Patrick’s Parabox"](../games/m-r/patricks-parabox.md)
- [`GAME-0201` — PAYDAY 2](../games/m-r/payday-2.md)
- [`GAME-0232` — PAYDAY 3](../games/m-r/payday-3.md)
- [`GAME-0203` — "PEAK"](../games/m-r/peak.md)
- [`GAME-0291` — Persona 5 Royal](../games/m-r/persona-5-royal.md)
- [`GAME-0035` — Pikmin 4](../games/m-r/pikmin-4.md)
- [`GAME-0160` — "Pokémon Legends: Z-A"](../games/m-r/pokemon-legends-z-a.md)
- [`GAME-0336` — "Pokémon Red Version"](../games/m-r/pokemon-red-version.md)
- [`GAME-0113` — Portal 2 — Cooperative Campaign](../games/m-r/portal-2-co-op.md)
- [`GAME-0033` — Portal](../games/m-r/portal.md)
- [`GAME-0279` — PowerWash Simulator](../games/m-r/powerwash-simulator.md)
- [`GAME-0258` — "Prey (2017)"](../games/m-r/prey-2017.md)
- [`GAME-0344` — "Prince of Persia: The Sands of Time"](../games/m-r/prince-of-persia-the-sands-of-time.md)
- [`GAME-0142` — Project Zomboid](../games/m-r/project-zomboid.md)
- [`GAME-0358` — Psychonauts](../games/m-r/psychonauts.md)
- [`GAME-0140` — "PUBG: BATTLEGROUNDS"](../games/m-r/pubg-battlegrounds.md)
- [`GAME-0334` — Quake](../games/m-r/quake.md)
- [`GAME-0165` — Red Dead Redemption 2](../games/m-r/red-dead-redemption-2.md)
- [`GAME-0280` — Resident Evil 2 (2019 remake)](../games/m-r/resident-evil-2-2019.md)
- [`GAME-0249` — Resident Evil 4 (2023 remake)](../games/m-r/resident-evil-4-2023.md)
- [`GAME-0348` — "Resident Evil: Director’s Cut"](../games/m-r/resident-evil-directors-cut.md)
- [`GAME-0270` — Risk of Rain 2](../games/m-r/risk-of-rain-2.md)
- [`GAME-0141` — Rust](../games/m-r/rust.md)
- [`GAME-0319` — Sea of Thieves](../games/s-z/sea-of-thieves.md)
- [`GAME-0288` — "Sekiro™: Shadows Die Twice - GOTY Edition"](../games/s-z/sekiro-shadows-die-twice.md)
- [`GAME-0272` — Serious Sam 4](../games/s-z/serious-sam-4.md)
- [`GAME-0237` — "Serious Sam HD: The First Encounter"](../games/s-z/serious-sam-hd-the-first-encounter.md)
- [`GAME-0356` — Shadow of the Colossus](../games/s-z/shadow-of-the-colossus.md)
- [`GAME-0050` — Shogun Showdown](../games/s-z/shogun-showdown.md)
- [`GAME-0303` — Sifu](../games/s-z/sifu.md)
- [`GAME-0330` — Silent Hill 2 (2024 remake)](../games/s-z/silent-hill-2-2024.md)
- [`GAME-0307` — Slime Rancher](../games/s-z/slime-rancher.md)
- [`GAME-0045` — Snakebird](../games/s-z/snakebird.md)
- [`GAME-0006` — Sokoban](../games/s-z/sokoban.md)
- [`GAME-0333` — "Sonic the Hedgehog"](../games/s-z/sonic-the-hedgehog.md)
- [`GAME-0305` — Sons Of The Forest](../games/s-z/sons-of-the-forest.md)
- [`GAME-0360` — "Space Invaders"](../games/s-z/space-invaders.md)
- [`GAME-0157` — Split Fiction](../games/s-z/split-fiction.md)
- [`GAME-0373` — Spore](../games/s-z/spore.md)
- [`GAME-0170` — "S.T.A.L.K.E.R. 2: Heart of Chornobyl"](../games/s-z/stalker-2-heart-of-chornobyl.md)
- [`GAME-0230` — "STAR WARS Battlefront II (2017)"](../games/s-z/star-wars-battlefront-ii-2017.md)
- [`GAME-0213` — "STAR WARS Jedi: Fallen Order"](../games/s-z/star-wars-jedi-fallen-order.md)
- [`GAME-0331` — Starfield](../games/s-z/starfield.md)
- [`GAME-0043` — Stephen’s Sausage Roll](../games/s-z/stephens-sausage-roll.md)
- [`GAME-0172` — Street Fighter 6](../games/s-z/street-fighter-6.md)
- [`GAME-0351` — "Street Fighter II: The World Warrior"](../games/s-z/street-fighter-ii-the-world-warrior.md)
- [`GAME-0178` — Subnautica](../games/s-z/subnautica.md)
- [`GAME-0387` — Super Bomberman](../games/s-z/super-bomberman.md)
- [`GAME-0311` — Super Mario Bros.](../games/s-z/super-mario-bros.md)
- [`GAME-0354` — Super Mario World](../games/s-z/super-mario-world.md)
- [`GAME-0337` — Super Metroid](../games/s-z/super-metroid.md)
- [`GAME-0094` — Superliminal](../games/s-z/superliminal.md)
- [`GAME-0313` — Tank 1990](../games/s-z/tank-1990.md)
- [`GAME-0187` — Team Fortress 2](../games/s-z/team-fortress-2.md)
- [`GAME-0366` — Tekken 3](../games/s-z/tekken-3.md)
- [`GAME-0283` — TEKKEN 8](../games/s-z/tekken-8.md)
- [`GAME-0153` — Terraria](../games/s-z/terraria.md)
- [`GAME-0164` — "The Binding of Isaac: Rebirth"](../games/s-z/the-binding-of-isaac-rebirth.md)
- [`GAME-0362` — "The Elder Scrolls III: Morrowind"](../games/s-z/the-elder-scrolls-iii-morrowind.md)
- [`GAME-0190` — "The Elder Scrolls V: Skyrim Special Edition"](../games/s-z/the-elder-scrolls-v-skyrim-special-edition.md)
- [`GAME-0292` — The Forest](../games/s-z/the-forest.md)
- [`GAME-0261` — The Last of Us Part I](../games/s-z/the-last-of-us-part-i.md)
- [`GAME-0395` — "The Legend of Zelda: Majora’s Mask"](../games/s-z/the-legend-of-zelda-majoras-mask.md)
- [`GAME-0363` — "The Legend of Zelda: Ocarina of Time"](../games/s-z/the-legend-of-zelda-ocarina-of-time.md)
- [`GAME-0325` — The Legend of Zelda](../games/s-z/the-legend-of-zelda.md)
- [`GAME-0285` — "The Long Dark"](../games/s-z/the-long-dark.md)
- [`GAME-0107` — The Pedestrian](../games/s-z/the-pedestrian.md)
- [`GAME-0116` — The Stanley Parable: Ultra Deluxe](../games/s-z/the-stanley-parable-ultra-deluxe.md)
- [`GAME-0038` — The Swapper](../games/s-z/the-swapper.md)
- [`GAME-0090` — The Talos Principle](../games/s-z/the-talos-principle.md)
- [`GAME-0205` — "The Witcher 3: Wild Hunt"](../games/s-z/the-witcher-3-wild-hunt.md)
- [`GAME-0253` — "Titanfall 2"](../games/s-z/titanfall-2.md)
- [`GAME-0174` — Tom Clancy’s Rainbow Six Siege](../games/s-z/tom-clancys-rainbow-six-siege.md)
- [`GAME-0349` — "Tom Clancy’s Splinter Cell"](../games/s-z/tom-clancys-splinter-cell.md)
- [`GAME-0250` — Tomb Raider (2013)](../games/s-z/tomb-raider-2013.md)
- [`GAME-0365` — Tony Hawk’s Pro Skater 1 + 2](../games/s-z/tony-hawks-pro-skater-1-plus-2.md)
- [`GAME-0104` — TUNIC](../games/s-z/tunic.md)
- [`GAME-0391` — "Uncharted 2: Among Thieves"](../games/s-z/uncharted-2-among-thieves.md)
- [`GAME-0268` — Undertale](../games/s-z/undertale.md)
- [`GAME-0294` — V Rising](../games/s-z/v-rising.md)
- [`GAME-0197` — Valheim](../games/s-z/valheim.md)
- [`GAME-0183` — Vampire Survivors](../games/s-z/vampire-survivors.md)
- [`GAME-0041` — Viewfinder](../games/s-z/viewfinder.md)
- [`GAME-0168` — Warframe](../games/s-z/warframe.md)
- [`GAME-0221` — World of Warcraft](../games/s-z/world-of-warcraft.md)
- [`GAME-0379` — Worms Armageddon](../games/s-z/worms-armageddon.md)

## ACT-009

- Назва: Штовхання сусіднього рухомого об’єкта
- Переглянуто: `2026-08-24`

### Операційне визначення

Спрямовуючи керованого агента тілом або прикріпленим інструментом до одного сусіднього рухомого об’єкта, гравець зсуває цей об’єкт на одну логічну позицію від агента; агент або інструмент займає звільнений бік контакту.

### Включає

Штовхання одного ящика Sokoban на одну ортогональну клітинку; одного об’єкта з призначеною властивістю `PUSH` у Baba Is You; одного сусіднього ящика Patrick’s Parabox до допустимого локального або міжмежового місця призначення; однієї ковбаски прикріпленою виделкою в Stephen’s Sausage Roll; однієї снігової кулі A Good Snowman Is Hard to Build до порожньої клітинки або сумісного стосу; одного дерева чи колоди A Monster’s Expedition із сусіднього доступного боку перед залежним від напрямку розв’язанням.

### Виключає

Тягнення об’єкта; незалежний вибір і переміщення об’єкта; автоматичну реакцію на зіткнення.

### Ігри-носії

- [`GAME-0044` — A Good Snowman Is Hard to Build](../games/a-f/a-good-snowman-is-hard-to-build.md)
- [`GAME-0054` — A Monster’s Expedition](../games/a-f/a-monsters-expedition.md)
- [`GAME-0013` — Baba Is You](../games/a-f/baba-is-you.md)
- [`GAME-0036` — "Patrick’s Parabox"](../games/m-r/patricks-parabox.md)
- [`GAME-0006` — Sokoban](../games/s-z/sokoban.md)
- [`GAME-0043` — Stephen’s Sausage Roll](../games/s-z/stephens-sausage-roll.md)

## ACT-010

- Назва: Перенесення доступної карти між зонами
- Переглянуто: `2026-08-24`

### Операційне визначення

Гравець обирає одну доступну на цей момент карту й переносить її до зони призначення, правило розміщення якої приймає цю карту.

### Включає

Перенесення відкритої карти табло FreeCell до іншого каскаду, порожньої вільної комірки, порожнього каскаду або допустимої бази; перенесення карти з вільної комірки до допустимого каскаду чи бази.

### Виключає

Відкриття прихованої карти; роздавання наступної карти; переміщення недоступної карти зсередини стосу; технічну скорочену команду, яка лише згортає кілька окремо допустимих однокарткових перенесень.

### Ігри-носії

- [`GAME-0007` — FreeCell](../games/a-f/freecell.md)

## ACT-011

- Назва: Обмін ортогонально сусідніх елементів поля
- Переглянуто: `2026-08-24`

### Операційне визначення

Гравець безпосередньо міняє місцями два вибрані елементи, що займають ортогонально сусідні адресовані клітинки.

### Включає

Обмін двох сусідніх кольорових елементів для створення збігу в Royal Match.

### Виключає

Переміщення одного елемента в порожню клітинку; обмін несусідніх елементів; автоматичне падіння або перемішування поля.

### Ігри-носії

- [`GAME-0109` — Candy Crush Saga](../games/a-f/candy-crush-saga.md)
- [`GAME-0009` — Royal Match](../games/m-r/royal-match.md)

## ACT-012

- Назва: Активація або поєднання підсилювача на полі
- Переглянуто: `2026-08-24`

### Операційне визначення

Гравець безпосередньо запускає один постійний спеціальний елемент поля або міняє місцями два сумісні спеціальні елементи, щоб запустити поєднаний ефект.

### Включає

Натискання або обмін `Rocket`, `TNT`, `Propeller` чи `Light Ball` у Royal Match, а також обмін двох підсилювачів між собою.

### Виключає

Автоматичне створення підсилювача зі збігу; вибір бустера перед рівнем; область очищення, яку система розв’язує після активації.

### Ігри-носії

- [`GAME-0109` — Candy Crush Saga](../games/a-f/candy-crush-saga.md)
- [`GAME-0009` — Royal Match](../games/m-r/royal-match.md)

## ACT-013

- Назва: Вибір контейнера-джерела й контейнера призначення
- Переглянуто: `2026-08-24`

### Операційне визначення

Гравець безпосередньо обирає один непорожній контейнер-джерело та відмінний від нього контейнер призначення, наказуючи системі спробувати одне перенесення між ними.

### Включає

Вибір двох пробірок Water Sort для спроби переливання з першої до другої.

### Виключає

Вибір кількості для перенесення; переміщення окремо вибраного внутрішнього шару; автоматичне перенесення без команди, що визначає місце призначення.

### Ігри-носії

- [`GAME-0010` — Water Sort](../games/s-z/water-sort.md)

## ACT-014

- Назва: Переміщення вибраної підконтрольної фігури поля
- Переглянуто: `2026-08-24`

### Операційне визначення

Гравець обирає одну фігуру поля, яку зараз контролює, і місце призначення, дозволене правилами руху цієї фігури, безпосередньо змінюючи її позицію та виконуючи передбачене місцем призначення взяття.

### Включає

Звичайні шахові ходи та взяття; рокіровку як визначений складений виняток, ініційований ходом короля; переміщення одного доступного меха у фазі гравця Into the Breach; вибір кілка Peg Solitaire та порожнього отвору за дві ортогональні позиції для одного стрибка; переміщення одного очолюваного командиром загону до допустимого місця на острові Bad North; ковзання однієї вибраної машини чи вантажівки Rush Hour до досяжної позиції на її фіксованій осі.

### Виключає

Переміщення фігури під контролем суперника; автоматичну відповідь суперника; вибір типу фігури для перетворення пішака; напрямлену навігацію постійно керованим агентом лише до сусідньої позиції (`ACT-008`).

### Ігри-носії

- [`GAME-0027` — Bad North: Jotunn Edition](../games/a-f/bad-north.md)
- [`GAME-0011` — Chess](../games/a-f/chess.md)
- [`GAME-0014` — Into the Breach](../games/g-l/into-the-breach.md)
- [`GAME-0019` — Peg Solitaire](../games/m-r/peg-solitaire.md)
- [`GAME-0063` — Rush Hour](../games/m-r/rush-hour.md)
- [`GAME-0048` — Tactical Breach Wizards](../games/s-z/tactical-breach-wizards.md)
- [`GAME-0191` — "Total War: WARHAMMER III"](../games/s-z/total-war-warhammer-iii.md)
- [`GAME-0176` — XCOM 2](../games/s-z/xcom-2.md)

## ACT-015

- Назва: Вибір типу заміни під час перетворення
- Переглянуто: `2026-08-24`

### Операційне визначення

Коли придатний юніт досягає своєї завершальної області, гравець безпосередньо обирає один тип із визначеної множини, щоб замінити цим типом юніт у межах того самого ходу.

### Включає

Вибір ферзя, тури, слона або коня для шахового пішака, що досяг найдальшої горизонталі.

### Виключає

Поліпшення, вибране системою; заміну, обмежену раніше знятими фігурами; саме переміщення до завершальної області.

### Ігри-носії

- [`GAME-0011` — Chess](../games/a-f/chess.md)

## ACT-016

- Назва: Прокладання шляху від фіксованої кінцевої точки
- Переглянуто: `2026-08-24`

### Операційне визначення

Гравець починає в одній фіксованій кінцевій точці й одним складеним жестом безпосередньо прокладає впорядкований маршрут змінної довжини через послідовно суміжні позиції поля до визначеної для неї завершальної точки.

### Включає

Протягування труби Flow Free від будь-якої кольорової точки через клітинки сітки до відповідної точки; прокладання однієї колії Cosmic Express від фіксованого входу до вибраного виходу; прокладання лінії панелі The Witness від початкового кола до кінцевої заглушки; прокладання одного маршруту LYNE від порожнистої кінцевої точки через маркери тієї самої родини до іншої порожнистої кінцевої точки.

### Виключає

Незалежне призначення не пов’язаних між собою клітинок; вибір лише двох кінцевих точок, між якими система сама знаходить маршрут; обертання вже наявних плиток труб.

### Ігри-носії

- [`GAME-0037` — Cosmic Express](../games/a-f/cosmic-express.md)
- [`GAME-0012` — Flow Free](../games/a-f/flow-free.md)
- [`GAME-0061` — LYNE](../games/g-l/lyne.md)
- [`GAME-0039` — The Witness](../games/s-z/the-witness.md)

## ACT-017

- Назва: Напрямлений крок усіх підконтрольних правилам об’єктів
- Переглянуто: `2026-08-24`

### Операційне визначення

Одна напрямлена команда наказує кожному об’єкту, який зараз визначено активним правилом керування, спробувати виконати той самий ортогональний крок на одну позицію.

### Включає

Переміщення всіх об’єктів, іменник яких у Baba Is You зараз має властивість `YOU`.

### Виключає

Переміщення одного постійно визначеного агента; глобальний максимальний зсув; автоматичний рух без команди гравця.

### Ігри-носії

- [`GAME-0013` — Baba Is You](../games/a-f/baba-is-you.md)

## ACT-018

- Назва: Штовхання суцільного ланцюга рухомих об’єктів
- Переглянуто: `2026-08-24`

### Операційне визначення

Наказуючи підконтрольному об’єкту рухатися до сусідньої послідовності штовхуваних об’єктів, гравець намагається зсунути весь суцільний ланцюг на одну логічну позицію в цьому напрямку відповідно до топології місця призначення.

### Включає

Штовхання ряду текстових об’єктів або об’єктів із властивістю `PUSH` у Baba Is You; штовхання вирівняного ряду ящиків у Patrick’s Parabox, зокрема коли найдальший елемент перетинає придатну межу контейнера.

### Виключає

Межу штовхання лише одного об’єкта (`ACT-009`); тягнення ланцюга; безпосередній вибір віддалених об’єктів; автоматичний рух конвеєром.

### Ігри-носії

- [`GAME-0013` — Baba Is You](../games/a-f/baba-is-you.md)
- [`GAME-0036` — "Patrick’s Parabox"](../games/m-r/patricks-parabox.md)

## ACT-019

- Назва: Вибрати здатність і ціль
- Переглянуто: `2026-08-24`

### Операційне визначення

Гравець вибирає доступну здатність керованого персонажа чи підрозділу та вказує ворога, союзника, позицію або область, на яку вона має подіяти.

### Включає

Постріл або ремонт меха в Into the Breach; класову здатність загону в Bad North; вибір Skill і цілі в Clair Obscur: Expedition 33; вибір атаки, закляття чи поштовху та відповідної цілі в Baldur’s Gate 3.

### Виключає

Переміщення того, хто діє; уже розпочату атаку ворога; автоматичні наслідки раніше вибраної здатності.

### Ігри-носії

- [`GAME-0132` — Anno 1800](../games/a-f/anno-1800.md)
- [`GAME-0027` — Bad North: Jotunn Edition](../games/a-f/bad-north.md)
- [`GAME-0148` — Baldur’s Gate 3](../games/a-f/baldurs-gate-3.md)
- [`GAME-0346` — Chrono Trigger](../games/a-f/chrono-trigger.md)
- [`GAME-0144` — Clair Obscur: Expedition 33](../games/a-f/clair-obscur-expedition-33.md)
- [`GAME-0281` — Darkest Dungeon](../games/a-f/darkest-dungeon.md)
- [`GAME-0301` — "Divinity: Original Sin 2 - Definitive Edition"](../games/a-f/divinity-original-sin-2-definitive-edition.md)
- [`GAME-0338` — Final Fantasy VII](../games/a-f/final-fantasy-vii.md)
- [`GAME-0014` — Into the Breach](../games/g-l/into-the-breach.md)
- [`GAME-0291` — Persona 5 Royal](../games/m-r/persona-5-royal.md)
- [`GAME-0160` — "Pokémon Legends: Z-A"](../games/m-r/pokemon-legends-z-a.md)
- [`GAME-0336` — "Pokémon Red Version"](../games/m-r/pokemon-red-version.md)
- [`GAME-0166` — Sid Meier’s Civilization VI](../games/s-z/sid-meiers-civilization-vi.md)
- [`GAME-0048` — Tactical Breach Wizards](../games/s-z/tactical-breach-wizards.md)
- [`GAME-0268` — Undertale](../games/s-z/undertale.md)
- [`GAME-0176` — XCOM 2](../games/s-z/xcom-2.md)

## ACT-020

- Назва: Розміщення першої плитки черги у вибраній позиції поля
- Переглянуто: `2026-08-24`

### Операційне визначення

Гравець обирає одну придатну позицію поля й розміщує там обов’язковий зараз перший елемент видимої черги в наданій орієнтації, за потреби замінюючи визначеного мешканця, якого дозволено замінювати.

### Включає

Розміщення нижньої деталі подавача Pipe Dream у порожній клітинці або підривання незаповненої звичайної труби через накладання на неї тієї самої першої деталі черги.

### Виключає

Вибір іншого елемента черги; обертання елемента; прокладання шляху; призначення довільного символу з області значень.

### Ігри-носії

- [`GAME-0016` — Pipe Mania / Pipe Dream](../games/m-r/pipe-mania.md)

## ACT-021

- Назва: Фіксація вибраної підмножини видимих карт
- Переглянуто: `2026-08-24`

### Операційне визначення

Гравець обирає обмежену непорожню підмножину карт з однієї поточно видимої карткової зони й фіксує її для оцінювання правилами або для скидання та заміни.

### Включає

Розіграш від однієї до п’яти карт Balatro для нарахування рахунку або скидання до п’яти вибраних карт із добором замін; вибір рівно трьох відкритих карт SET для перевірки відношень між ними.

### Виключає

Вибір карти поза допустимою видимою зоною; вибір ідентичностей карт, які буде дібрано на заміну; перенесення однієї відкритої карти між зонами ігрової викладки; призначення значення порожній позиції.

### Ігри-носії

- [`GAME-0017` — Balatro](../games/a-f/balatro.md)
- [`GAME-0064` — SET](../games/s-z/set.md)

## ACT-022

- Назва: Перевпорядкування послідовності постійних ефектів
- Переглянуто: `2026-08-24`

### Операційне визначення

Гравець переставляє постійні елементи з ефектами у впорядкованій зоні, щоб під час наступного автоматичного оцінювання їхні ефекти виконалися в новій послідовності.

### Включає

Переміщення Joker-карт у Balatro так, щоб додавальний ефект `Mult` розв’язався перед пізнішим множильним ефектом `XMult`.

### Виключає

Купівлю чи продаж ефекту; переставлення без механічного наслідку порядку; вибір карт для однієї результативної руки.

### Ігри-носії

- [`GAME-0017` — Balatro](../games/a-f/balatro.md)

## ACT-023

- Назва: Редагування впорядкованої транспортної лінії
- Переглянуто: `2026-08-24`

### Операційне визначення

Гравець створює, подовжує, скорочує, перепрокладає або вилучає постійний іменований маршрут, редагуючи впорядковану послідовність його вузлів обслуговування.

### Включає

Проведення лінії Mini Metro через станції, перетягування її кінця до нової станції, зміна проміжного з’єднання й повернення вилученої лінії до запасу для повторного використання; прокладання й редагування лінії громадського транспорту Cities: Skylines через її впорядковані зупинки.

### Виключає

Одноразове прокладання шляху від фіксованої точки; розміщення незмінних перших плиток черги; безпосередню команду наступної зупинки транспортного засобу.

### Ігри-носії

- [`GAME-0121` — "Cities: Skylines"](../games/a-f/cities-skylines.md)
- [`GAME-0018` — Mini Metro](../games/m-r/mini-metro.md)
- [`GAME-0134` — "Workers & Resources: Soviet Republic"](../games/s-z/workers-resources-soviet-republic.md)

## ACT-024

- Назва: Перепризначення транспортної місткості
- Переглянуто: `2026-08-24`

### Операційне визначення

Гравець призначає або переміщує багаторазовий транспортний засіб чи модуль збільшення місткості між придатними постійними маршрутами обслуговування.

### Включає

Розміщення локомотива Mini Metro на лінії, перенесення його на іншу лінію та приєднання або перепризначення вагона.

### Виключає

Скерування транспортного засобу вздовж маршруту; створення нового запасу; редагування самої впорядкованої послідовності станцій.

### Ігри-носії

- [`GAME-0018` — Mini Metro](../games/m-r/mini-metro.md)

## ACT-025

- Назва: Вибір періодичного поліпшення мережі
- Переглянуто: `2026-08-24`

### Операційне визначення

У запланований момент поступу гравець обирає одну із запропонованих інфраструктурних нагород або нагород місткості, щоб додати її до обмеженого запасу.

### Включає

Вибір нової лінії, вагона, тунелю чи іншого доступного на мапі щотижневого поліпшення Mini Metro поряд з автоматично наданим локомотивом; вибір одного із щотижневих поліпшень дорожньої мережі, запропонованих у Mini Motorways.

### Виключає

Купівлю довільних предметів будь-коли; призначення вибраного ресурсу маршруту; створення самих запропонованих варіантів.

### Ігри-носії

- [`GAME-0018` — Mini Metro](../games/m-r/mini-metro.md)
- [`GAME-0051` — Mini Motorways](../games/m-r/mini-motorways.md)

## ACT-026

- Назва: Орієнтація та розміщення обов’язкової першої плитки запасу
- Переглянуто: `2026-08-24`

### Операційне визначення

Гравець вибирає придатну порожню позицію й дозволену орієнтацію, а потім закріплює в цій позиції обов’язкову зараз першу плитку з наданої послідовності.

### Включає

Обертання поточної шестикутної плитки Dorfromantik і розміщення її поруч із наявним ландшафтом.

### Виключає

Вибір пізнішої наданої плитки; розміщення першої плитки черги з фіксованою орієнтацією (`ACT-020`); прокладання маршруту; обертання постійного зв’язаного шару.

### Ігри-носії

- [`GAME-0369` — Carcassonne](../games/a-f/carcassonne.md)
- [`GAME-0020` — Dorfromantik](../games/a-f/dorfromantik.md)

## ACT-027

- Назва: Перерізання вибраного опорного зв’язку свайпом
- Переглянуто: `2026-08-24`

### Операційне визначення

Гравець проводить короткий жест через один або кілька доступних зараз для розрізання зв’язків і наказує перерізати кожен перетнутий зв’язок у цей момент.

### Включає

Свайп через одну або кілька мотузок, що підтримують цукерку в Cut the Rope.

### Виключає

Перетягування підтримуваного тіла; вибір його траєкторії після звільнення; автоматичний розрив зв’язку під навантаженням; прокладання постійного маршруту.

### Ігри-носії

- [`GAME-0021` — Cut the Rope](../games/a-f/cut-the-rope.md)

## ACT-028

- Назва: Налаштування просторової схеми машини
- Переглянуто: `2026-08-24`

### Операційне визначення

Під час редагованої фази проєктування гравець розміщує, вилучає й орієнтує постійні компоненти машини, взаємна геометрія яких визначає, чого може досягти, куди провести або що перетворити пізніший запуск.

### Включає

Розташування маніпуляторів, рейок, гліфів і рухомих портів реагентів або продуктів Opus Magnum на робочому полі трансмутаційної машини; розміщення й орієнтацію конвеєрних та опорних вокселів Infinifactory для пізнішого запуску фабрики; розміщення й орієнтацію скінченних відрізків рейок і стрілок до запуску вагонів Railbound.

### Виключає

Розміщення витратної ігрової плитки; переміщення матеріалу під час роботи машини; редагування команд, які керують установленим механізмом.

### Ігри-носії

- [`GAME-0042` — Infinifactory](../games/g-l/infinifactory.md)
- [`GAME-0267` — Kerbal Space Program](../games/g-l/kerbal-space-program.md)
- [`GAME-0022` — Opus Magnum](../games/m-r/opus-magnum.md)
- [`GAME-0056` — Railbound](../games/m-r/railbound.md)

## ACT-029

- Назва: Редагування символьної стрічки команд механізму
- Переглянуто: `2026-08-24`

### Операційне визначення

Гравець призначає, вилучає або переміщує символи команд в адресованих позиціях циклу на рядку виконання одного постійного механізму.

### Включає

Програмування кожного маніпулятора Opus Magnum позиціями grab, drop, rotate, pivot, extend, retract, track-move, repeat, reset або wait.

### Виключає

Видання однієї команди безпосередньо фігурі, яка зараз рухається; зміну геометрії компонентів; переставлення пасивних ефектів, що розв’язуються після пізнішого оцінювання руки.

### Ігри-носії

- [`GAME-0022` — Opus Magnum](../games/m-r/opus-magnum.md)

## ACT-030

- Назва: Навігація та фокус у статичній сцені доказів
- Переглянуто: `2026-08-24`

### Операційне визначення

Гравець спрямовує точку спостереження або фокус вказівника крізь обмежену незмінну сцену й вибирає людей або деталі для ближчого огляду, не змінюючи представлену подію.

### Включає

Пересування й наближення всередині застиглого спогаду про смерть Return of the Obra Dinn для огляду облич, об’єктів, поз і ліній видимості; вибір людей, речей, документів або деталей мапи у фіксованій сцені The Case of the Golden Idol, щоб відкрити накладені панелі доказів.

### Виключає

Керування рухом ігрового агента, позиція якого змінює стан головоломки; маніпуляцію об’єктами доказів; вибір сцени, до якої слід увійти.

### Ігри-носії

- [`GAME-0023` — Return of the Obra Dinn](../games/m-r/return-of-the-obra-dinn.md)
- [`GAME-0046` — The Case of the Golden Idol](../games/s-z/the-case-of-the-golden-idol.md)

## ACT-031

- Назва: Активація пов’язаного з тілом спогаду-доказу
- Переглянуто: `2026-08-24`

### Операційне визначення

Гравець вибирає придатний знайдений труп або індексований запис смерті й дає команду ввійти до його фіксованої реконструкції доказів.

### Включає

Використання Memento Mortem біля трупа в Return of the Obra Dinn і повторне відвідування вже індексованого спогаду про смерть.

### Виключає

Розкриття невідомого випадкового результату; безпосереднє призначення особи загиблого; пересування всередині отриманої сцени.

### Ігри-носії

- [`GAME-0023` — Return of the Obra Dinn](../games/m-r/return-of-the-obra-dinn.md)

## ACT-032

- Назва: Призначення структурованої гіпотези особи та долі
- Переглянуто: `2026-08-24`

### Операційне визначення

Гравець редагує попереднє досьє суб’єкта, вибираючи можливу особу та структурований вираз долі, включно з відповідальною стороною або місцем, коли вибрана доля цього вимагає.

### Включає

Заповнення речення в книзі Obra Dinn однією особою з маніфесту, причиною смерті та вбивцею, істотою або місцем порятунку.

### Виключає

Запис нотаток у довільній формі; розкриття готового прихованого значення; отримання підтвердження правильності гіпотези.

### Ігри-носії

- [`GAME-0023` — Return of the Obra Dinn](../games/m-r/return-of-the-obra-dinn.md)

## ACT-033

- Назва: Переставлення цілої панелі між фіксованими слотами
- Переглянуто: `2026-08-24`

### Операційне визначення

Гравець перетягує одну цілу обрамлену сцену з її поточного верхньорівневого слота до іншого придатного слота, не змінюючи поточного внутрішнього ракурсу цієї панелі.

### Включає

Переміщення ілюстрованої панелі Gorogoa між чотирма позиціями ігрового поля два на два, щоб поставити її поруч з іншою сценою або поверх неї.

### Виключає

Наближення всередині панелі; від’єднання її переднього шару; розміщення наданої витратної плитки.

### Ігри-носії

- [`GAME-0024` — Gorogoa](../games/g-l/gorogoa.md)

## ACT-034

- Назва: Перехід між ракурсами ілюстрованої панелі
- Переглянуто: `2026-08-24`

### Операційне визначення

Гравець вибирає видимий фокус, засіб повернення або напрямковий елемент взаємодії, щоб наблизити чи панорамувати одну панель до пов’язаного ілюстрованого ракурсу, лишаючи її верхньорівневий слот незмінним.

### Включає

Наближення зображення Gorogoa, віддалення назад або панорамування до суміжної кімнати чи сцени в межах тієї самої панелі.

### Виключає

Переміщення всієї панелі між слотами; безпосередню маніпуляцію об’єктом, зображеним у сцені; рух камери крізь одну незмінну тривимірну сцену доказів.

### Ігри-носії

- [`GAME-0024` — Gorogoa](../games/g-l/gorogoa.md)

## ACT-035

- Назва: Від’єднання й перенесення шару ілюстрованої панелі
- Переглянуто: `2026-08-24`

### Операційне визначення

Коли панель відкриває відокремлюваний обрамлений шар, гравець піднімає цей шар із підкладки й переміщує до іншого слота або на іншу панель, тоді як обидва ілюстровані шари зберігаються.

### Включає

Зняття вікна, дверного отвору, рамки або переднього накладеного шару Gorogoa, щоб відкрити сцену під ним, і накладання від’єднаного шару в іншому місці.

### Виключає

Переміщення неподільної цілої панелі; стирання шару; вибір вкладеного ракурсу без зміни належності шару.

### Ігри-носії

- [`GAME-0024` — Gorogoa](../games/g-l/gorogoa.md)

## ACT-036

- Назва: Призначити вибрану роль автономному персонажу
- Переглянуто: `2026-08-24`

### Операційне визначення

Гравець вибирає доступну поведінкову роль і закріплює її за наявним автономним персонажем, не задаючи безпосередньо його подальший шлях і не керуючи безперервно виконанням ролі.

### Включає

Призначення однієї з восьми класичних навичок Lemmings вибраному lemming.

### Виключає

Вибір здібності безпосередньо керованого тактичного бійця й наведення її на окрему ділянку поля; покрокове керування рухом персонажа; автоматичну зміну стану без призначення гравцем.

### Ігри-носії

- [`GAME-0124` — Against the Storm](../games/a-f/against-the-storm.md)
- [`GAME-0324` — Contra Force](../games/a-f/contra-force.md)
- [`GAME-0130` — Frostpunk](../games/a-f/frostpunk.md)
- [`GAME-0025` — Lemmings](../games/g-l/lemmings.md)
- [`GAME-0305` — Sons Of The Forest](../games/s-z/sons-of-the-forest.md)

## ACT-037

- Назва: Регулювання швидкості автоматичного випуску популяції
- Переглянуто: `2026-08-24`

### Операційне визначення

Під час спроби гравець постійно підвищує або знижує частоту, з якою скінченна популяція, що очікує, автоматично виходить на активне ігрове поле, не змінюючи швидкості вже активних агентів.

### Включає

Використання кнопок мінус і плюс, щоб змінити release rate люка в Lemmings.

### Виключає

Тимчасове прискорення всієї активної симуляції; ручне породження одного вибраного юніта; зміну налаштування складності поза грою.

### Ігри-носії

- [`GAME-0025` — Lemmings](../games/g-l/lemmings.md)

## ACT-038

- Назва: Приєднання вибраного живого вузла до силової конструкції
- Переглянуто: `2026-08-24`

### Операційне визначення

Поки конструкція, рух якої визначають сили, лишається активною, гравець вибирає одного вільного або наразі від’єднуваного матеріального агента, перетягує його до позиції в безперервному просторі біля придатних структурних вузлів і відпускає, запитуючи приєднання.

### Включає

Захоплення вільної або придатної до повторного використання Goo Ball і розміщення її біля конструкції World of Goo.

### Виключає

Налаштування статичних відбитків машини до окремого запуску; призначення поведінкової ролі автономному агенту; розміщення дискретної плитки з обов’язкової черги.

### Ігри-носії

- [`GAME-0026` — World of Goo](../games/s-z/world-of-goo.md)

## ACT-039

- Назва: Розміщення вибраної карти світу з руки
- Переглянуто: `2026-08-24`

### Операційне визначення

Гравець вибирає одну карту світу, яку зараз тримає, і закріплює її в позиції мапи, дозволеній просторовою категорією цієї карти, створюючи або замінюючи постійну плитку світу, що впливає на наступні стани симуляції.

### Включає

Розміщення дорожньої, придорожньої або ландшафтної карти Loop Hero, щоб змінити мапу поточної експедиції.

### Виключає

Розігрування обов’язкового першого елемента черги; розігрування карти лише для негайного підрахунку очок; налаштування цілого світу до окремого запуску.

### Ігри-носії

- [`GAME-0028` — Loop Hero](../games/g-l/loop-hero.md)

## ACT-040

- Назва: Спорядити персонажа здобутим предметом
- Переглянуто: `2026-08-24`

### Операційне визначення

Гравець вибирає здобуту сумісну зброю, броню чи інший предмет спорядження, замінює ним поточний предмет і відповідно змінює характеристики персонажа.

### Включає

Спорядження щойно отриманої зброї або броні в Loop Hero; заміну зброї персонажа в Clair Obscur: Expedition 33; зміну зброї, броні й аксесуарів у Baldur’s Gate 3; спорядження зброї, броні та аксесуарів у Terraria.

### Виключає

Вибір класу до забігу; автоматичний приріст характеристики; переміщення карти між зонами розкладки.

### Ігри-носії

- [`GAME-0148` — Baldur’s Gate 3](../games/a-f/baldurs-gate-3.md)
- [`GAME-0144` — Clair Obscur: Expedition 33](../games/a-f/clair-obscur-expedition-33.md)
- [`GAME-0028` — Loop Hero](../games/g-l/loop-hero.md)
- [`GAME-0153` — Terraria](../games/s-z/terraria.md)

## ACT-041

- Назва: Добровільне завершення експедиції відступом
- Переглянуто: `2026-08-24`

### Операційне визначення

Гравець навмисно завершує активну експедицію й переносить до постійного сховища дозволену в поточному стані частку накопичених у ній ресурсів.

### Включає

Вихід з експедиції Loop Hero під час проходження багаття або прийняття меншої збереженої частки за відступ посеред кола.

### Виключає

Вимушену поразку; призупинення без завершення спроби; переміщення загону до евакуаційного носія, поки бій триває.

### Ігри-носії

- [`GAME-0028` — Loop Hero](../games/g-l/loop-hero.md)

## ACT-042

- Назва: Розміщення постійної команди проходження
- Переглянуто: `2026-08-24`

### Операційне визначення

Гравець записує орієнтовану поведінкову інструкцію у придатну позицію світу, де вона зберігається й впливає на автономних агентів, які пізніше входять у цю позицію, доки інструкцію не відредагують, не перемістять разом з опорою або не приберуть.

### Включає

Розміщення команд HUMANITY Turn або Jump на сітці сцени.

### Виключає

Безпосереднє призначення ролі одному вибраному агенту; розміщення карти, плитка якої пізніше породжує зустрічі; креслення сегмента маршруту.

### Ігри-носії

- [`GAME-0029` — HUMANITY](../games/g-l/humanity.md)

## ACT-043

- Назва: Переміщення й орієнтація активного маршрутного пристрою
- Переглянуто: `2026-08-24`

### Операційне визначення

Під час активної симуляції гравець вибирає один багаторазовий фізичний маршрутний об’єкт, переміщує його до допустимої позиції опори й задає орієнтацію, щоб пізніше автономні агенти фізично контактували з ним.

### Включає

Переміщення й обертання призматичного блока Tin Hearts або наведення барабана-батута в межах поточного рівня.

### Виключає

Розміщення символьного маркера інструкції; приєднання активного вузла до силової конструкції; налаштування машини лише до окремого запуску.

### Ігри-носії

- [`GAME-0030` — Tin Hearts](../games/s-z/tin-hearts.md)

## ACT-044

- Назва: Перемотування недавньої історії симуляції
- Переглянуто: `2026-08-24`

### Операційне визначення

Гравець безперервно або покроково відновлює збережені попередні стани активної симуляції, після чого може зупинитися в ранішому моменті й продовжити, здійснивши інше втручання.

### Включає

Перемотування солдатиків і маршрутних об’єктів Tin Hearts до моменту перед смертельним падінням, переміщення пристрою й відновлення безпечнішого перебігу; прокручування Timelie до моменту перед захопленням, перегляд команди персонажа й пошук нового майбутнього; перемотування Tim і звичайних сутностей Braid перед іншим локальним рухом; вибір ранішої автоматичної контрольної точки Pikmin 4 і розігрування замінної послідовності команд; прокручування Viewfinder до моменту перед падінням або розміщенням зображення й фіксація іншого просторового продовження.

### Виключає

Перезапуск усієї спроби з початкового стану; скасування лише останнього дискретного редагування; зворотне відтворення косметичної анімації без стану гри.

### Ігри-носії

- [`GAME-0034` — Braid, Anniversary Edition](../games/a-f/braid.md)
- [`GAME-0276` — Forza Horizon 5](../games/a-f/forza-horizon-5.md)
- [`GAME-0171` — Forza Horizon 6](../games/a-f/forza-horizon-6.md)
- [`GAME-0035` — Pikmin 4](../games/m-r/pikmin-4.md)
- [`GAME-0344` — "Prince of Persia: The Sands of Time"](../games/m-r/prince-of-persia-the-sands-of-time.md)
- [`GAME-0031` — Timelie](../games/s-z/timelie.md)
- [`GAME-0030` — Tin Hearts](../games/s-z/tin-hearts.md)
- [`GAME-0041` — Viewfinder](../games/s-z/viewfinder.md)

## ACT-045

- Назва: Редагування команди агента з часовою позначкою
- Переглянуто: `2026-08-24`

### Операційне визначення

У вибраний момент симуляції гравець призначає, замінює або очищає місце призначення чи контекстну взаємодію одного постійного актора, а команда лишається в часовому плані, доки її не переглянуть або не буде розв’язано.

### Включає

Вибір дівчини або кота Timelie у поточний момент курсора й планування місця призначення, клавіатури, вентиляційного проходу, нявкання чи пов’язаної взаємодії.

### Виключає

Локальне покрокове пересування аватара; запис багаторазової інструкції в клітинку світу; редагування циклічних символів механізму машини.

### Ігри-носії

- [`GAME-0031` — Timelie](../games/s-z/timelie.md)

## ACT-046

- Назва: Редагування просторового маршруту контролера й поля інструкцій
- Переглянуто: `2026-08-24`

### Операційне визначення

На фіксованій сітці машини гравець креслить напрямлений маршрут одного контролера й призначає клітинкам маршруту символи команд, специфічні для кольору або контролера, через що просторові адреси визначають порядок виконання.

### Включає

Створення маршрутів червоного й синього waldo у SpaceChem і розміщення їхніх інструкцій input, grab, rotate, bond, sync, drop та output.

### Виключає

Редагування команд в окремих адресованих часових стовпцях; розміщення фізичних компонентів машини; планування команди розташованому у світі актору на довільний момент симуляції.

### Ігри-носії

- [`GAME-0032` — SpaceChem](../games/s-z/spacechem.md)

## ACT-047

- Назва: Розміщення замінної кінцевої точки парного порталу
- Переглянуто: `2026-08-24`

### Операційне визначення

Гравець цілиться у придатну поверхню світу й створює на ній кінцеву точку певного кольору або каналу постійної просторової пари порталів, замінюючи попередню кінцеву точку того самого каналу.

### Включає

Постріл синього або помаранчевого порталу Portal на допустиму пласку поверхню камери після отримання повністю зарядженого ручного портального пристрою.

### Виключає

Прокладання кожної проміжної позиції маршруту; редагування впорядкованої транспортної лінії; переміщення твердого маршрутизувального пристрою, з яким агенти згодом стикаються.

### Ігри-носії

- [`GAME-0113` — Portal 2 — Cooperative Campaign](../games/m-r/portal-2-co-op.md)
- [`GAME-0033` — Portal](../games/m-r/portal.md)

## ACT-048

- Назва: Підняття й відпускання переносного твердого об’єкта
- Переглянуто: `2026-08-24`

### Операційне визначення

Гравець безпосередньо підхоплює один досяжний вільний твердий об’єкт, утримує його на керованій відстані під час пересування, а потім відпускає, кладе або кидає назад в активний стан світу.

### Включає

Піднімання, перенесення й опускання Weighted Storage Cube у Portal; хапання, перенесення й відпускання ящика з речами в Bonfire Peaks; узяття, розташування за лінією видимості й опускання шахової фігури Induction у Superliminal; піднімання, перенесення й розміщення придатного кольорового куба в Manifold Garden; піднімання, перенесення й розміщення поточного доступного для взаємодії представлення постійного золотого ключа Maquette.

### Виключає

Штовхання суміжного об’єкта на одну позицію дошки; безпосереднє переміщення фігури дошки до допустимого місця призначення; прикріплення вузла до конструкції.

### Ігри-носії

- [`GAME-0318` — Battletoads](../games/a-f/battletoads.md)
- [`GAME-0055` — Bonfire Peaks](../games/a-f/bonfire-peaks.md)
- [`GAME-0108` — Cocoon](../games/a-f/cocoon.md)
- [`GAME-0254` — CONTROL Ultimate Edition](../games/a-f/control-ultimate-edition.md)
- [`GAME-0301` — "Divinity: Original Sin 2 - Definitive Edition"](../games/a-f/divinity-original-sin-2-definitive-edition.md)
- [`GAME-0329` — "Donkey Kong Country"](../games/a-f/donkey-kong-country.md)
- [`GAME-0212` — Half-Life 2](../games/g-l/half-life-2.md)
- [`GAME-0112` — Human: Fall Flat](../games/g-l/human-fall-flat.md)
- [`GAME-0240` — "Kingdom Come: Deliverance II"](../games/g-l/kingdom-come-deliverance-ii.md)
- [`GAME-0095` — Manifold Garden](../games/m-r/manifold-garden.md)
- [`GAME-0096` — Maquette](../games/m-r/maquette.md)
- [`GAME-0323` — "Marvel’s Spider-Man 2"](../games/m-r/marvels-spider-man-2.md)
- [`GAME-0300` — Overcooked! 2](../games/m-r/overcooked-2.md)
- [`GAME-0203` — "PEAK"](../games/m-r/peak.md)
- [`GAME-0113` — Portal 2 — Cooperative Campaign](../games/m-r/portal-2-co-op.md)
- [`GAME-0033` — Portal](../games/m-r/portal.md)
- [`GAME-0279` — PowerWash Simulator](../games/m-r/powerwash-simulator.md)
- [`GAME-0319` — Sea of Thieves](../games/s-z/sea-of-thieves.md)
- [`GAME-0354` — Super Mario World](../games/s-z/super-mario-world.md)
- [`GAME-0094` — Superliminal](../games/s-z/superliminal.md)
- [`GAME-0261` — The Last of Us Part I](../games/s-z/the-last-of-us-part-i.md)
- [`GAME-0115` — Unpacking](../games/s-z/unpacking.md)

## ACT-049

- Назва: Перемикання досяжного перемикача у світі
- Переглянуто: `2026-08-24`

### Операційне визначення

Гравець змушує керованого на місці аватара активувати досяжний постійний перемикач, змінюючи заданий стан або напрямок руху пов’язаного механізму у світі.

### Включає

Використання важеля Braid, щоб запустити або розвернути пов’язану платформу; натискання досяжного синього перемикача Manifold Garden після періодичного переходу через прогалину, щоб відкрити пов’язані двері; установлення кожного досяжного вентиля в першій водній інструкції Chants of Sennaar у заданий відкритий або закритий стан.

### Виключає

Утримування натискної плити зайнятою; редагування віддаленої взаємодії з часовою позначкою; розміщення багаторазового маркера інструкції.

### Ігри-носії

- [`GAME-0034` — Braid, Anniversary Edition](../games/a-f/braid.md)
- [`GAME-0302` — "Captain Toad: Treasure Tracker"](../games/a-f/captain-toad-treasure-tracker.md)
- [`GAME-0101` — Chants of Sennaar](../games/a-f/chants-of-sennaar.md)
- [`GAME-0215` — It Takes Two](../games/g-l/it-takes-two.md)
- [`GAME-0095` — Manifold Garden](../games/m-r/manifold-garden.md)
- [`GAME-0334` — Quake](../games/m-r/quake.md)
- [`GAME-0157` — Split Fiction](../games/s-z/split-fiction.md)

## ACT-050

- Назва: Призначення вибраного послідовника контекстному завданню цілі
- Переглянуто: `2026-08-24`

### Операційне визначення

Гравець вибирає тип послідовників і спрямовує одного чи кількох доступних послідовників на ціль у світі, внаслідок чого клас цієї цілі визначає автономне завдання, яке вони розпочинають.

### Включає

Кидання Pikmin на скарб, потерпілого, ворога, перешкоду або ціль будівництва в Pikmin 4.

### Виключає

Вибір абстрактної поведінкової ролі до вибору її виконавця; безпосереднє переміщення загону до місця призначення; піднімання й утримування цільового об’єкта поруч з аватаром.

### Ігри-носії

- [`GAME-0266` — Deep Rock Galactic](../games/a-f/deep-rock-galactic.md)
- [`GAME-0035` — Pikmin 4](../games/m-r/pikmin-4.md)

## ACT-051

- Назва: Відкликання близьких послідовників із автономних завдань
- Переглянуто: `2026-08-24`

### Операційне визначення

Гравець подає просторово обмежену команду відкликання, яка припиняє або перериває поточний стан бездіяльності чи автономного завдання придатних близьких послідовників і повертає їх до загону активного лідера.

### Включає

Свисток, яким у Pikmin 4 збирають Pikmin назад до Rescue Officer або Oatchi.

### Виключає

Глобальний вибір кожного юніта незалежно від відстані; перемотування історії завдань; зміну постійної інструкції у світі.

### Ігри-носії

- [`GAME-0035` — Pikmin 4](../games/m-r/pikmin-4.md)

## ACT-052

- Назва: Передавання прямого керування між постійними тілами
- Переглянуто: `2026-08-24`

### Операційне визначення

Коли в одному стані світу активні кілька придатних постійних тіл, гравець передає унікальний осередок прямої навігації або командування з поточного тіла іншому, залишаючи попереднє у світі за оголошеними правилами без осередку.

### Включає

Перемикання між Rescue Officer і Oatchi після розділення груп Pikmin; перенесення свідомості поточного тіла The Swapper у видимого наявного клона.

### Виключає

Вибір актора лише для планування цілі; створення нового тіла без передачі керування; телепортацію одного незмінного тіла; змагальні почергові ходи.

### Ігри-носії

- [`GAME-0329` — "Donkey Kong Country"](../games/a-f/donkey-kong-country.md)
- [`GAME-0163` — EA SPORTS FC 26](../games/a-f/ea-sports-fc-26.md)
- [`GAME-0241` — NBA 2K26](../games/m-r/nba-2k26.md)
- [`GAME-0300` — Overcooked! 2](../games/m-r/overcooked-2.md)
- [`GAME-0035` — Pikmin 4](../games/m-r/pikmin-4.md)
- [`GAME-0038` — The Swapper](../games/s-z/the-swapper.md)

## ACT-054

- Назва: Створити тіло в прицільній досяжній позиції
- Переглянуто: `2026-08-24`

### Операційне визначення

Гравець наводиться на одну наразі допустиму позицію ігрового світу й наказує створити там нове кероване тіло, не переміщуючи наявне тіло вздовж проміжного шляху.

### Включає

Створення клона в The Swapper у безперешкодній допустимій точці в межах дальності пристрою.

### Виключає

Виклик автономної одиниці з резерву; розміщення інертного об’єкта; телепортація поточного тіла; автоматичне створення тіла за таймером.

### Ігри-носії

- [`GAME-0038` — The Swapper](../games/s-z/the-swapper.md)

## ACT-056

- Назва: Перемістити й повернути постійний фрагмент мапи
- Переглянуто: `2026-08-24`

### Операційне визначення

У режимі редагування мапи гравець вибирає один уже здобутий постійний фрагмент ігрового світу, переносить його на нову позицію мапи й може змінити його орієнтацію перед фіксацією нової схеми сусідства.

### Включає

Підняття, переміщення й поворот на чверть оберту квадратного фрагмента мапи Carto, зокрема фрагмента, на якому наразі перебуває аватар.

### Виключає

Витрачання обов’язкового першого елемента з поданої черги плиток; переміщення цілісної ілюстрації лише між фіксованими комірками інтерфейсу; обертання одного зв’язаного шару постійного механічного об’єкта; прокладання маршруту.

### Ігри-носії

- [`GAME-0040` — Carto](../games/a-f/carto.md)

## ACT-057

- Назва: Розмістити й зафіксувати утримуване перспективне зображення
- Переглянуто: `2026-08-24`

### Операційне визначення

Утримуючи одне доступне двовимірне вихідне зображення, гравець розміщує його площину в поточному тривимірному вигляді, вибирає орієнтацію й фіксує цю спроєктовану позу як запит на зміну ігрового світу.

### Включає

Підняття наданої фотографії у Viewfinder, утримання її перед сценою, переміщення або обертання в перспективі та відбиття в обраному місці.

### Виключає

Створення вихідного зображення; перестановка постійного фрагмента мапи; переміщення цілісної панелі між фіксованими комірками інтерфейсу; розміщення одного кінця зв’язаної пари апертур; перенесення й скидання жорсткого об’єкта ігрового світу.

### Ігри-носії

- [`GAME-0041` — Viewfinder](../games/s-z/viewfinder.md)

## ACT-058

- Назва: Повернути агента з проведенням прикріпленого до тіла інструмента
- Переглянуто: `2026-08-24`

### Операційне визначення

Гравець наказує постійному агенту повернутися на місці, тоді як прикріплений до його тіла інструмент проходить від однієї сусідньої орієнтованої клітинки до іншої й може торкнутися об’єкта в охопленій під час повороту області.

### Включає

Поворот персонажа Stephen’s Sausage Roll на чверть оберту, щоб закріплена виделка змінила напрямок і могла зрушити ковбасу боковим контактом.

### Виключає

Обертання віддалено вибраного об’єкта безпосередньо; зміна ракурсу; обертання активної фігури, що падає; поворот без прикріпленої займаної області, важливої для рішень.

### Ігри-носії

- [`GAME-0043` — Stephen’s Sausage Roll](../games/s-z/stephens-sausage-roll.md)

## ACT-059

- Назва: Видобути виділений термін із деталі доказу
- Переглянуто: `2026-08-24`

### Операційне визначення

Гравець вибирає одне явно допустиме слово або фразу у відкритій деталі доказу й копіює цей точний термін до постійного локального для справи словника гіпотез.

### Включає

Натискання виділених імен і назв місць у документах та на мапі прологу The Case of the Golden Idol, щоб вони потрапили до банку слів.

### Виключає

Лише читання невиділеного доказу; відкриття прихованого істинного значення; призначення видобутого терміна полю відповіді.

### Ігри-носії

- [`GAME-0046` — The Case of the Golden Idol](../games/s-z/the-case-of-the-golden-idol.md)

## ACT-060

- Назва: Призначити елемент фрази структурованому пропуску відповіді
- Переглянуто: `2026-08-24`

### Операційне визначення

Гравець вибирає один доступний елемент фрази й розміщує його в типізованому пропуску структурованого твердження, маючи змогу вилучити або замінити його до прийняття відповіді.

### Включає

Перетягування зібраних термінів The Case of the Golden Idol у пропуски особи, місця та сувою події на екрані Thinking у пролозі.

### Виключає

Введення необмеженого довільного тексту; видобування фрази з доказу; призначення повного досьє особи та її долі одному суб’єкту реєстру.

### Ігри-носії

- [`GAME-0046` — The Case of the Golden Idol](../games/s-z/the-case-of-the-golden-idol.md)

## ACT-061

- Назва: Розіграти просторову карту дії з руки
- Переглянуто: `2026-08-23`

### Операційне визначення

Гравець вибирає одну карту дії, яку наразі тримає в руці, та допустимий просторовий параметр цілі, витрачаючи цю карту для застосування оголошеного переходу переміщення, атаки, захисту або зміни позиції.

### Включає

Розігрування у Fights in Tight Spaces карти руху на допустиму клітинку або карти атаки / штовхання на допустимого ворога чи суміжну ціль; розігрування карти руху Golf Peaks з одним кардинальним напрямком як просторовою ціллю.

### Виключає

Вибір здібності з постійного меню одиниці; підтвердження підмножини карт із руки для оцінювання шаблону; розміщення карти як постійного об’єкта в ігровому світі; вибір цілі для вже зафіксованої атаки ворога.

### Ігри-носії

- [`GAME-0047` — Fights in Tight Spaces](../games/a-f/fights-in-tight-spaces.md)
- [`GAME-0057` — Golf Peaks](../games/g-l/golf-peaks.md)

## ACT-062

- Назва: Відкотити непідтверджену тактичну чернетку
- Переглянуто: `2026-08-23`

### Операційне визначення

До підтвердження поточного обмеженого тактичного ходу гравець відновлює будь-який попередній дискретний крок чернетки й може замінити наступні команди, тоді як завершені раніші ходи лишаються недоступними.

### Включає

Відкочування у Tactical Breach Wizards рішень щодо руху, здібностей і ресурсів після того, як Foresee показує небажаний наслідок поточного ходу.

### Виключає

Безперервне відмотування вже прожитої історії симуляції; довільне редагування команд із часовими мітками; звичайне скасування одного кроку головоломки без явного циклу тактичного прогнозу й підтвердження.

### Ігри-носії

- [`GAME-0048` — Tactical Breach Wizards](../games/s-z/tactical-breach-wizards.md)

## ACT-063

- Назва: Ствердити прихований бінарний клас клітинки
- Переглянуто: `2026-08-23`

### Операційне визначення

Гравець вибирає одну нерозв’язану позицію й стверджує, до якого з двох фіксованих прихованих класів вона вже належить.

### Включає

Натискання лівою кнопкою на помаранчевій клітинці Hexcells Infinite, щоб ствердити, що вона синя, або правою кнопкою — що вона чорна.

### Виключає

Команда системі лише відкрити невідоме значення; запис попереднього значення, яке лишається редагованим до перевірки; вибір значення, якого не існувало до цієї дії.

### Ігри-носії

- [`GAME-0049` — Hexcells Infinite](../games/g-l/hexcells-infinite.md)

## ACT-064

- Назва: Розвернути керованого агента в протилежний бік
- Переглянуто: `2026-08-23`

### Операційне визначення

Гравець наказує постійному керованому агенту розвернути напрямок погляду в протилежний бік, лишаючись у тій самій адресованій позиції.

### Включає

Розворот Wanderer у Shogun Showdown як бойова дія, що витрачає один хід.

### Виключає

Обертання прикріпленого до тіла інструмента, повна займана під час руху область якого впливає на рішення; зміна ракурсу камери; переміщення в іншу позицію.

### Ігри-носії

- [`GAME-0050` — Shogun Showdown](../games/s-z/shogun-showdown.md)

## ACT-065

- Назва: Редагувати обмежену чергу виконання атак
- Переглянуто: `2026-08-23`

### Операційне визначення

Гравець вставляє одну наразі готову плитку атаки в обмежену впорядковану чергу або до активації змінює склад чи порядок плиток, які вже чекають у цій черзі.

### Включає

Додавання плитки Shogun Showdown до трислотової черги атак і вільне перевпорядкування чи вилучення плиток із черги до її запуску.

### Виключає

Негайне виконання вибраної атаки; вибір обов’язкового першого елемента черги, поданого системою; редагування майбутніх команд із часовими мітками.

### Ігри-носії

- [`GAME-0050` — Shogun Showdown](../games/s-z/shogun-showdown.md)

## ACT-066

- Назва: Активувати підготовлену чергу атак
- Переглянуто: `2026-08-23`

### Операційне визначення

Гравець віддає поточну підготовлену впорядковану чергу атак на негайне автоматичне виконання як одну дію.

### Включає

Запуск від однієї до трьох плиток атак із черги Shogun Showdown.

### Виключає

Вставлення чи перевпорядкування плитки в черзі; окремий вибір цілі для кожної атаки; завершення фази планування, після якої виконуються ворожі наміри.

### Ігри-носії

- [`GAME-0050` — Shogun Showdown](../games/s-z/shogun-showdown.md)

## ACT-067

- Назва: Поміняти керованого агента місцями із сусідньою одиницею попереду
- Переглянуто: `2026-08-23`

### Операційне визначення

Віддавши команду руху вперед у зайняту сусідню позицію, гравець міняє місцями керованого агента й одиницю, в бік якої той дивиться, замість відхилення руху або штовхання цієї одиниці.

### Включає

Обмін Wanderer у Shogun Showdown місцями з ворогом безпосередньо перед нею.

### Виключає

Вибір будь-яких двох елементів поля для обміну; відштовхування сусідньої одиниці; телепортація без обміну позиціями.

### Ігри-носії

- [`GAME-0050` — Shogun Showdown](../games/s-z/shogun-showdown.md)

## ACT-068

- Назва: Редагувати постійну розгалужену дорожню мережу
- Переглянуто: `2026-08-24`

### Операційне визначення

Гравець малює, подовжує, перепрокладає, скасовує або позначає для вилучення постійний просторовий граф доріг, перехрестя якого можуть розгалужуватися, а зв’язаними сегментами автоматично користуються кілька транспортних засобів.

### Включає

Прокладання й перепрокладання звичайних доріг у місті режиму Classic у Mini Motorways, поки транспорт продовжує користуватися зв’язаною мережею; довільне малювання й редагування розв’язки Freeways між оцінюваннями руху; будівництво й удосконалення постійних доріг у SimCity 4 та Cities: Skylines.

### Виключає

Редагування однієї іменованої впорядкованої лінії сполучення; керування окремим транспортним засобом; прокладання одного нерозгалуженого маршруту, геометрія якого витрачається або назавжди блокується після початку прогону.

### Ігри-носії

- [`GAME-0132` — Anno 1800](../games/a-f/anno-1800.md)
- [`GAME-0284` — "Cities: Skylines II"](../games/a-f/cities-skylines-ii.md)
- [`GAME-0121` — "Cities: Skylines"](../games/a-f/cities-skylines.md)
- [`GAME-0052` — Freeways](../games/a-f/freeways.md)
- [`GAME-0130` — Frostpunk](../games/a-f/frostpunk.md)
- [`GAME-0051` — Mini Motorways](../games/m-r/mini-motorways.md)
- [`GAME-0390` — SimCity 2000](../games/s-z/simcity-2000.md)
- [`GAME-0118` — SimCity 4 Deluxe Edition](../games/s-z/simcity-4-deluxe-edition.md)
- [`GAME-0133` — Timberborn](../games/s-z/timberborn.md)
- [`GAME-0134` — "Workers & Resources: Soviet Republic"](../games/s-z/workers-resources-soviet-republic.md)

## ACT-069

- Назва: Регулювати висоту активного відрізка дороги
- Переглянуто: `2026-08-23`

### Операційне визначення

Під час прокладання однієї ділянки дороги гравець піднімає або опускає її активний відрізок, щоб геометричний перетин став різнорівневим шляхопроводом над або під іншою дорогою, а не перехрестям на одному рівні.

### Включає

Використання засобів підняття й опускання під час прокладання рампи у Freeways, щоб вона перетнула іншу дорогу без з’єднання з нею.

### Виключає

Зміна висоти камери; розміщення готового жетона мосту, яке лише витрачає запас; автоматичний вибір рівня перетину на основі геометрії.

### Ігри-носії

- [`GAME-0052` — Freeways](../games/a-f/freeways.md)

## ACT-070

- Назва: Вибрати, зорієнтувати й розмістити елемент зі скінченною займаною областю
- Переглянуто: `2026-08-23`

### Операційне визначення

Гравець вибирає будь-який із решти елементів у скінченному видимому запасі для побудови, задає одну з дозволених жорстких орієнтацій і фіксує всю його типізовану займану область із вибраним зміщенням у фіксованому контейнері.

### Включає

Вибір, обертання на чверть оберту й розміщення одного доступного багатоблокового харчового елемента в коробці першого розділу inbento; вибір, обертання й розміщення одного зібраного тетроміно в першому компонувальнику воріт A1 у The Talos Principle.

### Виключає

Розміщення обов’язкового наступного елемента з початку поданої черги; редагування постійного компонента машини; незалежне призначення значення кожній покритій клітинці; розігрування карти, яка віддає команду іншій рухомій сутності.

### Ігри-носії

- [`GAME-0058` — inbento](../games/g-l/inbento.md)
- [`GAME-0090` — The Talos Principle](../games/s-z/the-talos-principle.md)

## ACT-071

- Назва: Вибрати початкову клітинку зв’язної області та новий клас
- Переглянуто: `2026-08-23`

### Операційне визначення

Гравець вибирає один новий клас і одну адресовану клітинку, наказуючи змінити клас усього поточного зв’язного компонента, що містить цю початкову клітинку.

### Включає

Вибір кольору з палітри й натискання паперової клітинки іншого кольору в KAMI.

### Виключає

Призначення нового класу лише адресованій клітинці; вибір фіксованої геометричної області; вилучення групи однакових елементів; розширення з одного назавжди фіксованого початку.

### Ігри-носії

- [`GAME-0059` — KAMI](../games/g-l/kami.md)

## ACT-072

- Назва: Активувати адресований тригер механізму
- Переглянуто: `2026-08-23`

### Операційне визначення

Гравець вибирає один видимий тригер і наказує кожному механізму, що зараз із ним зв’язаний, почати оголошену автоматичну операцію.

### Включає

Натискання одного круглого тригера в HOOK, щоб утягнути один або кілька приєднаних механізмів із ліній та гаків; натискання адресованого символу вогню в The Room, щоб відкрити зв’язане з ним відділення для ключа.

### Виключає

Переміщення аватара до перемикача в ігровому світі; утримання натискної зони; редагування графа з’єднань; безпосереднє перетягування зв’язаних механізмів.

### Ігри-носії

- [`GAME-0060` — HOOK](../games/g-l/hook.md)
- [`GAME-0105` — Outer Wilds](../games/m-r/outer-wilds.md)
- [`GAME-0085` — The Room](../games/s-z/the-room.md)

## ACT-073

- Назва: Подати повну впорядковану гіпотезу із символів
- Переглянуто: `2026-08-23`

### Операційне визначення

Гравець заповнює кожну позицію однієї впорядкованої пропозиції фіксованої довжини символами з обмеженого словника й подає повну послідовність на порівняння з однією прихованою цільовою послідовністю.

### Включає

Розмістити чотири кольорові кілочки з дозволеними повторами й подати завершений рядок як одне припущення Mastermind; ввести й подати одне розпізнане п’ятибуквене припущення Wordle.

### Виключає

Редагування ще не поданого часткового призначення; незалежне твердження про одну приховану клітинку; вибір невпорядкованої підмножини; введення довільної відповіді, позиції якої не мають ідентичності.

### Ігри-носії

- [`GAME-0065` — Mastermind](../games/m-r/mastermind.md)
- [`GAME-0068` — Wordle](../games/s-z/wordle.md)

## ACT-074

- Назва: Запустити пробу з крайового входу
- Переглянуто: `2026-08-23`

### Операційне визначення

Гравець вибирає один невикористаний вхід на межі прихованого просторового поля й запускає одну пробу, внутрішню траєкторію та кінцевий категорійний результат якої визначає система.

### Включає

Запустити один лазер Black Box із ще не використаної крайової позиції, щоб отримати спостереження влучання, відбиття або парного виходу.

### Виключає

Виявлення адресованої крайової клітинки; малювання маршруту крізь поле; подання повної гіпотези прихованої розкладки; повтор уже розв’язаного входу як нового спостереження.

### Ігри-носії

- [`GAME-0066` — Black Box](../games/a-f/black-box.md)

## ACT-075

- Назва: Подати просторову гіпотезу точної потужності
- Переглянуто: `2026-08-23`

### Операційне визначення

Після позначення визначеної точної кількості позицій в обмеженому полі гравець подає цю повну пропозицію зайнятості на глобальне порівняння з прихованою просторовою системою.

### Включає

Натиснути `Check` у стандартному Black Box після позначення рівно п’яти клітинок як куль.

### Виключає

Подання впорядкованої послідовності символів; твердження про одну клітинку без глобальної перевірки; виявлення позначеної позиції; вибір невпорядкованої підмножини з уже видимих об’єктів.

### Ігри-носії

- [`GAME-0066` — Black Box](../games/a-f/black-box.md)

## ACT-076

- Назва: Відтворити показану впорядковану послідовність сигналів
- Переглянуто: `2026-08-23`

### Операційне визначення

Під час фази відповіді гравець натискає один елемент обмеженого набору елементів керування для кожної порядкової позиції послідовності, яку система щойно показала, зберігаючи ідентичність і порядок сигналів.

### Включає

Натискати чотири кольорові панелі Simon, щоб відтворити повну поточну світлову послідовність від першого сигналу до останнього.

### Виключає

Подання повністю редагованої пропозиції як одного запиту; вибір невпорядкованої підмножини; реакцію лише на найновіший сигнал; введення сигналів, поки система ще показує ціль.

### Ігри-носії

- [`GAME-0067` — Simon](../games/s-z/simon.md)

## ACT-077

- Назва: Натиснути адресовану клітинку з двостановим значенням
- Переглянуто: `2026-08-23`

### Операційне визначення

Гравець вибирає одну окремо адресовану клітинку фіксованого поля й підтверджує одне натискання, визначений ефект якого обчислюється від цієї позиції незалежно від того, в якому з двох станів клітинка перебуває зараз.

### Включає

Натиснути будь-яку ввімкнену або вимкнену кнопку оригінального поля Lights Out розміром 5 × 5.

### Виключає

Призначення запропонованого значення вибраній клітинці; виявлення прихованого значення; вибір віддаленого тригера механізму; вибір глобального напрямку замість позиції.

### Ігри-носії

- [`GAME-0069` — Lights Out](../games/g-l/lights-out.md)

## ACT-078

- Назва: Запустити призначене ковзне тіло у вибраному напрямі
- Переглянуто: `2026-08-23`

### Операційне визначення

Коли одне призначене тіло нерухоме, гравець вибирає один дозволений напрямок і запускає тіло в автоматичний прямолінійний рух, не вибираючи проміжної чи кінцевої клітинки.

### Включає

Запустити зелену кулю Inertia горизонтально, вертикально або діагонально з її поточної позиції зупинки.

### Виключає

Рух кожного елемента поля одним глобальним напрямком; безпосередній вибір цільової клітинки; кермування або зміну напрямку під час ще не завершеного руху; введення одного кроку до сусідньої клітинки, який лишається під контролем гравця.

### Ігри-носії

- [`GAME-0070` — Inertia](../games/g-l/inertia.md)

## ACT-079

- Назва: Перемкнути ортогональне парування суміжних клітинок
- Переглянуто: `2026-08-23`

### Операційне визначення

Гравець вибирає спільну межу двох ортогонально суміжних фіксованих клітинок, щоб установити або прибрати одне запропоноване відношення парування розміром 1 × 2.

### Включає

Об’єднати дві сусідні числові клітинки в одне доміно Dominosa.

### Виключає

Переміщення фізичного доміно з інвентарю; незалежне призначення символів двом клітинкам; малювання шляху довільної довжини; парування діагональних або непросторових ідентичностей.

### Ігри-носії

- [`GAME-0073` — Dominosa](../games/a-f/dominosa.md)

## ACT-080

- Назва: Циклічно змінити обмежену кратність зв’язку найближчих вершин
- Переглянуто: `2026-08-23`

### Операційне визначення

Гравець вибирає один напрямок від фіксованої вершини, націлюється на найближчу видиму вершину вздовж цього променя й циклічно змінює кратність зв’язку між ними у скінченному впорядкованому домені.

### Включає

Перетягнути від одного острова Bridges до його найближчого ортогонального сусіда, перемикаючи відсутній, одинарний і подвійний міст.

### Виключає

Вибір довільної не найближчої кінцевої точки; довільне малювання шляху; переміщення фізичної деталі мосту; перемикання одного незалежного двостанового ребра.

### Ігри-носії

- [`GAME-0074` — Bridges](../games/a-f/bridges.md)

## ACT-081

- Назва: Перемкнути незалежно адресоване двостанове ребро
- Переглянуто: `2026-08-23`

### Операційне визначення

Гравець вибирає одне фіксоване дозволене ребро й незалежно змінює, чи належить це ребро до запропонованого підграфа розв’язку.

### Включає

Клацнути лівою кнопкою по одному жовтому сегменту сітки Loopy, щоб позначити його частиною циклу, а потім клацнути знову, щоб повернути невідомий стан; накреслити або стерти одну фіксовану внутрішню межу клітинок у Galaxies; вибрати або очистити одне дозволене ортогональне з’єднання між центрами сусідніх клітинок Pearl.

### Виключає

Трасування безперервного маршруту одним жестом; вибір пари кінцевих точок і кратності; призначення символу грані; автоматичне поширення того самого стану на сусідні ребра.

### Ігри-носії

- [`GAME-0078` — Galaxies](../games/g-l/galaxies.md)
- [`GAME-0076` — Loopy](../games/g-l/loopy.md)
- [`GAME-0081` — Pearl](../games/m-r/pearl.md)

## ACT-082

- Назва: Зв’язати наступника вздовж напрямленого променя
- Переглянуто: `2026-08-23`

### Операційне визначення

Гравець вибирає одне адресоване джерело й одну допустиму ціль на будь-якій додатній відстані вздовж фіксованого напрямленого променя джерела, оголошуючи ціль безпосереднім наступником цього джерела у впорядкованому ланцюгу.

### Включає

Перетягнути від однієї клітинки Signpost до будь-якої ще допустимої клітинки, що лежить уздовж показаного ортогонального або діагонального напрямку її стрілки.

### Виключає

Зв’язування лише з найближчою видимою ціллю; трасування кожної проміжної позиції; рух агента вздовж променя; вибір напрямку, коли джерело вже його фіксує; зв’язування двох довільних клітинок без упорядкованого відношення.

### Ігри-носії

- [`GAME-0082` — Signpost](../games/s-z/signpost.md)

## ACT-083

- Назва: Повернути адресовану плитку на місці
- Переглянуто: `2026-08-23`

### Операційне визначення

Гравець вибирає одну стійку адресовану плитку й змінює лише її жорстку орієнтацію в тій самій позиції, зберігаючи її форму, порти та ідентичність.

### Включає

Повернути одну кінцеву, пряму, кутову або Т-подібну плитку Net за годинниковою стрілкою, проти неї чи на 180 градусів, не переміщуючи плитку до іншої клітинки.

### Виключає

Поворот активного рухомого елемента до його фіксації; поворот цілого зв’язаного шару; переміщення, а потім поворот фрагмента карти; вибір орієнтації під час установлення нової деталі; зміну кількості портів плитки.

### Ігри-носії

- [`GAME-0083` — Net](../games/m-r/net.md)

## ACT-084

- Назва: Циклічно зсунути адресовану лінію
- Переглянуто: `2026-08-23`

### Операційне визначення

Гравець вибирає один допустимий адресований рядок або стовпець і зміщує кожен стійкий елемент цієї лінії на однакову фіксовану кількість позицій, циклічно переносячи витіснений крайній елемент на протилежний кінець і зберігаючи орієнтацію кожного елемента.

### Включає

Зсунути один нецентральний рядок Netslide ліворуч або праворуч чи один нецентральний стовпець угору або вниз на одну плитку.

### Виключає

Застосування одного напрямку до кожного рухомого елемента на всьому полі; зсув лінії в порожній буфер; поворот жорсткого шару; рух лише одного вибраного елемента; автоматичне стискання або злиття лінії.

### Ігри-носії

- [`GAME-0084` — Netslide](../games/m-r/netslide.md)

## ACT-085

- Назва: Маніпулювати обмеженим дієгетичним компонентом
- Переглянуто: `2026-08-23`

### Операційне визначення

Гравець безпосередньо перетягує або повертає один стійкий видимий компонент механізму лише вздовж його авторськи визначеної локальної траєкторії чи в межах діапазону орієнтацій, фіксуючи отриманий фізичний стан компонента.

### Включає

Зсувати кришки замкових щілин The Room, повертати вставлений ключ або гайковий ключ, обертати одне переднє кільце й тягнути відімкнені дверцята сейфа; знімати ванну, що прикриває Джозефа в Machinarium, опускати відкритий тулуб і згинати закріплену опору звалища до придатного стану; повертати позначений центральний міст Monument Valley його авторськи визначеною локальною дугою, доки він не зупиниться в орієнтації, що утворює маршрут.

### Виключає

Поворот адресованої плитки сітки на абстрактний крок; зміну лише ракурсу камери; переміщення вільного твердого об’єкта у просторі світу; натискання тригера, після якого пов’язаний механізм рухається автоматично.

### Ігри-носії

- [`GAME-0123` — Inscryption](../games/g-l/inscryption.md)
- [`GAME-0086` — Machinarium](../games/m-r/machinarium.md)
- [`GAME-0093` — Monument Valley](../games/m-r/monument-valley.md)
- [`GAME-0111` — Myst](../games/m-r/myst.md)
- [`GAME-0085` — The Room](../games/s-z/the-room.md)

## ACT-086

- Назва: Змінити конфігурацію шарнірного предмета в інвентарі
- Переглянуто: `2026-08-23`

### Операційне визначення

Під час огляду одного отриманого предмета інвентарю гравець повертає або складає його шарнірні частини, фіксуючи одну з кількох стійких функціональних конфігурацій без витрачання чи встановлення предмета.

### Включає

Перемикати особливий ключ The Room між спіральною та короноподібною формами перед застосуванням до різних замків.

### Виключає

Поворот плитки поля; вибір фіксованої орієнтації під час установлення нової деталі; лише огляд утримуваного предмета з іншого ракурсу; заміну одного спорядженого предмета іншим.

### Ігри-носії

- [`GAME-0085` — The Room](../games/s-z/the-room.md)

## ACT-087

- Назва: Застосувати предмет з інвентарю до відповідного пристрою
- Переглянуто: `2026-08-24`

### Операційне визначення

Гравець вибирає здобутий предмет з інвентарю та застосовує його до конкретного постійного пристрою, якщо тип і поточний стан цього пристрою допускають таке використання.

### Включає

Вставити налаштований ключ The Room у відповідну замкову щілину, накласти металеву пластину на відповідний гвинт і встановити знайдену лінзу у вузол окуляра; застосувати складений інструмент із магніту й мотузки Machinarium до підготовленої опори звалища; застосувати готовий рибальський інструмент The Longest Journey до активної ділянки ключа біля колії.

### Виключає

Екіпірування здобичі зі статистичними показниками; встановлення будівельної деталі на поле; збирання предмета під час контакту; автоматичне відкриття перешкоди ключем, який несе персонаж, під час дотику.

### Ігри-носії

- [`GAME-0173` — Blue Prince](../games/a-f/blue-prince.md)
- [`GAME-0247` — Dishonored (2012)](../games/a-f/dishonored-2012.md)
- [`GAME-0186` — "Don’t Starve Together"](../games/a-f/dont-starve-together.md)
- [`GAME-0123` — Inscryption](../games/g-l/inscryption.md)
- [`GAME-0086` — Machinarium](../games/m-r/machinarium.md)
- [`GAME-0129` — Minecraft](../games/m-r/minecraft.md)
- [`GAME-0139` — Palworld](../games/m-r/palworld.md)
- [`GAME-0330` — Silent Hill 2 (2024 remake)](../games/s-z/silent-hill-2-2024.md)
- [`GAME-0087` — The Longest Journey](../games/s-z/the-longest-journey.md)
- [`GAME-0085` — The Room](../games/s-z/the-room.md)
- [`GAME-0343` — The Secret of Monkey Island](../games/s-z/the-secret-of-monkey-island.md)
- [`GAME-0294` — V Rising](../games/s-z/v-rising.md)
- [`GAME-0197` — Valheim](../games/s-z/valheim.md)

## ACT-088

- Назва: Змінити конфігурацію шарнірного аватара заради досяжності
- Переглянуто: `2026-08-23`

### Операційне визначення

Гравець безпосередньо переводить одного керованого шарнірного аватара між визначеними конфігураціями тіла, різна геометрія яких змінює, які можливості взаємодії поточної сцени доступні аватару.

### Включає

Витягнути телескопічний тулуб Джозефа в Machinarium, щоб забрати високо розташовану ляльку, а потім стиснути його перед звичайною ходьбою та обміном предметами.

### Виключає

Зміну масштабу камери; присідання без важливої для правил зміни досяжності; рух незалежного компонента механізму; екіпірування предмета, що змінює числовий показник дальності.

### Ігри-носії

- [`GAME-0086` — Machinarium](../games/m-r/machinarium.md)

## ACT-089

- Назва: Зібрати адресований предмет сцени в інвентар
- Переглянуто: `2026-08-23`

### Операційне визначення

Гравець вибирає один доступний зараз адресований предмет сцени, прибирає його з позиції в сцені й додає його стійку ідентичність до дискретного інвентарю утримуваних предметів.

### Включає

Забрати високо розташовану ляльку, незакріплений магніт і котушку мотузки в Machinarium після виконання відповідних передумов досяжності й пересування; забрати готову супербатарею Day of the Tentacle з полиці Реда.

### Виключає

Безперервне перенесення вільного твердого об’єкта у просторі світу; автоматичне отримання предмета від персонажа; збирання жетона очок під час контакту; виявлення предмета без його отримання.

### Ігри-носії

- [`GAME-0173` — Blue Prince](../games/a-f/blue-prince.md)
- [`GAME-0088` — Day of the Tentacle](../games/a-f/day-of-the-tentacle.md)
- [`GAME-0301` — "Divinity: Original Sin 2 - Definitive Edition"](../games/a-f/divinity-original-sin-2-definitive-edition.md)
- [`GAME-0086` — Machinarium](../games/m-r/machinarium.md)
- [`GAME-0330` — Silent Hill 2 (2024 remake)](../games/s-z/silent-hill-2-2024.md)
- [`GAME-0343` — The Secret of Monkey Island](../games/s-z/the-secret-of-monkey-island.md)

## ACT-090

- Назва: Об’єднати два предмети інвентарю
- Переглянуто: `2026-08-23`

### Операційне визначення

Гравець безпосередньо вибирає дві сумісні ідентичності утримуваних предметів і підтверджує їх заміну одним стійким складеним предметом інвентарю, застосування якого до пристрою відрізняється від застосування кожного складника окремо.

### Включає

Поєднати магніт і мотузку Machinarium в один рибальський інструмент; у The Longest Journey спочатку поєднати затискач із мотузкою для білизни, а потім цей складений предмет із надутою качечкою.

### Виключає

Зміну форми одного шарнірного предмета без зміни його ідентичності; активацію двох сусідніх підсилювачів на полі; виготовлення з абстрактної кількості ресурсів; застосування вже готового предмета до пристрою світу.

### Ігри-носії

- [`GAME-0086` — Machinarium](../games/m-r/machinarium.md)
- [`GAME-0330` — Silent Hill 2 (2024 remake)](../games/s-z/silent-hill-2-2024.md)
- [`GAME-0087` — The Longest Journey](../games/s-z/the-longest-journey.md)

## ACT-091

- Назва: Доставити переношуваний предмет адресованому одержувачу
- Переглянуто: `2026-09-08`

### Операційне визначення

Гравець вибирає один предмет, який зараз переносить, і підтверджує його передачу адресованому неігровому персонажу, чий поточний запит приймає цей предмет, вилучаючи предмет із переношуваного стану гравця.

### Включає

Передати ляльку малому роботу зі звалища Machinarium, який показав її у бульбашці запиту; передати Реду Едісону патент і три запитані складники батареї в Day of the Tentacle; забрати готову страву й доставити її відвідувачеві, чиє видиме замовлення називає цю страву, під час дослідженого першого обслуговування в DAVE THE DIVER.

### Виключає

Застосування інструмента до неживого пристрою; екіпірування предмета; відмову від абстрактної суми валюти; автоматичне збирання або обмін під час зіткнення без вибраного отримувача; додавання предмета до абстрактного меню без його перенесення одержувачу.

### Ігри-носії

- [`GAME-0320` — "Animal Crossing: New Horizons"](../games/a-f/animal-crossing-new-horizons.md)
- [`GAME-0278` — DAVE THE DIVER](../games/a-f/dave-the-diver.md)
- [`GAME-0088` — Day of the Tentacle](../games/a-f/day-of-the-tentacle.md)
- [`GAME-0240` — "Kingdom Come: Deliverance II"](../games/g-l/kingdom-come-deliverance-ii.md)
- [`GAME-0086` — Machinarium](../games/m-r/machinarium.md)
- [`GAME-0395` — "The Legend of Zelda: Majora’s Mask"](../games/s-z/the-legend-of-zelda-majoras-mask.md)
- [`GAME-0343` — The Secret of Monkey Island](../games/s-z/the-secret-of-monkey-island.md)

## ACT-092

- Назва: Змінити функціональний стан одного предмета в інвентарі
- Переглянуто: `2026-08-23`

### Операційне визначення

Гравець безпосередньо маніпулює одним отриманим предметом інвентарю, фіксуючи важливий для правил матеріальний стан або стан компонента, але зберігаючи ідентичність предмета й не вибираючи другого предмета інвентарю.

### Включає

Зняти пластир Band-Aid з гумової качечки The Longest Journey у режимі близького огляду, а тоді надути тепер уже діряву качечку за допомогою взаємодії `mouth`.

### Виключає

Повертати або складати шарнірні частини у стійку форму; поєднувати дві ідентичності предметів у новий складений предмет; лише оглядати предмет; застосовувати вже підготовлений предмет до пристрою сцени.

### Ігри-носії

- [`GAME-0087` — The Longest Journey](../games/s-z/the-longest-journey.md)

## ACT-093

- Назва: Передати кількість предметів у видиму вимогу
- Переглянуто: `2026-09-13`

### Операційне визначення

Гравець вибирає одну видиму предметну вимогу й безповоротно передає до її стійкого заповненого стану зазначену кількість придатних предметів з інвентарю — незалежно від того, чи одержувачем є комірка колекції, чи незавершена споруда.

### Включає

Розміщення одного мідного, залізного або золотого злитка у відповідній комірці `Blacksmith’s Bundle` Stardew Valley; розміщення 99 `Slime` або 10 `Bat Wings` в одній придатній комірці `Adventurer’s Bundle`; додавання по одній перенесеній палиці чи листку до розміщеного контуру Temporary Shelter у The Forest.

### Виключає

Передавання предмета конкретному персонажу; поєднання предметів у руках у нову ідентичність; сплату абстрактної валюти; переміщення предмета між оборотними контейнерами інвентарю.

### Ігри-носії

- [`GAME-0266` — Deep Rock Galactic](../games/a-f/deep-rock-galactic.md)
- [`GAME-0314` — Grounded](../games/g-l/grounded.md)
- [`GAME-0129` — Minecraft](../games/m-r/minecraft.md)
- [`GAME-0305` — Sons Of The Forest](../games/s-z/sons-of-the-forest.md)
- [`GAME-0089` — Stardew Valley](../games/s-z/stardew-valley.md)
- [`GAME-0292` — The Forest](../games/s-z/the-forest.md)

## ACT-094

- Назва: Повернути світ до сусіднього ортографічного виду
- Переглянуто: `2026-08-23`

### Операційне визначення

Гравець задає один горизонтальний чвертьоберт за або проти годинникової стрілки від поточного усталеного кардинального виду, роблячи сусідню ортографічну проєкцію авторитетною для подальшого пересування без вибору чи переміщення окремих об’єктів світу.

### Включає

Поворот області Fez ліворуч або праворуч між чотирма класичними двовимірними перспективами, унаслідок чого платформи, раніше розділені за глибиною, можуть отримати іншу суміжність на екрані.

### Виключає

Вільне обертання оглядової камери; поворот одного утримуваного або вибраного об’єкта; обертання зчленованого механізму світу; переміщення фрагмента мапи; фіксацію перспективного зображення, що створює замінну геометрію.

### Ігри-носії

- [`GAME-0091` — Fez](../games/a-f/fez.md)

## ACT-095

- Назва: Обертати камеру перспективи, що визначає правила
- Переглянуто: `2026-08-23`

### Операційне визначення

Гравець безперервно нахиляє або повертає рамку огляду навколо незмінної тривимірної геометрії маршруту, а правила використовують утворену екранну проєкцію, щоб визначити допустиме продовження шляху для непрямо керованого агента.

### Включає

Обертання лабіринту Echochrome, доки розділені кінці доріжки не збігаються на екрані або розрив не ховається, що дозволяє автономному Walker продовжити рух за чинним законом перспективи.

### Виключає

Чотири фіксовані кардинальні чвертьоберти; вільний огляд сцени, камера якого не змінює ігрових правил; обертання одного фізичного об’єкта; зміну гравітації світу; фіксацію перспективного зображення, що створює геометрію.

### Ігри-носії

- [`GAME-0092` — Echochrome](../games/a-f/echochrome.md)

## ACT-096

- Назва: Вибрати досяжний пункт призначення у світі
- Переглянуто: `2026-08-24`

### Операційне визначення

Гравець вибирає одну видиму й наразі досяжну точку, доручаючи системі самостійно пройти проміжний маршрут із кількох вузлів замість подання кожної окремої команди руху.

### Включає

Натискання на п’єдестал у розділі I Monument Valley після того, як поворотний міст зафіксувався у з’єднаному стані, щоб Іда сама пройшла до нього весь маршрут.

### Виключає

Безпосереднє керування рухом персонажа; малювання самого маршруту; наказ рухатися до недосяжної точки; призначення завдання автономному населенню; миттєве перенесення до вибраної точки.

### Ігри-носії

- [`GAME-0132` — Anno 1800](../games/a-f/anno-1800.md)
- [`GAME-0135` — "Captain of Industry"](../games/a-f/captain-of-industry.md)
- [`GAME-0301` — "Divinity: Original Sin 2 - Definitive Edition"](../games/a-f/divinity-original-sin-2-definitive-edition.md)
- [`GAME-0093` — Monument Valley](../games/m-r/monument-valley.md)
- [`GAME-0166` — Sid Meier’s Civilization VI](../games/s-z/sid-meiers-civilization-vi.md)
- [`GAME-0136` — "Surviving Mars: Relaunched"](../games/s-z/surviving-mars.md)
- [`GAME-0343` — The Secret of Monkey Island](../games/s-z/the-secret-of-monkey-island.md)
- [`GAME-0158` — The Sims 4](../games/s-z/the-sims-4.md)

## ACT-097

- Назва: Вибрати ортогональну поверхню як напрям униз
- Переглянуто: `2026-08-23`

### Операційне визначення

Гравець прицілюється в одну видиму придатну поверхню світу, вирівняну за осями, і фіксує її внутрішню нормаль як глобальний напрямок униз для локальної фізичної сцени, не обертаючи окреме тіло й не змінюючи лише камеру.

### Включає

Застосування `Gravity Shift` до стіни або стелі в Manifold Garden, після якого ця поверхня стає підлогою у відповідній кольоровій системі гравітації.

### Виключає

Обертання камери навколо сцени; поворот проєкції з чотирма видами; прохід крізь портал, що переорієнтовує швидкість; перемикання заданого авторами поля зворотної гравітації; вибір діагонального або довільного числового вектора гравітації.

### Ігри-носії

- [`GAME-0095` — Manifold Garden](../games/m-r/manifold-garden.md)

## ACT-098

- Назва: Спрямувати вільний погляд на геометрію, що визначає правило, або від неї
- Переглянуто: `2026-08-23`

### Операційне визначення

Зберігаючи пряме керування аватаром від першої особи, гравець навмисно змінює напрямок погляду на визначену поверхню світу або від неї, коли стан видимості цієї поверхні змінює просторове правило, а сам поворот камери не переміщує аватара.

### Включає

Утримання дверей `Now You See It` в Antichamber у полі зору, щоб їхнє призначення лишалося сталим, або поворот до скляного вікна, після якого двері виходять із поля зору й задана авторами заміна стає можливою.

### Виключає

Обертання навколо незмінної сцени, за якого визначальним стає суміщення в площині екрана; огляд застиглої сцени з доказами; обертання всього світу; прицілювання переносним об’єктом або зброєю; звичайний косметичний рух камери без наслідків для правил.

### Ігри-носії

- [`GAME-0097` — Antichamber](../games/a-f/antichamber.md)

## ACT-099

- Назва: Передати виключне для ролі спостереження або інструкцію
- Переглянуто: `2026-08-23`

### Операційне визначення

Одна людська роль навмисно передає іншій важливе для рішення спостереження, запит або інструкцію, оскільки жодна роль самостійно не має доступу водночас і до поточного стану задачі, і до процедури правил, потрібної для вибору наступної зафіксованої дії керування.

### Включає

У Keep Talking and Nobody Explodes Сапер голосом описує порядок дротів, вигляд кнопки чи ідентифікатори на краю бомби, а Експерт у відповідь називає вибраний дріт або дає часову інструкцію для кнопки.

### Виключає

Необов’язкове тактичне обговорення, коли кожен гравець бачить повний стан і правила; атмосферний діалог; автоматичну підказку; призначення поведінкової ролі симульованому агенту.

### Ігри-носії

- [`GAME-0100` — Keep Talking and Nobody Explodes](../games/g-l/keep-talking-and-nobody-explodes.md)

## ACT-100

- Назва: Зафіксувати дію керування на конкретному модулі бомби
- Переглянуто: `2026-08-23`

### Операційне визначення

Активна роль виконує одну незворотну або чутливу до часу фізичну дію керування на конкретному активному модулі бомби, після чого модуль одразу приймає цю дію або реєструє помилку.

### Включає

Перерізання одного вибраного дроту; натискання й негайне відпускання `Button`; утримування кнопки, щоб показати смугу, та відпускання на вибраній цифрі таймера.

### Виключає

Повідомлення, яку дію керування слід виконати; огляд корпуса; редагування попереднього припущення; натискання механізму, який можна скинути і який не має стану помилки.

### Ігри-носії

- [`GAME-0100` — Keep Talking and Nobody Explodes](../games/g-l/keep-talking-and-nobody-explodes.md)

## ACT-101

- Назва: Записати редаговане попереднє тлумачення гліфа
- Переглянуто: `2026-08-23`

### Операційне визначення

Гравець додає або виправляє довільне попереднє семантичне тлумачення одного повторюваного невідомого гліфа, доки його канонічне значення ще не підтверджено, зберігаючи гіпотезу для наступних появ цього гліфа.

### Включає

Записування й виправлення пробного значення під гліфом Devotee у нотатнику Chants of Sennaar до розв’язання першої сторінки перевірки.

### Виключає

Призначення значення клітинці поля; заповнення фіксованої комірки відповіді; вибір із запропонованих канонічних назв; редагування тексту після того, як перевірка його зафіксувала.

### Ігри-носії

- [`GAME-0101` — Chants of Sennaar](../games/a-f/chants-of-sennaar.md)

## ACT-102

- Назва: Зіставити знайдений гліф з ілюстрованим значенням
- Переглянуто: `2026-08-23`

### Операційне визначення

Гравець призначає один уже зустрінутий невідомий гліф одній заданій авторами ілюстрованій комірці значення на обмеженій сторінці перевірки, будуючи змінюване взаємно-однозначне тлумачення перед поданням усієї сторінки.

### Включає

Розміщення перших трьох гліфів Devotee поруч із малюнками нотатника для значень «відчинено», «зачинено» та «двері» в Chants of Sennaar.

### Виключає

Введення попереднього тлумачення довільним текстом; призначення числа клітинці сітки; складання слів у речення; вибір стану перемикача у світі.

### Ігри-носії

- [`GAME-0101` — Chants of Sennaar](../games/a-f/chants-of-sennaar.md)

## ACT-103

- Назва: Редагувати один постійний рядок відповіді довільної форми
- Переглянуто: `2026-08-23`

### Операційне визначення

Гравець вставляє, видаляє або замінює символи в будь-якому місці одного постійного рядка довільної форми, весь поточний вміст якого лишається відповіддю, що перевіряється.

### Включає

Редагування єдиного поля пароля в The Password Game, коли вже введені символи та відкриті раніше правила й далі беруть участь у грі.

### Виключає

Призначення символу одній обмеженій клітинці поля; заповнення типізованих комірок фрази зі заданого словника; подання цілісного припущення, яке після цього не можна змінити; редагування програмного коду поза грою.

### Ігри-носії

- [`GAME-0102` — The Password Game](../games/s-z/the-password-game.md)

## ACT-104

- Назва: Зіставити два видимі факти справи
- Переглянуто: `2026-08-23`

### Операційне визначення

Гравець вибирає два наразі відкриті факти з матеріалів справи, довідкових правил, мовлення або явно порожньої ділянки для обов’язкового документа й просить систему перевірити заявлений зв’язок між ними.

### Включає

Виділення в режимі перевірки Papers, Please терміну дії паспорта відвідувача й дати в кабіні або порожньої ділянки на стійці документів і чинного правила про дозвіл на в’їзд.

### Виключає

Пасивне читання двох полів; подання остаточного вердикту щодо всієї справи; порівняння двох прихованих значень; заповнення комірок відповіді фактами, видобутими з доказів.

### Ігри-носії

- [`GAME-0103` — Papers, Please](../games/m-r/papers-please.md)

## ACT-105

- Назва: Поставити справі остаточний двійковий штамп
- Переглянуто: `2026-08-23`

### Операційне визначення

Після перевірки однієї поданої справи гравець фіксує рівно одну з двох взаємовиключних остаточних класифікацій, ставлячи відповідну фізичну або дієгетичну позначку на матеріалі справи.

### Включає

Розміщення паспорта відвідувача під штампувальним пристроєм Papers, Please і поставлення штампа `APPROVED` або `DENIED` перед поверненням документів.

### Виключає

Позначення гіпотези, яку можна змінити; визначення класу однієї прихованої клітинки поля; вибір із кількох неостаточних реплік діалогу; автоматичне оцінювання справи без зафіксованого рішення гравця.

### Ігри-носії

- [`GAME-0103` — Papers, Please](../games/m-r/papers-please.md)

## ACT-106

- Назва: Ввести впорядкований код напрямків без переміщення
- Переглянуто: `2026-08-23`

### Операційне визначення

Звертаючись до одного сприйнятливого об’єкта світу, гравець вводить скінченну впорядковану послідовність кардинальних напрямків як символічні команди, а не переміщує керованого персонажа в цих напрямках.

### Включає

Введення послідовності «вниз, праворуч, угору, ліворуч, угору, праворуч» біля візерунчастих дверей TUNIC поруч із фонтаном у Верхньому світі.

### Виключає

Переміщення аватара маршрутом; безперервне креслення траєкторії вказівником; вибір напрямку діалогу; редагування повного коду перед надсиланням.

### Ігри-носії

- [`GAME-0159` — Helldivers 2](../games/g-l/helldivers-2.md)
- [`GAME-0104` — TUNIC](../games/s-z/tunic.md)

## ACT-107

- Назва: Дізнатися в розмові факт, потрібний для подальшої дії
- Переглянуто: `2026-08-24`

### Операційне визначення

Гравець завершує розмову, після якої гра записує один точний факт як відомий і дозволяє використати ці відомості в подальшій взаємодії, не видаючи предмета чи нової фізичної здібності.

### Включає

Розмову з Hornfels про коди запуску в Outer Wilds, після якої код реєструється як відомий; розмови в завданнях Cyberpunk 2077 і Baldur’s Gate 3, які відкривають корисні відомості про людей, місця або доступ.

### Виключає

Читання необов’язкового атмосферного тексту; отримання предмета-ключа; введення коду в цільовий механізм; вибір репліки, єдиним наслідком якої є зміна тону оповіді.

### Ігри-носії

- [`GAME-0148` — Baldur’s Gate 3](../games/a-f/baldurs-gate-3.md)
- [`GAME-0146` — Cyberpunk 2077](../games/a-f/cyberpunk-2077.md)
- [`GAME-0264` — Disco Elysium - The Final Cut](../games/a-f/disco-elysium-the-final-cut.md)
- [`GAME-0219` — Lineage II](../games/g-l/lineage-ii.md)
- [`GAME-0105` — Outer Wilds](../games/m-r/outer-wilds.md)
- [`GAME-0362` — "The Elder Scrolls III: Morrowind"](../games/s-z/the-elder-scrolls-iii-morrowind.md)
- [`GAME-0395` — "The Legend of Zelda: Majora’s Mask"](../games/s-z/the-legend-of-zelda-majoras-mask.md)
- [`GAME-0205` — "The Witcher 3: Wild Hunt"](../games/s-z/the-witcher-3-wild-hunt.md)
- [`GAME-0349` — "Tom Clancy’s Splinter Cell"](../games/s-z/tom-clancys-splinter-cell.md)
- [`GAME-0221` — World of Warcraft](../games/s-z/world-of-warcraft.md)

## ACT-108

- Назва: Подати вільний текстовий запит за термінами до архіву доказів
- Переглянуто: `2026-08-23`

### Операційне визначення

Гравець вводить одне чи кілька вільно вибраних слів і підтверджує їх як окремий запит на пошук у фіксованому архіві доказів.

### Включає

Введення слова або фрази до бази L.O.G.I.C. у Her Story і надсилання запиту для отримання кліпів інтерв’ю, що містять ці вимовлені терміни.

### Виключає

Редагування однієї постійної відповіді; вибір наданих тегів; заповнення структурованих слотів доказів; пошук у вихідному коді застосунку поза грою.

### Ігри-носії

- [`GAME-0106` — Her Story](../games/g-l/her-story.md)

## ACT-109

- Назва: Відтворити вибраний незмінний запис доказів
- Переглянуто: `2026-08-23`

### Операційне визначення

Гравець вибирає один доступний індексований аудіовізуальний запис і наказує відтворити його фіксований доказовий вміст, не змінюючи саму подію.

### Включає

Відкриття й повторне відтворення знайденого кліпу інтерв’ю Her Story для огляду вимовлених слів, виконання та контексту часової позначки.

### Виключає

Вхід у просторовий спогад через труп; пересування всередині завмерлої сцени; відтворення змінної симуляції; пасивне отримання автоматичної катсцени.

### Ігри-носії

- [`GAME-0106` — Her Story](../games/g-l/her-story.md)

## ACT-110

- Назва: Перемістити цілу прохідну панель у площині редагування
- Переглянуто: `2026-08-23`

### Операційне визначення

У зовнішньому режимі редагування компонування гравець поступально переміщує одну цілу панель із фіксованою прохідною геометрією та портами, зберігаючи її інтер’єр, орієнтацію й мешканців.

### Включає

Перетягування однієї ранньої панелі громадського знака The Pedestrian у нове місце в огляді перед побудовою маршруту пішохода.

### Виключає

Переміщення авторитетної ділянки мапи світу; переставляння ілюстрованої сцени між фіксованими слотами; обертання панелі; безпосереднє створення ребра пересування.

### Ігри-носії

- [`GAME-0107` — The Pedestrian](../games/s-z/the-pedestrian.md)

## ACT-111

- Назва: Спарувати сумісні порти прохідних панелей
- Переглянуто: `2026-08-23`

### Операційне визначення

Гравець вибирає два відкриті порти на різних прохідних панелях і підтверджує одне явне двобічне ребро графа між ними.

### Включає

Проведення з’єднання між сумісними кінцевими точками дверей або між взаємодоповнювальними кінцями драбини в ранньому наборі знаків The Pedestrian.

### Виключає

Лише розміщення панелей поруч; проведення через кожну проміжну позицію маршруту; розміщення порталу на геометрії світу; перемикання фіксованого ребра поля.

### Ігри-носії

- [`GAME-0107` — The Pedestrian](../games/s-z/the-pedestrian.md)

## ACT-112

- Назва: Встановити або забрати переносну сферу-світ із п’єдесталу переходу між світами
- Переглянуто: `2026-08-23`

### Операційне визначення

Несучи постійну сферу, що містить світ, гравець установлює її в сумісний п’єдестал переходу між світами або забирає ту саму сферу з п’єдесталу, переводячи її між станами перенесення та встановлення без зміни ідентичності чи вміщеного світу.

### Включає

Установлення помаранчевої сфери-світу Cocoon у сумісний механізм переходу, щоб відкрити її світ, і повернення тієї самої сфери після виходу назовні.

### Виключає

Викидання звичайного твердого предмета будь-де; споживання ключа інвентарю в кріпленні; розміщення кінцевої точки порталу на поверхні; зміну об’єкта або світу, який представляє сфера.

### Ігри-носії

- [`GAME-0108` — Cocoon](../games/a-f/cocoon.md)

## ACT-113

- Назва: Прицілитися й випустити снаряд із фіксованої пускової точки
- Переглянуто: `2026-08-23`

### Операційне визначення

Гравець налаштовує напрямок і силу запуску одного снаряда у фіксованій пусковій точці, а потім підтверджує його випуск у діючу фізичну симуляцію.

### Включає

Натягування й відпускання пташки з рогатки Angry Birds; прицілювання й постріл однією кулькою Peggle з верхньої пускової точки.

### Виключає

Керування снарядом після запуску; розміщення кінцевої точки порталу; вибір дискретного місця призначення без безперервної траєкторії запуску.

### Ігри-носії

- [`GAME-0110` — Angry Birds Classic](../games/a-f/angry-birds-classic.md)
- [`GAME-0114` — Peggle Deluxe](../games/m-r/peggle-deluxe.md)

## ACT-114

- Назва: Хапатися за геометрію світу незалежно керованими руками
- Переглянуто: `2026-08-23`

### Операційне визначення

Гравець незалежно піднімає й спрямовує кожну шарнірну руку та утримує контакт, щоб створити тимчасовий фізичний хват за досяжну геометрію.

### Включає

Хват за край однією чи обома руками в Human: Fall Flat із подальшим підтягуванням ragdoll-тіла вгору або підвішуванням під час зміни положення.

### Виключає

Піднімання одного твердого предмета в центровану позу перенесення; прикріплення автономного агента до конструкції; команду лазіння, що існує лише як анімація.

### Ігри-носії

- [`GAME-0112` — Human: Fall Flat](../games/g-l/human-fall-flat.md)

## ACT-115

- Назва: Оглянути створений грою артефакт зовнішнього інтерфейсу
- Переглянуто: `2026-08-23`

### Операційне визначення

Гравець залишає ігровий світ або переводить із нього фокус, щоб оглянути файл, шар робочого столу чи артефакт імітованої операційної системи, створений грою, і використовує його вміст як інформацію для головоломки.

### Включає

Відкриття авторського документа або підказки на робочому столі у PC-версії OneShot; огляд відповідного артефакту імітованої ОС у World Machine Edition.

### Виключає

Читання внутрішньоігрового посібника; пошук несанкціонованого проходження; відкриття суто діагностичного журналу без наслідків для головоломки.

### Ігри-носії

- [`GAME-0117` — OneShot](../games/m-r/oneshot.md)

## ACT-116

- Назва: Зонувати землю за класом використання та щільністю
- Переглянуто: `2026-08-23`

### Операційне визначення

Гравець позначає обмежені земельні ділянки дозволеним міським призначенням і щільністю, надаючи дозвіл, а не безпосередньо розміщуючи споруди, що можуть згодом там розвинутися.

### Включає

Малювання житлових, комерційних або промислових зон низької, середньої чи високої щільності в SimCity 4; позначення житлових, комерційних, промислових або офісних зон за доступною щільністю в Cities: Skylines.

### Виключає

Розміщення контуру конкретної споруди; зміну податкової політики; прокладання дороги чи комунальної лінії.

### Ігри-носії

- [`GAME-0284` — "Cities: Skylines II"](../games/a-f/cities-skylines-ii.md)
- [`GAME-0121` — "Cities: Skylines"](../games/a-f/cities-skylines.md)
- [`GAME-0390` — SimCity 2000](../games/s-z/simcity-2000.md)
- [`GAME-0118` — SimCity 4 Deluxe Edition](../games/s-z/simcity-4-deluxe-edition.md)

## ACT-117

- Назва: Розмістити міську установу або комунальну мережу за кошти
- Переглянуто: `2026-08-24`

### Операційне визначення

Гравець витрачає кошти на міську установу або прокладений сегмент розподільної мережі, розташування й робочий стан якого змінюють охоплення послугою.

### Включає

Розміщення електростанцій, об’єктів водопостачання, шкіл, лікарень, поліції, пожежних і сміттєвих служб та прокладання електричних або водорозподільних мереж у SimCity 4 і Cities: Skylines.

### Виключає

Зонування землі для автономної приватної забудови; прокладання дороги; зміну повзунка фінансування відомства.

### Ігри-носії

- [`GAME-0284` — "Cities: Skylines II"](../games/a-f/cities-skylines-ii.md)
- [`GAME-0121` — "Cities: Skylines"](../games/a-f/cities-skylines.md)
- [`GAME-0390` — SimCity 2000](../games/s-z/simcity-2000.md)
- [`GAME-0118` — SimCity 4 Deluxe Edition](../games/s-z/simcity-4-deluxe-edition.md)
- [`GAME-0134` — "Workers & Resources: Soviet Republic"](../games/s-z/workers-resources-soviet-republic.md)

## ACT-118

- Назва: Змінити муніципальну ставку податку або фінансування служби
- Переглянуто: `2026-08-23`

### Операційне визначення

Гравець змінює постійний фіскальний параметр, який визначає податкове навантаження сектора або регулярне фінансування й місткість громадської установи.

### Включає

Редагування ставок податку за категоріями зон у SimCity 4 або Cities: Skylines і зміну фінансування транспортних, комунальних чи міських служб.

### Виключає

Сплату одноразової вартості будівництва; прийняття угоди із сусідом; вибір швидкості симуляції.

### Ігри-носії

- [`GAME-0121` — "Cities: Skylines"](../games/a-f/cities-skylines.md)
- [`GAME-0390` — SimCity 2000](../games/s-z/simcity-2000.md)
- [`GAME-0118` — SimCity 4 Deluxe Edition](../games/s-z/simcity-4-deluxe-edition.md)

## ACT-119

- Назва: Розмістити, повернути або демонтувати фабричний об’єкт під час роботи системи
- Переглянуто: `2026-08-24`

### Операційне визначення

Поки виробничий світ працює, гравець розміщує, повертає, демонтує або замінює постійну машину чи об’єкт транспортної, енергетичної або оборонної мережі. Займана ним площа відразу стає частиною активної системи або змінює її.

### Включає

Розміщення й обертання в Factorio бурів, конвеєрів, маніпуляторів, складальних машин, труб, електричних опор, рейок, скринь, стін і турелей, а також їх демонтаж із поверненням до інвентарю, поки решта фабрики продовжує працювати.

### Виключає

Редагування машини лише в окремій зупиненій фазі проєктування; зонування землі для автономної забудови; накладання нематеріалізованого плану будівництва без забезпечення потрібними об’єктами.

### Ігри-носії

- [`GAME-0131` — Dyson Sphere Program](../games/a-f/dyson-sphere-program.md)
- [`GAME-0119` — Factorio](../games/a-f/factorio.md)
- [`GAME-0128` — Satisfactory](../games/s-z/satisfactory.md)
- [`GAME-0122` — shapez 2 - Factory](../games/s-z/shapez-2.md)

## ACT-120

- Назва: Налаштувати правило роботи окремої фабричної споруди
- Переглянуто: `2026-08-24`

### Операційне визначення

Гравець призначає або змінює постійне правило для одного встановленого фабричного об’єкта: що він виробляє, приймає чи відправляє або яку дію виконує після спрацювання видимої сигнальної умови.

### Включає

Вибір рецепта складальної машини Factorio; установлення фільтрів маніпулятора, розділювача, скрині чи поїзда; редагування розкладу поїзда; під’єднання машини до порогової умови логічної мережі.

### Виключає

Фізичне розміщення самого об’єкта; вибір глобальної технології для дослідження; безпосереднє переміщення предмета, який це правило оброблятиме згодом.

### Ігри-носії

- [`GAME-0124` — Against the Storm](../games/a-f/against-the-storm.md)
- [`GAME-0132` — Anno 1800](../games/a-f/anno-1800.md)
- [`GAME-0135` — "Captain of Industry"](../games/a-f/captain-of-industry.md)
- [`GAME-0126` — Dwarf Fortress](../games/a-f/dwarf-fortress.md)
- [`GAME-0131` — Dyson Sphere Program](../games/a-f/dyson-sphere-program.md)
- [`GAME-0119` — Factorio](../games/a-f/factorio.md)
- [`GAME-0130` — Frostpunk](../games/a-f/frostpunk.md)
- [`GAME-0125` — Oxygen Not Included](../games/m-r/oxygen-not-included.md)
- [`GAME-0127` — RimWorld](../games/m-r/rimworld.md)
- [`GAME-0128` — Satisfactory](../games/s-z/satisfactory.md)
- [`GAME-0136` — "Surviving Mars: Relaunched"](../games/s-z/surviving-mars.md)
- [`GAME-0133` — Timberborn](../games/s-z/timberborn.md)
- [`GAME-0134` — "Workers & Resources: Soviet Republic"](../games/s-z/workers-resources-soviet-republic.md)

## ACT-121

- Назва: Обрати поточну ціль технологічного дослідження
- Переглянуто: `2026-09-10`

### Операційне визначення

Гравець обирає доступну технологію для активного напряму досліджень або для місця в його збереженій черзі, після чого поступ цього напряму спрямовується на обрану ціль.

### Включає

Вибір технологій Factorio, додавання їхніх передумов до черги та зміна її порядку; призначення окремої технології кожному з трьох напрямів досліджень у Stellaris.

### Виключає

Виробництво наукових пакетів; вибір рецепта машини; автоматичне отримання вдосконалення без обраного гравцем порядку досліджень.

### Ігри-носії

- [`GAME-0179` — Age of Empires II: Definitive Edition](../games/a-f/age-of-empires-ii-definitive-edition.md)
- [`GAME-0135` — "Captain of Industry"](../games/a-f/captain-of-industry.md)
- [`GAME-0209` — Cossacks 3](../games/a-f/cossacks-3.md)
- [`GAME-0131` — Dyson Sphere Program](../games/a-f/dyson-sphere-program.md)
- [`GAME-0119` — Factorio](../games/a-f/factorio.md)
- [`GAME-0182` — Hearts of Iron IV](../games/g-l/hearts-of-iron-iv.md)
- [`GAME-0166` — Sid Meier’s Civilization VI](../games/s-z/sid-meiers-civilization-vi.md)
- [`GAME-0287` — Stellaris](../games/s-z/stellaris.md)
- [`GAME-0136` — "Surviving Mars: Relaunched"](../games/s-z/surviving-mars.md)

## ACT-122

- Назва: Вручну видобути ресурс або розібрати об’єкт світу
- Переглянуто: `2026-08-24`

### Операційне визначення

Гравець застосовує потрібний інструмент до досяжного ресурсу чи предмета обстановки й чекає завершення роботи, після чого отриманий матеріал або повернений предмет потрапляє до інвентарю чи лишається поруч.

### Включає

Ручний видобуток руди, каменю чи дерева та розбирання розміщених об’єктів у Factorio; розбирання меблів та інших предметів обстановки на матеріали у Project Zomboid.

### Виключає

Роботу машини, яка автоматично виробляє ресурс; знищення ворога зброєю; миттєвий вибір предмета, що вже перебуває у сховищі.

### Ігри-носії

- [`GAME-0233` — 7 Days to Die](../games/0-9/7-days-to-die.md)
- [`GAME-0186` — "Don’t Starve Together"](../games/a-f/dont-starve-together.md)
- [`GAME-0131` — Dyson Sphere Program](../games/a-f/dyson-sphere-program.md)
- [`GAME-0119` — Factorio](../games/a-f/factorio.md)
- [`GAME-0229` — "No Man’s Sky"](../games/m-r/no-mans-sky.md)
- [`GAME-0139` — Palworld](../games/m-r/palworld.md)
- [`GAME-0142` — Project Zomboid](../games/m-r/project-zomboid.md)
- [`GAME-0141` — Rust](../games/m-r/rust.md)
- [`GAME-0128` — Satisfactory](../games/s-z/satisfactory.md)
- [`GAME-0331` — Starfield](../games/s-z/starfield.md)
- [`GAME-0197` — Valheim](../games/s-z/valheim.md)

## ACT-123

- Назва: Виготовити предмет за вибраним відомим рецептом
- Переглянуто: `2026-08-24`

### Операційне визначення

Гравець вибирає один відомий і наразі доступний особистий рецепт та запускає виготовлення однієї чи кількох одиниць визначеного ним результату.

### Включає

Особисте виготовлення у Factorio, Cyberpunk 2077 та Elden Ring, польове виготовлення в Monster Hunter Wilds і негайне виготовлення з інвентарю або біля потрібного робочого місця в Terraria.

### Виключає

Призначення рецепта автономному виробничому об’єкту; довільне поєднання предметів; вибір дослідження; тривалість виконання, якою керує система.

### Ігри-носії

- [`GAME-0233` — 7 Days to Die](../games/0-9/7-days-to-die.md)
- [`GAME-0257` — "Alien: Isolation"](../games/a-f/alien-isolation.md)
- [`GAME-0320` — "Animal Crossing: New Horizons"](../games/a-f/animal-crossing-new-horizons.md)
- [`GAME-0143` — ARC Raiders](../games/a-f/arc-raiders.md)
- [`GAME-0186` — "Don’t Starve Together"](../games/a-f/dont-starve-together.md)
- [`GAME-0131` — Dyson Sphere Program](../games/a-f/dyson-sphere-program.md)
- [`GAME-0152` — Elden Ring](../games/a-f/elden-ring.md)
- [`GAME-0119` — Factorio](../games/a-f/factorio.md)
- [`GAME-0314` — Grounded](../games/g-l/grounded.md)
- [`GAME-0151` — Monster Hunter Wilds](../games/m-r/monster-hunter-wilds.md)
- [`GAME-0229` — "No Man’s Sky"](../games/m-r/no-mans-sky.md)
- [`GAME-0139` — Palworld](../games/m-r/palworld.md)
- [`GAME-0142` — Project Zomboid](../games/m-r/project-zomboid.md)
- [`GAME-0249` — Resident Evil 4 (2023 remake)](../games/m-r/resident-evil-4-2023.md)
- [`GAME-0141` — Rust](../games/m-r/rust.md)
- [`GAME-0128` — Satisfactory](../games/s-z/satisfactory.md)
- [`GAME-0178` — Subnautica](../games/s-z/subnautica.md)
- [`GAME-0153` — Terraria](../games/s-z/terraria.md)
- [`GAME-0261` — The Last of Us Part I](../games/s-z/the-last-of-us-part-i.md)
- [`GAME-0205` — "The Witcher 3: Wild Hunt"](../games/s-z/the-witcher-3-wild-hunt.md)
- [`GAME-0294` — V Rising](../games/s-z/v-rising.md)
- [`GAME-0197` — Valheim](../games/s-z/valheim.md)

## ACT-124

- Назва: Застосувати багаторазове креслення будівництва або демонтажу
- Переглянуто: `2026-08-24`

### Операційне визначення

Гравець розміщує в діючому світі багатооб’єктне креслення або позначає ділянку демонтажу. Це створює збережені завдання для будівельних агентів, а не миттєво будує чи прибирає кожен об’єкт вручну.

### Включає

Накладання, обертання й віддзеркалення креслення у Factorio, розміщення скопійованої ділянки фабрики та позначення території для вилучення будівельними роботами.

### Виключає

Безпосереднє розміщення одного забезпеченого об’єкта; декоративний шар без запиту на виконання; завантаження авторської схеми рівня.

### Ігри-носії

- [`GAME-0135` — "Captain of Industry"](../games/a-f/captain-of-industry.md)
- [`GAME-0131` — Dyson Sphere Program](../games/a-f/dyson-sphere-program.md)
- [`GAME-0119` — Factorio](../games/a-f/factorio.md)

## ACT-125

- Назва: Зіграти одну утримувану карту ефекту
- Переглянуто: `2026-08-23`

### Операційне визначення

Гравець вибирає одну карту, яку зараз тримає, указує будь-яку потрібну допустиму ціль і сплачує її поточну вартість, після чого виконуються негайні та постійні ефекти карти.

### Включає

Розіграш однієї карти Attack, Skill або Power у Slay the Spire під час фази гравця з вибором ворога, якщо карта потребує такої цілі.

### Виключає

Одночасне подання кількох утримуваних карт для оцінювання комбінації; розміщення карти як постійного об’єкта світу; карту, визначальним параметром якої є просторова клітинка, напрямок або геометрія переміщення.

### Ігри-носії

- [`GAME-0155` — Slay the Spire 2](../games/s-z/slay-the-spire-2.md)
- [`GAME-0120` — Slay the Spire](../games/s-z/slay-the-spire.md)

## ACT-126

- Назва: Завершити поточну бойову фазу гравця
- Переглянуто: `2026-08-23`

### Операційне визначення

Гравець явно підтверджує завершення поточної бойової фази, відмовляючись від решти звичайних розіграшів карт, щоб система виконала ефекти кінця ходу та ворожі дії.

### Включає

Натискання End Turn у Slay the Spire після будь-якої кількості допустимих використань карт і зіль.

### Виключає

Автоматичне виконання після кожної окремої команди; завершення зміни в реальному часі; активацію підготовленої просторової черги атак.

### Ігри-носії

- [`GAME-0123` — Inscryption](../games/g-l/inscryption.md)
- [`GAME-0155` — Slay the Spire 2](../games/s-z/slay-the-spire-2.md)
- [`GAME-0120` — Slay the Spire](../games/s-z/slay-the-spire.md)
- [`GAME-0176` — XCOM 2](../games/s-z/xcom-2.md)

## ACT-127

- Назва: Обрати досяжний вузол на відкритому розгалуженому маршруті
- Переглянуто: `2026-08-23`

### Операційне визначення

З поточної позиції на маршруті гравець вибирає один видимо з’єднаний наступний вузол, відкрита категорія якого визначає наступну зустріч або послугу.

### Включає

Вибір з’єднаного вузла мапи Slay the Spire, позначеного як звичайний бій, елітний бій, невідомість, місце відпочинку, крамниця або скарб.

### Виключає

Малювання чи редагування маршруту; вибір довільної віддаленої цілі; вибір серед нагород уже після завершення вузла.

### Ігри-носії

- [`GAME-0123` — Inscryption](../games/g-l/inscryption.md)
- [`GAME-0155` — Slay the Spire 2](../games/s-z/slay-the-spire-2.md)
- [`GAME-0120` — Slay the Spire](../games/s-z/slay-the-spire.md)

## ACT-128

- Назва: Прийняти або пропустити одну запропоновану карту постійної колоди
- Переглянуто: `2026-08-23`

### Операційне визначення

Після того як зустріч або подія показує обмежену пропозицію карт, гравець або додає рівно одну запропоновану карту до постійної колоди забігу, або відхиляє всю пропозицію.

### Включає

Вибір однієї зі звичайних карткових нагород після бою в Slay the Spire або натискання Skip.

### Виключає

Добір тимчасової бойової руки; придбання карти за визначену ціну; заміну карти через перетворення; вибір кількох карт з однієї пропозиції.

### Ігри-носії

- [`GAME-0123` — Inscryption](../games/g-l/inscryption.md)
- [`GAME-0155` — Slay the Spire 2](../games/s-z/slay-the-spire-2.md)
- [`GAME-0120` — Slay the Spire](../games/s-z/slay-the-spire.md)

## ACT-129

- Назва: Застосувати одну постійну зміну до карти колоди
- Переглянуто: `2026-08-27`

### Операційне визначення

Гравець вибирає одну допустиму карту, яка вже перебуває в постійній колоді забігу, і застосовує до неї оголошене тривале вдосконалення, вилучення або перетворення.

### Включає

Поліпшення однієї карти Slay the Spire у місці відпочинку, оплата вилучення однієї карти в торговця або прийняття варіанта події, що перетворює одну карту.

### Виключає

Додавання карти-нагороди; зміну карти лише до кінця поточного бою; сортування чи перегляд колоди без її зміни.

### Ігри-носії

- [`GAME-0123` — Inscryption](../games/g-l/inscryption.md)
- [`GAME-0155` — Slay the Spire 2](../games/s-z/slay-the-spire-2.md)
- [`GAME-0120` — Slay the Spire](../games/s-z/slay-the-spire.md)

## ACT-130

- Назва: Придбати запропонований предмет або послугу
- Переглянуто: `2026-08-27`

### Операційне визначення

Гравець витрачає валюту поточного забігу, матчу або кампанії, щоб отримати запропонований предмет чи скористатися платною послугою.

### Включає

Торговців у забігах; крамниці матчу в Dota 2; магазини Grand Theft Auto V і Cyberpunk 2077; товари в Hollow Knight: Silksong; придбання спорядження під час замороження або відведеного на купівлю часу в Counter-Strike 2; товари й послуги торговців у Baldur’s Gate 3; придбання Crafting Kit та інших товарів за руни в Elden Ring; товари й платні послуги міських неігрових персонажів у Terraria.

### Виключає

Безплатну нагороду; регулярні експлуатаційні витрати; недоступну пропозицію; торгівлю на ринку косметичних предметів.

### Ігри-носії

- [`GAME-0124` — Against the Storm](../games/a-f/against-the-storm.md)
- [`GAME-0148` — Baldur’s Gate 3](../games/a-f/baldurs-gate-3.md)
- [`GAME-0265` — Bloons TD 6](../games/a-f/bloons-td-6.md)
- [`GAME-0173` — Blue Prince](../games/a-f/blue-prince.md)
- [`GAME-0346` — Chrono Trigger](../games/a-f/chrono-trigger.md)
- [`GAME-0137` — Counter-Strike 2](../games/a-f/counter-strike-2.md)
- [`GAME-0218` — Counter-Strike](../games/a-f/counter-strike.md)
- [`GAME-0282` — Dead Cells](../games/a-f/dead-cells.md)
- [`GAME-0266` — Deep Rock Galactic](../games/a-f/deep-rock-galactic.md)
- [`GAME-0138` — Dota 2](../games/a-f/dota-2.md)
- [`GAME-0152` — Elden Ring](../games/a-f/elden-ring.md)
- [`GAME-0327` — Fable](../games/a-f/fable.md)
- [`GAME-0145` — Grand Theft Auto V](../games/g-l/grand-theft-auto-v.md)
- [`GAME-0251` — Hades](../games/g-l/hades.md)
- [`GAME-0150` — "Hollow Knight: Silksong"](../games/g-l/hollow-knight-silksong.md)
- [`GAME-0123` — Inscryption](../games/g-l/inscryption.md)
- [`GAME-0392` — Mario Party 2](../games/m-r/mario-party-2.md)
- [`GAME-0226` — "Need for Speed: Most Wanted (2005)"](../games/m-r/need-for-speed-most-wanted-2005.md)
- [`GAME-0298` — 'Planet Zoo: Console Edition'](../games/m-r/planet-zoo-console-edition.md)
- [`GAME-0336` — "Pokémon Red Version"](../games/m-r/pokemon-red-version.md)
- [`GAME-0165` — Red Dead Redemption 2](../games/m-r/red-dead-redemption-2.md)
- [`GAME-0270` — Risk of Rain 2](../games/m-r/risk-of-rain-2.md)
- [`GAME-0166` — Sid Meier’s Civilization VI](../games/s-z/sid-meiers-civilization-vi.md)
- [`GAME-0155` — Slay the Spire 2](../games/s-z/slay-the-spire-2.md)
- [`GAME-0120` — Slay the Spire](../games/s-z/slay-the-spire.md)
- [`GAME-0307` — Slime Rancher](../games/s-z/slime-rancher.md)
- [`GAME-0153` — Terraria](../games/s-z/terraria.md)
- [`GAME-0164` — "The Binding of Isaac: Rebirth"](../games/s-z/the-binding-of-isaac-rebirth.md)
- [`GAME-0343` — The Secret of Monkey Island](../games/s-z/the-secret-of-monkey-island.md)

## ACT-131

- Назва: Використати витратний предмет із особистого запасу для негайного ефекту
- Переглянуто: `2026-09-05`

### Операційне визначення

Гравець активує один предмет з обмеженого запасу при персонажі, за потреби вказує ціль, яку можна обрати, і остаточно витрачає предмет після його негайного результату.

### Включає

Використання зілля в Slay the Spire; Healing Tint у Clair Obscur: Expedition 33; зілля, сувої та метальні предмети в Baldur’s Gate 3; зілля, раціони та інші витратні предмети в Monster Hunter Wilds; метання Fire Pot та використання інших витратних предметів в Elden Ring; лікувальні зілля та постійні Life Crystals у Terraria; окремі запаси First Aid Kits і EVE Hypos при персонажі у BioShock™ Remastered.

### Виключає

Розіграш карти; спорядження постійного предмета; застосування об’єкта світу до певного місця; відкладене відновлення чи переривний лікувальний процес.

### Ігри-носії

- [`GAME-0148` — Baldur’s Gate 3](../games/a-f/baldurs-gate-3.md)
- [`GAME-0256` — "BioShock™ Remastered"](../games/a-f/bioshock-remastered.md)
- [`GAME-0173` — Blue Prince](../games/a-f/blue-prince.md)
- [`GAME-0144` — Clair Obscur: Expedition 33](../games/a-f/clair-obscur-expedition-33.md)
- [`GAME-0368` — Dead Rising](../games/a-f/dead-rising.md)
- [`GAME-0259` — "Dead Space (2023 remake)"](../games/a-f/dead-space-2023.md)
- [`GAME-0152` — Elden Ring](../games/a-f/elden-ring.md)
- [`GAME-0338` — Final Fantasy VII](../games/a-f/final-fantasy-vii.md)
- [`GAME-0123` — Inscryption](../games/g-l/inscryption.md)
- [`GAME-0240` — "Kingdom Come: Deliverance II"](../games/g-l/kingdom-come-deliverance-ii.md)
- [`GAME-0392` — Mario Party 2](../games/m-r/mario-party-2.md)
- [`GAME-0273` — Max Payne 3](../games/m-r/max-payne-3.md)
- [`GAME-0389` — Mega Man 2](../games/m-r/mega-man-2.md)
- [`GAME-0260` — Metro Exodus](../games/m-r/metro-exodus.md)
- [`GAME-0297` — 'MONSTER HUNTER RISE'](../games/m-r/monster-hunter-rise.md)
- [`GAME-0151` — Monster Hunter Wilds](../games/m-r/monster-hunter-wilds.md)
- [`GAME-0207` — 'Monster Hunter: World'](../games/m-r/monster-hunter-world.md)
- [`GAME-0341` — "Ninja Gaiden Black"](../games/m-r/ninja-gaiden-black.md)
- [`GAME-0160` — "Pokémon Legends: Z-A"](../games/m-r/pokemon-legends-z-a.md)
- [`GAME-0165` — Red Dead Redemption 2](../games/m-r/red-dead-redemption-2.md)
- [`GAME-0280` — Resident Evil 2 (2019 remake)](../games/m-r/resident-evil-2-2019.md)
- [`GAME-0249` — Resident Evil 4 (2023 remake)](../games/m-r/resident-evil-4-2023.md)
- [`GAME-0330` — Silent Hill 2 (2024 remake)](../games/s-z/silent-hill-2-2024.md)
- [`GAME-0155` — Slay the Spire 2](../games/s-z/slay-the-spire-2.md)
- [`GAME-0120` — Slay the Spire](../games/s-z/slay-the-spire.md)
- [`GAME-0153` — Terraria](../games/s-z/terraria.md)
- [`GAME-0164` — "The Binding of Isaac: Rebirth"](../games/s-z/the-binding-of-isaac-rebirth.md)
- [`GAME-0190` — "The Elder Scrolls V: Skyrim Special Edition"](../games/s-z/the-elder-scrolls-v-skyrim-special-edition.md)
- [`GAME-0205` — "The Witcher 3: Wild Hunt"](../games/s-z/the-witcher-3-wild-hunt.md)
- [`GAME-0268` — Undertale](../games/s-z/undertale.md)

## ACT-132

- Назва: Намалювати адміністративний район і призначити місцеву політику
- Переглянуто: `2026-08-23`

### Операційне визначення

Гравець окреслює постійний просторовий район і застосовує, скасовує або змінює оголошену політику чи спеціалізацію землекористування, механічна дія якої обмежена цією територією.

### Включає

Малювання району в Cities: Skylines і призначення йому місцевої політики базової гри або промислової спеціалізації.

### Виключає

Зміну загальноміської ставки податку; зонування приватної землі за призначенням і щільністю; розміщення однієї міської установи; декоративну назву району без впливу на правила.

### Ігри-носії

- [`GAME-0121` — "Cities: Skylines"](../games/a-f/cities-skylines.md)

## ACT-133

- Назва: Дублювати збудовану ділянку фабрики за багаторазовим кресленням
- Переглянуто: `2026-08-23`

### Операційне визначення

Гравець фіксує вибрану багатокомпонентну ділянку фабрики як багаторазовий план, а потім вставляє, повертає або віддзеркалює цей план так, щоб сумісні з ним об’єкти одразу стали частиною діючої фабрики.

### Включає

Креслення shapez 2, які копіюють схеми розміщення машин, конвеєрів, підйомників, труб або платформ і встановлюють інший працездатний екземпляр, витрачаючи передбачену кількість очок креслень.

### Виключає

Креслення Factorio, яке створює незабезпечені примарні запити; ручне відтворення кожного об’єкта; експорт зображення, що не впливає на ігровий світ.

### Ігри-носії

- [`GAME-0122` — shapez 2 - Factory](../games/s-z/shapez-2.md)

## ACT-134

- Назва: Відкрити одне постійне вдосконалення за очки досліджень
- Переглянуто: `2026-08-24`

### Операційне визначення

Гравець витрачає накопичені очки досліджень на один доступний вузол і назавжди додає до поточного збереження відповідну споруду, механіку, місткість, рецепт або вдосконалення.

### Включає

Придбання в shapez 2 рівнів машин, швидкості конвеєрів чи поїздів, місткості платформ, входів Vortex, дротів або інших уже доступних удосконалень крамниці; відкриття доступної технології за очки в Palworld.

### Виключає

Автоматичне отримання нагороди за рубіж; постановку в чергу дослідження, яке лабораторії просувають із часом; зміну локального правила роботи машини.

### Ігри-носії

- [`GAME-0139` — Palworld](../games/m-r/palworld.md)
- [`GAME-0122` — shapez 2 - Factory](../games/s-z/shapez-2.md)

## ACT-135

- Назва: Зіграти утримувану карту істоти у вільну бойову смугу
- Переглянуто: `2026-08-23`

### Операційне визначення

Гравець вибирає одну карту істоти з видимої руки, законно сплачує її поточну вартість і розміщує як постійного бійця в одній вибраній незайнятій дружній смузі.

### Включає

Розміщення карти Beast в Act I Inscryption в одному з чотирьох вільних карткових місць гравця після сплати її вартості Blood, Bone або нульової вартості.

### Виключає

Розіграш картки, ефекти якої розв’язуються без зайняття смуги; перенесення відкритої картки табло між зонами зберігання; розміщення картки як постійної плитки надсвіту.

### Ігри-носії

- [`GAME-0123` — Inscryption](../games/g-l/inscryption.md)

## ACT-136

- Назва: Пожертвувати вибраних керованих істот як плату Blood
- Переглянуто: `2026-08-23`

### Операційне визначення

Під час сплати вартості однієї очікуваної карти істоти гравець вибирає достатню підмножину допустимих дружніх бійців і затверджує їхню оголошену цінність жертви, зазвичай усуваючи їх зі смуг.

### Включає

Пожертву однієї чи кількох звичайних істот в Act I Inscryption для сплати позначок Blood істоти, яку наразі розігрують.

### Виключає

Усунення постійної карти колоди на події мапи; загибель істоти від ворожої шкоди; витрачання вже накопиченої числової валюти.

### Ігри-носії

- [`GAME-0123` — Inscryption](../games/g-l/inscryption.md)

## ACT-137

- Назва: Витягнути одну карту з вибраної бойової колоди
- Переглянуто: `2026-08-23`

### Операційне визначення

На звичайному кроці добору гравець вибирає одну з кількох наразі доступних упорядкованих стопок добору й бере її приховану верхню карту у видиму руку.

### Включає

Вибір між постійною основною колодою й бічною колодою Squirrel на початку ходу гравця в Act I Inscryption.

### Виключає

Вибір відомої карти з відкритого каталогу; автоматичну повну заміну руки; вибір карти, що ввійде до перетасованої колоди.

### Ігри-носії

- [`GAME-0123` — Inscryption](../games/g-l/inscryption.md)

## ACT-138

- Назва: Скласти карту для майбутніх проходжень із вибіркових вихідних ознак
- Переглянуто: `2026-08-23`

### Операційне визначення

Після невдалого проходження гравець робить послідовні вибори з обмежених вибірок вихідних карт, щоб одна нова карта успадкувала вибрані вартість, характеристики й набір здібностей для можливої появи в наступних проходженнях.

### Включає

Вибір вартості, Power і Health та Sigils для Deathcard в Act I Inscryption із трьох окремо вибраних груп із подальшим наданням їй назви.

### Виключає

Вільне призначення довільних значень картки; поліпшення наявної карти проходження; поєднання однакових карт протягом того самого проходження.

### Ігри-носії

- [`GAME-0123` — Inscryption](../games/g-l/inscryption.md)

## ACT-139

- Назва: Розмістити, перемістити або знести звичайну власну споруду
- Переглянуто: `2026-09-07`

### Операційне визначення

Гравець займає сумісну ділянку світу звичайною власною спорудою, може змінити її позицію там, де це дозволяють правила, або позначає її для знесення, змінюючи активний набір виробничих, житлових, робочих чи службових місць.

### Включає

Будівництво, переміщення або знесення звичайних споруд поселення в Against the Storm; розміщення завершених господарських або виробничих споруд в Age of Empires II: Definitive Edition та Command & Conquer Remastered Collection.

### Виключає

Вибір рецепта у вже розміщеній споруді; штампування багаторазового плану з кількох об’єктів; розміщення картки в бойовій смузі.

### Ігри-носії

- [`GAME-0124` — Against the Storm](../games/a-f/against-the-storm.md)
- [`GAME-0179` — Age of Empires II: Definitive Edition](../games/a-f/age-of-empires-ii-definitive-edition.md)
- [`GAME-0320` — "Animal Crossing: New Horizons"](../games/a-f/animal-crossing-new-horizons.md)
- [`GAME-0132` — Anno 1800](../games/a-f/anno-1800.md)
- [`GAME-0275` — Command & Conquer Remastered Collection](../games/a-f/command-and-conquer-remastered-collection.md)
- [`GAME-0209` — Cossacks 3](../games/a-f/cossacks-3.md)
- [`GAME-0130` — Frostpunk](../games/a-f/frostpunk.md)
- [`GAME-0335` — RollerCoaster Tycoon Deluxe](../games/m-r/rollercoaster-tycoon-deluxe.md)
- [`GAME-0166` — Sid Meier’s Civilization VI](../games/s-z/sid-meiers-civilization-vi.md)
- [`GAME-0370` — Theme Hospital](../games/s-z/theme-hospital.md)
- [`GAME-0133` — Timberborn](../games/s-z/timberborn.md)
- [`GAME-0134` — "Workers & Resources: Soviet Republic"](../games/s-z/workers-resources-soviet-republic.md)

## ACT-140

- Назва: Обрати один із кількох взаємовиключних довготривалих варіантів
- Переглянуто: `2026-08-24`

### Операційне визначення

Система пропонує кілька варіантів, з яких гравець може підтвердити лише один. Обране правило, завдання або винагорода зберігається після закриття інтерфейсу, а несумісні альтернативи не застосовуються.

### Включає

Вибір одного креслення, наріжного каменя, наказу, групи новоприбулих або способу завершення події галявини в Against the Storm; вибір завершального варіанта сюжетного режиму в Grand Theft Auto V; вибір завершального маршруту базової гри й відповіді на останній контракт у Cyberpunk 2077.

### Виключає

Придбання довільної кількості предметів із каталогу; вибір тимчасової репліки без постійного механічного наслідку; вибір відомої точки маршруту.

### Ігри-носії

- [`GAME-0124` — Against the Storm](../games/a-f/against-the-storm.md)
- [`GAME-0146` — Cyberpunk 2077](../games/a-f/cyberpunk-2077.md)
- [`GAME-0282` — Dead Cells](../games/a-f/dead-cells.md)
- [`GAME-0130` — Frostpunk](../games/a-f/frostpunk.md)
- [`GAME-0145` — Grand Theft Auto V](../games/g-l/grand-theft-auto-v.md)
- [`GAME-0251` — Hades](../games/g-l/hades.md)
- [`GAME-0332` — "Heroes of Might and Magic III: Complete"](../games/g-l/heroes-of-might-and-magic-iii-complete.md)
- [`GAME-0125` — Oxygen Not Included](../games/m-r/oxygen-not-included.md)
- [`GAME-0136` — "Surviving Mars: Relaunched"](../games/s-z/surviving-mars.md)
- [`GAME-0183` — Vampire Survivors](../games/s-z/vampire-survivors.md)

## ACT-141

- Назва: Надати перевагу одній групі населення коштом інших
- Переглянуто: `2026-08-23`

### Операційне визначення

Гравець визначає одну групу населення, яка отримує оголошений асиметричний модифікатор добробуту, тоді як конкуруючі групи отримують парний штраф.

### Включає

Надання переваги одному виду в Against the Storm із підвищенням його Resolve та зниженням Resolve усіх інших видів.

### Виключає

Призначення працівників до робіт; забезпечення однієї потреби всіх допустимих мешканців; вибір глобального модифікатора складності.

### Ігри-носії

- [`GAME-0124` — Against the Storm](../games/a-f/against-the-storm.md)

## ACT-142

- Назва: Вибрати досяжний пункт метасвіту й набір для вирушання
- Переглянуто: `2026-08-23`

### Операційне визначення

До початку обмеженого проходження гравець вибирає один наразі досяжний пункт на постійній мапі світу й затверджує обмежений набір початкових людей, ресурсів або бонусів.

### Включає

Вибір плитки вирушання й бонусів вирушання перед поселенням Against the Storm.

### Виключає

Звичайний рух усередині поселення; вибір вузла на самодостатній мапі проходження; вільне редагування початкового інвентарю.

### Ігри-носії

- [`GAME-0124` — Against the Storm](../games/a-f/against-the-storm.md)
- [`GAME-0126` — Dwarf Fortress](../games/a-f/dwarf-fortress.md)

## ACT-143

- Назва: Придбати постійне поліпшення метапоступу
- Переглянуто: `2026-08-23`

### Операційне визначення

Між обмеженими проходженнями гравець витрачає постійні ресурси на одне допустиме за передумовами поліпшення, правила або початкові переваги якого діють у наступних проходженнях.

### Включає

Придбання поліпшення Citadel у Against the Storm.

### Виключає

Придбання локального для проходження товару торговця; автоматичне відкриття вмісту на порозі рівня; вибір тимчасового наріжного каменя.

### Ігри-носії

- [`GAME-0124` — Against the Storm](../games/a-f/against-the-storm.md)

## ACT-144

- Назва: Позначити ділянку або об’єкт для автономної роботи
- Переглянуто: `2026-08-24`

### Операційне визначення

Гравець позначає комірки чи об’єкти світу для певного виду роботи, не керуючи безпосередньо працівником, який згодом візьме це доручення.

### Включає

Позначення в Oxygen Not Included наказів копати, збирати врожай, витирати, підмітати, дезінфікувати, атакувати, ловити істот, ремонтувати або демонтувати.

### Виключає

Безпосереднє пересування Дубліканта; розміщення плану споруди; зміну пріоритету вже створеного доручення.

### Ігри-носії

- [`GAME-0135` — "Captain of Industry"](../games/a-f/captain-of-industry.md)
- [`GAME-0126` — Dwarf Fortress](../games/a-f/dwarf-fortress.md)
- [`GAME-0125` — Oxygen Not Included](../games/m-r/oxygen-not-included.md)
- [`GAME-0127` — RimWorld](../games/m-r/rimworld.md)
- [`GAME-0133` — Timberborn](../games/s-z/timberborn.md)

## ACT-145

- Назва: Налаштувати пріоритети працівника й доручення
- Переглянуто: `2026-08-24`

### Операційне визначення

Гравець постійно змінює, як автономний працівник ранжує види роботи або як колонія ранжує окреме доручення серед рівнозначних.

### Включає

Пріоритети Дублікантів, вимкнені категорії, підпріоритети споруд і підвищення до жовтої тривоги в Oxygen Not Included.

### Виключає

Вибір працівника для однієї негайної дії; налаштування рецепта машини; редагування добового розкладу.

### Ігри-носії

- [`GAME-0135` — "Captain of Industry"](../games/a-f/captain-of-industry.md)
- [`GAME-0126` — Dwarf Fortress](../games/a-f/dwarf-fortress.md)
- [`GAME-0125` — Oxygen Not Included](../games/m-r/oxygen-not-included.md)
- [`GAME-0139` — Palworld](../games/m-r/palworld.md)
- [`GAME-0127` — RimWorld](../games/m-r/rimworld.md)
- [`GAME-0136` — "Surviving Mars: Relaunched"](../games/s-z/surviving-mars.md)
- [`GAME-0133` — Timberborn](../games/s-z/timberborn.md)
- [`GAME-0134` — "Workers & Resources: Soviet Republic"](../games/s-z/workers-resources-soviet-republic.md)

## ACT-146

- Назва: Навчити одного агента навички з передумовами
- Переглянуто: `2026-08-23`

### Операційне визначення

Гравець витрачає одне зароблене очко навички на допустимий вузол дерева передумов одного агента, назавжди надаючи його дозвіл або бонус і водночас підвищуючи вартість очікувань цього агента.

### Включає

Призначення одному Дублікантові навичок копання, дослідження, експлуатації, перенесення, землеробства, тваринництва або ракетної справи в Oxygen Not Included.

### Виключає

Пасивний досвід характеристик; дослідження технології колонії; вибір початкової риси.

### Ігри-носії

- [`GAME-0125` — Oxygen Not Included](../games/m-r/oxygen-not-included.md)

## ACT-147

- Назва: Редагувати розклад діяльності агентів
- Переглянуто: `2026-08-23`

### Операційне визначення

Гравець призначає агентів до повторюваного розкладу й редагує його блоки, щоб автономна поведінка перемикалася між працею, дозвіллям, гігієною та сном.

### Включає

Розклади Oxygen Not Included, склад їхніх груп і блоки циклу.

### Виключає

Пріоритезацію одного робочого доручення; призупинення всієї симуляції; фіксовану авторську зміну дня й ночі.

### Ігри-носії

- [`GAME-0125` — Oxygen Not Included](../games/m-r/oxygen-not-included.md)
- [`GAME-0127` — RimWorld](../games/m-r/rimworld.md)

## ACT-148

- Назва: Розмістити план споруди з вибраного матеріалу
- Переглянуто: `2026-09-13`

### Операційне визначення

Гравець вибирає відому споруду й затверджує придатне місце, орієнтацію та специфікацію матеріалів як стійкий план, який має завершити окремий етап постачання й будівництва гравцем або працівником.

### Включає

Споруди, плитки, дроти, труби, мережі автоматизації, драбини й ракетні модулі в Oxygen Not Included; розміщення та обертання контуру Temporary Shelter у The Forest до внесення будь-якої потрібної палиці чи листка.

### Виключає

Миттєве встановлення готового об’єкта з інвентарю; позначення природного рельєфу для копання; застосування багатооб’єктного креслення.

### Ігри-носії

- [`GAME-0135` — "Captain of Industry"](../games/a-f/captain-of-industry.md)
- [`GAME-0126` — Dwarf Fortress](../games/a-f/dwarf-fortress.md)
- [`GAME-0314` — Grounded](../games/g-l/grounded.md)
- [`GAME-0125` — Oxygen Not Included](../games/m-r/oxygen-not-included.md)
- [`GAME-0139` — Palworld](../games/m-r/palworld.md)
- [`GAME-0127` — RimWorld](../games/m-r/rimworld.md)
- [`GAME-0305` — Sons Of The Forest](../games/s-z/sons-of-the-forest.md)
- [`GAME-0136` — "Surviving Mars: Relaunched"](../games/s-z/surviving-mars.md)
- [`GAME-0292` — The Forest](../games/s-z/the-forest.md)
- [`GAME-0133` — Timberborn](../games/s-z/timberborn.md)
- [`GAME-0134` — "Workers & Resources: Soviet Republic"](../games/s-z/workers-resources-soviet-republic.md)

## ACT-149

- Назва: Вибрати ціль дослідження колонії
- Переглянуто: `2026-08-24`

### Операційне визначення

Гравець вибирає одну досяжну технологію як загальноколоніальну ціль, потрібні типи очок дослідження для якої вироблятимуть укомплектовані персоналом станції.

### Включає

Вибір вузла дерева досліджень Oxygen Not Included після завершення його передумов.

### Виключає

Призначення Дубліканта до дослідницької роботи; забезпечення станції матеріалом; придбання поліпшення метапоступу.

### Ігри-носії

- [`GAME-0130` — Frostpunk](../games/a-f/frostpunk.md)
- [`GAME-0125` — Oxygen Not Included](../games/m-r/oxygen-not-included.md)
- [`GAME-0127` — RimWorld](../games/m-r/rimworld.md)
- [`GAME-0134` — "Workers & Resources: Soviet Republic"](../games/s-z/workers-resources-soviet-republic.md)

## ACT-150

- Назва: Створити умовний виробничий наказ фортеці
- Переглянуто: `2026-08-23`

### Операційне визначення

Гравець створює повторюваний виробничий наказ, рецепт, кількість, частота й умови запасу якого зберігаються для автономного виконання.

### Включає

Керовані менеджером робочі накази Dwarf Fortress із матеріалом, кількістю, частотою повторення й перевірюваними умовами.

### Виключає

Наказ однієї негайної роботи майстерні; безпосереднє створення предмета; налаштування транспортних фільтрів.

### Ігри-носії

- [`GAME-0126` — Dwarf Fortress](../games/a-f/dwarf-fortress.md)
- [`GAME-0127` — RimWorld](../games/m-r/rimworld.md)

## ACT-151

- Назва: Налаштувати фільтрований склад і зв’язки постачання
- Переглянуто: `2026-08-23`

### Операційне визначення

Гравець оголошує, які категорії предметів може приймати просторовий склад, і за бажанням визначає напрямки його зв’язків віддавання або отримання.

### Включає

Власні фільтри складів Dwarf Fortress та зв’язки з майстернями або іншими складами.

### Виключає

Переміщення одного предмета вручну; вибір виробничого рецепта; креслення маршруту транспортного засобу.

### Ігри-носії

- [`GAME-0126` — Dwarf Fortress](../games/a-f/dwarf-fortress.md)
- [`GAME-0127` — RimWorld](../games/m-r/rimworld.md)

## ACT-152

- Назва: Визначити функціональну зону або приватну кімнату
- Переглянуто: `2026-08-23`

### Операційне визначення

Гравець позначає просторову область, вибирає її інституційну функцію й може призначити її мешканцеві або службі.

### Включає

Спальні, кабінети, їдальні, лікарні, місця зустрічей, пасовища та інші зони у Dwarf Fortress.

### Виключає

Розміщення потрібних меблів; вибір робочої спеціалізації; саме лише надання області назви.

### Ігри-носії

- [`GAME-0126` — Dwarf Fortress](../games/a-f/dwarf-fortress.md)
- [`GAME-0127` — RimWorld](../games/m-r/rimworld.md)

## ACT-153

- Назва: Налаштувати спорядження, розклад і наказ загону
- Переглянуто: `2026-08-23`

### Операційне визначення

Гравець постійно призначає мешканців до військової групи, задає її спорядження й розклад тренувань, а потім активує груповий наказ.

### Включає

Загони, уніформу, місячні розклади, тренування й накази зайняти позицію, патрулювати, убити або захищати у Dwarf Fortress.

### Виключає

Безпосереднє керування одним бійцем; цивільні робочі спеціалізації; автоматичний вибір цілі.

### Ігри-носії

- [`GAME-0126` — Dwarf Fortress](../games/a-f/dwarf-fortress.md)

## ACT-154

- Назва: Призначити мешканця на адміністративну або шляхетну посаду
- Переглянуто: `2026-08-23`

### Операційне визначення

Гравець призначає допустимого мешканця на постійну посаду, яка відкриває адміністративну працю або створює оголошені інституційні вимоги.

### Включає

Призначення менеджера, брокера, рахівника або командира ополчення у Dwarf Fortress і виділення кімнат, потрібних посаді.

### Виключає

Призначення однієї роботи майстерні; спадкове призначення, що відбувається лише в симуляції; вибір трудового вподобання.

### Ігри-носії

- [`GAME-0126` — Dwarf Fortress](../games/a-f/dwarf-fortress.md)

## ACT-155

- Назва: Призначити дозволену область і особисту політику колонії
- Переглянуто: `2026-08-23`

### Операційне визначення

Гравець постійно призначає одному автономному мешканцеві просторову дозволену область і одну чи кілька оголошених політик споживання, лікування або спорядження.

### Включає

Дозволені області RimWorld разом із політиками їжі, речовин, одягу й медикаментів.

### Виключає

Один негайний наказ руху; пріоритет категорії робіт; тимчасовий наказ після мобілізації.

### Ігри-носії

- [`GAME-0127` — RimWorld](../games/m-r/rimworld.md)

## ACT-156

- Назва: Мобілізувати мешканця й віддати точний тактичний наказ
- Переглянуто: `2026-08-23`

### Операційне визначення

Гравець тимчасово призупиняє звичайну працю одного автономного мешканця й безпосередньо наказує точне пересування, вибір цілі або бойові дії в реальному часі.

### Включає

Мобілізацію поселенців RimWorld, їх розташування та накази атакувати, рятувати, заарештовувати або лікувати в польових умовах.

### Виключає

Постійні пріоритети робіт; автономний бій із ворогами поблизу; політику загону.

### Ігри-носії

- [`GAME-0127` — RimWorld](../games/m-r/rimworld.md)

## ACT-157

- Назва: Сформувати й прокласти маршрут завантаженому світовому каравану
- Переглянуто: `2026-08-24`

### Операційне визначення

Гравець вибирає людей, тварин і вантаж для мандрівної групи, підтверджує її формування, а потім вибирає досяжні пункти призначення на мапі світу.

### Включає

Склад каравану RimWorld, припаси, в’ючних тварин і накази маршруту.

### Виключає

Локальне завдання перевезення; торговця, що прибуває; необмежену телепортацію.

### Ігри-носії

- [`GAME-0130` — Frostpunk](../games/a-f/frostpunk.md)
- [`GAME-0127` — RimWorld](../games/m-r/rimworld.md)

## ACT-158

- Назва: Налаштувати політику взаємодії з полоненим
- Переглянуто: `2026-08-23`

### Операційне визначення

Гравець призначає постійну мету поводження з полоненим і налаштування догляду, щоб допустимі наглядачі намагалися звільнити його, знизити опір або завербувати.

### Включає

Режими взаємодії з полоненими й політику медикаментів у RimWorld.

### Виключає

Один арешт у бою; придбання завербованого персонажа; автоматичне зростання населення.

### Ігри-носії

- [`GAME-0127` — RimWorld](../games/m-r/rimworld.md)

## ACT-159

- Назва: Націлитися на досяжну ділянку рельєфу та зруйнувати її
- Переглянуто: `2026-08-24`

### Операційне визначення

Гравець наводиться на одну досяжну змінювану ділянку рельєфу й утримує команду руйнування, щоб рукою або поточним інструментом прибрати блок, стіну чи встановлений об’єкт.

### Включає

Руйнування блока дерева чи каменю в режимі Survival Minecraft; видобування блока переднього плану, руйнування стіни заднього плану або повернення встановлених меблів до інвентарю в Terraria.

### Виключає

Установлення фабричного об’єкта; переміщення вільного предмета; зафарбовування абстрактної комірки поля без вимоги фізичної досяжності.

### Ігри-носії

- [`GAME-0129` — Minecraft](../games/m-r/minecraft.md)
- [`GAME-0153` — Terraria](../games/s-z/terraria.md)

## ACT-160

- Назва: Викладати матеріали з інвентарю в сітці виготовлення
- Переглянуто: `2026-08-24`

### Операційне визначення

Гравець розміщує матеріали з інвентарю в певних комірках доступної сітки й забирає готовий предмет, коли типи, кількість і просторове розташування матеріалів точно відповідають відомому рецепту.

### Включає

Рецепти в сітці інвентарю 2 × 2 та на верстаку 3 × 3 у Minecraft.

### Виключає

Вибір рецепта ручного виготовлення в черзі; поєднання двох довільних предметів у руках; призначення рецепта автономній машині.

### Ігри-носії

- [`GAME-0129` — Minecraft](../games/m-r/minecraft.md)

## ACT-161

- Назва: Прицілитися й атакувати досяжну ціль поточною зброєю
- Переглянуто: `2026-09-08`

### Операційне визначення

Гравець наводить споряджену зброю ближнього або дальнього бою на досяжного ворога чи на об'єкт світу, який можна зламати, й сам завдає удару чи виконує постріл, а не віддає наказ автономному загону й не вибирає абстрактну ціль картки.

### Включає

Атаки проти ворожих мобів і Ender Dragon у режимі Survival Minecraft; прицільні атаки зброєю та спорядженням у Counter-Strike 2; прицільні атаки вогнепальною й холодною зброєю в Cyberpunk 2077; основні атаки героїв у Marvel Rivals; прицільні удари Needle у Hollow Knight: Silksong; атаки по монстру або певній частині його тіла в Monster Hunter Wilds; атаки зброєю проти видимих досяжних ворогів у Baldur’s Gate 3; постріли й удари піхоти по ворогах у Battlefield 6; удари й постріли по істотах та Eye of Cthulhu у Terraria; удари ломом по маршрутному склу в Half-Life (1998); удари зброєю по перекритих дверях кімнати Collector у Dead Cells.

### Виключає

Автоматичний вогонь турелі; покрокову картку здібності; групову маршрутну точку, після якої бійці самі знаходять цілі; контекстну взаємодію з об'єктом оточення (ACT-341); міцність і руйнування самого об'єкта, які належать SYS-755.

### Ігри-носії

- [`GAME-0233` — 7 Days to Die](../games/0-9/7-days-to-die.md)
- [`GAME-0223` — Aion Classic](../games/a-f/aion-classic.md)
- [`GAME-0154` — Apex Legends](../games/a-f/apex-legends.md)
- [`GAME-0143` — ARC Raiders](../games/a-f/arc-raiders.md)
- [`GAME-0312` — ASTRO BOT](../games/a-f/astro-bot.md)
- [`GAME-0148` — Baldur’s Gate 3](../games/a-f/baldurs-gate-3.md)
- [`GAME-0386` — Banjo-Kazooie](../games/a-f/banjo-kazooie.md)
- [`GAME-0255` — "Batman: Arkham Asylum Game of the Year Edition"](../games/a-f/batman-arkham-asylum-game-of-the-year-edition.md)
- [`GAME-0234` — Battlefield 2042](../games/a-f/battlefield-2042.md)
- [`GAME-0149` — Battlefield 6](../games/a-f/battlefield-6.md)
- [`GAME-0243` — Battlefield Hardline](../games/a-f/battlefield-hardline.md)
- [`GAME-0220` — Battlefield V](../games/a-f/battlefield-v.md)
- [`GAME-0256` — "BioShock™ Remastered"](../games/a-f/bioshock-remastered.md)
- [`GAME-0189` — "Black Myth: Wukong"](../games/a-f/black-myth-wukong.md)
- [`GAME-0308` — Bloodborne™](../games/a-f/bloodborne.md)
- [`GAME-0222` — "Call of Juarez: Gunslinger"](../games/a-f/call-of-juarez-gunslinger.md)
- [`GAME-0347` — "Castlevania: Symphony of the Night"](../games/a-f/castlevania-symphony-of-the-night.md)
- [`GAME-0144` — Clair Obscur: Expedition 33](../games/a-f/clair-obscur-expedition-33.md)
- [`GAME-0324` — Contra Force](../games/a-f/contra-force.md)
- [`GAME-0254` — CONTROL Ultimate Edition](../games/a-f/control-ultimate-edition.md)
- [`GAME-0137` — Counter-Strike 2](../games/a-f/counter-strike-2.md)
- [`GAME-0218` — Counter-Strike](../games/a-f/counter-strike.md)
- [`GAME-0359` — "Crimson Skies: High Road to Revenge"](../games/a-f/crimson-skies-high-road-to-revenge.md)
- [`GAME-0246` — Crysis Remastered](../games/a-f/crysis-remastered.md)
- [`GAME-0277` — Cuphead](../games/a-f/cuphead.md)
- [`GAME-0146` — Cyberpunk 2077](../games/a-f/cyberpunk-2077.md)
- [`GAME-0262` — DARK SOULS™ III](../games/a-f/dark-souls-iii.md)
- [`GAME-0295` — DARK SOULS™: REMASTERED](../games/a-f/dark-souls-remastered.md)
- [`GAME-0210` — DayZ](../games/a-f/dayz.md)
- [`GAME-0282` — Dead Cells](../games/a-f/dead-cells.md)
- [`GAME-0368` — Dead Rising](../games/a-f/dead-rising.md)
- [`GAME-0259` — "Dead Space (2023 remake)"](../games/a-f/dead-space-2023.md)
- [`GAME-0266` — Deep Rock Galactic](../games/a-f/deep-rock-galactic.md)
- [`GAME-0200` — Delta Force](../games/a-f/delta-force.md)
- [`GAME-0193` — Destiny 2](../games/a-f/destiny-2.md)
- [`GAME-0353` — "Deus Ex: Game of the Year Edition"](../games/a-f/deus-ex-game-of-the-year-edition.md)
- [`GAME-0322` — "Diablo II: Resurrected"](../games/a-f/diablo-ii-resurrected.md)
- [`GAME-0247` — Dishonored (2012)](../games/a-f/dishonored-2012.md)
- [`GAME-0186` — "Don’t Starve Together"](../games/a-f/dont-starve-together.md)
- [`GAME-0352` — DOOM (1993)](../games/a-f/doom-1993.md)
- [`GAME-0245` — DOOM (2016)](../games/a-f/doom-2016.md)
- [`GAME-0286` — DOOM Eternal](../games/a-f/doom-eternal.md)
- [`GAME-0131` — Dyson Sphere Program](../games/a-f/dyson-sphere-program.md)
- [`GAME-0152` — Elden Ring](../games/a-f/elden-ring.md)
- [`GAME-0327` — Fable](../games/a-f/fable.md)
- [`GAME-0231` — Fallout 4](../games/a-f/fallout-4.md)
- [`GAME-0361` — Fallout: New Vegas](../games/a-f/fallout-new-vegas.md)
- [`GAME-0236` — Far Cry 3](../games/a-f/far-cry-3.md)
- [`GAME-0271` — Far Cry 5](../games/a-f/far-cry-5.md)
- [`GAME-0188` — FINAL FANTASY XIV Online](../games/a-f/final-fantasy-xiv-online.md)
- [`GAME-0227` — Fortnite](../games/a-f/fortnite.md)
- [`GAME-0321` — Gears of War](../games/g-l/gears-of-war.md)
- [`GAME-0263` — God of War](../games/g-l/god-of-war.md)
- [`GAME-0381` — GoldenEye 007](../games/g-l/goldeneye-007.md)
- [`GAME-0145` — Grand Theft Auto V](../games/g-l/grand-theft-auto-v.md)
- [`GAME-0314` — Grounded](../games/g-l/grounded.md)
- [`GAME-0251` — Hades](../games/g-l/hades.md)
- [`GAME-0239` — Half-Life (1998)](../games/g-l/half-life-1998.md)
- [`GAME-0212` — Half-Life 2](../games/g-l/half-life-2.md)
- [`GAME-0315` — Halo 3](../games/g-l/halo-3.md)
- [`GAME-0340` — "Halo: Combat Evolved Anniversary"](../games/g-l/halo-combat-evolved-anniversary.md)
- [`GAME-0159` — Helldivers 2](../games/g-l/helldivers-2.md)
- [`GAME-0248` — HITMAN World of Assassination](../games/g-l/hitman-world-of-assassination.md)
- [`GAME-0150` — "Hollow Knight: Silksong"](../games/g-l/hollow-knight-silksong.md)
- [`GAME-0274` — Hollow Knight](../games/g-l/hollow-knight.md)
- [`GAME-0192` — Left 4 Dead 2](../games/g-l/left-4-dead-2.md)
- [`GAME-0290` — Lies of P](../games/g-l/lies-of-p.md)
- [`GAME-0219` — Lineage II](../games/g-l/lineage-ii.md)
- [`GAME-0147` — Marvel Rivals](../games/m-r/marvel-rivals.md)
- [`GAME-0323` — "Marvel’s Spider-Man 2"](../games/m-r/marvels-spider-man-2.md)
- [`GAME-0367` — Mass Effect 2 (Legendary Edition)](../games/m-r/mass-effect-2-legendary-edition.md)
- [`GAME-0238` — "Max Payne (2001)"](../games/m-r/max-payne-2001.md)
- [`GAME-0273` — Max Payne 3](../games/m-r/max-payne-3.md)
- [`GAME-0389` — Mega Man 2](../games/m-r/mega-man-2.md)
- [`GAME-0306` — METAL GEAR SOLID V: THE PHANTOM PAIN](../games/m-r/metal-gear-solid-v-the-phantom-pain.md)
- [`GAME-0339` — Metal Gear Solid](../games/m-r/metal-gear-solid.md)
- [`GAME-0260` — Metro Exodus](../games/m-r/metro-exodus.md)
- [`GAME-0355` — Metroid Prime](../games/m-r/metroid-prime.md)
- [`GAME-0129` — Minecraft](../games/m-r/minecraft.md)
- [`GAME-0297` — 'MONSTER HUNTER RISE'](../games/m-r/monster-hunter-rise.md)
- [`GAME-0151` — Monster Hunter Wilds](../games/m-r/monster-hunter-wilds.md)
- [`GAME-0207` — 'Monster Hunter: World'](../games/m-r/monster-hunter-world.md)
- [`GAME-0194` — "Mount & Blade II: Bannerlord"](../games/m-r/mount-and-blade-ii-bannerlord.md)
- [`GAME-0202` — "NARAKA: BLADEPOINT"](../games/m-r/naraka-bladepoint.md)
- [`GAME-0341` — "Ninja Gaiden Black"](../games/m-r/ninja-gaiden-black.md)
- [`GAME-0299` — Nioh 2](../games/m-r/nioh-2.md)
- [`GAME-0296` — Noita](../games/m-r/noita.md)
- [`GAME-0382` — Ōkami HD](../games/m-r/okami-hd.md)
- [`GAME-0224` — Once Human](../games/m-r/once-human.md)
- [`GAME-0293` — Ori and the Will of the Wisps](../games/m-r/ori-and-the-will-of-the-wisps.md)
- [`GAME-0181` — Overwatch](../games/m-r/overwatch.md)
- [`GAME-0139` — Palworld](../games/m-r/palworld.md)
- [`GAME-0162` — Path of Exile 2](../games/m-r/path-of-exile-2.md)
- [`GAME-0201` — PAYDAY 2](../games/m-r/payday-2.md)
- [`GAME-0232` — PAYDAY 3](../games/m-r/payday-3.md)
- [`GAME-0291` — Persona 5 Royal](../games/m-r/persona-5-royal.md)
- [`GAME-0258` — "Prey (2017)"](../games/m-r/prey-2017.md)
- [`GAME-0344` — "Prince of Persia: The Sands of Time"](../games/m-r/prince-of-persia-the-sands-of-time.md)
- [`GAME-0142` — Project Zomboid](../games/m-r/project-zomboid.md)
- [`GAME-0358` — Psychonauts](../games/m-r/psychonauts.md)
- [`GAME-0140` — "PUBG: BATTLEGROUNDS"](../games/m-r/pubg-battlegrounds.md)
- [`GAME-0334` — Quake](../games/m-r/quake.md)
- [`GAME-0165` — Red Dead Redemption 2](../games/m-r/red-dead-redemption-2.md)
- [`GAME-0280` — Resident Evil 2 (2019 remake)](../games/m-r/resident-evil-2-2019.md)
- [`GAME-0249` — Resident Evil 4 (2023 remake)](../games/m-r/resident-evil-4-2023.md)
- [`GAME-0348` — "Resident Evil: Director’s Cut"](../games/m-r/resident-evil-directors-cut.md)
- [`GAME-0141` — Rust](../games/m-r/rust.md)
- [`GAME-0288` — "Sekiro™: Shadows Die Twice - GOTY Edition"](../games/s-z/sekiro-shadows-die-twice.md)
- [`GAME-0272` — Serious Sam 4](../games/s-z/serious-sam-4.md)
- [`GAME-0237` — "Serious Sam HD: The First Encounter"](../games/s-z/serious-sam-hd-the-first-encounter.md)
- [`GAME-0356` — Shadow of the Colossus](../games/s-z/shadow-of-the-colossus.md)
- [`GAME-0303` — Sifu](../games/s-z/sifu.md)
- [`GAME-0330` — Silent Hill 2 (2024 remake)](../games/s-z/silent-hill-2-2024.md)
- [`GAME-0360` — "Space Invaders"](../games/s-z/space-invaders.md)
- [`GAME-0157` — Split Fiction](../games/s-z/split-fiction.md)
- [`GAME-0170` — "S.T.A.L.K.E.R. 2: Heart of Chornobyl"](../games/s-z/stalker-2-heart-of-chornobyl.md)
- [`GAME-0230` — "STAR WARS Battlefront II (2017)"](../games/s-z/star-wars-battlefront-ii-2017.md)
- [`GAME-0213` — "STAR WARS Jedi: Fallen Order"](../games/s-z/star-wars-jedi-fallen-order.md)
- [`GAME-0225` — "STAR WARS: Squadrons"](../games/s-z/star-wars-squadrons.md)
- [`GAME-0331` — Starfield](../games/s-z/starfield.md)
- [`GAME-0311` — Super Mario Bros.](../games/s-z/super-mario-bros.md)
- [`GAME-0337` — Super Metroid](../games/s-z/super-metroid.md)
- [`GAME-0313` — Tank 1990](../games/s-z/tank-1990.md)
- [`GAME-0187` — Team Fortress 2](../games/s-z/team-fortress-2.md)
- [`GAME-0153` — Terraria](../games/s-z/terraria.md)
- [`GAME-0164` — "The Binding of Isaac: Rebirth"](../games/s-z/the-binding-of-isaac-rebirth.md)
- [`GAME-0190` — "The Elder Scrolls V: Skyrim Special Edition"](../games/s-z/the-elder-scrolls-v-skyrim-special-edition.md)
- [`GAME-0292` — The Forest](../games/s-z/the-forest.md)
- [`GAME-0261` — The Last of Us Part I](../games/s-z/the-last-of-us-part-i.md)
- [`GAME-0395` — "The Legend of Zelda: Majora’s Mask"](../games/s-z/the-legend-of-zelda-majoras-mask.md)
- [`GAME-0363` — "The Legend of Zelda: Ocarina of Time"](../games/s-z/the-legend-of-zelda-ocarina-of-time.md)
- [`GAME-0325` — The Legend of Zelda](../games/s-z/the-legend-of-zelda.md)
- [`GAME-0205` — "The Witcher 3: Wild Hunt"](../games/s-z/the-witcher-3-wild-hunt.md)
- [`GAME-0253` — "Titanfall 2"](../games/s-z/titanfall-2.md)
- [`GAME-0174` — Tom Clancy’s Rainbow Six Siege](../games/s-z/tom-clancys-rainbow-six-siege.md)
- [`GAME-0349` — "Tom Clancy’s Splinter Cell"](../games/s-z/tom-clancys-splinter-cell.md)
- [`GAME-0250` — Tomb Raider (2013)](../games/s-z/tomb-raider-2013.md)
- [`GAME-0294` — V Rising](../games/s-z/v-rising.md)
- [`GAME-0197` — Valheim](../games/s-z/valheim.md)
- [`GAME-0184` — War Thunder](../games/s-z/war-thunder.md)
- [`GAME-0168` — Warframe](../games/s-z/warframe.md)
- [`GAME-0211` — World of Tanks](../games/s-z/world-of-tanks.md)
- [`GAME-0221` — World of Warcraft](../games/s-z/world-of-warcraft.md)

## ACT-162

- Назва: Установити предмет з інвентарю в досяжній комірці світу
- Переглянуто: `2026-08-24`

### Операційне визначення

Гравець наводиться на досяжну опору й використовує один блок, стіну чи інший предмет з інвентарю, щоб установити його в сумісній комірці плиткового світу або на площі, що відповідає правилам цього предмета.

### Включає

Установлення блоків для укриття, мостів або сходів у режимі Survival Minecraft; установлення блоків, стін заднього плану, платформ, смолоскипів або меблів у Terraria.

### Виключає

Руйнування блока; установлення фабричної споруди з окремою займаною площею; необмежене редагування в режимі Creative.

### Ігри-носії

- [`GAME-0129` — Minecraft](../games/m-r/minecraft.md)
- [`GAME-0153` — Terraria](../games/s-z/terraria.md)

## ACT-163

- Назва: Кинути предмет-покажчик, щоб визначити напрямок у світі
- Переглянуто: `2026-08-24`

### Операційне визначення

Гравець використовує один витратний предмет-покажчик: той залишає руку й летить у напрямку найближчої відповідної прихованої цілі в ігровому світі.

### Включає

Кидання Eye of Ender у Minecraft для пошуку найближчої фортеці.

### Виключає

Читання статичної мапи; постріл снарядом, що завдає шкоди; телепортацію до цілі.

### Ігри-носії

- [`GAME-0129` — Minecraft](../games/m-r/minecraft.md)

## ACT-164

- Назва: Вибрати активний предмет, зброю або пристрій
- Переглянуто: `2026-08-24`

### Операційне визначення

Гравець вибирає зайняте місце швидкого доступу, і предмет, інструмент, зброя чи пристрій із нього стає готовим до наступної відповідної дії у світі.

### Включає

Вибір кирки, їжі, блока, Eye of Ender або Flint and Steel на панелі швидкого доступу Minecraft; перемикання між зброєю, гранатами, ножем і C4 у Counter-Strike 2; перемикання зброї в Cyberpunk 2077; вибір зброї або класового пристрою в Battlefield 6; вибір інструмента, зброї, блока, смолоскипа чи зілля на панелі швидкого доступу Terraria.

### Виключає

Переставляння складників рецепта; призначення інструмента автономному працівникові.

### Ігри-носії

- [`GAME-0233` — 7 Days to Die](../games/0-9/7-days-to-die.md)
- [`GAME-0257` — "Alien: Isolation"](../games/a-f/alien-isolation.md)
- [`GAME-0154` — Apex Legends](../games/a-f/apex-legends.md)
- [`GAME-0143` — ARC Raiders](../games/a-f/arc-raiders.md)
- [`GAME-0234` — Battlefield 2042](../games/a-f/battlefield-2042.md)
- [`GAME-0149` — Battlefield 6](../games/a-f/battlefield-6.md)
- [`GAME-0243` — Battlefield Hardline](../games/a-f/battlefield-hardline.md)
- [`GAME-0220` — Battlefield V](../games/a-f/battlefield-v.md)
- [`GAME-0256` — "BioShock™ Remastered"](../games/a-f/bioshock-remastered.md)
- [`GAME-0222` — "Call of Juarez: Gunslinger"](../games/a-f/call-of-juarez-gunslinger.md)
- [`GAME-0137` — Counter-Strike 2](../games/a-f/counter-strike-2.md)
- [`GAME-0218` — Counter-Strike](../games/a-f/counter-strike.md)
- [`GAME-0246` — Crysis Remastered](../games/a-f/crysis-remastered.md)
- [`GAME-0146` — Cyberpunk 2077](../games/a-f/cyberpunk-2077.md)
- [`GAME-0210` — DayZ](../games/a-f/dayz.md)
- [`GAME-0368` — Dead Rising](../games/a-f/dead-rising.md)
- [`GAME-0259` — "Dead Space (2023 remake)"](../games/a-f/dead-space-2023.md)
- [`GAME-0200` — Delta Force](../games/a-f/delta-force.md)
- [`GAME-0193` — Destiny 2](../games/a-f/destiny-2.md)
- [`GAME-0353` — "Deus Ex: Game of the Year Edition"](../games/a-f/deus-ex-game-of-the-year-edition.md)
- [`GAME-0247` — Dishonored (2012)](../games/a-f/dishonored-2012.md)
- [`GAME-0186` — "Don’t Starve Together"](../games/a-f/dont-starve-together.md)
- [`GAME-0352` — DOOM (1993)](../games/a-f/doom-1993.md)
- [`GAME-0245` — DOOM (2016)](../games/a-f/doom-2016.md)
- [`GAME-0286` — DOOM Eternal](../games/a-f/doom-eternal.md)
- [`GAME-0361` — Fallout: New Vegas](../games/a-f/fallout-new-vegas.md)
- [`GAME-0236` — Far Cry 3](../games/a-f/far-cry-3.md)
- [`GAME-0227` — Fortnite](../games/a-f/fortnite.md)
- [`GAME-0321` — Gears of War](../games/g-l/gears-of-war.md)
- [`GAME-0381` — GoldenEye 007](../games/g-l/goldeneye-007.md)
- [`GAME-0145` — Grand Theft Auto V](../games/g-l/grand-theft-auto-v.md)
- [`GAME-0239` — Half-Life (1998)](../games/g-l/half-life-1998.md)
- [`GAME-0212` — Half-Life 2](../games/g-l/half-life-2.md)
- [`GAME-0315` — Halo 3](../games/g-l/halo-3.md)
- [`GAME-0340` — "Halo: Combat Evolved Anniversary"](../games/g-l/halo-combat-evolved-anniversary.md)
- [`GAME-0159` — Helldivers 2](../games/g-l/helldivers-2.md)
- [`GAME-0248` — HITMAN World of Assassination](../games/g-l/hitman-world-of-assassination.md)
- [`GAME-0192` — Left 4 Dead 2](../games/g-l/left-4-dead-2.md)
- [`GAME-0367` — Mass Effect 2 (Legendary Edition)](../games/m-r/mass-effect-2-legendary-edition.md)
- [`GAME-0238` — "Max Payne (2001)"](../games/m-r/max-payne-2001.md)
- [`GAME-0273` — Max Payne 3](../games/m-r/max-payne-3.md)
- [`GAME-0306` — METAL GEAR SOLID V: THE PHANTOM PAIN](../games/m-r/metal-gear-solid-v-the-phantom-pain.md)
- [`GAME-0260` — Metro Exodus](../games/m-r/metro-exodus.md)
- [`GAME-0129` — Minecraft](../games/m-r/minecraft.md)
- [`GAME-0202` — "NARAKA: BLADEPOINT"](../games/m-r/naraka-bladepoint.md)
- [`GAME-0296` — Noita](../games/m-r/noita.md)
- [`GAME-0181` — Overwatch](../games/m-r/overwatch.md)
- [`GAME-0139` — Palworld](../games/m-r/palworld.md)
- [`GAME-0201` — PAYDAY 2](../games/m-r/payday-2.md)
- [`GAME-0232` — PAYDAY 3](../games/m-r/payday-3.md)
- [`GAME-0203` — "PEAK"](../games/m-r/peak.md)
- [`GAME-0160` — "Pokémon Legends: Z-A"](../games/m-r/pokemon-legends-z-a.md)
- [`GAME-0258` — "Prey (2017)"](../games/m-r/prey-2017.md)
- [`GAME-0142` — Project Zomboid](../games/m-r/project-zomboid.md)
- [`GAME-0140` — "PUBG: BATTLEGROUNDS"](../games/m-r/pubg-battlegrounds.md)
- [`GAME-0334` — Quake](../games/m-r/quake.md)
- [`GAME-0165` — Red Dead Redemption 2](../games/m-r/red-dead-redemption-2.md)
- [`GAME-0249` — Resident Evil 4 (2023 remake)](../games/m-r/resident-evil-4-2023.md)
- [`GAME-0141` — Rust](../games/m-r/rust.md)
- [`GAME-0272` — Serious Sam 4](../games/s-z/serious-sam-4.md)
- [`GAME-0237` — "Serious Sam HD: The First Encounter"](../games/s-z/serious-sam-hd-the-first-encounter.md)
- [`GAME-0307` — Slime Rancher](../games/s-z/slime-rancher.md)
- [`GAME-0170` — "S.T.A.L.K.E.R. 2: Heart of Chornobyl"](../games/s-z/stalker-2-heart-of-chornobyl.md)
- [`GAME-0178` — Subnautica](../games/s-z/subnautica.md)
- [`GAME-0337` — Super Metroid](../games/s-z/super-metroid.md)
- [`GAME-0187` — Team Fortress 2](../games/s-z/team-fortress-2.md)
- [`GAME-0153` — Terraria](../games/s-z/terraria.md)
- [`GAME-0261` — The Last of Us Part I](../games/s-z/the-last-of-us-part-i.md)
- [`GAME-0363` — "The Legend of Zelda: Ocarina of Time"](../games/s-z/the-legend-of-zelda-ocarina-of-time.md)
- [`GAME-0325` — The Legend of Zelda](../games/s-z/the-legend-of-zelda.md)
- [`GAME-0285` — "The Long Dark"](../games/s-z/the-long-dark.md)
- [`GAME-0253` — "Titanfall 2"](../games/s-z/titanfall-2.md)
- [`GAME-0174` — Tom Clancy’s Rainbow Six Siege](../games/s-z/tom-clancys-rainbow-six-siege.md)
- [`GAME-0250` — Tomb Raider (2013)](../games/s-z/tomb-raider-2013.md)
- [`GAME-0294` — V Rising](../games/s-z/v-rising.md)
- [`GAME-0197` — Valheim](../games/s-z/valheim.md)
- [`GAME-0168` — Warframe](../games/s-z/warframe.md)

## ACT-165

- Назва: З’їсти придатну їжу, щоб відновити відповідний стан
- Переглянуто: `2026-08-24`

### Операційне визначення

Гравець застосовує харчовий предмет, витрачає одну одиницю та поповнює передбачені цим предметом показники голоду, калорій, насичення, води чи здоров’я.

### Включає

Споживання їжі в режимі Survival Minecraft і придатної їжі в Rust.

### Виключає

Використання суто лікувального предмета; автоматичне годування автономного персонажа; виготовлення їжі.

### Ігри-носії

- [`GAME-0210` — DayZ](../games/a-f/dayz.md)
- [`GAME-0186` — "Don’t Starve Together"](../games/a-f/dont-starve-together.md)
- [`GAME-0240` — "Kingdom Come: Deliverance II"](../games/g-l/kingdom-come-deliverance-ii.md)
- [`GAME-0129` — Minecraft](../games/m-r/minecraft.md)
- [`GAME-0139` — Palworld](../games/m-r/palworld.md)
- [`GAME-0203` — "PEAK"](../games/m-r/peak.md)
- [`GAME-0142` — Project Zomboid](../games/m-r/project-zomboid.md)
- [`GAME-0141` — Rust](../games/m-r/rust.md)
- [`GAME-0178` — Subnautica](../games/s-z/subnautica.md)
- [`GAME-0285` — "The Long Dark"](../games/s-z/the-long-dark.md)

## ACT-166

- Назва: Налаштувати робочу зміну й відкриту здатність споруди
- Переглянуто: `2026-08-24`

### Операційне визначення

Гравець вмикає або вимикає споруду з працівниками, вибирає режим робочої зміни чи застосовує робочу здатність, відкриту законом або технологією.

### Включає

Увімкнення й вимкнення робочого місця у Frostpunk, вибір звичайної, подовженої або аварійної зміни та перемикання обігрівача чи здатності «Наглядач».

### Виключає

Призначення працівників; вибір виробничого рецепта; зміну швидкості симуляції всього міста.

### Ігри-носії

- [`GAME-0130` — Frostpunk](../games/a-f/frostpunk.md)
- [`GAME-0136` — "Surviving Mars: Relaunched"](../games/s-z/surviving-mars.md)

## ACT-167

- Назва: Підписати доступний незворотний закон
- Переглянуто: `2026-08-24`

### Операційне визначення

Гравець обирає доступний вузол у книзі законів, назавжди вводить у дію його правило та приймає всі наслідки для подальших гілок.

### Включає

Закони Адаптації у Frostpunk і взаємовиключний вибір між шляхами Порядку й Віри.

### Виключає

Зворотну політику району; вибір дослідження колонії; одну тимчасову відповідь на подію.

### Ігри-носії

- [`GAME-0130` — Frostpunk](../games/a-f/frostpunk.md)

## ACT-168

- Назва: Налаштувати режим генератора або місцевого джерела тепла
- Переглянуто: `2026-08-24`

### Операційне визначення

Гравець вмикає чи вимикає центральний генератор або окреме місцеве джерело тепла, вибирає його потужність чи тимчасовий режим із підвищеним ризиком.

### Включає

Увімкнення генератора Frostpunk, вибір його потужності й радіуса, форсований режим, розклад парового вузла та керування обігрівачами робочих місць.

### Виключає

Дослідження поліпшення опалення; розміщення споруди; призначення персоналу.

### Ігри-носії

- [`GAME-0130` — Frostpunk](../games/a-f/frostpunk.md)

## ACT-169

- Назва: Планувати орбітальний рій або мегаструктуру навколо зорі
- Переглянуто: `2026-08-24`

### Операційне визначення

Гравець створює або змінює збережений план орбітального будівництва: обирає зорю, шар чи орбіту й розміщує вузли, каркаси та ділянки оболонки, які згодом мають збудувати пускові системи.

### Включає

Налаштування орбіт рою Дайсона та креслення шарів, вузлів, каркасів і ділянок оболонки сфери Дайсона у Dyson Sphere Program.

### Виключає

Розміщення окремої споруди планетарної фабрики; запуск забезпеченої матеріалами ракети; застосування креслення поверхневої фабрики.

### Ігри-носії

- [`GAME-0131` — Dyson Sphere Program](../games/a-f/dyson-sphere-program.md)

## ACT-170

- Назва: Переводити меха в режим польоту, космічного плавання або викривлення простору
- Переглянуто: `2026-08-24`

### Операційне визначення

Гравець переводить безпосередньо керованого меха з наземного руху у відкритий режим польоту або під час керування в космосі вмикає викривлення простору, витрачаючи один викривлювач.

### Включає

Зліт Ікара, планетарний політ, космічне плавання між планетами й увімкнення викривлення простору у Dyson Sphere Program.

### Виключає

Вибір пункту призначення автономного логістичного судна; телепортацію між мапами; звичайне пересування поверхнею.

### Ігри-носії

- [`GAME-0131` — Dyson Sphere Program](../games/a-f/dyson-sphere-program.md)

## ACT-171

- Назва: Створити циклічний корабельний торговельний маршрут із вантажними наказами для кожного порту
- Переглянуто: `2026-08-24`

### Операційне визначення

Гравець створює або змінює постійний упорядкований цикл острівних портів для одного чи кількох кораблів і для кожної вантажної комірки задає товар та кількість, яку слід завантажити або вивантажити на кожній зупинці.

### Включає

Торговельні маршрути Anno 1800 з упорядкованими портами й окремими наказами для вантажних комірок, зокрема завантаженням із дотриманням мінімального запасу на острові.

### Виключає

Ручне переміщення одного стосу товару в порту; вибір складу місцевими возами; прокладання дороги; пару станцій, яку система самостійно поєднує відповідно до попиту.

### Ігри-носії

- [`GAME-0132` — Anno 1800](../games/a-f/anno-1800.md)

## ACT-172

- Назва: Підвищити готову оселю до наступного рівня населення
- Переглянуто: `2026-08-24`

### Операційне визначення

Гравець вибирає повністю заселену оселю із задоволеними базовими потребами й витрачає потрібні будівельні матеріали, щоб перетворити її на оселю наступної верстви населення.

### Включає

Послідовне підвищення осель у Anno 1800: від фермерів до робітників, ремісників, інженерів та інвесторів.

### Виключає

Автоматичне збільшення кількості мешканців у межах однієї верстви; будівництво нової оселі; відкриття споруд після досягнення порога населення.

### Ігри-носії

- [`GAME-0132` — Anno 1800](../games/a-f/anno-1800.md)

## ACT-173

- Назва: Замінити газетну статтю пропагандою
- Переглянуто: `2026-08-24`

### Операційне визначення

До публікації гравець вибирає створену системою газетну статтю й витрачає вплив, щоб замінити її одним із доступних пропагандистських матеріалів.

### Включає

Редагування випуску газети в Anno 1800, яке до наступного випуску змінює споживання, щастя або дохід населення.

### Виключає

Вибір постійного громадського закону; зміну вже опублікованої статті; сюжетну відповідь у діалозі без наслідків для симуляції.

### Ігри-носії

- [`GAME-0132` — Anno 1800](../games/a-f/anno-1800.md)

## ACT-174

- Назва: Спорядити корабель для експедиції та вирушити
- Переглянуто: `2026-08-24`

### Операційне визначення

Гравець призначає придатний корабель і заповнює його обмежені вантажні комірки товарами або фахівцями, чиї навички й припаси допомагатимуть під час оголошеної експедиції, а потім підтверджує відплиття.

### Включає

Підготовку обов’язкової експедиції Anno 1800 для відкриття Нового світу.

### Виключає

Створення повторюваного торговельного маршруту; ручне керування кораблем; вибір відповіді в подальшій події експедиції.

### Ігри-носії

- [`GAME-0132` — Anno 1800](../games/a-f/anno-1800.md)

## ACT-175

- Назва: Відкрити споруду за очки науки
- Переглянуто: `2026-08-24`

### Операційне визначення

Гравець витрачає накопичені поселенням очки науки на доступний запис каталогу й назавжди відкриває цю споруду на поточній мапі.

### Включає

Відкриття споруд і «Рекультиватора Землі» у Timberborn.

### Виключає

Вибір дослідження, яке ще треба виконати; умову чисельності населення; метапоступ, що зберігається між мапами.

### Ігри-носії

- [`GAME-0133` — Timberborn](../games/s-z/timberborn.md)

## ACT-176

- Назва: З’єднати й налаштувати автоматизацію
- Переглянуто: `2026-08-24`

### Операційне визначення

Гравець з’єднує вихід датчика, логічного елемента або ретранслятора із сумісною ціллю та задає сталі пороги чи логічні правила.

### Включає

Датчики Timberborn, що керують насосами, шлюзами або клапанами.

### Виключає

Ручне перемикання; вибір виробничого рецепта; приховану сценарну подію.

### Ігри-носії

- [`GAME-0133` — Timberborn](../games/s-z/timberborn.md)

## ACT-177

- Назва: Налаштувати зону, парк і вантажі диспетчерського осередку
- Переглянуто: `2026-08-24`

### Операційне визначення

Гравець задає постійному диспетчерському осередку територію роботи, доступну техніку, джерела, одержувачів, види вантажів або пороги запасів, після чого осередок самостійно відправляє придатний транспорт.

### Включає

Вежі керування шахтою в Captain of Industry, а також будівельні й розподільчі контори у Workers & Resources: Soviet Republic.

### Виключає

Редагування впорядкованих зупинок окремої транспортної лінії; розміщення самого диспетчерського осередку; безпосереднє керування доставленням.

### Ігри-носії

- [`GAME-0135` — "Captain of Industry"](../games/a-f/captain-of-industry.md)
- [`GAME-0134` — "Workers & Resources: Soviet Republic"](../games/s-z/workers-resources-soviet-republic.md)

## ACT-178

- Назва: Здійснити закордонну купівлю або налаштувати прикордонний обмін
- Переглянуто: `2026-08-24`

### Операційне визначення

Гравець витрачає рублі чи долари на імпортний транспортний засіб або налаштовує сумісне зовнішнє з’єднання на купівлю чи продаж електроенергії.

### Включає

Придбання транспорту на радянській митниці або митниці країн НАТО та налаштування зовнішньої лінії електропередачі на імпорт чи експорт.

### Виключає

Внутрішній виробничий рецепт; перетин митниці вантажем за вже створеною транспортною лінією; автоматичний податковий розрахунок.

### Ігри-носії

- [`GAME-0134` — "Workers & Resources: Soviet Republic"](../games/s-z/workers-resources-soviet-republic.md)

## ACT-179

- Назва: Укласти разову торговельну угоду або постійний контракт із селом
- Переглянуто: `2026-08-24`

### Операційне визначення

Гравець приймає пропозицію відкритого села й або негайно обмінює визначені товари, або запускає постійний обмін експорту на імпорт, кожен наступний рейс якого витрачає ресурс єдності.

### Включає

Разові обміни через торговельний причал і постійні контракти через вантажний термінал у Captain of Industry.

### Виключає

Внутрішні виробничі рецепти; автоматичні доставлення острівними вантажівками; зовнішню торгівлю через сухопутний кордон.

### Ігри-носії

- [`GAME-0135` — "Captain of Industry"](../games/a-f/captain-of-industry.md)

## ACT-180

- Назва: Добирати вантаж і відправляти марсіанську ракету
- Переглянуто: `2026-08-24`

### Операційне визначення

Гравець обирає доступну ракету й пункт призначення, заповнює її обмежену місткість ресурсами, збірними модулями, транспортом або колоністами та підтверджує запуск чи посадку; далі політ відбувається без ручного керування.

### Включає

Вантажні й пасажирські рейси, повернення на Землю та польоти до планетарних проєктів у Surviving Mars: Relaunched 1.0.7.

### Виключає

Налаштування повторюваного торговельного маршруту; безпосереднє пілотування космічного апарата; одноразовий запуск промислової ракети з незмінним вантажем.

### Ігри-носії

- [`GAME-0136` — "Surviving Mars: Relaunched"](../games/s-z/surviving-mars.md)

## ACT-181

- Назва: Готувати марсіанський закон, домовлятися про підтримку й проводити голосування
- Переглянуто: `2026-08-24`

### Операційне визначення

Гравець обирає доступний закон або один із його варіантів, готує пропозицію, може пообіцяти фракції поступку в обмін на підтримку та оголошує голосування, яке ухвалює або відхиляє нове правило колонії.

### Включає

Закони Земної ради й Марсіанської асамблеї в Surviving Mars: Relaunched, зокрема декларацію незалежності.

### Виключає

Одностороннє остаточне підписання закону без голосування; вибір технології для дослідження; одноразову відповідь у сюжетній події.

### Ігри-носії

- [`GAME-0136` — "Surviving Mars: Relaunched"](../games/s-z/surviving-mars.md)

## ACT-183

- Назва: Перезарядити активну магазинну зброю з резерву набоїв
- Переглянуто: `2026-08-24`

### Операційне визначення

Гравець витрачає час, щоб перенести набої з резерву до активної зброї та наповнити її магазин; під час цієї дії зброя тимчасово не готова стріляти.

### Включає

Ручне перезаряджання вогнепальної зброї в Counter-Strike 2, Cyberpunk 2077 і Battlefield 6.

### Виключає

Автоматичне поповнення боєприпасів між спробами; зміну активної зброї; постріл набоєм, що лишився в патроннику.

### Ігри-носії

- [`GAME-0154` — Apex Legends](../games/a-f/apex-legends.md)
- [`GAME-0234` — Battlefield 2042](../games/a-f/battlefield-2042.md)
- [`GAME-0149` — Battlefield 6](../games/a-f/battlefield-6.md)
- [`GAME-0243` — Battlefield Hardline](../games/a-f/battlefield-hardline.md)
- [`GAME-0220` — Battlefield V](../games/a-f/battlefield-v.md)
- [`GAME-0256` — "BioShock™ Remastered"](../games/a-f/bioshock-remastered.md)
- [`GAME-0222` — "Call of Juarez: Gunslinger"](../games/a-f/call-of-juarez-gunslinger.md)
- [`GAME-0137` — Counter-Strike 2](../games/a-f/counter-strike-2.md)
- [`GAME-0218` — Counter-Strike](../games/a-f/counter-strike.md)
- [`GAME-0246` — Crysis Remastered](../games/a-f/crysis-remastered.md)
- [`GAME-0146` — Cyberpunk 2077](../games/a-f/cyberpunk-2077.md)
- [`GAME-0210` — DayZ](../games/a-f/dayz.md)
- [`GAME-0259` — "Dead Space (2023 remake)"](../games/a-f/dead-space-2023.md)
- [`GAME-0200` — Delta Force](../games/a-f/delta-force.md)
- [`GAME-0193` — Destiny 2](../games/a-f/destiny-2.md)
- [`GAME-0353` — "Deus Ex: Game of the Year Edition"](../games/a-f/deus-ex-game-of-the-year-edition.md)
- [`GAME-0361` — Fallout: New Vegas](../games/a-f/fallout-new-vegas.md)
- [`GAME-0236` — Far Cry 3](../games/a-f/far-cry-3.md)
- [`GAME-0227` — Fortnite](../games/a-f/fortnite.md)
- [`GAME-0321` — Gears of War](../games/g-l/gears-of-war.md)
- [`GAME-0145` — Grand Theft Auto V](../games/g-l/grand-theft-auto-v.md)
- [`GAME-0239` — Half-Life (1998)](../games/g-l/half-life-1998.md)
- [`GAME-0212` — Half-Life 2](../games/g-l/half-life-2.md)
- [`GAME-0315` — Halo 3](../games/g-l/halo-3.md)
- [`GAME-0340` — "Halo: Combat Evolved Anniversary"](../games/g-l/halo-combat-evolved-anniversary.md)
- [`GAME-0159` — Helldivers 2](../games/g-l/helldivers-2.md)
- [`GAME-0248` — HITMAN World of Assassination](../games/g-l/hitman-world-of-assassination.md)
- [`GAME-0192` — Left 4 Dead 2](../games/g-l/left-4-dead-2.md)
- [`GAME-0367` — Mass Effect 2 (Legendary Edition)](../games/m-r/mass-effect-2-legendary-edition.md)
- [`GAME-0238` — "Max Payne (2001)"](../games/m-r/max-payne-2001.md)
- [`GAME-0273` — Max Payne 3](../games/m-r/max-payne-3.md)
- [`GAME-0306` — METAL GEAR SOLID V: THE PHANTOM PAIN](../games/m-r/metal-gear-solid-v-the-phantom-pain.md)
- [`GAME-0260` — Metro Exodus](../games/m-r/metro-exodus.md)
- [`GAME-0202` — "NARAKA: BLADEPOINT"](../games/m-r/naraka-bladepoint.md)
- [`GAME-0181` — Overwatch](../games/m-r/overwatch.md)
- [`GAME-0201` — PAYDAY 2](../games/m-r/payday-2.md)
- [`GAME-0232` — PAYDAY 3](../games/m-r/payday-3.md)
- [`GAME-0258` — "Prey (2017)"](../games/m-r/prey-2017.md)
- [`GAME-0140` — "PUBG: BATTLEGROUNDS"](../games/m-r/pubg-battlegrounds.md)
- [`GAME-0165` — Red Dead Redemption 2](../games/m-r/red-dead-redemption-2.md)
- [`GAME-0280` — Resident Evil 2 (2019 remake)](../games/m-r/resident-evil-2-2019.md)
- [`GAME-0249` — Resident Evil 4 (2023 remake)](../games/m-r/resident-evil-4-2023.md)
- [`GAME-0272` — Serious Sam 4](../games/s-z/serious-sam-4.md)
- [`GAME-0170` — "S.T.A.L.K.E.R. 2: Heart of Chornobyl"](../games/s-z/stalker-2-heart-of-chornobyl.md)
- [`GAME-0187` — Team Fortress 2](../games/s-z/team-fortress-2.md)
- [`GAME-0261` — The Last of Us Part I](../games/s-z/the-last-of-us-part-i.md)
- [`GAME-0253` — "Titanfall 2"](../games/s-z/titanfall-2.md)
- [`GAME-0174` — Tom Clancy’s Rainbow Six Siege](../games/s-z/tom-clancys-rainbow-six-siege.md)
- [`GAME-0250` — Tomb Raider (2013)](../games/s-z/tomb-raider-2013.md)
- [`GAME-0168` — Warframe](../games/s-z/warframe.md)
- [`GAME-0176` — XCOM 2](../games/s-z/xcom-2.md)

## ACT-184

- Назва: Підготувати й кинути тактичну гранату зі спорядження
- Переглянуто: `2026-08-24`

### Операційне визначення

Гравець обирає наявну одноразову гранату, визначає напрям і силу кидка та запускає її по дузі крізь ігровий світ.

### Включає

Кидки димових, світлошумових, уламкових і запалювальних гранат у Counter-Strike 2 та відповідних гранат у Battlefield 6.

### Виключає

Постріл зі стаціонарної пускової установки; установлення постійної пастки; звичайну стрільбу з вогнепальної зброї.

### Ігри-носії

- [`GAME-0154` — Apex Legends](../games/a-f/apex-legends.md)
- [`GAME-0234` — Battlefield 2042](../games/a-f/battlefield-2042.md)
- [`GAME-0149` — Battlefield 6](../games/a-f/battlefield-6.md)
- [`GAME-0220` — Battlefield V](../games/a-f/battlefield-v.md)
- [`GAME-0137` — Counter-Strike 2](../games/a-f/counter-strike-2.md)
- [`GAME-0218` — Counter-Strike](../games/a-f/counter-strike.md)
- [`GAME-0200` — Delta Force](../games/a-f/delta-force.md)
- [`GAME-0321` — Gears of War](../games/g-l/gears-of-war.md)
- [`GAME-0145` — Grand Theft Auto V](../games/g-l/grand-theft-auto-v.md)
- [`GAME-0315` — Halo 3](../games/g-l/halo-3.md)
- [`GAME-0340` — "Halo: Combat Evolved Anniversary"](../games/g-l/halo-combat-evolved-anniversary.md)
- [`GAME-0159` — Helldivers 2](../games/g-l/helldivers-2.md)
- [`GAME-0192` — Left 4 Dead 2](../games/g-l/left-4-dead-2.md)
- [`GAME-0140` — "PUBG: BATTLEGROUNDS"](../games/m-r/pubg-battlegrounds.md)
- [`GAME-0253` — "Titanfall 2"](../games/s-z/titanfall-2.md)
- [`GAME-0174` — Tom Clancy’s Rainbow Six Siege](../games/s-z/tom-clancys-rainbow-six-siege.md)

## ACT-185

- Назва: Безперервно встановлювати або знешкоджувати бомбу
- Переглянуто: `2026-08-24`

### Операційне визначення

Гравець, який виконав потрібні умови, утримує взаємодію з ціллю протягом визначеного часу без переривання, щоб установити вибухівку зі спорядження або знешкодити вже активний пристрій.

### Включає

Установлення C4 терористами та знешкодження контртерористами в Counter-Strike 2, зокрема скорочення часу знешкодження за наявності набору сапера.

### Виключає

Миттєве перемикання стану; пошкодження пристрою атакою; постановочну сцену без керованої тривалої дії.

### Ігри-носії

- [`GAME-0137` — Counter-Strike 2](../games/a-f/counter-strike-2.md)
- [`GAME-0218` — Counter-Strike](../games/a-f/counter-strike.md)
- [`GAME-0174` — Tom Clancy’s Rainbow Six Siege](../games/s-z/tom-clancys-rainbow-six-siege.md)

## ACT-186

- Назва: Викидати зброю або предмет цілі для передавання іншому гравцеві
- Переглянуто: `2026-08-24`

### Операційне визначення

Гравець вилучає дозволену зброю чи предмет цілі зі свого спорядження й залишає його в поточному місці світу, де предмет може підібрати союзник або суперник.

### Включає

Викидання зброї та C4 у Counter-Strike 2 для перерозподілу спорядження всередині команди.

### Виключає

Викидання використаних магазинів; застосування гранати; продаж предмета в крамниці.

### Ігри-носії

- [`GAME-0154` — Apex Legends](../games/a-f/apex-legends.md)
- [`GAME-0137` — Counter-Strike 2](../games/a-f/counter-strike-2.md)
- [`GAME-0218` — Counter-Strike](../games/a-f/counter-strike.md)
- [`GAME-0227` — Fortnite](../games/a-f/fortnite.md)
- [`GAME-0202` — "NARAKA: BLADEPOINT"](../games/m-r/naraka-bladepoint.md)
- [`GAME-0203` — "PEAK"](../games/m-r/peak.md)
- [`GAME-0140` — "PUBG: BATTLEGROUNDS"](../games/m-r/pubg-battlegrounds.md)
- [`GAME-0174` — Tom Clancy’s Rainbow Six Siege](../games/s-z/tom-clancys-rainbow-six-siege.md)

## ACT-187

- Назва: Передати союзникам поточне спостереження, попередження або план
- Переглянуто: `2026-08-24`

### Операційне визначення

Поки спільна гра триває в реальному часі, гравець навмисно повідомляє команді про позицію, побачену подію, небезпеку чи задум через доступний голосовий, текстовий, радіоканал або позначку.

### Включає

Командні голосові, текстові й радіосигнали в Counter-Strike 2; чат, позначки й малюнки про ворогів, відновлення здібностей, рух і цілі в Dota 2; голос, текст, позначки й швидкі сигнали в Marvel Rivals; позначки, голосовий і текстовий зв’язок загону в Battlefield 6.

### Виключає

Пояснення правил або постійного стану; спілкування поза грою без обмеженого командного каналу; автоматичні системні повідомлення.

### Ігри-носії

- [`GAME-0154` — Apex Legends](../games/a-f/apex-legends.md)
- [`GAME-0234` — Battlefield 2042](../games/a-f/battlefield-2042.md)
- [`GAME-0149` — Battlefield 6](../games/a-f/battlefield-6.md)
- [`GAME-0220` — Battlefield V](../games/a-f/battlefield-v.md)
- [`GAME-0137` — Counter-Strike 2](../games/a-f/counter-strike-2.md)
- [`GAME-0218` — Counter-Strike](../games/a-f/counter-strike.md)
- [`GAME-0200` — Delta Force](../games/a-f/delta-force.md)
- [`GAME-0138` — Dota 2](../games/a-f/dota-2.md)
- [`GAME-0159` — Helldivers 2](../games/g-l/helldivers-2.md)
- [`GAME-0147` — Marvel Rivals](../games/m-r/marvel-rivals.md)
- [`GAME-0181` — Overwatch](../games/m-r/overwatch.md)
- [`GAME-0187` — Team Fortress 2](../games/s-z/team-fortress-2.md)
- [`GAME-0174` — Tom Clancy’s Rainbow Six Siege](../games/s-z/tom-clancys-rainbow-six-siege.md)

## ACT-188

- Назва: Закріпити одного персонажа й варіант розвитку за місцем у команді
- Переглянуто: `2026-08-27`

### Операційне визначення

Під час обмеженого командного вибору гравець закріплює за своїм місцем одного доступного персонажа та показаний перед матчем або відкритий пізніше варіант його розвитку.

### Включає

Вибір героя та передматчевого варіанта розвитку в Dota 2; вибір легенди й наступний вибір переваги в межах матчу в Apex Legends.

### Виключає

Косметичне спорядження; зміну на іншого персонажа після початку активної гри.

### Ігри-носії

- [`GAME-0154` — Apex Legends](../games/a-f/apex-legends.md)
- [`GAME-0138` — Dota 2](../games/a-f/dota-2.md)
- [`GAME-0181` — Overwatch](../games/m-r/overwatch.md)
- [`GAME-0174` — Tom Clancy’s Rainbow Six Siege](../games/s-z/tom-clancys-rainbow-six-siege.md)

## ACT-189

- Назва: Віддати героєві наказ рухатися або атакувати
- Переглянуто: `2026-08-24`

### Операційне визначення

Гравець задає керованому героєві точку призначення, ціль або наказ рухатися з атакою, який потім виконує автоматичний пошук шляху.

### Включає

Накази рухатися, атакувати, рухатися з атакою, зупинитися й утримувати позицію в Dota 2.

### Виключає

Безпосереднє керування кожним кроком персонажа; застосування здібності; самостійний рух лінійних кріпів.

### Ігри-носії

- [`GAME-0179` — Age of Empires II: Definitive Edition](../games/a-f/age-of-empires-ii-definitive-edition.md)
- [`GAME-0275` — Command & Conquer Remastered Collection](../games/a-f/command-and-conquer-remastered-collection.md)
- [`GAME-0209` — Cossacks 3](../games/a-f/cossacks-3.md)
- [`GAME-0204` — "Crusader Kings III"](../games/a-f/crusader-kings-iii.md)
- [`GAME-0368` — Dead Rising](../games/a-f/dead-rising.md)
- [`GAME-0264` — Disco Elysium - The Final Cut](../games/a-f/disco-elysium-the-final-cut.md)
- [`GAME-0138` — Dota 2](../games/a-f/dota-2.md)
- [`GAME-0182` — Hearts of Iron IV](../games/g-l/hearts-of-iron-iv.md)
- [`GAME-0332` — "Heroes of Might and Magic III: Complete"](../games/g-l/heroes-of-might-and-magic-iii-complete.md)
- [`GAME-0367` — Mass Effect 2 (Legendary Edition)](../games/m-r/mass-effect-2-legendary-edition.md)
- [`GAME-0194` — "Mount & Blade II: Bannerlord"](../games/m-r/mount-and-blade-ii-bannerlord.md)
- [`GAME-0317` — StarCraft II](../games/s-z/starcraft-ii.md)
- [`GAME-0287` — Stellaris](../games/s-z/stellaris.md)
- [`GAME-0191` — "Total War: WARHAMMER III"](../games/s-z/total-war-warhammer-iii.md)
- [`GAME-0328` — "Warcraft III: Reign of Chaos"](../games/s-z/warcraft-iii-reign-of-chaos.md)

## ACT-190

- Назва: Застосувати активну здібність персонажа або предмета
- Переглянуто: `2026-09-07`

### Операційне визначення

Гравець застосовує доступну активну здібність персонажа або активну властивість переносного предмета й задає потрібну істоту, точку, вектор, напрям чи дію без окремої цілі, зокрема утримує команду протягом потрібного каналу.

### Включає

Заклинання, перемикачі та активні предмети Dota 2; здібності героїв у Marvel Rivals; класові пристрої Battlefield 6; Silk Skills і споряджені Tools у Hollow Knight: Silksong; утримуване зосередження для лікування в Hollow Knight.

### Виключає

Автоматичний вибір цілі для атаки; пасивні ефекти; звичайну атаку зброєю; косметичні емоції.

### Ігри-носії

- [`GAME-0223` — Aion Classic](../games/a-f/aion-classic.md)
- [`GAME-0154` — Apex Legends](../games/a-f/apex-legends.md)
- [`GAME-0148` — Baldur’s Gate 3](../games/a-f/baldurs-gate-3.md)
- [`GAME-0234` — Battlefield 2042](../games/a-f/battlefield-2042.md)
- [`GAME-0149` — Battlefield 6](../games/a-f/battlefield-6.md)
- [`GAME-0220` — Battlefield V](../games/a-f/battlefield-v.md)
- [`GAME-0189` — "Black Myth: Wukong"](../games/a-f/black-myth-wukong.md)
- [`GAME-0254` — CONTROL Ultimate Edition](../games/a-f/control-ultimate-edition.md)
- [`GAME-0277` — Cuphead](../games/a-f/cuphead.md)
- [`GAME-0259` — "Dead Space (2023 remake)"](../games/a-f/dead-space-2023.md)
- [`GAME-0200` — Delta Force](../games/a-f/delta-force.md)
- [`GAME-0193` — Destiny 2](../games/a-f/destiny-2.md)
- [`GAME-0286` — DOOM Eternal](../games/a-f/doom-eternal.md)
- [`GAME-0138` — Dota 2](../games/a-f/dota-2.md)
- [`GAME-0188` — FINAL FANTASY XIV Online](../games/a-f/final-fantasy-xiv-online.md)
- [`GAME-0251` — Hades](../games/g-l/hades.md)
- [`GAME-0159` — Helldivers 2](../games/g-l/helldivers-2.md)
- [`GAME-0150` — "Hollow Knight: Silksong"](../games/g-l/hollow-knight-silksong.md)
- [`GAME-0274` — Hollow Knight](../games/g-l/hollow-knight.md)
- [`GAME-0219` — Lineage II](../games/g-l/lineage-ii.md)
- [`GAME-0309` — "Mario Kart 8 Deluxe"](../games/m-r/mario-kart-8-deluxe.md)
- [`GAME-0147` — Marvel Rivals](../games/m-r/marvel-rivals.md)
- [`GAME-0323` — "Marvel’s Spider-Man 2"](../games/m-r/marvels-spider-man-2.md)
- [`GAME-0367` — Mass Effect 2 (Legendary Edition)](../games/m-r/mass-effect-2-legendary-edition.md)
- [`GAME-0355` — Metroid Prime](../games/m-r/metroid-prime.md)
- [`GAME-0297` — 'MONSTER HUNTER RISE'](../games/m-r/monster-hunter-rise.md)
- [`GAME-0202` — "NARAKA: BLADEPOINT"](../games/m-r/naraka-bladepoint.md)
- [`GAME-0299` — Nioh 2](../games/m-r/nioh-2.md)
- [`GAME-0181` — Overwatch](../games/m-r/overwatch.md)
- [`GAME-0201` — PAYDAY 2](../games/m-r/payday-2.md)
- [`GAME-0232` — PAYDAY 3](../games/m-r/payday-3.md)
- [`GAME-0270` — Risk of Rain 2](../games/m-r/risk-of-rain-2.md)
- [`GAME-0213` — "STAR WARS Jedi: Fallen Order"](../games/s-z/star-wars-jedi-fallen-order.md)
- [`GAME-0187` — Team Fortress 2](../games/s-z/team-fortress-2.md)
- [`GAME-0164` — "The Binding of Isaac: Rebirth"](../games/s-z/the-binding-of-isaac-rebirth.md)
- [`GAME-0190` — "The Elder Scrolls V: Skyrim Special Edition"](../games/s-z/the-elder-scrolls-v-skyrim-special-edition.md)
- [`GAME-0205` — "The Witcher 3: Wild Hunt"](../games/s-z/the-witcher-3-wild-hunt.md)
- [`GAME-0253` — "Titanfall 2"](../games/s-z/titanfall-2.md)
- [`GAME-0174` — Tom Clancy’s Rainbow Six Siege](../games/s-z/tom-clancys-rainbow-six-siege.md)
- [`GAME-0328` — "Warcraft III: Reign of Chaos"](../games/s-z/warcraft-iii-reign-of-chaos.md)
- [`GAME-0168` — Warframe](../games/s-z/warframe.md)
- [`GAME-0221` — World of Warcraft](../games/s-z/world-of-warcraft.md)

## ACT-191

- Назва: Витратити одне очко розвитку персонажа
- Переглянуто: `2026-08-24`

### Операційне визначення

Гравець витрачає одне доступне очко на відкритий ступінь здібності, характеристику, талант або вузол дерева розвитку, змінюючи можливості персонажа на поточний матч чи подальше проходження.

### Включає

Вибір здібностей і талантів у Dota 2; розподіл розвитку персонажа в Clair Obscur, Cyberpunk 2077 і Baldur’s Gate 3; розподіл очок дерева навичок в ARC Raiders.

### Виключає

Придбання предмета; автоматичні винагороди за рівень; косметичний розвиток усього облікового запису.

### Ігри-носії

- [`GAME-0154` — Apex Legends](../games/a-f/apex-legends.md)
- [`GAME-0143` — ARC Raiders](../games/a-f/arc-raiders.md)
- [`GAME-0148` — Baldur’s Gate 3](../games/a-f/baldurs-gate-3.md)
- [`GAME-0189` — "Black Myth: Wukong"](../games/a-f/black-myth-wukong.md)
- [`GAME-0222` — "Call of Juarez: Gunslinger"](../games/a-f/call-of-juarez-gunslinger.md)
- [`GAME-0144` — Clair Obscur: Expedition 33](../games/a-f/clair-obscur-expedition-33.md)
- [`GAME-0146` — Cyberpunk 2077](../games/a-f/cyberpunk-2077.md)
- [`GAME-0353` — "Deus Ex: Game of the Year Edition"](../games/a-f/deus-ex-game-of-the-year-edition.md)
- [`GAME-0322` — "Diablo II: Resurrected"](../games/a-f/diablo-ii-resurrected.md)
- [`GAME-0138` — Dota 2](../games/a-f/dota-2.md)
- [`GAME-0332` — "Heroes of Might and Magic III: Complete"](../games/g-l/heroes-of-might-and-magic-iii-complete.md)
- [`GAME-0181` — Overwatch](../games/m-r/overwatch.md)
- [`GAME-0162` — Path of Exile 2](../games/m-r/path-of-exile-2.md)
- [`GAME-0213` — "STAR WARS Jedi: Fallen Order"](../games/s-z/star-wars-jedi-fallen-order.md)
- [`GAME-0191` — "Total War: WARHAMMER III"](../games/s-z/total-war-warhammer-iii.md)
- [`GAME-0328` — "Warcraft III: Reign of Chaos"](../games/s-z/warcraft-iii-reign-of-chaos.md)

## ACT-192

- Назва: Налаштувати доставлення предметів зі сховку кур’єром
- Переглянуто: `2026-08-24`

### Операційне визначення

Гравець перекладає доступні предмети матчу між героєм, сховком і командним кур’єром або наказує кур’єрові забрати й доставити їх.

### Включає

Отримання предметів зі сховку й доставлення їх кур’єром у Dota 2.

### Виключає

Придбання предмета; викидання його для підбирання із землі; безпосередній рух героя.

### Ігри-носії

- [`GAME-0138` — Dota 2](../games/a-f/dota-2.md)

## ACT-193

- Назва: Сплатити викуп за негайне повернення героя
- Переглянуто: `2026-08-24`

### Операційне визначення

Поки керований герой мертвий, гравець сплачує показану вартість у золоті, щоб не чекати решту часу до відродження й негайно повернути героя.

### Включає

Викуп у Dota 2 після виконання умов щодо вартості й часу відновлення.

### Виключає

Звичайне безплатне відродження; оживлення союзним ефектом; придбання для облікового запису.

### Ігри-носії

- [`GAME-0138` — Dota 2](../games/a-f/dota-2.md)

## ACT-194

- Назва: Застосувати пристрій захоплення до придатної дикої істоти
- Переглянуто: `2026-08-24`

### Операційне визначення

Гравець через поточну взаємодію у світі або бою застосовує й витрачає один переносний пристрій захоплення на придатну дику істоту, запускаючи перевірку замість звичайної атаки.

### Включає

Кидок Pal Sphere у Palworld, Poké Ball у Pokémon Legends: Z-A та вибір Poké Ball через ITEM у Pokémon Red Version.

### Виключає

Перемогу над істотою; гарантоване сюжетне приєднання; переміщення вже захопленого пала між списками.

### Ігри-носії

- [`GAME-0139` — Palworld](../games/m-r/palworld.md)
- [`GAME-0160` — "Pokémon Legends: Z-A"](../games/m-r/pokemon-legends-z-a.md)
- [`GAME-0336` — "Pokémon Red Version"](../games/m-r/pokemon-red-version.md)

## ACT-195

- Назва: Випустити одного пала із загону або відкликати його
- Переглянуто: `2026-08-24`

### Операційне визначення

Гравець вибирає одного пала з активного загону, кидає його сферу в досяжне місце світу або повертає вже випущеного пала до переносного стану.

### Включає

Випускання й відкликання пала з активного загону під час дослідження або бою в Palworld.

### Виключає

Призначення пала на роботу на базі; безпосереднє керування рухом персонажа; захоплення нової істоти.

### Ігри-носії

- [`GAME-0139` — Palworld](../games/m-r/palworld.md)
- [`GAME-0160` — "Pokémon Legends: Z-A"](../games/m-r/pokemon-legends-z-a.md)

## ACT-196

- Назва: Перемістити захопленого пала між сховищем, загоном і базою
- Переглянуто: `2026-08-24`

### Операційне визначення

Через постійний засіб керування гравець переводить одного захопленого пала між резервним сховищем, обмеженим активним загоном і вільним місцем працівника бази.

### Включає

Переміщення через Palbox між сховищем палів, активним загоном і призначеннями на базі.

### Виключає

Захоплення дикої істоти; тимчасове випускання пала у світ; розведення двох істот зі сховища.

### Ігри-носії

- [`GAME-0139` — Palworld](../games/m-r/palworld.md)
- [`GAME-0160` — "Pokémon Legends: Z-A"](../games/m-r/pokemon-legends-z-a.md)

## ACT-197

- Назва: Застосувати оголошену активну здібність напарника
- Переглянуто: `2026-09-06`

### Операційне визначення

Коли потрібний напарник і стан спорядження це дозволяють, гравець запускає оголошену для нього партнерську взаємодію, форму для пересування верхи або активну здібність.

### Включає

Їзду на придатному палі, використання його для пересування або застосування активної Partner Skill у Palworld; наказ напарникові випустити стріли в поточну ціль у визначеному початковому розділі God of War.

### Виключає

Самостійні звичайні дії напарника поруч із прямим керуванням; пасивну робочу придатність; безпосереднє використання зброї самим гравцем.

### Ігри-носії

- [`GAME-0263` — God of War](../games/g-l/god-of-war.md)
- [`GAME-0139` — Palworld](../games/m-r/palworld.md)

## ACT-198

- Назва: Покинути літак і керувати повітряним висадженням
- Переглянуто: `2026-08-24`

### Операційне визначення

Гравець обирає мить виходу з транспортного літака, керує персонажем під час вільного падіння й польоту з парашутом і так визначає досяжну початкову область до переходу до звичайного наземного руху.

### Включає

Вихід із літака, вільне падіння й керування парашутом у PUBG Normal Match.

### Виключає

Вибір статичної точки появи; стрибок під час наземного пересування; вхід до транспорту після приземлення.

### Ігри-носії

- [`GAME-0154` — Apex Legends](../games/a-f/apex-legends.md)
- [`GAME-0227` — Fortnite](../games/a-f/fortnite.md)
- [`GAME-0140` — "PUBG: BATTLEGROUNDS"](../games/m-r/pubg-battlegrounds.md)

## ACT-199

- Назва: Перенести й спорядити один сумісний наявний предмет
- Переглянуто: `2026-09-03`

### Операційне визначення

Гравець обирає один досяжний або вже наявний предмет і переносить його до сумісної комірки стосу, зброї, модуля, захисту чи сховища, за потреби замінюючи споряджений предмет.

### Включає

Дії підбирання, перенесення й спорядження зброї, набоїв, модулів, броні, наплічників і витратних предметів у PUBG: BATTLEGROUNDS та Cyberpunk 2077; одягання особисто виготовленого Primitive Outfit у 7 Days to Die.

### Виключає

Автоматичне підбирання через контакт; придбання предмета; виготовлення; збирання абстрактного жетона рахунку.

### Ігри-носії

- [`GAME-0233` — 7 Days to Die](../games/0-9/7-days-to-die.md)
- [`GAME-0257` — "Alien: Isolation"](../games/a-f/alien-isolation.md)
- [`GAME-0320` — "Animal Crossing: New Horizons"](../games/a-f/animal-crossing-new-horizons.md)
- [`GAME-0154` — Apex Legends](../games/a-f/apex-legends.md)
- [`GAME-0143` — ARC Raiders](../games/a-f/arc-raiders.md)
- [`GAME-0148` — Baldur’s Gate 3](../games/a-f/baldurs-gate-3.md)
- [`GAME-0220` — Battlefield V](../games/a-f/battlefield-v.md)
- [`GAME-0256` — "BioShock™ Remastered"](../games/a-f/bioshock-remastered.md)
- [`GAME-0222` — "Call of Juarez: Gunslinger"](../games/a-f/call-of-juarez-gunslinger.md)
- [`GAME-0347` — "Castlevania: Symphony of the Night"](../games/a-f/castlevania-symphony-of-the-night.md)
- [`GAME-0146` — Cyberpunk 2077](../games/a-f/cyberpunk-2077.md)
- [`GAME-0262` — DARK SOULS™ III](../games/a-f/dark-souls-iii.md)
- [`GAME-0295` — DARK SOULS™: REMASTERED](../games/a-f/dark-souls-remastered.md)
- [`GAME-0281` — Darkest Dungeon](../games/a-f/darkest-dungeon.md)
- [`GAME-0210` — DayZ](../games/a-f/dayz.md)
- [`GAME-0282` — Dead Cells](../games/a-f/dead-cells.md)
- [`GAME-0259` — "Dead Space (2023 remake)"](../games/a-f/dead-space-2023.md)
- [`GAME-0310` — "DEATH STRANDING DIRECTOR’S CUT"](../games/a-f/death-stranding-directors-cut.md)
- [`GAME-0353` — "Deus Ex: Game of the Year Edition"](../games/a-f/deus-ex-game-of-the-year-edition.md)
- [`GAME-0322` — "Diablo II: Resurrected"](../games/a-f/diablo-ii-resurrected.md)
- [`GAME-0264` — Disco Elysium - The Final Cut](../games/a-f/disco-elysium-the-final-cut.md)
- [`GAME-0301` — "Divinity: Original Sin 2 - Definitive Edition"](../games/a-f/divinity-original-sin-2-definitive-edition.md)
- [`GAME-0186` — "Don’t Starve Together"](../games/a-f/dont-starve-together.md)
- [`GAME-0231` — Fallout 4](../games/a-f/fallout-4.md)
- [`GAME-0361` — Fallout: New Vegas](../games/a-f/fallout-new-vegas.md)
- [`GAME-0227` — Fortnite](../games/a-f/fortnite.md)
- [`GAME-0321` — Gears of War](../games/g-l/gears-of-war.md)
- [`GAME-0239` — Half-Life (1998)](../games/g-l/half-life-1998.md)
- [`GAME-0212` — Half-Life 2](../games/g-l/half-life-2.md)
- [`GAME-0315` — Halo 3](../games/g-l/halo-3.md)
- [`GAME-0340` — "Halo: Combat Evolved Anniversary"](../games/g-l/halo-combat-evolved-anniversary.md)
- [`GAME-0240` — "Kingdom Come: Deliverance II"](../games/g-l/kingdom-come-deliverance-ii.md)
- [`GAME-0192` — Left 4 Dead 2](../games/g-l/left-4-dead-2.md)
- [`GAME-0219` — Lineage II](../games/g-l/lineage-ii.md)
- [`GAME-0367` — Mass Effect 2 (Legendary Edition)](../games/m-r/mass-effect-2-legendary-edition.md)
- [`GAME-0238` — "Max Payne (2001)"](../games/m-r/max-payne-2001.md)
- [`GAME-0273` — Max Payne 3](../games/m-r/max-payne-3.md)
- [`GAME-0260` — Metro Exodus](../games/m-r/metro-exodus.md)
- [`GAME-0194` — "Mount & Blade II: Bannerlord"](../games/m-r/mount-and-blade-ii-bannerlord.md)
- [`GAME-0202` — "NARAKA: BLADEPOINT"](../games/m-r/naraka-bladepoint.md)
- [`GAME-0296` — Noita](../games/m-r/noita.md)
- [`GAME-0162` — Path of Exile 2](../games/m-r/path-of-exile-2.md)
- [`GAME-0201` — PAYDAY 2](../games/m-r/payday-2.md)
- [`GAME-0232` — PAYDAY 3](../games/m-r/payday-3.md)
- [`GAME-0203` — "PEAK"](../games/m-r/peak.md)
- [`GAME-0258` — "Prey (2017)"](../games/m-r/prey-2017.md)
- [`GAME-0142` — Project Zomboid](../games/m-r/project-zomboid.md)
- [`GAME-0140` — "PUBG: BATTLEGROUNDS"](../games/m-r/pubg-battlegrounds.md)
- [`GAME-0280` — Resident Evil 2 (2019 remake)](../games/m-r/resident-evil-2-2019.md)
- [`GAME-0348` — "Resident Evil: Director’s Cut"](../games/m-r/resident-evil-directors-cut.md)
- [`GAME-0141` — Rust](../games/m-r/rust.md)
- [`GAME-0170` — "S.T.A.L.K.E.R. 2: Heart of Chornobyl"](../games/s-z/stalker-2-heart-of-chornobyl.md)
- [`GAME-0230` — "STAR WARS Battlefront II (2017)"](../games/s-z/star-wars-battlefront-ii-2017.md)
- [`GAME-0331` — Starfield](../games/s-z/starfield.md)
- [`GAME-0362` — "The Elder Scrolls III: Morrowind"](../games/s-z/the-elder-scrolls-iii-morrowind.md)
- [`GAME-0190` — "The Elder Scrolls V: Skyrim Special Edition"](../games/s-z/the-elder-scrolls-v-skyrim-special-edition.md)
- [`GAME-0261` — The Last of Us Part I](../games/s-z/the-last-of-us-part-i.md)
- [`GAME-0363` — "The Legend of Zelda: Ocarina of Time"](../games/s-z/the-legend-of-zelda-ocarina-of-time.md)
- [`GAME-0285` — "The Long Dark"](../games/s-z/the-long-dark.md)
- [`GAME-0205` — "The Witcher 3: Wild Hunt"](../games/s-z/the-witcher-3-wild-hunt.md)
- [`GAME-0250` — Tomb Raider (2013)](../games/s-z/tomb-raider-2013.md)
- [`GAME-0191` — "Total War: WARHAMMER III"](../games/s-z/total-war-warhammer-iii.md)
- [`GAME-0294` — V Rising](../games/s-z/v-rising.md)
- [`GAME-0197` — Valheim](../games/s-z/valheim.md)
- [`GAME-0221` — World of Warcraft](../games/s-z/world-of-warcraft.md)

## ACT-200

- Назва: Застосувати переривний предмет відновлення чи ремонту
- Переглянуто: `2026-08-24`

### Операційне визначення

Гравець починає тривале застосування наявного в інвентарі предмета відновлення або ремонту й отримує його миттєвий чи поступовий ефект лише тоді, коли жодна скасувальна дія не перервала процес.

### Включає

Bandages, First Aid Kits, Med Kits, Energy Drinks, Painkillers і Adrenaline Syringes у PUBG; обмежені ковтки з Gourd у Black Myth: Wukong; Vitalia, Armor Powder і набори для ремонту зброї у NARAKA: BLADEPOINT.

### Виключає

Миттєве використання зілля в покроковій грі; пасивне відновлення без предмета; оживлення іншого учасника.

### Ігри-носії

- [`GAME-0154` — Apex Legends](../games/a-f/apex-legends.md)
- [`GAME-0143` — ARC Raiders](../games/a-f/arc-raiders.md)
- [`GAME-0220` — Battlefield V](../games/a-f/battlefield-v.md)
- [`GAME-0189` — "Black Myth: Wukong"](../games/a-f/black-myth-wukong.md)
- [`GAME-0308` — Bloodborne™](../games/a-f/bloodborne.md)
- [`GAME-0262` — DARK SOULS™ III](../games/a-f/dark-souls-iii.md)
- [`GAME-0295` — DARK SOULS™: REMASTERED](../games/a-f/dark-souls-remastered.md)
- [`GAME-0210` — DayZ](../games/a-f/dayz.md)
- [`GAME-0152` — Elden Ring](../games/a-f/elden-ring.md)
- [`GAME-0236` — Far Cry 3](../games/a-f/far-cry-3.md)
- [`GAME-0271` — Far Cry 5](../games/a-f/far-cry-5.md)
- [`GAME-0192` — Left 4 Dead 2](../games/g-l/left-4-dead-2.md)
- [`GAME-0290` — Lies of P](../games/g-l/lies-of-p.md)
- [`GAME-0202` — "NARAKA: BLADEPOINT"](../games/m-r/naraka-bladepoint.md)
- [`GAME-0299` — Nioh 2](../games/m-r/nioh-2.md)
- [`GAME-0203` — "PEAK"](../games/m-r/peak.md)
- [`GAME-0140` — "PUBG: BATTLEGROUNDS"](../games/m-r/pubg-battlegrounds.md)
- [`GAME-0170` — "S.T.A.L.K.E.R. 2: Heart of Chornobyl"](../games/s-z/stalker-2-heart-of-chornobyl.md)
- [`GAME-0213` — "STAR WARS Jedi: Fallen Order"](../games/s-z/star-wars-jedi-fallen-order.md)
- [`GAME-0261` — The Last of Us Part I](../games/s-z/the-last-of-us-part-i.md)

## ACT-201

- Назва: Сісти в техніку й безпосередньо керувати нею
- Переглянуто: `2026-08-24`

### Операційне визначення

Гравець займає вільне місце в транспорті або бойовій техніці, керує прискоренням і напрямком руху з місця водія чи пілота, може пересідати й сам обирає мить виходу.

### Включає

Керування чи поїздку в наземному транспорті Erangel у PUBG Normal Match; вхід, викрадення й керування дорожнім, водним або повітряним транспортом у Story Mode Grand Theft Auto V; водіння в Cyberpunk 2077; керування танками, гелікоптерами й літаками та використання місць стрільців у Battlefield 6.

### Виключає

Призначення автономного транспортного маршруту; транспортний літак висадження, яким гравець не може керувати; пересування персонажа пішки.

### Ігри-носії

- [`GAME-0289` — American Truck Simulator](../games/a-f/american-truck-simulator.md)
- [`GAME-0234` — Battlefield 2042](../games/a-f/battlefield-2042.md)
- [`GAME-0149` — Battlefield 6](../games/a-f/battlefield-6.md)
- [`GAME-0220` — Battlefield V](../games/a-f/battlefield-v.md)
- [`GAME-0200` — Delta Force](../games/a-f/delta-force.md)
- [`GAME-0169` — Euro Truck Simulator 2](../games/a-f/euro-truck-simulator-2.md)
- [`GAME-0196` — Farming Simulator 25](../games/a-f/farming-simulator-25.md)
- [`GAME-0357` — "Grand Theft Auto: San Andreas"](../games/g-l/grand-theft-auto-san-andreas.md)
- [`GAME-0145` — Grand Theft Auto V](../games/g-l/grand-theft-auto-v.md)
- [`GAME-0214` — "Mafia (2002)"](../games/m-r/mafia-2002.md)
- [`GAME-0229` — "No Man’s Sky"](../games/m-r/no-mans-sky.md)
- [`GAME-0140` — "PUBG: BATTLEGROUNDS"](../games/m-r/pubg-battlegrounds.md)
- [`GAME-0165` — Red Dead Redemption 2](../games/m-r/red-dead-redemption-2.md)
- [`GAME-0157` — Split Fiction](../games/s-z/split-fiction.md)
- [`GAME-0178` — Subnautica](../games/s-z/subnautica.md)

## ACT-202

- Назва: Змінити положення або конфігурацію тіла персонажа
- Переглянуто: `2026-09-21`

### Операційне визначення

Гравець переводить керованого персонажа між стоянням, присіданням, лежанням, бічним нахилом або збереженою компактною конфігурацією тіла, змінюючи габарит зіткнень, доступні кути огляду чи дії інструмента, рух і, де це має значення, відкритість тіла або поводження зі зброєю без передавання керування іншому персонажу.

### Включає

Зміни положення тіла й визирання з-за укриття в PUBG; стояче й присіле положення в Cyberpunk 2077; присідання й положення лежачи в PowerWash Simulator; вхід у Morphing Ball і вихід із нього в Super Metroid.

### Виключає

Звичайне переміщення місцевістю; зміну перспективи камери; автоматичне положення після відкидання; контекстну анімацію, що не змінює доступ, видимість чи іншу значущу можливість.

### Ігри-носії

- [`GAME-0243` — Battlefield Hardline](../games/a-f/battlefield-hardline.md)
- [`GAME-0324` — Contra Force](../games/a-f/contra-force.md)
- [`GAME-0246` — Crysis Remastered](../games/a-f/crysis-remastered.md)
- [`GAME-0146` — Cyberpunk 2077](../games/a-f/cyberpunk-2077.md)
- [`GAME-0353` — "Deus Ex: Game of the Year Edition"](../games/a-f/deus-ex-game-of-the-year-edition.md)
- [`GAME-0247` — Dishonored (2012)](../games/a-f/dishonored-2012.md)
- [`GAME-0236` — Far Cry 3](../games/a-f/far-cry-3.md)
- [`GAME-0340` — "Halo: Combat Evolved Anniversary"](../games/g-l/halo-combat-evolved-anniversary.md)
- [`GAME-0248` — HITMAN World of Assassination](../games/g-l/hitman-world-of-assassination.md)
- [`GAME-0306` — METAL GEAR SOLID V: THE PHANTOM PAIN](../games/m-r/metal-gear-solid-v-the-phantom-pain.md)
- [`GAME-0339` — Metal Gear Solid](../games/m-r/metal-gear-solid.md)
- [`GAME-0260` — Metro Exodus](../games/m-r/metro-exodus.md)
- [`GAME-0355` — Metroid Prime](../games/m-r/metroid-prime.md)
- [`GAME-0393` — Mortal Kombat II](../games/m-r/mortal-kombat-ii.md)
- [`GAME-0279` — PowerWash Simulator](../games/m-r/powerwash-simulator.md)
- [`GAME-0140` — "PUBG: BATTLEGROUNDS"](../games/m-r/pubg-battlegrounds.md)
- [`GAME-0249` — Resident Evil 4 (2023 remake)](../games/m-r/resident-evil-4-2023.md)
- [`GAME-0288` — "Sekiro™: Shadows Die Twice - GOTY Edition"](../games/s-z/sekiro-shadows-die-twice.md)
- [`GAME-0230` — "STAR WARS Battlefront II (2017)"](../games/s-z/star-wars-battlefront-ii-2017.md)
- [`GAME-0337` — Super Metroid](../games/s-z/super-metroid.md)
- [`GAME-0366` — Tekken 3](../games/s-z/tekken-3.md)
- [`GAME-0283` — TEKKEN 8](../games/s-z/tekken-8.md)
- [`GAME-0190` — "The Elder Scrolls V: Skyrim Special Edition"](../games/s-z/the-elder-scrolls-v-skyrim-special-edition.md)
- [`GAME-0261` — The Last of Us Part I](../games/s-z/the-last-of-us-part-i.md)
- [`GAME-0174` — Tom Clancy’s Rainbow Six Siege](../games/s-z/tom-clancys-rainbow-six-siege.md)
- [`GAME-0349` — "Tom Clancy’s Splinter Cell"](../games/s-z/tom-clancys-splinter-cell.md)

## ACT-203

- Назва: Викопати тактичне укриття в руйнівному ґрунті
- Переглянуто: `2026-08-24`

### Операційне визначення

Гравець спрямовує придатний інструмент або вибухівку на руйнівний ґрунт і завдає удару, який прибирає обмежену частину землі та створює прохідну виїмку або край укриття.

### Включає

Копання киркою та руйнування ґрунту гранатами, мінометом, Panzerfaust, C4 або вибухом транспорту на Erangel у PUBG Update 41.1.

### Виключає

Пошкодження ворога; руйнування будівлі; необмежене видобування вокселів; косметичні сліди без зміни прохідної поверхні.

### Ігри-носії

- [`GAME-0140` — "PUBG: BATTLEGROUNDS"](../games/m-r/pubg-battlegrounds.md)

## ACT-204

- Назва: Розмістити, зміцнити або полагодити з’єднаний будівельний блок
- Переглянуто: `2026-08-24`

### Операційне визначення

Гравець наводиться на дозволену точку з’єднання або наявний блок споруди й витрачає відповідний матеріал, щоб поставити початкову конструкцію, зробити її міцнішою чи відновити втрачену міцність.

### Включає

Фундаменти, стіни, підлоги, стелі й дверні рами Rust, які ставлять за допомогою Building Plan, а зміцнюють і лагодять Hammer.

### Виключає

Розміщення окремого предмета; створення креслення для автономних працівників; зміна рельєфу.

### Ігри-носії

- [`GAME-0141` — Rust](../games/m-r/rust.md)
- [`GAME-0294` — V Rising](../games/s-z/v-rising.md)
- [`GAME-0197` — Valheim](../games/s-z/valheim.md)

## ACT-205

- Назва: Налаштувати право доступу до об’єкта світу
- Переглянуто: `2026-08-24`

### Операційне визначення

Гравець взаємодіє з досяжним об’єктом власності чи замком, щоб додати або вилучити особу зі списку доступу, установити чи ввести ключові дані або очистити поточний список.

### Включає

Додавання гравця до Tool Cupboard і введення чи зміна коду Code Lock у Rust.

### Виключає

Відкривання дверей із уже наданим доступом; перенесення збережених предметів; права адміністратора сервера.

### Ігри-носії

- [`GAME-0141` — Rust](../games/m-r/rust.md)

## ACT-206

- Назва: Завантажити й запустити пристрій перероблення матеріалів
- Переглянуто: `2026-08-24`

### Операційне визначення

Гравець переносить сумісну сировину та потрібне паливо до досяжного пристрою, за потреби запускає чи зупиняє його, а згодом забирає готові продукти й залишки.

### Включає

Завантаження та запалювання Furnace і перероблення компонентів у Recycler монумента в Rust.

### Виключає

Ручне виготовлення; призначення рецепта автономному виробництву; просте зберігання незмінених предметів.

### Ігри-носії

- [`GAME-0229` — "No Man’s Sky"](../games/m-r/no-mans-sky.md)
- [`GAME-0141` — Rust](../games/m-r/rust.md)

## ACT-207

- Назва: Витратити дослідницький ресурс, щоб вивчити рецепт предмета
- Переглянуто: `2026-08-24`

### Операційне визначення

Гравець обирає придатний предмет у дослідницькому пристрої або доступний вузол дерева технологій і витрачає визначений ресурс, щоб додати рецепт до особистих знань.

### Включає

Дослідження за scrap на Research Table і відкриття вузла дерева технологій Workbench у Rust.

### Виключає

Виготовлення вже вивченого предмета; безкоштовний початковий рецепт; поліпшення самого Workbench.

### Ігри-носії

- [`GAME-0141` — Rust](../games/m-r/rust.md)

## ACT-208

- Назва: Розмістити й призначити постійне місце відродження
- Переглянуто: `2026-08-24`

### Операційне визначення

Гравець ставить придатний для сну об’єкт у спільному світі та призначає його одній особі як майбутнє місце появи після смерті.

### Включає

Розміщення й призначення Sleeping Bag у Rust.

### Виключає

Випадкова поява на пляжі після смерті; автоматичне збереження контрольної точки; тимчасове оживлення товариша.

### Ігри-носії

- [`GAME-0141` — Rust](../games/m-r/rust.md)

## ACT-209

- Назва: Закласти заряд із відкладеним вибухом на споруду
- Переглянуто: `2026-08-24`

### Операційне визначення

Гравець кидає або прикріплює переносний заряд до досяжної поверхні, після чого запал сам доводить його до вибуху по споруді.

### Включає

Установлення Timed Explosive Charge на двері чи будівельний блок під час рейду в Rust.

### Виключає

Постріл зі зброї; зміна лише рельєфу; знищення об’єкта командою адміністратора.

### Ігри-носії

- [`GAME-0141` — Rust](../games/m-r/rust.md)

## ACT-210

- Назва: Обрати початкове тло та сумісні риси
- Переглянуто: `2026-09-21`

### Операційне визначення

Перед звичайною появою у світі гравець обирає одне початкове тло або професію та необов’язковий сумісний набір рис, які визначають початкові навички й постійні особливості.

### Включає

Професія й збалансовані очками риси у Build 42 Project Zomboid; тло та до трьох сумісних необов’язкових рис у Starfield.

### Виключає

Розвиток навичок після появи у світі; косметичну зовнішність; налаштування самого світу.

### Ігри-носії

- [`GAME-0142` — Project Zomboid](../games/m-r/project-zomboid.md)
- [`GAME-0331` — Starfield](../games/s-z/starfield.md)

## ACT-211

- Назва: Надати першу допомогу вибраній рані
- Переглянуто: `2026-08-24`

### Операційне визначення

Гравець обирає видиму рану на певній ділянці тіла й використовує відповідний медичний засіб: очищає або перев’язує рану, накладає шину, виймає сторонній предмет чи знімає попереднє лікування.

### Включає

Перев’язування та інший догляд за ранами через панель Health у Project Zomboid.

### Виключає

Споживання їжі; пасивне загоєння; лікування спільної шкали здоров’я без вибору ділянки тіла.

### Ігри-носії

- [`GAME-0142` — Project Zomboid](../games/m-r/project-zomboid.md)

## ACT-212

- Назва: Додати або зняти один шар барикади
- Переглянуто: `2026-08-24`

### Операційне визначення

Гравець обирає доступний бік дверей чи вікна й за допомогою відповідних інструментів додає один шар дощок або металу. Так само можна зняти вже встановлений шар, якщо до нього є доступ і потрібні інструменти.

### Включає

Барикади з дощок, металевих листів і прутів у Project Zomboid.

### Виключає

Будівництво окремої стіни; закривання завіси; руйнування дверей чи вікна в бою.

### Ігри-носії

- [`GAME-0142` — Project Zomboid](../games/m-r/project-zomboid.md)
- [`GAME-0174` — Tom Clancy’s Rainbow Six Siege](../games/s-z/tom-clancys-rainbow-six-siege.md)

## ACT-213

- Назва: Посадити, доглянути або зібрати один посів
- Переглянуто: `2026-08-24`

### Операційне визначення

Гравець працює з однією грядкою: висіває насіння, поливає рослину, лікує її або збирає врожай. Посів лишається у світі й змінюється з часом.

### Включає

Сезонне городництво у Build 42 Project Zomboid.

### Виключає

Автономне фермерство колонії; збирання диких рослин; приготування їжі за рецептом.

### Ігри-носії

- [`GAME-0142` — Project Zomboid](../games/m-r/project-zomboid.md)

## ACT-214

- Назва: Укласти вцілілого спати
- Переглянуто: `2026-08-24`

### Операційне визначення

Гравець обирає придатне місце для сну й тимчасово втрачає безпосереднє керування. Поки вцілілий відпочиває, його втома зменшується, а час у світі продовжує минати до пробудження або переривання сну.

### Включає

Сон протягом одного життя в одиночній грі Project Zomboid.

### Виключає

Вибір місця відродження; паузу симуляції; відпочинок без впливу на час або втому.

### Ігри-носії

- [`GAME-0142` — Project Zomboid](../games/m-r/project-zomboid.md)
- [`GAME-0292` — The Forest](../games/s-z/the-forest.md)
- [`GAME-0285` — "The Long Dark"](../games/s-z/the-long-dark.md)

## ACT-215

- Назва: Підготувати обмежений комплект спорядження
- Переглянуто: `2026-08-24`

### Операційне визначення

Перед вилазкою або бойовим відрізком гравець заповнює обмежену кількість місць зброєю, захистом, пристроями та іншими можливостями, що відповідають вибраній схемі спорядження.

### Включає

Комплекти для рейду в ARC Raiders; прив’язані до класу комплекти перед висадженням у Battlefield 6; спорядження Crest і Tools біля Bench у Hollow Knight: Silksong.

### Виключає

Суто косметичні зміни; здобич, знайдену вже після висадження; зміну лише активного предмета швидкого доступу; вибір самого керованого героя.

### Ігри-носії

- [`GAME-0143` — ARC Raiders](../games/a-f/arc-raiders.md)
- [`GAME-0234` — Battlefield 2042](../games/a-f/battlefield-2042.md)
- [`GAME-0149` — Battlefield 6](../games/a-f/battlefield-6.md)
- [`GAME-0220` — Battlefield V](../games/a-f/battlefield-v.md)
- [`GAME-0200` — Delta Force](../games/a-f/delta-force.md)
- [`GAME-0193` — Destiny 2](../games/a-f/destiny-2.md)
- [`GAME-0159` — Helldivers 2](../games/g-l/helldivers-2.md)
- [`GAME-0150` — "Hollow Knight: Silksong"](../games/g-l/hollow-knight-silksong.md)
- [`GAME-0293` — Ori and the Will of the Wisps](../games/m-r/ori-and-the-will-of-the-wisps.md)
- [`GAME-0160` — "Pokémon Legends: Z-A"](../games/m-r/pokemon-legends-z-a.md)
- [`GAME-0174` — Tom Clancy’s Rainbow Six Siege](../games/s-z/tom-clancys-rainbow-six-siege.md)
- [`GAME-0168` — Warframe](../games/s-z/warframe.md)

## ACT-216

- Назва: Обшукати досяжний контейнер або знищену машину
- Переглянуто: `2026-08-24`

### Операційне визначення

Гравець починає обшук поблизу одного контейнера, уламка чи знищеної машини й доводить взаємодію до кінця, щоб відкрити вміст для подальшого підбирання.

### Включає

Обшук шафок, шухляд, ящиків, оболонок і знищених ARC заради матеріалів у ARC Raiders.

### Виключає

Підбирання вже видимої здобичі із землі; віддалене розкриття мапи; автоматичне збирання ресурсів після вбивства.

### Ігри-носії

- [`GAME-0143` — ARC Raiders](../games/a-f/arc-raiders.md)
- [`GAME-0285` — "The Long Dark"](../games/s-z/the-long-dark.md)

## ACT-217

- Назва: Перекласти предмет до захищеної кишені або з неї
- Переглянуто: `2026-08-24`

### Операційне визначення

Під час рейду гравець переносить відповідний предмет між наплічником і обмеженою захищеною кишенею, вміст якої не втрачається за звичайним правилом поразки.

### Включає

Перенесення предметів до Safe Pocket і з неї в ARC Raiders.

### Виключає

Звичайне впорядкування наплічника; збереження всього вантажу після успішної евакуації; перенесення забороненої зброї чи активного пристрою через помилку гри.

### Ігри-носії

- [`GAME-0143` — ARC Raiders](../games/a-f/arc-raiders.md)

## ACT-218

- Назва: Активувати точку евакуації та встигнути до виходу
- Переглянуто: `2026-08-24`

### Операційне визначення

Гравець дістається доступного засобу евакуації, викликає або розблоковує його та входить до зони відправлення до того, як точка закриється.

### Включає

Евакуаційні ліфти, виходи метро й Raider Hatches у ARC Raiders.

### Виключає

Вихід із матчу через меню; смерть на Поверхні (Topside); завершення завдання без повернення до Speranza.

### Ігри-носії

- [`GAME-0143` — ARC Raiders](../games/a-f/arc-raiders.md)
- [`GAME-0266` — Deep Rock Galactic](../games/a-f/deep-rock-galactic.md)
- [`GAME-0159` — Helldivers 2](../games/g-l/helldivers-2.md)
- [`GAME-0306` — METAL GEAR SOLID V: THE PHANTOM PAIN](../games/m-r/metal-gear-solid-v-the-phantom-pain.md)
- [`GAME-0168` — Warframe](../games/s-z/warframe.md)

## ACT-219

- Назва: Продати або розібрати один власний предмет
- Переглянуто: `2026-08-24`

### Операційне визначення

Гравець обирає власну річ і безповоротно обмінює її продажем чи розбиранням на показану кількість монет або складників.

### Включає

Продаж і розбирання у Speranza та польове розбирання (Field Recycling) на Поверхні в ARC Raiders.

### Виключає

Викидання здобичі для іншого рейдера; використання лікувального предмета; скасування виготовлення з поверненням ресурсів.

### Ігри-носії

- [`GAME-0143` — ARC Raiders](../games/a-f/arc-raiders.md)
- [`GAME-0269` — DREDGE](../games/a-f/dredge.md)
- [`GAME-0319` — Sea of Thieves](../games/s-z/sea-of-thieves.md)
- [`GAME-0307` — Slime Rancher](../games/s-z/slime-rancher.md)

## ACT-221

- Назва: Полагодити або вдосконалити власну зброю
- Переглянуто: `2026-08-24`

### Операційне визначення

У безпечному місці гравець обирає власну зброю й витрачає вказані матеріали, щоб відновити її міцність або підвищити рівень удосконалення.

### Включає

Ремонт і вдосконалення зброї в майстерні Workshop ARC Raiders; поліпшення зброї за відкритим шляхом у кузні Monster Hunter Wilds; поліпшення зброї за Smithing Stones і руни в Elden Ring.

### Виключає

Лікування в польових умовах; установлення модифікації зброї; заміну зламаної зброї іншою копією.

### Ігри-носії

- [`GAME-0143` — ARC Raiders](../games/a-f/arc-raiders.md)
- [`GAME-0152` — Elden Ring](../games/a-f/elden-ring.md)
- [`GAME-0151` — Monster Hunter Wilds](../games/m-r/monster-hunter-wilds.md)
- [`GAME-0170` — "S.T.A.L.K.E.R. 2: Heart of Chornobyl"](../games/s-z/stalker-2-heart-of-chornobyl.md)

## ACT-222

- Назва: Вчасно натиснути під час власної бойової дії
- Переглянуто: `2026-08-24`

### Операційне визначення

Після вибору атаки, Skill, лікування чи підсилення гравець натискає показану команду в потрібну мить анімації, щоб посилити, продовжити або інакше змінити цю дію.

### Включає

Натискання під час атак і Skills у Clair Obscur: Expedition 33.

### Виключає

Вибір команди чи цілі; реакцію на атаку ворога; випадковий критичний удар.

### Ігри-носії

- [`GAME-0144` — Clair Obscur: Expedition 33](../games/a-f/clair-obscur-expedition-33.md)

## ACT-223

- Назва: Обрати вчасне ухилення, парирування або стрибок
- Переглянуто: `2026-09-07`

### Операційне визначення

Під час завчасно позначеної ворожої атаки гравець у вибрану мить живої послідовності застосовує доступну захисну відповідь.

### Включає

Ухилення, парирування й відкритий згодом стрибок у Clair Obscur: Expedition 33; звичайні та ідеальні ухилення в Black Myth: Wukong; вчасні стрибки або зміна позиції проти атак стража в Hollow Knight.

### Виключає

Вибір команди ходу; пасивне ухилення; постійний захист броні.

### Ігри-носії

- [`GAME-0189` — "Black Myth: Wukong"](../games/a-f/black-myth-wukong.md)
- [`GAME-0144` — Clair Obscur: Expedition 33](../games/a-f/clair-obscur-expedition-33.md)
- [`GAME-0277` — Cuphead](../games/a-f/cuphead.md)
- [`GAME-0263` — God of War](../games/g-l/god-of-war.md)
- [`GAME-0274` — Hollow Knight](../games/g-l/hollow-knight.md)
- [`GAME-0202` — "NARAKA: BLADEPOINT"](../games/m-r/naraka-bladepoint.md)
- [`GAME-0341` — "Ninja Gaiden Black"](../games/m-r/ninja-gaiden-black.md)
- [`GAME-0293` — Ori and the Will of the Wisps](../games/m-r/ori-and-the-will-of-the-wisps.md)
- [`GAME-0162` — Path of Exile 2](../games/m-r/path-of-exile-2.md)
- [`GAME-0288` — "Sekiro™: Shadows Die Twice - GOTY Edition"](../games/s-z/sekiro-shadows-die-twice.md)
- [`GAME-0303` — Sifu](../games/s-z/sifu.md)
- [`GAME-0213` — "STAR WARS Jedi: Fallen Order"](../games/s-z/star-wars-jedi-fallen-order.md)
- [`GAME-0205` — "The Witcher 3: Wild Hunt"](../games/s-z/the-witcher-3-wild-hunt.md)
- [`GAME-0294` — V Rising](../games/s-z/v-rising.md)
- [`GAME-0197` — Valheim](../games/s-z/valheim.md)

## ACT-224

- Назва: Відпочити біля відкритої контрольної точки
- Переглянуто: `2026-09-07`

### Операційне визначення

Гравець свідомо відпочиває біля відкритої контрольної точки, щоб відновитися та прийняти пов’язані з відпочинком зміни стану світу.

### Включає

Відпочинок біля Expedition Flags у Clair Obscur: Expedition 33, біля Benches у Hollow Knight: Silksong і Hollow Knight, біля Sites of Grace в Elden Ring і біля Keeper's Shrines у Black Myth: Wukong.

### Виключає

Лише активацію контрольної точки; бойове лікування; сон у безперервній симуляції відкритого світу.

### Ігри-носії

- [`GAME-0189` — "Black Myth: Wukong"](../games/a-f/black-myth-wukong.md)
- [`GAME-0308` — Bloodborne™](../games/a-f/bloodborne.md)
- [`GAME-0144` — Clair Obscur: Expedition 33](../games/a-f/clair-obscur-expedition-33.md)
- [`GAME-0262` — DARK SOULS™ III](../games/a-f/dark-souls-iii.md)
- [`GAME-0295` — DARK SOULS™: REMASTERED](../games/a-f/dark-souls-remastered.md)
- [`GAME-0152` — Elden Ring](../games/a-f/elden-ring.md)
- [`GAME-0150` — "Hollow Knight: Silksong"](../games/g-l/hollow-knight-silksong.md)
- [`GAME-0274` — Hollow Knight](../games/g-l/hollow-knight.md)
- [`GAME-0290` — Lies of P](../games/g-l/lies-of-p.md)
- [`GAME-0299` — Nioh 2](../games/m-r/nioh-2.md)
- [`GAME-0288` — "Sekiro™: Shadows Die Twice - GOTY Edition"](../games/s-z/sekiro-shadows-die-twice.md)
- [`GAME-0213` — "STAR WARS Jedi: Fallen Order"](../games/s-z/star-wars-jedi-fallen-order.md)

## ACT-225

- Назва: Розподілити Pictos і Luminas між персонажами
- Переглянуто: `2026-08-24`

### Операційне визначення

Поза боєм гравець споряджає здобуті Pictos і вмикає вивчені Luminas, не перевищуючи кількість місць та очок кожного персонажа.

### Включає

Налаштування Pictos і Luminas окремих персонажів у Clair Obscur: Expedition 33.

### Виключає

Спорядження зброєю; витрачання Skill Point; чотири перемоги, після яких властивість Picto стає вивченою Lumina.

### Ігри-носії

- [`GAME-0144` — Clair Obscur: Expedition 33](../games/a-f/clair-obscur-expedition-33.md)

## ACT-226

- Назва: Зайняти бойове укриття або вийти з нього
- Переглянуто: `2026-08-24`

### Операційне визначення

Гравець притискає керованого героя до досяжної захисної поверхні, рухається вздовж неї, визирає з краю та свідомо залишає укриття під час бою.

### Включає

Укриття за стінами, транспортом і низькими об’єктами в Story Mode Grand Theft Auto V.

### Виключає

Лише присідання у відкритому просторі; пасивну броню; укриття, яким користуються тільки союзники під керуванням гри.

### Ігри-носії

- [`GAME-0321` — Gears of War](../games/g-l/gears-of-war.md)
- [`GAME-0145` — Grand Theft Auto V](../games/g-l/grand-theft-auto-v.md)
- [`GAME-0367` — Mass Effect 2 (Legendary Edition)](../games/m-r/mass-effect-2-legendary-edition.md)
- [`GAME-0273` — Max Payne 3](../games/m-r/max-payne-3.md)
- [`GAME-0165` — Red Dead Redemption 2](../games/m-r/red-dead-redemption-2.md)
- [`GAME-0250` — Tomb Raider (2013)](../games/s-z/tomb-raider-2013.md)

## ACT-227

- Назва: Поставити власну позначку на мапі
- Переглянуто: `2026-08-24`

### Операційне визначення

Гравець обирає відоме місце на мапі як власний орієнтир, а навігація показує позначку або прокладає до неї маршрут без автоматичного пересування героя.

### Включає

Власні позначки й дорожні маршрути в Story Mode Grand Theft Auto V та Cyberpunk 2077; позначки й маяки, видимі на мапі або компасі Elden Ring.

### Виключає

Наказ рухатися автоматично; позначки завдань, які встановлює сама гра; проєктування транспортної мережі.

### Ігри-носії

- [`GAME-0289` — American Truck Simulator](../games/a-f/american-truck-simulator.md)
- [`GAME-0152` — Elden Ring](../games/a-f/elden-ring.md)
- [`GAME-0169` — Euro Truck Simulator 2](../games/a-f/euro-truck-simulator-2.md)
- [`GAME-0171` — Forza Horizon 6](../games/a-f/forza-horizon-6.md)
- [`GAME-0145` — Grand Theft Auto V](../games/g-l/grand-theft-auto-v.md)
- [`GAME-0165` — Red Dead Redemption 2](../games/m-r/red-dead-redemption-2.md)

## ACT-228

- Назва: Передати керування іншому доступному героєві
- Переглянуто: `2026-08-24`

### Операційне визначення

Гравець обирає іншого доступного сюжетного героя й одразу перебирає керування його рухом, боєм і взаємодіями, не починаючи нового збереження чи мережевої сесії.

### Включає

Перемикання між Michael, Franklin і Trevor під час вільного дослідження та у визначені миті місій Story Mode Grand Theft Auto V.

### Виключає

Зміну зовнішності аватара; наказ союзникові під керуванням гри; вибір персонажа в покроковій групі.

### Ігри-носії

- [`GAME-0324` — Contra Force](../games/a-f/contra-force.md)
- [`GAME-0145` — Grand Theft Auto V](../games/g-l/grand-theft-auto-v.md)

## ACT-229

- Назва: Увімкнути особливу здібність керованого героя
- Переглянуто: `2026-08-24`

### Операційне визначення

Гравець використовує готовий особливий ресурс героя, щоб на певний час увійти в його бойову форму або отримати модифікатор під час водіння.

### Включає

Стрілецьку концентрацію Michael, водійську концентрацію Franklin і лють Trevor у Story Mode Grand Theft Auto V; Red Tides у Black Myth: Wukong.

### Виключає

Пасивні характеристики; чит-коди; дії Quickplay у GTA Online.

### Ігри-носії

- [`GAME-0189` — "Black Myth: Wukong"](../games/a-f/black-myth-wukong.md)
- [`GAME-0222` — "Call of Juarez: Gunslinger"](../games/a-f/call-of-juarez-gunslinger.md)
- [`GAME-0145` — Grand Theft Auto V](../games/g-l/grand-theft-auto-v.md)
- [`GAME-0238` — "Max Payne (2001)"](../games/m-r/max-payne-2001.md)
- [`GAME-0273` — Max Payne 3](../games/m-r/max-payne-3.md)
- [`GAME-0226` — "Need for Speed: Most Wanted (2005)"](../games/m-r/need-for-speed-most-wanted-2005.md)

## ACT-230

- Назва: Вибрати підхід і команду для пограбування
- Переглянуто: `2026-08-24`

### Операційне визначення

На дошці планування гравець обирає один підхід до пограбування та призначає відкритих фахівців на всі потрібні ролі до початку підготовки або виконання.

### Включає

Вибір підходу, стрільця, водія й хакера для великих пограбувань у Story Mode Grand Theft Auto V.

### Виключає

Перемикання героя під час виконання; мережеве лобі; суто косметичний вибір команди.

### Ігри-носії

- [`GAME-0145` — Grand Theft Auto V](../games/g-l/grand-theft-auto-v.md)

## ACT-231

- Назва: Обрати життєвий шлях і розподілити початкові характеристики
- Переглянуто: `2026-08-24`

### Операційне визначення

Перед початком кампанії гравець обирає одне походження персонажа й розподіляє встановлений запас початкових очок між характеристиками, які зберігаються під час проходження.

### Включає

Вибір життєвого шляху Кочівника, Дитяти вулиць або Корпората та початковий розподіл п’яти характеристик — Сили, Інтелекту, Реакції, Техніки й Холоднокровності — у Cyberpunk 2077.

### Виключає

Косметичну зовнішність; подальше витрачання очок характеристик; вибір тимчасової відповіді в діалозі.

### Ігри-носії

- [`GAME-0146` — Cyberpunk 2077](../games/a-f/cyberpunk-2077.md)

## ACT-232

- Назва: Обрати одну репліку або рішення в завданні
- Переглянуто: `2026-08-24`

### Операційне визначення

Під час розмови чи важливого рішення гравець підтверджує один із доступних варіантів, наслідок якого може змінити відомості, стосунки, поточне завдання або пізнішу сюжетну гілку.

### Включає

Варіанти діалогів, обмежені часом відповіді й рішення прийняти маршрут Hanako під час Nocturne Op55N1 в основній грі Cyberpunk 2077.

### Виключає

Необов’язкові репліки для колориту без зміни стану; купівлю предмета з каталогу; розподіл очка персонажа.

### Ігри-носії

- [`GAME-0148` — Baldur’s Gate 3](../games/a-f/baldurs-gate-3.md)
- [`GAME-0146` — Cyberpunk 2077](../games/a-f/cyberpunk-2077.md)
- [`GAME-0252` — "Detroit: Become Human"](../games/a-f/detroit-become-human.md)
- [`GAME-0353` — "Deus Ex: Game of the Year Edition"](../games/a-f/deus-ex-game-of-the-year-edition.md)
- [`GAME-0264` — Disco Elysium - The Final Cut](../games/a-f/disco-elysium-the-final-cut.md)
- [`GAME-0301` — "Divinity: Original Sin 2 - Definitive Edition"](../games/a-f/divinity-original-sin-2-definitive-edition.md)
- [`GAME-0327` — Fable](../games/a-f/fable.md)
- [`GAME-0231` — Fallout 4](../games/a-f/fallout-4.md)
- [`GAME-0361` — Fallout: New Vegas](../games/a-f/fallout-new-vegas.md)
- [`GAME-0240` — "Kingdom Come: Deliverance II"](../games/g-l/kingdom-come-deliverance-ii.md)
- [`GAME-0388` — L.A. Noire](../games/g-l/la-noire.md)
- [`GAME-0367` — Mass Effect 2 (Legendary Edition)](../games/m-r/mass-effect-2-legendary-edition.md)
- [`GAME-0194` — "Mount & Blade II: Bannerlord"](../games/m-r/mount-and-blade-ii-bannerlord.md)
- [`GAME-0385` — 'Phoenix Wright: Ace Attorney'](../games/m-r/phoenix-wright-ace-attorney.md)
- [`GAME-0170` — "S.T.A.L.K.E.R. 2: Heart of Chornobyl"](../games/s-z/stalker-2-heart-of-chornobyl.md)
- [`GAME-0331` — Starfield](../games/s-z/starfield.md)
- [`GAME-0362` — "The Elder Scrolls III: Morrowind"](../games/s-z/the-elder-scrolls-iii-morrowind.md)
- [`GAME-0343` — The Secret of Monkey Island](../games/s-z/the-secret-of-monkey-island.md)
- [`GAME-0205` — "The Witcher 3: Wild Hunt"](../games/s-z/the-witcher-3-wild-hunt.md)

## ACT-233

- Назва: Просканувати ціль і запустити один скрипт
- Переглянуто: `2026-08-24`

### Операційне визначення

Гравець утримує сканер на підтримуваній людині, пристрої чи транспорті, обирає доступний скрипт і запускає його через установлену кібердеку.

### Включає

Бойові, потайні й пристроєві скрипти в основній грі Cyberpunk 2077.

### Виключає

Постріл зі зброї; пасивне виявлення цілі; вибір відповіді в діалозі; злам без установленої сумісної операційної системи.

### Ігри-носії

- [`GAME-0146` — Cyberpunk 2077](../games/a-f/cyberpunk-2077.md)

## ACT-234

- Назва: Установити, замінити або поліпшити кіберімплант
- Переглянуто: `2026-08-24`

### Операційне визначення

В інтерфейсі ріпера гравець купує, установлює, знімає, замінює чи поліпшує імплант у відповідній комірці тіла, не перевищуючи доступну місткість.

### Включає

Налаштування кіберімплантів через спеціаліста починаючи з версії 2.0 Cyberpunk 2077.

### Виключає

Спорядження переносною зброєю; суто косметичні зміни гардероба; розподіл очка характеристики чи здібності.

### Ігри-носії

- [`GAME-0146` — Cyberpunk 2077](../games/a-f/cyberpunk-2077.md)

## ACT-235

- Назва: Зблизька знешкодити досяжного ворога до виявлення
- Переглянуто: `2026-09-10`

### Операційне визначення

Із відповідної близької позиції поза активним виявленням гравець смертельно чи несмертельно знешкоджує одного ворога замість звичайної атаки у відкритому бою; захоплення або подальше переміщення тіла є параметрами носія.

### Включає

Приховані захоплення й нейтралізації в Cyberpunk 2077; смертельні удари по ворогу, який не помітив гравця, у Sekiro.

### Виключає

Удари ближнього бою проти настороженого ворога; затримання, яке відбувається лише в розмові; віддалений запуск скрипту.

### Ігри-носії

- [`GAME-0255` — "Batman: Arkham Asylum Game of the Year Edition"](../games/a-f/batman-arkham-asylum-game-of-the-year-edition.md)
- [`GAME-0243` — Battlefield Hardline](../games/a-f/battlefield-hardline.md)
- [`GAME-0146` — Cyberpunk 2077](../games/a-f/cyberpunk-2077.md)
- [`GAME-0247` — Dishonored (2012)](../games/a-f/dishonored-2012.md)
- [`GAME-0236` — Far Cry 3](../games/a-f/far-cry-3.md)
- [`GAME-0271` — Far Cry 5](../games/a-f/far-cry-5.md)
- [`GAME-0248` — HITMAN World of Assassination](../games/g-l/hitman-world-of-assassination.md)
- [`GAME-0306` — METAL GEAR SOLID V: THE PHANTOM PAIN](../games/m-r/metal-gear-solid-v-the-phantom-pain.md)
- [`GAME-0260` — Metro Exodus](../games/m-r/metro-exodus.md)
- [`GAME-0249` — Resident Evil 4 (2023 remake)](../games/m-r/resident-evil-4-2023.md)
- [`GAME-0288` — "Sekiro™: Shadows Die Twice - GOTY Edition"](../games/s-z/sekiro-shadows-die-twice.md)
- [`GAME-0261` — The Last of Us Part I](../games/s-z/the-last-of-us-part-i.md)
- [`GAME-0250` — Tomb Raider (2013)](../games/s-z/tomb-raider-2013.md)

## ACT-236

- Назва: Використати один відновлюваний заряд бойового предмета
- Переглянуто: `2026-08-24`

### Операційне визначення

Гравець витрачає готовий заряд спорядженого лікувального предмета чи гранати, за потреби прицілюючись, але сам багаторазовий предмет не зникає назавжди.

### Включає

Заряди лікувальних предметів і гранат у Cyberpunk 2077 починаючи з оновлення 2.0.

### Виключає

Витрачання обмеженого стосу одноразових предметів; постріл зі зброї; пасивне відновлення здоров’я; використання заряду, який ще відновлюється.

### Ігри-носії

- [`GAME-0146` — Cyberpunk 2077](../games/a-f/cyberpunk-2077.md)

## ACT-237

- Назва: Обрати героя й варіант Team-Up у кімнаті появи
- Переглянуто: `2026-08-24`

### Операційне визначення

Перед виходом із кімнати появи гравець обирає одного вільного героя й один із запропонованих варіантів Team-Up. Обраний герой переходить під пряме керування та отримує основний ефект цього варіанта.

### Включає

Початковий вибір героя у Quick Match Marvel Rivals, зміну героя під час матчу через кімнату появи та вибір одного з двох варіантів Team-Up у Season 9.

### Виключає

Драфт, що закріплює одного героя на весь матч; вибір косметичного образу; тимчасове копіювання іншого героя ультимативною здібністю.

### Ігри-носії

- [`GAME-0147` — Marvel Rivals](../games/m-r/marvel-rivals.md)

## ACT-238

- Назва: Створити власного персонажа для кампанії
- Переглянуто: `2026-08-24`

### Операційне визначення

Перед початком кампанії гравець обирає расу або підрасу, клас, передісторію, характеристики та володіння навичками. Підтверджений набір визначає початкові можливості нового персонажа.

### Включає

Створення власного Tav у Baldur’s Gate 3: раса чи підраса, клас, передісторія, розподіл 27 очок характеристик, володіння навичками та початкові рішення.

### Виключає

Косметичну зовнішність; вибір готового персонажа Origin; подальше підвищення рівня, поєднання класів або зміну спорядження.

### Ігри-носії

- [`GAME-0148` — Baldur’s Gate 3](../games/a-f/baldurs-gate-3.md)
- [`GAME-0194` — "Mount & Blade II: Bannerlord"](../games/m-r/mount-and-blade-ii-bannerlord.md)
- [`GAME-0362` — "The Elder Scrolls III: Morrowind"](../games/s-z/the-elder-scrolls-iii-morrowind.md)

## ACT-240

- Назва: Обрати доступне командне місце висадження й повернутися до бою
- Переглянуто: `2026-08-24`

### Операційне визначення

Коли безпосереднє керування бійцем недоступне, гравець обирає в інтерфейсі одне місце, яке зараз відповідає умовам висадження команди, і повертає туди підготовленого бійця.

### Включає

Висадження в Conquest Battlefield 6 зі штабу, утримуваної точки, біля бійця загону поза боєм чи Deploy Beacon або у вільне місце техніки.

### Виключає

Пересування пішки з наявної позиції; автоматичне відродження на контрольній точці; установлення самого місця висадження.

### Ігри-носії

- [`GAME-0234` — Battlefield 2042](../games/a-f/battlefield-2042.md)
- [`GAME-0149` — Battlefield 6](../games/a-f/battlefield-6.md)
- [`GAME-0220` — Battlefield V](../games/a-f/battlefield-v.md)
- [`GAME-0200` — Delta Force](../games/a-f/delta-force.md)

## ACT-241

- Назва: Оживити або перемістити пораненого союзника
- Переглянуто: `2026-08-27`

### Операційне визначення

Гравець взаємодіє з досяжним пораненим союзником, за наявності такого правила може перемістити його й завершує оживлення або застосовує миттєвий засіб до завершення відведеного часу.

### Включає

Оживлення бійця свого загону будь-яким класом, командне оживлення класом Support, перетягування в укриття й завершене застосування Defibrillator у Battlefield 6; оживлення збитого з ніг союзника в Apex Legends.

### Виключає

Самолікування; повернення після смерті; перенесення предмета цілі; воскресіння персонажа після смерті в кампанії.

### Ігри-носії

- [`GAME-0154` — Apex Legends](../games/a-f/apex-legends.md)
- [`GAME-0234` — Battlefield 2042](../games/a-f/battlefield-2042.md)
- [`GAME-0149` — Battlefield 6](../games/a-f/battlefield-6.md)
- [`GAME-0220` — Battlefield V](../games/a-f/battlefield-v.md)
- [`GAME-0200` — Delta Force](../games/a-f/delta-force.md)
- [`GAME-0321` — Gears of War](../games/g-l/gears-of-war.md)
- [`GAME-0192` — Left 4 Dead 2](../games/g-l/left-4-dead-2.md)
- [`GAME-0201` — PAYDAY 2](../games/m-r/payday-2.md)
- [`GAME-0232` — PAYDAY 3](../games/m-r/payday-3.md)
- [`GAME-0174` — Tom Clancy’s Rainbow Six Siege](../games/s-z/tom-clancys-rainbow-six-siege.md)

## ACT-243

- Назва: Викликати Seikret, сісти верхи й вибрати відстежувану ціль
- Переглянуто: `2026-08-24`

### Операційне визначення

Гравець викликає Seikret, сідає верхи або спішується та може вибрати поточну відстежувану ціль для автоматичної подорожі, не втрачаючи можливості керувати рухом вручну.

### Включає

Виклик і їзду на Seikret у Monster Hunter Wilds до цілі завдання, позначки мапи чи відстежуваного монстра.

### Виключає

Безпосереднє пересування мисливця пішки; швидке переміщення без проходження шляху; супутника, на якому не можна їхати.

### Ігри-носії

- [`GAME-0151` — Monster Hunter Wilds](../games/m-r/monster-hunter-wilds.md)

## ACT-244

- Назва: Поміняти активну зброю на запасну з Seikret
- Переглянуто: `2026-08-24`

### Операційне визначення

Під час їзди гравець бере із Seikret одну призначену запасну зброю, а поточну активну зброю залишає замість неї.

### Включає

Обмін двох вибраних для поля видів зброї на Seikret у Monster Hunter Wilds.

### Виключає

Вибір будь-якої зброї зі сховища табору; перезаряджання боєприпасів; зміну лише вигляду зброї.

### Ігри-носії

- [`GAME-0151` — Monster Hunter Wilds](../games/m-r/monster-hunter-wilds.md)

## ACT-245

- Назва: Зібрати або вирізати одну досяжну порцію матеріалу
- Переглянуто: `2026-08-24`

### Операційне визначення

Гравець взаємодіє з досяжним польовим джерелом або тушею переможеного монстра, щоб перенести до інвентарю одну з порцій матеріалу, які там іще лишилися.

### Включає

Збирання рослин, руди чи кісток у Monster Hunter Wilds і вирізання матеріалів із туші великого монстра, доки вона доступна.

### Виключає

Автоматичне підбирання під час дотику; нагороди завдання без окремої взаємодії у світі; руйнування рельєфу заради випадіння.

### Ігри-носії

- [`GAME-0278` — DAVE THE DIVER](../games/a-f/dave-the-diver.md)
- [`GAME-0269` — DREDGE](../games/a-f/dredge.md)
- [`GAME-0314` — Grounded](../games/g-l/grounded.md)
- [`GAME-0240` — "Kingdom Come: Deliverance II"](../games/g-l/kingdom-come-deliverance-ii.md)
- [`GAME-0297` — 'MONSTER HUNTER RISE'](../games/m-r/monster-hunter-rise.md)
- [`GAME-0151` — Monster Hunter Wilds](../games/m-r/monster-hunter-wilds.md)
- [`GAME-0207` — 'Monster Hunter: World'](../games/m-r/monster-hunter-world.md)
- [`GAME-0165` — Red Dead Redemption 2](../games/m-r/red-dead-redemption-2.md)
- [`GAME-0305` — Sons Of The Forest](../games/s-z/sons-of-the-forest.md)
- [`GAME-0178` — Subnautica](../games/s-z/subnautica.md)
- [`GAME-0292` — The Forest](../games/s-z/the-forest.md)
- [`GAME-0205` — "The Witcher 3: Wild Hunt"](../games/s-z/the-witcher-3-wild-hunt.md)

## ACT-246

- Назва: Спрямувати й виконати Focus Strike поточної зброї
- Переглянуто: `2026-08-24`

### Операційне визначення

У Focus Mode гравець наводить властивий поточній зброї Focus Strike на підсвічену відкриту рану або відповідну ламку частину тіла й виконує удар.

### Включає

Focus Strikes у Monster Hunter Wilds, спрямовані на відкриту рану чи відповідну ламку частину монстра.

### Виключає

Звичайні повторювані атаки; саме підсвічування ран; Focus Strike, який не дістає до цілі.

### Ігри-носії

- [`GAME-0151` — Monster Hunter Wilds](../games/m-r/monster-hunter-wilds.md)

## ACT-247

- Назва: Викликати й безпосередньо вести особистого польового скакуна
- Переглянуто: `2026-09-13`

### Операційне визначення

Гравець викликає доступного особистого польового скакуна, переходить у стан їзди або виходить із нього та сам керує рухом по землі, стрибками й дозволеними діями верхи.

### Включає

Виклик і їзду верхи на Torrent у дослідженій Limgrave в Elden Ring; виклик, посадку, керування, ривок і спішування зі стартового Palamute під час першого Village-полювання в MONSTER HUNTER RISE.

### Виключає

Рух Seikret за автоматичним маршрутом до цілі; автономний транспорт; швидке переміщення.

### Ігри-носії

- [`GAME-0152` — Elden Ring](../games/a-f/elden-ring.md)
- [`GAME-0306` — METAL GEAR SOLID V: THE PHANTOM PAIN](../games/m-r/metal-gear-solid-v-the-phantom-pain.md)
- [`GAME-0297` — 'MONSTER HUNTER RISE'](../games/m-r/monster-hunter-rise.md)

## ACT-248

- Назва: Підвищити вибраний атрибут на один рівень за руни
- Переглянуто: `2026-08-24`

### Операційне визначення

Біля відповідного Site of Grace гравець вибирає один атрибут персонажа й витрачає показану кількість рун, щоб підвищити його на одиницю.

### Включає

Підвищення Vigor, Mind або іншого атрибута після угоди з Melina в Elden Ring.

### Виключає

Автоматичне підвищення рівня за досвід; придбання навички; поліпшення зброї.

### Ігри-носії

- [`GAME-0152` — Elden Ring](../games/a-f/elden-ring.md)

## ACT-249

- Назва: Повернути валюту з місця попередньої смерті
- Переглянуто: `2026-09-05`

### Операційне визначення

Гравець дістається єдиного поточного місця загибелі й торкається світного сліду, щоб знову додати залишений там запас витратної валюти до запасу персонажа.

### Включає

Повернення втрачених рун в Elden Ring до наступної смерті персонажа; дотик до кривавої плями в дослідженому маршруті DARK SOULS III, щоб забрати залишені там душі.

### Виключає

Звичайне підбирання здобичі; пошук інвентарю тіла; повернення Rosaries із Cocoon.

### Ігри-носії

- [`GAME-0308` — Bloodborne™](../games/a-f/bloodborne.md)
- [`GAME-0262` — DARK SOULS™ III](../games/a-f/dark-souls-iii.md)
- [`GAME-0295` — DARK SOULS™: REMASTERED](../games/a-f/dark-souls-remastered.md)
- [`GAME-0152` — Elden Ring](../games/a-f/elden-ring.md)
- [`GAME-0290` — Lies of P](../games/g-l/lies-of-p.md)
- [`GAME-0299` — Nioh 2](../games/m-r/nioh-2.md)

## ACT-250

- Назва: Викликати духів із вибраного Spirit Ash
- Переглянуто: `2026-08-24`

### Операційне визначення

У зоні зі знаком виклику гравець витрачає потрібну кількість FP і закликає одного духа або групу духів із вибраного Spirit Ash.

### Включає

Виклик Spirit Jellyfish та інших ранніх Spirit Ash у дозволених польових зонах і боях із босами Elden Ring.

### Виключає

Союзників онлайн; знаки виклику NPC; безпосередньо керованих супутників.

### Ігри-носії

- [`GAME-0152` — Elden Ring](../games/a-f/elden-ring.md)

## ACT-251

- Назва: Призначити зброї Ash of War і доступну властивість
- Переглянуто: `2026-08-24`

### Операційне визначення

У відповідному меню гравець вибирає здобутий Ash of War, сумісну зброю та одну доступну для неї властивість.

### Включає

Призначення Storm Stomp і властивості Standard за допомогою Whetstone Knife на початку Elden Ring.

### Виключає

Виконання самої навички; підвищення рівня зброї; запам’ятовування закляття.

### Ігри-носії

- [`GAME-0152` — Elden Ring](../games/a-f/elden-ring.md)

## ACT-253

- Назва: Повернути загиблого союзника через одне джерело відновлення
- Переглянуто: `2026-08-27`

### Операційне визначення

Поки хоча б один учасник загону лишається активним, гравець застосовує поточний предмет або стан відновлення загиблого союзника до одного дозволеного джерела повернення.

### Включає

Повернення через контейнер смерті або ланцюг із Legend Banner, Replicator і Respawn Beacon в Apex Legends.

### Виключає

Оживлення союзника, якого лише збили з ніг; автоматичне повернення між раундами; воскресіння на рівні облікового запису.

### Ігри-носії

- [`GAME-0154` — Apex Legends](../games/a-f/apex-legends.md)
- [`GAME-0159` — Helldivers 2](../games/g-l/helldivers-2.md)

## ACT-254

- Назва: Вибрати одне обов’язкове благословення Ancient на початку акту
- Переглянуто: `2026-08-27`

### Операційне визначення

Перед початком маршруту акту гравець вибирає рівно один предмет з обмеженої пропозиції поточного Ancient і закріплює його тривалий ефект за забігом.

### Включає

Вибір однієї з трьох запропонованих реліквій Ancient на початку акту Slay the Spire 2.

### Виключає

Необов’язкову карткову нагороду після бою; платну покупку; автоматичне відкриття за віху; випадковий вибір того, який Ancient з’явиться.

### Ігри-носії

- [`GAME-0155` — Slay the Spire 2](../games/s-z/slay-the-spire-2.md)

## ACT-255

- Назва: Провести й надіслати слово шляхом через сусідні літери
- Переглянуто: `2026-08-27`

### Операційне визначення

Гравець починає на будь-якій допустимій літерній клітинці, проводить упорядковану послідовність довільної довжини через послідовно сусідні різні клітинки й надсилає утворене слово як одну складену пропозицію.

### Включає

Тематичне слово, spangram або допустиме нетематичне слово в Strands, проведене через сусідні по горизонталі, вертикалі чи діагоналі клітинки.

### Виключає

Введення слова без вибору його просторового маршруту; шлях від незмінної стартової точки; вибір роз’єднаних літер; просте підсвічування маршруту, який відкрила система.

### Ігри-носії

- [`GAME-0156` — Strands](../games/s-z/strands.md)

## ACT-256

- Назва: Виконати свою половину парної взаємодії
- Переглянуто: `2026-08-27`

### Операційне визначення

Один керований людиною персонаж подає свою локально допустиму команду до взаємодії зі світом, просування якої залежить від окремо керованого партнера з доповнювальною командою, а не від повторення обох кроків одним персонажем.

### Включає

Один гравець Split Fiction працює зі своєю стороною одночасної консолі, парного руків’я, однією з двох плит або своєю частиною спільних дверей, а інший подає другу потрібну команду.

### Виключає

Звичайний перемикач, який перемикає один персонаж; автоматичного супутника, що виконує другу команду; незалежні атаки двох гравців по одній цілі; утримування механізму, який уже відкрив одиночний маршрут.

### Ігри-носії

- [`GAME-0157` — Split Fiction](../games/s-z/split-fiction.md)

## ACT-257

- Назва: Спрямувати активного мешканця до контекстної взаємодії
- Переглянуто: `2026-08-27`

### Операційне визначення

Гравець вибирає активного постійного мешканця, указує допустимого іншого мешканця, об’єкт або ділянку та наказує виконати одну запропоновану соціальну, побутову чи світову взаємодію.

### Включає

Спрямування Farrah Nouvel познайомитися, поговорити, запросити Sim, скористатися побутовим об’єктом або виконати іншу запропоновану взаємодію базової гри The Sims 4.

### Виключає

Безпосереднє керування кожним кроком; загальний пріоритет роботи колонії; вибір авторської репліки без симульованого стану актора.

### Ігри-носії

- [`GAME-0383` — The Sims 2: Legacy Collection](../games/s-z/the-sims-2-legacy-collection.md)
- [`GAME-0158` — The Sims 4](../games/s-z/the-sims-4.md)

## ACT-258

- Назва: Перемкнути активного бойового компаньйона з команди
- Переглянуто: `2026-08-27`

### Операційне визначення

Під час бою гравець вибирає іншого допустимого живого члена команди, який замінює єдиного поточного керованого компаньйона, тоді як обидва зберігають власні здоров’я, стан, рівень і прийоми.

### Включає

Добровільну або вимушену після непритомності заміну Pokémon у Pokémon Legends: Z-A та Pokémon Red Version.

### Виключає

Перенесення між сховищем Boxes і командою; відкликання без заміни; зміну прямого керування людьми.

### Ігри-носії

- [`GAME-0160` — "Pokémon Legends: Z-A"](../games/m-r/pokemon-legends-z-a.md)
- [`GAME-0336` — "Pokémon Red Version"](../games/m-r/pokemon-red-version.md)

## ACT-259

- Назва: Вибрати одного постійного стартового компаньйона
- Переглянуто: `2026-08-27`

### Операційне визначення

На початку кампанії гравець приймає рівно одного учасника обмеженої пропозиції, і його особа та початковий набір стають постійною власністю команди.

### Включає

Вибір Chikorita, Tepig або Totodile у Pokémon Legends: Z-A.

### Виключає

Героя лише на матч; косметику; пізніше захоплення у світі.

### Ігри-носії

- [`GAME-0160` — "Pokémon Legends: Z-A"](../games/m-r/pokemon-legends-z-a.md)
- [`GAME-0336` — "Pokémon Red Version"](../games/m-r/pokemon-red-version.md)

## ACT-260

- Назва: Утримувати одну доступну взаємодію вцілілого
- Переглянуто: `2026-08-27`

### Операційне визначення

Безпосередньо керований вцілілий утримує контекстну взаємодію з досяжною ціллю або союзником, а поступ зростає лише за сумісного стану й неперерваної дії.

### Включає

Ремонт генератора, лікування чи піднімання союзника, зняття з гака та роботу із заживленим перемикачем воріт у Dead by Daylight.

### Виключає

Пересування; миттєве опускання палети; піднімання вцілілого вбивцею; автономно доручену роботу.

### Ігри-носії

- [`GAME-0161` — Dead by Daylight](../games/a-f/dead-by-daylight.md)
- [`GAME-0192` — Left 4 Dead 2](../games/g-l/left-4-dead-2.md)

## ACT-261

- Назва: Вчасно натиснути, поки рухомий покажчик у показаному проміжку успіху
- Переглянуто: `2026-09-06`

### Операційне визначення

Під час тривалої взаємодії гравець один раз натискає, коли рухомий покажчик перетинає показаний проміжок успіху, й отримує один із градуйованих результатів, не обираючи нової цілі.

### Включає

Добру, відмінну й невдалу перевірку навички під час ремонту або лікування в Dead by Daylight; підсічку в мить, коли рухома позначка перетинає показаний проміжок, у визначеному першому дні DREDGE.

### Виключає

Парирування атаки всередині обраної бойової дії; повну ритмічну послідовність, ноти якої і є метою; пасивну випадкову перевірку без введення гравця.

### Ігри-носії

- [`GAME-0161` — Dead by Daylight](../games/a-f/dead-by-daylight.md)
- [`GAME-0269` — DREDGE](../games/a-f/dredge.md)

## ACT-262

- Назва: Опустити одну підняту палету під час переслідування
- Переглянуто: `2026-08-27`

### Операційне визначення

Керований утікач переводить досяжну підняту палету в опущений стан, створюючи сталу місцеву перешкоду та коротке вікно можливого удару по переслідувачу.

### Включає

Опускання палети вцілілим з оглушенням убивці або без нього в Dead by Daylight.

### Виключає

Перестрибування; руйнування палети вбивцею; установлення перенесеної будівельної деталі.

### Ігри-носії

- [`GAME-0161` — Dead by Daylight](../games/a-f/dead-by-daylight.md)

## ACT-263

- Назва: Вигравіювати вибране вміння або підтримку з необробленого каменю
- Переглянуто: `2026-08-27`

### Операційне визначення

Гравець витрачає один необроблений камінь, вибирає одне з допустимих запропонованих умінь або одну підтримку й отримує відповідний камінь.

### Включає

Гравіювання каменів умінь і підтримки з необроблених каменів у Path of Exile 2.

### Виключає

Вставлення готового каменю підтримки; автоматичне вивчення під час підвищення рівня.

### Ігри-носії

- [`GAME-0162` — Path of Exile 2](../games/m-r/path-of-exile-2.md)

## ACT-264

- Назва: Вставити або вийняти сумісний камінь підтримки
- Переглянуто: `2026-08-27`

### Операційне визначення

Гравець переносить камінь підтримки у вільне допустиме гніздо вибраного активного вміння або виймає його, змінюючи складену поведінку вміння.

### Включає

Керування гніздами підтримки у Path of Exile 2.

### Виключає

Гравіювання каменю; заміна спорядження; вибір пасивного вузла.

### Ігри-носії

- [`GAME-0162` — Path of Exile 2](../games/m-r/path-of-exile-2.md)

## ACT-265

- Назва: Застосувати валютний предмет до допустимої речі
- Переглянуто: `2026-08-27`

### Операційне визначення

Гравець вибирає валютний предмет і цільову річ, витрачаючи валюту на заявлену зміну рідкості, властивості або гнізда.

### Включає

Звичайне ремесло валютними предметами у Path of Exile 2.

### Виключає

Купівля у торговця; споряджання; зовнішній обчислювач.

### Ігри-носії

- [`GAME-0162` — Path of Exile 2](../games/m-r/path-of-exile-2.md)

## ACT-266

- Назва: Активувати заряджений флакон відновлення
- Переглянуто: `2026-08-27`

### Операційне визначення

Гравець активує споряджений флакон здоров’я або мани, негайно витрачає заряди й запускає відновлення, не втрачаючи сам предмет.

### Включає

Флакони здоров’я й мани в кампанії Path of Exile 2.

### Виключає

Перериване споживання їжі; пасивне відновлення; одноразове зілля.

### Ігри-носії

- [`GAME-0162` — Path of Exile 2](../games/m-r/path-of-exile-2.md)

## ACT-267

- Назва: Спрямувати передачу м’яча до допустимого партнера
- Переглянуто: `2026-08-27`

### Операційне визначення

Керуючи власником м’яча, гравець задає напрям, силу й тип передачі, а система визначає адресата та траєкторію.

### Включає

Низові, розрізні й навісні передачі та подачі у EA SPORTS FC 26.

### Виключає

Удар по воротах; автономне винесення; призначення місця для пошуку шляху.

### Ігри-носії

- [`GAME-0163` — EA SPORTS FC 26](../games/a-f/ea-sports-fc-26.md)

## ACT-268

- Назва: Спрямувати удар по воротах суперника
- Переглянуто: `2026-08-27`

### Операційне визначення

Керуючи допустимим нападником, гравець виконує удар, призначений провести живий м’яч через ворота суперника.

### Включає

Звичайні, обвідні, перекидні удари й удари головою у EA SPORTS FC 26.

### Виключає

Передача партнерові; серія післяматчевих пенальті; автономне винесення м’яча.

### Ігри-носії

- [`GAME-0163` — EA SPORTS FC 26](../games/a-f/ea-sports-fc-26.md)

## ACT-269

- Назва: Виконати допустиму спробу відбору
- Переглянуто: `2026-08-27`

### Операційне визначення

Керований захисник виконує відбір стоячи, поштовх плечем або підкат, щоб відібрати чи перехопити живий м’яч.

### Включає

Своєчасні відбори у EA SPORTS FC 26.

### Виключає

Автоматична опіка; простий рух; бій із запасом здоров’я.

### Ігри-носії

- [`GAME-0163` — EA SPORTS FC 26](../games/a-f/ea-sports-fc-26.md)

## ACT-270

- Назва: Установити одну доступну бомбу із запалом
- Переглянуто: `2026-09-21`

### Операційне визначення

Коли керований персонаж перебуває в сумісному стані, гравець установлює одну живу місцеву вибухівку зі скінченного перенесеного запасу або зі збереженої багаторазової здібності й запускає її запал.

### Включає

Установлення звичайної бомби в базовій The Binding of Isaac: Rebirth; установлення багаторазової Bomb у формі Morphing Ball у Super Metroid.

### Виключає

Кинута тактична граната; вибуховий снаряд; автоматичний вибух від предмета без витрати перенесеної бомби.

### Ігри-носії

- [`GAME-0387` — Super Bomberman](../games/s-z/super-bomberman.md)
- [`GAME-0337` — Super Metroid](../games/s-z/super-metroid.md)
- [`GAME-0164` — "The Binding of Isaac: Rebirth"](../games/s-z/the-binding-of-isaac-rebirth.md)

## ACT-271

- Назва: Підкликати постійного власного скакуна до керованого персонажа
- Переглянуто: `2026-09-10`

### Операційне визначення

Коли керований персонаж не сидить верхи, а його поточний постійний власний скакун може відгукнутися, гравець дистанційною командою просить скакуна самостійно наблизитися, не перебираючи керування ним і не переходячи до їзди.

### Включає

Свист, яким Артур підкликає свого поточного осідланого коня протягом визначеного маршруту розділу 2 Red Dead Redemption 2.

### Виключає

Посадку верхи, безпосередню їзду чи спішування (ACT-348); виклик спектрального скакуна з переходом до їзди однією активацією (ACT-247); автоматичний кінний маршрут (ACT-243); повернення звичайного автономного супутника; швидку подорож.

### Ігри-носії

- [`GAME-0165` — Red Dead Redemption 2](../games/m-r/red-dead-redemption-2.md)
- [`GAME-0356` — Shadow of the Colossus](../games/s-z/shadow-of-the-colossus.md)

## ACT-272

- Назва: Чистити власну вогнепальну зброю збройовою оливою
- Переглянуто: `2026-08-27`

### Операційне визначення

Гравець оглядає власну вогнепальну зброю й витрачає одну одиницю збройової оливи, щоб відновити її поточну справність.

### Включає

Польове чищення зброї в розділі 2.

### Виключає

Перезаряджання; платну послугу зброяра; ремонт у центральній зоні; косметичну деталь.

### Ігри-носії

- [`GAME-0165` — Red Dead Redemption 2](../games/m-r/red-dead-redemption-2.md)

## ACT-273

- Назва: Передавати придатні цінності спільному табору банди
- Переглянуто: `2026-08-27`

### Операційне визначення

Гравець обирає особисті гроші, коштовність, харчі або тушу й безповоротно передає їх до спільних коштів чи припасів табору.

### Включає

Скриньку пожертв у Horseshoe Overlook і придатні пожертви Пірсону.

### Виключає

Купівлю через журнал; продаж за особисті гроші; немеханічний подарунок.

### Ігри-носії

- [`GAME-0165` — Red Dead Redemption 2](../games/m-r/red-dead-redemption-2.md)

## ACT-274

- Назва: Обирати одну контекстну соціальну відповідь
- Переглянуто: `2026-08-27`

### Операційне визначення

Зосередившись на живій близькій людині, гравець обирає доступну відповідь: привітатися, вороже звернутися, заспокоїти, погрожувати або здатися.

### Включає

Цивільних, свідків і правоохоронців у межах сюжетного режиму.

### Виключає

Фіксовану сюжетну гілку; атаку; пасивний діалог.

### Ігри-носії

- [`GAME-0165` — Red Dead Redemption 2](../games/m-r/red-dead-redemption-2.md)

## ACT-275

- Назва: Обирати поточний виробничий проєкт міста
- Переглянуто: `2026-08-27`

### Операційне визначення

Спрямовувати виробництво одного міста на обрану одиницю, споруду, район, диво або міський чи космічний проєкт, доки ціль не завершено або не змінено.

### Включає

Вибір поселенця, кампусу, космодрому чи марсіанського модуля у виробничому меню.

### Виключає

Купівлю за золото; розміщення району на мапі; автоматичне паралельне виробництво кількох цілей.

### Ігри-носії

- [`GAME-0166` — Sid Meier’s Civilization VI](../games/s-z/sid-meiers-civilization-vi.md)

## ACT-276

- Назва: Обирати активний громадянський інститут
- Переглянуто: `2026-08-27`

### Операційне визначення

Обирати доступний вузол дерева громадянських інститутів, у який надалі надходитиме культура, зі збереженням уже набутого поступу після перемикання.

### Включає

Вибір «Зводу законів», «Політичної філософії» або «Космічної гонки» за виконаних передумов.

### Виключає

Дослідження технології; встановлення політики; культурну перемогу як ціль.

### Ігри-носії

- [`GAME-0166` — Sid Meier’s Civilization VI](../games/s-z/sid-meiers-civilization-vi.md)

## ACT-277

- Назва: Призначати громадянина на ділянку або місце фахівця
- Переглянуто: `2026-08-27`

### Операційне визначення

Перерозподіляти одного громадянина міста між допустимою оброблюваною ділянкою, місцем фахівця та станом без роботи, змінюючи наступні міські надходження.

### Включає

Перенесення громадянина з ферми до шахти або в кампус.

### Виключає

Створення населення; вибір виробничого проєкту; автоматичний розподіл без рішення гравця.

### Ігри-носії

- [`GAME-0166` — Sid Meier’s Civilization VI](../games/s-z/sid-meiers-civilization-vi.md)

## ACT-278

- Назва: Обирати уряд і заповнювати слоти політик
- Переглянуто: `2026-08-27`

### Операційне визначення

Обирати відкритий тип уряду та вставляти доступні військові, економічні, дипломатичні або універсальні політики лише у сумісні слоти.

### Включає

Перехід до класичної республіки та добір карток до її набору слотів.

### Виключає

Саме відкриття уряду в дереві; постійний ефект політики після встановлення; дипломатичну угоду.

### Ігри-носії

- [`GAME-0166` — Sid Meier’s Civilization VI](../games/s-z/sid-meiers-civilization-vi.md)

## ACT-279

- Назва: Спрямовувати торговця до допустимого міста
- Переглянуто: `2026-08-27`

### Операційне визначення

Обирати для вільного торговця досяжне місто призначення з показаними надходженнями, після чого запускати маршрут на визначений строк.

### Включає

Внутрішній маршрут між двома римськими містами або міжнародний маршрут до знайомого суперника.

### Виключає

Разову дипломатичну торгівлю; ручне прокладання дороги; переміщення військової одиниці.

### Ігри-носії

- [`GAME-0166` — Sid Meier’s Civilization VI](../games/s-z/sid-meiers-civilization-vi.md)

## ACT-280

- Назва: Укладати угоду, оголошувати війну або домовлятися про мир
- Переглянуто: `2026-08-27`

### Операційне визначення

Обирати доступну дипломатичну дію щодо знайомої цивілізації, формувати або приймати умови угоди та підтверджувати війну чи мир за чинних обмежень.

### Включає

Обмін золотом і ресурсами, оголошення війни та мирна угода з одним із трьох суперників.

### Виключає

Автоматичну зміну ставлення; бій одиниць; взаємодію з вимкненими містами-державами.

### Ігри-носії

- [`GAME-0166` — Sid Meier’s Civilization VI](../games/s-z/sid-meiers-civilization-vi.md)

## ACT-281

- Назва: Завершувати багатокомандний стратегічний хід держави
- Переглянуто: `2026-09-21`

### Операційне визначення

Явно завершувати відкритий стратегічний хід держави після будь-якої допустимої підмножини наказів одиницям, героям, поселенням, економіці чи дипломатії, щоб розпочався підсумок і хід наступної держави.

### Включає

Завершення ходу в Civilization VI та Homecoming Heroes III.

### Виключає

Завершення окремої дії; автоматичний такт реального часу; пропуск незакритого обов’язкового вибору.

### Ігри-носії

- [`GAME-0332` — "Heroes of Might and Magic III: Complete"](../games/g-l/heroes-of-might-and-magic-iii-complete.md)
- [`GAME-0166` — Sid Meier’s Civilization VI](../games/s-z/sid-meiers-civilization-vi.md)
- [`GAME-0191` — "Total War: WARHAMMER III"](../games/s-z/total-war-warhammer-iii.md)

## ACT-282

- Назва: Керувати висотою однією командою, значення якої залежить від форми
- Переглянуто: `2026-08-27`

### Операційне визначення

Поки іконка автоматично рухається вперед, натискати, утримувати або відпускати єдину команду, яка запитує стрибок куба чи зміну висоти польоту корабля залежно від поточної форми.

### Включає

Натискання й утримання для стрибків куба та утримання й відпускання для польоту корабля у `Stereo Madness`.

### Виключає

Вільне керування у двох осях, вибір місця призначення, безпосередній вибір форми чи горизонтальної швидкості.

### Ігри-носії

- [`GAME-0167` — Geometry Dash](../games/g-l/geometry-dash.md)

## ACT-283

- Назва: Установити або зняти сумісний Мод зі спорядження
- Переглянуто: `2026-08-27`

### Операційне визначення

Під час налаштування спорядження помістити один наявний сумісний Мод у допустимий слот або зняти його перед поверненням до місії в реальному часі.

### Включає

Налаштування вибраного Warframe або стартової зброї в Арсеналі під час `Vor's Prize`.

### Виключає

Підбирання Мода в місії, підвищення рангу спорядження або застосування здібності.

### Ігри-носії

- [`GAME-0168` — Warframe](../games/s-z/warframe.md)

## ACT-284

- Назва: Повернути вузли термінала й утворити зв’язний шифр
- Переглянуто: `2026-08-27`

### Операційне визначення

Поки працює таймер зламу, повертати показані вузли, доки їхні лінії не утворять прийнятий зв’язний рисунок.

### Включає

Злам терміналів Grineer у вступному маршруті Warframe.

### Виключає

Введення пароля, витрачання готового `Cipher` для обходу або бій біля консолі.

### Ігри-носії

- [`GAME-0168` — Warframe](../games/s-z/warframe.md)

## ACT-285

- Назва: Прийняти одне вантажне замовлення з транспортом роботодавця
- Переглянуто: `2026-08-27`

### Операційне визначення

На поточному ринку прийняти одну пропозицію, яка фіксує вантаж, початковий і кінцевий пункти, строк доставки й оплату та надає завантажений транспорт на час рейсу.

### Включає

Прийняття одного замовлення `Quick Job` у Euro Truck Simulator 2.

### Виключає

Замовлення через `Freight Market` для власної вантажівки, придбання вантажівки, доручення автономному працівникові або лише перегляд пропозиції.

### Ігри-носії

- [`GAME-0289` — American Truck Simulator](../games/a-f/american-truck-simulator.md)
- [`GAME-0169` — Euro Truck Simulator 2](../games/a-f/euro-truck-simulator-2.md)

## ACT-286

- Назва: Вибрати тривалість відпочинку на дозволеній стоянці
- Переглянуто: `2026-08-27`

### Операційне визначення

Зупинившись у дозволеному місці, вибрати тривалість сну й просунути годинник світу та рейсу на цей проміжок, відновлюючи стан водія.

### Включає

Вибір часу пробудження за правилами Euro Truck Simulator 2 1.60.

### Виключає

Паузу, заздалегідь визначену системою тривалість сну або відпочинок у контрольній точці зі скиданням бою.

### Ігри-носії

- [`GAME-0289` — American Truck Simulator](../games/a-f/american-truck-simulator.md)
- [`GAME-0169` — Euro Truck Simulator 2](../games/a-f/euro-truck-simulator-2.md)

## ACT-287

- Назва: Вибрати спосіб здачі причепа
- Переглянуто: `2026-08-27`

### Операційне визначення

У пункті призначення вибрати запропонований спосіб здачі, за якого розташування зони або можливість пропустити паркування визначають потрібний маневр і доступний досвід.

### Включає

Звичайне, спрощене або автоматичне паркування з пропуском ручного маневру в Euro Truck Simulator 2.

### Виключає

Саме керування, прийняття замовлення або довільне паркування без наслідків для доставки.

### Ігри-носії

- [`GAME-0289` — American Truck Simulator](../games/a-f/american-truck-simulator.md)
- [`GAME-0169` — Euro Truck Simulator 2](../games/a-f/euro-truck-simulator-2.md)

## ACT-288

- Назва: Кинути болт, щоб перевірити шлях крізь аномалію
- Переглянуто: `2026-08-27`

### Операційне визначення

Кинути болт у вибраному напрямку, щоб аномалія спрацювала й показала, чи з’явилося коротке вікно для проходу.

### Включає

Перевірку аномалій Малої Зони після прологу.

### Виключає

Шкоду від гранат, постійне вимкнення небезпеки або пошук артефакту детектором.

### Ігри-носії

- [`GAME-0170` — "S.T.A.L.K.E.R. 2: Heart of Chornobyl"](../games/s-z/stalker-2-heart-of-chornobyl.md)

## ACT-289

- Назва: Знайти й забрати артефакт за допомогою детектора
- Переглянуто: `2026-08-27`

### Операційне визначення

Увімкнути детектор, іти за зміною його сигналу в аномальному полі та забрати артефакт після його проявлення на критичній відстані.

### Включає

Артефакт у пролозі та Mold у Piece of Cake.

### Виключає

Звичайну видиму здобич, зовнішню мапу або спорядження вже знайденого артефакту.

### Ігри-носії

- [`GAME-0170` — "S.T.A.L.K.E.R. 2: Heart of Chornobyl"](../games/s-z/stalker-2-heart-of-chornobyl.md)

## ACT-290

- Назва: Безпосередньо керувати призначеним автомобілем
- Переглянуто: `2026-09-04`

### Операційне визначення

Поки гравцеві призначено один автомобіль, він безпосередньо керує напрямком, газом, гальмуванням, вибором передачі та передбаченим ручним гальмом без попередньої посадки на місце водія або подальшого виходу з нього.

### Включає

Керування кожним призначеним дорожнім, ґрунтовим, позашляховим автомобілем і авто для Time Attack у визначеному вступі Forza Horizon 6; кермування, прискорення, задній хід, гальмування й керовані заноси одного призначеного авто Rocket League; керування фіксованим початковим авто Story у Shopping Spree в Need for Speed Unbound; керування фіксованим Mustang із подальшою заданою передачею Regera у The Highway Heist в Need for Speed Payback; кермування, прискорення й гальмування призначеного CarSport на Summer 2026 - 01 у Trackmania; кермування, прискорення, гальмування й ручне гальмо фіксованого початкового авто без змін у вступному Circuit Need for Speed Underground.

### Виключає

Посадку й вихід із постійного транспорту світу; призначення автономного транспортного маршруту; вибір власного авто, яке стане активним.

### Ігри-носії

- [`GAME-0195` — BeamNG.drive](../games/a-f/beamng-drive.md)
- [`GAME-0374` — Burnout Paradise](../games/a-f/burnout-paradise.md)
- [`GAME-0384` — F-Zero GX](../games/a-f/f-zero-gx.md)
- [`GAME-0276` — Forza Horizon 5](../games/a-f/forza-horizon-5.md)
- [`GAME-0171` — Forza Horizon 6](../games/a-f/forza-horizon-6.md)
- [`GAME-0316` — Gran Turismo](../games/g-l/gran-turismo.md)
- [`GAME-0309` — "Mario Kart 8 Deluxe"](../games/m-r/mario-kart-8-deluxe.md)
- [`GAME-0244` — "Need for Speed Heat"](../games/m-r/need-for-speed-heat.md)
- [`GAME-0226` — "Need for Speed: Most Wanted (2005)"](../games/m-r/need-for-speed-most-wanted-2005.md)
- [`GAME-0208` — 'Need for Speed Payback'](../games/m-r/need-for-speed-payback.md)
- [`GAME-0235` — "Need for Speed: The Run"](../games/m-r/need-for-speed-the-run.md)
- [`GAME-0199` — "Need for Speed Unbound"](../games/m-r/need-for-speed-unbound.md)
- [`GAME-0217` — "Need for Speed Underground"](../games/m-r/need-for-speed-underground.md)
- [`GAME-0177` — Rocket League](../games/m-r/rocket-league.md)
- [`GAME-0216` — Trackmania](../games/s-z/trackmania.md)
- [`GAME-0184` — War Thunder](../games/s-z/war-thunder.md)
- [`GAME-0211` — World of Tanks](../games/s-z/world-of-tanks.md)

## ACT-291

- Назва: Обрати поточний автомобіль із придатної колекції
- Переглянуто: `2026-08-27`

### Операційне визначення

Поза заблокованою подією обрати один власний придатний автомобіль, який стане поточним і безпосередньо керованим.

### Включає

Вибір стартового автомобіля й перемикання між власними машинами перед подіями Forza Horizon 6.

### Виключає

Купівлю, вантажний контракт або зміну автомобіля після фіксації події.

### Ігри-носії

- [`GAME-0171` — Forza Horizon 6](../games/a-f/forza-horizon-6.md)
- [`GAME-0235` — "Need for Speed: The Run"](../games/m-r/need-for-speed-the-run.md)

## ACT-292

- Назва: Налаштувати допомогу з водінням і складність суперників
- Переглянуто: `2026-09-04`

### Операційне визначення

Гравець фіксує сумісний профіль допомоги з водінням і складності суперників, який змінює опрацювання прямого керування, підказок та автономних суперників у допустимих транспортних подіях.

### Включає

Налаштування кермування, гальмування, коробки передач, тяги, стійкості, траєкторії, Rewind і складності Drivatar у Forza Horizon 6; профіль суперників і поліції Relaxed у Story та автоматичну коробку передач Need for Speed Unbound; суперників Easy й автоматичну коробку передач Need for Speed Payback; суперників Easy для окремої події й автоматичну коробку передач Need for Speed Underground.

### Виключає

Зміну лише якості зображення; налаштування механічних деталей авто; вибір іншої події або власного автомобіля.

### Ігри-носії

- [`GAME-0384` — F-Zero GX](../games/a-f/f-zero-gx.md)
- [`GAME-0171` — Forza Horizon 6](../games/a-f/forza-horizon-6.md)
- [`GAME-0309` — "Mario Kart 8 Deluxe"](../games/m-r/mario-kart-8-deluxe.md)
- [`GAME-0244` — "Need for Speed Heat"](../games/m-r/need-for-speed-heat.md)
- [`GAME-0226` — "Need for Speed: Most Wanted (2005)"](../games/m-r/need-for-speed-most-wanted-2005.md)
- [`GAME-0208` — 'Need for Speed Payback'](../games/m-r/need-for-speed-payback.md)
- [`GAME-0235` — "Need for Speed: The Run"](../games/m-r/need-for-speed-the-run.md)
- [`GAME-0199` — "Need for Speed Unbound"](../games/m-r/need-for-speed-unbound.md)
- [`GAME-0217` — "Need for Speed Underground"](../games/m-r/need-for-speed-underground.md)

## ACT-293

- Назва: Почати одну доступну транспортну подію на мапі
- Переглянуто: `2026-09-04`

### Операційне визначення

Гравець обирає позначку поточної відкритої транспортної події та приймає її заданий автором маршрут, вимоги до авто й правила результату.

### Включає

Вхід у визначені Trail, Circuit, Cross Country, Time Attack і Horizon Invitational у Forza Horizon 6; підтвердження доступної позначки Shopping Spree у Story Need for Speed Unbound; підтвердження доступної сюжетної позначки The Highway Heist у Need for Speed Payback; підтвердження першої доступної події Jose's Got Your Back у Need for Speed Underground.

### Виключає

Розміщення навігаційної точки без початку події; створення власного маршруту; вибір добірки багатокористувацьких подій.

### Ігри-носії

- [`GAME-0242` — "Asphalt Legends"](../games/a-f/asphalt-legends.md)
- [`GAME-0374` — Burnout Paradise](../games/a-f/burnout-paradise.md)
- [`GAME-0384` — F-Zero GX](../games/a-f/f-zero-gx.md)
- [`GAME-0171` — Forza Horizon 6](../games/a-f/forza-horizon-6.md)
- [`GAME-0309` — "Mario Kart 8 Deluxe"](../games/m-r/mario-kart-8-deluxe.md)
- [`GAME-0244` — "Need for Speed Heat"](../games/m-r/need-for-speed-heat.md)
- [`GAME-0208` — 'Need for Speed Payback'](../games/m-r/need-for-speed-payback.md)
- [`GAME-0199` — "Need for Speed Unbound"](../games/m-r/need-for-speed-unbound.md)
- [`GAME-0217` — "Need for Speed Underground"](../games/m-r/need-for-speed-underground.md)

## ACT-294

- Назва: Призначити бійця, сторону й тип керування для дуелі
- Переглянуто: `2026-08-31`

### Операційне визначення

Перед початком фіксованого матчу призначити кожному учаснику доступного бійця, сторону та підтримувану схему введення.

### Включає

Ryu на стороні P1, Luke під керуванням CPU і Classic controls для обох.

### Виключає

Зміну бійця всередині раунду, командний склад або постійного аватара кампанії.

### Ігри-носії

- [`GAME-0198` — Brawlhalla](../games/a-f/brawlhalla.md)
- [`GAME-0393` — Mortal Kombat II](../games/m-r/mortal-kombat-ii.md)
- [`GAME-0172` — Street Fighter 6](../games/s-z/street-fighter-6.md)
- [`GAME-0351` — "Street Fighter II: The World Warrior"](../games/s-z/street-fighter-ii-the-world-warrior.md)
- [`GAME-0366` — Tekken 3](../games/s-z/tekken-3.md)
- [`GAME-0283` — TEKKEN 8](../games/s-z/tekken-8.md)

## ACT-295

- Назва: Ввести атаку безпосередньо керованого персонажа
- Переглянуто: `2026-09-21`

### Операційне визначення

Коли безпосередньо керований персонаж може діяти, гравець вводить один допустимий власний стан атаки через оголошену послідовність напрямку, пози й кнопки: звичайний удар, бойову команду, снаряд, стрибок-клубок, перекат або колесо.

### Включає

Звичайні атаки Ryu, Hadoken і Super Art; стрибок-клубок і рухомий перекат Соніка.

### Виключає

Рух без атаки; автоматичне розв’язання контакту; споряджену вогнепальну зброю чи інструмент; тактичну покрокову команду.

### Ігри-носії

- [`GAME-0318` — Battletoads](../games/a-f/battletoads.md)
- [`GAME-0198` — Brawlhalla](../games/a-f/brawlhalla.md)
- [`GAME-0326` — Crash Bandicoot](../games/a-f/crash-bandicoot.md)
- [`GAME-0329` — "Donkey Kong Country"](../games/a-f/donkey-kong-country.md)
- [`GAME-0393` — Mortal Kombat II](../games/m-r/mortal-kombat-ii.md)
- [`GAME-0333` — "Sonic the Hedgehog"](../games/s-z/sonic-the-hedgehog.md)
- [`GAME-0172` — Street Fighter 6](../games/s-z/street-fighter-6.md)
- [`GAME-0351` — "Street Fighter II: The World Warrior"](../games/s-z/street-fighter-ii-the-world-warrior.md)
- [`GAME-0354` — Super Mario World](../games/s-z/super-mario-world.md)
- [`GAME-0366` — Tekken 3](../games/s-z/tekken-3.md)
- [`GAME-0283` — TEKKEN 8](../games/s-z/tekken-8.md)

## ACT-296

- Назва: Утримувати або відпускати блок проти суперника
- Переглянуто: `2026-09-24`

### Операційне визначення

Утримувати введення блоку проти поточного суперника, щоб захищатися стоячи чи навприсядки, або відпустити це введення під час бою. Залежно від гри блок задається напрямком від суперника або окремою кнопкою.

### Включає

Звичайний високий і низький блок у Street Fighter 6; блок кнопками L/R в оригінальній Mortal Kombat II для SNES.

### Виключає

Drive Parry, броню атаки, покроковий захист або прив’язування до укриття.

### Ігри-носії

- [`GAME-0393` — Mortal Kombat II](../games/m-r/mortal-kombat-ii.md)
- [`GAME-0172` — Street Fighter 6](../games/s-z/street-fighter-6.md)
- [`GAME-0351` — "Street Fighter II: The World Warrior"](../games/s-z/street-fighter-ii-the-world-warrior.md)
- [`GAME-0366` — Tekken 3](../games/s-z/tekken-3.md)
- [`GAME-0283` — TEKKEN 8](../games/s-z/tekken-8.md)

## ACT-297

- Назва: Спробувати близький кидок або відповідний Throw Escape
- Переглянуто: `2026-08-31`

### Операційне визначення

На близькій дистанції ввести кидок, щоб захопити придатного суперника, або в належне вікно вирватися зі звичайного кидка суперника.

### Включає

Звичайний throw і Throw Escape у Versus.

### Виключає

Командний grab як параметр бійця, перенесення непритомного тіла або автоматичне відштовхування.

### Ігри-носії

- [`GAME-0393` — Mortal Kombat II](../games/m-r/mortal-kombat-ii.md)
- [`GAME-0172` — Street Fighter 6](../games/s-z/street-fighter-6.md)
- [`GAME-0351` — "Street Fighter II: The World Warrior"](../games/s-z/street-fighter-ii-the-world-warrior.md)
- [`GAME-0366` — Tekken 3](../games/s-z/tekken-3.md)
- [`GAME-0283` — TEKKEN 8](../games/s-z/tekken-8.md)

## ACT-298

- Назва: Застосувати одну допустиму техніку Drive
- Переглянуто: `2026-08-31`

### Операційне визначення

Із придатного бойового стану запросити одну зі спільних технік Drive System і прийняти її поточну вартість та перехід.

### Включає

Drive Impact, Drive Parry, Drive Rush, Drive Reversal і Overdrive attacks.

### Виключає

Звичайний блок, витрату Super Art або пасивне відновлення Drive.

### Ігри-носії

- [`GAME-0172` — Street Fighter 6](../games/s-z/street-fighter-6.md)

## ACT-299

- Назва: Вибрати один запропонований план кімнати за вказаними дверима
- Переглянуто: `2026-08-28`

### Операційне визначення

Біля одних невідчинених дверей вибрати рівно один показаний план з обмеженої пропозиції та зафіксувати його як майбутню кімнату.

### Включає

Вибір одного з трьох планів кімнат у Blue Prince.

### Виключає

Перестановку вже наявної плитки, придбання товару або довільне будівництво.

### Ігри-носії

- [`GAME-0173` — Blue Prince](../games/a-f/blue-prince.md)

## ACT-300

- Назва: Завершити день у маєтку й запросити нове креслення
- Переглянуто: `2026-08-28`

### Операційне визначення

Явно закінчити поточну спробу в маєтку, прийняти втрату щоденного стану й почати наступний ранок з новим планом.

### Включає

Call it a Day у Blue Prince.

### Виключає

Автоматичний таймер, смерть, завантаження збереження або вихід з однієї кімнати.

### Ігри-носії

- [`GAME-0173` — Blue Prince](../games/a-f/blue-prince.md)

## ACT-301

- Назва: Заборонити одного оператора протилежної ролі
- Переглянуто: `2026-08-28`

### Операційне визначення

Під час запланованої фази командою додати допустимого оператора протилежної ролі до спільного списку недоступних.

### Включає

Бани нападників і захисників у Rainbow Six Siege Pro League.

### Виключає

Вибір власного оператора, косметику або турнірне вето мап.

### Ігри-носії

- [`GAME-0174` — Tom Clancy’s Rainbow Six Siege](../games/s-z/tom-clancys-rainbow-six-siege.md)

## ACT-302

- Назва: Керувати активним пристроєм спостереження або його каналом
- Переглянуто: `2026-08-28`

### Операційне визначення

Увійти до каналу справного віддаленого пристрою та, якщо можливо, рухати чи повертати його, сканувати або ставити позначку.

### Включає

Дрони нападників і камери захисників у Rainbow Six Siege.

### Виключає

Зір персонажа, статичну мапу або післяматчевий повтор.

### Ігри-носії

- [`GAME-0174` — Tom Clancy’s Rainbow Six Siege](../games/s-z/tom-clancys-rainbow-six-siege.md)

## ACT-303

- Назва: Проламати допустиму поверхню
- Переглянуто: `2026-08-28`

### Операційне визначення

Застосувати сумісний удар, вибухівку або hard-breach засіб до стіни, підлоги, стелі, дверей чи вікна, щоб створити прохід або лінію огляду.

### Включає

М’який і hard breach у Rainbow Six Siege.

### Виключає

Декоративне сміття, звичайне проникнення кулі або видобування блоків.

### Ігри-носії

- [`GAME-0174` — Tom Clancy’s Rainbow Six Siege](../games/s-z/tom-clancys-rainbow-six-siege.md)

## ACT-304

- Назва: Налаштувати склад автономної футбольної команди й двофазний тактичний план
- Переглянуто: `2026-08-31`

### Операційне визначення

Призначити допустимих футболістів на місця складу й задати окремі формації, ролі та вказівки у володінні й без м’яча.

### Включає

Вибір команди та подвійна тактика у Football Manager 26.

### Виключає

Пряме пересування футболіста, трансфер або декоративна схема.

### Ігри-носії

- [`GAME-0175` — Football Manager 26](../games/a-f/football-manager-26.md)

## ACT-305

- Назва: Підтвердити живу менеджерську заміну або тактичну зміну
- Переглянуто: `2026-08-31`

### Операційне визначення

Під час автономного матчу підтвердити допустиму зміну футболіста, ролі, формації чи командної вказівки.

### Включає

Заміни й тактичні зміни Football Manager 26.

### Виключає

Пряме керування тілом або непідтверджений перегляд плану.

### Ігри-носії

- [`GAME-0175` — Football Manager 26](../games/a-f/football-manager-26.md)

## ACT-306

- Назва: Підготувати реактивний вогонь бійця на рух ворога
- Переглянуто: `2026-08-31`

### Операційне визначення

Витратити залишок дій бійця, щоб підготувати один постріл, який може спрацювати на допустимий рух видимого ворога у ворожій фазі.

### Включає

Overwatch у місії Operation Gatecrasher XCOM 2.

### Виключає

Негайний постріл, постійну автоматичну зону або непідготовлену реакцію.

### Ігри-носії

- [`GAME-0176` — XCOM 2](../games/s-z/xcom-2.md)

## ACT-307

- Назва: Виконати сусідню тактичну взаємодію місії
- Переглянуто: `2026-08-31`

### Операційне визначення

Наказати бійцеві біля допустимого об’єкта виконати оголошену взаємодію, витративши потрібну дію й змінивши стан цілі.

### Включає

Встановлення X4 на монументі ADVENT у XCOM 2.

### Виключає

Звичайний рух, косметичний об’єкт або автоматичне завершення через вхід у зону.

### Ігри-носії

- [`GAME-0176` — XCOM 2](../games/s-z/xcom-2.md)

## ACT-308

- Назва: Виконати стрибок, dodge або повітряну орієнтацію авто
- Переглянуто: `2026-08-31`

### Операційне визначення

Під час прямого керування авто виконати допустимий jump, directional dodge або безперервну зміну орієнтації, що виходить за межі наземного steering.

### Включає

Jump, double jump, directional flip, air roll і aerial control у Rocket League.

### Виключає

Звичайне наземне steering, boost без jump-дії або автоматичний stunt.

### Ігри-носії

- [`GAME-0177` — Rocket League](../games/m-r/rocket-league.md)

## ACT-309

- Назва: Витрачати скінченний запас машини на спрямоване прискорення
- Переглянуто: `2026-09-06`

### Операційне визначення

Під час прямого керування машиною гравець вмикає, утримує або відпускає її скінченний запас прискорення, витрачаючи весь поточний обсяг або його частину, щоб додати спрямовану тягу вздовж поточної орієнтації машини в наземному чи повітряному русі; сама команда не володіє правилом, за яким той запас поповнюють, обмежують або відновлюють.

### Включає

Наземне прискорення, повітряний набір висоти й повернення через накопичений запас у Rocket League; звичайне нітро Need for Speed Payback у дослідженій погоні за перевізником; увімкнення Burst Nitrous у дослідженому заїзді або обов’язковій погоні Need for Speed Unbound.

### Виключає

Пасивну тягу двигуна; постійний необмежений приріст швидкості; витрату носимого лікувального підсилювача; особливу бойову чи водійську форму героя; системну поведінку, що поповнює, обмежує або відновлює цей запас.

### Ігри-носії

- [`GAME-0242` — "Asphalt Legends"](../games/a-f/asphalt-legends.md)
- [`GAME-0374` — Burnout Paradise](../games/a-f/burnout-paradise.md)
- [`GAME-0384` — F-Zero GX](../games/a-f/f-zero-gx.md)
- [`GAME-0226` — "Need for Speed: Most Wanted (2005)"](../games/m-r/need-for-speed-most-wanted-2005.md)
- [`GAME-0208` — 'Need for Speed Payback'](../games/m-r/need-for-speed-payback.md)
- [`GAME-0235` — "Need for Speed: The Run"](../games/m-r/need-for-speed-the-run.md)
- [`GAME-0199` — "Need for Speed Unbound"](../games/m-r/need-for-speed-unbound.md)
- [`GAME-0177` — Rocket League](../games/m-r/rocket-league.md)

## ACT-310

- Назва: Обрати точку відродження після demolition на своєму боці
- Переглянуто: `2026-08-31`

### Операційне визначення

У короткому вікні після demolition обрати одну з доступних позицій відносно власних воріт до повернення авто в живу гру.

### Включає

Вибір точки відродження після demolition у мережевому матчі Rocket League v2.72.

### Виключає

Стартову kickoff-позицію, стале місце відродження або повернення лише в наступному раунді.

### Ігри-носії

- [`GAME-0177` — Rocket League](../games/m-r/rocket-league.md)

## ACT-311

- Назва: Випити запас води
- Переглянуто: `2026-08-28`

### Операційне визначення

Гравець споживає один придатний напій із наплічника, щоб збільшити поточний запас води персонажа.

### Включає

Вживання фільтрованої води чи іншого напою в режимі виживання Subnautica.

### Виключає

Їжу для відновлення ситості; автоматичне пиття з довкілля; виготовлення напою.

### Ігри-носії

- [`GAME-0210` — DayZ](../games/a-f/dayz.md)
- [`GAME-0178` — Subnautica](../games/s-z/subnautica.md)
- [`GAME-0285` — "The Long Dark"](../games/s-z/the-long-dark.md)

## ACT-312

- Назва: Спіймати рухливу малу істоту
- Переглянуто: `2026-08-28`

### Операційне визначення

Гравець простягає руку до доступної малої істоти, що вільно рухається, і забирає її до наплічника, доки вона не вийшла за межі досяжності.

### Включає

Ловлю рукою доступного піпера чи риби-міхура в Subnautica.

### Виключає

Збір нерухомої сировини; вбивство істоти зброєю; автоматичний вилов пасткою.

### Ігри-носії

- [`GAME-0178` — Subnautica](../games/s-z/subnautica.md)

## ACT-313

- Назва: Утримувати аналізатор на одній досяжній цілі світу
- Переглянуто: `2026-09-22`

### Операційне визначення

Гравець споряджає живлений сканер або аналізатор, утримує одну придатну ціль світу зафіксованою в межах дії та тримає команду сканування, щоб просувати збережуваний поступ аналізу саме цієї цілі.

### Включає

Сканування уламків технологій та організмів ручним сканером у Subnautica; сканування однієї досяжної цілі на Frigate Orpheon через Scan Visor у Metroid Prime.

### Виключає

Вибір готового креслення у виробничому меню; автоматичний пошук ресурсів кімнатою сканування; миттєвий підбір або одноімпульсне обстеження цілі; типізований результат після завершення сканування.

### Ігри-носії

- [`GAME-0243` — Battlefield Hardline](../games/a-f/battlefield-hardline.md)
- [`GAME-0355` — Metroid Prime](../games/m-r/metroid-prime.md)
- [`GAME-0178` — Subnautica](../games/s-z/subnautica.md)

## ACT-314

- Назва: Збудувати або розібрати модуль бази
- Переглянуто: `2026-08-28`

### Операційне визначення

Гравець спрямовує заряджений будівельний інструмент на допустиме місце чи наявний підводний модуль і утримує будівництво або розбирання до завершення поступу, забезпеченого матеріалами.

### Включає

Будівництво або демонтаж I-відсіку, люка чи сонячної панелі Habitat Builder-ом у Subnautica.

### Виключає

Миттєве встановлення переносного блока; лагодження пробоїни; розгортання плавучої виробничої платформи.

### Ігри-носії

- [`GAME-0178` — Subnautica](../games/s-z/subnautica.md)

## ACT-315

- Назва: Розгорнути або скласти мобільну виробничу платформу
- Переглянуто: `2026-09-07`

### Операційне визначення

Гравець перетворює придатну переносну або рухому виробничу платформу на закріплений чи робочий об’єкт у світі, а там, де правила це дозволяють, повертає незайняту платформу до переносного стану.

### Включає

Розгортання, посадку на платформу й подальше складання Mobile Vehicle Bay у Subnautica; розгортання мобільної будівельної машини у стаціонарний будівельний майданчик у Command & Conquer Remastered Collection.

### Виключає

Будівництво з’єднаного модуля бази; посадку у виготовлений транспорт; вибір рецепта транспорту.

### Ігри-носії

- [`GAME-0275` — Command & Conquer Remastered Collection](../games/a-f/command-and-conquer-remastered-collection.md)
- [`GAME-0178` — Subnautica](../games/s-z/subnautica.md)

## ACT-316

- Назва: Додати одне замовлення до черги придатного виробничого місця
- Переглянуто: `2026-09-07`

### Операційне визначення

Гравець вибирає власне виробниче місце або спільну панель цього місця й додає один доступний загін чи споруду до скінченної живої черги або виробничого каналу.

### Включає

Селян і військові загони у придатних спорудах Age of Empires II: Definitive Edition; споруди й піхоту у відповідних виробничих місцях Command & Conquer Remastered Collection.

### Виключає

Єдину ціль виробництва міста на хід; безкоштовний сценарний юніт; дослідження технології замість юніта.

### Ігри-носії

- [`GAME-0179` — Age of Empires II: Definitive Edition](../games/a-f/age-of-empires-ii-definitive-edition.md)
- [`GAME-0275` — Command & Conquer Remastered Collection](../games/a-f/command-and-conquer-remastered-collection.md)
- [`GAME-0209` — Cossacks 3](../games/a-f/cossacks-3.md)
- [`GAME-0287` — Stellaris](../games/s-z/stellaris.md)

## ACT-317

- Назва: Задати формацію та стійку вибраній групі
- Переглянуто: `2026-08-31`

### Операційне визначення

Гравець призначає вибраній групі доступну просторову формацію й бойову стійку, змінюючи розташування її учасників, захоплення цілей і утримання позиції після наступних наказів.

### Включає

Лінійну, коробчасту, розосереджену чи флангову формацію та агресивну, захисну, утримання позиції або заборону атаки (aggressive, defensive, stand ground, no attack) в Age of Empires II: Definitive Edition.

### Виключає

Косметичний стрій; футбольні ролі; окрему траєкторію кожного учасника.

### Ігри-носії

- [`GAME-0179` — Age of Empires II: Definitive Edition](../games/a-f/age-of-empires-ii-definitive-edition.md)
- [`GAME-0209` — Cossacks 3](../games/a-f/cossacks-3.md)
- [`GAME-0194` — "Mount & Blade II: Bannerlord"](../games/m-r/mount-and-blade-ii-bannerlord.md)
- [`GAME-0191` — "Total War: WARHAMMER III"](../games/s-z/total-war-warhammer-iii.md)

## ACT-318

- Назва: Призначити селянина на доступну господарську роботу
- Переглянуто: `2026-08-31`

### Операційне визначення

Гравець наказує одному чи кільком вибраним селянам збирати доступний ресурс, будувати поставлений фундамент або ремонтувати придатний пошкоджений об’єкт.

### Включає

Роботу з харчами, деревиною, золотом, каменем, будівництвом і ремонтом в Age of Empires II: Definitive Edition.

### Виключає

Автоматичні тики праці; глобальний пріоритет працівників; прямий військовий наказ.

### Ігри-носії

- [`GAME-0179` — Age of Empires II: Definitive Edition](../games/a-f/age-of-empires-ii-definitive-edition.md)
- [`GAME-0209` — Cossacks 3](../games/a-f/cossacks-3.md)

## ACT-319

- Назва: Налаштувати й запустити обмежений план Free Flight
- Переглянуто: `2026-08-30`

### Операційне визначення

До отримання керування гравець вибирає один літак, виліт, прибуття, маршрут, умови середовища й допоміжні функції та запускає сформований сценарій Free Flight.

### Включає

Маршрут Cessna 172 G1000 від стоянки KBFI до стоянки KTIW за фіксованих денних Clear Skies у Microsoft Flight Simulator 2024.

### Виключає

Прийняття завдання Career; зміну погоди наживо після запуску; автономний транспортний розклад; вибір лише однієї дорожньої точки.

### Ігри-носії

- [`GAME-0180` — Microsoft Flight Simulator 2024](../games/m-r/microsoft-flight-simulator-2024.md)

## ACT-320

- Назва: Керувати живленням, двигуном і конфігурацією літака
- Переглянуто: `2026-08-30`

### Операційне визначення

Гравець перемикає тумблери й важелі в кабіні, які встановлюють або змінюють подачу пального, електроживлення, роботу двигуна, освітлення й аеродинамічну конфігурацію, не делегуючи системі керування польотом.

### Включає

Паливний кран, акумулятор і генератор, авіоніку, регулятор складу суміші, магнето й стартер, важіль тяги, освітлення, тример і закрилки Cessna 172 у Microsoft Flight Simulator 2024.

### Виключає

Рух штурвала або педалей для зміни просторового положення; автоматичний запуск однією кнопкою; вибір літака до створення польоту.

### Ігри-носії

- [`GAME-0180` — Microsoft Flight Simulator 2024](../games/m-r/microsoft-flight-simulator-2024.md)

## ACT-321

- Назва: Безпосередньо пілотувати літак із фіксованим крилом
- Переглянуто: `2026-08-30`

### Операційне визначення

Гравець безперервно керує тангажем, креном, рисканням, тягою й колісними гальмами, щоб рулити, злітати, летіти, сідати й зупинятися, замість вибору цілі для автономного руху.

### Включає

Ручний політ і наземне керування Cessna 172 G1000 без автопілота в Microsoft Flight Simulator 2024.

### Виключає

Перемикання режимів меха; керування парашутом; автономне пілотування ШІ; керування дорожнім транспортом без причинної моделі підіймальної сили й допустимих режимів польоту.

### Ігри-носії

- [`GAME-0180` — Microsoft Flight Simulator 2024](../games/m-r/microsoft-flight-simulator-2024.md)

## ACT-322

- Назва: Обрати роль до пошуку матчу
- Переглянуто: `2026-08-31`

### Операційне визначення

До пошуку матчу гравець фіксує одну із запропонованих бойових ролей, резервуючи її командне місце й відповідний набір доступних героїв для майбутнього матчу.

### Включає

Вибір танка (Tank), героя шкоди (Damage) або героя підтримки (Support) у звичайній черзі Overwatch 5v5 Role Queue.

### Виключає

Вибір героя після створення лобі; побажання в Open Queue; автономна роль агента; позначка профілю.

### Ігри-носії

- [`GAME-0181` — Overwatch](../games/m-r/overwatch.md)

## ACT-323

- Назва: Проголосувати за мапу або Random Map
- Переглянуто: `2026-08-31`

### Операційне визначення

Під час передматчевого голосування гравець віддає один голос за показану мапу або явний випадковий варіант до визначення арени.

### Включає

Три видимі варіанти мапи й четвертий варіант Random Map у Overwatch Quick Play.

### Виключає

Одноосібний вибір мапи; заборона героя; зовнішнє опитування; приховане побажання для добору матчу.

### Ігри-носії

- [`GAME-0181` — Overwatch](../games/m-r/overwatch.md)

## ACT-324

- Назва: Обрати один доступний національний фокус
- Переглянуто: `2026-08-31`

### Операційне визначення

Гравець обирає одну доступну гілку розвитку країни як активний фокус, щоб календарний поступ привів до її тривалих наслідків.

### Включає

Вибір базового італійського національного фокусу під час навчальної війни.

### Виключає

Вибір технології; зміна закону; автоматична національна подія.

### Ігри-носії

- [`GAME-0182` — Hearts of Iron IV](../games/g-l/hearts-of-iron-iv.md)

## ACT-325

- Назва: Пріоритезувати державне будівництво
- Переглянуто: `2026-08-31`

### Операційне визначення

Гравець додає допустиму споруду або інфраструктуру штату до загальнодержавної черги та визначає її місце в розподілі цивільних фабрик.

### Включає

Додавання й переміщення італійського будівництва в доступному штаті.

### Виключає

Призначення окремого робітника; виробництво спорядження; миттєва купівля споруди.

### Ігри-носії

- [`GAME-0182` — Hearts of Iron IV](../games/g-l/hearts-of-iron-iv.md)

## ACT-326

- Назва: Налаштувати державну лінію спорядження
- Переглянуто: `2026-08-31`

### Операційне визначення

Гравець створює або змінює відкриту виробничу лінію та призначає їй частину військових фабрик країни.

### Включає

Розподіл італійських військових фабрик між піхотним спорядженням, артилерією та літаками підтримки у визначених правилах Hearts of Iron IV.

### Виключає

Державне будівництво; ручне виготовлення предмета; зміна шаблону дивізії.

### Ігри-носії

- [`GAME-0182` — Hearts of Iron IV](../games/g-l/hearts-of-iron-iv.md)

## ACT-327

- Назва: Організувати дивізії під командувачем
- Переглянуто: `2026-08-31`

### Операційне визначення

Гравець призначає вибрані дивізії до однієї армії та обирає командувача, який керує всією формацією.

### Включає

Групування італійських дивізій північного й південного фронтів.

### Виключає

Малювання просторового плану армії; безпосереднє переміщення однієї дивізії; зміна шаблону спорядження дивізії.

### Ігри-носії

- [`GAME-0182` — Hearts of Iron IV](../games/g-l/hearts-of-iron-iv.md)

## ACT-328

- Назва: Намалювати й виконати план фронту
- Переглянуто: `2026-08-31`

### Операційне визначення

Гравець малює допустимі лінії фронту й наступу для армії, а потім запускає, призупиняє або видаляє цей збережений план.

### Включає

Визначення й виконання італійських фронтів з Еритреї або Сомаліленду в напрямку Ефіопії.

### Виключає

Окремий наказ дивізії; вибір командувача; дипломатична мета війни.

### Ігри-носії

- [`GAME-0182` — Hearts of Iron IV](../games/g-l/hearts-of-iron-iv.md)

## ACT-329

- Назва: Призначити авіакрило регіону й завданню
- Переглянуто: `2026-08-31`

### Операційне визначення

Гравець спрямовує доступне авіакрило в допустимий повітряний регіон і вмикає підтримуване завдання.

### Включає

Призначення винищувачів або літаків безпосередньої підтримки до Східної Африки та ввімкнення завдань переваги в повітрі чи підтримки наземних сил.

### Виключає

Ручне пілотування; виробнича лінія літака; наказ флоту.

### Ігри-носії

- [`GAME-0182` — Hearts of Iron IV](../games/g-l/hearts-of-iron-iv.md)

## ACT-330

- Назва: Вибрати машину для наступного наземного виходу
- Переглянуто: `2026-08-31`

### Операційне визначення

На початковому екрані або після втрати техніки гравець вибирає одну доступну машину із зафіксованого складу як наступний безпосередньо керований об’єкт.

### Включає

Вибір M2A4, LVT(A)(1) або M2A2 в обмеженому матчі Ground Arcade без предметів Backup.

### Виключає

Купівлю чи дослідження машини; зміну вже наявної машини поза матчем; вхід до машини, яка вже є у світі; тимчасові літакові вильоти.

### Ігри-носії

- [`GAME-0184` — War Thunder](../games/s-z/war-thunder.md)

## ACT-331

- Назва: Лишити або замінити початкову руку
- Переглянуто: `2026-08-31`

### Операційне визначення

До першого ходу гравець приймає показану руку або бере муліган, а потім кладе потрібну кількість карт униз бібліотеки.

### Включає

London mulligan в одній визначеній партії Starter Deck Duel.

### Виключає

Скидання карт під час партії; конструювання колоди; повторний добір під час бою.

### Ігри-носії

- [`GAME-0185` — "Magic: The Gathering Arena"](../games/m-r/magic-the-gathering-arena.md)

## ACT-332

- Назва: Зіграти одну землю з руки
- Переглянуто: `2026-08-31`

### Операційне визначення

Активний гравець кладе карту землі з руки на поле бою під час допустимої головної фази, не розігруючи її як закляття.

### Включає

Plains, Island, Tranquil Cove або Temple of Enlightenment.

### Виключає

Розігрування постійного закляття; манове уміння; поява землі внаслідок іншого ефекту.

### Ігри-носії

- [`GAME-0185` — "Magic: The Gathering Arena"](../games/m-r/magic-the-gathering-arena.md)

## ACT-333

- Назва: Розіграти закляття з видимої руки
- Переглянуто: `2026-08-31`

### Операційне визначення

Гравець обирає придатну карту, оголошує режими, цілі й значення та сплачує вартість, щоб помістити закляття у стос.

### Включає

Істоту, миттєве закляття, чаклунство, артефакт або чари з Arcane Aerialists.

### Виключає

Розігрування землі; активоване уміння; негайне виконання без вікна пріоритету.

### Ігри-носії

- [`GAME-0185` — "Magic: The Gathering Arena"](../games/m-r/magic-the-gathering-arena.md)

## ACT-334

- Назва: Активувати уміння контрольованої карти
- Переглянуто: `2026-08-31`

### Операційне визначення

Гравець обирає активоване уміння контрольованої карти, задає потрібні варіанти й цілі та сплачує вартість активації.

### Включає

Будь-яке допустиме активоване уміння в партії готовими колодами.

### Виключає

Розігрування самої карти-джерела; спрацьовуване уміння; автоматичне виконання системою.

### Ігри-носії

- [`GAME-0185` — "Magic: The Gathering Arena"](../games/m-r/magic-the-gathering-arena.md)

## ACT-335

- Назва: Передати пріоритет без нового об’єкта
- Переглянуто: `2026-08-31`

### Операційне визначення

Гравець із пріоритетом відмовляється від закляття, уміння чи особливої дії та надає супернику можливість відповісти.

### Включає

Явне або автоматичне передавання пріоритету в Arena.

### Виключає

Одностороннє завершення ходу; здачу; виконання об’єкта до можливості відповісти.

### Ігри-носії

- [`GAME-0185` — "Magic: The Gathering Arena"](../games/m-r/magic-the-gathering-arena.md)

## ACT-336

- Назва: Оголосити допустимий набір нападників
- Переглянуто: `2026-08-31`

### Операційне визначення

На кроці оголошення нападників активний гравець обирає будь-яку допустиму підмножину контрольованих істот і призначає кожну з них нападником проти суперника або іншого дозволеного захисника.

### Включає

Неповернуті істоти Arcane Aerialists, які досить довго перебувають під контролем гравця або мають прискорення.

### Виключає

Бойову шкоду; вибір блокувальників; закляття у вікні бою.

### Ігри-носії

- [`GAME-0185` — "Magic: The Gathering Arena"](../games/m-r/magic-the-gathering-arena.md)

## ACT-337

- Назва: Призначити допустимих блокувальників
- Переглянуто: `2026-08-31`

### Операційне визначення

Захисник зіставляє свої неповернуті істоти з нападниками відповідно до здатностей обходу, обмежень і вимог.

### Включає

Призначення придатних істот Arcane Aerialists блокувальниками, зокрема блокування нападника з польотом летючою істотою.

### Виключає

Вибір нападників; бойову шкоду; пізніше миттєве закляття.

### Ігри-носії

- [`GAME-0185` — "Magic: The Gathering Arena"](../games/m-r/magic-the-gathering-arena.md)

## ACT-338

- Назва: Розмістити створену споруду для виживання
- Переглянуто: `2026-08-31`

### Операційне визначення

Гравець обирає вільне сумісне місце й установлює там уже створену переносну споруду як постійний об’єкт світу.

### Включає

Вогнище, постійне вогнище, наукова машина, алхімічний двигун, казан або скриня.

### Виключає

Створення предмета; додавання палива; багатокомпонентний план; звичайне викидання речі.

### Ігри-носії

- [`GAME-0186` — "Don’t Starve Together"](../games/a-f/dont-starve-together.md)
- [`GAME-0229` — "No Man’s Sky"](../games/m-r/no-mans-sky.md)

## ACT-339

- Назва: Передати привиду напарника предмет відродження
- Переглянуто: `2026-08-31`

### Операційне визначення

Живий гравець застосовує перенесене серце до привида загиблого напарника й повертає його до тілесної гри.

### Включає

Передавання Telltale Heart привиду другого вцілілого.

### Виключає

Самовідродження; автоматична поява; лікування живого напарника.

### Ігри-носії

- [`GAME-0186` — "Don’t Starve Together"](../games/a-f/dont-starve-together.md)

## ACT-340

- Назва: Вибрати або змінити клас у командній зоні появи
- Переглянуто: `2026-08-31`

### Операційне визначення

У дозволеній командній зоні появи гравець вибирає доступний клас і надає поточному або наступному керованому тілу його базове стандартне спорядження.

### Включає

Вибір і зміна одного з дев’яти звичайних класів Team Fortress 2 із дозволеними дублями в команді.

### Виключає

Вибір на весь матч; чергу ролей; напарника Team-Up; альтернативну зброю; оздоблення.

### Ігри-носії

- [`GAME-0187` — Team Fortress 2](../games/s-z/team-fortress-2.md)

## ACT-341

- Назва: Виконати контекстну взаємодію зі станом сутності світу
- Переглянуто: `2026-09-21`

### Операційне визначення

Гравець звертається до одного досяжного заданого автором актора, пристрою або створеного гравцем об’єкта світу зі змінним станом і підтверджує його поточну допустиму взаємодію: допомогу, читання, активацію, збирання, встановлення, ремонт, відмикання або відкриття. Це змінює місцевий стан цілі, актора, пристрою, інвентарю чи маршруту.

### Включає

Читання Bloody Memo у Sastasha, активацію відповідного корала й відкритого перемикача, збирання та використання ключів Captain's Quarters і Waverider Gate, відкриття їхніх брам і включеної до дослідження скрині; керування дверима, ліфтом і бомбою Reactor No. 1 та звільнення Jessie зі сценарної пастки у Final Fantasy VII.

### Виключає

Звичайну атаку зброєю; довільне виготовлення предметів; вибір репліки; взаємодію поза поточним обмеженим маршрутом або ціллю.

### Ігри-носії

- [`GAME-0228` — A Way Out](../games/a-f/a-way-out.md)
- [`GAME-0223` — Aion Classic](../games/a-f/aion-classic.md)
- [`GAME-0257` — "Alien: Isolation"](../games/a-f/alien-isolation.md)
- [`GAME-0320` — "Animal Crossing: New Horizons"](../games/a-f/animal-crossing-new-horizons.md)
- [`GAME-0312` — ASTRO BOT](../games/a-f/astro-bot.md)
- [`GAME-0386` — Banjo-Kazooie](../games/a-f/banjo-kazooie.md)
- [`GAME-0255` — "Batman: Arkham Asylum Game of the Year Edition"](../games/a-f/batman-arkham-asylum-game-of-the-year-edition.md)
- [`GAME-0256` — "BioShock™ Remastered"](../games/a-f/bioshock-remastered.md)
- [`GAME-0347` — "Castlevania: Symphony of the Night"](../games/a-f/castlevania-symphony-of-the-night.md)
- [`GAME-0346` — Chrono Trigger](../games/a-f/chrono-trigger.md)
- [`GAME-0254` — CONTROL Ultimate Edition](../games/a-f/control-ultimate-edition.md)
- [`GAME-0359` — "Crimson Skies: High Road to Revenge"](../games/a-f/crimson-skies-high-road-to-revenge.md)
- [`GAME-0281` — Darkest Dungeon](../games/a-f/darkest-dungeon.md)
- [`GAME-0282` — Dead Cells](../games/a-f/dead-cells.md)
- [`GAME-0368` — Dead Rising](../games/a-f/dead-rising.md)
- [`GAME-0259` — "Dead Space (2023 remake)"](../games/a-f/dead-space-2023.md)
- [`GAME-0266` — Deep Rock Galactic](../games/a-f/deep-rock-galactic.md)
- [`GAME-0193` — Destiny 2](../games/a-f/destiny-2.md)
- [`GAME-0252` — "Detroit: Become Human"](../games/a-f/detroit-become-human.md)
- [`GAME-0353` — "Deus Ex: Game of the Year Edition"](../games/a-f/deus-ex-game-of-the-year-edition.md)
- [`GAME-0264` — Disco Elysium - The Final Cut](../games/a-f/disco-elysium-the-final-cut.md)
- [`GAME-0247` — Dishonored (2012)](../games/a-f/dishonored-2012.md)
- [`GAME-0301` — "Divinity: Original Sin 2 - Definitive Edition"](../games/a-f/divinity-original-sin-2-definitive-edition.md)
- [`GAME-0352` — DOOM (1993)](../games/a-f/doom-1993.md)
- [`GAME-0245` — DOOM (2016)](../games/a-f/doom-2016.md)
- [`GAME-0286` — DOOM Eternal](../games/a-f/doom-eternal.md)
- [`GAME-0269` — DREDGE](../games/a-f/dredge.md)
- [`GAME-0231` — Fallout 4](../games/a-f/fallout-4.md)
- [`GAME-0361` — Fallout: New Vegas](../games/a-f/fallout-new-vegas.md)
- [`GAME-0271` — Far Cry 5](../games/a-f/far-cry-5.md)
- [`GAME-0338` — Final Fantasy VII](../games/a-f/final-fantasy-vii.md)
- [`GAME-0188` — FINAL FANTASY XIV Online](../games/a-f/final-fantasy-xiv-online.md)
- [`GAME-0321` — Gears of War](../games/g-l/gears-of-war.md)
- [`GAME-0381` — GoldenEye 007](../games/g-l/goldeneye-007.md)
- [`GAME-0314` — Grounded](../games/g-l/grounded.md)
- [`GAME-0239` — Half-Life (1998)](../games/g-l/half-life-1998.md)
- [`GAME-0212` — Half-Life 2](../games/g-l/half-life-2.md)
- [`GAME-0315` — Halo 3](../games/g-l/halo-3.md)
- [`GAME-0248` — HITMAN World of Assassination](../games/g-l/hitman-world-of-assassination.md)
- [`GAME-0240` — "Kingdom Come: Deliverance II"](../games/g-l/kingdom-come-deliverance-ii.md)
- [`GAME-0388` — L.A. Noire](../games/g-l/la-noire.md)
- [`GAME-0192` — Left 4 Dead 2](../games/g-l/left-4-dead-2.md)
- [`GAME-0394` — LittleBigPlanet 2](../games/g-l/littlebigplanet-2.md)
- [`GAME-0367` — Mass Effect 2 (Legendary Edition)](../games/m-r/mass-effect-2-legendary-edition.md)
- [`GAME-0238` — "Max Payne (2001)"](../games/m-r/max-payne-2001.md)
- [`GAME-0273` — Max Payne 3](../games/m-r/max-payne-3.md)
- [`GAME-0339` — Metal Gear Solid](../games/m-r/metal-gear-solid.md)
- [`GAME-0260` — Metro Exodus](../games/m-r/metro-exodus.md)
- [`GAME-0244` — "Need for Speed Heat"](../games/m-r/need-for-speed-heat.md)
- [`GAME-0341` — "Ninja Gaiden Black"](../games/m-r/ninja-gaiden-black.md)
- [`GAME-0382` — Ōkami HD](../games/m-r/okami-hd.md)
- [`GAME-0224` — Once Human](../games/m-r/once-human.md)
- [`GAME-0293` — Ori and the Will of the Wisps](../games/m-r/ori-and-the-will-of-the-wisps.md)
- [`GAME-0201` — PAYDAY 2](../games/m-r/payday-2.md)
- [`GAME-0232` — PAYDAY 3](../games/m-r/payday-3.md)
- [`GAME-0291` — Persona 5 Royal](../games/m-r/persona-5-royal.md)
- [`GAME-0258` — "Prey (2017)"](../games/m-r/prey-2017.md)
- [`GAME-0344` — "Prince of Persia: The Sands of Time"](../games/m-r/prince-of-persia-the-sands-of-time.md)
- [`GAME-0358` — Psychonauts](../games/m-r/psychonauts.md)
- [`GAME-0280` — Resident Evil 2 (2019 remake)](../games/m-r/resident-evil-2-2019.md)
- [`GAME-0249` — Resident Evil 4 (2023 remake)](../games/m-r/resident-evil-4-2023.md)
- [`GAME-0348` — "Resident Evil: Director’s Cut"](../games/m-r/resident-evil-directors-cut.md)
- [`GAME-0270` — Risk of Rain 2](../games/m-r/risk-of-rain-2.md)
- [`GAME-0319` — Sea of Thieves](../games/s-z/sea-of-thieves.md)
- [`GAME-0330` — Silent Hill 2 (2024 remake)](../games/s-z/silent-hill-2-2024.md)
- [`GAME-0305` — Sons Of The Forest](../games/s-z/sons-of-the-forest.md)
- [`GAME-0230` — "STAR WARS Battlefront II (2017)"](../games/s-z/star-wars-battlefront-ii-2017.md)
- [`GAME-0213` — "STAR WARS Jedi: Fallen Order"](../games/s-z/star-wars-jedi-fallen-order.md)
- [`GAME-0331` — Starfield](../games/s-z/starfield.md)
- [`GAME-0362` — "The Elder Scrolls III: Morrowind"](../games/s-z/the-elder-scrolls-iii-morrowind.md)
- [`GAME-0292` — The Forest](../games/s-z/the-forest.md)
- [`GAME-0261` — The Last of Us Part I](../games/s-z/the-last-of-us-part-i.md)
- [`GAME-0395` — "The Legend of Zelda: Majora’s Mask"](../games/s-z/the-legend-of-zelda-majoras-mask.md)
- [`GAME-0363` — "The Legend of Zelda: Ocarina of Time"](../games/s-z/the-legend-of-zelda-ocarina-of-time.md)
- [`GAME-0253` — "Titanfall 2"](../games/s-z/titanfall-2.md)
- [`GAME-0349` — "Tom Clancy’s Splinter Cell"](../games/s-z/tom-clancys-splinter-cell.md)
- [`GAME-0250` — Tomb Raider (2013)](../games/s-z/tomb-raider-2013.md)
- [`GAME-0268` — Undertale](../games/s-z/undertale.md)
- [`GAME-0294` — V Rising](../games/s-z/v-rising.md)
- [`GAME-0221` — World of Warcraft](../games/s-z/world-of-warcraft.md)

## ACT-342

- Назва: Повернути розподілені очки розвитку на контрольній точці
- Переглянуто: `2026-08-31`

### Операційне визначення

На дозволеній контрольній точці кампанії гравець вибирає раніше відкриті вузли й повертає вкладені очки до нерозподіленого запасу.

### Включає

Reignite the Sparks у Black Myth: Wukong для одного вузла, гілки або всіх Sparks без плати Will.

### Виключає

Витрата вільного очка; платне скидання характеристик; повернення предмета; розвиток облікового запису.

### Ігри-носії

- [`GAME-0189` — "Black Myth: Wukong"](../games/a-f/black-myth-wukong.md)

## ACT-343

- Назва: Підтвердити походження й тілесну зовнішність
- Переглянуто: `2026-08-31`

### Операційне визначення

На обов’язковому етапі створення нового персонажа гравець обирає доступне походження та фіксує дозволені тіло, обличчя, стать й ім’я як сталу особу для кампанії.

### Включає

Вибір Nord і підтвердження тіла, обличчя та імені на початку Helgen у The Elder Scrolls V: Skyrim Special Edition.

### Виключає

Вибір класу, передісторії чи розподілу очок; зміна спорядження; редактор зовнішності без впливу на вхід до кампанії.

### Ігри-носії

- [`GAME-0190` — "The Elder Scrolls V: Skyrim Special Edition"](../games/s-z/the-elder-scrolls-v-skyrim-special-edition.md)

## ACT-344

- Назва: Дослідити й повернути замок крихкою відмичкою
- Переглянуто: `2026-08-31`

### Операційне визначення

Гравець змінює кут однієї витратної відмички та подає обертальне зусилля, щоб перевірити, чи поточне зміщення поверне циліндр достатньо для відкриття.

### Включає

Один заявлений замок тюремної камери рівня Novice на маршруті Hadvar через Helgen Keep.

### Виключає

Використання відповідного ключа; числовий код; автоматична перевірка навички; руйнування дверей ударом.

### Ігри-носії

- [`GAME-0190` — "The Elder Scrolls V: Skyrim Special Edition"](../games/s-z/the-elder-scrolls-v-skyrim-special-edition.md)
- [`GAME-0349` — "Tom Clancy’s Splinter Cell"](../games/s-z/tom-clancys-splinter-cell.md)

## ACT-345

- Назва: Замовити допустиму будівлю у власному поселенні
- Переглянуто: `2026-09-21`

### Операційне визначення

Гравець обирає поточно допустиму будівлю або рівень ланцюга у власному поселенні й сплачує зазначені ресурси незалежно від того, чи результат негайний, чи входить до обмеженої черги кампанії.

### Включає

Черговий Store House у Kislev Refuge та одна споруда за день у місті Heroes III.

### Виключає

Вільне просторове будівництво в реальному часі; міське виробництво з поступовим накопиченням; найм підрозділу; безкоштовна декорація.

### Ігри-носії

- [`GAME-0332` — "Heroes of Might and Magic III: Complete"](../games/g-l/heroes-of-might-and-magic-iii-complete.md)
- [`GAME-0191` — "Total War: WARHAMMER III"](../games/s-z/total-war-warhammer-iii.md)

## ACT-346

- Назва: Розташувати підрозділи в зоні розгортання
- Переглянуто: `2026-08-31`

### Операційне визначення

До початку бою гравець задає позицію, напрямок, ширину й групування керованих підрозділів у межах дозволеної для сторони області.

### Включає

Розташування допустимих шикувань Kislev Expedition перед першою битвою біля Beacon у визначеному пролозі Total War: WARHAMMER III.

### Виключає

Наказ рухатися після початку бою; поява підкріплень; розміщення поза межею; декоративна схема.

### Ігри-носії

- [`GAME-0191` — "Total War: WARHAMMER III"](../games/s-z/total-war-warhammer-iii.md)

## ACT-347

- Назва: Найняти доступних у поселенні бійців до сталої сили
- Переглянуто: `2026-09-21`

### Операційне визначення

У власному чи відвіданому поселенні вибрати доступний тип і кількість новобранців та сплатити ціну, щоб запас увійшов до сумісних комірок або стосів сталої сили кампанії.

### Включає

Новобранці Tevea в Bannerlord і істоти з жител власного міста Heroes III.

### Виключає

Черга тренування в стратегії реального часу; переконання полоненого; сюжетний супутник; автоматичне зростання населення.

### Ігри-носії

- [`GAME-0332` — "Heroes of Might and Magic III: Complete"](../games/g-l/heroes-of-might-and-magic-iii-complete.md)
- [`GAME-0194` — "Mount & Blade II: Bannerlord"](../games/m-r/mount-and-blade-ii-bannerlord.md)

## ACT-348

- Назва: Сісти верхи, безпосередньо вести доступного скакуна й спішитися
- Переглянуто: `2026-09-10`

### Операційне визначення

Гравець дістається придатного доступного скакуна, переходить до їзди або виходить із неї, а верхи безпосередньо керує темпом, напрямком, стрибком і зупинкою, не доручаючи маршрут автоматичному руху.

### Включає

Посадку, безпосередню їзду й спішування з поточного осідланого коня Артура протягом визначеного розділу 2 Red Dead Redemption 2 та з початкового коня в навчальних польових боях Mount & Blade II: Bannerlord.

### Виключає

Дистанційне підкликання постійного скакуна до персонажа (ACT-271); виклик відсутнього спектрального скакуна з переходом до їзди однією активацією (ACT-247); автоматичний кінний маршрут (ACT-243); окрему здатність супутника (ACT-197); керування дорожнім транспортом (ACT-201).

### Ігри-носії

- [`GAME-0318` — Battletoads](../games/a-f/battletoads.md)
- [`GAME-0329` — "Donkey Kong Country"](../games/a-f/donkey-kong-country.md)
- [`GAME-0194` — "Mount & Blade II: Bannerlord"](../games/m-r/mount-and-blade-ii-bannerlord.md)
- [`GAME-0165` — Red Dead Redemption 2](../games/m-r/red-dead-redemption-2.md)
- [`GAME-0356` — Shadow of the Colossus](../games/s-z/shadow-of-the-colossus.md)
- [`GAME-0354` — Super Mario World](../games/s-z/super-mario-world.md)

## ACT-349

- Назва: Спрямувати блок проти напрямку удару
- Переглянуто: `2026-08-31`

### Операційне визначення

У живому ближньому бою навести й утримувати зброю або щит у вибраному напрямку, щоб геометрія захисту могла зустріти вхідний удар.

### Включає

Напрямлені блоки зброєю та щитом у навчанні Bannerlord.

### Виключає

Верхній або нижній захист у файтингу; часовий парирувальний прийом без вибору напрямку; пасивна броня; покроковий захист.

### Ігри-носії

- [`GAME-0194` — "Mount & Blade II: Bannerlord"](../games/m-r/mount-and-blade-ii-bannerlord.md)

## ACT-350

- Назва: Запросити дозволене місією відновлення виданої машини
- Переглянуто: `2026-08-31`

### Операційне визначення

Під час прямого керування виданою місією машиною запросити передбачене правилами відновлення, ремонт або переміщення до точки відновлення, щоб пошкоджена, розвернута чи застрягла машина могла продовжити спробу без автоматичного зарахування маршруту.

### Включає

Звичайну команду Recover Vehicle у Road Master; повний перезапуск лишається чистою межею повторної спроби.

### Виключає

Кероване перемотування історії; завантаження збереження; перенесення через вільну камеру; довільна домашня позиція.

### Ігри-носії

- [`GAME-0195` — BeamNG.drive](../games/a-f/beamng-drive.md)
- [`GAME-0235` — "Need for Speed: The Run"](../games/m-r/need-for-speed-the-run.md)

## ACT-351

- Назва: Прийняти польовий контракт із позиченою технікою
- Переглянуто: `2026-08-31`

### Операційне визначення

У поточному списку контрактів прийняти одну пропозицію, яка фіксує вид роботи, призначене поле, винагороду й поріг завершення, та погодитися на оголошену плату за сумісну техніку роботодавця.

### Включає

Прийняття контракту Fertilizing у Farming Simulator 25 через Borrow Items.

### Виключає

Перевезення завантаженого дорожнього вантажу; загальний лізинг чи купівлю техніки; призначення працівника зі штучним інтелектом; сам перегляд пропозиції.

### Ігри-носії

- [`GAME-0196` — Farming Simulator 25](../games/a-f/farming-simulator-25.md)

## ACT-352

- Назва: Зчепити й керувати агрегатом із приводом
- Переглянуто: `2026-08-31`

### Операційне визначення

Вирівняти керовану машину із сумісним агрегатом, приєднати або від’єднати його через передбачене зчеплення та під час руху піднімати, опускати, вмикати й вимикати робочий механізм.

### Включає

Зчеплення, опускання й увімкнення позиченого розкидача добрива за трактором.

### Виключає

Постійний вантажний причіп; ручний інструмент; модифікацію зброї; косметичне налаштування; помічника зі штучним інтелектом.

### Ігри-носії

- [`GAME-0196` — Farming Simulator 25](../games/a-f/farming-simulator-25.md)

## ACT-353

- Назва: З’їсти окрему страву й зайняти часовий слот
- Переглянуто: `2026-08-31`

### Операційне визначення

З’їсти перенесену страву іншого типу, додавши або поновивши її обмежений у часі внесок у дозволеному слоті, щоб змінити особисті показники виживання.

### Включає

Одна страва з біому Meadows в одному з трьох активних слотів Valheim.

### Виключає

Запобігання голодній смерті; лікувальне зілля; пасивний запас; надто рання заміна, якої ще не дозволяє травлення.

### Ігри-носії

- [`GAME-0197` — Valheim](../games/s-z/valheim.md)

## ACT-354

- Назва: Прочитати світовий дороговказ до вівтаря боса
- Переглянуто: `2026-08-31`

### Операційне визначення

Взаємодіяти з дороговказом, прив’язаним до певного боса, щоб позначити на особистій мапі найближчий відповідний згенерований вівтар.

### Включає

Вегвізир Ейктюра біля Жертовних Каменів у Valheim.

### Виключає

Рух до вже відомої позначки; кидання витратного засобу пошуку; відкриття орієнтира лише після входу в його радіус.

### Ігри-носії

- [`GAME-0197` — Valheim](../games/s-z/valheim.md)

## ACT-355

- Назва: Підібрати, кинути або втратити зброю з арени
- Переглянуто: `2026-08-31`

### Операційне визначення

Під час бою взаємодіяти з досяжним нейтральним предметом, щоб озброїти бійця, або кинути чи втратити поточну зброю й повернутися до набору команд без зброї.

### Включає

Підбирання та кидання Sword або Hammer бійцем Bödvar у визначеному матчі Stock у Brawlhalla.

### Виключає

Вибір швидкого слота; постійна здобич в інвентарі; gadget; косметичне оформлення зброї.

### Ігри-носії

- [`GAME-0198` — Brawlhalla](../games/a-f/brawlhalla.md)

## ACT-356

- Назва: Виконати ухилення на місці або в напрямку
- Переглянуто: `2026-08-31`

### Операційне визначення

У дозволеному стані виконати ухилення на місці або в обраному напрямку, розпочавши захищене переміщення та прийнявши подальшу затримку до поновлення дії.

### Включає

Наземне ухилення на місці та повітряне ухилення на місці або в напрямку у визначеному матчі Stock у Brawlhalla.

### Виключає

Пасивне уникнення; захист відносно суперника; підказка ходу; перевертання транспортного засобу.

### Ігри-носії

- [`GAME-0198` — Brawlhalla](../games/a-f/brawlhalla.md)
- [`GAME-0282` — Dead Cells](../games/a-f/dead-cells.md)
- [`GAME-0251` — Hades](../games/g-l/hades.md)
- [`GAME-0202` — "NARAKA: BLADEPOINT"](../games/m-r/naraka-bladepoint.md)
- [`GAME-0330` — Silent Hill 2 (2024 remake)](../games/s-z/silent-hill-2-2024.md)

## ACT-358

- Назва: Підкорити, зв’язати або перемістити досяжного цивільного
- Переглянуто: `2026-08-31`

### Операційне визначення

Гравець звертається до одного досяжного цивільного дозволеною командою пограбування: наказує підкоритися, застосовує одну обмежену стяжку або спрямовує вже покірного заручника йти чи зупинитися.

### Включає

Наказ цивільному Bank Heist лягти, зв’язування стяжкою та команди йти або чекати.

### Виключає

Постріл у ворога; передавання плану людині-союзнику; автоматична паніка; обмін заручника після арешту.

### Ігри-носії

- [`GAME-0201` — PAYDAY 2](../games/m-r/payday-2.md)
- [`GAME-0232` — PAYDAY 3](../games/m-r/payday-3.md)

## ACT-359

- Назва: Підняти, нести, кинути або здати важку сумку
- Переглянуто: `2026-09-03`

### Операційне визначення

Гравець переводить допустиму запаковану здобич у спеціальний стан перенесення, рухається або кидає її у світі й здає в сумісній зоні зарахування.

### Включає

Пакування готівки Bank Heist у сумку, перенесення або кидання й завантаження до фургона; пакування, передавання й здавання рідкісноземельної здобичі в Road Rage.

### Виключає

Підбирання розсипаної готівки; спорядження зброї; довільний фізичний предмет; подальший розрахунок виплати.

### Ігри-носії

- [`GAME-0201` — PAYDAY 2](../games/m-r/payday-2.md)
- [`GAME-0232` — PAYDAY 3](../games/m-r/payday-3.md)

## ACT-360

- Назва: Вибрати допустиму область появи перед матчем
- Переглянуто: `2026-08-31`

### Операційне визначення

Під час обмеженої підготовки гравець вибирає одну доступну область мапи як початкову позицію керованого учасника й приймає цей вибір після завершення відліку.

### Включає

Вибір Viper Ning точки появи перед Solo BOT Mode на Wanchu.

### Виключає

Вистрибування з літака; пізніше повернення; випадкову появу без вибору.

### Ігри-носії

- [`GAME-0202` — "NARAKA: BLADEPOINT"](../games/m-r/naraka-bladepoint.md)

## ACT-361

- Назва: Спрямувати себе до цілі тросом із гаком
- Переглянуто: `2026-09-10`

### Операційне визначення

Гравець прицілює багаторазову здібність або витратний заряд гака в поверхню чи учасника, до яких можна зачепитися, і підтверджує рух уздовж троса до вибраної цілі.

### Включає

Пересування, переслідування та відступ із Grappling Hook у NARAKA: BLADEPOINT; рух до позначених опор у Sekiro.

### Виключає

Підтягування предмета до себе; телепортацію без руху вздовж троса; приховане знешкодження цілі.

### Ігри-носії

- [`GAME-0202` — "NARAKA: BLADEPOINT"](../games/m-r/naraka-bladepoint.md)
- [`GAME-0288` — "Sekiro™: Shadows Die Twice - GOTY Edition"](../games/s-z/sekiro-shadows-die-twice.md)

## ACT-362

- Назва: Утримувати або відпускати досяжний хват
- Переглянуто: `2026-09-22`

### Операційне визначення

Коли кероване тіло дістає до придатної нерухомої або рухомої поверхні й має доступний запас хвату, гравець утримує команду для зчеплення та спрямованого руху тіла або відпускає її.

### Включає

Хват за поверхню, підтягування, перехід на уступ і навмисне відпускання в PEAK; хват за хутро й виступи першого рухомого колоса у Shadow of the Colossus.

### Виключає

Звичайну ходьбу; автоматичну драбину; необмежене лазіння по стінах; окреме керування двома руками.

### Ігри-носії

- [`GAME-0203` — "PEAK"](../games/m-r/peak.md)
- [`GAME-0356` — Shadow of the Colossus](../games/s-z/shadow-of-the-colossus.md)

## ACT-363

- Назва: Установити альпіністський засіб на місцевості
- Переглянуто: `2026-08-31`

### Операційне визначення

Гравець вибирає скінченний засіб зі спорядження й застосовує його до сумісної досяжної поверхні, щоб створити опору, лінію чи місце відпочинку.

### Включає

Установлення Rope Spool або Piton у PEAK.

### Виключає

Миттєве підтягування гаком; постійне будівництво; викидання інертного предмета.

### Ігри-носії

- [`GAME-0203` — "PEAK"](../games/m-r/peak.md)

## ACT-364

- Назва: Активувати переносний сигнал у допустимій зоні
- Переглянуто: `2026-09-09`

### Операційне визначення

Маючи придатний сигнальний предмет у визначеній зоні, гравець запалює або запускає його, витрачає звичайне подальше використання й викликає пов’язану відповідь порятунку чи завершення.

### Включає

Запалення Flare у зоні PEAK; постріл із зарядженого Distress Pistol на верхівці Lighthouse у The Long Dark.

### Виключає

Використання того самого предмета лише як зброї; автоматичний вихід від самого прибуття; декоративну дію.

### Ігри-носії

- [`GAME-0203` — "PEAK"](../games/m-r/peak.md)
- [`GAME-0285` — "The Long Dark"](../games/s-z/the-long-dark.md)

## ACT-365

- Назва: Обрати доступне спрямування способу життя
- Переглянуто: `2026-08-31`

### Операційне визначення

Гравець обирає одне доступне спрямування в межах способу життя керованого персонажа, замінюючи сталі впливи цього спрямування без зміни решти стану персонажа.

### Включає

Вибір дипломатичного спрямування для Мурхада у визначеному навчанні Crusader Kings III.

### Виключає

Витрату очка переваги; зміну культури; вибір режиму гри.

### Ігри-носії

- [`GAME-0204` — "Crusader Kings III"](../games/a-f/crusader-kings-iii.md)

## ACT-366

- Назва: Запропонувати допустимий політичний шлюб
- Переглянуто: `2026-08-31`

### Операційне визначення

Гравець обирає двох допустимих персонажів і надсилає звичайну шлюбну пропозицію, яку розв’язують показані правила прийняття та зв’язків.

### Включає

Улаштування запропонованого шляху звичайного шлюбу Мурхада.

### Виключає

велике весілля; автоматичний роман; народження дітей чи спадкування; суто декоративний вибір партнера.

### Ігри-носії

- [`GAME-0204` — "Crusader Kings III"](../games/a-f/crusader-kings-iii.md)

## ACT-367

- Назва: Призначити радника й доручити завдання
- Переглянуто: `2026-08-31`

### Операційне визначення

Гравець заповнює посаду в раді допустимим персонажем або обирає законне завдання й ціль для вже призначеної посадової особи.

### Включає

Раду й указані завдання базового навчання за Мурхада.

### Виключає

Зміну феодальної угоди; найм посади при дворі з доповнення; негайне виконання наслідку завдання.

### Ігри-носії

- [`GAME-0204` — "Crusader Kings III"](../games/a-f/crusader-kings-iii.md)

## ACT-368

- Назва: Оголосити війну за доступною законною підставою
- Переглянуто: `2026-08-31`

### Операційне визначення

Гравець обирає законну ціль і доступну підставу війни, переглядає мету, витрати й наслідки завершення, а тоді починає війну між державами.

### Включає

Оголошення вказаної війни за Десмонд у навчанні Мурхада.

### Виключає

Напад без законної підстави; вибір тактики битви; виконання вимог після перемоги.

### Ігри-носії

- [`GAME-0204` — "Crusader Kings III"](../games/a-f/crusader-kings-iii.md)

## ACT-369

- Назва: Зібрати або розпустити військо держави
- Переглянуто: `2026-08-31`

### Операційне визначення

Гравець наказує доступному ополченню й професійним воїнам зібратися в законній точці або повертає допустиме підняте військо до внесків держави.

### Включає

Збирання війська Мурхада для війни за Десмонд.

### Виключає

Створення нового загону; пересування зібраного війська; сталу сценарну армію без державних зобов’язань.

### Ігри-носії

- [`GAME-0204` — "Crusader Kings III"](../games/a-f/crusader-kings-iii.md)

## ACT-370

- Назва: Зосередити чуття й оглянути виділений доказ
- Переглянуто: `2026-08-31`

### Операційне визначення

Гравець утримує слідчий режим навколо персонажа, простежує показаний поблизу слід і оглядає один досяжний виділений доказ, щоб долучити його до поточного авторського розслідування.

### Включає

Відьмацьке чуття для огляду розгромленого табору, відбитків, гнізда грифона й тіла у завданні «Звір із Білого Саду».

### Виключає

Автоматичне відкриття всіх майбутніх доказів; зовнішнє проходження; детектор, що повідомляє лише фізичну близькість.

### Ігри-носії

- [`GAME-0255` — "Batman: Arkham Asylum Game of the Year Edition"](../games/a-f/batman-arkham-asylum-game-of-the-year-edition.md)
- [`GAME-0205` — "The Witcher 3: Wild Hunt"](../games/s-z/the-witcher-3-wild-hunt.md)

## ACT-371

- Назва: Звичайно викликати або встановити одного монстра
- Переглянуто: `2026-09-01`

### Операційне визначення

У допустимій власній головній фазі гравець викладає законного монстра з руки горілиць у позицію атаки як звичайний виклик або долілиць у позицію захисту як звичайне встановлення й витрачає спільне право цього ходу.

### Включає

Звичайного монстра 4-го або нижчого рівня в розділі 10003.

### Виключає

Особливий чи переворотний виклик; виклик за дією ефекту; розв’язання атаки.

### Ігри-носії

- [`GAME-0206` — "Yu-Gi-Oh! Master Duel"](../games/s-z/yu-gi-oh-master-duel.md)

## ACT-372

- Назва: Виконати один особливий виклик за процедурою
- Переглянуто: `2026-09-01`

### Операційне визначення

Гравець оголошує одну зараз допустиму процедуру особливого виклику, вибирає всі потрібні матеріали або джерело й остаточно витрачає їх, щоб відповідний монстр увійшов до законної зони та позиції.

### Включає

Доступні Synchro, Xyz або Link Summon із п’яти карт додаткової колоди розділу 10003.

### Виключає

Звичайний виклик із жертвою; автоматичний виклик ефектом без обраної процедури; створення колоди.

### Ігри-носії

- [`GAME-0206` — "Yu-Gi-Oh! Master Duel"](../games/s-z/yu-gi-oh-master-duel.md)

## ACT-373

- Назва: Установити одну карту Spell або Trap із руки
- Переглянуто: `2026-09-01`

### Операційне визначення

У допустимій головній фазі гравець кладе одну карту Spell або Trap із руки долілиць у вільну сумісну зону, не розв’язуючи її текст.

### Включає

Установлення Ballista Squad, Call of the Haunted або Skill Successor у незмінному пакеті Tutorial.

### Виключає

Активацію карти; звичайне встановлення монстра; безпосереднє відкрите розміщення тривалого об’єкта.

### Ігри-носії

- [`GAME-0206` — "Yu-Gi-Oh! Master Duel"](../games/s-z/yu-gi-oh-master-duel.md)

## ACT-374

- Назва: Активувати одну допустиму карту або ефект
- Переглянуто: `2026-09-01`

### Операційне визначення

Гравець оголошує одну зараз доступну карту Spell, Trap або ефект монстра, сплачує визначену вартість і вибирає потрібні цілі, щоб активація стала першою нерозв’язаною ланкою ланцюга.

### Включає

Активацію звичайної Spell, раніше встановленої Trap або допустимого ефекту монстра з незмінного пакета.

### Виключає

Негайне розв’язання тексту; відповідь пізнішою ланкою; сталий текст без активації.

### Ігри-носії

- [`GAME-0206` — "Yu-Gi-Oh! Master Duel"](../games/s-z/yu-gi-oh-master-duel.md)

## ACT-375

- Назва: Додати допустиму відповідь наступною ланкою ланцюга
- Переглянуто: `2026-09-01`

### Операційне визначення

Після чужої активації гравець вибирає законну відповідь такої самої або вищої швидкості, сплачує її вартість і додає її наступною пронумерованою ланкою до розв’язання будь-якого ефекту.

### Включає

Відповідь допустимою Trap, Quick-Play Spell або Quick Effect у визначеному двобої.

### Виключає

Відповідь із Spell Speed 1; нову ланку під час розв’язання завершеного ланцюга; передачу пріоритету за правилами MTG.

### Ігри-носії

- [`GAME-0206` — "Yu-Gi-Oh! Master Duel"](../games/s-z/yu-gi-oh-master-duel.md)

## ACT-376

- Назва: Оголосити атаку одного допустимого монстра
- Переглянуто: `2026-09-01`

### Операційне визначення

У законній фазі бою гравець вибирає одного придатного відкритого монстра в позиції атаки й остаточно спрямовує його звичайну атаку на законного ворожого монстра або безпосередньо, коли поле це дозволяє.

### Включає

Кожне окреме оголошення атаки в розділі 10003.

### Виключає

Одночасний вибір групи нападників; вибір блокувальника; розрахунок бойової шкоди.

### Ігри-носії

- [`GAME-0206` — "Yu-Gi-Oh! Master Duel"](../games/s-z/yu-gi-oh-master-duel.md)

## ACT-377

- Назва: Змінити бойову позицію одного допустимого монстра
- Переглянуто: `2026-09-01`

### Операційне визначення

У допустимій власній головній фазі гравець переводить одного монстра між відкритими позиціями атаки й захисту або виконує переворотний виклик придатного встановленого монстра.

### Включає

Законну ручну зміну позиції або Flip Summon у розділі 10003.

### Виключає

Зміну позиції ефектом; звичайне встановлення з руки; оголошення атаки.

### Ігри-носії

- [`GAME-0206` — "Yu-Gi-Oh! Master Duel"](../games/s-z/yu-gi-oh-master-duel.md)

## ACT-378

- Назва: Обслуговувати споряджену зброю ближнього бою в польових умовах
- Переглянуто: `2026-09-13`

### Операційне визначення

Гравець починає незахищену дію з багаторазовим засобом обслуговування спорядженої зброї ближнього бою; після завершення анімації її поточна циклічна шкала гостроти або міцності відновлюється, а бій і час маршруту весь цей час тривають.

### Включає

Заточування Hunter's Knife I точильним каменем під час визначеного завдання Monster Hunter: World; відновлення додатної міцності зброї багаторазовим Grinder у визначеному вступі Lies of P.

### Виключає

Витрачання скінченного лікувального предмета; поліпшення в кузні; автоматичне відновлення після бою; ремонт незворотного руйнування зброї.

### Ігри-носії

- [`GAME-0290` — Lies of P](../games/g-l/lies-of-p.md)
- [`GAME-0297` — 'MONSTER HUNTER RISE'](../games/m-r/monster-hunter-rise.md)
- [`GAME-0207` — 'Monster Hunter: World'](../games/m-r/monster-hunter-world.md)

## ACT-379

- Назва: Таранити досяжний ворожий автомобіль
- Переглянуто: `2026-09-01`

### Операційне визначення

Під час безпосереднього керування гравець спрямовує свій автомобіль у досяжну ворожу машину, погоджуючись на втрату швидкості, позиції та стану заради руйнівного зіткнення.

### Включає

Таран автомобіля охорони House у визначених етапах The Highway Heist гри Need for Speed Payback.

### Виключає

Випадкове зіткнення з потоком; постріл зі встановленої зброї; постановочну аварію без керованого заходу.

### Ігри-носії

- [`GAME-0208` — 'Need for Speed Payback'](../games/m-r/need-for-speed-payback.md)

## ACT-380

- Назва: Завантажити або вивантажити вибрані підрозділи через транспорт
- Переглянуто: `2026-09-01`

### Операційне визначення

Гравець вибирає допустимі наземні підрозділи й наказує їм увійти до одного досяжного транспорту або вибирає транспорт із пасажирами й наказує повернути їх на прохідну землю в допустимому місці.

### Включає

Завантаження шведських селян і солдатів на пором та їх вивантаження на протилежному березі в Cossacks 3: War Ruse — Peace.

### Виключає

Рух самого порома; автоматичну висадку підкріплення; посадку одного безпосередньо керованого персонажа в автомобіль; телепортацію між сталими точками.

### Ігри-носії

- [`GAME-0209` — Cossacks 3](../games/a-f/cossacks-3.md)

## ACT-381

- Назва: Застосувати контекстну дію одного предмета до іншого
- Переглянуто: `2026-09-01`

### Операційне визначення

Гравець бере один предмет до рук, вибирає сумісний предмет у спорядженні або світі й виконує доступне поєднання, поділ, заряджання, ремонт чи просте ручне виготовлення.

### Включає

Дії Combine, поділ стосу, заряджання набоями, ремонт і виготовлення з двох предметів у DayZ.

### Виключає

Абстрактну чергу рецептів; незмінне вдягання здобичі; безпосереднє споживання; автоматичне підбирання; недоступні для цієї пари поєднання.

### Ігри-носії

- [`GAME-0210` — DayZ](../games/a-f/dayz.md)

## ACT-382

- Назва: Звернутися до людей поблизу голосом або жестом
- Переглянуто: `2026-09-01`

### Операційне визначення

Гравець навмисно говорить через просторовий канал або виконує видимий жест до людей поруч, поки керування спільним світом триває.

### Включає

Голос поблизу та жести DayZ для привітання, попередження, переговорів, здачі або обману незнайомця.

### Виключає

Надійний командний канал; зовнішній голосовий сервіс; автоматичні звуки болю; гарантовану правду, союз чи відповідь.

### Ігри-носії

- [`GAME-0210` — DayZ](../games/a-f/dayz.md)

## ACT-383

- Назва: Тримати або відпускати сталий захист у ближньому бою
- Переглянуто: `2026-09-01`

### Операційне визначення

Під час живого ближнього бою гравець тримає зброю в постійному захисті або відпускає цю команду, приймаючи подальше виснаження шкали блоку й можливу відкритість після її вичерпання.

### Включає

Утримання та відпускання блоку світловим мечем Кела під час визначеного першого візиту на Богано.

### Виключає

Верхній або нижній захист файтингу; спрямований блок; одиничне своєчасне парирування; пасивну броню чи хід «Захист».

### Ігри-носії

- [`GAME-0288` — "Sekiro™: Shadows Die Twice - GOTY Edition"](../games/s-z/sekiro-shadows-die-twice.md)
- [`GAME-0303` — Sifu](../games/s-z/sifu.md)
- [`GAME-0213` — "STAR WARS Jedi: Fallen Order"](../games/s-z/star-wars-jedi-fallen-order.md)

## ACT-384

- Назва: Перемикати обмежувач швидкості автомобіля
- Переглянуто: `2026-09-01`

### Операційне визначення

Під час безпосереднього керування дорожнім автомобілем гравець вмикає або вимикає верхню межу швидкості, яка обмежує подальше прискорення, але залишає ручними кермо, гальма й вибір маршруту.

### Включає

Перемикання обмежувача клавішею F5 під час визначених поїздок таксі у Mafia (2002).

### Виключає

Автоматичний рух маршрутом; постійне вдосконалення двигуна; налаштування складності; звичайне гальмування; довільну швидкість круїз-контролю.

### Ігри-носії

- [`GAME-0214` — "Mafia (2002)"](../games/m-r/mafia-2002.md)

## ACT-385

- Назва: Кидати або відкликати багаторазовий ручний інструмент
- Переглянуто: `2026-09-05`

### Операційне визначення

Гравець наводить один доступний багаторазовий ручний інструмент на сумісну досяжну ціль і кидає його або відкликає вже встановлений інструмент назад до стану, придатного для тримання в руці.

### Включає

Кидання й миттєве відкликання обмеженого набору цвяхів Коді у відрізку The Shed гри It Takes Two; наведення, кидок і відкликання Leviathan Axe у дослідженому початковому маршруті God of War.

### Виключає

Витратний постріл у ворога; встановлення будівельної деталі з інвентарю; відкликання самостійного напарника; підбирання звичайної здобичі.

### Ігри-носії

- [`GAME-0263` — God of War](../games/g-l/god-of-war.md)
- [`GAME-0215` — It Takes Two](../games/g-l/it-takes-two.md)

## ACT-386

- Назва: Бити молотком своєї ролі по досяжному механізму
- Переглянуто: `2026-09-01`

### Операційне визначення

Закріплений за роллю гравець завдає близького удару молотком по сумісному досяжному механізму, щоб запустити його місцеву дію.

### Включає

Удари Мей по позначених кнопках, замках, замках Toolbox і механізму запуску у визначеному відрізку The Shed.

### Виключає

Прицільну атаку по тілу ворога; звичайну взаємодію без знаряддя; ремонт будівлі; декоративний замах без відповіді механізму.

### Ігри-носії

- [`GAME-0215` — It Takes Two](../games/g-l/it-takes-two.md)

## ACT-387

- Назва: Підтвердити перехід до доступного першого класу
- Переглянуто: `2026-09-01`

### Операційне визначення

Після виконання умов переходу до першого класу гравець обирає один сумісний запропонований клас і підтверджує виключну зміну класу цього постійного персонажа.

### Включає

Підтвердження Warrior для Human Fighter рівня 20 із завершеним Path of Destiny - Beginning на Chronos у Lineage II Live.

### Виключає

Вибір початкової раси й класу під час створення; тимчасову зміну ролі на появі; розподіл очка вміння; пізнішу платну зміну класу.

### Ігри-носії

- [`GAME-0219` — Lineage II](../games/g-l/lineage-ii.md)

## ACT-388

- Назва: Будувати або ремонтувати задане польове укріплення
- Переглянуто: `2026-09-01`

### Операційне визначення

Гравець вибирає видимий авторський контур, дістає сумісний польовий інструмент і тримає взаємодію, доки не зведе або не відремонтує захисну чи постачальну споруду.

### Включає

Траншеї, мішки з піском, перешкоди, протитанкові загородження й станції постачання на Arras у Battlefield V.

### Виключає

Довільне будівництво; укріплення стіни з командного запасу Siege; ремонт техніки; руйнування геометрії.

### Ігри-носії

- [`GAME-0220` — Battlefield V](../games/a-f/battlefield-v.md)

## ACT-389

- Назва: Витратити очки загону на виклик підкріплення
- Переглянуто: `2026-09-01`

### Операційне визначення

Поточний командир загону вибирає доступне підкріплення, визначає потрібну ціль і підтверджує витрату спільно зароблених очок загону.

### Включає

Виклик постачання, димової завіси або допустимого удару в Battlefield V.

### Виключає

Особистий ґаджет; гранату з інвентарю; валюту облікового запису; автоматичний постановочний удар.

### Ігри-носії

- [`GAME-0220` — Battlefield V](../games/a-f/battlefield-v.md)

## ACT-390

- Назва: Готувати приціл і руку, тоді вихоплювати зброю в дуелі
- Переглянуто: `2026-09-02`

### Операційне визначення

Перед дуеллю з визначеним суперником гравець одночасно тримає прицільну зосередженість на ньому та руку персонажа біля кобури, а тоді вихоплює револьвер раніше або у відповідь на видимий рух суперника.

### Включає

Підготовку Сайласа проти Пата Ґарретта в першій сюжетній дуелі Call of Juarez: Gunslinger.

### Виключає

Звичайне прицілювання з уже вихопленою зброєю; вибір бійця перед матчем; одну кнопку без підготовчого стану; автоматичну сцену.

### Ігри-носії

- [`GAME-0222` — "Call of Juarez: Gunslinger"](../games/a-f/call-of-juarez-gunslinger.md)

## ACT-391

- Назва: Ударяти по вдосконалюваному джерелу нагороди перед отриманням
- Переглянуто: `2026-09-02`

### Операційне визначення

Після появи небойового джерела нагороди гравець спрямовує на нього звичайні атаки, щоб спробувати змінити рівень нагороди, а потім окремо взаємодіє з ним і забирає результат.

### Включає

Удари по Mystic Cube of Light and Darkness в Aion Classic перед отриманням посиленого спорядження.

### Виключає

Атаку ворога; відкривання незмінної скрині; руйнування пристрою задля проходу; гарантоване вдосконалення за валюту.

### Ігри-носії

- [`GAME-0223` — Aion Classic](../games/a-f/aion-classic.md)

## ACT-392

- Назва: Керувати тягою й трьома осями повороту апарата
- Переглянуто: `2026-09-06`

### Операційне визначення

Безперервно задавати тягу, тангаж, рискання й крен одного апарата, щоб змінювати його положення та орієнтацію у відкритому тривимірному просторі, зберігаючи пряме керування цим апаратом.

### Включає

Політ на закріпленому винищувачі T-65B X-wing у місії Form the Vanguard; керування тягою та трьома осями зібраної ракети-носія від стартового столу до орбітального польоту в дослідженому завданні Kerbal Space Program.

### Виключає

Вибір цілі на мапі; наказ автономному загону; аеродинамічний політ літака з розбігом по смузі, кермовими поверхнями й гальмуванням коліс; наземне водіння від третьої особи; неінтерактивну сцену польоту.

### Ігри-носії

- [`GAME-0359` — "Crimson Skies: High Road to Revenge"](../games/a-f/crimson-skies-high-road-to-revenge.md)
- [`GAME-0267` — Kerbal Space Program](../games/g-l/kerbal-space-program.md)
- [`GAME-0225` — "STAR WARS: Squadrons"](../games/s-z/star-wars-squadrons.md)
- [`GAME-0331` — Starfield](../games/s-z/starfield.md)

## ACT-393

- Назва: Розподіляти скінченну енергію між живими системами апарата
- Переглянуто: `2026-09-21`

### Операційне визначення

Під час польоту перенаправляти один спільний скінченний запас енергії між поточними системами руху, захисту, зброї або подорожі чи відновлювати збалансований розподіл.

### Включає

Двигуни, лазери й щити X-wing; двигуни, щити, зброя та grav drive Frontier у Starfield.

### Виключає

Купівлю поліпшень; постійний компонент; перенесення заряду між сторонами щита.

### Ігри-носії

- [`GAME-0225` — "STAR WARS: Squadrons"](../games/s-z/star-wars-squadrons.md)
- [`GAME-0331` — Starfield](../games/s-z/starfield.md)

## ACT-394

- Назва: Спрямовувати заряд щита до одного боку винищувача
- Переглянуто: `2026-09-02`

### Операційне визначення

Переносити наявний заряд захисного поля до передньої або задньої півсфери чи знову врівноважувати його під час польоту.

### Включає

Переднє та заднє фокусування щитів X-wing у Form the Vanguard.

### Виключає

Подавання енергії до щитів; розворот корабля; ремонт корпусу.

### Ігри-носії

- [`GAME-0225` — "STAR WARS: Squadrons"](../games/s-z/star-wars-squadrons.md)

## ACT-395

- Назва: Випускати готовий протиракетний засіб винищувача
- Переглянуто: `2026-09-02`

### Операційне визначення

У відповідь на попередження про керовану ракету витратити один готовий протиракетний заряд у вибраний момент, щоб спробувати зірвати наведення або перехопити загрозу.

### Включає

Використання Seeker Warheads із фіксованого спорядження X-wing.

### Виключає

Ухилення лише керуванням; запуск ракети по цілі; пасивне поглинання щитом.

### Ігри-носії

- [`GAME-0225` — "STAR WARS: Squadrons"](../games/s-z/star-wars-squadrons.md)

## ACT-396

- Назва: Просити ремонт і поповнення в ШІ-напарника
- Переглянуто: `2026-09-02`

### Операційне визначення

Подати контекстний запит підтримки, щоб ШІ-напарник доставив до поточного винищувача ремонтний і боєприпасний вантаж під час місії.

### Включає

Запит підтримки в U-wing Ганні у Form the Vanguard.

### Виключає

Стикування зі станцією; власний ремонтний набір; автоматичне відновлення.

### Ігри-носії

- [`GAME-0225` — "STAR WARS: Squadrons"](../games/s-z/star-wars-squadrons.md)

## ACT-397

- Назва: Активувати досяжну консоль спільних правил
- Переглянуто: `2026-09-02`

### Операційне визначення

Взаємодіяти з досяжною консоллю поточного матчу, щоб отримати показану типізовану зміну правил для заявленого кола учасників.

### Включає

Захоплення Override Console у Fortnite v42.00 Zero Build Solo.

### Виключає

Введення Lobby Hack до добору гравців; налаштування приватного сервера; підбирання пасивного предмета; придбання поліпшення акаунта.

### Ігри-носії

- [`GAME-0227` — Fortnite](../games/a-f/fortnite.md)

## ACT-398

- Назва: Передати переносне кооперативне знаряддя досяжному напарникові
- Переглянуто: `2026-09-02`

### Операційне визначення

Безпосередньо передати одне переносне цільове знаряддя від поточного носія придатному незалежно керованому напарникові через заданий зв'язок передачі.

### Включає

Передавання різця від Лео до Вінсента після завершення власного пролому в Cell Breach у A Way Out.

### Виключає

Викидання звичайної здобичі для будь-кого; дублювання предмета; віддалену зміну чужого інвентарю; відкликання особистого багаторазового знаряддя.

### Ігри-носії

- [`GAME-0228` — A Way Out](../games/a-f/a-way-out.md)

## ACT-399

- Назва: Подати сумісний матеріал до вказаного технологічного гнізда
- Переглянуто: `2026-09-02`

### Операційне визначення

Вибрати пошкоджене або заряджуване технологічне гніздо й подати сумісний переношуваний матеріал чи складник, щоб просунути ремонт або запас заряду.

### Включає

Заповнення потрібного гнізда Scanner, Analysis Visor, Mining Beam, Pulse Engine, Launch Thruster, захисту від середовища або життєзабезпечення в ранній No Man’s Sky.

### Виключає

Виготовлення складника; ремонт будівельного блока; застосування лікування; необов'язкове поліпшення неушкодженої технології.

### Ігри-носії

- [`GAME-0229` — "No Man’s Sky"](../games/m-r/no-mans-sky.md)

## ACT-400

- Назва: Запустити локальний оглядовий імпульс із відновленням
- Переглянуто: `2026-09-02`

### Операційне визначення

Активувати справний локальний оглядовий пристрій, щоб один обмежений імпульс запросив показ придатних ресурсів поблизу.

### Включає

Запуск відремонтованого Scanner у навчанні No Man’s Sky.

### Виключає

Тривале наведення аналізатора на одну ціль; quickhack; віддалене сканування сектора; постійні пасивні позначки.

### Ігри-носії

- [`GAME-0229` — "No Man’s Sky"](../games/m-r/no-mans-sky.md)

## ACT-401

- Назва: Розподілити фіксований початковий запас характеристик персонажа
- Переглянуто: `2026-09-03`

### Операційне визначення

До входу в кампанію змінити значення названих механічних характеристик персонажа й підтвердити профіль, у якому підвищення витрачають один спільний фіксований запас очок.

### Включає

Розподіл початкових очок S.P.E.C.I.A.L. у Fallout 4 і підтвердження стартового профілю.

### Виключає

Косметичну зовнішність; вибір життєвого шляху, походження, класу або передісторії; витрату пізнішого очка рівня чи здібності; спорядження.

### Ігри-носії

- [`GAME-0231` — Fallout 4](../games/a-f/fallout-4.md)
- [`GAME-0361` — Fallout: New Vegas](../games/a-f/fallout-new-vegas.md)

## ACT-402

- Назва: Забрати одну записану нагороду за виконане випробування
- Переглянуто: `2026-09-03`

### Операційне визначення

Гравець явно підтверджує один запис виконаного випробування в журналі, щоб перевести його окрему нагороду до стану гравця.

### Включає

Окреме забирання кожного завершеного рядка Basics of Survival у 7 Days to Die.

### Виключає

Автоматичну видачу без команди; забирання предмета зі світу; здавання завдання NPC.

### Ігри-носії

- [`GAME-0233` — 7 Days to Die](../games/0-9/7-days-to-die.md)

## ACT-403

- Назва: Замінити один доступний сумісний модуль чинної зброї в бою
- Переглянуто: `2026-09-03`

### Операційне визначення

Під живим керуванням відкрити обмежену панель модулів, обрати доступний сумісний варіант однієї категорії чинної зброї й підтвердити заміну без повернення до підготовки.

### Включає

Заміну прицілу, ствола, боєприпасу або підствольного модуля через Plus у Battlefield 2042.

### Виключає

Налаштування наступного спорядження; зміну самої зброї; добування модуля; косметичне оформлення.

### Ігри-носії

- [`GAME-0234` — Battlefield 2042](../games/a-f/battlefield-2042.md)
- [`GAME-0246` — Crysis Remastered](../games/a-f/crysis-remastered.md)

## ACT-404

- Назва: Замовити одну доступну машину підтримки до допустимої позиції
- Переглянуто: `2026-09-03`

### Операційне визначення

Під живим керуванням обрати доступну машину на спільній панелі, указати допустиму позицію доставлення у світі й підтвердити запит.

### Включає

Замовлення наземної машини через планшет call-in у Battlefield 2042.

### Виключає

Появу всередині машини з екрана розгортання; витрату валюти акаунта; виклик удару командиром загону; посадку після доставлення.

### Ігри-носії

- [`GAME-0234` — Battlefield 2042](../games/a-f/battlefield-2042.md)

## ACT-405

- Назва: Позначати видимого учасника оптичним пристроєм
- Переглянуто: `2026-09-03`

### Операційне визначення

Користуючись оптичним пристроєм спостереження, гравець достатньо довго тримає у фокусі одного видимого допустимого живого учасника, щоб запросити прив’язану до нього сталу тактичну мітку.

### Включає

Позначення камерою пірата або сторожового собаки в межах першого аванпосту Far Cry 3.

### Виключає

Саме лише бачення учасника; довільну позначку на мапі; автоматичне командне виявлення; огляд ресурсів місцевості замість живого учасника.

### Ігри-носії

- [`GAME-0243` — Battlefield Hardline](../games/a-f/battlefield-hardline.md)
- [`GAME-0246` — Crysis Remastered](../games/a-f/crysis-remastered.md)
- [`GAME-0236` — Far Cry 3](../games/a-f/far-cry-3.md)
- [`GAME-0306` — METAL GEAR SOLID V: THE PHANTOM PAIN](../games/m-r/metal-gear-solid-v-the-phantom-pain.md)

## ACT-406

- Назва: Кидати інертне відволікання досяжною точкою світу
- Переглянуто: `2026-09-03`

### Операційне визначення

Гравець обирає досяжний напрямок або місце падіння й кидає неушкоджувальний предмет, чия правилами визначена мета — створити помітний подразник, а не поранити ціль.

### Включає

Кидання каменя, щоб відвернути допустимого пірата в межах першого аванпосту Far Cry 3.

### Виключає

Кидання ушкоджувальної гранати; постріл; позначку на мапі; заданий звук, місце якого гравець не обирає.

### Ігри-носії

- [`GAME-0257` — "Alien: Isolation"](../games/a-f/alien-isolation.md)
- [`GAME-0243` — Battlefield Hardline](../games/a-f/battlefield-hardline.md)
- [`GAME-0236` — Far Cry 3](../games/a-f/far-cry-3.md)
- [`GAME-0248` — HITMAN World of Assassination](../games/g-l/hitman-world-of-assassination.md)
- [`GAME-0260` — Metro Exodus](../games/m-r/metro-exodus.md)
- [`GAME-0261` — The Last of Us Part I](../games/s-z/the-last-of-us-part-i.md)

## ACT-407

- Назва: Спожити переносний відновлювальний засіб без зупинки живого керування
- Переглянуто: `2026-09-03`

### Операційне визначення

Поки керований боєць зберігає рух і бойові дії в реальному часі, гравець витрачає одну одиницю зі скінченного переносного запасу відновлення та запускає відкладене повернення стану замість переривного лікувального процесу.

### Включає

Використання одного painkiller у Roscoe Street Station, поки рух, прицілювання й ворожі дії лишаються доступними.

### Виключає

Переривне лікування бинтом або шприцом за таймером; пасивне відновлення здоров’я; покроковий предмет із миттєвим повним ефектом; лікування іншого учасника.

### Ігри-носії

- [`GAME-0238` — "Max Payne (2001)"](../games/m-r/max-payne-2001.md)

## ACT-408

- Назва: Перемикати досяжного союзного учасника між слідуванням і очікуванням
- Переглянуто: `2026-09-03`

### Операційне визначення

Гравець звертається до одного досяжного допустимого союзного учасника світу й контекстною командою переводить його з місцевого очікування до слідування за керованим персонажем або зі слідування назад до очікування.

### Включає

Використання вченого або охоронця, щоб почати чи припинити слідування в межах Unforeseen Consequences у Half-Life (1998).

### Виключає

Розгортання власного супутника з інвентарю; наказ рухатися до точки або атакувати; вибір репліки; пряме керування союзним тілом; заданий супровід без перемикання.

### Ігри-носії

- [`GAME-0239` — Half-Life (1998)](../games/g-l/half-life-1998.md)

## ACT-409

- Назва: Перемикати персональний переносний освітлювальний пристрій
- Переглянуто: `2026-09-10`

### Операційне визначення

Під час безпосереднього керування гравець перемикає один переносний персональний освітлювальний пристрій між активним місцевим світловим полем і неактивним станом, не втрачаючи звичайних повноважень руху чи зброї; переходи заряду та окрема команда поповнення належать іншим генам.

### Включає

Увімкнення й вимкнення ліхтарика HEV у межах Unforeseen Consequences у Half-Life (1998) та ліхтарика зі скінченними батарейками у визначеній лікарняній місії Alien: Isolation.

### Виключає

Розміщення смолоскипа; підживлення багаття; косметичне освітлення; спалах зброї; нічне бачення без місцевого світлового поля; одноразовий кинутий фаєр; команду витратити переносний запас на поповнення пристрою (ACT-453).

### Ігри-носії

- [`GAME-0257` — "Alien: Isolation"](../games/a-f/alien-isolation.md)
- [`GAME-0239` — Half-Life (1998)](../games/g-l/half-life-1998.md)
- [`GAME-0340` — "Halo: Combat Evolved Anniversary"](../games/g-l/halo-combat-evolved-anniversary.md)
- [`GAME-0260` — Metro Exodus](../games/m-r/metro-exodus.md)
- [`GAME-0261` — The Last of Us Part I](../games/s-z/the-last-of-us-part-i.md)

## ACT-410

- Назва: Виконувати один ручний крок рецепта на робочій станції
- Переглянуто: `2026-09-03`

### Операційне визначення

На досяжній ручній станції гравець обирає й безпосередньо застосовує один сумісний складник або орган керування, змінюючи незавершену суміш замість одноразового замовлення всього рецепта.

### Включає

Додавання основи чи складника, керування нагріванням, пісковим годинником, ступкою та вихідною посудиною у визначеному варінні Kingdom Come: Deliverance II.

### Виключає

Одноразове виготовлення відомого рецепта; сітка ремесла; автономне виробництво; декоративна взаємодія без стану суміші.

### Ігри-носії

- [`GAME-0240` — "Kingdom Come: Deliverance II"](../games/g-l/kingdom-come-deliverance-ii.md)
- [`GAME-0300` — Overcooked! 2](../games/m-r/overcooked-2.md)

## ACT-411

- Назва: Підтвердити команди й параметри одного очного матчу
- Переглянуто: `2026-09-03`

### Операційне визначення

Перед початком обмеженого змагання гравець підтверджує одну допустиму керовану сторону, суперника й відкриті параметри, що визначають цю окрему спробу.

### Включає

Вибір Thunder, Knicks, локального матчу проти CPU, складності Pro й п’ятихвилинних чвертей у NBA 2K26.

### Виключає

Побудову постійного складу; добір суперника мережею; драфт; цілий сезон; зміну правил під час гри; конкретні назви й числа як гени.

### Ігри-носії

- [`GAME-0241` — NBA 2K26](../games/m-r/nba-2k26.md)

## ACT-412

- Назва: Спрямувати пас утримуваного м’яча допустимому партнерові
- Переглянуто: `2026-09-03`

### Операційне визначення

Коли керований гравець володіє спільним м’ячем у руках, гравець задає ціль, напрям і вид пасу, що випускає м’яч до допустимого партнера.

### Включає

Прямі, відскокові, навісні й випереджальні паси у визначеному матчі NBA 2K26.

### Виключає

Передачу футбольного м’яча ногою; нецільове позбавлення м’яча; кидок у кошик; автоматичний пас; вибір адресата в меню.

### Ігри-носії

- [`GAME-0241` — NBA 2K26](../games/m-r/nba-2k26.md)

## ACT-413

- Назва: Виконати кидок у кошик із керованим моментом випуску
- Переглянуто: `2026-09-03`

### Операційне визначення

Гравець починає й відпускає допустимий кидок у кошик, фіксуючи напрям, вид спроби й момент випуску для негайного оцінювання просторового та захисного контексту.

### Включає

Кидки кнопкою чи стіком, проходи під кошик і данки у визначеному матчі NBA 2K26.

### Виключає

Удар у футбольні ворота; штрафний, започаткований лише суддівською послідовністю; автоматичний результат симуляції; пас біля кошика.

### Ігри-носії

- [`GAME-0241` — NBA 2K26](../games/m-r/nba-2k26.md)

## ACT-414

- Назва: Виконати спробу перехоплення, блокування або протидії кидку
- Переглянуто: `2026-09-03`

### Операційне визначення

Під час захисту живого володіння гравець виконує типізоване втручання проти носія, лінії пасу або кидка, ризикуючи позицією й контактом заради відхилення, втрати або промаху.

### Включає

Перехоплення біля м’яча чи в лінії пасу, блокування та протидія кидку у NBA 2K26.

### Виключає

Саму пасивну близькість; футбольний підкат; вибір схеми в меню; автоматичне втручання партнера; навмисний фол як окрему стратегію.

### Ігри-носії

- [`GAME-0241` — NBA 2K26](../games/m-r/nba-2k26.md)

## ACT-415

- Назва: Викликати заслін партнера для поточного носія м’яча
- Переглянуто: `2026-09-03`

### Операційне визначення

Керуючи носієм м’яча, гравець просить допустимого партнера підійти й поставити тимчасовий законний заслін, а потім обирає спосіб використати розгалуження маршруту.

### Включає

Виклик і використання заслону для проходу, пасу або кидка у NBA 2K26.

### Виключає

Постійну перешкоду; керування цілою тактичною схемою; невикликаний автоматичний заслін; незаконний рухомий контакт.

### Ігри-носії

- [`GAME-0241` — NBA 2K26](../games/m-r/nba-2k26.md)

## ACT-416

- Назва: Підтвердити один підказаний маневр за допоміжного кермування
- Переглянуто: `2026-09-03`

### Операційне визначення

Поки система безперервно рухає й кермує транспортом, гравець підтверджує одну доступну гілку маршруту, дрифт або повітряний маневр, за яким система перебудує траєкторію.

### Включає

Вибір гілки чи підказаного маневру TouchDrive та початок допустимого дрифту у визначеній Career-гонці Asphalt Legends.

### Виключає

Необмежене аналогове кермування; маршрут на паузі; пасивне автоматичне ведення без живого вибору; витрату нітро.

### Ігри-носії

- [`GAME-0242` — "Asphalt Legends"](../games/a-f/asphalt-legends.md)

## ACT-417

- Назва: Наказати придатному противникові підкоритися й заарештувати його живим
- Переглянуто: `2026-09-03`

### Операційне визначення

Пред’являючи законні повноваження й підтримуючи достатню прицільну загрозу, гравець наказує одному чи кільком придатним противникам підкоритися, а потім бере одного контрольованого досяжного підозрюваного під живу варту, доки покору не втрачено.

### Включає

Команду Freeze й арешт підкореного підозрюваного у визначеному першому сюжетному епізоді Battlefield Hardline.

### Виключає

Сюжетне затримання в діалозі; залякування нейтрального цивільного; смертельне усунення противника; автоматичний арешт після вичерпання здоров’я.

### Ігри-носії

- [`GAME-0243` — Battlefield Hardline](../games/a-f/battlefield-hardline.md)

## ACT-418

- Назва: Прийняти запропоновану плату за негайне припинення переслідування
- Переглянуто: `2026-09-04`

### Операційне визначення

Під час придатної поточної сутички гравець приймає чинну й посильну пропозицію заплатити за негайне припинення переслідування противником, не втрачаючи накопиченого множника нагороди сесії.

### Включає

Прийняття поліцейського хабаря за низького HEAT у визначеній першій ночі Heat.

### Виключає

Штраф після затримання; купівлю спорядження; сплату постійної винагороди за розшук після сутички; необмежене платне зняття переслідування без чинного вікна пропозиції.

### Ігри-носії

- [`GAME-0244` — "Need for Speed Heat"](../games/m-r/need-for-speed-heat.md)

## ACT-419

- Назва: Виконати підказану ближню дію по приголомшеному ворогу
- Переглянуто: `2026-09-10`

### Операційне визначення

Гравець виконує показану контекстну ближню дію по одному досяжному живому ворогу, доки чинна тимчасова можливість після приголомшення; чи переможе ця дія ціль, визначає системний результат.

### Включає

Glory Kill у DOOM (2016) і DOOM Eternal; наземне добивання у Batman: Arkham Asylum; близькі страти у God of War і Sekiro; показану ближню атаку в Resident Evil 4 (2023 remake).

### Виключає

Звичайний удар ближнього бою; усунення необізнаної цілі; постріл по приголомшеному ворогу здалеку; автоматичний результат без окремої команди гравця; вимогу, щоб ближня дія неодмінно перемагала ціль.

### Ігри-носії

- [`GAME-0255` — "Batman: Arkham Asylum Game of the Year Edition"](../games/a-f/batman-arkham-asylum-game-of-the-year-edition.md)
- [`GAME-0308` — Bloodborne™](../games/a-f/bloodborne.md)
- [`GAME-0245` — DOOM (2016)](../games/a-f/doom-2016.md)
- [`GAME-0286` — DOOM Eternal](../games/a-f/doom-eternal.md)
- [`GAME-0263` — God of War](../games/g-l/god-of-war.md)
- [`GAME-0290` — Lies of P](../games/g-l/lies-of-p.md)
- [`GAME-0323` — "Marvel’s Spider-Man 2"](../games/m-r/marvels-spider-man-2.md)
- [`GAME-0299` — Nioh 2](../games/m-r/nioh-2.md)
- [`GAME-0249` — Resident Evil 4 (2023 remake)](../games/m-r/resident-evil-4-2023.md)
- [`GAME-0288` — "Sekiro™: Shadows Die Twice - GOTY Edition"](../games/s-z/sekiro-shadows-die-twice.md)
- [`GAME-0303` — Sifu](../games/s-z/sifu.md)

## ACT-420

- Назва: Вибрати один посилений режим особистої спроможності під час живого керування
- Переглянуто: `2026-09-04`

### Операційне визначення

Під час безпосереднього керування гравець вибирає один доступний режим із взаємовиключної множини особистих спроможностей, замінюючи чинний режим до наступної сумісної дії руху, захисту або маскування.

### Включає

Вибір Speed, Strength, Armor або Cloak через Classic Nanosuit menu у визначеній першій місії Crysis Remastered.

### Виключає

Вибір переносної зброї; одночасне накладання кількох незалежних перемикачів; безперервний розподіл потужності між одночасними системами транспорту; придбання постійної навички; автоматично запущений пасивний ефект.

### Ігри-носії

- [`GAME-0246` — Crysis Remastered](../games/a-f/crysis-remastered.md)

## ACT-421

- Назва: Націлити й виконати коротке переміщення у світі
- Переглянуто: `2026-09-04`

### Операційне визначення

Під час безпосереднього керування у світі гравець націлює точку в межах обмеженої здатності переміщення й одразу переносить кероване тіло до прийнятої точки, не проходячи кожну проміжну позицію.

### Включає

Прицілювання та виконання Blink I до допустимої точки підлоги, даху чи уступу у визначеній місії Dishonored.

### Виключає

Звичайну безперервну ходьбу чи стрибок; переміщення вибраної фігури на полі; перенесення керування в інше тіло; телепортацію до контрольної точки; перехід у сцені без попереднього показу.

### Ігри-носії

- [`GAME-0247` — Dishonored (2012)](../games/a-f/dishonored-2012.md)

## ACT-422

- Назва: Одягнути здобуте вбрання з рольовою ознакою під час проникнення
- Переглянуто: `2026-09-04`

### Операційне визначення

Після нейтралізації допустимого актора світу гравець забирає й одягає доступне вбрання, замінюючи поточну представлену соціальну роль керованого актора в тій самій живій місії.

### Включає

Забрати й одягнути одне сумісне маскування у визначеній сюжетній місії Paris у HITMAN World of Assassination.

### Виключає

Косметичний гардероб; вибір бойового класу під час появи; обладунок лише для характеристик; вселення в іншого актора; постійну зміну особи поза місією.

### Ігри-носії

- [`GAME-0248` — HITMAN World of Assassination](../games/g-l/hitman-world-of-assassination.md)

## ACT-423

- Назва: Викликати місцевий огляд ситуації під час живого керування
- Переглянуто: `2026-09-04`

### Операційне визначення

Під час безпосереднього керування втіленим актором гравець утримує введення огляду, замінює звичайний вигляд обмеженим показом близьких акторів, цілей та об’єктів, а після відпускання повертається до незміненої живої ролі.

### Включає

Утримувати Instinct для огляду близьких цілей, акторів та інтерактивних об’єктів у визначеній місії Paris.

### Виключає

Постійно позначати актора оптичним пристроєм; призупиняти гру на повній тактичній мапі; вмикати нічне бачення; звертатися до зовнішнього проходження; записувати сканований ресурс у постійні знання.

### Ігри-носії

- [`GAME-0248` — HITMAN World of Assassination](../games/g-l/hitman-world-of-assassination.md)
- [`GAME-0261` — The Last of Us Part I](../games/s-z/the-last-of-us-part-i.md)
- [`GAME-0250` — Tomb Raider (2013)](../games/s-z/tomb-raider-2013.md)

## ACT-424

- Назва: Пересувати й обертати предмети в обмеженій переносній сітці
- Переглянуто: `2026-09-05`

### Операційне визначення

У поданні переносного спорядження гравець вибирає збережений предмет, змінює його позицію або дозволену орієнтацію й підтверджує розміщення лише тоді, коли отриманий контур уміщується у вільних клітинках.

### Включає

Пересування й обертання зброї або припасів у кейсі в межах визначеної першої глави Resident Evil 4.

### Виключає

Розкладання складників у сітці рецепта; вибір незміненого предмета швидкого доступу; пересування об’єкта у світі; сортування необмеженого списку; зміну загальних розмірів спорядження.

### Ігри-носії

- [`GAME-0353` — "Deus Ex: Game of the Year Edition"](../games/a-f/deus-ex-game-of-the-year-edition.md)
- [`GAME-0269` — DREDGE](../games/a-f/dredge.md)
- [`GAME-0249` — Resident Evil 4 (2023 remake)](../games/m-r/resident-evil-4-2023.md)

## ACT-425

- Назва: Вчасно парирувати ближньою зброєю атаку, що надходить
- Переглянуто: `2026-09-05`

### Операційне визначення

Під час живого ближнього бою гравець виконує одну реактивну захисну дію придатною ближньою зброєю, щоб її момент міг протидіяти допустимій атаці, що надходить, замість утримування безперервного блоку.

### Включає

Парирування ножем допустимої атаки в межах визначеної першої глави Resident Evil 4.

### Виключає

Утримування постійного захисту; узгодження спрямованого блоку; покрокову дію захисту; пасивний обладунок; атаку до появи удару, що надходить.

### Ігри-носії

- [`GAME-0282` — Dead Cells](../games/a-f/dead-cells.md)
- [`GAME-0290` — Lies of P](../games/g-l/lies-of-p.md)
- [`GAME-0249` — Resident Evil 4 (2023 remake)](../games/m-r/resident-evil-4-2023.md)
- [`GAME-0288` — "Sekiro™: Shadows Die Twice - GOTY Edition"](../games/s-z/sekiro-shadows-die-twice.md)

## ACT-427

- Назва: Прокручувати фіксовану реконструкцію події до причинного моменту
- Переглянуто: `2026-09-05`

### Операційне визначення

У заданій автором реконструкції вже сталої минулої події гравець переміщує часовий вказівник у межах її скінченного інтервалу й підтверджує огляд у допустимий причинний момент, щоб зареєструвати пов’язаний доказ, не змінюючи представлену подію чи історію живого світу.

### Включає

Прокручування реконструкції тіла або місця події у вступному інциденті Detroit: Become Human для знаходження траєкторії зброї, послідовності нападу чи іншого авторського причинного моменту.

### Виключає

Повернення живої симуляції назад; редагування команд на часовій шкалі; відтворення аудіовізуального доказу без придатного до огляду причинного моменту; вільне вигадування минулого; вибір деталі в одному застиглому tableau.

### Ігри-носії

- [`GAME-0252` — "Detroit: Become Human"](../games/a-f/detroit-become-human.md)

## ACT-428

- Назва: Увійти до пов’язаної союзної бойової платформи для безпосереднього керування
- Переглянуто: `2026-09-05`

### Операційне визначення

Піший оператор входить до однієї доступної відновленої союзної бойової платформи й підтверджує заміну особистих команд руху, атаки та здібностей на безпосереднє керування цією платформою, лишаючись її пасажиром.

### Включає

Вхід до відновленої союзної платформи після операторського з’єднання в обмеженій главі BT-7274 гри Titanfall 2.

### Виключає

Зайняття звичайного водійського місця дорожнього транспорту; зовнішнє командування автономним союзником; вільне перемикання між незалежними постійними тілами; декоративну посадку без передачі керування.

### Ігри-носії

- [`GAME-0253` — "Titanfall 2"](../games/s-z/titanfall-2.md)

## ACT-429

- Назва: Виконати підказану контратаку проти одного ближнього удару
- Переглянуто: `2026-09-05`

### Операційне визначення

У живому ближньому бою гравець виконує одну реактивну контратаку після того, як видима підказка повідомляє про допустимий удар супротивника, щоб перервати або відвести його до контакту, а не тримати постійний захист.

### Включає

Контратаку проти позначеного удару в’язня в обмеженому вступному маршруті Story Mode гри Batman: Arkham Asylum Game of the Year Edition.

### Виключає

Утримування постійного блоку; парирування обов’язковою спорядженою зброєю; атаку до появи ворожого удару; покроковий захист; пасивну броню чи автоматичне ухилення.

### Ігри-носії

- [`GAME-0255` — "Batman: Arkham Asylum Game of the Year Edition"](../games/a-f/batman-arkham-asylum-game-of-the-year-edition.md)
- [`GAME-0299` — Nioh 2](../games/m-r/nioh-2.md)

## ACT-430

- Назва: Переміститися гаком до допустимої висотної точки
- Переглянуто: `2026-09-05`

### Операційне визначення

Під час безпосереднього керування тілом гравець обирає одну наразі допустиму висотну точку світу й підтверджує переміщення гаком від поточної позиції до неї.

### Включає

Переміщення гаком до позначеного верхнього виступу чи спостережної точки в обмеженому вступному маршруті Story Mode гри Batman: Arkham Asylum Game of the Year Edition.

### Виключає

Підтягування віддаленого предмета; захоплення близького ворога; миттєве перенесення без проходження проміжного шляху; встановлення скінченного пристрою для лазіння; сюжетний перехід без обраної точки.

### Ігри-носії

- [`GAME-0255` — "Batman: Arkham Asylum Game of the Year Edition"](../games/a-f/batman-arkham-asylum-game-of-the-year-edition.md)

## ACT-431

- Назва: Перемикати канали готової зброї та активної здібності
- Переглянуто: `2026-09-05`

### Операційне визначення

Під час безпосереднього живого керування гравець перемикає основну команду застосування між поточною вибраною переносною зброєю та поточною вибраною активною особистою здібністю, зберігаючи вибір усередині кожного каналу.

### Включає

Перемикання між поточним Pistol або Wrench і поточним Plasmid Electro Bolt в обмеженому вступному маршруті BioShock™ Remastered.

### Виключає

Вибір іншої зброї всередині запасу; вибір іншого елемента набору здібностей; одночасне застосування зброї та здібності окремими командами; зміну спорядження перед початком.

### Ігри-носії

- [`GAME-0256` — "BioShock™ Remastered"](../games/a-f/bioshock-remastered.md)

## ACT-432

- Назва: Піднімати або опускати переносний детектор місцевого руху
- Переглянуто: `2026-09-05`

### Операційне визначення

Під час безпосереднього керування тілом гравець піднімає переносний детектор руху в активне поле спостереження або знову опускає його, зберігаючи звичайні повноваження руху.

### Включає

Піднімання й опускання детектора руху у визначеній лікарняній місії Alien: Isolation.

### Виключає

Встановлення постійного датчика у світі; позначення одного видимого актора; відкриття всезнаючої мапи; сканування нерухомого ресурсу чи доказу; пасивне попередження без команди детектора.

### Ігри-носії

- [`GAME-0257` — "Alien: Isolation"](../games/a-f/alien-isolation.md)

## ACT-433

- Назва: Входити до авторської схованки або виходити з неї
- Переглянуто: `2026-09-05`

### Операційне визначення

Гравець переводить безпосередньо кероване тіло в одну досяжну авторську позицію маскування, прив’язану до геометрії світу, лишається в цьому обмеженому стані й навмисно виходить, щоб відновити вільний рух.

### Включає

Вхід, очікування й вихід із шафки, шафи або допустимої схованки під меблями у визначеній лікарняній місії Alien: Isolation.

### Виключає

Звичайне присідання за непрозорою перешкодою; прив’язування до бойового укриття; невидимість від активної здібності; сюжетну сцену ховання; маскування лише автономного актора.

### Ігри-носії

- [`GAME-0257` — "Alien: Isolation"](../games/a-f/alien-isolation.md)

## ACT-434

- Назва: Переорієнтовувати лінійний рисунок пострілу готового інструмента
- Переглянуто: `2026-09-05`

### Операційне визначення

Поки один сумісний інструмент лишається готовим, гравець повертає або перемикає його видовжений рисунок пострілу між визначеними просторовими орієнтаціями перед наступним прицільним пострілом.

### Включає

Перемикання трьох променів Plasma Cutter між горизонтальною та вертикальною орієнтаціями в обмеженому вступному розділі Dead Space (2023).

### Виключає

Повертання предмета в інвентарі; поворот керованого тіла чи камери; зміну типу боєприпасів; вибір іншої зброї; випадкову віддачу після пострілу.

### Ігри-носії

- [`GAME-0259` — "Dead Space (2023 remake)"](../games/a-f/dead-space-2023.md)

## ACT-435

- Назва: Замінити скінченний фільтр в особистому дихальному спорядженні
- Переглянуто: `2026-09-05`

### Операційне визначення

Поки сумісне особисте дихальне спорядження доступне у визначеному стані заміни, гравець виконує обмін фільтра: відкидає поточний картридж і переносить один сумісний картридж із власного запасу до спорядження, відновлюючи тривалість придатного захисту без зміни навколишнього повітря.

### Включає

Заміну фільтра протигаза в обмеженому розділі Moscow гри Metro Exodus.

### Виключає

Надягання або знімання всього протигаза; наповнення кисневого балона; полагодження пошкодженого скла; уживання ліків; виготовлення нового картриджа; автоматичну зміну фільтра без команди гравця.

### Ігри-носії

- [`GAME-0260` — Metro Exodus](../games/m-r/metro-exodus.md)

## ACT-436

- Назва: Виконати ухильний перекид за рахунок спільного запасу
- Переглянуто: `2026-09-05`

### Операційне визначення

Зі звичайного живого руху гравець виконує одне спрямоване ухильне переміщення, ціну якого беруть зі спільного вичерпного запасу зусиль, а не з окремого часу відновлення дії, і приймає визначений проміжок відновлення після нього.

### Включає

Спрямований перекид, яким перетинають ворожий удар у дослідженому маршруті Cemetery of Ash гри DARK SOULS III.

### Виключає

Звичайне переміщення рельєфом; ухилення, ціна якого — лише власний час відновлення чи скидання стану; блок або парирування; стрибок, що лише змінює висоту; автоматичне сюжетне ухилення.

### Ігри-носії

- [`GAME-0308` — Bloodborne™](../games/a-f/bloodborne.md)
- [`GAME-0262` — DARK SOULS™ III](../games/a-f/dark-souls-iii.md)
- [`GAME-0295` — DARK SOULS™: REMASTERED](../games/a-f/dark-souls-remastered.md)
- [`GAME-0290` — Lies of P](../games/g-l/lies-of-p.md)
- [`GAME-0299` — Nioh 2](../games/m-r/nioh-2.md)

## ACT-437

- Назва: Утримувати й відпускати ненаправлений захист у бік погляду
- Переглянуто: `2026-09-06`

### Операційне визначення

Під час живого бою гравець піднімає й утримує вдягнене захисне спорядження в бік поточного повороту персонажа, щоб допустимі зустрічні атаки послаблювались або поглинались замість того, щоб повністю лягати на здоров’я, і відпускає його, щоб повернутися до звичайних дій; сама команда не володіє тим, чи і як саме те поглинання оплачується.

### Включає

Утримування щита проти ударів Grave Warden і стражів у дослідженому маршруті Cemetery of Ash гри DARK SOULS III; утримування щита Guardian Shield у дослідженому початковому маршруті God of War.

### Виключає

Наведення захисту в бік однієї вибраної атаки; захист бійцівської гри вгору чи вниз, який запитують напрямком руху; тривалий захист зброєю, власна шкала якого може вичерпатися до відкритого стану; вікно вчасного парирування чи відбиття; тимчасовий запас поглинання перед здоров’ям; сталий захист обладунка, що не потребує утримування.

### Ігри-носії

- [`GAME-0347` — "Castlevania: Symphony of the Night"](../games/a-f/castlevania-symphony-of-the-night.md)
- [`GAME-0262` — DARK SOULS™ III](../games/a-f/dark-souls-iii.md)
- [`GAME-0295` — DARK SOULS™: REMASTERED](../games/a-f/dark-souls-remastered.md)
- [`GAME-0282` — Dead Cells](../games/a-f/dead-cells.md)
- [`GAME-0327` — Fable](../games/a-f/fable.md)
- [`GAME-0263` — God of War](../games/g-l/god-of-war.md)
- [`GAME-0290` — Lies of P](../games/g-l/lies-of-p.md)
- [`GAME-0341` — "Ninja Gaiden Black"](../games/m-r/ninja-gaiden-black.md)
- [`GAME-0299` — Nioh 2](../games/m-r/nioh-2.md)
- [`GAME-0344` — "Prince of Persia: The Sands of Time"](../games/m-r/prince-of-persia-the-sands-of-time.md)
- [`GAME-0363` — "The Legend of Zelda: Ocarina of Time"](../games/s-z/the-legend-of-zelda-ocarina-of-time.md)

## ACT-438

- Назва: Прив’язати огляд і поворот атак до однієї обраної цілі
- Переглянуто: `2026-09-05`

### Операційне визначення

Гравець обирає одну поточно допустиму сусідню ворожу ціль і прив’язує до неї камеру та напрямок атак персонажа, тож подальший рух стає відносним до цього актора, доки гравець не зніме прив’язку або ціль не втратить допустимість.

### Включає

Прив’язку до Grave Warden або до стража маршруту в дослідженому маршруті DARK SOULS III.

### Виключає

Збережену тактичну позначку, що переживає перешкоди чи сутичку; автоматичну допомогу з наведенням, яку гравець не обирає; вибір абстрактної картки чи пункту меню; наказ іншому актору атакувати ціль.

### Ігри-носії

- [`GAME-0308` — Bloodborne™](../games/a-f/bloodborne.md)
- [`GAME-0262` — DARK SOULS™ III](../games/a-f/dark-souls-iii.md)
- [`GAME-0295` — DARK SOULS™: REMASTERED](../games/a-f/dark-souls-remastered.md)
- [`GAME-0327` — Fable](../games/a-f/fable.md)
- [`GAME-0290` — Lies of P](../games/g-l/lies-of-p.md)
- [`GAME-0299` — Nioh 2](../games/m-r/nioh-2.md)
- [`GAME-0288` — "Sekiro™: Shadows Die Twice - GOTY Edition"](../games/s-z/sekiro-shadows-die-twice.md)

## ACT-440

- Назва: Прийняти перевірку здібності з показаними шансами
- Переглянуто: `2026-09-05`

### Операційне визначення

Гравець вибирає запропонований варіант із перевіркою здібності, читає показані шанси на успіх і доданки, що їх утворюють, і підтверджує його, знаючи, що результат вирішить випадковий розрахунок, а не якість виконання команди.

### Включає

Підтвердження активної білої або червоної перевірки на репліці чи предметі в дослідженому початковому епізоді Disco Elysium - The Final Cut.

### Виключає

Звичайну авторську відповідь із наперед визначеним наслідком; вчасне натискання, успіх якого залежить від миті; здібність, обмежену лише ресурсом чи часом відновлення; приховану перевірку, яку гравець не обирає.

### Ігри-носії

- [`GAME-0264` — Disco Elysium - The Final Cut](../games/a-f/disco-elysium-the-final-cut.md)

## ACT-441

- Назва: Поставити платного постійного захисника на відомий маршрут
- Переглянуто: `2026-09-06`

### Операційне визначення

Гравець вибирає один тип із платного каталогу й ставить його на обрану допустиму позицію на мапі, де маршрут ворогів незмінний і відомий заздалегідь, тож обрана позиція визначає, яку ділянку цього маршруту новий постійний захисник зможе опрацьовувати до кінця спроби.

### Включає

Розміщення купленої мавпи на суходолі початкової мапи в дослідженому легкому стандартному маршруті Bloons TD 6.

### Виключає

Розміщення споруди, чия позиція змінює покриття міських послуг; розміщення чи поворот об’єкта в робочому виробничому плануванні; купівлю активу без вибору позиції у світі; висадку загону, який потім рухається або отримує прямі накази.

### Ігри-носії

- [`GAME-0265` — Bloons TD 6](../games/a-f/bloons-td-6.md)

## ACT-442

- Назва: Задати поставленому захисникові правило вибору цілі
- Переглянуто: `2026-09-06`

### Операційне визначення

Для одного вже поставленого автономного захисника гравець вибирає серед оголошених правил те, яке вирішуватиме, кого з допустимих ворогів у межах досяжності він атакуватиме наступним, змінюючи майбутні автоматичні вибори цього захисника й не наказуючи жодної окремої сутички.

### Включає

Перемикання поставленої мавпи між оголошеними правилами «перший», «останній», «найближчий» і «найсильніший» у дослідженому маршруті Bloons TD 6.

### Виключає

Призначення шикування та бойової постави загону під прямим керуванням; вибір здібності та її цілі; наведення удару; поставу, що змінює, рухається актор чи тримає позицію.

### Ігри-носії

- [`GAME-0265` — Bloons TD 6](../games/a-f/bloons-td-6.md)

## ACT-443

- Назва: Прорізати породу й забрати вміщений у ній видобуток
- Переглянуто: `2026-09-06`

### Операційне визначення

Гравець наводить різальний інструмент на досяжну тверду породу й усуває її суцільний об’єм, назавжди відкриваючи цей об’єм як прохідний простір; якщо в усунутому об’ємі було родовище, та сама дія переносить його заявлений матеріал до перенесеного запасу.

### Включає

Удари спільним кайлом або свердлами класу Driller крізь печерну породу й крізь родовища мінералів у дослідженій одиночній експедиції Deep Rock Galactic.

### Виключає

Руйнування однієї окремої комірки, брили чи стіни світу; усунення обмеженого об’єму ґрунту лише заради заглиблення чи укриття; утримування команди видобутку на окремому ресурсному об’єкті, який не є породою; збирання з польового джерела чи з переможеного тіла; руйнування породи винятково заради появи окремої здобичі.

### Ігри-носії

- [`GAME-0266` — Deep Rock Galactic](../games/a-f/deep-rock-galactic.md)

## ACT-444

- Назва: Розподілити частини по впорядкованому списку запусків і просувати його
- Переглянуто: `2026-09-06`

### Операційне визначення

Під час складання гравець розподіляє частини побудованого апарата по впорядкованому списку кроків запуску й може вільно міняти порядок цього списку; під час роботи одна повторювана команда просуває список рівно на один крок, безповоротно запалюючи або відділяючи кожну частину цього кроку.

### Включає

Укладання списку запусків у складальному ангарі та його просування по одному кроку в польоті в дослідженому завданні Sandbox гри Kerbal Space Program.

### Виключає

Розміщення чи орієнтування складника; редагування місцевого правила роботи окремого об’єкта або просторового поля команд; вибір однієї здібності та її цілі; час відновлення, що повертає використану дію; активацію, яку система виконує за власним розкладом.

### Ігри-носії

- [`GAME-0267` — Kerbal Space Program](../games/g-l/kerbal-space-program.md)

## ACT-445

- Назва: Вести підвладну фішку обмеженим полем, уникаючи чужих фігур
- Переглянуто: `2026-09-06`

### Операційне визначення

Поки діє супротивник, гравець безперервно веде одну малу підвладну фішку обмеженим полем, яке вона не може покинути, так щоб фішка уникала дотику до фігур, що супротивник випускає в те саме поле; це ведення є єдиним захисним введенням, і жодного удару, блоку чи вчасної відповіді при цьому не пропонують.

### Включає

Рух фішки-серця всередині замкненої рамки, поки її перетинають снаряди чудовиська, у дослідженому початковому маршруті Undertale.

### Виключає

Одне вчасне ухилення, парирування чи стрибок у вибрану мить; захищений проміжок, куплений зі спільного запасу; утримування блоку; проведення сталого персонажа геометрією рівня; наведення зброї на нападника.

### Ігри-носії

- [`GAME-0268` — Undertale](../games/s-z/undertale.md)

## ACT-446

- Назва: Спрямувати безперервний струмінь на досяжну поверхню
- Переглянуто: `2026-09-08`

### Операційне визначення

Гравець наводить наявний безперервний робочий інструмент на досяжну поверхню й утримує або перемикає його вихід, тож наслідком дії є площа, яку струмінь укриває з часом, а не окремий завершений удар.

### Включає

Ведення мийного струменя по панелях автомобіля в дослідженому першому завданні кар’єри PowerWash Simulator.

### Виключає

Прицільний постріл або удар по ворогові; вилучення скінченної здобичі з джерела; окрему дію догляду за одним власним предметом; встановлення постійного об’єкта; знаряддя, дія якого спрацьовує на відпусканні, а не під час дотику.

### Ігри-носії

- [`GAME-0296` — Noita](../games/m-r/noita.md)
- [`GAME-0279` — PowerWash Simulator](../games/m-r/powerwash-simulator.md)

## ACT-447

- Назва: Скласти обмежене меню обслуговування з доступних порцій рецептів
- Переглянуто: `2026-09-08`

### Операційне визначення

До або під час обмеженої сесії обслуговування гравець вибирає доступний рецепт і додає його з вибраною або визначеною правилами кількістю порцій до меню сесії, після чого нові замовлення можуть його обрати, а складники опиняються під загрозою витрати чи втрати наприкінці сесії.

### Включає

Додавання відкритої страви до меню першого вечора в DAVE THE DIVER з кількістю порцій, яку забезпечує риба з обов’язкового другого занурення.

### Виключає

Виготовлення одного особистого предмета інвентарю; призначення безперервного рецепта автоматичній фабриці; купівлю пропозиції каталогу; доставку готової порції одержувачу; саме лише читання рецепта.

### Ігри-носії

- [`GAME-0278` — DAVE THE DIVER](../games/a-f/dave-the-diver.md)

## ACT-448

- Назва: Утримувати й відпустити дозатор біля цільового рівня наповнення
- Переглянуто: `2026-09-08`

### Операційне визначення

Гравець утримує команду безперервної подачі, поки видима посудина наповнюється, а потім відпускає її у вибрану мить, щоб досягнутий рівень оцінили відносно оголошеної цілі замість автоматичної зупинки на ній.

### Включає

Наливання обов’язкового раннього напою в навчанні першого обслуговування DAVE THE DIVER, де рівень під час відпускання змінює оцінку відвідувача й оплату.

### Виключає

Перенесення найбільшої сумісної кількості між двома вибраними місткостями; утримування безперервного апарата над поверхнею; один вчасний удар у рухоме вікно; вибір фіксованої кількості в меню.

### Ігри-носії

- [`GAME-0278` — DAVE THE DIVER](../games/a-f/dave-the-diver.md)

## ACT-449

- Назва: Вручну знизити спільну шкалу світла загону
- Переглянуто: `2026-09-08`

### Операційне визначення

Гравець безпосередньо знижує спільну шкалу світла експедиції на оголошений крок або до нуля в будь-який момент поза розрахунком дії і так змінює пороговий діапазон шкали перед подальшим рухом, боєм і розподілом здобичі.

### Включає

Гасіння смолоскипа в Darkest Dungeon кроками по 25 пунктів або повністю через саму шкалу світла протягом визначеного навчального маршруту Old Road, де маршрут це радить, але ніколи не наказує.

### Виключає

Автоматичний спад світла від руху (SYS-829); підвищення шкали витратою предмета світла з інвентарю, якого у визначеному пакеті не засвідчено, тож воно лишається поза цією межею; навичку, побічний ефект якої змінює світло; перемикання особистого джерела освітлення, що створює локальне поле світла (ACT-409); вживання відновлювального предмета.

### Ігри-носії

- [`GAME-0281` — Darkest Dungeon](../games/a-f/darkest-dungeon.md)

## ACT-450

- Назва: Пересунути одного героя строєм загону ціною його ходу
- Переглянуто: `2026-09-08`

### Операційне визначення

Під час бойового ходу героя гравець наказує йому пересунутися на оголошену кількість позицій уперед або назад уздовж одновимірного строю загону, міняючись місцями із союзниками, яких він проминає, і цей наказ витрачає дію героя на цей раунд.

### Включає

Команду переміщення в Darkest Dungeon із дальністю руху кожного героя вперед і назад, якою Dismas або Reynauld повертають у ряд, з якого їхні споряджені навички допустимі після відкидання, протягом визначеного навчального маршруту Old Road.

### Виключає

Переміщення як побічний ефект навички або ворожого ефекту переміщення; вільну зміну строю поза боєм; переміщення юніта двовимірною сіткою (ACT-014); обмін місцями через крок у сусідній юніт (ACT-067).

### Ігри-носії

- [`GAME-0281` — Darkest Dungeon](../games/a-f/darkest-dungeon.md)

## ACT-451

- Назва: Вкласти наявну валюту в один обраний платний запис реєстру
- Переглянуто: `2026-09-08`

### Операційне визначення

Гравець обирає один доступний платний запис у постійному реєстрі й вкладає в його ціну наявну валюту проходження — до розміру балансу або залишку ціни, — причому запис не мусить бути посильним чи здобутим унаслідок цього вкладення.

### Включає

Вкладення клітин у доступний запис Collector, починаючи з Health Flask I, у Passage після визначеного першого проходження Prisoners' Quarters у Dead Cells, незалежно від того, чи покриває вкладення ціну повністю, чи лишає її сплаченою частково.

### Виключає

Купівлю, що одразу дає запропоноване (ACT-130); купівлю між проходженнями за постійні ресурси (ACT-143); внесок типізованого предмета до комірки колекції (ACT-093); заставу, яку можна повернути; збереження й завершення запису в реєстрі (SYS-835).

### Ігри-носії

- [`GAME-0282` — Dead Cells](../games/a-f/dead-cells.md)

## ACT-452

- Назва: Витратити готовий заряд і повернути керування після смертельної поразки
- Переглянуто: `2026-09-10`

### Операційне визначення

Після смертельної шкоди, але до остаточного завершення смерті, гравець підтверджує витрату готового заряду самовідновлення, повертає кероване тіло на тому самому місці й продовжує ту саму живу сутичку.

### Включає

Вибір Resurrection після смертельної поразки в обмеженому початковому маршруті Sekiro.

### Виключає

Оживлення іншого учасника; автоматичне додаткове життя; повернення до контрольної точки; поява нового тіла; пасивне виживання без команди після поразки.

### Ігри-носії

- [`GAME-0288` — "Sekiro™: Shadows Die Twice - GOTY Edition"](../games/s-z/sekiro-shadows-die-twice.md)

## ACT-453

- Назва: Витратити одну одиницю переносного запасу на поповнення пристрою
- Переглянуто: `2026-09-10`

### Операційне визначення

Коли сумісному переносному пристрою бракує заряду до придатної межі, гравець окремою командою безповоротно переносить до нього одну сумісну одиницю зі скінченного запасу, не обираючи іншого спорядженого засобу.

### Включає

Ручне витрачання однієї переносної батарейки на поповнення ліхтарика у визначеній лікарняній місії Alien: Isolation.

### Виключає

Перемикання пристрою (ACT-409); автоматичне відновлення заряду в неактивному стані; перезарядження магазинної зброї (ACT-183); заміну дихального фільтра (ACT-435); підбирання змінної одиниці; виготовлення чи спорядження іншого пристрою.

### Ігри-носії

- [`GAME-0257` — "Alien: Isolation"](../games/a-f/alien-isolation.md)

## ACT-454

- Назва: Живитися кров’ю ослабленої цілі
- Переглянуто: `2026-09-13`

### Операційне визначення

Гравець спрямовує команду на близьку ослаблену живу ціль і утримує живлення до завершення або застосовує дозволений ранній укус, щоб забрати її кров.

### Включає

Feed і завершальний Bite по придатній людині чи істоті на початку V Rising.

### Виключає

Звичайний удар; споживання переносного предмета; підбирання Blood Essence; автоматичне викрадення здоров’я; взаємодію з трупом.

### Ігри-носії

- [`GAME-0294` — V Rising](../games/s-z/v-rising.md)

## ACT-455

- Назва: Редагувати мережу гостьових і службових стежок
- Переглянуто: `2026-09-18`

### Операційне визначення

Гравець прокладає, подовжує або прибирає з'єднані ділянки пішохідних стежок; їхня розгалужена мережа визначає, куди можуть самостійно дістатися відвідувачі та працівники.

### Включає

З'єднання воріт вольєра страусів з наявною стежкою в Goodwin House гри Planet Zoo: Console Edition.

### Виключає

Мережу автомобільних доріг (ACT-068); один нерозгалужений маршрут головоломки; декоративне фарбування землі; пряме керування відвідувачем або доглядачем.

### Ігри-носії

- [`GAME-0298` — 'Planet Zoo: Console Edition'](../games/m-r/planet-zoo-console-edition.md)
- [`GAME-0335` — RollerCoaster Tycoon Deluxe](../games/m-r/rollercoaster-tycoon-deluxe.md)

## ACT-456

- Назва: Побудувати замкнену огорожу вольєра та його ворота
- Переглянуто: `2026-09-18`

### Операційне визначення

Гравець розміщує або змінює суміжні секції огорожі й одні службові ворота, утворюючи окремий вольєр для тварин, межа та вхід якого залишаються частиною чинного стану зоопарку.

### Включає

Завершення огорожі, воріт і скляної оглядової секції вольєра страусів у Goodwin House.

### Виключає

Звичайну стіну без функції утримання тварин; стежку поза вольєром (ACT-455); автоматичну перевірку придатності (CON-635); розміщення годівниць та оглядових об'єктів (ACT-457).

### Ігри-носії

- [`GAME-0298` — 'Planet Zoo: Console Edition'](../games/m-r/planet-zoo-console-edition.md)

## ACT-457

- Назва: Розмістити окремий об'єкт догляду чи огляду
- Переглянуто: `2026-09-18`

### Операційне визначення

Гравець ставить вибраний окремий об'єкт у допустимому місці зоопарку, додаючи його визначену функцію догляду до вольєра або функцію для відвідувачів до прилеглої оглядової ділянки.

### Включає

Годівниці, поїлки, ігрове чи харчове збагачення та скриньку для пожертв біля огляду страусів у Goodwin House.

### Виключає

Побудову огорожі (ACT-456); редагування стежки (ACT-455); звичайну виробничу будівлю (ACT-139); фактичне годування тварини працівником.

### Ігри-носії

- [`GAME-0298` — 'Planet Zoo: Console Edition'](../games/m-r/planet-zoo-console-edition.md)

## ACT-458

- Назва: Призначити тварині зі сховища придатний вольєр
- Переглянуто: `2026-09-18`

### Операційне визначення

Гравець вибирає тварину, що вже перебуває у сховищі зоопарку, і замовляє її перевезення до одного вибраного придатного вольєра; саме переміщення виконують доступні працівники.

### Включає

Призначення придбаних бородавочників і страусів із торгового центру до відповідних вольєрів Goodwin House.

### Виключає

Придбання тварини (ACT-130); власноручне перенесення зоопарком; автономне перевезення працівником (SYS-866); удаване успішне призначення непридатного вольєра.

### Ігри-носії

- [`GAME-0298` — 'Planet Zoo: Console Edition'](../games/m-r/planet-zoo-console-edition.md)

## ACT-459

- Назва: Обирати бойову стійку зі зброєю
- Переглянуто: `2026-09-18`

### Операційне визначення

Під час безпосереднього керування боєм гравець перемикає споряджену ближню зброю між передбаченими стійками, одразу обираючи інший набір швидкості, досяжності й тривалості наступних ударів.

### Включає

Вибір високої, середньої чи низької стійки в першій місії Nioh 2 для PS4.

### Виключає

Зміну самої зброї; призначення бойового шикування автономним підрозділам; одноразове парирування; стійку, вибрану лише перед боєм.

### Ігри-носії

- [`GAME-0308` — Bloodborne™](../games/a-f/bloodborne.md)
- [`GAME-0299` — Nioh 2](../games/m-r/nioh-2.md)

## ACT-460

- Назва: Вчасно повернути витрачену силу після удару
- Переглянуто: `2026-09-18`

### Операційне визначення

Після придатного удару гравець виконує імпульс у короткому видимому проміжку відновлення, повертаючи доступну частину щойно витраченого запасу сили та застосовуючи передбачене локальне очищення.

### Включає

Вчасний Ki Pulse після удару зброєю та очищення сусідньої плями світу йокаїв у першій місії Nioh 2.

### Виключає

Пасивне відновлення з часом; поповнення витратним предметом; імпульс без попереднього придатного удару; захист щитом або відповідь на небезпечну атаку.

### Ігри-носії

- [`GAME-0299` — Nioh 2](../games/m-r/nioh-2.md)

## ACT-461

- Назва: Подати готову тарілку через вікно видачі
- Переглянуто: `2026-09-18`

### Операційне визначення

Гравець підносить завершену страву на тарілці до спільного вікна видачі й передає її для звірення з поточними замовленнями; після подачі кухар уже не тримає тарілку.

### Включає

Подачу тарілки із сашимі з нарізаної риби або креветки через вікно видачі першої кухні Overcooked! 2.

### Виключає

Передачу предмета конкретному персонажеві (ACT-091); саме викладання їжі на тарілку; автоматичне виконання замовлення без подачі; сирий інгредієнт замість страви.

### Ігри-носії

- [`GAME-0300` — Overcooked! 2](../games/m-r/overcooked-2.md)

## ACT-462

- Назва: Націлити й виконати прийом за заряд Focus
- Переглянуто: `2026-09-18`

### Операційне визначення

Коли бойовий заряд готовий, гравець у сповільненому виборі вказує вразливу точку доступного супротивника й підтверджує особливий ближній прийом, який витрачає заряд.

### Включає

Вибір цілі та витрату Focus на прийом у першому сховку Sifu на складності Disciple.

### Виключає

Звичайний удар; автоматичну зміну цілі; прийом Focus, прив’язаний до конкретної зброї; здібність тільки з таймером відновлення; прийом без окремого прицільного вибору.

### Ігри-носії

- [`GAME-0303` — Sifu](../games/s-z/sifu.md)

## ACT-463

- Назва: Підтвердити повернення талісманом після смерті
- Переглянуто: `2026-09-18`

### Операційне визначення

У проміжку вибору після смертельного удару гравець підтверджує негайне продовження з придатним талісманом замість завершення поточної спроби.

### Включає

Підйом після смерті в першому сховку Sifu, коли талісман іще може повернути героя.

### Виключає

Автоматичне відродження на контрольній точці; заряджене воскресіння в Sekiro; допомогу напарника; вибір навички на тому самому екрані; автоматичне збільшення віку після підтвердження.

### Ігри-носії

- [`GAME-0303` — Sifu](../games/s-z/sifu.md)

## ACT-464

- Назва: Взяти всі плитки одного кольору з одного джерела
- Переглянуто: `2026-09-18`

### Операційне визначення

У свій хід гравець обирає одне видиме джерело та колір і мусить забрати з нього всі плитки цього кольору, а не довільну кількість.

### Включає

Вибір однієї з п’яти майстерень або спільного центру в партії Azul на двох.

### Виключає

Невидимий набір із мішка; різні кольори за один вибір; залишення плитки вибраного кольору; розміщення партії на підготовчому рядку.

### Ігри-носії

- [`GAME-0304` — Azul](../games/a-f/azul.md)

## ACT-465

- Назва: Призначити набраний колір одному підготовчому рядку
- Переглянуто: `2026-09-18`

### Операційне визначення

Після набору гравець обирає один придатний підготовчий рядок для всіх прийнятих плиток цього кольору; відхилені та зайві плитки йдуть на штрафну лінію, а не розподіляються між рядками.

### Включає

Заповнення одного рядка Azul справа наліво або свідоме скидання партії на підлогу.

### Виключає

Вибір спільного джерела; автоматичне перенесення завершеного рядка на стіну; заповнення двох рядків однією партією.

### Ігри-носії

- [`GAME-0304` — Azul](../games/a-f/azul.md)

## ACT-466

- Назва: Перенести живу ціль місії до евакуаційного транспорту
- Переглянуто: `2026-09-18`

### Операційне визначення

Гравець піднімає допустиму непритомну або поранену живу ціль місії, фізично несе її світом в окремому стані перенесення й розміщує у відповідному евакуаційному транспорті, перш ніж власний від’їзд завершить порятунок.

### Включає

Винести пораненого Казухіру Міллера з Da Ghwandai Khar і посадити його в другий вертоліт під час першої спроби Phantom Limbs у METAL GEAR SOLID V: THE PHANTOM PAIN.

### Виключає

Ховати тіло знешкодженого ворога; наказувати самостійним носіям доставити людину; користуватися Fulton; нести чи кидати сумку зі здобиччю; самому сідати у вертоліт після посадки врятованого.

### Ігри-носії

- [`GAME-0306` — METAL GEAR SOLID V: THE PHANTOM PAIN](../games/m-r/metal-gear-solid-v-the-phantom-pain.md)

## ACT-467

- Назва: Всмоктувати або вистрілювати досяжний об’єкт через активний бак
- Переглянуто: `2026-09-19`

### Операційне визначення

Гравець прицілює переносний вакуумний інструмент і або затягує сумісну досяжну рухому сутність зі світу до вибраного типізованого бака, або вистрілює запасені одиниці з цього бака назад у вибрану ділянку світу чи приймальний пристрій.

### Включає

Всмоктувати Pink Slime, їжу та Pink Plort у вибраний бак Vacpack, а потім запускати слаймів чи їжу в стартовий загін і plort’и в Plort Market у новому збереженні Adventure.

### Виключає

Контактне підбирання без прицільного всмоктування; вибір бака; продаж випущеного plort’а; автоматичне поїдання їжі або створення plort’а; переміщення нерухомого об’єкта середовища.

### Ігри-носії

- [`GAME-0307` — Slime Rancher](../games/s-z/slime-rancher.md)

## ACT-468

- Назва: Утримувати й відпустити заряджений дрифт машини
- Переглянуто: `2026-09-19`

### Операційне визначення

Безпосередньо керуючи машиною в повороті, гравець утримує дрифт, який продовжує змінювати поточну траєкторію, а після появи видимого рівня заряду сам обирає мить відпускання.

### Включає

Утримувати дрифт Mario Kart 8 Deluxe в повороті й відпустити його на рівні іскор Mini-Turbo, Super Mini-Turbo або Ultra Mini-Turbo за вимкненого Smart Steering.

### Виключає

Витрачання запасу прискорення, який можна зберігати після маневру; оцінювання тривалості дрифту; допоміжне кермування з окремою підказкою дрифту; звичайний розворот ручним гальмом без заряду й виплати.

### Ігри-носії

- [`GAME-0309` — "Mario Kart 8 Deluxe"](../games/m-r/mario-kart-8-deluxe.md)

## ACT-469

- Назва: Перерозподіляти вантаж між місцями на тілі
- Переглянуто: `2026-09-19`

### Операційне визначення

Гравець переносить пакунки між сумісними місцями на тілі, костюмі чи наплічнику або запускає автоматичне впорядкування, щоб змінити розподіл поточного вантажу без зміни призначення пакунків.

### Включає

Ручне й автоматичне впорядкування вантажу в першому замовленні DEATH STRANDING DIRECTOR'S CUT.

### Виключає

Підбирання вантажу зі світу (`ACT-199`); зберігання у транспорті; скидання всього вантажу; косметичне оформлення наплічника.

### Ігри-носії

- [`GAME-0310` — "DEATH STRANDING DIRECTOR’S CUT"](../games/a-f/death-stranding-directors-cut.md)

## ACT-470

- Назва: Стабілізувати бік зміщеного вантажу
- Переглянуто: `2026-09-19`

### Операційне визначення

Під час руху з вантажем на тілі гравець утримує ліве, праве або обидва визначені захоплення, щоб протидіяти поточному боковому зміщенню й стабілізувати носія до розв’язання рівноваги.

### Включає

Стабілізацію одного або двох боків у першій доставці DEATH STRANDING DIRECTOR'S CUT.

### Виключає

Пасивну стійкість спорядження; блокування бойової атаки; керування транспортом; автоматичне виправлення без команди гравця.

### Ігри-носії

- [`GAME-0310` — "DEATH STRANDING DIRECTOR’S CUT"](../games/a-f/death-stranding-directors-cut.md)

## ACT-471

- Назва: Випускати локальний імпульс огляду рельєфу й вантажу
- Переглянуто: `2026-09-19`

### Операційне визначення

Гравець запускає обмежений локальний сенсорний імпульс, який класифікує ризик сусідньої прохідної місцевості й позначає допустимий вантаж, не обираючи пункт призначення й не розв’язуючи маршрут.

### Включає

Скан Odradek у першому замовленні DEATH STRANDING DIRECTOR'S CUT.

### Виключає

Імпульс лише для ресурсів; постійне відкриття всієї мапи; автоматичне виявлення ворогів; обчислення маршруту.

### Ігри-носії

- [`GAME-0310` — "DEATH STRANDING DIRECTOR’S CUT"](../games/a-f/death-stranding-directors-cut.md)

## ACT-472

- Назва: З’єднувати топографічні позначки у запланований маршрут
- Переглянуто: `2026-09-19`

### Операційне визначення

Гравець ставить, упорядковує, редагує або видаляє позначки мапи, послідовні позиції яких утворюють видиму заплановану лінію через топографічний рельєф без команди автоматичного проходження.

### Включає

З’єднані позначки маршруту в першій доставці DEATH STRANDING DIRECTOR'S CUT.

### Виключає

Одну ціль із автоматично прокладеною дорогою; малювання рельєфу; команди автономному підрозділу.

### Ігри-носії

- [`GAME-0310` — "DEATH STRANDING DIRECTOR’S CUT"](../games/a-f/death-stranding-directors-cut.md)

## ACT-473

- Назва: Надувати кероване тіло для вертикального підйому
- Переглянуто: `2026-09-19`

### Операційне визначення

Поки доступна оголошена тимчасова здатність до надування, гравець утримує її окрему команду, щоб збільшити безпосередньо кероване тіло й спрямувати плавучий підйом до досяжного простору в повітрі або водному маршруті.

### Включає

Утримання Inflate у Sky Garden гри ASTRO BOT для підйому до фрагмента пазла біля фламінго, платформ вежі та верхньої частини водної труби.

### Виключає

Звичайний стрибок або скінченне лазерне зависання; пасивну плавучість повітряної кулі; плавання без тимчасової форми; вибір далекої цілі для автоматичного польоту.

### Ігри-носії

- [`GAME-0312` — ASTRO BOT](../games/a-f/astro-bot.md)

## ACT-474

- Назва: Керувати одним досяжним постом судна
- Переглянуто: `2026-09-20`

### Операційне визначення

Гравець фізично дістається одного поста керування судном і змінює збережене налаштування цього поста, тоді як решта постів і саме судно лишаються у своєму поточному живому стані.

### Включає

Поворот керма Sloop, піднімання чи опускання якоря шпилем і зміна довжини або кута вітрила в навчальній подорожі Gold Hoarders гри Sea of Thieves.

### Виключає

Вибір віддаленого місця для автоматичної подорожі; керування транспортом з одного спільного місця; наказ автономному судну; косметичне вітрило.

### Ігри-носії

- [`GAME-0319` — Sea of Thieves](../games/s-z/sea-of-thieves.md)

## ACT-475

- Назва: Копати в одній обраній точці місцевості
- Переглянуто: `2026-09-20`

### Операційне визначення

Гравець наводить знаряддя копання на одну обрану досяжну точку поверхні й проводить удар, щоб світ перевірив і, за сумісності, просунув стан похованого предмета в цьому місці.

### Включає

Удари лопатою навколо позначеного місця єдиної закопаної Sailor’s Chest у навчальній подорожі Gold Hoarders гри Sea of Thieves.

### Виключає

Видалення місцевості для укриття; добування видимого ресурсу; відкривання вже знайденого контейнера; автоматичне копання за мапною позначкою.

### Ігри-носії

- [`GAME-0319` — Sea of Thieves](../games/s-z/sea-of-thieves.md)

## ACT-476

- Назва: Закинути вудку й підсікти після сигналу клювання
- Переглянуто: `2026-09-20`

### Операційне визначення

Гравець наводить і закидає вудку в досяжну воду біля однієї видимої придатної цілі, перечікує проміжні торкання й проводить підсікання лише після оголошеного сигналу клювання.

### Включає

Закидання flimsy fishing rod біля тіні риби та підсікання після занурення поплавця в Animal Crossing: New Horizons.

### Виключає

Безпосереднє хапання вільно плаваючої істоти; автоматичну риболовлю; мінігру після вже прийнятого гачка; ловлю комахи сачком.

### Ігри-носії

- [`GAME-0320` — "Animal Crossing: New Horizons"](../games/a-f/animal-crossing-new-horizons.md)

## ACT-477

- Назва: Змахнути сачком крізь досяжну комаху
- Переглянуто: `2026-09-20`

### Операційне визначення

Гравець розташовує безпосередньо керованого персонажа й проводить один короткий замах сачком крізь обраний досяжний об’єм світу, перевіряючи контакт із присутньою комахою.

### Включає

Наближення й замах flimsy net по видимій комасі першого повного дня Animal Crossing: New Horizons.

### Виключає

Закидання вудки; автономну пастку; хапання рукою; бій за здобич; автоматичний збір від контакту.

### Ігри-носії

- [`GAME-0320` — "Animal Crossing: New Horizons"](../games/a-f/animal-crossing-new-horizons.md)

## ACT-478

- Назва: Виконати друге натискання активного перезарядження
- Переглянуто: `2026-09-20`

### Операційне визначення

Після початку перезарядження магазина гравець навмисно вдруге натискає кнопку перезарядження в обраний момент, доки діє авторський індикатор часу, просячи систему оцінити втручання замість звичайної тривалості.

### Включає

Друге натискання правого бампера під час active reload у навчальному маршруті оригінальної Gears of War для Xbox 360.

### Виключає

Початок звичайного перезарядження; таймінг атаки; охолодження теплової зброї без перенесення запасних набоїв; пасивний показник швидкості.

### Ігри-носії

- [`GAME-0321` — Gears of War](../games/g-l/gears-of-war.md)

## ACT-479

- Назва: Чергувати прив’язане розгойдування й аеродинамічне планерування
- Переглянуто: `2026-09-20`

### Операційне визначення

Під час безпосереднього керування персонажем у безперервному тривимірному світі гравець повторно прикріплює лінію руху до придатної навколишньої геометрії або розкриває перенесену аеродинамічну поверхню, а потім керує розгойдуванням чи планеруванням зі збереженням живого імпульсу між режимами.

### Включає

Поєднання павутинного розгойдування та Web Wings Peter або Miles у Surface Tension у Marvel's Spider-Man 2.

### Виключає

Притягування до однієї обраної кінцевої точки; сценарний кінематографічний політ; звичайний стрибок; парашут після транспорту; телепортацію між позначками.

### Ігри-носії

- [`GAME-0323` — "Marvel’s Spider-Man 2"](../games/m-r/marvels-spider-man-2.md)

## ACT-480

- Назва: Застосувати виділений рівень особистої шкали підсилень
- Переглянуто: `2026-09-20`

### Операційне визначення

Після того як зібрані підсилення просунули впорядковану шкалу одного безпосередньо керованого персонажа, гравець навмисно застосовує поточний виділений рівень і обирає його зброю або рухову можливість замість очікування пізнішого рівня.

### Включає

Натискання SELECT на виділеному рівні ряду Burn, Iron, Smith або Beans у першій місії Contra Force.

### Виключає

Підбирання об’єкта, який просуває шкалу; перемикання героя; активацію підсилення поля; купівлю постійного поліпшення.

### Ігри-носії

- [`GAME-0324` — Contra Force](../games/a-f/contra-force.md)

## ACT-481

- Назва: Сканувати одну доступну місцеву ціль для даних огляду
- Переглянуто: `2026-09-21`

### Операційне визначення

У режимі ручного огляду гравець наводиться на одну доступну ціль у межах дальності й записує один збережений зразок до поступу огляду її класу або місцевості.

### Включає

Сканування однієї рослини, тварини або мінералу на Kreet у Starfield.

### Виключає

Утримання сканера до завершення технологічного креслення; пасивний імпульс ресурсів; вибір віддаленої планети; підбирання цілі.

### Ігри-носії

- [`GAME-0331` — Starfield](../games/s-z/starfield.md)

## ACT-482

- Назва: Обрати досяжну ціль на зоряній мапі й підтвердити подорож корабля
- Переглянуто: `2026-09-21`

### Операційне визначення

На навігаційній поверхні корабля гравець обирає один поточно досяжний зоряний регіон, планету, орбіту чи місце посадки й підтверджує допустимий маршрут.

### Включає

Подорожі Frontier з Vectera до Kreet, із Kreet до Jemison і посадка в New Atlantis у Starfield.

### Виключає

Безпосередній політ у місцевому просторі; швидке переміщення персонажа в межах одного місця; караван; необмежену телепортацію.

### Ігри-носії

- [`GAME-0331` — Starfield](../games/s-z/starfield.md)

## ACT-483

- Назва: Ділити, об'єднувати або передавати одновидовий загін істот
- Переглянуто: `2026-09-21`

### Операційне визначення

Переміщувати вибрану кількість одного виду істот між допустимими комірками армії героя чи гарнізону міста, ділячи загін, об'єднуючи сумісні загони або передаючи його повністю без зміни виду.

### Включає

Перебудову армії Christian і гарнізону Caryatid у Homecoming Heroes III.

### Виключає

Найм нових істот; рух героя мапою; інвентар; змішування різних видів.

### Ігри-носії

- [`GAME-0332` — "Heroes of Might and Magic III: Complete"](../games/g-l/heroes-of-might-and-magic-iii-complete.md)

## ACT-484

- Назва: Підтвердити одну допустиму дію активного загону в бою
- Переглянуто: `2026-09-21`

### Операційне визначення

На бойовому ході поточно активного загону підтвердити один допустимий рух гексами, ближню чи дальню атаку, очікування або захист.

### Включає

Ручне керування загоном у бою Homecoming Heroes III.

### Виключає

Рух героя мапою; наказ наживо; закляття; автоматичну відплату.

### Ігри-носії

- [`GAME-0332` — "Heroes of Might and Magic III: Complete"](../games/g-l/heroes-of-might-and-magic-iii-complete.md)

## ACT-485

- Назва: Редагувати платну колію й станцію авторського атракціону
- Переглянуто: `2026-09-21`

### Операційне визначення

Розміщувати або прибирати типізовані сегменти колії та станції, а тоді ставити вхід і вихід атракціону, створюючи одну сталу прохідну геометрію з оплатою кожного сегмента.

### Включає

Будівництво колії, станції, входу й виходу Steel Mini Roller Coaster у Forest Frontiers RollerCoaster Tycoon Deluxe.

### Виключає

Фіксований атракціон чи кіоск; гостьові доріжки; тестування, відкриття або ціноутворення; пряме керування вагоном.

### Ігри-носії

- [`GAME-0335` — RollerCoaster Tycoon Deluxe](../games/m-r/rollercoaster-tycoon-deluxe.md)

## ACT-486

- Назва: Налаштувати й запустити один гостьовий атракціон
- Переглянуто: `2026-09-21`

### Операційне визначення

Перемикати збудований атракціон між закритим, тестовим і відкритим станами та задавати його ціну, умову відправлення, найменший і найбільший час очікування й інтервал огляду без зміни геометрії.

### Включає

Тестування, відкриття й робочі налаштування атракціонів у Forest Frontiers.

### Виключає

Будівництво колії; відкриття всього парку; автоматичну посадку й відправлення; пряме керування вагоном.

### Ігри-носії

- [`GAME-0335` — RollerCoaster Tycoon Deluxe](../games/m-r/rollercoaster-tycoon-deluxe.md)

## ACT-487

- Назва: Задати відкритість і вхідну ціну керованого закладу
- Переглянуто: `2026-09-21`

### Операційне визначення

Відкривати або закривати один керований громадський заклад і, якщо правила дозволяють, змінювати спільну вхідну ціну, яку мають прийняти нові відвідувачі.

### Включає

Відкриття Forest Frontiers і налаштування ціни входу в парк.

### Виключає

Стан чи ціну окремого атракціону; будівництво входу; маркетинг; купівлю квитка відвідувачем.

### Ігри-носії

- [`GAME-0335` — RollerCoaster Tycoon Deluxe](../games/m-r/rollercoaster-tycoon-deluxe.md)
- [`GAME-0370` — Theme Hospital](../games/s-z/theme-hospital.md)

## ACT-488

- Назва: Найняти й обмежити автономного працівника сервісу
- Переглянуто: `2026-09-21`

### Операційне визначення

Наймати одного працівника в оголошену автономну сервісну роль, розміщувати його на досяжній керованій території та за потреби обмежувати зону патрулювання чи дозволені класи робіт без керування кожним кроком.

### Включає

Найм, розміщення й зонування механіка у Forest Frontiers.

### Виключає

Пряме ведення працівника; одну негайну ціль руху; наперед наданого працівника; саму регулярну зарплату.

### Ігри-носії

- [`GAME-0335` — RollerCoaster Tycoon Deluxe](../games/m-r/rollercoaster-tycoon-deluxe.md)
- [`GAME-0370` — Theme Hospital](../games/s-z/theme-hospital.md)

## ACT-489

- Назва: Стукнути по сусідній поверхні, щоб створити приманку
- Переглянуто: `2026-09-21`

### Операційне визначення

Перебуваючи біля сумісної поверхні, гравець виконує окрему контекстну дію, яка не пошкоджує її, а створює локалізований звук у світі, на чиє положення можуть відреагувати придатні автономні актори поблизу.

### Включає

Стук Solid Snake по стіні чи іншій сумісній поверхні, щоб відвернути придатного Genome Soldier у вступі Metal Gear Solid.

### Виключає

Випадкові кроки або шум калюжі; кидок приманки; постріл; удар по актору; руйнування чи зміну поверхні.

### Ігри-носії

- [`GAME-0339` — Metal Gear Solid](../games/m-r/metal-gear-solid.md)

## ACT-490

- Назва: Прицілити світловий пістолет до екрана й натиснути спуск
- Переглянуто: `2026-09-21`

### Операційне визначення

Гравець фізично спрямовує сумісний світлочутливий пістолет на показане ігрове поле й натискає спуск, запитуючи один просторовий постріл, для якого напрям наведення визначає відгук екрана, зчитаний пістолетом.

### Включає

Одне натискання спуску NES Zapper, спрямованого на поточну качку Game A в оригінальному північноамериканському картриджі Duck Hunt.

### Виключає

Переміщення екранного прицілу стіком або мишею; вибір цілі з меню; звичайне вільне прицілювання в симуляції вогнепальної зброї; наступне системне визначення влучання чи промаху; сучасну заміну-вказівник, положення якої надходить незалежно від світла екрана.

### Ігри-носії

- [`GAME-0345` — "Duck Hunt"](../games/a-f/duck-hunt.md)

## ACT-491

- Назва: Перенести й покласти непритомне тіло
- Переглянуто: `2026-09-21`

### Операційне визначення

Гравець бере одне досяжне мертве або непритомне тіло у винятковий стан перенесення, рухається з ним і відпускає в обраному досяжному місці; тіло лишається видимим і виявлюваним об’єктом світу, а не стає предметом спорядження.

### Включає

Sam Fisher підіймає непритомного охоронця, переносить його в тінь і тихо кладе під час обмеженого маршруту Training Course та Police Station в оригінальній Xbox-версії Splinter Cell.

### Виключає

Підіймання предмета до inventory; перенесення або кидання мішка з цільовою здобиччю; доставлення живого підопічного в транспорт; тягнення притомного утримуваного актора до потрібного пристрою; автоматичний рух ragdoll; остаточне вилучення переможеного актора зі світу.

### Ігри-носії

- [`GAME-0349` — "Tom Clancy’s Splinter Cell"](../games/s-z/tom-clancys-splinter-cell.md)

## ACT-492

- Назва: Виконати показану послідовність графіті на позначеній поверхні
- Переглянуто: `2026-09-21`

### Операційне визначення

Перебуваючи біля придатної позначеної поверхні, гравець починає нанесення графіті й, коли поверхня вимагає послідовності, вводить показані напрямки до переривання живої спроби.

### Включає

Початок великого чи надвеликого обов’язкового графіті та виконання його напрямленої послідовності у вступі Jet Set Radio для Xbox 360.

### Виключає

Вибір зображення в редакторі; довільне малювання; вибір покрокової бойової команди; автоматичну заміну поверхні від дотику; системне списання фарби й зарахування завершення.

### Ігри-носії

- [`GAME-0350` — "Jet Set Radio"](../games/g-l/jet-set-radio.md)

## ACT-493

- Назва: Наказати їздовому компаньйону проковтнути або виплюнути придатне тіло
- Переглянуто: `2026-09-22`

### Операційне визначення

Під час прямої їзди на сумісному компаньйоні гравець наказує йому простягнути орган поглинання до одного досяжного придатного тіла світу, взяти це тіло в утримуваний стан рота або виплюнути утримуване тіло до автоматичного розв’язання.

### Включає

Йоші простягає язик, щоб з’їсти ягоду чи придатний панцир Купи, та випльовує утримуваний панцир у межах Yoshi's Island 2 із Super Mario World.

### Виключає

Посадку, керування чи спішування; системний ефект від типу тіла; автоматичне ковтання після таймера; пряме збирання предмета в інвентар вершника; ненадану гравцем атаку компаньйона.

### Ігри-носії

- [`GAME-0354` — Super Mario World](../games/s-z/super-mario-world.md)

## ACT-494

- Назва: Утримувати ціль світу у фіксації та рухатися відносно неї
- Переглянуто: `2026-09-22`

### Операційне визначення

Гравець утримує одну придатну ціль світу поточною зафіксованою ціллю, зберігає напрям погляду на неї та задає рух або окремий ривок навколо неї, до неї чи від неї.

### Включає

Рух по орбіті та бічний ривок навколо Parasite Queen із затиснутою фіксацією Combat Visor у вступі Metroid Prime.

### Виключає

Вільне прицілювання без утримуваної цілі; наведений снаряд після пострілу; обертання оглядової камери; вибір цілі лише в меню; автоматичний вибір цілі для атаки.

### Ігри-носії

- [`GAME-0355` — Metroid Prime](../games/m-r/metroid-prime.md)
- [`GAME-0363` — "The Legend of Zelda: Ocarina of Time"](../games/s-z/the-legend-of-zelda-ocarina-of-time.md)

## ACT-495

- Назва: Сфокусувати відбите сонячне світло для запиту напряму у світі
- Переглянуто: `2026-09-22`

### Операційне визначення

Коли перенесений відбивний інструмент перебуває під достатнім прямим світлом, гравець утримує його команду фокусування й спрямовує інструмент, доки відбиті промені не зійдуться, запитуючи напрям до поточної авторської цілі світу.

### Включає

Підняття й спрямування Ancient Sword у відкритому сонячному світлі для зведення напрямного променя до першого колоса у вступі Shadow of the Colossus.

### Виключає

Постійний компас; кинутий визначник напряму; читання готової позначки на мапі; виявлення слабкого місця на тілі; звичайне прицілювання зброєю.

### Ігри-носії

- [`GAME-0356` — Shadow of the Colossus](../games/s-z/shadow-of-the-colossus.md)

## ACT-496

- Назва: Запускати авторський маневр літака або турборивок
- Переглянуто: `2026-09-22`

### Операційне визначення

Під час прямого керування придатним літаком гравець запускає один доступний запрограмований маневр положення або обмежений турборивок, запитуючи його авторську зміну орієнтації чи швидкості з поточного живого стану польоту.

### Включає

Запуск Immelmann, barrel roll або турборивка в обмеженій першій місії The Morning After оригінальної Xbox-версії Crimson Skies: High Road to Revenge.

### Виключає

Звичайне безперервне керування; розподіл потужності між підсистемами літака; випуск накопиченого drift boost; вибір пункту на мапі; кінематографічний маневр без команди гравця.

### Ігри-носії

- [`GAME-0359` — "Crimson Skies: High Road to Revenge"](../games/a-f/crimson-skies-high-road-to-revenge.md)

## ACT-497

- Назва: Підтвердити фіксований набір різних стартових профільних навичок
- Переглянуто: `2026-09-22`

### Операційне визначення

До початку кампанії гравець обирає й підтверджує точно оголошену кількість різних навичок із ширшого списку; кожна вибрана навичка отримує початковий профільний бонус без витрати числового запасу очок.

### Включає

Вибір Explosives, Medicine і Speech як трьох tagged skills у Fallout: New Vegas перед виходом із послідовності створення персонажа Doc Mitchell.

### Виключає

Розподіл числових очок характеристик; вибір класу; optional traits; витрачання пізнішого skill або perk point; тренування активного агента; тимчасовий бонус спорядження.

### Ігри-носії

- [`GAME-0361` — Fallout: New Vegas](../games/a-f/fallout-new-vegas.md)

## ACT-498

- Назва: Налаштувати місце та напрям перед кидком
- Переглянуто: `2026-09-22`

### Операційне визначення

Перед випуском кулі на доріжку гравець перемикається між налаштуванням місця збоку та кута прицілу й окремо змінює обидва параметри, ще не починаючи рух кулі.

### Включає

Вибір місця та напряму за допомогою хрестовини й кнопки A в оригінальному боулінгу Wii Sports.

### Виключає

Прицілювання з нерухомої пускової установки; керування кулею після випуску; вибір напряму вільного кидка без окремого налаштування місця біля доріжки.

### Ігри-носії

- [`GAME-0364` — Wii Sports](../games/s-z/wii-sports.md)

## ACT-499

- Назва: Випустити кулю рухом руки у вибрану мить
- Переглянуто: `2026-09-22`

### Операційне визначення

Утримуючи кнопку кидка, гравець робить фізичний помах; її відпускання в певну мить задає початковий рух кулі, на який впливають помах і поворот зап’ястка.

### Включає

Утримування B, помах пультом Wii Remote, відпускання B поблизу нижньої точки та необов’язковий поворот зап’ястка в оригінальному боулінгу Wii Sports.

### Виключає

Клацання по нерухомій пусковій установці; заряджений постріл лише кнопкою; пряме керування кулею після випуску; автоматичний випуск у нижній точці помаху.

### Ігри-носії

- [`GAME-0364` — Wii Sports](../games/s-z/wii-sports.md)

## ACT-500

- Назва: Обирати трюк і переходити до наступного без розриву руху
- Переглянуто: `2026-09-23`

### Операційне визначення

Керуючи рухомим скейтером, гравець вибирає допустиму комбінацію напряму й кнопки для поточного стану в повітрі, на рейці чи на землі та може перейти через мануал або розворот до іншого допустимого трюку, не підсумовуючи відразу весь зв’язаний ланцюг.

### Включає

Керування трюками з переворотом дошки, захватом і ковзанням рейкою на PlayStation, напрямленими Manual і Nose Manual, обертанням у повітрі та продовженням через Revert у стандартному наборі рухів Tony Hawk's Pro Skater 1 + 2 в Warehouse Tour.

### Виключає

Постійну зміну слотів трюків персонажа; автоматичний вибір трюку; фіксовану серію бойових ударів; очки без успішно виконаного трюку; старі набори рухів Classic THPS1 або Classic THPS2.

### Ігри-носії

- [`GAME-0365` — Tony Hawk’s Pro Skater 1 + 2](../games/s-z/tony-hawks-pro-skater-1-plus-2.md)

## ACT-501

- Назва: Вирівнювати дошку під час тривалого трюку
- Переглянуто: `2026-09-23`

### Операційне визначення

Поки триває ковзання рейкою або мануал, гравець коригує баланс рухомого скейтера за показаним станом, щоб зберегти трюк і зв’язаний ланцюг до добровільного виходу з нього.

### Включає

Активне вирівнювання під час ковзання рейкою чи мануалу в стандартних правилах Warehouse Tour без допоміжних режимів Tony Hawk's Pro Skater 1 + 2.

### Виключає

Допоміжні режими Perfect Rail Balance і Perfect Manual Balance; одноразовий вибір стійки; саме лише спостереження за індикатором; загальне відновлення здоров’я чи витривалості.

### Ігри-носії

- [`GAME-0365` — Tony Hawk’s Pro Skater 1 + 2](../games/s-z/tony-hawks-pro-skater-1-plus-2.md)

## ACT-502

- Назва: Зробити знімок поточного кадру
- Переглянуто: `2026-09-23`

### Операційне визначення

Коли камера готова та має доступний ресурс для знімка, гравець наводить її на досяжний живий об’єкт і один раз натискає спуск: поточну сцену фіксують для оцінювання за змістом.

### Включає

Знімок возз’єднання Джеффа й Наталі на даху в режимі «72 години» Dead Rising; фотографію Пікачу зі скінченного запасу кадрів під час автоматичного руху маршрутом Beach у Pokémon Snap.

### Виключає

Просте наведення камери без знімка; системний скриншот; фотографію, яка змінює геометрію світу; оцінювання й нарахування очок після знімка.

### Ігри-носії

- [`GAME-0368` — Dead Rising](../games/a-f/dead-rising.md)
- [`GAME-0371` — Pokémon Snap](../games/m-r/pokemon-snap.md)

## ACT-503

- Назва: Зайняти об’єкт щойно викладеного тайла підданим
- Переглянуто: `2026-09-23`

### Операційне визначення

Після викладання тайла гравець може поставити одного доступного підданого на допустиму частину дороги, міста чи монастиря цього тайла або покласти його як селянина на поле.

### Включає

Одного міпла на щойно викладеному тайлі Carcassonne: стоячи в місті, на дорозі чи монастирі або лежачи на полі.

### Виключає

Підданого на старому тайлі; двох підданих за один хід; підрахунок очок і повернення підданого.

### Ігри-носії

- [`GAME-0369` — Carcassonne](../games/a-f/carcassonne.md)

## ACT-504

- Назва: Спроєктувати й обладнати кабінет перед відкриттям
- Переглянуто: `2026-09-23`

### Операційне визначення

Гравець задає допустимий розмір кабінету, розміщує двері й обов’язкові меблі у дозволених місцях, а потім відкриває обладнаний кабінет для відповідної послуги.

### Включає

Кабінет терапевта, загальну діагностику, аптеку, психіатричний кабінет і клініку лікування роздутої голови в першій лікарні Theme Hospital.

### Виключає

Звичайне встановлення предмета в коридорі; саме лікування; роботу кабінету без потрібного працівника.

### Ігри-носії

- [`GAME-0370` — Theme Hospital](../games/s-z/theme-hospital.md)

## ACT-505

- Назва: Змінювати черги й правила діагностики пацієнтів
- Переглянуто: `2026-09-23`

### Операційне визначення

Гравець змінює стале правило для пацієнтів із неповним діагнозом або відпочинку персоналу чи переставляє пацієнта в черзі або переводить його до іншої черги того самого виду до початку послуги.

### Включає

Ліміти й перенесення черг, пороги «відправити додому» та «спробувати лікувати», поріг відпочинку працівників у Theme Hospital.

### Виключає

Покрокове керування рухом кожного пацієнта; переведення до несумісного кабінету; наслідок лікування; будівництво кабінету.

### Ігри-носії

- [`GAME-0370` — Theme Hospital](../games/s-z/theme-hospital.md)

## ACT-506

- Назва: Кинути приманку біля самостійного персонажа
- Переглянуто: `2026-09-23`

### Операційне визначення

Під час живої сцени гравець кидає доступну нешкідливу приманку в досяжне місце біля рухомої істоти, щоб та могла відреагувати на місце падіння без прямого наказу гравця.

### Включає

Кинути розблоковану Pokémon Food біля Пікачу на маршруті Beach у Pokémon Snap, коли камера не перебуває в режимі фокусування.

### Виключає

Пряме керування істотою; звукову приманку стуканням по стіні; бойовий снаряд; подальшу реакцію істоти.

### Ігри-носії

- [`GAME-0371` — Pokémon Snap](../games/m-r/pokemon-snap.md)

## ACT-507

- Назва: Позначити один знятий кадр кожного виду для оцінювання
- Переглянуто: `2026-09-23`

### Операційне визначення

Після обмеженої фотосесії гравець вибирає один кадр істоти певного виду й позначає його для подальшого оцінювання; зміна вибору замінює попереднього кандидата того самого виду.

### Включає

Вибір однієї фотографії Пікачу в Camera Check та позначення її знаком професора Оука перед перевіркою Pokémon Snap.

### Виключає

Саме фотографування; окрему позначку тільки для альбому; одночасне подання всіх знімків виду; результат оцінювання.

### Ігри-носії

- [`GAME-0371` — Pokémon Snap](../games/m-r/pokemon-snap.md)

## ACT-508

- Назва: Затиснути лади й ударити по струнах у мить ноти
- Переглянуто: `2026-09-23`

### Операційне визначення

Гравець затискає лади, які відповідають показаній одиничній ноті або одночасному акорду, і б’є по струнах, коли подія доходить до лінії удару; система перевіряє цю дію за заданим графіком пісні.

### Включає

Одиничні ноти й акорди на зеленому, червоному та жовтому ладах в одиночному Quick Play Guitar Hero III на Easy.

### Виключає

Натискання для ухилення від просторової перешкоди; вільне музикування без заданих нот; автоматичне влучання від самого затискання ладу без удару по струнах.

### Ігри-носії

- [`GAME-0372` — "Guitar Hero III: Legends of Rock"](../games/g-l/guitar-hero-iii-legends-of-rock.md)

## ACT-509

- Назва: Активувати накопичений запас підсилення під час пісні
- Переглянуто: `2026-09-23`

### Операційне визначення

Коли здобутий запас підсилення сягає встановленого мінімуму, гравець свідомо активує його під час рухомого графіка пісні й витрачає заряд протягом тимчасового посилення очок.

### Включає

Активацію щонайменше напівзаповненого Star Power нахилом гітарного контролера Les Paul або кнопкою SELECT в одиночній пісні Guitar Hero III для PS3.

### Виключає

Саме здобуття заряду за послідовність нот; постійний множник; атаки на іншого гравця в режимі дуелі.

### Ігри-носії

- [`GAME-0372` — "Guitar Hero III: Legends of Rock"](../games/g-l/guitar-hero-iii-legends-of-rock.md)

## ACT-510

- Назва: Покликати партнера й дістатися редактора тіла
- Переглянуто: `2026-09-23`

### Операційне визначення

Керуючи істотою в активному етапі, гравець кличе партнера й дістається до нього, щоб перейти з живого світу до редактора наступної версії цієї істоти.

### Включає

Поклик, заплив до партнера й вхід до Cell Creator у Spore після того, як перша знайдена частина відкриває цю дію.

### Виключає

Незалежний редактор у галереї без партнера в активному етапі; автоматичне зростання без входу до редактора; зміну частин під час плавання.

### Ігри-носії

- [`GAME-0373` — Spore](../games/s-z/spore.md)

## ACT-511

- Назва: Змінити тіло живої лінії частинами
- Переглянуто: `2026-09-23`

### Операційне визначення

У редакторі, до якого переходять з активного етапу життя, гравець розміщує доступну функціональну частину на тілі керованої лінії або прибирає її, а тоді зберігає змінену форму для продовження гри.

### Включає

Додавання, налаштування або вилучення рота, частин руху й зброї в Cell Creator Spore перед збереженням клітини та поверненням у воду.

### Виключає

Суто декоративне фарбування; заміну спорядження у фіксованому слоті під час бою; створення сторонньої істоти в окремій галереї.

### Ігри-носії

- [`GAME-0373` — Spore](../games/s-z/spore.md)

## ACT-512

- Назва: Прибирати сміття із саду інструментом
- Переглянуто: `2026-09-23`

### Операційне визначення

Гравець спрямовує садовий інструмент на предмет сміття й повторює дію, доки предмет не перестане займати ділянку землі.

### Включає

Прибирання початкового сміття лопатою від Leafos в оригінальній Viva Piñata.

### Виключає

Пошук закопаного предмета, збирання врожаю, знищення мешканця або оплата роботи помічника.

### Ігри-носії

- [`GAME-0375` — Viva Piñata](../games/s-z/viva-pinata.md)

## ACT-513

- Назва: Домовлятися про обмін ресурсами з іншим гравцем
- Переглянуто: `2026-09-23`

### Операційне визначення

Активний гравець домовляється з іншим про обмін карток ресурсів визначених видів і кількостей; умови може запропонувати будь-хто з них, а передача відбувається лише після згоди обох учасників.

### Включає

Добровільний обмін під час фази CATAN, зокрема зустрічну пропозицію суперника активному гравцеві.

### Виключає

Подарунок без зустрічного ресурсу, обмін із банком, картки розвитку та відхилену пропозицію.

### Ігри-носії

- [`GAME-0377` — CATAN](../games/a-f/catan.md)

## ACT-514

- Назва: Обмінювати однакові ресурси з банком
- Переглянуто: `2026-09-23`

### Операційне визначення

Гравець повертає до банку потрібну кількість карток одного виду й бере одну картку іншого виду за доступним йому курсом.

### Включає

Морський обмін у CATAN за звичайним курсом 4:1 або за знижкою відповідної гавані 3:1 чи 2:1.

### Виключає

Домовленість з іншим гравцем, безкоштовні ресурси від картки розвитку й обмін без потрібної кількості однакових карток.

### Ігри-носії

- [`GAME-0377` — CATAN](../games/a-f/catan.md)

## ACT-515

- Назва: Оплатити й розмістити законну споруду в мережі
- Переглянуто: `2026-09-23`

### Операційне визначення

Гравець сплачує потрібні ресурси й розміщує доступну власну фігуру на дозволеному ребрі чи вершині або поліпшує власну споруду на тому самому місці.

### Включає

Будівництво дороги чи поселення та заміну свого поселення містом у CATAN.

### Виключає

Безкоштовні дороги від картки розвитку, недозволену позицію й купівлю картки розвитку.

### Ігри-носії

- [`GAME-0377` — CATAN](../games/a-f/catan.md)

## ACT-516

- Назва: Купити приховану картку розвитку
- Переглянуто: `2026-09-23`

### Операційне визначення

Гравець сплачує потрібні три види ресурсів і бере верхню закриту картку зі скінченної колоди розвитку, не вибираючи її вміст.

### Включає

Купівлю картки розвитку за руду, вовну й зерно у CATAN.

### Виключає

Використання вже придбаної картки, вибір із відкритої пропозиції та купівлю з порожньої колоди.

### Ігри-носії

- [`GAME-0377` — CATAN](../games/a-f/catan.md)

## ACT-517

- Назва: Зіграти дозволену картку розвитку
- Переглянуто: `2026-09-23`

### Операційне визначення

На власному ході гравець обирає придатну картку розвитку з руки, відкриває її й запускає надруковану дію з урахуванням обмежень ходу та часу купівлі.

### Включає

Лицаря, картку прогресу й особливе відкриття картки переможного очка для виграшу у CATAN.

### Виключає

Купівлю картки, обмін нею та розіграш двох лицарів або карток прогресу за один хід.

### Ігри-носії

- [`GAME-0377` — CATAN](../games/a-f/catan.md)

## ACT-518

- Назва: Пересунути розбійника й обрати сусіда для крадіжки
- Переглянуто: `2026-09-23`

### Операційне визначення

Після відповідної події активний гравець переносить розбійника на інший гекс і за наявності сусідніх споруд суперників обирає одного власника, у якого випадково береться картка ресурсу.

### Включає

Переміщення розбійника після сімки або зіграного лицаря у CATAN.

### Виключає

Примусове скидання надлишку карток, вибір конкретної прихованої картки й залишення розбійника на тому самому гексі.

### Ігри-носії

- [`GAME-0377` — CATAN](../games/a-f/catan.md)

## ACT-519

- Назва: Безперервно нахиляти трасу, щоб скеровувати кулю
- Переглянуто: `2026-09-23`

### Операційне визначення

Гравець безперервним рухом стика змінює нахил прохідної траси, щоб сила тяжіння скеровувала рухому кулю її поверхнею; він не задає кулі точну позицію або окремий фіксований хід.

### Включає

Нахил першої траси Simple у Super Monkey Ball 2 стиком GameCube, щоб провести кулю з мавпочкою до фінішу.

### Виключає

Безпосереднє пересування аватара за ACT-008, дискретний вибір нової грані сили тяжіння за ACT-097, зміну камери без нахилу траси й автоматичний пошук шляху до вибраної цілі.

### Ігри-носії

- [`GAME-0378` — Super Monkey Ball 2](../games/s-z/super-monkey-ball-2.md)

## ACT-520

- Назва: Прицілитися й вистрілити зброєю чергового черв’яка
- Переглянуто: `2026-09-24`

### Операційне визначення

Протягом ходу своєї команди гравець обирає доступну зброю черв’яка, задає потрібні для неї кут, силу або час запалу з поточної позиції рухомого черв’яка, а потім робить один постріл для фізичного розв’язання.

### Включає

Прицілювання та постріл із базуки або гранати з налаштованими запалом і відскоком у дослідженому локальному матчі Worms Armageddon.

### Виключає

Нерухомий пусковий пристрій за ACT-113, кілька різних пострілів за один хід і безпосереднє керування снарядом після запуску.

### Ігри-носії

- [`GAME-0379` — Worms Armageddon](../games/s-z/worms-armageddon.md)

## ACT-521

- Назва: Обвести й підтвердити місце на малюнку
- Переглянуто: `2026-09-24`

### Операційне визначення

У загадці з малюнком гравець проводить замкнену лінію навколо однієї з можливих ділянок і окремо підтверджує вибране місце як відповідь для перевірки.

### Включає

Обведення стилусом потрібного села на початковій карті Professor Layton and the Curious Village та натискання кнопки підтвердження.

### Виключає

Змінну позначку-гіпотезу ACT-004, заповнення всієї сітки, вибір точки для пересування персонажа та дотик до екрана без підтвердження відповіді.

### Ігри-носії

- [`GAME-0380` — Professor Layton and the Curious Village](../games/m-r/professor-layton-and-the-curious-village.md)

## ACT-522

- Назва: Купити наступну підказку за монету
- Переглянуто: `2026-09-24`

### Операційне визначення

Під час нерозв’язаної авторської загадки гравець свідомо витрачає одну наявну монету підказок, щоб відкрити наступне заздалегідь написане уточнення, не подаючи відповіді.

### Включає

Придбання наступної з трьох підказок до початкової загадки Professor Layton and the Curious Village.

### Виключає

Автоматичну навчальну пораду, пошук прихованої монети в сцені, купівлю стороннього предмета й відкриття всіх підказок одним платежем.

### Ігри-носії

- [`GAME-0380` — Professor Layton and the Curious Village](../games/m-r/professor-layton-and-the-curious-village.md)

## ACT-523

- Назва: Малювати мазок пензлем по ігровому світу
- Переглянуто: `2026-09-24`

### Операційне визначення

Гравець відкриває окремий вид небесного пензля на поточний світ, проводить просторову лінію по видимому придатному об’єкту або прогалині й закриває цей вид, подаючи мазок на перевірку для дії вже вивченої техніки.

### Включає

Домалювання відсутньої частини Небесної ріки чи меча статуї Наґі та розрізання валуна, перегороди або ніжки плоду в дослідженому початку Ōkami HD.

### Виключає

Позначення відповіді в окремій загадці ACT-521, удар дзеркалом ACT-161, суто декоративний слід курсора й застосування ще не вивченої техніки.

### Ігри-носії

- [`GAME-0382` — Ōkami HD](../games/m-r/okami-hd.md)

## ACT-524

- Назва: Перемикати вибраного члена постійної сім’ї
- Переглянуто: `2026-09-24`

### Операційне визначення

Гравець вибирає іншого мешканця тієї самої постійної сім’ї, якому адресує контекстні накази, а раніше вибраний мешканець залишається в будинку й продовжує діяти за правилами симуляції.

### Включає

Перемикання між двома дорослими в дослідженій сім’ї The Sims 2: Legacy Collection через портрети в режимі життя.

### Виключає

Заміну всієї сім’ї; безпосереднє керування кожним кроком персонажа ACT-228; вибір предмета без зміни активного мешканця.

### Ігри-носії

- [`GAME-0383` — The Sims 2: Legacy Collection](../games/s-z/the-sims-2-legacy-collection.md)

## ACT-525

- Назва: Завдати бічного або обертального удару гоночною машиною
- Переглянуто: `2026-09-24`

### Операційне визначення

Безпосередньо керуючи машиною поблизу суперників, гравець виконує спрямований бічний удар або обертальну атаку, що при контакті може зрушити чи вибити іншу машину з заїзду.

### Включає

Бічні й обертальні атаки F-Zero GX у дослідженому першому заїзді Ruby Cup.

### Виключає

Звичайне зіткнення під час кермування; застосування випадково отриманого предмета; удар персонажа поза гоночною машиною.

### Ігри-носії

- [`GAME-0384` — F-Zero GX](../games/a-f/f-zero-gx.md)

## ACT-526

- Назва: Уточнювати вибраний рядок свідчень
- Переглянуто: `2026-09-24`

### Операційне визначення

Під час перехресного допиту гравець вибирає доступний рядок підготовлених свідчень і просить свідка пояснити його, щоб отримати уточнення або, за потреби, змінений рядок.

### Включає

Запитання до вибраного твердження Френка Соуіта в першій справі Phoenix Wright: Ace Attorney.

### Виключає

Звичайне гортання діалогу; подання доказу проти рядка ACT-527; довільний допит поза свідченнями; припущення, що кожне запитання змінює матеріали справи.

### Ігри-носії

- [`GAME-0385` — 'Phoenix Wright: Ace Attorney'](../games/m-r/phoenix-wright-ace-attorney.md)

## ACT-527

- Назва: Подавати доказ проти вибраного рядка свідчень
- Переглянуто: `2026-09-24`

### Операційне визначення

Коли вибрано рядок підготовлених свідчень, гравець бере один наявний матеріал справи й подає його до суду як доказ суперечності саме цьому твердженню.

### Включає

Подання звіту про розтин проти твердження Соуіта про час або запису про відключення електрики проти його слів про телевізор у першій справі.

### Виключає

Уточнення через запитання ACT-526; саме лише читання доказу; позначення двох змінних фактів в інтерфейсі перевірки ACT-104; особисте затвердження вироку для всієї справи ACT-105.

### Ігри-носії

- [`GAME-0385` — 'Phoenix Wright: Ace Attorney'](../games/m-r/phoenix-wright-ace-attorney.md)

## ACT-528

- Назва: Оглядати предмет, доки не відкриється доказова деталь
- Переглянуто: `2026-09-24`

### Операційне визначення

Після вибору досяжного предмета на місці події гравець змінює кут огляду або фокус, доки не побачить важливе для справи маркування, напис чи приховану поверхню; тоді гра записує знайдене як доказ.

### Включає

Поворот окулярів, щоб прочитати марку виробника, та огляд посвідчення в гаманці біля вантажного депо у справі The Driver's Seat гри L.A. Noire.

### Виключає

Підбирання декорації без корисного доказу; автоматично отриману в розмові відомість; збирання інструмента для інвентарю ACT-089; подання матеріалу судової справи проти свідчення ACT-527.

### Ігри-носії

- [`GAME-0388` — L.A. Noire](../games/g-l/la-noire.md)

## ACT-529

- Назва: Підтверджувати звинувачення записаним доказом
- Переглянуто: `2026-09-24`

### Операційне визначення

Звинувативши співрозмовника щодо поточної відповіді, гравець вибирає один уже внесений до записника доказ як конкретну суперечність його словам.

### Включає

Вибір знайденого доказу після команди Accuse в допиті першої справи дорожнього відділу у версії L.A. Noire для PS4.

### Виключає

Вибір Good Cop або Bad Cop без доказу ACT-232; подання доказу проти окремого рядка судових свідчень ACT-527; позначення двох фактів у документах ACT-104.

### Ігри-носії

- [`GAME-0388` — L.A. Noire](../games/g-l/la-noire.md)

## ACT-530

- Назва: Вибирати напрям на розвилці ігрового поля
- Переглянуто: `2026-09-24`

### Операційне визначення

Коли фішка проходить зв’язаний маршрут на кількість клітинок, визначену кубиком, активний гравець на розвилці обирає один допустимий напрям. Фішка витрачає решту того самого кидка на обрану гілку.

### Включає

Спрямувати персонажа на розвилці Pirate Land у Mario Party 2 після того, як кубик уже визначив кількість кроків.

### Виключає

Вибір результату кубика SYS-004; редагування мережі поля; вибір наступного вузла в Slay the Spire ACT-127; необмежене переміщення до віддаленої клітинки; вибір результату мінігри.

### Ігри-носії

- [`GAME-0392` — Mario Party 2](../games/m-r/mario-party-2.md)

## ACT-531

- Назва: Зачепитися тросом, змінити його довжину й відпустити
- Переглянуто: `2026-09-24`

### Операційне визначення

Гравець спрямовує багаторазовий трос на сумісну досяжну опору, утримує зачеплення, керує тілом у підвішеному стані й змінює довжину троса, а потім у вибраний момент відпускає його для вільного руху.

### Включає

Гак у дослідженому маршруті Grab and Swing гри LittleBigPlanet 2: зачеплення за губку, розгойдування вбік, підтягування або опускання та своєчасне відпускання.

### Виключає

Односпрямоване підтягування з завершенням руху біля вибраної опори ACT-361; лазіння по закріпленій мотузці без прицілювання; перенесення вільного предмета; автоматичне розгойдування без рішення гравця про відпускання.

### Ігри-носії

- [`GAME-0394` — LittleBigPlanet 2](../games/g-l/littlebigplanet-2.md)

## ACT-532

- Назва: Увести вивчену послідовність символів
- Переглянуто: `2026-09-24`

### Операційне визначення

Гравець звертається до інтерфейсу, що приймає команди, і по черзі вводить скінченну вивчену послідовність символів, які не є напрямками, не пересуваючи персонажа відповідним маршрутом.

### Включає

Ввести відомий числовий пароль Бомберів при проході до обсерваторії та зіграти послідовність нот Пісні часу на повернутій окарині в першому циклі Majora's Mask.

### Виключає

Команди з основних напрямків ACT-106; ходіння маршрутом; довільне музикування; вибір відповіді в розмові; скидання світу без введення послідовності.

### Ігри-носії

- [`GAME-0395` — "The Legend of Zelda: Majora’s Mask"](../games/s-z/the-legend-of-zelda-majoras-mask.md)

## ACT-533

- Назва: Повторювати ритмічну фразу викладача
- Переглянуто: `2026-09-25`

### Операційне визначення

Після музичного прикладу викладача гравець у своїй частині пісні натискає потрібні кнопки в заданому порядку й у відповідні моменти ритму.

### Включає

Відповіді на фрази першого уроку в PaRappa the Rapper Remastered на звичайній складності.

### Виключає

Одночасне затискання ладів і удар по струнах у ACT-508; уведення пароля без музичного прикладу в ACT-532; довільне музикування без відповіді.

### Ігри-носії

- [`GAME-0396` — "PaRappa the Rapper Remastered"](../games/m-r/parappa-the-rapper-remastered.md)
