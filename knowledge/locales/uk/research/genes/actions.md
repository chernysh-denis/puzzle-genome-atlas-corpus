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

- [`GAME-0452` — Dr. Mario](../games/a-f/dr-mario.md)
- [`GAME-0649` — Drop Duchy](../games/a-f/drop-duchy.md)
- [`GAME-0442` — 'Lumines: Puzzle Fusion'](../games/g-l/lumines-puzzle-fusion.md)
- [`GAME-0529` — Tetris Effect](../games/s-z/tetris-effect.md)
- [`GAME-0004` — Tetris](../games/s-z/tetris.md)

## ACT-006

- Назва: Прискорити автоматичний перебіг
- Переглянуто: `2026-08-24`

### Операційне визначення

Гравець тимчасово збільшує швидкість автоматичної зміни стану, керованої часом, не змінюючи її напрямку чи умови завершення.

### Включає

Утримання кнопки вниз для швидшого падіння активного тетроміно в NES Tetris; вибір режиму FAST для прискорення Flooz у Pipe Dream після розміщення труб; вибір швидшого годинника симуляції Mini Metro, поки тривають автоматичні попит і перевезення; прискорення симуляції натовпу в HUMANITY після підготовки поля команд; прискорення солдатиків Tin Hearts без зміни їхнього фізичного маршруту; утримання регулятора швидкості Echochrome, поки Walker іде тим самим маршрутом, визначеним проєкцією.

### Виключає

Миттєве жорстке падіння; вибір напрямку руху; зміна постійного рівня складності поза грою.

### Ігри-носії

- [`GAME-0124` — Against the Storm](../games/a-f/against-the-storm.md)
- [`GAME-0132` — Anno 1800](../games/a-f/anno-1800.md)
- [`GAME-0135` — "Captain of Industry"](../games/a-f/captain-of-industry.md)
- [`GAME-0589` — ChuChu Rocket!](../games/a-f/chuchu-rocket.md)
- [`GAME-0284` — "Cities: Skylines II"](../games/a-f/cities-skylines-ii.md)
- [`GAME-0121` — "Cities: Skylines"](../games/a-f/cities-skylines.md)
- [`GAME-0204` — "Crusader Kings III"](../games/a-f/crusader-kings-iii.md)
- [`GAME-0452` — Dr. Mario](../games/a-f/dr-mario.md)
- [`GAME-0126` — Dwarf Fortress](../games/a-f/dwarf-fortress.md)
- [`GAME-0092` — Echochrome](../games/a-f/echochrome.md)
- [`GAME-0175` — Football Manager 26](../games/a-f/football-manager-26.md)
- [`GAME-0504` — Frostpunk 2](../games/a-f/frostpunk-2.md)
- [`GAME-0130` — Frostpunk](../games/a-f/frostpunk.md)
- [`GAME-0182` — Hearts of Iron IV](../games/g-l/hearts-of-iron-iv.md)
- [`GAME-0029` — HUMANITY](../games/g-l/humanity.md)
- [`GAME-0638` — "Lemmings 2: The Tribes"](../games/g-l/lemmings-2-the-tribes.md)
- [`GAME-0442` — 'Lumines: Puzzle Fusion'](../games/g-l/lumines-puzzle-fusion.md)
- [`GAME-0018` — Mini Metro](../games/m-r/mini-metro.md)
- [`GAME-0051` — Mini Motorways](../games/m-r/mini-motorways.md)
- [`GAME-0125` — Oxygen Not Included](../games/m-r/oxygen-not-included.md)
- [`GAME-0016` — Pipe Mania / Pipe Dream](../games/m-r/pipe-mania.md)
- [`GAME-0298` — 'Planet Zoo: Console Edition'](../games/m-r/planet-zoo-console-edition.md)
- [`GAME-0142` — Project Zomboid](../games/m-r/project-zomboid.md)
- [`GAME-0446` — Railroad Tycoon II](../games/m-r/railroad-tycoon-ii.md)
- [`GAME-0127` — RimWorld](../games/m-r/rimworld.md)
- [`GAME-0335` — RollerCoaster Tycoon Deluxe](../games/m-r/rollercoaster-tycoon-deluxe.md)
- [`GAME-0390` — SimCity 2000](../games/s-z/simcity-2000.md)
- [`GAME-0118` — SimCity 4 Deluxe Edition](../games/s-z/simcity-4-deluxe-edition.md)
- [`GAME-0287` — Stellaris](../games/s-z/stellaris.md)
- [`GAME-0136` — "Surviving Mars: Relaunched"](../games/s-z/surviving-mars.md)
- [`GAME-0529` — Tetris Effect](../games/s-z/tetris-effect.md)
- [`GAME-0004` — Tetris](../games/s-z/tetris.md)
- [`GAME-0370` — Theme Hospital](../games/s-z/theme-hospital.md)
- [`GAME-0133` — Timberborn](../games/s-z/timberborn.md)
- [`GAME-0030` — Tin Hearts](../games/s-z/tin-hearts.md)
- [`GAME-0498` — Transport Fever 2](../games/s-z/transport-fever-2.md)
- [`GAME-0134` — "Workers & Resources: Soviet Republic"](../games/s-z/workers-resources-soviet-republic.md)

## ACT-007

- Назва: Призначити символ редагованій позиції
- Переглянуто: `2026-08-24`

### Операційне визначення

Гравець обирає одну позицію, якій зараз можна призначити значення, і записує один символ із дозволеної множини значень як запропоноване значення цієї позиції.

### Включає

Внесення цифри від 1 до 9 у порожню клітинку Sudoku; позначення клітинки Nonogram як заповненої або підтверджено порожньої; натискання редагованої клітинки Hexologic, щоб призначити чи замінити її запропоноване значення з однієї, двох або трьох цяток; призначення символу / або зворотної скісної риски одній клітинці Slant; установлення чи вилучення лампи в одній білій клітинці Light Up; призначення одного з чотирьох кольорів палітри одній редагованій області Map; призначення цифри від 1 до 9 одній редагованій клітинці Filling; призначення цифри від 1 до 6 одній клітинці Keen; установлення намету або явної позначки відсутності намету в одній редагованій клітинці Tents.

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
- [`GAME-0685` — "Squeakross: Home Squeak Home"](../games/s-z/squeakross-home-squeak-home.md)
- [`GAME-0005` — Sudoku](../games/s-z/sudoku.md)
- [`GAME-0072` — Tents](../games/s-z/tents.md)

## ACT-008

- Назва: Безпосередньо пересувати керованого учасника
- Переглянуто: `2026-10-03`

### Операційне визначення

Гравець безпосередньо пересуває одного постійного керованого учасника крізь прохідну геометрію рівня за місцевими командами руху, а не обирає віддалене призначення для автоматичного пошуку шляху.

### Включає

Переміщення комірника на одну ортогональну клітинку підлоги в Sokoban без руху ящика; біг і стрибки сіба-іну в HUMANITY крізь випробування до позицій командування; ходіння й стрибки Chell камерою Portal і Tim рівнем Braid; навігація активним Rescue Officer або Oatchi поверхнею Pikmin 4; ходіння між сполученими кімнатами, обраними з планів поточного маєтку Blue Prince; переміщення Patrick на одну кардинально сусідню локальну клітинку вкладеного простору Patrick’s Parabox; ходіння й стрибки активним тілом у кімнаті The Swapper; ходіння Carto поточним з’єднаним ландшафтом фрагментів мапи; ходіння й стрибки поточною тривимірною геометрією Viewfinder; переміщення чудовиська на одну кардинально сусідню клітинку саду в A Good Snowman Is Hard to Build; просування голови Snakebird на одну кардинально сусідню клітинку з автоматичним слідуванням тіла; просування будь-якого поточного кінця Can of Wormholes на одну кардинально сусідню клітинку; ходіння чудовиськом A Monster’s Expedition суходолом або завершеним мостом із колоди; ходіння й стрибки сновидцем Superliminal кімнатою Induction та її відкритим виходом; ходіння, стрибки й керування падінням періодичною архітектурою Part 1 у Manifold Garden; ходіння між центральною моделлю Maquette, пов’язаними масштабом подвір’ями, мостами для ключа та фіксованим виходом із будинку; біг, біг підтюпцем і ведення м’яча поточним керованим футболістом полем EA SPORTS FC 26; ходіння, присідання, стрибки й ривки Ryu в обмеженій арені Versus Street Fighter 6; ходіння, прискорений біг, стрибки й присідання Ві в Найт-Сіті та створених для завдань локаціях Cyberpunk 2077; безпосереднє переміщення й стрибки обраним героєм Marvel Rivals живою ареною; біг і стрибки Hornet сполученими кімнатами Pharloom у Hollow Knight: Silksong; біг, стрибки, ривки, плавання й пересування гаком Mio або Zoe розділом Rader Publishing у Split Fiction; ходіння тренером через Pallet Town, Route 1, Viridian Forest і Pewter Gym у Pokémon Red Version.

### Виключає

Зміну ракурсу; переміщення сусіднього об’єкта; телепортацію або пошук шляху, що автоматично виконує кілька кроків.

### Ігри-носії

- [`GAME-0635` — "1000xRESIST"](../games/0-9/1000xresist.md)
- [`GAME-0233` — 7 Days to Die](../games/0-9/7-days-to-die.md)
- [`GAME-0694` — "A Game About Digging A Hole"](../games/a-f/a-game-about-digging-a-hole.md)
- [`GAME-0044` — A Good Snowman Is Hard to Build](../games/a-f/a-good-snowman-is-hard-to-build.md)
- [`GAME-0718` — "A Highland Song"](../games/a-f/a-highland-song.md)
- [`GAME-0054` — A Monster’s Expedition](../games/a-f/a-monsters-expedition.md)
- [`GAME-0653` — "A Quiet Place: The Road Ahead"](../games/a-f/a-quiet-place-the-road-ahead.md)
- [`GAME-0228` — A Way Out](../games/a-f/a-way-out.md)
- [`GAME-0540` — Afterplace](../games/a-f/afterplace.md)
- [`GAME-0223` — Aion Classic](../games/a-f/aion-classic.md)
- [`GAME-0427` — Alan Wake](../games/a-f/alan-wake.md)
- [`GAME-0257` — "Alien: Isolation"](../games/a-f/alien-isolation.md)
- [`GAME-0620` — Alien Soldier](../games/a-f/alien-soldier.md)
- [`GAME-0719` — "Alisia Dragoon"](../games/a-f/alisia-dragoon.md)
- [`GAME-0456` — Alone in the Dark](../games/a-f/alone-in-the-dark.md)
- [`GAME-0320` — "Animal Crossing: New Horizons"](../games/a-f/animal-crossing-new-horizons.md)
- [`GAME-0511` — Animal Crossing: New Leaf](../games/a-f/animal-crossing-new-leaf.md)
- [`GAME-0520` — Animal Well](../games/a-f/animal-well.md)
- [`GAME-0097` — Antichamber](../games/a-f/antichamber.md)
- [`GAME-0413` — Ape Escape](../games/a-f/ape-escape.md)
- [`GAME-0154` — Apex Legends](../games/a-f/apex-legends.md)
- [`GAME-0143` — ARC Raiders](../games/a-f/arc-raiders.md)
- [`GAME-0312` — ASTRO BOT](../games/a-f/astro-bot.md)
- [`GAME-0506` — Avowed](../games/a-f/avowed.md)
- [`GAME-0709` — "Baby Steps"](../games/a-f/baby-steps.md)
- [`GAME-0148` — Baldur’s Gate 3](../games/a-f/baldurs-gate-3.md)
- [`GAME-0610` — "BALL x PIT"](../games/a-f/ball-x-pit.md)
- [`GAME-0386` — Banjo-Kazooie](../games/a-f/banjo-kazooie.md)
- [`GAME-0255` — "Batman: Arkham Asylum Game of the Year Edition"](../games/a-f/batman-arkham-asylum-game-of-the-year-edition.md)
- [`GAME-0662` — "Batman: Arkham Shadow"](../games/a-f/batman-arkham-shadow.md)
- [`GAME-0234` — Battlefield 2042](../games/a-f/battlefield-2042.md)
- [`GAME-0149` — Battlefield 6](../games/a-f/battlefield-6.md)
- [`GAME-0243` — Battlefield Hardline](../games/a-f/battlefield-hardline.md)
- [`GAME-0220` — Battlefield V](../games/a-f/battlefield-v.md)
- [`GAME-0318` — Battletoads](../games/a-f/battletoads.md)
- [`GAME-0594` — "Bionic Bay"](../games/a-f/bionic-bay.md)
- [`GAME-0256` — "BioShock™ Remastered"](../games/a-f/bioshock-remastered.md)
- [`GAME-0189` — "Black Myth: Wukong"](../games/a-f/black-myth-wukong.md)
- [`GAME-0539` — Blast Corps](../games/a-f/blast-corps.md)
- [`GAME-0308` — Bloodborne™](../games/a-f/bloodborne.md)
- [`GAME-0173` — Blue Prince](../games/a-f/blue-prince.md)
- [`GAME-0557` — "Boktai: The Sun Is in Your Hand"](../games/a-f/boktai-the-sun-is-in-your-hand.md)
- [`GAME-0736` — "Bomb Rush Cyberfunk"](../games/a-f/bomb-rush-cyberfunk.md)
- [`GAME-0055` — Bonfire Peaks](../games/a-f/bonfire-peaks.md)
- [`GAME-0034` — Braid, Anniversary Edition](../games/a-f/braid.md)
- [`GAME-0198` — Brawlhalla](../games/a-f/brawlhalla.md)
- [`GAME-0546` — Burning Rangers](../games/a-f/burning-rangers.md)
- [`GAME-0641` — "Bushido Blade"](../games/a-f/bushido-blade.md)
- [`GAME-0646` — Cairn](../games/a-f/cairn.md)
- [`GAME-0222` — "Call of Juarez: Gunslinger"](../games/a-f/call-of-juarez-gunslinger.md)
- [`GAME-0053` — Can of Wormholes](../games/a-f/can-of-wormholes.md)
- [`GAME-0302` — "Captain Toad: Treasure Tracker"](../games/a-f/captain-toad-treasure-tracker.md)
- [`GAME-0040` — Carto](../games/a-f/carto.md)
- [`GAME-0601` — "Cassette Beasts"](../games/a-f/cassette-beasts.md)
- [`GAME-0347` — "Castlevania: Symphony of the Night"](../games/a-f/castlevania-symphony-of-the-night.md)
- [`GAME-0477` — Catherine](../games/a-f/catherine.md)
- [`GAME-0555` — Chibi-Robo!](../games/a-f/chibi-robo.md)
- [`GAME-0666` — "Chicory: A Colorful Tale"](../games/a-f/chicory-a-colorful-tale.md)
- [`GAME-0346` — Chrono Trigger](../games/a-f/chrono-trigger.md)
- [`GAME-0144` — Clair Obscur: Expedition 33](../games/a-f/clair-obscur-expedition-33.md)
- [`GAME-0108` — Cocoon](../games/a-f/cocoon.md)
- [`GAME-0490` — Comix Zone](../games/a-f/comix-zone.md)
- [`GAME-0324` — Contra Force](../games/a-f/contra-force.md)
- [`GAME-0705` — "Contraband Police"](../games/a-f/contraband-police.md)
- [`GAME-0254` — CONTROL Ultimate Edition](../games/a-f/control-ultimate-edition.md)
- [`GAME-0137` — Counter-Strike 2](../games/a-f/counter-strike-2.md)
- [`GAME-0218` — Counter-Strike](../games/a-f/counter-strike.md)
- [`GAME-0326` — Crash Bandicoot](../games/a-f/crash-bandicoot.md)
- [`GAME-0725` — "Crypt Custodian"](../games/a-f/crypt-custodian.md)
- [`GAME-0246` — Crysis Remastered](../games/a-f/crysis-remastered.md)
- [`GAME-0570` — Cult of the Lamb](../games/a-f/cult-of-the-lamb.md)
- [`GAME-0277` — Cuphead](../games/a-f/cuphead.md)
- [`GAME-0596` — "Custom Robo"](../games/a-f/custom-robo.md)
- [`GAME-0146` — Cyberpunk 2077](../games/a-f/cyberpunk-2077.md)
- [`GAME-0629` — "Dark Cloud"](../games/a-f/dark-cloud.md)
- [`GAME-0262` — DARK SOULS™ III](../games/a-f/dark-souls-iii.md)
- [`GAME-0295` — DARK SOULS™: REMASTERED](../games/a-f/dark-souls-remastered.md)
- [`GAME-0281` — Darkest Dungeon](../games/a-f/darkest-dungeon.md)
- [`GAME-0278` — DAVE THE DIVER](../games/a-f/dave-the-diver.md)
- [`GAME-0459` — Daxter](../games/a-f/daxter.md)
- [`GAME-0210` — DayZ](../games/a-f/dayz.md)
- [`GAME-0161` — Dead by Daylight](../games/a-f/dead-by-daylight.md)
- [`GAME-0282` — Dead Cells](../games/a-f/dead-cells.md)
- [`GAME-0494` — Dead or Alive 2](../games/a-f/dead-or-alive-2.md)
- [`GAME-0368` — Dead Rising](../games/a-f/dead-rising.md)
- [`GAME-0259` — "Dead Space (2023 remake)"](../games/a-f/dead-space-2023.md)
- [`GAME-0310` — "DEATH STRANDING DIRECTOR’S CUT"](../games/a-f/death-stranding-directors-cut.md)
- [`GAME-0266` — Deep Rock Galactic](../games/a-f/deep-rock-galactic.md)
- [`GAME-0200` — Delta Force](../games/a-f/delta-force.md)
- [`GAME-0631` — "despelote"](../games/a-f/despelote.md)
- [`GAME-0193` — Destiny 2](../games/a-f/destiny-2.md)
- [`GAME-0252` — "Detroit: Become Human"](../games/a-f/detroit-become-human.md)
- [`GAME-0353` — "Deus Ex: Game of the Year Edition"](../games/a-f/deus-ex-game-of-the-year-edition.md)
- [`GAME-0322` — "Diablo II: Resurrected"](../games/a-f/diablo-ii-resurrected.md)
- [`GAME-0515` — Dino Crisis](../games/a-f/dino-crisis.md)
- [`GAME-0247` — Dishonored (2012)](../games/a-f/dishonored-2012.md)
- [`GAME-0545` — Dispatch](../games/a-f/dispatch.md)
- [`GAME-0565` — Dome Keeper](../games/a-f/dome-keeper.md)
- [`GAME-0619` — Donkey Kong Bananza](../games/a-f/donkey-kong-bananza.md)
- [`GAME-0495` — Donkey Kong Country Returns](../games/a-f/donkey-kong-country-returns.md)
- [`GAME-0329` — "Donkey Kong Country"](../games/a-f/donkey-kong-country.md)
- [`GAME-0186` — "Don’t Starve Together"](../games/a-f/dont-starve-together.md)
- [`GAME-0352` — DOOM (1993)](../games/a-f/doom-1993.md)
- [`GAME-0245` — DOOM (2016)](../games/a-f/doom-2016.md)
- [`GAME-0286` — DOOM Eternal](../games/a-f/doom-eternal.md)
- [`GAME-0608` — "Dosa Divas"](../games/a-f/dosa-divas.md)
- [`GAME-0269` — DREDGE](../games/a-f/dredge.md)
- [`GAME-0597` — "Duck Detective: The Ghost of Glamping"](../games/a-f/duck-detective-the-ghost-of-glamping.md)
- [`GAME-0699` — "Dungeon Master"](../games/a-f/dungeon-master.md)
- [`GAME-0592` — Dungeons of Hinterberg](../games/a-f/dungeons-of-hinterberg.md)
- [`GAME-0131` — Dyson Sphere Program](../games/a-f/dyson-sphere-program.md)
- [`GAME-0163` — EA SPORTS FC 26](../games/a-f/ea-sports-fc-26.md)
- [`GAME-0435` — EarthBound](../games/a-f/earthbound.md)
- [`GAME-0656` — "Ecco the Dolphin: Defender of the Future"](../games/a-f/ecco-the-dolphin-defender-of-the-future.md)
- [`GAME-0433` — Ecco the Dolphin](../games/a-f/ecco-the-dolphin.md)
- [`GAME-0152` — Elden Ring](../games/a-f/elden-ring.md)
- [`GAME-0491` — Elite](../games/a-f/elite.md)
- [`GAME-0702` — "Escaping Wonderland"](../games/a-f/escaping-wonderland.md)
- [`GAME-0473` — "Eternal Darkness: Sanity's Requiem"](../games/a-f/eternal-darkness-sanitys-requiem.md)
- [`GAME-0405` — Fable II](../games/a-f/fable-ii.md)
- [`GAME-0327` — Fable](../games/a-f/fable.md)
- [`GAME-0231` — Fallout 4](../games/a-f/fallout-4.md)
- [`GAME-0361` — Fallout: New Vegas](../games/a-f/fallout-new-vegas.md)
- [`GAME-0236` — Far Cry 3](../games/a-f/far-cry-3.md)
- [`GAME-0271` — Far Cry 5](../games/a-f/far-cry-5.md)
- [`GAME-0591` — Fatal Frame](../games/a-f/fatal-frame.md)
- [`GAME-0501` — F.E.A.R.](../games/a-f/fear.md)
- [`GAME-0091` — Fez](../games/a-f/fez.md)
- [`GAME-0338` — Final Fantasy VII](../games/a-f/final-fantasy-vii.md)
- [`GAME-0188` — FINAL FANTASY XIV Online](../games/a-f/final-fantasy-xiv-online.md)
- [`GAME-0713` — "Firestriker"](../games/a-f/firestriker.md)
- [`GAME-0633` — "Flock"](../games/a-f/flock.md)
- [`GAME-0227` — Fortnite](../games/a-f/fortnite.md)
- [`GAME-0724` — "Frequency"](../games/a-f/frequency.md)
- [`GAME-0321` — Gears of War](../games/g-l/gears-of-war.md)
- [`GAME-0400` — "Geometry Wars: Retro Evolved"](../games/g-l/geometry-wars-retro-evolved.md)
- [`GAME-0550` — Ghost of Yōtei](../games/g-l/ghost-of-yotei.md)
- [`GAME-0263` — God of War](../games/g-l/god-of-war.md)
- [`GAME-0381` — GoldenEye 007](../games/g-l/goldeneye-007.md)
- [`GAME-0357` — "Grand Theft Auto: San Andreas"](../games/g-l/grand-theft-auto-san-andreas.md)
- [`GAME-0145` — Grand Theft Auto V](../games/g-l/grand-theft-auto-v.md)
- [`GAME-0468` — Gravity Rush](../games/g-l/gravity-rush.md)
- [`GAME-0582` — Grim Fandango](../games/g-l/grim-fandango.md)
- [`GAME-0314` — Grounded](../games/g-l/grounded.md)
- [`GAME-0560` — Gunstar Heroes](../games/g-l/gunstar-heroes.md)
- [`GAME-0532` — Hades II](../games/g-l/hades-ii.md)
- [`GAME-0251` — Hades](../games/g-l/hades.md)
- [`GAME-0239` — Half-Life (1998)](../games/g-l/half-life-1998.md)
- [`GAME-0212` — Half-Life 2](../games/g-l/half-life-2.md)
- [`GAME-0315` — Halo 3](../games/g-l/halo-3.md)
- [`GAME-0340` — "Halo: Combat Evolved Anniversary"](../games/g-l/halo-combat-evolved-anniversary.md)
- [`GAME-0581` — "Hardspace: Shipbreaker"](../games/g-l/hardspace-shipbreaker.md)
- [`GAME-0444` — "Harvest Moon: Back to Nature"](../games/g-l/harvest-moon-back-to-nature.md)
- [`GAME-0159` — Helldivers 2](../games/g-l/helldivers-2.md)
- [`GAME-0516` — Hi-Fi RUSH](../games/g-l/hi-fi-rush.md)
- [`GAME-0248` — HITMAN World of Assassination](../games/g-l/hitman-world-of-assassination.md)
- [`GAME-0150` — "Hollow Knight: Silksong"](../games/g-l/hollow-knight-silksong.md)
- [`GAME-0274` — Hollow Knight](../games/g-l/hollow-knight.md)
- [`GAME-0654` — "Hotel Dusk: Room 215"](../games/g-l/hotel-dusk-room-215.md)
- [`GAME-0112` — Human: Fall Flat](../games/g-l/human-fall-flat.md)
- [`GAME-0029` — HUMANITY](../games/g-l/humanity.md)
- [`GAME-0098` — Hyperbolica](../games/g-l/hyperbolica.md)
- [`GAME-0099` — HyperRogue](../games/g-l/hyperrogue.md)
- [`GAME-0399` — Ico](../games/g-l/ico.md)
- [`GAME-0484` — Impossible Mission](../games/g-l/impossible-mission.md)
- [`GAME-0510` — Indiana Jones and the Great Circle](../games/g-l/indiana-jones-and-the-great-circle.md)
- [`GAME-0585` — Into the Radius](../games/g-l/into-the-radius.md)
- [`GAME-0215` — It Takes Two](../games/g-l/it-takes-two.md)
- [`GAME-0464` — "Jet Set Radio Future"](../games/g-l/jet-set-radio-future.md)
- [`GAME-0350` — "Jet Set Radio"](../games/g-l/jet-set-radio.md)
- [`GAME-0436` — Journey](../games/g-l/journey.md)
- [`GAME-0552` — Jusant](../games/g-l/jusant.md)
- [`GAME-0376` — Katamari Damacy REROLL](../games/g-l/katamari-damacy-reroll.md)
- [`GAME-0720` — "Kaze and the Wild Masks"](../games/g-l/kaze-and-the-wild-masks.md)
- [`GAME-0543` — Keeper](../games/g-l/keeper.md)
- [`GAME-0240` — "Kingdom Come: Deliverance II"](../games/g-l/kingdom-come-deliverance-ii.md)
- [`GAME-0655` — "Kirby Air Riders"](../games/g-l/kirby-air-riders.md)
- [`GAME-0408` — Kirby's Adventure](../games/g-l/kirbys-adventure.md)
- [`GAME-0692` — "Klonoa 2: Lunatea's Veil"](../games/g-l/klonoa-2-lunateas-veil.md)
- [`GAME-0706` — "Kula World"](../games/g-l/kula-world.md)
- [`GAME-0583` — "Kunitsu-Gami: Path of the Goddess"](../games/g-l/kunitsu-gami-path-of-the-goddess.md)
- [`GAME-0609` — "Kuru Kuru Kururin"](../games/g-l/kuru-kuru-kururin.md)
- [`GAME-0388` — L.A. Noire](../games/g-l/la-noire.md)
- [`GAME-0683` — "Last Window: The Secret of Cape West"](../games/g-l/last-window-the-secret-of-cape-west.md)
- [`GAME-0192` — Left 4 Dead 2](../games/g-l/left-4-dead-2.md)
- [`GAME-0290` — Lies of P](../games/g-l/lies-of-p.md)
- [`GAME-0219` — Lineage II](../games/g-l/lineage-ii.md)
- [`GAME-0394` — LittleBigPlanet 2](../games/g-l/littlebigplanet-2.md)
- [`GAME-0569` — Lode Runner](../games/g-l/lode-runner.md)
- [`GAME-0563` — Lorelei and the Laser Eyes](../games/g-l/lorelei-and-the-laser-eyes.md)
- [`GAME-0403` — "Luigi's Mansion"](../games/g-l/luigis-mansion.md)
- [`GAME-0214` — "Mafia (2002)"](../games/m-r/mafia-2002.md)
- [`GAME-0095` — Manifold Garden](../games/m-r/manifold-garden.md)
- [`GAME-0096` — Maquette](../games/m-r/maquette.md)
- [`GAME-0147` — Marvel Rivals](../games/m-r/marvel-rivals.md)
- [`GAME-0323` — "Marvel’s Spider-Man 2"](../games/m-r/marvels-spider-man-2.md)
- [`GAME-0367` — Mass Effect 2 (Legendary Edition)](../games/m-r/mass-effect-2-legendary-edition.md)
- [`GAME-0238` — "Max Payne (2001)"](../games/m-r/max-payne-2001.md)
- [`GAME-0273` — Max Payne 3](../games/m-r/max-payne-3.md)
- [`GAME-0509` — MechAssault](../games/m-r/mechassault.md)
- [`GAME-0389` — Mega Man 2](../games/m-r/mega-man-2.md)
- [`GAME-0652` — Mega Man Battle Network](../games/m-r/mega-man-battle-network.md)
- [`GAME-0306` — METAL GEAR SOLID V: THE PHANTOM PAIN](../games/m-r/metal-gear-solid-v-the-phantom-pain.md)
- [`GAME-0339` — Metal Gear Solid](../games/m-r/metal-gear-solid.md)
- [`GAME-0462` — Metal Slug 3](../games/m-r/metal-slug-3.md)
- [`GAME-0728` — "Metal Warriors"](../games/m-r/metal-warriors.md)
- [`GAME-0260` — Metro Exodus](../games/m-r/metro-exodus.md)
- [`GAME-0474` — Metroid Fusion](../games/m-r/metroid-fusion.md)
- [`GAME-0678` — "Metroid Prime 4: Beyond"](../games/m-r/metroid-prime-4-beyond.md)
- [`GAME-0355` — Metroid Prime](../games/m-r/metroid-prime.md)
- [`GAME-0129` — Minecraft](../games/m-r/minecraft.md)
- [`GAME-0607` — "Mischief Makers"](../games/m-r/mischief-makers.md)
- [`GAME-0676` — "Mixtape"](../games/m-r/mixtape.md)
- [`GAME-0614` — "Mole Mania"](../games/m-r/mole-mania.md)
- [`GAME-0297` — 'MONSTER HUNTER RISE'](../games/m-r/monster-hunter-rise.md)
- [`GAME-0151` — Monster Hunter Wilds](../games/m-r/monster-hunter-wilds.md)
- [`GAME-0207` — 'Monster Hunter: World'](../games/m-r/monster-hunter-world.md)
- [`GAME-0393` — Mortal Kombat II](../games/m-r/mortal-kombat-ii.md)
- [`GAME-0558` — Moss](../games/m-r/moss.md)
- [`GAME-0194` — "Mount & Blade II: Bannerlord"](../games/m-r/mount-and-blade-ii-bannerlord.md)
- [`GAME-0111` — Myst](../games/m-r/myst.md)
- [`GAME-0202` — "NARAKA: BLADEPOINT"](../games/m-r/naraka-bladepoint.md)
- [`GAME-0241` — NBA 2K26](../games/m-r/nba-2k26.md)
- [`GAME-0600` — "NBA Street Vol. 2"](../games/m-r/nba-street-vol-2.md)
- [`GAME-0572` — Neon White](../games/m-r/neon-white.md)
- [`GAME-0588` — Neva](../games/m-r/neva.md)
- [`GAME-0734` — "Nex Machina"](../games/m-r/nex-machina.md)
- [`GAME-0445` — "NiGHTS into Dreams"](../games/m-r/nights-into-dreams.md)
- [`GAME-0527` — Nine Sols](../games/m-r/nine-sols.md)
- [`GAME-0341` — "Ninja Gaiden Black"](../games/m-r/ninja-gaiden-black.md)
- [`GAME-0625` — "Ninja Gaiden Dragon Sword"](../games/m-r/ninja-gaiden-dragon-sword.md)
- [`GAME-0299` — Nioh 2](../games/m-r/nioh-2.md)
- [`GAME-0229` — "No Man’s Sky"](../games/m-r/no-mans-sky.md)
- [`GAME-0296` — Noita](../games/m-r/noita.md)
- [`GAME-0483` — "Oddworld: Stranger's Wrath"](../games/m-r/oddworld-strangers-wrath.md)
- [`GAME-0382` — Ōkami HD](../games/m-r/okami-hd.md)
- [`GAME-0224` — Once Human](../games/m-r/once-human.md)
- [`GAME-0117` — OneShot](../games/m-r/oneshot.md)
- [`GAME-0431` — Ori and the Blind Forest](../games/m-r/ori-and-the-blind-forest.md)
- [`GAME-0293` — Ori and the Will of the Wisps](../games/m-r/ori-and-the-will-of-the-wisps.md)
- [`GAME-0105` — Outer Wilds](../games/m-r/outer-wilds.md)
- [`GAME-0605` — "Outtrigger"](../games/m-r/outtrigger.md)
- [`GAME-0300` — Overcooked! 2](../games/m-r/overcooked-2.md)
- [`GAME-0181` — Overwatch](../games/m-r/overwatch.md)
- [`GAME-0342` — "PAC-MAN"](../games/m-r/pac-man.md)
- [`GAME-0500` — Pacific Drive](../games/m-r/pacific-drive.md)
- [`GAME-0139` — Palworld](../games/m-r/palworld.md)
- [`GAME-0647` — Panzer Dragoon Saga](../games/m-r/panzer-dragoon-saga.md)
- [`GAME-0624` — "Paradise Killer"](../games/m-r/paradise-killer.md)
- [`GAME-0562` — Parasite Eve](../games/m-r/parasite-eve.md)
- [`GAME-0703` — "Part Time UFO"](../games/m-r/part-time-ufo.md)
- [`GAME-0162` — Path of Exile 2](../games/m-r/path-of-exile-2.md)
- [`GAME-0036` — "Patrick’s Parabox"](../games/m-r/patricks-parabox.md)
- [`GAME-0201` — PAYDAY 2](../games/m-r/payday-2.md)
- [`GAME-0232` — PAYDAY 3](../games/m-r/payday-3.md)
- [`GAME-0203` — "PEAK"](../games/m-r/peak.md)
- [`GAME-0731` — "Pengo"](../games/m-r/pengo.md)
- [`GAME-0523` — Pentiment](../games/m-r/pentiment.md)
- [`GAME-0622` — "Pepper Grinder"](../games/m-r/pepper-grinder.md)
- [`GAME-0291` — Persona 5 Royal](../games/m-r/persona-5-royal.md)
- [`GAME-0670` — "Phantom Dust"](../games/m-r/phantom-dust.md)
- [`GAME-0035` — Pikmin 4](../games/m-r/pikmin-4.md)
- [`GAME-0602` — "Pilotwings 64"](../games/m-r/pilotwings-64.md)
- [`GAME-0661` — "Pilotwings"](../games/m-r/pilotwings.md)
- [`GAME-0612` — "Pipistrello and the Cursed Yoyo"](../games/m-r/pipistrello-and-the-cursed-yoyo.md)
- [`GAME-0479` — Pitfall!](../games/m-r/pitfall.md)
- [`GAME-0640` — "Pizza Tower"](../games/m-r/pizza-tower.md)
- [`GAME-0700` — "Planet of Lana II: Children of the Leaf"](../games/m-r/planet-of-lana-ii.md)
- [`GAME-0463` — "Pokémon Gold Version"](../games/m-r/pokemon-gold-version.md)
- [`GAME-0160` — "Pokémon Legends: Z-A"](../games/m-r/pokemon-legends-z-a.md)
- [`GAME-0518` — Pokémon Pokopia](../games/m-r/pokemon-pokopia.md)
- [`GAME-0336` — "Pokémon Red Version"](../games/m-r/pokemon-red-version.md)
- [`GAME-0113` — Portal 2 — Cooperative Campaign](../games/m-r/portal-2-co-op.md)
- [`GAME-0033` — Portal](../games/m-r/portal.md)
- [`GAME-0681` — "Power Stone 2"](../games/m-r/power-stone-2.md)
- [`GAME-0519` — Power Stone](../games/m-r/power-stone.md)
- [`GAME-0534` — PowerWash Simulator 2](../games/m-r/powerwash-simulator-2.md)
- [`GAME-0279` — PowerWash Simulator](../games/m-r/powerwash-simulator.md)
- [`GAME-0536` — PRAGMATA](../games/m-r/pragmata.md)
- [`GAME-0258` — "Prey (2017)"](../games/m-r/prey-2017.md)
- [`GAME-0344` — "Prince of Persia: The Sands of Time"](../games/m-r/prince-of-persia-the-sands-of-time.md)
- [`GAME-0142` — Project Zomboid](../games/m-r/project-zomboid.md)
- [`GAME-0561` — Psychonauts 2](../games/m-r/psychonauts-2.md)
- [`GAME-0358` — Psychonauts](../games/m-r/psychonauts.md)
- [`GAME-0140` — "PUBG: BATTLEGROUNDS"](../games/m-r/pubg-battlegrounds.md)
- [`GAME-0737` — "Pullblox"](../games/m-r/pullblox.md)
- [`GAME-0715` — "Pushover"](../games/m-r/pushover.md)
- [`GAME-0438` — Q*bert](../games/m-r/qbert.md)
- [`GAME-0722` — "QuackShot Starring Donald Duck"](../games/m-r/quackshot-starring-donald-duck.md)
- [`GAME-0334` — Quake](../games/m-r/quake.md)
- [`GAME-0404` — Ratchet & Clank](../games/m-r/ratchet-and-clank.md)
- [`GAME-0508` — Ready or Not](../games/m-r/ready-or-not.md)
- [`GAME-0684` — "REANIMAL"](../games/m-r/reanimal.md)
- [`GAME-0165` — Red Dead Redemption 2](../games/m-r/red-dead-redemption-2.md)
- [`GAME-0691` — "REPLACED"](../games/m-r/replaced.md)
- [`GAME-0280` — Resident Evil 2 (2019 remake)](../games/m-r/resident-evil-2-2019.md)
- [`GAME-0249` — Resident Evil 4 (2023 remake)](../games/m-r/resident-evil-4-2023.md)
- [`GAME-0348` — "Resident Evil: Director’s Cut"](../games/m-r/resident-evil-directors-cut.md)
- [`GAME-0512` — Resident Evil Requiem](../games/m-r/resident-evil-requiem.md)
- [`GAME-0492` — "Resistance: Fall of Man"](../games/m-r/resistance-fall-of-man.md)
- [`GAME-0522` — Returnal](../games/m-r/returnal.md)
- [`GAME-0270` — Risk of Rain 2](../games/m-r/risk-of-rain-2.md)
- [`GAME-0659` — "Ristar"](../games/m-r/ristar.md)
- [`GAME-0643` — "Rocket Knight Adventures"](../games/m-r/rocket-knight-adventures.md)
- [`GAME-0549` — Roto Force](../games/m-r/roto-force.md)
- [`GAME-0141` — Rust](../games/m-r/rust.md)
- [`GAME-0667` — "SAROS"](../games/s-z/saros.md)
- [`GAME-0584` — Saturn Bomberman](../games/s-z/saturn-bomberman.md)
- [`GAME-0556` — Sayonara Wild Hearts](../games/s-z/sayonara-wild-hearts.md)
- [`GAME-0440` — Scribblenauts](../games/s-z/scribblenauts.md)
- [`GAME-0319` — Sea of Thieves](../games/s-z/sea-of-thieves.md)
- [`GAME-0665` — "Sega Worldwide Soccer '97"](../games/s-z/sega-worldwide-soccer-97.md)
- [`GAME-0288` — "Sekiro™: Shadows Die Twice - GOTY Edition"](../games/s-z/sekiro-shadows-die-twice.md)
- [`GAME-0272` — Serious Sam 4](../games/s-z/serious-sam-4.md)
- [`GAME-0237` — "Serious Sam HD: The First Encounter"](../games/s-z/serious-sam-hd-the-first-encounter.md)
- [`GAME-0356` — Shadow of the Colossus](../games/s-z/shadow-of-the-colossus.md)
- [`GAME-0485` — Shenmue](../games/s-z/shenmue.md)
- [`GAME-0050` — Shogun Showdown](../games/s-z/shogun-showdown.md)
- [`GAME-0487` — Sid Meier's Pirates!](../games/s-z/sid-meiers-pirates.md)
- [`GAME-0303` — Sifu](../games/s-z/sifu.md)
- [`GAME-0616` — Silent Bomber](../games/s-z/silent-bomber.md)
- [`GAME-0330` — Silent Hill 2 (2024 remake)](../games/s-z/silent-hill-2-2024.md)
- [`GAME-0430` — Silent Hill](../games/s-z/silent-hill.md)
- [`GAME-0615` — "Skate Story"](../games/s-z/skate-story.md)
- [`GAME-0307` — Slime Rancher](../games/s-z/slime-rancher.md)
- [`GAME-0417` — Sly Cooper and the Thievius Raccoonus](../games/s-z/sly-cooper-and-the-thievius-raccoonus.md)
- [`GAME-0045` — Snakebird](../games/s-z/snakebird.md)
- [`GAME-0006` — Sokoban](../games/s-z/sokoban.md)
- [`GAME-0733` — "Solomon's Key"](../games/s-z/solomons-key.md)
- [`GAME-0690` — "Sonic Advance"](../games/s-z/sonic-advance.md)
- [`GAME-0472` — Sonic Adventure](../games/s-z/sonic-adventure.md)
- [`GAME-0682` — "Sonic Dream Team"](../games/s-z/sonic-dream-team.md)
- [`GAME-0333` — "Sonic the Hedgehog"](../games/s-z/sonic-the-hedgehog.md)
- [`GAME-0305` — Sons Of The Forest](../games/s-z/sons-of-the-forest.md)
- [`GAME-0455` — Soulcalibur](../games/s-z/soulcalibur.md)
- [`GAME-0502` — South of Midnight](../games/s-z/south-of-midnight.md)
- [`GAME-0360` — "Space Invaders"](../games/s-z/space-invaders.md)
- [`GAME-0548` — Space Station Silicon Valley](../games/s-z/space-station-silicon-valley.md)
- [`GAME-0412` — Splatoon 3](../games/s-z/splatoon-3.md)
- [`GAME-0157` — Split Fiction](../games/s-z/split-fiction.md)
- [`GAME-0373` — Spore](../games/s-z/spore.md)
- [`GAME-0450` — SSX Tricky](../games/s-z/ssx-tricky.md)
- [`GAME-0170` — "S.T.A.L.K.E.R. 2: Heart of Chornobyl"](../games/s-z/stalker-2-heart-of-chornobyl.md)
- [`GAME-0230` — "STAR WARS Battlefront II (2017)"](../games/s-z/star-wars-battlefront-ii-2017.md)
- [`GAME-0213` — "STAR WARS Jedi: Fallen Order"](../games/s-z/star-wars-jedi-fallen-order.md)
- [`GAME-0331` — Starfield](../games/s-z/starfield.md)
- [`GAME-0043` — Stephen’s Sausage Roll](../games/s-z/stephens-sausage-roll.md)
- [`GAME-0172` — Street Fighter 6](../games/s-z/street-fighter-6.md)
- [`GAME-0351` — "Street Fighter II: The World Warrior"](../games/s-z/street-fighter-ii-the-world-warrior.md)
- [`GAME-0466` — Streets of Rage 2](../games/s-z/streets-of-rage-2.md)
- [`GAME-0178` — Subnautica](../games/s-z/subnautica.md)
- [`GAME-0387` — Super Bomberman](../games/s-z/super-bomberman.md)
- [`GAME-0460` — Super Mario 64](../games/s-z/super-mario-64.md)
- [`GAME-0311` — Super Mario Bros.](../games/s-z/super-mario-bros.md)
- [`GAME-0428` — Super Mario Maker](../games/s-z/super-mario-maker.md)
- [`GAME-0354` — Super Mario World](../games/s-z/super-mario-world.md)
- [`GAME-0337` — Super Metroid](../games/s-z/super-metroid.md)
- [`GAME-0094` — Superliminal](../games/s-z/superliminal.md)
- [`GAME-0599` — "Sword of the Sea"](../games/s-z/sword-of-the-sea.md)
- [`GAME-0313` — Tank 1990](../games/s-z/tank-1990.md)
- [`GAME-0187` — Team Fortress 2](../games/s-z/team-fortress-2.md)
- [`GAME-0426` — Tearaway](../games/s-z/tearaway.md)
- [`GAME-0568` — Teardown](../games/s-z/teardown.md)
- [`GAME-0366` — Tekken 3](../games/s-z/tekken-3.md)
- [`GAME-0283` — TEKKEN 8](../games/s-z/tekken-8.md)
- [`GAME-0695` — "Terranigma"](../games/s-z/terranigma.md)
- [`GAME-0153` — Terraria](../games/s-z/terraria.md)
- [`GAME-0648` — Thank Goodness You're Here!](../games/s-z/thank-goodness-youre-here.md)
- [`GAME-0604` — "The Alters"](../games/s-z/the-alters.md)
- [`GAME-0164` — "The Binding of Isaac: Rebirth"](../games/s-z/the-binding-of-isaac-rebirth.md)
- [`GAME-0636` — "The Dig"](../games/s-z/the-dig.md)
- [`GAME-0362` — "The Elder Scrolls III: Morrowind"](../games/s-z/the-elder-scrolls-iii-morrowind.md)
- [`GAME-0190` — "The Elder Scrolls V: Skyrim Special Edition"](../games/s-z/the-elder-scrolls-v-skyrim-special-edition.md)
- [`GAME-0292` — The Forest](../games/s-z/the-forest.md)
- [`GAME-0576` — The Forgotten City](../games/s-z/the-forgotten-city.md)
- [`GAME-0707` — "The Gunk"](../games/s-z/the-gunk.md)
- [`GAME-0729` — "The Last Campfire"](../games/s-z/the-last-campfire.md)
- [`GAME-0559` — The Last Guardian](../games/s-z/the-last-guardian.md)
- [`GAME-0261` — The Last of Us Part I](../games/s-z/the-last-of-us-part-i.md)
- [`GAME-0458` — The Legend of Zelda: Link's Awakening](../games/s-z/the-legend-of-zelda-links-awakening.md)
- [`GAME-0395` — "The Legend of Zelda: Majora’s Mask"](../games/s-z/the-legend-of-zelda-majoras-mask.md)
- [`GAME-0363` — "The Legend of Zelda: Ocarina of Time"](../games/s-z/the-legend-of-zelda-ocarina-of-time.md)
- [`GAME-0593` — "The Legend of Zelda: The Minish Cap"](../games/s-z/the-legend-of-zelda-the-minish-cap.md)
- [`GAME-0325` — The Legend of Zelda](../games/s-z/the-legend-of-zelda.md)
- [`GAME-0285` — "The Long Dark"](../games/s-z/the-long-dark.md)
- [`GAME-0553` — The Lost Vikings](../games/s-z/the-lost-vikings.md)
- [`GAME-0531` — The Midnight Walk](../games/s-z/the-midnight-walk.md)
- [`GAME-0528` — The Neverhood](../games/s-z/the-neverhood.md)
- [`GAME-0107` — The Pedestrian](../games/s-z/the-pedestrian.md)
- [`GAME-0651` — The Plucky Squire](../games/s-z/the-plucky-squire.md)
- [`GAME-0606` — "The Séance of Blake Manor"](../games/s-z/the-seance-of-blake-manor.md)
- [`GAME-0116` — The Stanley Parable: Ultra Deluxe](../games/s-z/the-stanley-parable-ultra-deluxe.md)
- [`GAME-0038` — The Swapper](../games/s-z/the-swapper.md)
- [`GAME-0090` — The Talos Principle](../games/s-z/the-talos-principle.md)
- [`GAME-0205` — "The Witcher 3: Wild Hunt"](../games/s-z/the-witcher-3-wild-hunt.md)
- [`GAME-0513` — Thief: The Dark Project](../games/s-z/thief-the-dark-project.md)
- [`GAME-0696` — "Tides of Tomorrow"](../games/s-z/tides-of-tomorrow.md)
- [`GAME-0253` — "Titanfall 2"](../games/s-z/titanfall-2.md)
- [`GAME-0732` — "TOEM"](../games/s-z/toem.md)
- [`GAME-0735` — "Toki Tori"](../games/s-z/toki-tori.md)
- [`GAME-0174` — Tom Clancy’s Rainbow Six Siege](../games/s-z/tom-clancys-rainbow-six-siege.md)
- [`GAME-0349` — "Tom Clancy’s Splinter Cell"](../games/s-z/tom-clancys-splinter-cell.md)
- [`GAME-0451` — Tomb Raider (1996)](../games/s-z/tomb-raider-1996.md)
- [`GAME-0250` — Tomb Raider (2013)](../games/s-z/tomb-raider-2013.md)
- [`GAME-0668` — "Tomba!"](../games/s-z/tomba.md)
- [`GAME-0365` — Tony Hawk’s Pro Skater 1 + 2](../games/s-z/tony-hawks-pro-skater-1-plus-2.md)
- [`GAME-0104` — TUNIC](../games/s-z/tunic.md)
- [`GAME-0391` — "Uncharted 2: Among Thieves"](../games/s-z/uncharted-2-among-thieves.md)
- [`GAME-0268` — Undertale](../games/s-z/undertale.md)
- [`GAME-0294` — V Rising](../games/s-z/v-rising.md)
- [`GAME-0499` — Vagrant Story](../games/s-z/vagrant-story.md)
- [`GAME-0197` — Valheim](../games/s-z/valheim.md)
- [`GAME-0183` — Vampire Survivors](../games/s-z/vampire-survivors.md)
- [`GAME-0041` — Viewfinder](../games/s-z/viewfinder.md)
- [`GAME-0580` — Viewtiful Joe](../games/s-z/viewtiful-joe.md)
- [`GAME-0571` — Virtua Tennis](../games/s-z/virtua-tennis.md)
- [`GAME-0693` — "Void Stranger"](../games/s-z/void-stranger.md)
- [`GAME-0168` — Warframe](../games/s-z/warframe.md)
- [`GAME-0496` — "Warhammer 40,000: Space Marine 2"](../games/s-z/warhammer-40000-space-marine-2.md)
- [`GAME-0645` — Wario Land 3](../games/s-z/wario-land-3.md)
- [`GAME-0497` — Wario Land 4](../games/s-z/wario-land-4.md)
- [`GAME-0644` — "WHAT THE CAR?"](../games/s-z/what-the-car.md)
- [`GAME-0603` — "Wheel World"](../games/s-z/wheel-world.md)
- [`GAME-0669` — "Wilmot Works It Out"](../games/s-z/wilmot-works-it-out.md)
- [`GAME-0564` — Windjammers](../games/s-z/windjammers.md)
- [`GAME-0221` — World of Warcraft](../games/s-z/world-of-warcraft.md)
- [`GAME-0379` — Worms Armageddon](../games/s-z/worms-armageddon.md)
- [`GAME-0671` — "Yoshi and the Mysterious Book"](../games/s-z/yoshi-and-the-mysterious-book.md)

## ACT-009

- Назва: Штовхання сусіднього рухомого об’єкта
- Переглянуто: `2026-08-24`

### Операційне визначення

Спрямовуючи керованого агента тілом або прикріпленим інструментом до одного сусіднього рухомого об’єкта, гравець зсуває цей об’єкт на одну логічну позицію від агента; агент або інструмент займає звільнений бік контакту.

### Включає

Штовхання одного ящика Sokoban на одну ортогональну клітинку; одного об’єкта з призначеною властивістю PUSH у Baba Is You; одного сусіднього ящика Patrick’s Parabox до допустимого локального або міжмежового місця призначення; однієї ковбаски прикріпленою виделкою в Stephen’s Sausage Roll; однієї снігової кулі A Good Snowman Is Hard to Build до порожньої клітинки або сумісного стосу; одного дерева чи колоди A Monster’s Expedition із сусіднього доступного боку перед залежним від напрямку розв’язанням.

### Виключає

Тягнення об’єкта; вибір і переміщення об’єкта незалежно від агента; автоматичну реакцію на зіткнення.

### Ігри-носії

- [`GAME-0044` — A Good Snowman Is Hard to Build](../games/a-f/a-good-snowman-is-hard-to-build.md)
- [`GAME-0054` — A Monster’s Expedition](../games/a-f/a-monsters-expedition.md)
- [`GAME-0456` — Alone in the Dark](../games/a-f/alone-in-the-dark.md)
- [`GAME-0013` — Baba Is You](../games/a-f/baba-is-you.md)
- [`GAME-0477` — Catherine](../games/a-f/catherine.md)
- [`GAME-0490` — Comix Zone](../games/a-f/comix-zone.md)
- [`GAME-0515` — Dino Crisis](../games/a-f/dino-crisis.md)
- [`GAME-0592` — Dungeons of Hinterberg](../games/a-f/dungeons-of-hinterberg.md)
- [`GAME-0614` — "Mole Mania"](../games/m-r/mole-mania.md)
- [`GAME-0036` — "Patrick’s Parabox"](../games/m-r/patricks-parabox.md)
- [`GAME-0006` — Sokoban](../games/s-z/sokoban.md)
- [`GAME-0043` — Stephen’s Sausage Roll](../games/s-z/stephens-sausage-roll.md)
- [`GAME-0458` — The Legend of Zelda: Link's Awakening](../games/s-z/the-legend-of-zelda-links-awakening.md)
- [`GAME-0593` — "The Legend of Zelda: The Minish Cap"](../games/s-z/the-legend-of-zelda-the-minish-cap.md)
- [`GAME-0499` — Vagrant Story](../games/s-z/vagrant-story.md)
- [`GAME-0669` — "Wilmot Works It Out"](../games/s-z/wilmot-works-it-out.md)

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

- [`GAME-0411` — Bejeweled 3](../games/a-f/bejeweled-3.md)
- [`GAME-0109` — Candy Crush Saga](../games/a-f/candy-crush-saga.md)
- [`GAME-0515` — Dino Crisis](../games/a-f/dino-crisis.md)
- [`GAME-0009` — Royal Match](../games/m-r/royal-match.md)

## ACT-012

- Назва: Активація або поєднання підсилювача на полі
- Переглянуто: `2026-08-24`

### Операційне визначення

Гравець безпосередньо запускає один постійний спеціальний елемент поля або міняє місцями два сумісні спеціальні елементи, щоб запустити поєднаний ефект.

### Включає

Натискання або обмін Rocket, TNT, Propeller чи Light Ball у Royal Match, а також обмін двох підсилювачів між собою.

### Виключає

Автоматичне створення підсилювача зі збігу; вибір бустера перед рівнем; область очищення, яку система розв’язує після активації.

### Ігри-носії

- [`GAME-0411` — Bejeweled 3](../games/a-f/bejeweled-3.md)
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

Переміщення фігури під контролем суперника; автоматичну відповідь суперника; вибір типу фігури для перетворення пішака; напрямлену навігацію постійно керованим агентом лише до сусідньої позиції (ACT-008).

### Ігри-носії

- [`GAME-0416` — Advance Wars](../games/a-f/advance-wars.md)
- [`GAME-0027` — Bad North: Jotunn Edition](../games/a-f/bad-north.md)
- [`GAME-0011` — Chess](../games/a-f/chess.md)
- [`GAME-0711` — "ELOH"](../games/a-f/eloh.md)
- [`GAME-0486` — Final Fantasy Tactics](../games/a-f/final-fantasy-tactics.md)
- [`GAME-0014` — Into the Breach](../games/g-l/into-the-breach.md)
- [`GAME-0679` — "Jeanne d'Arc"](../games/g-l/jeanne-darc.md)
- [`GAME-0514` — Mewgenics](../games/m-r/mewgenics.md)
- [`GAME-0019` — Peg Solitaire](../games/m-r/peg-solitaire.md)
- [`GAME-0063` — Rush Hour](../games/m-r/rush-hour.md)
- [`GAME-0618` — Shining Force III](../games/s-z/shining-force-iii.md)
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

Гравець починає в одній фіксованій кінцевій точці й одним складеним жестом безпосередньо прокладає впорядкований маршрут змінної довжини через послідовно суміжні позиції поля до визначеної кінцевої точки цього маршруту.

### Включає

Протягування труби Flow Free від будь-якої кольорової точки через клітинки сітки до відповідної точки; прокладання однієї колії Cosmic Express від фіксованого вхідного відрізка колії до вибраного виходу; прокладання лінії панелі The Witness від початкового кола до кінцевої заглушки; прокладання одного маршруту LYNE від порожнистої кінцевої точки через маркери тієї самої родини до іншої порожнистої кінцевої точки.

### Виключає

Незалежне призначення не пов’язаних між собою клітинок; вибір лише двох кінцевих точок, між якими система сама знаходить маршрут; обертання вже наявних плиток труб.

### Ігри-носії

- [`GAME-0037` — Cosmic Express](../games/a-f/cosmic-express.md)
- [`GAME-0012` — Flow Free](../games/a-f/flow-free.md)
- [`GAME-0061` — LYNE](../games/g-l/lyne.md)
- [`GAME-0586` — Spooky Express](../games/s-z/spooky-express.md)
- [`GAME-0039` — The Witness](../games/s-z/the-witness.md)

## ACT-017

- Назва: Напрямлений крок усіх підконтрольних правилам об’єктів
- Переглянуто: `2026-08-24`

### Операційне визначення

Одна напрямлена команда наказує кожному об’єкту, який зараз визначено активним правилом керування, спробувати виконати той самий ортогональний крок на одну позицію.

### Включає

Переміщення всіх об’єктів, іменник яких у Baba Is You зараз має властивість YOU.

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

Штовхання ряду текстових об’єктів або об’єктів із властивістю PUSH у Baba Is You; штовхання вирівняного ряду ящиків у Patrick’s Parabox, зокрема коли найдальший елемент перетинає придатну межу контейнера.

### Виключає

Межу штовхання лише одного об’єкта (ACT-009); тягнення ланцюга; безпосередній вибір віддалених об’єктів; автоматичний рух конвеєром.

### Ігри-носії

- [`GAME-0013` — Baba Is You](../games/a-f/baba-is-you.md)
- [`GAME-0036` — "Patrick’s Parabox"](../games/m-r/patricks-parabox.md)

## ACT-019

- Назва: Вибрати здатність і ціль
- Переглянуто: `2026-10-05`

### Операційне визначення

Гравець обирає одного наразі доступного керованого учасника, вибирає одну з його визначених здібностей і вказує дозволеного для неї учасника, позицію або область, на яких ця здібність виконається.

### Включає

Постріл зброї меха чи вибір дії ремонту цього меха в Into the Breach; вибір цілі доступної класової здібності загону в Bad North; вибір одного вивченого прийому покемона й ворожої цілі в бою в Pokémon Red Version.

### Виключає

Переміщення того, хто діє; виконання ворогом уже підтвердженої атаки; автоматичні шкоду, поштовх чи зіткнення від здібності.

### Ігри-носії

- [`GAME-0416` — Advance Wars](../games/a-f/advance-wars.md)
- [`GAME-0453` — Age of Mythology](../games/a-f/age-of-mythology.md)
- [`GAME-0132` — Anno 1800](../games/a-f/anno-1800.md)
- [`GAME-0027` — Bad North: Jotunn Edition](../games/a-f/bad-north.md)
- [`GAME-0148` — Baldur’s Gate 3](../games/a-f/baldurs-gate-3.md)
- [`GAME-0601` — "Cassette Beasts"](../games/a-f/cassette-beasts.md)
- [`GAME-0346` — Chrono Trigger](../games/a-f/chrono-trigger.md)
- [`GAME-0144` — Clair Obscur: Expedition 33](../games/a-f/clair-obscur-expedition-33.md)
- [`GAME-0281` — Darkest Dungeon](../games/a-f/darkest-dungeon.md)
- [`GAME-0301` — "Divinity: Original Sin 2 - Definitive Edition"](../games/a-f/divinity-original-sin-2-definitive-edition.md)
- [`GAME-0608` — "Dosa Divas"](../games/a-f/dosa-divas.md)
- [`GAME-0435` — EarthBound](../games/a-f/earthbound.md)
- [`GAME-0486` — Final Fantasy Tactics](../games/a-f/final-fantasy-tactics.md)
- [`GAME-0338` — Final Fantasy VII](../games/a-f/final-fantasy-vii.md)
- [`GAME-0626` — "Fuga: Melodies of Steel"](../games/a-f/fuga-melodies-of-steel.md)
- [`GAME-0489` — Golden Sun](../games/g-l/golden-sun.md)
- [`GAME-0014` — Into the Breach](../games/g-l/into-the-breach.md)
- [`GAME-0679` — "Jeanne d'Arc"](../games/g-l/jeanne-darc.md)
- [`GAME-0530` — Lost Odyssey](../games/g-l/lost-odyssey.md)
- [`GAME-0688` — "Lunar: Silver Star Story Complete"](../games/g-l/lunar-silver-star-story-complete.md)
- [`GAME-0514` — Mewgenics](../games/m-r/mewgenics.md)
- [`GAME-0449` — Paper Mario](../games/m-r/paper-mario.md)
- [`GAME-0562` — Parasite Eve](../games/m-r/parasite-eve.md)
- [`GAME-0577` — People of Note](../games/m-r/people-of-note.md)
- [`GAME-0291` — Persona 5 Royal](../games/m-r/persona-5-royal.md)
- [`GAME-0463` — "Pokémon Gold Version"](../games/m-r/pokemon-gold-version.md)
- [`GAME-0160` — "Pokémon Legends: Z-A"](../games/m-r/pokemon-legends-z-a.md)
- [`GAME-0336` — "Pokémon Red Version"](../games/m-r/pokemon-red-version.md)
- [`GAME-0618` — Shining Force III](../games/s-z/shining-force-iii.md)
- [`GAME-0166` — Sid Meier’s Civilization VI](../games/s-z/sid-meiers-civilization-vi.md)
- [`GAME-0535` — Skies of Arcadia](../games/s-z/skies-of-arcadia.md)
- [`GAME-0048` — Tactical Breach Wizards](../games/s-z/tactical-breach-wizards.md)
- [`GAME-0268` — Undertale](../games/s-z/undertale.md)
- [`GAME-0499` — Vagrant Story](../games/s-z/vagrant-story.md)
- [`GAME-0176` — XCOM 2](../games/s-z/xcom-2.md)

## ACT-020

- Назва: Розміщення першої плитки черги у вибраній позиції поля
- Переглянуто: `2026-08-24`

### Операційне визначення

Гравець обирає одну придатну позицію поля й розміщує там обов’язковий зараз перший елемент видимої черги в наданій орієнтації, за потреби замінюючи визначений елемент, який займає цю позицію та для якого дозволено заміну.

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

Розіграш від однієї до п’яти карт Balatro для нарахування очок або скидання до п’яти вибраних карт із добором замін; вибір рівно трьох відкритих карт SET для перевірки відношень між ними.

### Виключає

Вибір карти поза допустимою видимою зоною; вибір ідентичностей карт, які буде дібрано на заміну; перенесення однієї відкритої карти між зонами ігрової викладки; призначення значення порожній позиції.

### Ігри-носії

- [`GAME-0017` — Balatro](../games/a-f/balatro.md)
- [`GAME-0649` — Drop Duchy](../games/a-f/drop-duchy.md)
- [`GAME-0652` — Mega Man Battle Network](../games/m-r/mega-man-battle-network.md)
- [`GAME-0064` — SET](../games/s-z/set.md)

## ACT-022

- Назва: Перевпорядкування послідовності постійних ефектів
- Переглянуто: `2026-08-24`

### Операційне визначення

Гравець переставляє постійні елементи з ефектами у впорядкованій зоні, щоб під час наступного автоматичного оцінювання їхні ефекти виконалися в новій послідовності.

### Включає

Переміщення Joker-карт у Balatro так, щоб додавальний ефект Mult розв’язався перед пізнішим множильним ефектом XMult.

### Виключає

Купівлю чи продаж ефекту; переставлення без механічного наслідку порядку; вибір карт для одного розіграшу, за який нараховують очки.

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
- [`GAME-0498` — Transport Fever 2](../games/s-z/transport-fever-2.md)
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
- [`GAME-0498` — Transport Fever 2](../games/s-z/transport-fever-2.md)

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

Вибір пізнішої наданої плитки; розміщення першої плитки черги з фіксованою орієнтацією (ACT-020); прокладання маршруту; обертання постійного зв’язаного шару.

### Ігри-носії

- [`GAME-0369` — Carcassonne](../games/a-f/carcassonne.md)
- [`GAME-0020` — Dorfromantik](../games/a-f/dorfromantik.md)
- [`GAME-0708` — "Rampart"](../games/m-r/rampart.md)

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
- [`GAME-0675` — "Teeny Tiny Trains"](../games/s-z/teeny-tiny-trains.md)
- [`GAME-0421` — The Incredible Machine](../games/s-z/the-incredible-machine.md)

## ACT-029

- Назва: Редагування символьної стрічки команд механізму
- Переглянуто: `2026-08-24`

### Операційне визначення

Гравець призначає, вилучає або переміщує символи команд в адресованих позиціях циклу на рядку виконання одного постійного механізму.

### Включає

Програмування кожного маніпулятора Opus Magnum розміщенням команд захоплення, відпускання, обертання, повороту, висування, втягування, переміщення вздовж рейки, повторення, скидання чи очікування у відповідних позиціях.

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

- [`GAME-0597` — "Duck Detective: The Ghost of Glamping"](../games/a-f/duck-detective-the-ghost-of-glamping.md)
- [`GAME-0023` — Return of the Obra Dinn](../games/m-r/return-of-the-obra-dinn.md)
- [`GAME-0046` — The Case of the Golden Idol](../games/s-z/the-case-of-the-golden-idol.md)
- [`GAME-0541` — The Incident at Galley House](../games/s-z/the-incident-at-galley-house.md)
- [`GAME-0538` — The Rise of the Golden Idol](../games/s-z/the-rise-of-the-golden-idol.md)
- [`GAME-0660` — "The Roottrees are Dead"](../games/s-z/the-roottrees-are-dead.md)

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

Заповнення речення в книзі Obra Dinn однією особою з маніфесту, причиною смерті та вбивцею, істотою або місцем, куди особа втекла.

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

Призначення однієї з восьми класичних навичок Lemmings вибраному лемінгу.

### Виключає

Вибір здібності безпосередньо керованого тактичного бійця й наведення її на окрему ділянку поля; покрокове керування рухом персонажа; автоматичну зміну стану без призначення гравцем.

### Ігри-носії

- [`GAME-0124` — Against the Storm](../games/a-f/against-the-storm.md)
- [`GAME-0425` — "Black & White"](../games/a-f/black-and-white.md)
- [`GAME-0324` — Contra Force](../games/a-f/contra-force.md)
- [`GAME-0130` — Frostpunk](../games/a-f/frostpunk.md)
- [`GAME-0583` — "Kunitsu-Gami: Path of the Goddess"](../games/g-l/kunitsu-gami-path-of-the-goddess.md)
- [`GAME-0638` — "Lemmings 2: The Tribes"](../games/g-l/lemmings-2-the-tribes.md)
- [`GAME-0025` — Lemmings](../games/g-l/lemmings.md)
- [`GAME-0305` — Sons Of The Forest](../games/s-z/sons-of-the-forest.md)

## ACT-037

- Назва: Регулювання швидкості автоматичного випуску популяції
- Переглянуто: `2026-08-24`

### Операційне визначення

Під час спроби гравець постійно підвищує або знижує частоту, з якою скінченна популяція, що очікує, автоматично виходить на активне ігрове поле, не змінюючи швидкості вже активних агентів.

### Включає

Використання кнопок мінус і плюс, щоб змінити частоту випуску лемінгів із люка в грі Lemmings.

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

- Назва: Замінити споряджений предмет здобутим
- Переглянуто: `2026-10-14`

### Операційне визначення

Гравець вибирає один здобутий предмет з інвентарю й поміщає його в сумісне місце спорядження, замінюючи поточний предмет і змінюючи бойові характеристики цього персонажа.

### Включає

Заміну спорядження щойно здобутою зброєю або бронею під час експедиції Loop Hero; заміну зброї персонажа в Clair Obscur: Expedition 33; заміну зброї, броні чи аксесуара члена загону в Baldur’s Gate 3; заміну броні чи аксесуара в Terraria.

### Виключає

Вибір класу персонажа до початку проходження; автоматичний приріст характеристики; переміщення звичайної карти між зонами розкладки.

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

Вихід з експедиції Loop Hero під час проходження ділянки з багаттям або прийняття меншої збереженої частки за відступ посеред кола.

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

- [`GAME-0589` — ChuChu Rocket!](../games/a-f/chuchu-rocket.md)
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

Перемотування солдатиків і маршрутних об’єктів Tin Hearts до моменту перед смертельним падінням, переміщення пристрою й відновлення безпечнішого перебігу; прокручування Timelie до моменту перед захопленням, зміна команди персонажа й пошук нового майбутнього; перемотування Tim і звичайних сутностей Braid перед іншим локальним рухом; вибір ранішої автоматичної контрольної точки Pikmin 4 і розігрування замінної послідовності команд; прокручування Viewfinder до моменту перед падінням або розміщенням зображення й фіксація іншого просторового продовження.

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

У вибраний момент симуляції гравець призначає, замінює або очищає місце призначення чи контекстну взаємодію одного постійного актора, а команда лишається в часовому плані, доки її не змінять або не буде розв’язано.

### Включає

Вибір дівчини або кота Timelie у поточний момент часового курсора й планування місця призначення або контекстної дії: взаємодії з кодовою панеллю чи вентиляційним проходом, нявкання або іншої пов’язаної дії.

### Виключає

Локальне покрокове пересування аватара; запис багаторазової інструкції в клітинку світу; редагування циклічних символів механізму машини.

### Ігри-носії

- [`GAME-0031` — Timelie](../games/s-z/timelie.md)

## ACT-046

- Назва: Редагування просторового маршруту контролера й поля інструкцій
- Переглянуто: `2026-08-24`

### Операційне визначення

На фіксованій сітці машини гравець прокладає напрямлений маршрут переміщення одного контролера й призначає клітинкам цього маршруту символи команд, прив’язані до конкретного кольору або контролера. Просторові адреси клітинок визначають порядок виконання команд.

### Включає

Створення маршрутів червоного й синього маніпуляторів у SpaceChem та розміщення на цих маршрутах їхніх команд введення (input), захоплення (grab), обертання (rotate), утворення зв’язку (bond), синхронізації (sync), відпускання (drop) і виведення (output).

### Виключає

Редагування команд в окремих адресованих часових стовпцях; розміщення фізичних компонентів машини; призначення команди акторові в ігровому світі на довільний момент симуляції.

### Ігри-носії

- [`GAME-0032` — SpaceChem](../games/s-z/spacechem.md)

## ACT-047

- Назва: Розміщення замінної кінцевої точки парного порталу
- Переглянуто: `2026-08-24`

### Операційне визначення

Гравець цілиться у придатну поверхню світу й створює на ній кінцеву точку певного кольору або каналу постійної просторової пари порталів, замінюючи попередню кінцеву точку того самого каналу.

### Включає

Постріл синього або помаранчевого порталу Portal на допустиму пласку поверхню камери після отримання повнофункціонального ручного портального пристрою.

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

- [`GAME-0423` — "Banjo-Kazooie: Nuts & Bolts"](../games/a-f/banjo-kazooie-nuts-and-bolts.md)
- [`GAME-0318` — Battletoads](../games/a-f/battletoads.md)
- [`GAME-0557` — "Boktai: The Sun Is in Your Hand"](../games/a-f/boktai-the-sun-is-in-your-hand.md)
- [`GAME-0055` — Bonfire Peaks](../games/a-f/bonfire-peaks.md)
- [`GAME-0108` — Cocoon](../games/a-f/cocoon.md)
- [`GAME-0429` — Commandos: Behind Enemy Lines](../games/a-f/commandos-behind-enemy-lines.md)
- [`GAME-0254` — CONTROL Ultimate Edition](../games/a-f/control-ultimate-edition.md)
- [`GAME-0301` — "Divinity: Original Sin 2 - Definitive Edition"](../games/a-f/divinity-original-sin-2-definitive-edition.md)
- [`GAME-0565` — Dome Keeper](../games/a-f/dome-keeper.md)
- [`GAME-0495` — Donkey Kong Country Returns](../games/a-f/donkey-kong-country-returns.md)
- [`GAME-0329` — "Donkey Kong Country"](../games/a-f/donkey-kong-country.md)
- [`GAME-0560` — Gunstar Heroes](../games/g-l/gunstar-heroes.md)
- [`GAME-0212` — Half-Life 2](../games/g-l/half-life-2.md)
- [`GAME-0581` — "Hardspace: Shipbreaker"](../games/g-l/hardspace-shipbreaker.md)
- [`GAME-0112` — Human: Fall Flat](../games/g-l/human-fall-flat.md)
- [`GAME-0510` — Indiana Jones and the Great Circle](../games/g-l/indiana-jones-and-the-great-circle.md)
- [`GAME-0240` — "Kingdom Come: Deliverance II"](../games/g-l/kingdom-come-deliverance-ii.md)
- [`GAME-0095` — Manifold Garden](../games/m-r/manifold-garden.md)
- [`GAME-0096` — Maquette](../games/m-r/maquette.md)
- [`GAME-0323` — "Marvel’s Spider-Man 2"](../games/m-r/marvels-spider-man-2.md)
- [`GAME-0727` — "Miniatures"](../games/m-r/miniatures.md)
- [`GAME-0300` — Overcooked! 2](../games/m-r/overcooked-2.md)
- [`GAME-0500` — Pacific Drive](../games/m-r/pacific-drive.md)
- [`GAME-0703` — "Part Time UFO"](../games/m-r/part-time-ufo.md)
- [`GAME-0203` — "PEAK"](../games/m-r/peak.md)
- [`GAME-0113` — Portal 2 — Cooperative Campaign](../games/m-r/portal-2-co-op.md)
- [`GAME-0033` — Portal](../games/m-r/portal.md)
- [`GAME-0681` — "Power Stone 2"](../games/m-r/power-stone-2.md)
- [`GAME-0519` — Power Stone](../games/m-r/power-stone.md)
- [`GAME-0534` — PowerWash Simulator 2](../games/m-r/powerwash-simulator-2.md)
- [`GAME-0279` — PowerWash Simulator](../games/m-r/powerwash-simulator.md)
- [`GAME-0561` — Psychonauts 2](../games/m-r/psychonauts-2.md)
- [`GAME-0715` — "Pushover"](../games/m-r/pushover.md)
- [`GAME-0319` — Sea of Thieves](../games/s-z/sea-of-thieves.md)
- [`GAME-0466` — Streets of Rage 2](../games/s-z/streets-of-rage-2.md)
- [`GAME-0354` — Super Mario World](../games/s-z/super-mario-world.md)
- [`GAME-0567` — SUPERHOT VR](../games/s-z/superhot-vr.md)
- [`GAME-0094` — Superliminal](../games/s-z/superliminal.md)
- [`GAME-0568` — Teardown](../games/s-z/teardown.md)
- [`GAME-0729` — "The Last Campfire"](../games/s-z/the-last-campfire.md)
- [`GAME-0559` — The Last Guardian](../games/s-z/the-last-guardian.md)
- [`GAME-0261` — The Last of Us Part I](../games/s-z/the-last-of-us-part-i.md)
- [`GAME-0651` — The Plucky Squire](../games/s-z/the-plucky-squire.md)
- [`GAME-0115` — Unpacking](../games/s-z/unpacking.md)
- [`GAME-0499` — Vagrant Story](../games/s-z/vagrant-story.md)
- [`GAME-0497` — Wario Land 4](../games/s-z/wario-land-4.md)
- [`GAME-0669` — "Wilmot Works It Out"](../games/s-z/wilmot-works-it-out.md)

## ACT-049

- Назва: Перемикання досяжного перемикача у світі
- Переглянуто: `2026-10-04`

### Операційне визначення

Гравець керує аватаром на місці й активує досяжний постійний перемикач, змінюючи заданий стан або напрямок руху пов’язаного механізму у світі.

### Включає

Використання важеля Braid, щоб запустити або розвернути пов’язану платформу; натискання досяжного синього перемикача Manifold Garden після періодичного переходу через прогалину, щоб відкрити пов’язані двері; установлення кожного досяжного вентиля в першій водній інструкції Chants of Sennaar у заданий відкритий або закритий стан; активацію досяжних консолей Chapter 1 у Split Fiction, які змінюють пов’язаний бар’єр або платформу незалежно від парних умов спільної гри.

### Виключає

Утримування натискної плити зайнятою; редагування віддаленої взаємодії з часовою позначкою; розміщення багаторазового маркера інструкції.

### Ігри-носії

- [`GAME-0034` — Braid, Anniversary Edition](../games/a-f/braid.md)
- [`GAME-0302` — "Captain Toad: Treasure Tracker"](../games/a-f/captain-toad-treasure-tracker.md)
- [`GAME-0101` — Chants of Sennaar](../games/a-f/chants-of-sennaar.md)
- [`GAME-0592` — Dungeons of Hinterberg](../games/a-f/dungeons-of-hinterberg.md)
- [`GAME-0533` — "Ghost Trick: Phantom Detective"](../games/g-l/ghost-trick-phantom-detective.md)
- [`GAME-0582` — Grim Fandango](../games/g-l/grim-fandango.md)
- [`GAME-0399` — Ico](../games/g-l/ico.md)
- [`GAME-0215` — It Takes Two](../games/g-l/it-takes-two.md)
- [`GAME-0095` — Manifold Garden](../games/m-r/manifold-garden.md)
- [`GAME-0500` — Pacific Drive](../games/m-r/pacific-drive.md)
- [`GAME-0334` — Quake](../games/m-r/quake.md)
- [`GAME-0512` — Resident Evil Requiem](../games/m-r/resident-evil-requiem.md)
- [`GAME-0157` — Split Fiction](../games/s-z/split-fiction.md)
- [`GAME-0528` — The Neverhood](../games/s-z/the-neverhood.md)
- [`GAME-0651` — The Plucky Squire](../games/s-z/the-plucky-squire.md)
- [`GAME-0513` — Thief: The Dark Project](../games/s-z/thief-the-dark-project.md)
- [`GAME-0451` — Tomb Raider (1996)](../games/s-z/tomb-raider-1996.md)
- [`GAME-0499` — Vagrant Story](../games/s-z/vagrant-story.md)
- [`GAME-0497` — Wario Land 4](../games/s-z/wario-land-4.md)

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
- Переглянуто: `2026-10-15`

### Операційне визначення

Коли в одному стані світу активні кілька допустимих постійних тіл, гравець передає єдиний осередок прямої навігації або повноважень командування з поточного тіла іншому. Попереднє тіло залишається у світі й діє за оголошеними правилами для тіла, яке більше не є цим осередком.

### Включає

Перемикання від Rescue Officer до Oatchi після розділення їхніх груп Pikmin у Pikmin 4; перенесення свідомості з поточного тіла The Swapper у видимого наявного клона, коли попереднє тіло залишається; перемикання прямого керування на допустимого партнера в EA SPORTS FC 26, коли попередній футболіст лишається на полі під керуванням командного ШІ.

### Виключає

Вибір актора лише для задавання віддаленого пункту призначення; створення нового тіла без передавання керування; телепортацію одного незмінного тіла; чергування змагальних ходів.

### Ігри-носії

- [`GAME-0329` — "Donkey Kong Country"](../games/a-f/donkey-kong-country.md)
- [`GAME-0163` — EA SPORTS FC 26](../games/a-f/ea-sports-fc-26.md)
- [`GAME-0241` — NBA 2K26](../games/m-r/nba-2k26.md)
- [`GAME-0600` — "NBA Street Vol. 2"](../games/m-r/nba-street-vol-2.md)
- [`GAME-0300` — Overcooked! 2](../games/m-r/overcooked-2.md)
- [`GAME-0035` — Pikmin 4](../games/m-r/pikmin-4.md)
- [`GAME-0665` — "Sega Worldwide Soccer '97"](../games/s-z/sega-worldwide-soccer-97.md)
- [`GAME-0548` — Space Station Silicon Valley](../games/s-z/space-station-silicon-valley.md)
- [`GAME-0553` — The Lost Vikings](../games/s-z/the-lost-vikings.md)
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

Підняття наданої фотографії у Viewfinder, утримання її перед сценою, переміщення або обертання в перспективі та фіксація цього зображення в обраному місці.

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

Перетягування зібраних термінів The Case of the Golden Idol у пропуски панелей визначення особи й місця та сувою події на екрані Thinking у пролозі.

### Виключає

Введення необмеженого довільного тексту; видобування фрази з доказу; призначення повного досьє особи та її долі одному суб’єкту реєстру.

### Ігри-носії

- [`GAME-0597` — "Duck Detective: The Ghost of Glamping"](../games/a-f/duck-detective-the-ghost-of-glamping.md)
- [`GAME-0046` — The Case of the Golden Idol](../games/s-z/the-case-of-the-golden-idol.md)
- [`GAME-0538` — The Rise of the Golden Idol](../games/s-z/the-rise-of-the-golden-idol.md)
- [`GAME-0606` — "The Séance of Blake Manor"](../games/s-z/the-seance-of-blake-manor.md)

## ACT-061

- Назва: Розіграти просторову карту дії з руки
- Переглянуто: `2026-08-23`

### Операційне визначення

Гравець вибирає одну карту дії, яку наразі тримає в руці, та допустимий просторовий параметр цілі, витрачаючи цю карту для застосування оголошеного переходу переміщення, атаки, захисту або зміни позиції.

### Включає

Розігрування у Fights in Tight Spaces карти руху на допустиму клітинку або карти атаки / штовхання на допустимого ворога чи суміжну ціль; розігрування карти руху Golf Peaks з одним із чотирьох основних напрямків як просторовою ціллю.

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

Гравець наказує постійному керованому агенту розвернутися в протилежний бік, не змінюючи своєї визначеної позиції.

### Включає

Розворот Wanderer у Shogun Showdown як бойова дія, що витрачає один хід.

### Виключає

Обертання прикріпленого до тіла інструмента, коли вся область, яку він охоплює під час обертання, має значення для рішення; зміну ракурсу камери; переміщення в іншу позицію.

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

Командою руху вперед у зайняту сусідню позицію гравець обмінює позиції керованого агента й одиниці, до якої той обернений, замість того, щоб рух було відхилено або цю одиницю відштовхнуто.

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

- [`GAME-0525` — "Anno 117: Pax Romana"](../games/a-f/anno-117-pax-romana.md)
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

- [`GAME-0654` — "Hotel Dusk: Room 215"](../games/g-l/hotel-dusk-room-215.md)
- [`GAME-0058` — inbento](../games/g-l/inbento.md)
- [`GAME-0554` — Strange Horticulture](../games/s-z/strange-horticulture.md)
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

- [`GAME-0705` — "Contraband Police"](../games/a-f/contraband-police.md)
- [`GAME-0699` — "Dungeon Master"](../games/a-f/dungeon-master.md)
- [`GAME-0711` — "ELOH"](../games/a-f/eloh.md)
- [`GAME-0702` — "Escaping Wonderland"](../games/a-f/escaping-wonderland.md)
- [`GAME-0680` — "Ghost Town"](../games/g-l/ghost-town.md)
- [`GAME-0060` — HOOK](../games/g-l/hook.md)
- [`GAME-0563` — Lorelei and the Laser Eyes](../games/g-l/lorelei-and-the-laser-eyes.md)
- [`GAME-0105` — Outer Wilds](../games/m-r/outer-wilds.md)
- [`GAME-0698` — "Song of Bloom"](../games/s-z/song-of-bloom.md)
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

- [`GAME-0563` — Lorelei and the Laser Eyes](../games/g-l/lorelei-and-the-laser-eyes.md)
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

Розкриття адресованої клітинки на межі; малювання маршруту крізь поле; подання повної гіпотези прихованої розкладки; повтор уже розв’язаного входу як нового спостереження.

### Ігри-носії

- [`GAME-0066` — Black Box](../games/a-f/black-box.md)

## ACT-075

- Назва: Подати просторову гіпотезу точної потужності
- Переглянуто: `2026-08-23`

### Операційне визначення

Після позначення визначеної точної кількості позицій в обмеженому полі гравець подає цю повну пропозицію зайнятості на глобальне порівняння з прихованою просторовою системою.

### Включає

Натиснути Check у стандартному Black Box після позначення рівно п’яти клітинок як куль.

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

Подання повністю редагованої пропозиції як одного запиту; вибір невпорядкованої підмножини; реакцію лише на найновіший сигнал; введення команд, поки система ще показує ціль.

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

- [`GAME-0563` — Lorelei and the Laser Eyes](../games/g-l/lorelei-and-the-laser-eyes.md)
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

- [`GAME-0680` — "Ghost Town"](../games/g-l/ghost-town.md)
- [`GAME-0123` — Inscryption](../games/g-l/inscryption.md)
- [`GAME-0563` — Lorelei and the Laser Eyes](../games/g-l/lorelei-and-the-laser-eyes.md)
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

- Назва: Застосувати предмет з інвентарю до сумісного об’єкта сцени
- Переглянуто: `2026-08-24`

### Операційне визначення

Гравець вибирає один здобутий предмет з інвентарю та застосовує його до конкретного постійного об’єкта сцени, якщо тип і поточний стан цього об’єкта допускають передбачене правилами використання саме цього предмета.

### Включає

Вставити налаштований ключ The Room у відповідну замкову щілину, накласти металеву пластину на відповідний гвинт і встановити знайдену лінзу у вузол окуляра; застосувати складений інструмент із магніту й мотузки Machinarium до підготовленої опори звалища; застосувати готовий рибальський інструмент The Longest Journey до активної ділянки ключа біля колії.

### Виключає

Екіпірування здобичі зі статистичними показниками; встановлення будівельної деталі на поле; збирання предмета під час контакту; автоматичне відкриття перешкоди ключем, який несе персонаж, під час дотику.

### Ігри-носії

- [`GAME-0173` — Blue Prince](../games/a-f/blue-prince.md)
- [`GAME-0247` — Dishonored (2012)](../games/a-f/dishonored-2012.md)
- [`GAME-0186` — "Don’t Starve Together"](../games/a-f/dont-starve-together.md)
- [`GAME-0680` — "Ghost Town"](../games/g-l/ghost-town.md)
- [`GAME-0582` — Grim Fandango](../games/g-l/grim-fandango.md)
- [`GAME-0123` — Inscryption](../games/g-l/inscryption.md)
- [`GAME-0563` — Lorelei and the Laser Eyes](../games/g-l/lorelei-and-the-laser-eyes.md)
- [`GAME-0086` — Machinarium](../games/m-r/machinarium.md)
- [`GAME-0686` — "Maniac Mansion"](../games/m-r/maniac-mansion.md)
- [`GAME-0129` — Minecraft](../games/m-r/minecraft.md)
- [`GAME-0139` — Palworld](../games/m-r/palworld.md)
- [`GAME-0330` — Silent Hill 2 (2024 remake)](../games/s-z/silent-hill-2-2024.md)
- [`GAME-0430` — Silent Hill](../games/s-z/silent-hill.md)
- [`GAME-0554` — Strange Horticulture](../games/s-z/strange-horticulture.md)
- [`GAME-0636` — "The Dig"](../games/s-z/the-dig.md)
- [`GAME-0613` — "The Drifter"](../games/s-z/the-drifter.md)
- [`GAME-0087` — The Longest Journey](../games/s-z/the-longest-journey.md)
- [`GAME-0553` — The Lost Vikings](../games/s-z/the-lost-vikings.md)
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

- Назва: Забирати вибраний предмет сцени в інвентар
- Переглянуто: `2026-10-04`

### Операційне визначення

Гравець вибирає один доступний зараз вказаний предмет сцени, прибирає його з цього місця й додає його стійку ідентичність до дискретного інвентарю предметів при собі.

### Включає

Забирання високо розташованої ляльки, незакріпленого магніту й котушки мотузки в Machinarium після виконання відповідних передумов досяжності та пересування; забирання готової супербатареї Day of the Tentacle з полиці Реда.

### Виключає

Безперервне перенесення вільного твердого об’єкта у просторі світу; автоматичне отримання предмета від персонажа; збирання жетона очок під час контакту; виявлення предмета без його отримання.

### Ігри-носії

- [`GAME-0453` — Age of Mythology](../games/a-f/age-of-mythology.md)
- [`GAME-0456` — Alone in the Dark](../games/a-f/alone-in-the-dark.md)
- [`GAME-0511` — Animal Crossing: New Leaf](../games/a-f/animal-crossing-new-leaf.md)
- [`GAME-0173` — Blue Prince](../games/a-f/blue-prince.md)
- [`GAME-0555` — Chibi-Robo!](../games/a-f/chibi-robo.md)
- [`GAME-0490` — Comix Zone](../games/a-f/comix-zone.md)
- [`GAME-0088` — Day of the Tentacle](../games/a-f/day-of-the-tentacle.md)
- [`GAME-0515` — Dino Crisis](../games/a-f/dino-crisis.md)
- [`GAME-0301` — "Divinity: Original Sin 2 - Definitive Edition"](../games/a-f/divinity-original-sin-2-definitive-edition.md)
- [`GAME-0699` — "Dungeon Master"](../games/a-f/dungeon-master.md)
- [`GAME-0405` — Fable II](../games/a-f/fable-ii.md)
- [`GAME-0582` — Grim Fandango](../games/g-l/grim-fandango.md)
- [`GAME-0510` — Indiana Jones and the Great Circle](../games/g-l/indiana-jones-and-the-great-circle.md)
- [`GAME-0563` — Lorelei and the Laser Eyes](../games/g-l/lorelei-and-the-laser-eyes.md)
- [`GAME-0086` — Machinarium](../games/m-r/machinarium.md)
- [`GAME-0686` — "Maniac Mansion"](../games/m-r/maniac-mansion.md)
- [`GAME-0431` — Ori and the Blind Forest](../games/m-r/ori-and-the-blind-forest.md)
- [`GAME-0500` — Pacific Drive](../games/m-r/pacific-drive.md)
- [`GAME-0562` — Parasite Eve](../games/m-r/parasite-eve.md)
- [`GAME-0463` — "Pokémon Gold Version"](../games/m-r/pokemon-gold-version.md)
- [`GAME-0518` — Pokémon Pokopia](../games/m-r/pokemon-pokopia.md)
- [`GAME-0512` — Resident Evil Requiem](../games/m-r/resident-evil-requiem.md)
- [`GAME-0330` — Silent Hill 2 (2024 remake)](../games/s-z/silent-hill-2-2024.md)
- [`GAME-0430` — Silent Hill](../games/s-z/silent-hill.md)
- [`GAME-0554` — Strange Horticulture](../games/s-z/strange-horticulture.md)
- [`GAME-0636` — "The Dig"](../games/s-z/the-dig.md)
- [`GAME-0613` — "The Drifter"](../games/s-z/the-drifter.md)
- [`GAME-0528` — The Neverhood](../games/s-z/the-neverhood.md)
- [`GAME-0343` — The Secret of Monkey Island](../games/s-z/the-secret-of-monkey-island.md)
- [`GAME-0513` — Thief: The Dark Project](../games/s-z/thief-the-dark-project.md)
- [`GAME-0451` — Tomb Raider (1996)](../games/s-z/tomb-raider-1996.md)

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
- [`GAME-0511` — Animal Crossing: New Leaf](../games/a-f/animal-crossing-new-leaf.md)
- [`GAME-0278` — DAVE THE DIVER](../games/a-f/dave-the-diver.md)
- [`GAME-0088` — Day of the Tentacle](../games/a-f/day-of-the-tentacle.md)
- [`GAME-0437` — Diner Dash](../games/a-f/diner-dash.md)
- [`GAME-0608` — "Dosa Divas"](../games/a-f/dosa-divas.md)
- [`GAME-0405` — Fable II](../games/a-f/fable-ii.md)
- [`GAME-0582` — Grim Fandango](../games/g-l/grim-fandango.md)
- [`GAME-0240` — "Kingdom Come: Deliverance II"](../games/g-l/kingdom-come-deliverance-ii.md)
- [`GAME-0086` — Machinarium](../games/m-r/machinarium.md)
- [`GAME-0576` — The Forgotten City](../games/s-z/the-forgotten-city.md)
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

Розміщення одного мідного, залізного або золотого злитка у відповідній комірці Blacksmith’s Bundle Stardew Valley; розміщення 99 Slime або 10 Bat Wings в одній придатній комірці Adventurer’s Bundle; додавання по одній перенесеній палиці чи листку до розміщеного контуру Temporary Shelter у The Forest.

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

Гравець задає один горизонтальний чвертьоберт за або проти годинникової стрілки від поточного усталеного виду з одного із чотирьох основних напрямків огляду, роблячи сусідню ортографічну проєкцію визначальною для подальшого пересування без вибору чи переміщення окремих об’єктів світу.

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

Чотири фіксовані чвертьоберти між основними напрямками огляду; вільний огляд сцени, камера якого не змінює ігрових правил; обертання одного фізичного об’єкта; зміну гравітації світу; фіксацію перспективного зображення, що створює геометрію.

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
- [`GAME-0686` — "Maniac Mansion"](../games/m-r/maniac-mansion.md)
- [`GAME-0093` — Monument Valley](../games/m-r/monument-valley.md)
- [`GAME-0722` — "QuackShot Starring Donald Duck"](../games/m-r/quackshot-starring-donald-duck.md)
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

Застосування Gravity Shift до стіни або стелі в Manifold Garden, після якого ця поверхня стає підлогою у відповідній кольоровій системі гравітації.

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

Утримання дверей Now You See It в Antichamber у полі зору, щоб місце, куди вони ведуть, лишалося сталим, або поворот до скляного вікна, після якого двері виходять із поля зору й задана авторами заміна стає можливою.

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

У Keep Talking and Nobody Explodes Сапер голосом описує порядок дротів, вигляд кнопки чи ідентифікатори на краю бомби, а Експерт у відповідь називає вибраний дріт або дає інструкцію з часовою умовою для кнопки.

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

Перерізання одного вибраного дроту; натискання й негайне відпускання Button; утримування кнопки, щоб показати смугу, та відпускання на вибраній цифрі таймера.

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

- [`GAME-0705` — "Contraband Police"](../games/a-f/contraband-police.md)
- [`GAME-0103` — Papers, Please](../games/m-r/papers-please.md)

## ACT-105

- Назва: Поставити на справі штамп з одним із двох остаточних вердиктів
- Переглянуто: `2026-08-23`

### Операційне визначення

Після перевірки однієї поданої справи гравець фіксує рівно одну з двох взаємовиключних остаточних класифікацій, ставлячи відповідну фізичну або дієгетичну позначку на матеріалі справи.

### Включає

Розміщення паспорта відвідувача під штампувальним пристроєм Papers, Please і поставлення штампа APPROVED або DENIED перед поверненням документів.

### Виключає

Позначення гіпотези, яку можна змінити; визначення класу однієї прихованої клітинки поля; вибір із кількох неостаточних реплік діалогу; автоматичне оцінювання справи без зафіксованого рішення гравця.

### Ігри-носії

- [`GAME-0705` — "Contraband Police"](../games/a-f/contraband-police.md)
- [`GAME-0103` — Papers, Please](../games/m-r/papers-please.md)

## ACT-106

- Назва: Ввести впорядкований код напрямків без переміщення
- Переглянуто: `2026-10-13`

### Операційне визначення

Звертаючись до одного сприйнятливого об’єкта світу або інтерфейсу команд, гравець вводить скінченну впорядковану послідовність основних напрямків як символічні команди, а не переміщує керованого персонажа в цих напрямках.

### Включає

Введення послідовності «вниз, праворуч, угору, ліворуч, угору, праворуч» біля візерунчастих дверей TUNIC поруч із фонтаном у Верхньому світі; введення коду напрямків вибраної стратагеми в Helldivers 2.

### Виключає

Переміщення аватара маршрутом; безперервне креслення траєкторії вказівником; вибір напрямку діалогу; редагування повного коду перед надсиланням.

### Ігри-носії

- [`GAME-0545` — Dispatch](../games/a-f/dispatch.md)
- [`GAME-0159` — Helldivers 2](../games/g-l/helldivers-2.md)
- [`GAME-0104` — TUNIC](../games/s-z/tunic.md)

## ACT-107

- Назва: Дізнатися в розмові факт, потрібний для подальшої дії
- Переглянуто: `2026-10-02`

### Операційне визначення

Гравець завершує розмову, після якої гра записує один точний факт як відомий і дозволяє використати ці відомості в подальшій взаємодії, не видаючи предмета чи нової фізичної здібності.

### Включає

Розмову з Hornfels про коди запуску в Outer Wilds, після якої код реєструється як відомий; розмови в завданнях Cyberpunk 2077, які відкривають корисні відомості про людей, місця або доступ.

### Виключає

Читання необов’язкового атмосферного тексту; отримання предмета-ключа; введення коду в цільовий механізм; вибір репліки, єдиним наслідком якої є зміна тону оповіді.

### Ігри-носії

- [`GAME-0635` — "1000xRESIST"](../games/0-9/1000xresist.md)
- [`GAME-0148` — Baldur’s Gate 3](../games/a-f/baldurs-gate-3.md)
- [`GAME-0146` — Cyberpunk 2077](../games/a-f/cyberpunk-2077.md)
- [`GAME-0264` — Disco Elysium - The Final Cut](../games/a-f/disco-elysium-the-final-cut.md)
- [`GAME-0582` — Grim Fandango](../games/g-l/grim-fandango.md)
- [`GAME-0219` — Lineage II](../games/g-l/lineage-ii.md)
- [`GAME-0563` — Lorelei and the Laser Eyes](../games/g-l/lorelei-and-the-laser-eyes.md)
- [`GAME-0105` — Outer Wilds](../games/m-r/outer-wilds.md)
- [`GAME-0624` — "Paradise Killer"](../games/m-r/paradise-killer.md)
- [`GAME-0523` — Pentiment](../games/m-r/pentiment.md)
- [`GAME-0485` — Shenmue](../games/s-z/shenmue.md)
- [`GAME-0554` — Strange Horticulture](../games/s-z/strange-horticulture.md)
- [`GAME-0362` — "The Elder Scrolls III: Morrowind"](../games/s-z/the-elder-scrolls-iii-morrowind.md)
- [`GAME-0576` — The Forgotten City](../games/s-z/the-forgotten-city.md)
- [`GAME-0395` — "The Legend of Zelda: Majora’s Mask"](../games/s-z/the-legend-of-zelda-majoras-mask.md)
- [`GAME-0593` — "The Legend of Zelda: The Minish Cap"](../games/s-z/the-legend-of-zelda-the-minish-cap.md)
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
- [`GAME-0660` — "The Roottrees are Dead"](../games/s-z/the-roottrees-are-dead.md)

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

У зовнішньому режимі редагування компонування гравець поступально переміщує одну цілу панель із фіксованою прохідною геометрією та портами, зберігаючи її внутрішню будову, орієнтацію й розташовані на ній елементи.

### Включає

Перетягування однієї ранньої панелі громадського знака The Pedestrian у нове місце в огляді перед побудовою маршруту пішохода.

### Виключає

Переміщення ділянки мапи світу, що визначає його будову; переставляння ілюстрованої сцени між фіксованими слотами; обертання панелі; безпосереднє створення ребра пересування.

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

- Назва: Установити переносну сферу-світ на п’єдестал переходу між світами або забрати її звідти
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

Хват за край однією чи обома руками в Human: Fall Flat із подальшим підтягуванням шарнірного фізичного тіла вгору або підвішуванням під час зміни положення.

### Виключає

Піднімання одного твердого предмета в центровану позу перенесення; прикріплення автономного агента до конструкції; команду лазіння, що існує лише як анімація.

### Ігри-носії

- [`GAME-0112` — Human: Fall Flat](../games/g-l/human-fall-flat.md)
- [`GAME-0552` — Jusant](../games/g-l/jusant.md)

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
- [`GAME-0716` — "Terra Nil"](../games/s-z/terra-nil.md)
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

- Назва: Налаштувати правило роботи окремого фабричного об’єкта
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
- [`GAME-0504` — Frostpunk 2](../games/a-f/frostpunk-2.md)
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

Вибір технологій Factorio, додавання їхніх передумов до черги та зміна її порядку або заміна поточної цілі; призначення окремої технології кожному з трьох напрямів досліджень у Stellaris.

### Виключає

Виробництво наукових пакетів; вибір рецепта машини; автоматичне отримання вдосконалення без обраного гравцем порядку досліджень.

### Ігри-носії

- [`GAME-0179` — Age of Empires II: Definitive Edition](../games/a-f/age-of-empires-ii-definitive-edition.md)
- [`GAME-0453` — Age of Mythology](../games/a-f/age-of-mythology.md)
- [`GAME-0135` — "Captain of Industry"](../games/a-f/captain-of-industry.md)
- [`GAME-0209` — Cossacks 3](../games/a-f/cossacks-3.md)
- [`GAME-0131` — Dyson Sphere Program](../games/a-f/dyson-sphere-program.md)
- [`GAME-0119` — Factorio](../games/a-f/factorio.md)
- [`GAME-0504` — Frostpunk 2](../games/a-f/frostpunk-2.md)
- [`GAME-0182` — Hearts of Iron IV](../games/g-l/hearts-of-iron-iv.md)
- [`GAME-0517` — Homeworld](../games/g-l/homeworld.md)
- [`GAME-0166` — Sid Meier’s Civilization VI](../games/s-z/sid-meiers-civilization-vi.md)
- [`GAME-0287` — Stellaris](../games/s-z/stellaris.md)
- [`GAME-0136` — "Surviving Mars: Relaunched"](../games/s-z/surviving-mars.md)

## ACT-122

- Назва: Вручну видобути ресурс або розібрати об’єкт світу
- Переглянуто: `2026-10-14`

### Операційне визначення

Гравець безпосередньо добуває матеріали з досяжного ресурсу ігрового світу або розбирає об’єкт, з якого можна отримати матеріали чи повернути предмет. Правила визначають, чи результат одразу потрапляє до інвентарю, чи потребує окремого підбору.

### Включає

Ручний видобуток руди, каменю або деревини й повернення розміщеного об’єкта у Factorio; розбирання предмета обстановки на матеріали в Project Zomboid; ручне добування ресурсів на Луках у Valheim; утримувані або повторювані дії добування ресурсів у дослідженому навчальному маршруті 7 Days to Die.

### Виключає

Автоматичний видобуток руди працюючим буром; знищення ворога зброєю; видалення об’єкта без отримання матеріалів чи повернення предмета; просте переміщення вже відокремленого або збереженого предмета.

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
- Переглянуто: `2026-10-05`

### Операційне визначення

Гравець вибирає один відомий і наразі доступний особистий рецепт та запускає виготовлення однієї чи кількох одиниць визначеного ним результату.

### Включає

Особисте виготовлення у Factorio й Cyberpunk 2077, польове виготовлення в Monster Hunter Wilds та виготовлення з інвентарю або біля потрібної станції в Terraria.

### Виключає

Призначення рецепта автономному виробничому об’єкту; довільне поєднання предметів; вибір дослідження; тривалість виконання, якою керує система.

### Ігри-носії

- [`GAME-0233` — 7 Days to Die](../games/0-9/7-days-to-die.md)
- [`GAME-0257` — "Alien: Isolation"](../games/a-f/alien-isolation.md)
- [`GAME-0320` — "Animal Crossing: New Horizons"](../games/a-f/animal-crossing-new-horizons.md)
- [`GAME-0143` — ARC Raiders](../games/a-f/arc-raiders.md)
- [`GAME-0186` — "Don’t Starve Together"](../games/a-f/dont-starve-together.md)
- [`GAME-0608` — "Dosa Divas"](../games/a-f/dosa-divas.md)
- [`GAME-0131` — Dyson Sphere Program](../games/a-f/dyson-sphere-program.md)
- [`GAME-0152` — Elden Ring](../games/a-f/elden-ring.md)
- [`GAME-0119` — Factorio](../games/a-f/factorio.md)
- [`GAME-0314` — Grounded](../games/g-l/grounded.md)
- [`GAME-0151` — Monster Hunter Wilds](../games/m-r/monster-hunter-wilds.md)
- [`GAME-0229` — "No Man’s Sky"](../games/m-r/no-mans-sky.md)
- [`GAME-0500` — Pacific Drive](../games/m-r/pacific-drive.md)
- [`GAME-0139` — Palworld](../games/m-r/palworld.md)
- [`GAME-0518` — Pokémon Pokopia](../games/m-r/pokemon-pokopia.md)
- [`GAME-0142` — Project Zomboid](../games/m-r/project-zomboid.md)
- [`GAME-0249` — Resident Evil 4 (2023 remake)](../games/m-r/resident-evil-4-2023.md)
- [`GAME-0141` — Rust](../games/m-r/rust.md)
- [`GAME-0128` — Satisfactory](../games/s-z/satisfactory.md)
- [`GAME-0178` — Subnautica](../games/s-z/subnautica.md)
- [`GAME-0153` — Terraria](../games/s-z/terraria.md)
- [`GAME-0604` — "The Alters"](../games/s-z/the-alters.md)
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

- [`GAME-0611` — "Culdcept"](../games/a-f/culdcept.md)
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

- [`GAME-0664` — "Dicey Dungeons"](../games/a-f/dicey-dungeons.md)
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

- [`GAME-0570` — Cult of the Lamb](../games/a-f/cult-of-the-lamb.md)
- [`GAME-0649` — Drop Duchy](../games/a-f/drop-duchy.md)
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
- Переглянуто: `2026-10-04`

### Операційне визначення

Гравець витрачає поточну валюту дослідженого відрізка, щоб придбати один наявний у пропозиції актив або скористатися однією платною послугою.

### Включає

Торговців у забігах; крамниці кімнат у Blue Prince; крамниці матчу в Dota 2; магазини Grand Theft Auto V і Cyberpunk 2077; товари в Hollow Knight: Silksong; придбання спорядження під час замороження або відведеного на купівлю часу в Counter-Strike 2.

### Виключає

Безплатну нагороду; регулярні експлуатаційні витрати; недоступну пропозицію; торгівлю на ринку косметичних предметів.

### Ігри-носії

- [`GAME-0694` — "A Game About Digging A Hole"](../games/a-f/a-game-about-digging-a-hole.md)
- [`GAME-0124` — Against the Storm](../games/a-f/against-the-storm.md)
- [`GAME-0453` — Age of Mythology](../games/a-f/age-of-mythology.md)
- [`GAME-0511` — Animal Crossing: New Leaf](../games/a-f/animal-crossing-new-leaf.md)
- [`GAME-0148` — Baldur’s Gate 3](../games/a-f/baldurs-gate-3.md)
- [`GAME-0265` — Bloons TD 6](../games/a-f/bloons-td-6.md)
- [`GAME-0173` — Blue Prince](../games/a-f/blue-prince.md)
- [`GAME-0346` — Chrono Trigger](../games/a-f/chrono-trigger.md)
- [`GAME-0137` — Counter-Strike 2](../games/a-f/counter-strike-2.md)
- [`GAME-0218` — Counter-Strike](../games/a-f/counter-strike.md)
- [`GAME-0282` — Dead Cells](../games/a-f/dead-cells.md)
- [`GAME-0266` — Deep Rock Galactic](../games/a-f/deep-rock-galactic.md)
- [`GAME-0565` — Dome Keeper](../games/a-f/dome-keeper.md)
- [`GAME-0138` — Dota 2](../games/a-f/dota-2.md)
- [`GAME-0152` — Elden Ring](../games/a-f/elden-ring.md)
- [`GAME-0491` — Elite](../games/a-f/elite.md)
- [`GAME-0405` — Fable II](../games/a-f/fable-ii.md)
- [`GAME-0327` — Fable](../games/a-f/fable.md)
- [`GAME-0145` — Grand Theft Auto V](../games/g-l/grand-theft-auto-v.md)
- [`GAME-0251` — Hades](../games/g-l/hades.md)
- [`GAME-0444` — "Harvest Moon: Back to Nature"](../games/g-l/harvest-moon-back-to-nature.md)
- [`GAME-0150` — "Hollow Knight: Silksong"](../games/g-l/hollow-knight-silksong.md)
- [`GAME-0123` — Inscryption](../games/g-l/inscryption.md)
- [`GAME-0392` — Mario Party 2](../games/m-r/mario-party-2.md)
- [`GAME-0226` — "Need for Speed: Most Wanted (2005)"](../games/m-r/need-for-speed-most-wanted-2005.md)
- [`GAME-0298` — 'Planet Zoo: Console Edition'](../games/m-r/planet-zoo-console-edition.md)
- [`GAME-0463` — "Pokémon Gold Version"](../games/m-r/pokemon-gold-version.md)
- [`GAME-0336` — "Pokémon Red Version"](../games/m-r/pokemon-red-version.md)
- [`GAME-0446` — Railroad Tycoon II](../games/m-r/railroad-tycoon-ii.md)
- [`GAME-0165` — Red Dead Redemption 2](../games/m-r/red-dead-redemption-2.md)
- [`GAME-0270` — Risk of Rain 2](../games/m-r/risk-of-rain-2.md)
- [`GAME-0166` — Sid Meier’s Civilization VI](../games/s-z/sid-meiers-civilization-vi.md)
- [`GAME-0155` — Slay the Spire 2](../games/s-z/slay-the-spire-2.md)
- [`GAME-0120` — Slay the Spire](../games/s-z/slay-the-spire.md)
- [`GAME-0307` — Slime Rancher](../games/s-z/slime-rancher.md)
- [`GAME-0502` — South of Midnight](../games/s-z/south-of-midnight.md)
- [`GAME-0153` — Terraria](../games/s-z/terraria.md)
- [`GAME-0164` — "The Binding of Isaac: Rebirth"](../games/s-z/the-binding-of-isaac-rebirth.md)
- [`GAME-0343` — The Secret of Monkey Island](../games/s-z/the-secret-of-monkey-island.md)
- [`GAME-0461` — The Sims](../games/s-z/the-sims.md)
- [`GAME-0513` — Thief: The Dark Project](../games/s-z/thief-the-dark-project.md)
- [`GAME-0498` — Transport Fever 2](../games/s-z/transport-fever-2.md)

## ACT-131

- Назва: Витрачати один негайно дієвий предмет із особистого запасу
- Переглянуто: `2026-10-04`

### Операційне визначення

Гравець активує одну одиницю обмеженого запасу витратних предметів при собі, за потреби вказує дозволену ціль і остаточно витрачає одиницю після виконання її негайного ефекту.

### Включає

Випивання чи метання власного зілля Slay the Spire у дозволений момент бою.

### Виключає

Розіграш карти колоди; спорядження постійної реліквії; застосування предмета світу до механізму в ігровому світі.

### Ігри-носії

- [`GAME-0506` — Avowed](../games/a-f/avowed.md)
- [`GAME-0148` — Baldur’s Gate 3](../games/a-f/baldurs-gate-3.md)
- [`GAME-0256` — "BioShock™ Remastered"](../games/a-f/bioshock-remastered.md)
- [`GAME-0173` — Blue Prince](../games/a-f/blue-prince.md)
- [`GAME-0557` — "Boktai: The Sun Is in Your Hand"](../games/a-f/boktai-the-sun-is-in-your-hand.md)
- [`GAME-0144` — Clair Obscur: Expedition 33](../games/a-f/clair-obscur-expedition-33.md)
- [`GAME-0490` — Comix Zone](../games/a-f/comix-zone.md)
- [`GAME-0368` — Dead Rising](../games/a-f/dead-rising.md)
- [`GAME-0259` — "Dead Space (2023 remake)"](../games/a-f/dead-space-2023.md)
- [`GAME-0515` — Dino Crisis](../games/a-f/dino-crisis.md)
- [`GAME-0435` — EarthBound](../games/a-f/earthbound.md)
- [`GAME-0152` — Elden Ring](../games/a-f/elden-ring.md)
- [`GAME-0501` — F.E.A.R.](../games/a-f/fear.md)
- [`GAME-0338` — Final Fantasy VII](../games/a-f/final-fantasy-vii.md)
- [`GAME-0489` — Golden Sun](../games/g-l/golden-sun.md)
- [`GAME-0510` — Indiana Jones and the Great Circle](../games/g-l/indiana-jones-and-the-great-circle.md)
- [`GAME-0123` — Inscryption](../games/g-l/inscryption.md)
- [`GAME-0240` — "Kingdom Come: Deliverance II"](../games/g-l/kingdom-come-deliverance-ii.md)
- [`GAME-0530` — Lost Odyssey](../games/g-l/lost-odyssey.md)
- [`GAME-0392` — Mario Party 2](../games/m-r/mario-party-2.md)
- [`GAME-0273` — Max Payne 3](../games/m-r/max-payne-3.md)
- [`GAME-0389` — Mega Man 2](../games/m-r/mega-man-2.md)
- [`GAME-0260` — Metro Exodus](../games/m-r/metro-exodus.md)
- [`GAME-0297` — 'MONSTER HUNTER RISE'](../games/m-r/monster-hunter-rise.md)
- [`GAME-0151` — Monster Hunter Wilds](../games/m-r/monster-hunter-wilds.md)
- [`GAME-0207` — 'Monster Hunter: World'](../games/m-r/monster-hunter-world.md)
- [`GAME-0341` — "Ninja Gaiden Black"](../games/m-r/ninja-gaiden-black.md)
- [`GAME-0500` — Pacific Drive](../games/m-r/pacific-drive.md)
- [`GAME-0562` — Parasite Eve](../games/m-r/parasite-eve.md)
- [`GAME-0160` — "Pokémon Legends: Z-A"](../games/m-r/pokemon-legends-z-a.md)
- [`GAME-0518` — Pokémon Pokopia](../games/m-r/pokemon-pokopia.md)
- [`GAME-0536` — PRAGMATA](../games/m-r/pragmata.md)
- [`GAME-0165` — Red Dead Redemption 2](../games/m-r/red-dead-redemption-2.md)
- [`GAME-0280` — Resident Evil 2 (2019 remake)](../games/m-r/resident-evil-2-2019.md)
- [`GAME-0249` — Resident Evil 4 (2023 remake)](../games/m-r/resident-evil-4-2023.md)
- [`GAME-0512` — Resident Evil Requiem](../games/m-r/resident-evil-requiem.md)
- [`GAME-0330` — Silent Hill 2 (2024 remake)](../games/s-z/silent-hill-2-2024.md)
- [`GAME-0430` — Silent Hill](../games/s-z/silent-hill.md)
- [`GAME-0535` — Skies of Arcadia](../games/s-z/skies-of-arcadia.md)
- [`GAME-0155` — Slay the Spire 2](../games/s-z/slay-the-spire-2.md)
- [`GAME-0120` — Slay the Spire](../games/s-z/slay-the-spire.md)
- [`GAME-0621` — "Sonic Racing: CrossWorlds"](../games/s-z/sonic-racing-crossworlds.md)
- [`GAME-0153` — Terraria](../games/s-z/terraria.md)
- [`GAME-0164` — "The Binding of Isaac: Rebirth"](../games/s-z/the-binding-of-isaac-rebirth.md)
- [`GAME-0190` — "The Elder Scrolls V: Skyrim Special Edition"](../games/s-z/the-elder-scrolls-v-skyrim-special-edition.md)
- [`GAME-0553` — The Lost Vikings](../games/s-z/the-lost-vikings.md)
- [`GAME-0205` — "The Witcher 3: Wild Hunt"](../games/s-z/the-witcher-3-wild-hunt.md)
- [`GAME-0696` — "Tides of Tomorrow"](../games/s-z/tides-of-tomorrow.md)
- [`GAME-0451` — Tomb Raider (1996)](../games/s-z/tomb-raider-1996.md)
- [`GAME-0268` — Undertale](../games/s-z/undertale.md)
- [`GAME-0499` — Vagrant Story](../games/s-z/vagrant-story.md)

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

Креслення shapez 2, які копіюють схеми розміщення машин, конвеєрів, підйомників, труб або платформ і встановлюють інший працездатний екземпляр, сплачуючи передбачену налаштуваннями вартість в очках креслень, якщо така плата застосовується.

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

Придбання в shapez 2 рівнів машин, швидкості конвеєрів чи поїздів, місткості платформ, входів Vortex, дротів або інших уже доступних удосконалень крамниці.

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
- [`GAME-0453` — Age of Mythology](../games/a-f/age-of-mythology.md)
- [`GAME-0320` — "Animal Crossing: New Horizons"](../games/a-f/animal-crossing-new-horizons.md)
- [`GAME-0525` — "Anno 117: Pax Romana"](../games/a-f/anno-117-pax-romana.md)
- [`GAME-0132` — Anno 1800](../games/a-f/anno-1800.md)
- [`GAME-0397` — 'Command & Conquer: Red Alert 2'](../games/a-f/command-and-conquer-red-alert-2.md)
- [`GAME-0275` — Command & Conquer Remastered Collection](../games/a-f/command-and-conquer-remastered-collection.md)
- [`GAME-0209` — Cossacks 3](../games/a-f/cossacks-3.md)
- [`GAME-0629` — "Dark Cloud"](../games/a-f/dark-cloud.md)
- [`GAME-0504` — Frostpunk 2](../games/a-f/frostpunk-2.md)
- [`GAME-0130` — Frostpunk](../games/a-f/frostpunk.md)
- [`GAME-0410` — Halo Wars](../games/g-l/halo-wars.md)
- [`GAME-0335` — RollerCoaster Tycoon Deluxe](../games/m-r/rollercoaster-tycoon-deluxe.md)
- [`GAME-0166` — Sid Meier’s Civilization VI](../games/s-z/sid-meiers-civilization-vi.md)
- [`GAME-0469` — StarCraft](../games/s-z/starcraft.md)
- [`GAME-0370` — Theme Hospital](../games/s-z/theme-hospital.md)
- [`GAME-0133` — Timberborn](../games/s-z/timberborn.md)
- [`GAME-0498` — Transport Fever 2](../games/s-z/transport-fever-2.md)
- [`GAME-0701` — "Warcraft II: Tides of Darkness"](../games/s-z/warcraft-ii-tides-of-darkness.md)
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
- [`GAME-0453` — Age of Mythology](../games/a-f/age-of-mythology.md)
- [`GAME-0610` — "BALL x PIT"](../games/a-f/ball-x-pit.md)
- [`GAME-0570` — Cult of the Lamb](../games/a-f/cult-of-the-lamb.md)
- [`GAME-0146` — Cyberpunk 2077](../games/a-f/cyberpunk-2077.md)
- [`GAME-0282` — Dead Cells](../games/a-f/dead-cells.md)
- [`GAME-0504` — Frostpunk 2](../games/a-f/frostpunk-2.md)
- [`GAME-0130` — Frostpunk](../games/a-f/frostpunk.md)
- [`GAME-0145` — Grand Theft Auto V](../games/g-l/grand-theft-auto-v.md)
- [`GAME-0251` — Hades](../games/g-l/hades.md)
- [`GAME-0332` — "Heroes of Might and Magic III: Complete"](../games/g-l/heroes-of-might-and-magic-iii-complete.md)
- [`GAME-0125` — Oxygen Not Included](../games/m-r/oxygen-not-included.md)
- [`GAME-0535` — Skies of Arcadia](../games/s-z/skies-of-arcadia.md)
- [`GAME-0136` — "Surviving Mars: Relaunched"](../games/s-z/surviving-mars.md)
- [`GAME-0499` — Vagrant Story](../games/s-z/vagrant-story.md)
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

Вибір клітинки мапи й бонусів для вирушання перед заснуванням поселення в Against the Storm.

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
- [`GAME-0504` — Frostpunk 2](../games/a-f/frostpunk-2.md)
- [`GAME-0125` — Oxygen Not Included](../games/m-r/oxygen-not-included.md)
- [`GAME-0127` — RimWorld](../games/m-r/rimworld.md)
- [`GAME-0133` — Timberborn](../games/s-z/timberborn.md)

## ACT-145

- Назва: Налаштувати пріоритети працівника й доручення
- Переглянуто: `2026-08-24`

### Операційне визначення

Гравець змінює збережені налаштування, за якими один автономний агент ранжує види роботи або колонія ранжує одне створене доручення серед інших.

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

Гравець витрачає одне зароблене очко навички на допустимий вузол дерева передумов одного агента. Агент отримує дозвіл або бонус цього вузла як збережену зміну стану, а вартість його очікувань зростає.

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

- Назва: Розмістити план будівництва з вимогами до матеріалів
- Переглянуто: `2026-09-13`

### Операційне визначення

Гравець вибирає відому споруду й затверджує придатний контур розміщення, орієнтацію та специфікацію матеріалів як стійкий план, який має завершити окремий етап постачання й будівництва гравцем або працівником.

### Включає

Споруди, плитки, дроти, труби, мережі автоматизації, драбини й ракетні модулі в Oxygen Not Included; розміщення та обертання контуру Temporary Shelter у The Forest до внесення будь-якої потрібної палиці чи листка.

### Виключає

Миттєве встановлення готового об’єкта з інвентарю; позначення природного рельєфу для копання; застосування багатооб’єктного креслення.

### Ігри-носії

- [`GAME-0135` — "Captain of Industry"](../games/a-f/captain-of-industry.md)
- [`GAME-0570` — Cult of the Lamb](../games/a-f/cult-of-the-lamb.md)
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

- [`GAME-0573` — Dungeon Keeper](../games/a-f/dungeon-keeper.md)
- [`GAME-0126` — Dwarf Fortress](../games/a-f/dwarf-fortress.md)
- [`GAME-0127` — RimWorld](../games/m-r/rimworld.md)

## ACT-153

- Назва: Налаштувати спорядження, розклад і наказ загону
- Переглянуто: `2026-08-23`

### Операційне визначення

Гравець закріплює мешканців за військовою групою, задає її спорядження й розклад тренувань, а потім активує груповий наказ.

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

Гравець призначає одному автономному мешканцеві дозволену просторову область і одну чи кілька оголошених політик споживання, лікування або спорядження; ці призначення зберігаються.

### Включає

Дозволені області RimWorld разом із політиками харчування, уживання речовин, одягу й медикаментів.

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

- Назва: Сформувати завантажений караван і задати йому маршрут на мапі світу
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

Руйнування блока дерева чи каменю в режимі Survival Minecraft; видобування блока переднього плану, руйнування стіни заднього плану або вилучення встановлених меблів у Terraria.

### Виключає

Установлення фабричного об’єкта; переміщення вільного предмета; зафарбовування абстрактної комірки поля без вимоги фізичної досяжності.

### Ігри-носії

- [`GAME-0565` — Dome Keeper](../games/a-f/dome-keeper.md)
- [`GAME-0129` — Minecraft](../games/m-r/minecraft.md)
- [`GAME-0153` — Terraria](../games/s-z/terraria.md)

## ACT-160

- Назва: Викладати матеріали з інвентарю в сітці виготовлення
- Переглянуто: `2026-08-24`

### Операційне визначення

Гравець розміщує матеріали з інвентарю в певних комірках доступної сітки виготовлення й забирає результат рецепта, коли типи, кількість і просторове розташування матеріалів повністю відповідають одному заданому рецепту.

### Включає

Рецепти в сітці інвентарю 2 × 2 та на верстаку 3 × 3 у Minecraft.

### Виключає

Вибір рецепта ручного виготовлення в черзі; поєднання двох довільних предметів у руках; призначення рецепта автономній машині.

### Ігри-носії

- [`GAME-0129` — Minecraft](../games/m-r/minecraft.md)

## ACT-161

- Назва: Націлитися й ударити поточним інструментом досяжного ворога або об’єкт світу, який можна зламати
- Переглянуто: `2026-10-05`

### Операційне визначення

Гравець наводить споряджену зброю ближнього або дальнього бою на досяжного ворога чи на об'єкт світу, який можна зламати, й сам завдає удару чи виконує постріл, а не віддає наказ автономному загону й не вибирає абстрактну ціль картки.

### Включає

Атаки проти ворожих істот і Ender Dragon у режимі Survival Minecraft; прицільні постріли, удари ножем і атаки спорядженням у Counter-Strike 2; прицільні атаки вогнепальною й холодною зброєю проти досяжних ворогів у Cyberpunk 2077; основні атаки героїв Marvel Rivals проти видимих противників; прицільні удари голкою Hornet проти досяжних ворогів у Hollow Knight: Silksong; постріли стрільця й прямі атаки проти передбачених авторами ворогів у розділі 1 гри Split Fiction; удари ломом по склу маршруту Half-Life (1998); удари зброєю по перекритих дверях кімнати Collector у Dead Cells.

### Виключає

Автоматичний вогонь турелі; покрокову картку здібності; групову маршрутну точку, після якої бійці самі знаходять цілі; контекстну взаємодію з об'єктом оточення (ACT-341); міцність і руйнування самого об'єкта, які належать SYS-755.

### Ігри-носії

- [`GAME-0233` — 7 Days to Die](../games/0-9/7-days-to-die.md)
- [`GAME-0540` — Afterplace](../games/a-f/afterplace.md)
- [`GAME-0223` — Aion Classic](../games/a-f/aion-classic.md)
- [`GAME-0427` — Alan Wake](../games/a-f/alan-wake.md)
- [`GAME-0620` — Alien Soldier](../games/a-f/alien-soldier.md)
- [`GAME-0456` — Alone in the Dark](../games/a-f/alone-in-the-dark.md)
- [`GAME-0154` — Apex Legends](../games/a-f/apex-legends.md)
- [`GAME-0143` — ARC Raiders](../games/a-f/arc-raiders.md)
- [`GAME-0312` — ASTRO BOT](../games/a-f/astro-bot.md)
- [`GAME-0506` — Avowed](../games/a-f/avowed.md)
- [`GAME-0148` — Baldur’s Gate 3](../games/a-f/baldurs-gate-3.md)
- [`GAME-0386` — Banjo-Kazooie](../games/a-f/banjo-kazooie.md)
- [`GAME-0255` — "Batman: Arkham Asylum Game of the Year Edition"](../games/a-f/batman-arkham-asylum-game-of-the-year-edition.md)
- [`GAME-0662` — "Batman: Arkham Shadow"](../games/a-f/batman-arkham-shadow.md)
- [`GAME-0234` — Battlefield 2042](../games/a-f/battlefield-2042.md)
- [`GAME-0149` — Battlefield 6](../games/a-f/battlefield-6.md)
- [`GAME-0243` — Battlefield Hardline](../games/a-f/battlefield-hardline.md)
- [`GAME-0220` — Battlefield V](../games/a-f/battlefield-v.md)
- [`GAME-0256` — "BioShock™ Remastered"](../games/a-f/bioshock-remastered.md)
- [`GAME-0189` — "Black Myth: Wukong"](../games/a-f/black-myth-wukong.md)
- [`GAME-0308` — Bloodborne™](../games/a-f/bloodborne.md)
- [`GAME-0623` — "Blue Lightning"](../games/a-f/blue-lightning.md)
- [`GAME-0557` — "Boktai: The Sun Is in Your Hand"](../games/a-f/boktai-the-sun-is-in-your-hand.md)
- [`GAME-0546` — Burning Rangers](../games/a-f/burning-rangers.md)
- [`GAME-0222` — "Call of Juarez: Gunslinger"](../games/a-f/call-of-juarez-gunslinger.md)
- [`GAME-0347` — "Castlevania: Symphony of the Night"](../games/a-f/castlevania-symphony-of-the-night.md)
- [`GAME-0144` — Clair Obscur: Expedition 33](../games/a-f/clair-obscur-expedition-33.md)
- [`GAME-0490` — Comix Zone](../games/a-f/comix-zone.md)
- [`GAME-0429` — Commandos: Behind Enemy Lines](../games/a-f/commandos-behind-enemy-lines.md)
- [`GAME-0324` — Contra Force](../games/a-f/contra-force.md)
- [`GAME-0254` — CONTROL Ultimate Edition](../games/a-f/control-ultimate-edition.md)
- [`GAME-0137` — Counter-Strike 2](../games/a-f/counter-strike-2.md)
- [`GAME-0218` — Counter-Strike](../games/a-f/counter-strike.md)
- [`GAME-0359` — "Crimson Skies: High Road to Revenge"](../games/a-f/crimson-skies-high-road-to-revenge.md)
- [`GAME-0725` — "Crypt Custodian"](../games/a-f/crypt-custodian.md)
- [`GAME-0246` — Crysis Remastered](../games/a-f/crysis-remastered.md)
- [`GAME-0570` — Cult of the Lamb](../games/a-f/cult-of-the-lamb.md)
- [`GAME-0277` — Cuphead](../games/a-f/cuphead.md)
- [`GAME-0596` — "Custom Robo"](../games/a-f/custom-robo.md)
- [`GAME-0146` — Cyberpunk 2077](../games/a-f/cyberpunk-2077.md)
- [`GAME-0738` — "Dandara: Trials of Fear Edition"](../games/a-f/dandara-trials-of-fear-edition.md)
- [`GAME-0262` — DARK SOULS™ III](../games/a-f/dark-souls-iii.md)
- [`GAME-0295` — DARK SOULS™: REMASTERED](../games/a-f/dark-souls-remastered.md)
- [`GAME-0459` — Daxter](../games/a-f/daxter.md)
- [`GAME-0210` — DayZ](../games/a-f/dayz.md)
- [`GAME-0282` — Dead Cells](../games/a-f/dead-cells.md)
- [`GAME-0368` — Dead Rising](../games/a-f/dead-rising.md)
- [`GAME-0259` — "Dead Space (2023 remake)"](../games/a-f/dead-space-2023.md)
- [`GAME-0266` — Deep Rock Galactic](../games/a-f/deep-rock-galactic.md)
- [`GAME-0200` — Delta Force](../games/a-f/delta-force.md)
- [`GAME-0193` — Destiny 2](../games/a-f/destiny-2.md)
- [`GAME-0353` — "Deus Ex: Game of the Year Edition"](../games/a-f/deus-ex-game-of-the-year-edition.md)
- [`GAME-0322` — "Diablo II: Resurrected"](../games/a-f/diablo-ii-resurrected.md)
- [`GAME-0515` — Dino Crisis](../games/a-f/dino-crisis.md)
- [`GAME-0247` — Dishonored (2012)](../games/a-f/dishonored-2012.md)
- [`GAME-0565` — Dome Keeper](../games/a-f/dome-keeper.md)
- [`GAME-0186` — "Don’t Starve Together"](../games/a-f/dont-starve-together.md)
- [`GAME-0352` — DOOM (1993)](../games/a-f/doom-1993.md)
- [`GAME-0245` — DOOM (2016)](../games/a-f/doom-2016.md)
- [`GAME-0286` — DOOM Eternal](../games/a-f/doom-eternal.md)
- [`GAME-0592` — Dungeons of Hinterberg](../games/a-f/dungeons-of-hinterberg.md)
- [`GAME-0131` — Dyson Sphere Program](../games/a-f/dyson-sphere-program.md)
- [`GAME-0650` — Einhänder](../games/a-f/einhander.md)
- [`GAME-0152` — Elden Ring](../games/a-f/elden-ring.md)
- [`GAME-0491` — Elite](../games/a-f/elite.md)
- [`GAME-0473` — "Eternal Darkness: Sanity's Requiem"](../games/a-f/eternal-darkness-sanitys-requiem.md)
- [`GAME-0405` — Fable II](../games/a-f/fable-ii.md)
- [`GAME-0327` — Fable](../games/a-f/fable.md)
- [`GAME-0231` — Fallout 4](../games/a-f/fallout-4.md)
- [`GAME-0361` — Fallout: New Vegas](../games/a-f/fallout-new-vegas.md)
- [`GAME-0236` — Far Cry 3](../games/a-f/far-cry-3.md)
- [`GAME-0271` — Far Cry 5](../games/a-f/far-cry-5.md)
- [`GAME-0501` — F.E.A.R.](../games/a-f/fear.md)
- [`GAME-0188` — FINAL FANTASY XIV Online](../games/a-f/final-fantasy-xiv-online.md)
- [`GAME-0227` — Fortnite](../games/a-f/fortnite.md)
- [`GAME-0321` — Gears of War](../games/g-l/gears-of-war.md)
- [`GAME-0400` — "Geometry Wars: Retro Evolved"](../games/g-l/geometry-wars-retro-evolved.md)
- [`GAME-0550` — Ghost of Yōtei](../games/g-l/ghost-of-yotei.md)
- [`GAME-0263` — God of War](../games/g-l/god-of-war.md)
- [`GAME-0381` — GoldenEye 007](../games/g-l/goldeneye-007.md)
- [`GAME-0145` — Grand Theft Auto V](../games/g-l/grand-theft-auto-v.md)
- [`GAME-0314` — Grounded](../games/g-l/grounded.md)
- [`GAME-0560` — Gunstar Heroes](../games/g-l/gunstar-heroes.md)
- [`GAME-0532` — Hades II](../games/g-l/hades-ii.md)
- [`GAME-0251` — Hades](../games/g-l/hades.md)
- [`GAME-0239` — Half-Life (1998)](../games/g-l/half-life-1998.md)
- [`GAME-0212` — Half-Life 2](../games/g-l/half-life-2.md)
- [`GAME-0315` — Halo 3](../games/g-l/halo-3.md)
- [`GAME-0340` — "Halo: Combat Evolved Anniversary"](../games/g-l/halo-combat-evolved-anniversary.md)
- [`GAME-0159` — Helldivers 2](../games/g-l/helldivers-2.md)
- [`GAME-0516` — Hi-Fi RUSH](../games/g-l/hi-fi-rush.md)
- [`GAME-0248` — HITMAN World of Assassination](../games/g-l/hitman-world-of-assassination.md)
- [`GAME-0150` — "Hollow Knight: Silksong"](../games/g-l/hollow-knight-silksong.md)
- [`GAME-0274` — Hollow Knight](../games/g-l/hollow-knight.md)
- [`GAME-0399` — Ico](../games/g-l/ico.md)
- [`GAME-0510` — Indiana Jones and the Great Circle](../games/g-l/indiana-jones-and-the-great-circle.md)
- [`GAME-0585` — Into the Radius](../games/g-l/into-the-radius.md)
- [`GAME-0627` — "Killer7"](../games/g-l/killer7.md)
- [`GAME-0583` — "Kunitsu-Gami: Path of the Goddess"](../games/g-l/kunitsu-gami-path-of-the-goddess.md)
- [`GAME-0192` — Left 4 Dead 2](../games/g-l/left-4-dead-2.md)
- [`GAME-0290` — Lies of P](../games/g-l/lies-of-p.md)
- [`GAME-0219` — Lineage II](../games/g-l/lineage-ii.md)
- [`GAME-0147` — Marvel Rivals](../games/m-r/marvel-rivals.md)
- [`GAME-0323` — "Marvel’s Spider-Man 2"](../games/m-r/marvels-spider-man-2.md)
- [`GAME-0367` — Mass Effect 2 (Legendary Edition)](../games/m-r/mass-effect-2-legendary-edition.md)
- [`GAME-0238` — "Max Payne (2001)"](../games/m-r/max-payne-2001.md)
- [`GAME-0273` — Max Payne 3](../games/m-r/max-payne-3.md)
- [`GAME-0509` — MechAssault](../games/m-r/mechassault.md)
- [`GAME-0389` — Mega Man 2](../games/m-r/mega-man-2.md)
- [`GAME-0652` — Mega Man Battle Network](../games/m-r/mega-man-battle-network.md)
- [`GAME-0306` — METAL GEAR SOLID V: THE PHANTOM PAIN](../games/m-r/metal-gear-solid-v-the-phantom-pain.md)
- [`GAME-0339` — Metal Gear Solid](../games/m-r/metal-gear-solid.md)
- [`GAME-0462` — Metal Slug 3](../games/m-r/metal-slug-3.md)
- [`GAME-0728` — "Metal Warriors"](../games/m-r/metal-warriors.md)
- [`GAME-0260` — Metro Exodus](../games/m-r/metro-exodus.md)
- [`GAME-0474` — Metroid Fusion](../games/m-r/metroid-fusion.md)
- [`GAME-0355` — Metroid Prime](../games/m-r/metroid-prime.md)
- [`GAME-0129` — Minecraft](../games/m-r/minecraft.md)
- [`GAME-0297` — 'MONSTER HUNTER RISE'](../games/m-r/monster-hunter-rise.md)
- [`GAME-0151` — Monster Hunter Wilds](../games/m-r/monster-hunter-wilds.md)
- [`GAME-0207` — 'Monster Hunter: World'](../games/m-r/monster-hunter-world.md)
- [`GAME-0558` — Moss](../games/m-r/moss.md)
- [`GAME-0194` — "Mount & Blade II: Bannerlord"](../games/m-r/mount-and-blade-ii-bannerlord.md)
- [`GAME-0202` — "NARAKA: BLADEPOINT"](../games/m-r/naraka-bladepoint.md)
- [`GAME-0572` — Neon White](../games/m-r/neon-white.md)
- [`GAME-0588` — Neva](../games/m-r/neva.md)
- [`GAME-0527` — Nine Sols](../games/m-r/nine-sols.md)
- [`GAME-0341` — "Ninja Gaiden Black"](../games/m-r/ninja-gaiden-black.md)
- [`GAME-0299` — Nioh 2](../games/m-r/nioh-2.md)
- [`GAME-0296` — Noita](../games/m-r/noita.md)
- [`GAME-0483` — "Oddworld: Stranger's Wrath"](../games/m-r/oddworld-strangers-wrath.md)
- [`GAME-0382` — Ōkami HD](../games/m-r/okami-hd.md)
- [`GAME-0224` — Once Human](../games/m-r/once-human.md)
- [`GAME-0431` — Ori and the Blind Forest](../games/m-r/ori-and-the-blind-forest.md)
- [`GAME-0293` — Ori and the Will of the Wisps](../games/m-r/ori-and-the-will-of-the-wisps.md)
- [`GAME-0181` — Overwatch](../games/m-r/overwatch.md)
- [`GAME-0500` — Pacific Drive](../games/m-r/pacific-drive.md)
- [`GAME-0139` — Palworld](../games/m-r/palworld.md)
- [`GAME-0587` — Panzer Dragoon II Zwei](../games/m-r/panzer-dragoon-ii-zwei.md)
- [`GAME-0647` — Panzer Dragoon Saga](../games/m-r/panzer-dragoon-saga.md)
- [`GAME-0505` — Panzer Dragoon](../games/m-r/panzer-dragoon.md)
- [`GAME-0162` — Path of Exile 2](../games/m-r/path-of-exile-2.md)
- [`GAME-0201` — PAYDAY 2](../games/m-r/payday-2.md)
- [`GAME-0232` — PAYDAY 3](../games/m-r/payday-3.md)
- [`GAME-0291` — Persona 5 Royal](../games/m-r/persona-5-royal.md)
- [`GAME-0670` — "Phantom Dust"](../games/m-r/phantom-dust.md)
- [`GAME-0612` — "Pipistrello and the Cursed Yoyo"](../games/m-r/pipistrello-and-the-cursed-yoyo.md)
- [`GAME-0681` — "Power Stone 2"](../games/m-r/power-stone-2.md)
- [`GAME-0519` — Power Stone](../games/m-r/power-stone.md)
- [`GAME-0536` — PRAGMATA](../games/m-r/pragmata.md)
- [`GAME-0258` — "Prey (2017)"](../games/m-r/prey-2017.md)
- [`GAME-0344` — "Prince of Persia: The Sands of Time"](../games/m-r/prince-of-persia-the-sands-of-time.md)
- [`GAME-0142` — Project Zomboid](../games/m-r/project-zomboid.md)
- [`GAME-0358` — Psychonauts](../games/m-r/psychonauts.md)
- [`GAME-0140` — "PUBG: BATTLEGROUNDS"](../games/m-r/pubg-battlegrounds.md)
- [`GAME-0334` — Quake](../games/m-r/quake.md)
- [`GAME-0697` — "Radiant Silvergun"](../games/m-r/radiant-silvergun.md)
- [`GAME-0708` — "Rampart"](../games/m-r/rampart.md)
- [`GAME-0404` — Ratchet & Clank](../games/m-r/ratchet-and-clank.md)
- [`GAME-0508` — Ready or Not](../games/m-r/ready-or-not.md)
- [`GAME-0165` — Red Dead Redemption 2](../games/m-r/red-dead-redemption-2.md)
- [`GAME-0280` — Resident Evil 2 (2019 remake)](../games/m-r/resident-evil-2-2019.md)
- [`GAME-0249` — Resident Evil 4 (2023 remake)](../games/m-r/resident-evil-4-2023.md)
- [`GAME-0348` — "Resident Evil: Director’s Cut"](../games/m-r/resident-evil-directors-cut.md)
- [`GAME-0492` — "Resistance: Fall of Man"](../games/m-r/resistance-fall-of-man.md)
- [`GAME-0522` — Returnal](../games/m-r/returnal.md)
- [`GAME-0526` — Rez](../games/m-r/rez.md)
- [`GAME-0639` — "Rollerdrome"](../games/m-r/rollerdrome.md)
- [`GAME-0549` — Roto Force](../games/m-r/roto-force.md)
- [`GAME-0141` — Rust](../games/m-r/rust.md)
- [`GAME-0667` — "SAROS"](../games/s-z/saros.md)
- [`GAME-0288` — "Sekiro™: Shadows Die Twice - GOTY Edition"](../games/s-z/sekiro-shadows-die-twice.md)
- [`GAME-0272` — Serious Sam 4](../games/s-z/serious-sam-4.md)
- [`GAME-0237` — "Serious Sam HD: The First Encounter"](../games/s-z/serious-sam-hd-the-first-encounter.md)
- [`GAME-0356` — Shadow of the Colossus](../games/s-z/shadow-of-the-colossus.md)
- [`GAME-0618` — Shining Force III](../games/s-z/shining-force-iii.md)
- [`GAME-0487` — Sid Meier's Pirates!](../games/s-z/sid-meiers-pirates.md)
- [`GAME-0303` — Sifu](../games/s-z/sifu.md)
- [`GAME-0330` — Silent Hill 2 (2024 remake)](../games/s-z/silent-hill-2-2024.md)
- [`GAME-0430` — Silent Hill](../games/s-z/silent-hill.md)
- [`GAME-0417` — Sly Cooper and the Thievius Raccoonus](../games/s-z/sly-cooper-and-the-thievius-raccoonus.md)
- [`GAME-0502` — South of Midnight](../games/s-z/south-of-midnight.md)
- [`GAME-0360` — "Space Invaders"](../games/s-z/space-invaders.md)
- [`GAME-0548` — Space Station Silicon Valley](../games/s-z/space-station-silicon-valley.md)
- [`GAME-0412` — Splatoon 3](../games/s-z/splatoon-3.md)
- [`GAME-0157` — Split Fiction](../games/s-z/split-fiction.md)
- [`GAME-0170` — "S.T.A.L.K.E.R. 2: Heart of Chornobyl"](../games/s-z/stalker-2-heart-of-chornobyl.md)
- [`GAME-0424` — "Star Fox 64"](../games/s-z/star-fox-64.md)
- [`GAME-0230` — "STAR WARS Battlefront II (2017)"](../games/s-z/star-wars-battlefront-ii-2017.md)
- [`GAME-0213` — "STAR WARS Jedi: Fallen Order"](../games/s-z/star-wars-jedi-fallen-order.md)
- [`GAME-0225` — "STAR WARS: Squadrons"](../games/s-z/star-wars-squadrons.md)
- [`GAME-0331` — Starfield](../games/s-z/starfield.md)
- [`GAME-0466` — Streets of Rage 2](../games/s-z/streets-of-rage-2.md)
- [`GAME-0311` — Super Mario Bros.](../games/s-z/super-mario-bros.md)
- [`GAME-0337` — Super Metroid](../games/s-z/super-metroid.md)
- [`GAME-0567` — SUPERHOT VR](../games/s-z/superhot-vr.md)
- [`GAME-0313` — Tank 1990](../games/s-z/tank-1990.md)
- [`GAME-0187` — Team Fortress 2](../games/s-z/team-fortress-2.md)
- [`GAME-0695` — "Terranigma"](../games/s-z/terranigma.md)
- [`GAME-0153` — Terraria](../games/s-z/terraria.md)
- [`GAME-0164` — "The Binding of Isaac: Rebirth"](../games/s-z/the-binding-of-isaac-rebirth.md)
- [`GAME-0190` — "The Elder Scrolls V: Skyrim Special Edition"](../games/s-z/the-elder-scrolls-v-skyrim-special-edition.md)
- [`GAME-0292` — The Forest](../games/s-z/the-forest.md)
- [`GAME-0261` — The Last of Us Part I](../games/s-z/the-last-of-us-part-i.md)
- [`GAME-0458` — The Legend of Zelda: Link's Awakening](../games/s-z/the-legend-of-zelda-links-awakening.md)
- [`GAME-0395` — "The Legend of Zelda: Majora’s Mask"](../games/s-z/the-legend-of-zelda-majoras-mask.md)
- [`GAME-0363` — "The Legend of Zelda: Ocarina of Time"](../games/s-z/the-legend-of-zelda-ocarina-of-time.md)
- [`GAME-0593` — "The Legend of Zelda: The Minish Cap"](../games/s-z/the-legend-of-zelda-the-minish-cap.md)
- [`GAME-0325` — The Legend of Zelda](../games/s-z/the-legend-of-zelda.md)
- [`GAME-0553` — The Lost Vikings](../games/s-z/the-lost-vikings.md)
- [`GAME-0205` — "The Witcher 3: Wild Hunt"](../games/s-z/the-witcher-3-wild-hunt.md)
- [`GAME-0513` — Thief: The Dark Project](../games/s-z/thief-the-dark-project.md)
- [`GAME-0253` — "Titanfall 2"](../games/s-z/titanfall-2.md)
- [`GAME-0174` — Tom Clancy’s Rainbow Six Siege](../games/s-z/tom-clancys-rainbow-six-siege.md)
- [`GAME-0349` — "Tom Clancy’s Splinter Cell"](../games/s-z/tom-clancys-splinter-cell.md)
- [`GAME-0451` — Tomb Raider (1996)](../games/s-z/tomb-raider-1996.md)
- [`GAME-0250` — Tomb Raider (2013)](../games/s-z/tomb-raider-2013.md)
- [`GAME-0409` — 'Twisted Metal: Black'](../games/s-z/twisted-metal-black.md)
- [`GAME-0294` — V Rising](../games/s-z/v-rising.md)
- [`GAME-0197` — Valheim](../games/s-z/valheim.md)
- [`GAME-0184` — War Thunder](../games/s-z/war-thunder.md)
- [`GAME-0168` — Warframe](../games/s-z/warframe.md)
- [`GAME-0496` — "Warhammer 40,000: Space Marine 2"](../games/s-z/warhammer-40000-space-marine-2.md)
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
- [`GAME-0518` — Pokémon Pokopia](../games/m-r/pokemon-pokopia.md)
- [`GAME-0153` — Terraria](../games/s-z/terraria.md)
- [`GAME-0693` — "Void Stranger"](../games/s-z/void-stranger.md)

## ACT-163

- Назва: Кинути предмет-покажчик, щоб визначити напрямок у світі
- Переглянуто: `2026-08-24`

### Операційне визначення

Гравець використовує один витратний предмет-покажчик: той залишає руку й рухається в напрямку своєї поточної прихованої цілі в ігровому світі.

### Включає

Кидання Eye of Ender у Minecraft для пошуку найближчої фортеці.

### Виключає

Читання статичної мапи; постріл снарядом, що завдає шкоди; телепортацію до цілі.

### Ігри-носії

- [`GAME-0129` — Minecraft](../games/m-r/minecraft.md)

## ACT-164

- Назва: Вибрати предмет швидкого доступу для активної руки
- Переглянуто: `2026-10-05`

### Операційне визначення

Гравець вибирає одну зайняту комірку швидкого доступу, щоб її предмет або інструмент став активним засобом введення для наступної сумісної дії у світі.

### Включає

Вибір кирки, їжі, блока, Eye або Flint and Steel на панелі швидкого доступу Minecraft; перемикання між наявною зброєю, гранатами, ножем і C4 у Counter-Strike 2; перемикання комірок зброї в Cyberpunk 2077.

### Виключає

Переставляння складників рецепта; призначення інструмента автономному працівникові.

### Ігри-носії

- [`GAME-0233` — 7 Days to Die](../games/0-9/7-days-to-die.md)
- [`GAME-0257` — "Alien: Isolation"](../games/a-f/alien-isolation.md)
- [`GAME-0413` — Ape Escape](../games/a-f/ape-escape.md)
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
- [`GAME-0501` — F.E.A.R.](../games/a-f/fear.md)
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
- [`GAME-0510` — Indiana Jones and the Great Circle](../games/g-l/indiana-jones-and-the-great-circle.md)
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
- [`GAME-0500` — Pacific Drive](../games/m-r/pacific-drive.md)
- [`GAME-0139` — Palworld](../games/m-r/palworld.md)
- [`GAME-0201` — PAYDAY 2](../games/m-r/payday-2.md)
- [`GAME-0232` — PAYDAY 3](../games/m-r/payday-3.md)
- [`GAME-0203` — "PEAK"](../games/m-r/peak.md)
- [`GAME-0160` — "Pokémon Legends: Z-A"](../games/m-r/pokemon-legends-z-a.md)
- [`GAME-0258` — "Prey (2017)"](../games/m-r/prey-2017.md)
- [`GAME-0142` — Project Zomboid](../games/m-r/project-zomboid.md)
- [`GAME-0140` — "PUBG: BATTLEGROUNDS"](../games/m-r/pubg-battlegrounds.md)
- [`GAME-0334` — Quake](../games/m-r/quake.md)
- [`GAME-0404` — Ratchet & Clank](../games/m-r/ratchet-and-clank.md)
- [`GAME-0508` — Ready or Not](../games/m-r/ready-or-not.md)
- [`GAME-0165` — Red Dead Redemption 2](../games/m-r/red-dead-redemption-2.md)
- [`GAME-0249` — Resident Evil 4 (2023 remake)](../games/m-r/resident-evil-4-2023.md)
- [`GAME-0512` — Resident Evil Requiem](../games/m-r/resident-evil-requiem.md)
- [`GAME-0492` — "Resistance: Fall of Man"](../games/m-r/resistance-fall-of-man.md)
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
- [`GAME-0553` — The Lost Vikings](../games/s-z/the-lost-vikings.md)
- [`GAME-0513` — Thief: The Dark Project](../games/s-z/thief-the-dark-project.md)
- [`GAME-0253` — "Titanfall 2"](../games/s-z/titanfall-2.md)
- [`GAME-0174` — Tom Clancy’s Rainbow Six Siege](../games/s-z/tom-clancys-rainbow-six-siege.md)
- [`GAME-0250` — Tomb Raider (2013)](../games/s-z/tomb-raider-2013.md)
- [`GAME-0294` — V Rising](../games/s-z/v-rising.md)
- [`GAME-0197` — Valheim](../games/s-z/valheim.md)
- [`GAME-0168` — Warframe](../games/s-z/warframe.md)
- [`GAME-0496` — "Warhammer 40,000: Space Marine 2"](../games/s-z/warhammer-40000-space-marine-2.md)

## ACT-165

- Назва: Спожити придатну їжу для живлення персонажа
- Переглянуто: `2026-10-14`

### Операційне визначення

Гравець явно наказує керованому персонажеві з’їсти всю або частину придатної їжі з перенесеного запасу чи досяжного місця годування. Ця кількість їжі витрачається, а її поживна дія та пов’язані зміни стану застосовуються за правилами гри.

### Включає

Споживання їжі в режимі Survival Minecraft за достатнього голоду; споживання всієї або частини харчового предмета в Project Zomboid; споживання перенесеної порції в DayZ; їжу з казана в дослідженому маршруті Fortuna у Kingdom Come: Deliverance II.

### Виключає

Використання лікувального зілля; споживання напою лише для відновлення водного запасу; автоматичне годування автономного персонажа; виготовлення їжі; живлення через контакт рота, що поповнює ДНК й ріст замість явної команди з’їсти.

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

- [`GAME-0504` — Frostpunk 2](../games/a-f/frostpunk-2.md)
- [`GAME-0130` — Frostpunk](../games/a-f/frostpunk.md)
- [`GAME-0136` — "Surviving Mars: Relaunched"](../games/s-z/surviving-mars.md)

## ACT-167

- Назва: Підписати доступний незворотний закон
- Переглянуто: `2026-08-24`

### Операційне визначення

Гравець обирає доступний вузол у книзі законів, назавжди вводить у дію його правило та приймає всі наслідки для подальших гілок.

### Включає

Закони Адаптації у Frostpunk і взаємовиключні шляхи Порядку або Віри в гілці Purpose.

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

Увімкнення й вимкнення генератора Frostpunk, вибір його потужності й радіуса, форсований режим, розклад парового вузла та керування обігрівачами робочих місць.

### Виключає

Дослідження поліпшення опалення; розміщення споруди; призначення персоналу.

### Ігри-носії

- [`GAME-0504` — Frostpunk 2](../games/a-f/frostpunk-2.md)
- [`GAME-0130` — Frostpunk](../games/a-f/frostpunk.md)

## ACT-169

- Назва: Планувати орбітальний рій або мегаструктуру навколо зорі
- Переглянуто: `2026-08-24`

### Операційне визначення

Гравець створює або змінює збережений план орбітального будівництва: обирає зорю, шар чи орбіту й розміщує структурні елементи визначених типів, які згодом намагаються збудувати пускові системи.

### Включає

Налаштування орбіт рою Дайсона та креслення шарів, вузлів, каркасів і ділянок оболонки сфери Дайсона у Dyson Sphere Program.

### Виключає

Розміщення окремої споруди планетарної фабрики; запуск однієї наданої ракети; застосування креслення поверхневої фабрики.

### Ігри-носії

- [`GAME-0131` — Dyson Sphere Program](../games/a-f/dyson-sphere-program.md)

## ACT-170

- Назва: Переводити меха в режим польоту, космічного плавання або викривлення простору
- Переглянуто: `2026-08-24`

### Операційне визначення

Гравець переводить безпосередньо керованого меха з наземного руху у відкритий режим польоту або під час керування в космосі вмикає викривлення простору, витрачаючи один викривлювач.

### Включає

Зліт Ікара, планетарний політ, космічне плавання між планетами й застосування Space Warper у Dyson Sphere Program.

### Виключає

Вибір пункту призначення автономного логістичного судна; телепортацію між мапами; звичайне пересування поверхнею.

### Ігри-носії

- [`GAME-0131` — Dyson Sphere Program](../games/a-f/dyson-sphere-program.md)
- [`GAME-0509` — MechAssault](../games/m-r/mechassault.md)

## ACT-171

- Назва: Створити циклічний корабельний торговельний маршрут із вантажними наказами для кожного порту
- Переглянуто: `2026-08-24`

### Операційне визначення

Гравець створює або змінює постійний упорядкований цикл острівних портів для одного чи кількох кораблів і для кожної вантажної комірки задає товар та кількість, яку слід завантажити або вивантажити на кожній зупинці.

### Включає

Торговельні маршрути Anno 1800 з упорядкованими портами та окремим завантаженням і вивантаженням для кожної вантажної комірки, зокрема забиранням товару з урахуванням мінімального запасу на острові.

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

Послідовне підвищення осель у Anno 1800: від фермерів до робітників, ремісників, інженерів та інвесторів, коли стан базових потреб і заселеність оселі це дозволяють.

### Виключає

Автоматичне збільшення кількості мешканців у межах однієї верстви; будівництво нової оселі; відкриття споруд після досягнення порога населення.

### Ігри-носії

- [`GAME-0525` — "Anno 117: Pax Romana"](../games/a-f/anno-117-pax-romana.md)
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

Гравець витрачає накопичені поселенням очки науки на один допустимий запис каталогу; після цього цей запис залишається доступним на поточній мапі.

### Включає

Відкриття споруд і «Рекультиватора Землі» у Timberborn.

### Виключає

Вибір дослідження, яке ще треба виконати; умову чисельності населення; метапоступ, що зберігається між мапами.

### Ігри-носії

- [`GAME-0133` — Timberborn](../games/s-z/timberborn.md)

## ACT-176

- Назва: З’єднати й налаштувати локальний сигнал автоматизації
- Переглянуто: `2026-08-24`

### Операційне визначення

Гравець з’єднує вихід датчика, логічного елемента або ретранслятора із сумісною ціллю та задає сталі пороги чи логічні правила.

### Включає

Датчики Timberborn, що керують насосами, шлюзами або клапанами.

### Виключає

Ручне перемикання; вибір виробничого рецепта; приховані програмні сценарії.

### Ігри-носії

- [`GAME-0133` — Timberborn](../games/s-z/timberborn.md)

## ACT-177

- Назва: Налаштувати зону, парк і вантажі диспетчерського осередку
- Переглянуто: `2026-08-24`

### Операційне визначення

Гравець задає постійному диспетчерському осередку територію роботи, доступну техніку, джерела, одержувачів, види вантажів або пороги запасів, після чого осередок самостійно відправляє придатний транспорт.

### Включає

Будівельні контори Workers & Resources: Soviet Republic із заданими джерелами й ділянками робіт та розподільчі контори з правилами постачання, попиту, ресурсів і відсотка заповнення складів; вежі керування шахтою в Captain of Industry.

### Виключає

Редагування впорядкованого маршруту одного транспортного засобу; розміщення самого диспетчерського осередку; безпосереднє керування доставленням.

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

- Назва: Укласти острівну торговельну угоду або контракт постачання
- Переглянуто: `2026-08-24`

### Операційне визначення

Гравець вибирає показану торговельну пропозицію острова й підтверджує або один негайний обмін, або збережений контракт обміну експорту на імпорт, подальші вантажні цикли якого витрачають визначений інституційний ресурс.

### Включає

Разові обміни в Captain of Industry та контракти із селами в цій грі. За контрактами витрачається Unity, а для повторюваних потоків використовуються сумісні модулі вантажного термінала та кораблі.

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

Налаштування повторюваного торговельного маршруту; безпосереднє пілотування космічного апарата; запуск однієї промислової ракети з незмінним вантажем.

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

- [`GAME-0504` — Frostpunk 2](../games/a-f/frostpunk-2.md)
- [`GAME-0136` — "Surviving Mars: Relaunched"](../games/s-z/surviving-mars.md)

## ACT-183

- Назва: Перезарядити активну магазинну зброю з резерву набоїв
- Переглянуто: `2026-10-05`

### Операційне визначення

Гравець витрачає час, щоб перенести набої з резерву до активної зброї та наповнити її магазин; під час цієї дії зброя тимчасово не готова стріляти.

### Включає

Ручне перезаряджання вогнепальної зброї в Counter-Strike 2 і Cyberpunk 2077.

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
- [`GAME-0501` — F.E.A.R.](../games/a-f/fear.md)
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
- [`GAME-0483` — "Oddworld: Stranger's Wrath"](../games/m-r/oddworld-strangers-wrath.md)
- [`GAME-0181` — Overwatch](../games/m-r/overwatch.md)
- [`GAME-0562` — Parasite Eve](../games/m-r/parasite-eve.md)
- [`GAME-0201` — PAYDAY 2](../games/m-r/payday-2.md)
- [`GAME-0232` — PAYDAY 3](../games/m-r/payday-3.md)
- [`GAME-0258` — "Prey (2017)"](../games/m-r/prey-2017.md)
- [`GAME-0140` — "PUBG: BATTLEGROUNDS"](../games/m-r/pubg-battlegrounds.md)
- [`GAME-0508` — Ready or Not](../games/m-r/ready-or-not.md)
- [`GAME-0165` — Red Dead Redemption 2](../games/m-r/red-dead-redemption-2.md)
- [`GAME-0280` — Resident Evil 2 (2019 remake)](../games/m-r/resident-evil-2-2019.md)
- [`GAME-0249` — Resident Evil 4 (2023 remake)](../games/m-r/resident-evil-4-2023.md)
- [`GAME-0492` — "Resistance: Fall of Man"](../games/m-r/resistance-fall-of-man.md)
- [`GAME-0272` — Serious Sam 4](../games/s-z/serious-sam-4.md)
- [`GAME-0170` — "S.T.A.L.K.E.R. 2: Heart of Chornobyl"](../games/s-z/stalker-2-heart-of-chornobyl.md)
- [`GAME-0187` — Team Fortress 2](../games/s-z/team-fortress-2.md)
- [`GAME-0261` — The Last of Us Part I](../games/s-z/the-last-of-us-part-i.md)
- [`GAME-0253` — "Titanfall 2"](../games/s-z/titanfall-2.md)
- [`GAME-0174` — Tom Clancy’s Rainbow Six Siege](../games/s-z/tom-clancys-rainbow-six-siege.md)
- [`GAME-0250` — Tomb Raider (2013)](../games/s-z/tomb-raider-2013.md)
- [`GAME-0168` — Warframe](../games/s-z/warframe.md)
- [`GAME-0496` — "Warhammer 40,000: Space Marine 2"](../games/s-z/warhammer-40000-space-marine-2.md)
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
- [`GAME-0501` — F.E.A.R.](../games/a-f/fear.md)
- [`GAME-0321` — Gears of War](../games/g-l/gears-of-war.md)
- [`GAME-0145` — Grand Theft Auto V](../games/g-l/grand-theft-auto-v.md)
- [`GAME-0315` — Halo 3](../games/g-l/halo-3.md)
- [`GAME-0340` — "Halo: Combat Evolved Anniversary"](../games/g-l/halo-combat-evolved-anniversary.md)
- [`GAME-0159` — Helldivers 2](../games/g-l/helldivers-2.md)
- [`GAME-0192` — Left 4 Dead 2](../games/g-l/left-4-dead-2.md)
- [`GAME-0140` — "PUBG: BATTLEGROUNDS"](../games/m-r/pubg-battlegrounds.md)
- [`GAME-0508` — Ready or Not](../games/m-r/ready-or-not.md)
- [`GAME-0492` — "Resistance: Fall of Man"](../games/m-r/resistance-fall-of-man.md)
- [`GAME-0253` — "Titanfall 2"](../games/s-z/titanfall-2.md)
- [`GAME-0174` — Tom Clancy’s Rainbow Six Siege](../games/s-z/tom-clancys-rainbow-six-siege.md)
- [`GAME-0496` — "Warhammer 40,000: Space Marine 2"](../games/s-z/warhammer-40000-space-marine-2.md)

## ACT-185

- Назва: Безперервно активувати або знешкоджувати встановлюваний пристрій раунду
- Переглянуто: `2026-10-13`

### Операційне визначення

Гравець, який відповідає умовам, безперервно утримує взаємодію з ціллю протягом визначеного часу, щоб активувати переносний пристрій раунду в дозволеному місці або знешкодити активний встановлений пристрій.

### Включає

Установлення й знешкодження C4 у Counter-Strike 2 та встановлення й вимкнення деактиватора у Rainbow Six Siege.

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

Взаємодоповнювальний поділ інформації про правила й поточний стан між ролями (ACT-099); спілкування поза грою без обмеженого командного каналу; автоматичні системні повідомлення.

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

Вибір героя та аспекту в режимі All Pick Dota 2; вибір легенди в Apex Legends із подальшим вибором переваг у межах матчу; вибір оперативника й фіксація спорядження раунду в Rainbow Six Siege.

### Виключає

Косметичне спорядження; зміну на іншого персонажа після початку активної гри.

### Ігри-носії

- [`GAME-0154` — Apex Legends](../games/a-f/apex-legends.md)
- [`GAME-0138` — Dota 2](../games/a-f/dota-2.md)
- [`GAME-0181` — Overwatch](../games/m-r/overwatch.md)
- [`GAME-0174` — Tom Clancy’s Rainbow Six Siege](../games/s-z/tom-clancys-rainbow-six-siege.md)

## ACT-189

- Назва: Віддати керованій одиниці контекстний наказ рухатися або атакувати
- Переглянуто: `2026-10-13`

### Операційне визначення

Гравець звертається до керованої одиниці й підтверджує точку призначення у світі, ціль або наказ рухатися з атакою, який потім виконує автономний пошук шляху.

### Включає

Накази герою рухатися, атакувати, рухатися з атакою, зупинитися й утримувати позицію в Dota 2.

### Виключає

Безпосереднє керування кожним кроком персонажа; застосування здібності; автономну поведінку кріпів на лініях.

### Ігри-носії

- [`GAME-0179` — Age of Empires II: Definitive Edition](../games/a-f/age-of-empires-ii-definitive-edition.md)
- [`GAME-0453` — Age of Mythology](../games/a-f/age-of-mythology.md)
- [`GAME-0397` — 'Command & Conquer: Red Alert 2'](../games/a-f/command-and-conquer-red-alert-2.md)
- [`GAME-0275` — Command & Conquer Remastered Collection](../games/a-f/command-and-conquer-remastered-collection.md)
- [`GAME-0429` — Commandos: Behind Enemy Lines](../games/a-f/commandos-behind-enemy-lines.md)
- [`GAME-0209` — Cossacks 3](../games/a-f/cossacks-3.md)
- [`GAME-0204` — "Crusader Kings III"](../games/a-f/crusader-kings-iii.md)
- [`GAME-0368` — Dead Rising](../games/a-f/dead-rising.md)
- [`GAME-0264` — Disco Elysium - The Final Cut](../games/a-f/disco-elysium-the-final-cut.md)
- [`GAME-0138` — Dota 2](../games/a-f/dota-2.md)
- [`GAME-0410` — Halo Wars](../games/g-l/halo-wars.md)
- [`GAME-0182` — Hearts of Iron IV](../games/g-l/hearts-of-iron-iv.md)
- [`GAME-0332` — "Heroes of Might and Magic III: Complete"](../games/g-l/heroes-of-might-and-magic-iii-complete.md)
- [`GAME-0517` — Homeworld](../games/g-l/homeworld.md)
- [`GAME-0583` — "Kunitsu-Gami: Path of the Goddess"](../games/g-l/kunitsu-gami-path-of-the-goddess.md)
- [`GAME-0367` — Mass Effect 2 (Legendary Edition)](../games/m-r/mass-effect-2-legendary-edition.md)
- [`GAME-0194` — "Mount & Blade II: Bannerlord"](../games/m-r/mount-and-blade-ii-bannerlord.md)
- [`GAME-0508` — Ready or Not](../games/m-r/ready-or-not.md)
- [`GAME-0317` — StarCraft II](../games/s-z/starcraft-ii.md)
- [`GAME-0469` — StarCraft](../games/s-z/starcraft.md)
- [`GAME-0287` — Stellaris](../games/s-z/stellaris.md)
- [`GAME-0191` — "Total War: WARHAMMER III"](../games/s-z/total-war-warhammer-iii.md)
- [`GAME-0658` — "Unicorn Overlord"](../games/s-z/unicorn-overlord.md)
- [`GAME-0701` — "Warcraft II: Tides of Darkness"](../games/s-z/warcraft-ii-tides-of-darkness.md)
- [`GAME-0328` — "Warcraft III: Reign of Chaos"](../games/s-z/warcraft-iii-reign-of-chaos.md)

## ACT-190

- Назва: Застосувати активну здібність персонажа або предмета
- Переглянуто: `2026-10-03`

### Операційне визначення

Гравець застосовує одну наразі доступну активну здібність персонажа або активну властивість переносного предмета й задає допустиму цільову одиницю, точку, вектор, напрям чи введення без окремої цілі, зокрема утримує команду протягом потрібного застосування.

### Включає

Заклинання, перемикачі та активні предмети Dota 2; здібності героїв і застосування ультимативних прийомів Marvel Rivals; прицільні, розміщувані та застосовувані без цілі класові пристрої Battlefield 6; Silk Skills і споряджені Tools Hollow Knight: Silksong із дозволеним напрямковим введенням чи без окремої цілі; утримування команди зосередження в Hollow Knight для відновлення здоров’я; кидання маяка стратагеми в Helldivers 2 до допустимої цілі у світі після введення коду стратагеми.

### Виключає

Автоматичний вибір цілі для атаки; пасивні ефекти; звичайну атаку зброєю; косметичні емоції.

### Ігри-носії

- [`GAME-0223` — Aion Classic](../games/a-f/aion-classic.md)
- [`GAME-0154` — Apex Legends](../games/a-f/apex-legends.md)
- [`GAME-0506` — Avowed](../games/a-f/avowed.md)
- [`GAME-0148` — Baldur’s Gate 3](../games/a-f/baldurs-gate-3.md)
- [`GAME-0234` — Battlefield 2042](../games/a-f/battlefield-2042.md)
- [`GAME-0149` — Battlefield 6](../games/a-f/battlefield-6.md)
- [`GAME-0220` — Battlefield V](../games/a-f/battlefield-v.md)
- [`GAME-0594` — "Bionic Bay"](../games/a-f/bionic-bay.md)
- [`GAME-0189` — "Black Myth: Wukong"](../games/a-f/black-myth-wukong.md)
- [`GAME-0254` — CONTROL Ultimate Edition](../games/a-f/control-ultimate-edition.md)
- [`GAME-0277` — Cuphead](../games/a-f/cuphead.md)
- [`GAME-0259` — "Dead Space (2023 remake)"](../games/a-f/dead-space-2023.md)
- [`GAME-0200` — Delta Force](../games/a-f/delta-force.md)
- [`GAME-0193` — Destiny 2](../games/a-f/destiny-2.md)
- [`GAME-0565` — Dome Keeper](../games/a-f/dome-keeper.md)
- [`GAME-0286` — DOOM Eternal](../games/a-f/doom-eternal.md)
- [`GAME-0138` — Dota 2](../games/a-f/dota-2.md)
- [`GAME-0592` — Dungeons of Hinterberg](../games/a-f/dungeons-of-hinterberg.md)
- [`GAME-0188` — FINAL FANTASY XIV Online](../games/a-f/final-fantasy-xiv-online.md)
- [`GAME-0532` — Hades II](../games/g-l/hades-ii.md)
- [`GAME-0251` — Hades](../games/g-l/hades.md)
- [`GAME-0159` — Helldivers 2](../games/g-l/helldivers-2.md)
- [`GAME-0150` — "Hollow Knight: Silksong"](../games/g-l/hollow-knight-silksong.md)
- [`GAME-0274` — Hollow Knight](../games/g-l/hollow-knight.md)
- [`GAME-0408` — Kirby's Adventure](../games/g-l/kirbys-adventure.md)
- [`GAME-0219` — Lineage II](../games/g-l/lineage-ii.md)
- [`GAME-0309` — "Mario Kart 8 Deluxe"](../games/m-r/mario-kart-8-deluxe.md)
- [`GAME-0147` — Marvel Rivals](../games/m-r/marvel-rivals.md)
- [`GAME-0323` — "Marvel’s Spider-Man 2"](../games/m-r/marvels-spider-man-2.md)
- [`GAME-0367` — Mass Effect 2 (Legendary Edition)](../games/m-r/mass-effect-2-legendary-edition.md)
- [`GAME-0355` — Metroid Prime](../games/m-r/metroid-prime.md)
- [`GAME-0297` — 'MONSTER HUNTER RISE'](../games/m-r/monster-hunter-rise.md)
- [`GAME-0202` — "NARAKA: BLADEPOINT"](../games/m-r/naraka-bladepoint.md)
- [`GAME-0527` — Nine Sols](../games/m-r/nine-sols.md)
- [`GAME-0299` — Nioh 2](../games/m-r/nioh-2.md)
- [`GAME-0181` — Overwatch](../games/m-r/overwatch.md)
- [`GAME-0201` — PAYDAY 2](../games/m-r/payday-2.md)
- [`GAME-0232` — PAYDAY 3](../games/m-r/payday-3.md)
- [`GAME-0561` — Psychonauts 2](../games/m-r/psychonauts-2.md)
- [`GAME-0526` — Rez](../games/m-r/rez.md)
- [`GAME-0270` — Risk of Rain 2](../games/m-r/risk-of-rain-2.md)
- [`GAME-0502` — South of Midnight](../games/s-z/south-of-midnight.md)
- [`GAME-0548` — Space Station Silicon Valley](../games/s-z/space-station-silicon-valley.md)
- [`GAME-0412` — Splatoon 3](../games/s-z/splatoon-3.md)
- [`GAME-0213` — "STAR WARS Jedi: Fallen Order"](../games/s-z/star-wars-jedi-fallen-order.md)
- [`GAME-0187` — Team Fortress 2](../games/s-z/team-fortress-2.md)
- [`GAME-0164` — "The Binding of Isaac: Rebirth"](../games/s-z/the-binding-of-isaac-rebirth.md)
- [`GAME-0190` — "The Elder Scrolls V: Skyrim Special Edition"](../games/s-z/the-elder-scrolls-v-skyrim-special-edition.md)
- [`GAME-0553` — The Lost Vikings](../games/s-z/the-lost-vikings.md)
- [`GAME-0205` — "The Witcher 3: Wild Hunt"](../games/s-z/the-witcher-3-wild-hunt.md)
- [`GAME-0253` — "Titanfall 2"](../games/s-z/titanfall-2.md)
- [`GAME-0174` — Tom Clancy’s Rainbow Six Siege](../games/s-z/tom-clancys-rainbow-six-siege.md)
- [`GAME-0328` — "Warcraft III: Reign of Chaos"](../games/s-z/warcraft-iii-reign-of-chaos.md)
- [`GAME-0168` — Warframe](../games/s-z/warframe.md)
- [`GAME-0488` — wipEout](../games/s-z/wipeout.md)
- [`GAME-0221` — World of Warcraft](../games/s-z/world-of-warcraft.md)

## ACT-191

- Назва: Витратити одне очко розвитку персонажа
- Переглянуто: `2026-08-24`

### Операційне визначення

Гравець витрачає одне доступне очко на відкритий ступінь здібності, характеристику, талант або вузол дерева розвитку, змінюючи можливості персонажа на поточний матч чи подальше проходження.

### Включає

Вибір здібностей і талантів у Dota 2; розподіл розвитку персонажа в Clair Obscur, Cyberpunk 2077 і Baldur’s Gate 3; розподіл очок дерева навичок в ARC Raiders; розподіл очок Spark у Black Myth: Wukong.

### Виключає

Придбання предмета; автоматичні винагороди за рівень; косметичний розвиток усього облікового запису.

### Ігри-носії

- [`GAME-0154` — Apex Legends](../games/a-f/apex-legends.md)
- [`GAME-0143` — ARC Raiders](../games/a-f/arc-raiders.md)
- [`GAME-0506` — Avowed](../games/a-f/avowed.md)
- [`GAME-0148` — Baldur’s Gate 3](../games/a-f/baldurs-gate-3.md)
- [`GAME-0189` — "Black Myth: Wukong"](../games/a-f/black-myth-wukong.md)
- [`GAME-0222` — "Call of Juarez: Gunslinger"](../games/a-f/call-of-juarez-gunslinger.md)
- [`GAME-0144` — Clair Obscur: Expedition 33](../games/a-f/clair-obscur-expedition-33.md)
- [`GAME-0146` — Cyberpunk 2077](../games/a-f/cyberpunk-2077.md)
- [`GAME-0353` — "Deus Ex: Game of the Year Edition"](../games/a-f/deus-ex-game-of-the-year-edition.md)
- [`GAME-0322` — "Diablo II: Resurrected"](../games/a-f/diablo-ii-resurrected.md)
- [`GAME-0545` — Dispatch](../games/a-f/dispatch.md)
- [`GAME-0138` — Dota 2](../games/a-f/dota-2.md)
- [`GAME-0332` — "Heroes of Might and Magic III: Complete"](../games/g-l/heroes-of-might-and-magic-iii-complete.md)
- [`GAME-0181` — Overwatch](../games/m-r/overwatch.md)
- [`GAME-0562` — Parasite Eve](../games/m-r/parasite-eve.md)
- [`GAME-0162` — Path of Exile 2](../games/m-r/path-of-exile-2.md)
- [`GAME-0213` — "STAR WARS Jedi: Fallen Order"](../games/s-z/star-wars-jedi-fallen-order.md)
- [`GAME-0191` — "Total War: WARHAMMER III"](../games/s-z/total-war-warhammer-iii.md)
- [`GAME-0328` — "Warcraft III: Reign of Chaos"](../games/s-z/warcraft-iii-reign-of-chaos.md)

## ACT-192

- Назва: Налаштувати переміщення зі сховку або доставлення кур’єром
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

Гравець через поточну взаємодію у світі або бою застосовує й витрачає на придатну дику істоту один пристрій захоплення, який має при собі, запускаючи перевірку захоплення замість звичайної атаки.

### Включає

Кидок Pal Sphere в ослабленого дикого пала в Palworld; кидок Poké Ball безпосередньо або після ослаблення придатного дикого покемона в Pokémon Legends: Z-A; вибір Poké Ball через бойову команду ITEM проти придатного дикого покемона в Pokémon Red Version.

### Виключає

Перемогу над істотою; гарантоване сюжетне приєднання; переміщення вже захопленого супутника між складами груп.

### Ігри-носії

- [`GAME-0139` — Palworld](../games/m-r/palworld.md)
- [`GAME-0441` — Pokémon GO](../games/m-r/pokemon-go.md)
- [`GAME-0463` — "Pokémon Gold Version"](../games/m-r/pokemon-gold-version.md)
- [`GAME-0160` — "Pokémon Legends: Z-A"](../games/m-r/pokemon-legends-z-a.md)
- [`GAME-0336` — "Pokémon Red Version"](../games/m-r/pokemon-red-version.md)

## ACT-195

- Назва: Випустити одного переносного супутника або відкликати його
- Переглянуто: `2026-10-13`

### Операційне визначення

Гравець вибирає одного члена активного загону супутників і випускає його кидком у досяжному місці світу або повертає вже випущеного супутника до переносного стану.

### Включає

Випускання й відкликання пала з активного загону під час дослідження або бою в Palworld; вибір і випускання поточного партнера із загону в Pokémon Legends: Z-A.

### Виключає

Призначення пала на роботу на базі; безпосереднє керування рухом персонажа; захоплення нової істоти.

### Ігри-носії

- [`GAME-0139` — Palworld](../games/m-r/palworld.md)
- [`GAME-0160` — "Pokémon Legends: Z-A"](../games/m-r/pokemon-legends-z-a.md)

## ACT-196

- Назва: Перемістити захопленого супутника між обмеженими списками
- Переглянуто: `2026-10-13`

### Операційне визначення

Через постійний засіб керування гравець переводить одного захопленого супутника між резервним сховищем, обмеженим активним загоном і будь-яким доступним списком призначень, передбаченим правилами.

### Включає

Переміщення через Palbox між сховищем палів, загоном і призначеннями на базі; переміщення між Boxes і загоном із шести учасників у Pokémon Legends: Z-A.

### Виключає

Захоплення дикої істоти; тимчасове випускання супутника у світ; розведення двох істот зі сховища.

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

Самостійні звичайні атаки напарника; пасивну робочу придатність; безпосереднє використання зброї гравцем.

### Ігри-носії

- [`GAME-0263` — God of War](../games/g-l/god-of-war.md)
- [`GAME-0139` — Palworld](../games/m-r/palworld.md)

## ACT-198

- Назва: Покинути літак і керувати повітряним висадженням
- Переглянуто: `2026-08-24`

### Операційне визначення

Гравець обирає мить виходу з рухомого транспортного літака, керує персонажем під час вільного падіння й польоту з парашутом і так визначає досяжну початкову область до переходу до звичайного наземного руху.

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
- Переглянуто: `2026-10-05`

### Операційне визначення

Гравець обирає один досяжний предмет або предмет, який уже має при собі, і переносить його до сумісної комірки стосу, зброї, модуля, захисту чи сховища, за потреби замінюючи споряджений предмет.

### Включає

Взаємодія зі здобиччю на землі та перенесення чи спорядження через інвентар вогнепальної зброї, набоїв, приєднуваних деталей, броні, наплічників і витратних предметів у PUBG; перенесення здобичі зі світу й спорядження через інвентар у Cyberpunk 2077.

### Виключає

Автоматичне підбирання через контакт; придбання предмета для раунду; виготовлення предмета; збирання абстрактного жетона рахунку.

### Ігри-носії

- [`GAME-0233` — 7 Days to Die](../games/0-9/7-days-to-die.md)
- [`GAME-0257` — "Alien: Isolation"](../games/a-f/alien-isolation.md)
- [`GAME-0456` — Alone in the Dark](../games/a-f/alone-in-the-dark.md)
- [`GAME-0320` — "Animal Crossing: New Horizons"](../games/a-f/animal-crossing-new-horizons.md)
- [`GAME-0511` — Animal Crossing: New Leaf](../games/a-f/animal-crossing-new-leaf.md)
- [`GAME-0154` — Apex Legends](../games/a-f/apex-legends.md)
- [`GAME-0143` — ARC Raiders](../games/a-f/arc-raiders.md)
- [`GAME-0506` — Avowed](../games/a-f/avowed.md)
- [`GAME-0148` — Baldur’s Gate 3](../games/a-f/baldurs-gate-3.md)
- [`GAME-0220` — Battlefield V](../games/a-f/battlefield-v.md)
- [`GAME-0256` — "BioShock™ Remastered"](../games/a-f/bioshock-remastered.md)
- [`GAME-0557` — "Boktai: The Sun Is in Your Hand"](../games/a-f/boktai-the-sun-is-in-your-hand.md)
- [`GAME-0222` — "Call of Juarez: Gunslinger"](../games/a-f/call-of-juarez-gunslinger.md)
- [`GAME-0347` — "Castlevania: Symphony of the Night"](../games/a-f/castlevania-symphony-of-the-night.md)
- [`GAME-0555` — Chibi-Robo!](../games/a-f/chibi-robo.md)
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
- [`GAME-0473` — "Eternal Darkness: Sanity's Requiem"](../games/a-f/eternal-darkness-sanitys-requiem.md)
- [`GAME-0231` — Fallout 4](../games/a-f/fallout-4.md)
- [`GAME-0361` — Fallout: New Vegas](../games/a-f/fallout-new-vegas.md)
- [`GAME-0501` — F.E.A.R.](../games/a-f/fear.md)
- [`GAME-0227` — Fortnite](../games/a-f/fortnite.md)
- [`GAME-0321` — Gears of War](../games/g-l/gears-of-war.md)
- [`GAME-0239` — Half-Life (1998)](../games/g-l/half-life-1998.md)
- [`GAME-0212` — Half-Life 2](../games/g-l/half-life-2.md)
- [`GAME-0315` — Halo 3](../games/g-l/halo-3.md)
- [`GAME-0340` — "Halo: Combat Evolved Anniversary"](../games/g-l/halo-combat-evolved-anniversary.md)
- [`GAME-0240` — "Kingdom Come: Deliverance II"](../games/g-l/kingdom-come-deliverance-ii.md)
- [`GAME-0192` — Left 4 Dead 2](../games/g-l/left-4-dead-2.md)
- [`GAME-0219` — Lineage II](../games/g-l/lineage-ii.md)
- [`GAME-0530` — Lost Odyssey](../games/g-l/lost-odyssey.md)
- [`GAME-0367` — Mass Effect 2 (Legendary Edition)](../games/m-r/mass-effect-2-legendary-edition.md)
- [`GAME-0238` — "Max Payne (2001)"](../games/m-r/max-payne-2001.md)
- [`GAME-0273` — Max Payne 3](../games/m-r/max-payne-3.md)
- [`GAME-0260` — Metro Exodus](../games/m-r/metro-exodus.md)
- [`GAME-0194` — "Mount & Blade II: Bannerlord"](../games/m-r/mount-and-blade-ii-bannerlord.md)
- [`GAME-0202` — "NARAKA: BLADEPOINT"](../games/m-r/naraka-bladepoint.md)
- [`GAME-0296` — Noita](../games/m-r/noita.md)
- [`GAME-0500` — Pacific Drive](../games/m-r/pacific-drive.md)
- [`GAME-0562` — Parasite Eve](../games/m-r/parasite-eve.md)
- [`GAME-0162` — Path of Exile 2](../games/m-r/path-of-exile-2.md)
- [`GAME-0201` — PAYDAY 2](../games/m-r/payday-2.md)
- [`GAME-0232` — PAYDAY 3](../games/m-r/payday-3.md)
- [`GAME-0203` — "PEAK"](../games/m-r/peak.md)
- [`GAME-0463` — "Pokémon Gold Version"](../games/m-r/pokemon-gold-version.md)
- [`GAME-0258` — "Prey (2017)"](../games/m-r/prey-2017.md)
- [`GAME-0142` — Project Zomboid](../games/m-r/project-zomboid.md)
- [`GAME-0140` — "PUBG: BATTLEGROUNDS"](../games/m-r/pubg-battlegrounds.md)
- [`GAME-0280` — Resident Evil 2 (2019 remake)](../games/m-r/resident-evil-2-2019.md)
- [`GAME-0348` — "Resident Evil: Director’s Cut"](../games/m-r/resident-evil-directors-cut.md)
- [`GAME-0512` — Resident Evil Requiem](../games/m-r/resident-evil-requiem.md)
- [`GAME-0522` — Returnal](../games/m-r/returnal.md)
- [`GAME-0141` — Rust](../games/m-r/rust.md)
- [`GAME-0598` — "Sega Bass Fishing"](../games/s-z/sega-bass-fishing.md)
- [`GAME-0170` — "S.T.A.L.K.E.R. 2: Heart of Chornobyl"](../games/s-z/stalker-2-heart-of-chornobyl.md)
- [`GAME-0230` — "STAR WARS Battlefront II (2017)"](../games/s-z/star-wars-battlefront-ii-2017.md)
- [`GAME-0331` — Starfield](../games/s-z/starfield.md)
- [`GAME-0362` — "The Elder Scrolls III: Morrowind"](../games/s-z/the-elder-scrolls-iii-morrowind.md)
- [`GAME-0190` — "The Elder Scrolls V: Skyrim Special Edition"](../games/s-z/the-elder-scrolls-v-skyrim-special-edition.md)
- [`GAME-0261` — The Last of Us Part I](../games/s-z/the-last-of-us-part-i.md)
- [`GAME-0458` — The Legend of Zelda: Link's Awakening](../games/s-z/the-legend-of-zelda-links-awakening.md)
- [`GAME-0363` — "The Legend of Zelda: Ocarina of Time"](../games/s-z/the-legend-of-zelda-ocarina-of-time.md)
- [`GAME-0285` — "The Long Dark"](../games/s-z/the-long-dark.md)
- [`GAME-0553` — The Lost Vikings](../games/s-z/the-lost-vikings.md)
- [`GAME-0205` — "The Witcher 3: Wild Hunt"](../games/s-z/the-witcher-3-wild-hunt.md)
- [`GAME-0250` — Tomb Raider (2013)](../games/s-z/tomb-raider-2013.md)
- [`GAME-0191` — "Total War: WARHAMMER III"](../games/s-z/total-war-warhammer-iii.md)
- [`GAME-0294` — V Rising](../games/s-z/v-rising.md)
- [`GAME-0499` — Vagrant Story](../games/s-z/vagrant-story.md)
- [`GAME-0197` — Valheim](../games/s-z/valheim.md)
- [`GAME-0221` — World of Warcraft](../games/s-z/world-of-warcraft.md)

## ACT-200

- Назва: Застосувати переривний предмет відновлення чи ремонту
- Переглянуто: `2026-08-24`

### Операційне визначення

Гравець починає застосування одного предмета відновлення або ремонту, який має при собі. Застосування потребує часу, а визначений миттєвий або поступовий ефект настає лише тоді, коли жодна скасувальна дія не перериває цей процес.

### Включає

Bandages, First Aid Kits, Med Kits, Energy Drinks, Painkillers і Adrenaline Syringes у PUBG; скінченну кількість ковтків із Gourd у Black Myth: Wukong; Vitalia, Armor Powder і набори для ремонту зброї у NARAKA: BLADEPOINT.

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
- [`GAME-0473` — "Eternal Darkness: Sanity's Requiem"](../games/a-f/eternal-darkness-sanitys-requiem.md)
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
- Переглянуто: `2026-10-05`

### Операційне визначення

Гравець займає вільне місце в транспорті або бойовій техніці, керує прискоренням і напрямком руху з місця водія чи пілота, може пересідати й сам обирає мить виходу.

### Включає

Керування наземною технікою Erangel або поїздка в ній у PUBG Normal Match; вхід, викрадення й керування дорожнім, водним або повітряним транспортом у Story Mode Grand Theft Auto V; керування власним або доступним транспортом у Cyberpunk 2077; безпосереднє керування транспортом для втечі у розділі 1 гри Split Fiction, поки напарник виконує окрему роль стрільця турелі.

### Виключає

Призначення автономного транспортного маршруту; транспортний літак висадження, яким гравець не може керувати; пересування персонажа пішки.

### Ігри-носії

- [`GAME-0289` — American Truck Simulator](../games/a-f/american-truck-simulator.md)
- [`GAME-0423` — "Banjo-Kazooie: Nuts & Bolts"](../games/a-f/banjo-kazooie-nuts-and-bolts.md)
- [`GAME-0234` — Battlefield 2042](../games/a-f/battlefield-2042.md)
- [`GAME-0149` — Battlefield 6](../games/a-f/battlefield-6.md)
- [`GAME-0220` — Battlefield V](../games/a-f/battlefield-v.md)
- [`GAME-0539` — Blast Corps](../games/a-f/blast-corps.md)
- [`GAME-0200` — Delta Force](../games/a-f/delta-force.md)
- [`GAME-0169` — Euro Truck Simulator 2](../games/a-f/euro-truck-simulator-2.md)
- [`GAME-0196` — Farming Simulator 25](../games/a-f/farming-simulator-25.md)
- [`GAME-0357` — "Grand Theft Auto: San Andreas"](../games/g-l/grand-theft-auto-san-andreas.md)
- [`GAME-0145` — Grand Theft Auto V](../games/g-l/grand-theft-auto-v.md)
- [`GAME-0214` — "Mafia (2002)"](../games/m-r/mafia-2002.md)
- [`GAME-0462` — Metal Slug 3](../games/m-r/metal-slug-3.md)
- [`GAME-0229` — "No Man’s Sky"](../games/m-r/no-mans-sky.md)
- [`GAME-0500` — Pacific Drive](../games/m-r/pacific-drive.md)
- [`GAME-0140` — "PUBG: BATTLEGROUNDS"](../games/m-r/pubg-battlegrounds.md)
- [`GAME-0165` — Red Dead Redemption 2](../games/m-r/red-dead-redemption-2.md)
- [`GAME-0492` — "Resistance: Fall of Man"](../games/m-r/resistance-fall-of-man.md)
- [`GAME-0157` — Split Fiction](../games/s-z/split-fiction.md)
- [`GAME-0178` — Subnautica](../games/s-z/subnautica.md)
- [`GAME-0568` — Teardown](../games/s-z/teardown.md)

## ACT-202

- Назва: Змінити положення або конфігурацію тіла персонажа
- Переглянуто: `2026-10-04`

### Операційне визначення

Гравець переводить керованого персонажа між стоянням, присіданням, лежанням, бічним нахилом або збереженою компактною конфігурацією тіла, змінюючи габарит зіткнень, доступні кути огляду чи дії інструмента, рух і, де це має значення, відкритість тіла або поводження зі зброєю без передавання керування іншому персонажу.

### Включає

Зміни положення тіла та визирання ліворуч або праворуч з-за укриття в PUBG; стояче й присіле положення для скритного руху або бою в Cyberpunk 2077; присідання й положення лежачи, щоб спрямувати мийний інструмент під низькі поверхні в PowerWash Simulator.

### Виключає

Звичайне переміщення місцевістю; зміну перспективи камери; автоматичне положення після відкидання; контекстну анімацію, що не змінює доступ, видимість чи іншу значущу можливість.

### Ігри-носії

- [`GAME-0243` — Battlefield Hardline](../games/a-f/battlefield-hardline.md)
- [`GAME-0557` — "Boktai: The Sun Is in Your Hand"](../games/a-f/boktai-the-sun-is-in-your-hand.md)
- [`GAME-0490` — Comix Zone](../games/a-f/comix-zone.md)
- [`GAME-0429` — Commandos: Behind Enemy Lines](../games/a-f/commandos-behind-enemy-lines.md)
- [`GAME-0324` — Contra Force](../games/a-f/contra-force.md)
- [`GAME-0246` — Crysis Remastered](../games/a-f/crysis-remastered.md)
- [`GAME-0146` — Cyberpunk 2077](../games/a-f/cyberpunk-2077.md)
- [`GAME-0459` — Daxter](../games/a-f/daxter.md)
- [`GAME-0494` — Dead or Alive 2](../games/a-f/dead-or-alive-2.md)
- [`GAME-0353` — "Deus Ex: Game of the Year Edition"](../games/a-f/deus-ex-game-of-the-year-edition.md)
- [`GAME-0247` — Dishonored (2012)](../games/a-f/dishonored-2012.md)
- [`GAME-0495` — Donkey Kong Country Returns](../games/a-f/donkey-kong-country-returns.md)
- [`GAME-0236` — Far Cry 3](../games/a-f/far-cry-3.md)
- [`GAME-0501` — F.E.A.R.](../games/a-f/fear.md)
- [`GAME-0560` — Gunstar Heroes](../games/g-l/gunstar-heroes.md)
- [`GAME-0340` — "Halo: Combat Evolved Anniversary"](../games/g-l/halo-combat-evolved-anniversary.md)
- [`GAME-0248` — HITMAN World of Assassination](../games/g-l/hitman-world-of-assassination.md)
- [`GAME-0575` — Metal Gear Acid](../games/m-r/metal-gear-acid.md)
- [`GAME-0306` — METAL GEAR SOLID V: THE PHANTOM PAIN](../games/m-r/metal-gear-solid-v-the-phantom-pain.md)
- [`GAME-0339` — Metal Gear Solid](../games/m-r/metal-gear-solid.md)
- [`GAME-0462` — Metal Slug 3](../games/m-r/metal-slug-3.md)
- [`GAME-0260` — Metro Exodus](../games/m-r/metro-exodus.md)
- [`GAME-0474` — Metroid Fusion](../games/m-r/metroid-fusion.md)
- [`GAME-0355` — Metroid Prime](../games/m-r/metroid-prime.md)
- [`GAME-0393` — Mortal Kombat II](../games/m-r/mortal-kombat-ii.md)
- [`GAME-0534` — PowerWash Simulator 2](../games/m-r/powerwash-simulator-2.md)
- [`GAME-0279` — PowerWash Simulator](../games/m-r/powerwash-simulator.md)
- [`GAME-0140` — "PUBG: BATTLEGROUNDS"](../games/m-r/pubg-battlegrounds.md)
- [`GAME-0722` — "QuackShot Starring Donald Duck"](../games/m-r/quackshot-starring-donald-duck.md)
- [`GAME-0508` — Ready or Not](../games/m-r/ready-or-not.md)
- [`GAME-0249` — Resident Evil 4 (2023 remake)](../games/m-r/resident-evil-4-2023.md)
- [`GAME-0512` — Resident Evil Requiem](../games/m-r/resident-evil-requiem.md)
- [`GAME-0492` — "Resistance: Fall of Man"](../games/m-r/resistance-fall-of-man.md)
- [`GAME-0288` — "Sekiro™: Shadows Die Twice - GOTY Edition"](../games/s-z/sekiro-shadows-die-twice.md)
- [`GAME-0455` — Soulcalibur](../games/s-z/soulcalibur.md)
- [`GAME-0412` — Splatoon 3](../games/s-z/splatoon-3.md)
- [`GAME-0230` — "STAR WARS Battlefront II (2017)"](../games/s-z/star-wars-battlefront-ii-2017.md)
- [`GAME-0337` — Super Metroid](../games/s-z/super-metroid.md)
- [`GAME-0568` — Teardown](../games/s-z/teardown.md)
- [`GAME-0366` — Tekken 3](../games/s-z/tekken-3.md)
- [`GAME-0283` — TEKKEN 8](../games/s-z/tekken-8.md)
- [`GAME-0190` — "The Elder Scrolls V: Skyrim Special Edition"](../games/s-z/the-elder-scrolls-v-skyrim-special-edition.md)
- [`GAME-0559` — The Last Guardian](../games/s-z/the-last-guardian.md)
- [`GAME-0261` — The Last of Us Part I](../games/s-z/the-last-of-us-part-i.md)
- [`GAME-0593` — "The Legend of Zelda: The Minish Cap"](../games/s-z/the-legend-of-zelda-the-minish-cap.md)
- [`GAME-0513` — Thief: The Dark Project](../games/s-z/thief-the-dark-project.md)
- [`GAME-0443` — Time Crisis](../games/s-z/time-crisis.md)
- [`GAME-0174` — Tom Clancy’s Rainbow Six Siege](../games/s-z/tom-clancys-rainbow-six-siege.md)
- [`GAME-0349` — "Tom Clancy’s Splinter Cell"](../games/s-z/tom-clancys-splinter-cell.md)
- [`GAME-0497` — Wario Land 4](../games/s-z/wario-land-4.md)

## ACT-203

- Назва: Викопати тактичне укриття в ґрунті, придатному для руйнування
- Переглянуто: `2026-08-24`

### Операційне визначення

Гравець спрямовує придатний інструмент або вибухівку на придатний для руйнування ґрунт світу й завдає удару з метою прибрати обмежений об’єм землі та створити прохідну виїмку або край укриття.

### Включає

Копання киркою та руйнування ґрунту гранатами, мінометом, Panzerfaust, C4 або вибухом транспорту на Erangel у PUBG Update 41.1.

### Виключає

Пошкодження ворога; руйнування будівлі; необмежене видобування вокселів; косметичні сліди без зміни геометрії зіткнень.

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

Гравець взаємодіє з досяжним об’єктом власності чи замком, щоб додати або вилучити особу зі списку доступу, установити чи ввести дані доступу або очистити поточний список.

### Включає

Додавання гравця до списку доступу Tool Cupboard і введення чи зміна коду Code Lock у Rust.

### Виключає

Відкривання дверей із уже наданим доступом; перенесення збережених предметів; права адміністратора сервера.

### Ігри-носії

- [`GAME-0141` — Rust](../games/m-r/rust.md)

## ACT-206

- Назва: Завантажити пристрій перероблення матеріалів і керувати його роботою
- Переглянуто: `2026-08-24`

### Операційне визначення

Гравець переносить сумісні вхідні матеріали й будь-яке потрібне паливо до досяжного пристрою перероблення, запускає або зупиняє його, якщо це передбачено, а згодом забирає стоси одержаних продуктів або залишків.

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

Гравець вибирає на Research Table дозволений для дослідження предмет або доступний вузол дерева технологій Workbench і витрачає вказаний дослідницький ресурс, щоб додати цей рецепт до особисто вивчених креслень.

### Включає

Дослідження предметів за ресурс Scrap на Research Table та відкриття вузлів дерева технологій Workbench у Rust.

### Виключає

Виготовлення вже вивченого предмета; відкриття безкоштовного початкового рецепта; поліпшення самого Workbench.

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

Вибір випадкового місця появи на пляжі після смерті; автоматичне збереження контрольної точки; тимчасове оживлення товариша.

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

Постріл зі зброї; дії, спрямовані лише на розкопування рельєфу; знищення об’єкта командою адміністратора.

### Ігри-носії

- [`GAME-0141` — Rust](../games/m-r/rust.md)

## ACT-210

- Назва: Обрати початкове тло та сумісні риси
- Переглянуто: `2026-09-21`

### Операційне визначення

Перед звичайною появою у світі гравець обирає одне початкове тло або професію та необов’язковий допустимий набір сумісних рис, які визначають початкові навички й постійні особливості.

### Включає

Професія й збалансовані очками риси у Build 42 Project Zomboid; тло та до трьох сумісних необов’язкових рис у Starfield.

### Виключає

Набуття досвіду навичок після появи у світі; косметичну зовнішність; зміну шаблону налаштувань світу.

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

- Назва: Додати або зняти захисний матеріал з отвору чи поверхні
- Переглянуто: `2026-10-13`

### Операційне визначення

Гравець обирає досяжний отвір або поверхню, що відповідає умовам, і за допомогою сумісного матеріалу додає один захисний шар або знімає з тієї самої цілі один шар, який дозволено прибрати.

### Включає

Барикади з дощок, металевих листів і прутів у Project Zomboid; барикади дверей і вікон та укріплення стін і люків у Rainbow Six Siege.

### Виключає

Будівництво окремої стіни; закривання звичайної завіси; пошкодження отвору в бою.

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

- [`GAME-0444` — "Harvest Moon: Back to Nature"](../games/g-l/harvest-moon-back-to-nature.md)
- [`GAME-0142` — Project Zomboid](../games/m-r/project-zomboid.md)

## ACT-214

- Назва: Укласти вцілілого спати
- Переглянуто: `2026-08-24`

### Операційне визначення

Гравець користується придатним місцем відпочинку й відмовляється від звичайного безпосереднього керування. До пробудження або дозволеного переривання стан втоми персонажа оновлюється, а час у світі продовжує минати.

### Включає

Сон протягом одного життя в одиночній грі Project Zomboid.

### Виключає

Розміщення об’єкта відродження; паузу симуляції; суто візуальний відпочинок без впливу на час або втому.

### Ігри-носії

- [`GAME-0444` — "Harvest Moon: Back to Nature"](../games/g-l/harvest-moon-back-to-nature.md)
- [`GAME-0142` — Project Zomboid](../games/m-r/project-zomboid.md)
- [`GAME-0292` — The Forest](../games/s-z/the-forest.md)
- [`GAME-0285` — "The Long Dark"](../games/s-z/the-long-dark.md)

## ACT-215

- Назва: Підготувати один сумісний бойовий комплект спорядження в заданих межах
- Переглянуто: `2026-10-03`

### Операційне визначення

У допустимому стані підготовки гравець заповнює або змінює обмежені комірки спорядження й можливостей для наступного розгортання під керуванням гравця або відрізка активної гри.

### Включає

Комплекти рейду ARC Raiders; прив’язані до класу комплекти висадження Battlefield 6; спорядження герба й інструментів біля лави Hollow Knight: Silksong; вибір зброї, захисту, підсилювача й чотирьох стратагем перед висадженням Helldivers 2; підготовка зброї та допоміжного пристрою оперативника Rainbow Six Siege.

### Виключає

Суто косметичні зміни; збирання здобичі після розгортання; перемикання лише активної комірки спорядження; вибір самого керованого героя.

### Ігри-носії

- [`GAME-0143` — ARC Raiders](../games/a-f/arc-raiders.md)
- [`GAME-0506` — Avowed](../games/a-f/avowed.md)
- [`GAME-0234` — Battlefield 2042](../games/a-f/battlefield-2042.md)
- [`GAME-0149` — Battlefield 6](../games/a-f/battlefield-6.md)
- [`GAME-0220` — Battlefield V](../games/a-f/battlefield-v.md)
- [`GAME-0200` — Delta Force](../games/a-f/delta-force.md)
- [`GAME-0193` — Destiny 2](../games/a-f/destiny-2.md)
- [`GAME-0159` — Helldivers 2](../games/g-l/helldivers-2.md)
- [`GAME-0150` — "Hollow Knight: Silksong"](../games/g-l/hollow-knight-silksong.md)
- [`GAME-0293` — Ori and the Will of the Wisps](../games/m-r/ori-and-the-will-of-the-wisps.md)
- [`GAME-0160` — "Pokémon Legends: Z-A"](../games/m-r/pokemon-legends-z-a.md)
- [`GAME-0508` — Ready or Not](../games/m-r/ready-or-not.md)
- [`GAME-0549` — Roto Force](../games/m-r/roto-force.md)
- [`GAME-0487` — Sid Meier's Pirates!](../games/s-z/sid-meiers-pirates.md)
- [`GAME-0174` — Tom Clancy’s Rainbow Six Siege](../games/s-z/tom-clancys-rainbow-six-siege.md)
- [`GAME-0499` — Vagrant Story](../games/s-z/vagrant-story.md)
- [`GAME-0168` — Warframe](../games/s-z/warframe.md)

## ACT-216

- Назва: Обшукати досяжний контейнер або знешкоджену машину
- Переглянуто: `2026-10-02`

### Операційне визначення

Гравець починає обшук поблизу одного контейнера, уламка чи знешкодженої машини; завершення взаємодії відкриває вміст, який можна забрати й перенести далі.

### Включає

Обшук шафок, шухляд, ящиків, оболонок і знищених ARC заради матеріалів у ARC Raiders.

### Виключає

Підбирання вже видимої здобичі із землі; віддалене розкриття мапи; автоматичне збирання ресурсів після вбивства.

### Ігри-носії

- [`GAME-0456` — Alone in the Dark](../games/a-f/alone-in-the-dark.md)
- [`GAME-0143` — ARC Raiders](../games/a-f/arc-raiders.md)
- [`GAME-0484` — Impossible Mission](../games/g-l/impossible-mission.md)
- [`GAME-0500` — Pacific Drive](../games/m-r/pacific-drive.md)
- [`GAME-0285` — "The Long Dark"](../games/s-z/the-long-dark.md)

## ACT-217

- Назва: Перекласти предмет до захищеної кишені або з неї
- Переглянуто: `2026-08-24`

### Операційне визначення

Під час активного рейду гравець переносить допустимий предмет при собі між звичайним сховищем наплічника й обмеженою захищеною кишенею, для вмісту якої діє інше правило збереження після поразки.

### Включає

Перенесення предметів до Safe Pocket і з неї в ARC Raiders.

### Виключає

Звичайне впорядкування наплічника; збереження всього вантажу після успішної евакуації; перенесення забороненої зброї чи активного пристрою через помилку гри.

### Ігри-носії

- [`GAME-0143` — ARC Raiders](../games/a-f/arc-raiders.md)

## ACT-218

- Назва: Активувати точку евакуації під час гри й увійти до зони відправлення
- Переглянуто: `2026-08-24`

### Операційне визначення

Гравець дістається доступного засобу евакуації, починає взаємодію виклику чи розблокування, якщо це потрібно, та входить до обмеженої зони відправлення до закриття точки евакуації.

### Включає

Евакуаційні ліфти, виходи метро й Raider Hatches у ARC Raiders; виклик евакуації через термінал у Helldivers 2 і вхід до Pelican після його приземлення.

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
- Переглянуто: `2026-09-28`

### Операційне визначення

Гравець обирає власну річ і безповоротно передає її для продажу чи розбирання з визначеною винагородою в грошах або складниках; обмін може завершитися відразу або під час окремо запланованого вивезення.

### Включає

Продаж і розбирання у Speranza та польове розбирання (Field Recycling) на Поверхні в ARC Raiders; вкладання зібраної культури до скрині відвантаження в оригінальній Harvest Moon: Back to Nature для PlayStation перед наступним можливим вивезенням.

### Виключає

Викидання здобичі для іншого рейдера; використання лікувального предмета; скасування виготовлення з поверненням ресурсів.

### Ігри-носії

- [`GAME-0453` — Age of Mythology](../games/a-f/age-of-mythology.md)
- [`GAME-0511` — Animal Crossing: New Leaf](../games/a-f/animal-crossing-new-leaf.md)
- [`GAME-0143` — ARC Raiders](../games/a-f/arc-raiders.md)
- [`GAME-0555` — Chibi-Robo!](../games/a-f/chibi-robo.md)
- [`GAME-0269` — DREDGE](../games/a-f/dredge.md)
- [`GAME-0491` — Elite](../games/a-f/elite.md)
- [`GAME-0444` — "Harvest Moon: Back to Nature"](../games/g-l/harvest-moon-back-to-nature.md)
- [`GAME-0319` — Sea of Thieves](../games/s-z/sea-of-thieves.md)
- [`GAME-0307` — Slime Rancher](../games/s-z/slime-rancher.md)
- [`GAME-0499` — Vagrant Story](../games/s-z/vagrant-story.md)

## ACT-221

- Назва: Полагодити або вдосконалити одну збережену одиницю зброї
- Переглянуто: `2026-08-24`

### Операційне визначення

У безпечному осередку гравець вибирає одну збережену одиницю зброї й витрачає визначені сумісні ресурси, щоб відновити її міцність або підвищити її поточний ступінь удосконалення.

### Включає

Ремонт зброї та вдосконалення з ремонтом у майстерні Workshop ARC Raiders; поліпшення зброї за доступним рецептом у кузні Monster Hunter Wilds; поліпшення зброї в Elden Ring.

### Виключає

Лікування в польових умовах; установлення модифікації зброї; заміну зламаної зброї іншою копією.

### Ігри-носії

- [`GAME-0143` — ARC Raiders](../games/a-f/arc-raiders.md)
- [`GAME-0152` — Elden Ring](../games/a-f/elden-ring.md)
- [`GAME-0151` — Monster Hunter Wilds](../games/m-r/monster-hunter-wilds.md)
- [`GAME-0170` — "S.T.A.L.K.E.R. 2: Heart of Chornobyl"](../games/s-z/stalker-2-heart-of-chornobyl.md)

## ACT-222

- Назва: Вчасно виконати підказане введення під час вибраної бойової дії
- Переглянуто: `2026-08-24`

### Операційне визначення

Після вибору покрокової атаки, здібності, лікування або підсилення гравець натискає показану команду чи виконує показану послідовність натискань у реальному часі під час анімації, щоб змінити заявлений ефект дії.

### Включає

Вчасне введення за підказками під час атакувальних і підтримувальних дій у Clair Obscur: Expedition 33.

### Виключає

Вибір команди чи цілі; реакцію на атаку ворога; пасивну ймовірність критичного влучання.

### Ігри-носії

- [`GAME-0144` — Clair Obscur: Expedition 33](../games/a-f/clair-obscur-expedition-33.md)
- [`GAME-0608` — "Dosa Divas"](../games/a-f/dosa-divas.md)
- [`GAME-0530` — Lost Odyssey](../games/g-l/lost-odyssey.md)
- [`GAME-0449` — Paper Mario](../games/m-r/paper-mario.md)
- [`GAME-0577` — People of Note](../games/m-r/people-of-note.md)
- [`GAME-0714` — "Thirsty Suitors"](../games/s-z/thirsty-suitors.md)

## ACT-223

- Назва: Обрати вчасне ухилення, парирування або стрибок
- Переглянуто: `2026-10-04`

### Операційне визначення

Під час завчасно позначеної ворожої атаки гравець у вибрану мить живої послідовності застосовує доступну захисну відповідь.

### Включає

Ухилення, парирування й відкритий згодом стрибок у Clair Obscur: Expedition 33; звичайні та ідеальні ухилення в Black Myth: Wukong; вчасні стрибки або зміна позиції проти атак стража в Hollow Knight.

### Виключає

Вибір покрокової команди; пасивну ймовірність ухилення; блокування постійним показником броні.

### Ігри-носії

- [`GAME-0427` — Alan Wake](../games/a-f/alan-wake.md)
- [`GAME-0506` — Avowed](../games/a-f/avowed.md)
- [`GAME-0189` — "Black Myth: Wukong"](../games/a-f/black-myth-wukong.md)
- [`GAME-0546` — Burning Rangers](../games/a-f/burning-rangers.md)
- [`GAME-0641` — "Bushido Blade"](../games/a-f/bushido-blade.md)
- [`GAME-0144` — Clair Obscur: Expedition 33](../games/a-f/clair-obscur-expedition-33.md)
- [`GAME-0570` — Cult of the Lamb](../games/a-f/cult-of-the-lamb.md)
- [`GAME-0277` — Cuphead](../games/a-f/cuphead.md)
- [`GAME-0494` — Dead or Alive 2](../games/a-f/dead-or-alive-2.md)
- [`GAME-0608` — "Dosa Divas"](../games/a-f/dosa-divas.md)
- [`GAME-0592` — Dungeons of Hinterberg](../games/a-f/dungeons-of-hinterberg.md)
- [`GAME-0263` — God of War](../games/g-l/god-of-war.md)
- [`GAME-0516` — Hi-Fi RUSH](../games/g-l/hi-fi-rush.md)
- [`GAME-0274` — Hollow Knight](../games/g-l/hollow-knight.md)
- [`GAME-0583` — "Kunitsu-Gami: Path of the Goddess"](../games/g-l/kunitsu-gami-path-of-the-goddess.md)
- [`GAME-0202` — "NARAKA: BLADEPOINT"](../games/m-r/naraka-bladepoint.md)
- [`GAME-0588` — Neva](../games/m-r/neva.md)
- [`GAME-0527` — Nine Sols](../games/m-r/nine-sols.md)
- [`GAME-0341` — "Ninja Gaiden Black"](../games/m-r/ninja-gaiden-black.md)
- [`GAME-0293` — Ori and the Will of the Wisps](../games/m-r/ori-and-the-will-of-the-wisps.md)
- [`GAME-0162` — Path of Exile 2](../games/m-r/path-of-exile-2.md)
- [`GAME-0577` — People of Note](../games/m-r/people-of-note.md)
- [`GAME-0519` — Power Stone](../games/m-r/power-stone.md)
- [`GAME-0536` — PRAGMATA](../games/m-r/pragmata.md)
- [`GAME-0691` — "REPLACED"](../games/m-r/replaced.md)
- [`GAME-0639` — "Rollerdrome"](../games/m-r/rollerdrome.md)
- [`GAME-0667` — "SAROS"](../games/s-z/saros.md)
- [`GAME-0288` — "Sekiro™: Shadows Die Twice - GOTY Edition"](../games/s-z/sekiro-shadows-die-twice.md)
- [`GAME-0303` — Sifu](../games/s-z/sifu.md)
- [`GAME-0616` — Silent Bomber](../games/s-z/silent-bomber.md)
- [`GAME-0455` — Soulcalibur](../games/s-z/soulcalibur.md)
- [`GAME-0213` — "STAR WARS Jedi: Fallen Order"](../games/s-z/star-wars-jedi-fallen-order.md)
- [`GAME-0458` — The Legend of Zelda: Link's Awakening](../games/s-z/the-legend-of-zelda-links-awakening.md)
- [`GAME-0205` — "The Witcher 3: Wild Hunt"](../games/s-z/the-witcher-3-wild-hunt.md)
- [`GAME-0294` — V Rising](../games/s-z/v-rising.md)
- [`GAME-0197` — Valheim](../games/s-z/valheim.md)
- [`GAME-0580` — Viewtiful Joe](../games/s-z/viewtiful-joe.md)
- [`GAME-0496` — "Warhammer 40,000: Space Marine 2"](../games/s-z/warhammer-40000-space-marine-2.md)
- [`GAME-0564` — Windjammers](../games/s-z/windjammers.md)

## ACT-224

- Назва: Відпочити біля відкритої контрольної точки
- Переглянуто: `2026-09-07`

### Операційне визначення

Гравець свідомо відпочиває біля активованої контрольної точки кампанії, щоб прийняти пов’язані з цим відновлення та скидання стану світу.

### Включає

Відпочинок біля Expedition Flags у Clair Obscur: Expedition 33; біля активованих Benches у Hollow Knight: Silksong і Hollow Knight; біля активованого Keeper’s Shrine у Black Myth: Wukong; біля Sites of Grace в Elden Ring.

### Виключає

Дотик до контрольної точки без відпочинку; використання предмета бойового лікування; сон у безперервній симуляції відкритого світу.

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

- Назва: Налаштувати споряджені Pictos й активні Luminas
- Переглянуто: `2026-08-24`

### Операційне визначення

Поза боєм гравець споряджає здобуті Pictos і вмикає вивчені Luminas, не перевищуючи кількість місць та очок кожного персонажа.

### Включає

Налаштування Pictos і Luminas окремих персонажів у Clair Obscur: Expedition 33.

### Виключає

Спорядження зброєю; витрачання очка навички; автоматичне опанування Picto, після якого його пасивна властивість стає доступною як Lumina.

### Ігри-носії

- [`GAME-0144` — Clair Obscur: Expedition 33](../games/a-f/clair-obscur-expedition-33.md)

## ACT-226

- Назва: Зайняти бойове укриття або вийти з нього
- Переглянуто: `2026-08-24`

### Операційне визначення

Гравець притискає керованого героя до досяжної захисної поверхні, рухається вздовж її доступного краю або огинає його й свідомо виходить зі стану укриття, поки триває безпосередній бій.

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
- Переглянуто: `2026-10-14`

### Операційне визначення

Гравець обирає одну досяжну позицію на мапі або відому позначку як власний пункт призначення, щоб навігаційний інтерфейс міг розрахувати й показати дорожній маршрут без автоматичного переміщення персонажа.

### Включає

Власні точки на мапі й розраховані дорожні маршрути в Story Mode Grand Theft Auto V та Cyberpunk 2077.

### Виключає

Безпосередню команду автономного пересування; задані позначки завдань, які система встановлює без вибору гравця; малювання транспортної мережі.

### Ігри-носії

- [`GAME-0289` — American Truck Simulator](../games/a-f/american-truck-simulator.md)
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

Зміну зовнішності аватара; наказ союзникові під керуванням гри; вибір команди персонажа покрокової групи.

### Ігри-носії

- [`GAME-0324` — Contra Force](../games/a-f/contra-force.md)
- [`GAME-0145` — Grand Theft Auto V](../games/g-l/grand-theft-auto-v.md)

## ACT-229

- Назва: Увімкнути особливу здібність керованого героя
- Переглянуто: `2026-10-05`

### Операційне визначення

Гравець використовує готовий особливий ресурс героя, щоб на певний час увійти в його бойову форму або отримати модифікатор під час водіння.

### Включає

Стрілецьку концентрацію Michael, водійську концентрацію Franklin і лють Trevor у Story Mode Grand Theft Auto V; набуте перетворення Red Tides у Black Myth: Wukong.

### Виключає

Пасивні характеристики; чит-коди; дії Quickplay у GTA Online.

### Ігри-носії

- [`GAME-0189` — "Black Myth: Wukong"](../games/a-f/black-myth-wukong.md)
- [`GAME-0222` — "Call of Juarez: Gunslinger"](../games/a-f/call-of-juarez-gunslinger.md)
- [`GAME-0501` — F.E.A.R.](../games/a-f/fear.md)
- [`GAME-0145` — Grand Theft Auto V](../games/g-l/grand-theft-auto-v.md)
- [`GAME-0238` — "Max Payne (2001)"](../games/m-r/max-payne-2001.md)
- [`GAME-0273` — Max Payne 3](../games/m-r/max-payne-3.md)
- [`GAME-0226` — "Need for Speed: Most Wanted (2005)"](../games/m-r/need-for-speed-most-wanted-2005.md)
- [`GAME-0580` — Viewtiful Joe](../games/s-z/viewtiful-joe.md)

## ACT-230

- Назва: Вибрати підхід і команду фахівців для пограбування
- Переглянуто: `2026-08-24`

### Операційне визначення

На заданій авторами дошці планування гравець вибирає один доступний підхід до операції та призначає придатних фахівців на кожну потрібну роль команди до початку підготовки або виконання.

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
- Переглянуто: `2026-10-05`

### Операційне визначення

Під час написаної для гри розмови або рішення в завданні гравець обирає одну з поточних запропонованих відповідей, описаний або прихований наслідок якої може змінити відомості, стосунки, стан місії чи пізнішу гілку.

### Включає

Варіанти діалогів, обмежені часом відповіді й рішення прийняти маршрут Hanako під час Nocturne Op55N1 в основній грі Cyberpunk 2077.

### Виключає

Необов’язкові репліки для колориту без зміни стану; купівлю предмета з каталогу; розподіл очка персонажа.

### Ігри-носії

- [`GAME-0478` — 80 Days](../games/0-9/80-days.md)
- [`GAME-0506` — Avowed](../games/a-f/avowed.md)
- [`GAME-0148` — Baldur’s Gate 3](../games/a-f/baldurs-gate-3.md)
- [`GAME-0146` — Cyberpunk 2077](../games/a-f/cyberpunk-2077.md)
- [`GAME-0252` — "Detroit: Become Human"](../games/a-f/detroit-become-human.md)
- [`GAME-0353` — "Deus Ex: Game of the Year Edition"](../games/a-f/deus-ex-game-of-the-year-edition.md)
- [`GAME-0264` — Disco Elysium - The Final Cut](../games/a-f/disco-elysium-the-final-cut.md)
- [`GAME-0545` — Dispatch](../games/a-f/dispatch.md)
- [`GAME-0301` — "Divinity: Original Sin 2 - Definitive Edition"](../games/a-f/divinity-original-sin-2-definitive-edition.md)
- [`GAME-0405` — Fable II](../games/a-f/fable-ii.md)
- [`GAME-0327` — Fable](../games/a-f/fable.md)
- [`GAME-0231` — Fallout 4](../games/a-f/fallout-4.md)
- [`GAME-0361` — Fallout: New Vegas](../games/a-f/fallout-new-vegas.md)
- [`GAME-0582` — Grim Fandango](../games/g-l/grim-fandango.md)
- [`GAME-0654` — "Hotel Dusk: Room 215"](../games/g-l/hotel-dusk-room-215.md)
- [`GAME-0240` — "Kingdom Come: Deliverance II"](../games/g-l/kingdom-come-deliverance-ii.md)
- [`GAME-0388` — L.A. Noire](../games/g-l/la-noire.md)
- [`GAME-0367` — Mass Effect 2 (Legendary Edition)](../games/m-r/mass-effect-2-legendary-edition.md)
- [`GAME-0194` — "Mount & Blade II: Bannerlord"](../games/m-r/mount-and-blade-ii-bannerlord.md)
- [`GAME-0523` — Pentiment](../games/m-r/pentiment.md)
- [`GAME-0385` — 'Phoenix Wright: Ace Attorney'](../games/m-r/phoenix-wright-ace-attorney.md)
- [`GAME-0432` — Reigns](../games/m-r/reigns.md)
- [`GAME-0556` — Sayonara Wild Hearts](../games/s-z/sayonara-wild-hearts.md)
- [`GAME-0170` — "S.T.A.L.K.E.R. 2: Heart of Chornobyl"](../games/s-z/stalker-2-heart-of-chornobyl.md)
- [`GAME-0331` — Starfield](../games/s-z/starfield.md)
- [`GAME-0362` — "The Elder Scrolls III: Morrowind"](../games/s-z/the-elder-scrolls-iii-morrowind.md)
- [`GAME-0576` — The Forgotten City](../games/s-z/the-forgotten-city.md)
- [`GAME-0606` — "The Séance of Blake Manor"](../games/s-z/the-seance-of-blake-manor.md)
- [`GAME-0343` — The Secret of Monkey Island](../games/s-z/the-secret-of-monkey-island.md)
- [`GAME-0205` — "The Witcher 3: Wild Hunt"](../games/s-z/the-witcher-3-wild-hunt.md)
- [`GAME-0696` — "Tides of Tomorrow"](../games/s-z/tides-of-tomorrow.md)
- [`GAME-0498` — Transport Fever 2](../games/s-z/transport-fever-2.md)

## ACT-233

- Назва: Просканувати ціль у світі й завантажити один скрипт швидкого зламу
- Переглянуто: `2026-08-24`

### Операційне визначення

Гравець утримує фокус сканера на допустимій людині, пристрої чи транспортному засобі, вибирає один доступний скрипт швидкого зламу й запускає його завантаження з установленої кібердеки; завантаження триває певний час.

### Включає

Бойові, потайні й пристроєві скрипти в основній грі Cyberpunk 2077.

### Виключає

Постріл зі зброї; пасивне виявлення цілі; вибір відповіді в діалозі; злам без установленої сумісної операційної системи.

### Ігри-носії

- [`GAME-0146` — Cyberpunk 2077](../games/a-f/cyberpunk-2077.md)

## ACT-234

- Назва: Налаштувати встановлені кіберімпланти у спеціаліста
- Переглянуто: `2026-10-13`

### Операційне визначення

У доступному інтерфейсі спеціаліста гравець купує, установлює, знімає, замінює чи поліпшує один імплант у сумісній комірці тіла, зберігаючи комплект, що відповідає правилам місткості та явно відкритим виняткам.

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

Приховані захоплення й нейтралізації в Cyberpunk 2077; смертельні удари з допустимих позицій, у яких гравця не помічено, у Sekiro.

### Виключає

Удари ближнього бою проти настороженого ворога; затримання, яке відбувається лише в розмові; віддалене завантаження скрипту швидкого зламу.

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

Перед виходом з активної кімнати появи команди гравець вибирає одного наразі доступного героя й один запропонований партнерський набір Team-Up, передаючи цьому героєві пряме керування та відповідну конфігурацію базових здібностей.

### Включає

Вибір героя в Quick Match Marvel Rivals, допустимі зміни героя під час матчу в кімнаті появи та вибір партнера Team-Up у Season 9.

### Виключає

Драфт, що закріплює одного героя на весь матч; вибір косметичного образу; тимчасове копіювання іншого героя ультимативною здібністю.

### Ігри-носії

- [`GAME-0147` — Marvel Rivals](../games/m-r/marvel-rivals.md)

## ACT-238

- Назва: Створити власного персонажа для кампанії
- Переглянуто: `2026-08-24`

### Операційне визначення

Перед початком заданої авторами кампанії, стан якої зберігається, гравець підтверджує один сумісний набір раси або підраси, класу, передісторії, розподілу характеристик і володінь. Цей набір визначає початкові можливості нового персонажа.

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

Висадження у штабі, на утримуваній точці, біля придатного для висадження бійця загону поза боєм чи Deploy Beacon або в сумісне вільне місце техніки в Conquest Battlefield 6.

### Виключає

Пересування пішки з наявної позиції; автоматичне відродження на контрольній точці; установлення самого місця висадження.

### Ігри-носії

- [`GAME-0234` — Battlefield 2042](../games/a-f/battlefield-2042.md)
- [`GAME-0149` — Battlefield 6](../games/a-f/battlefield-6.md)
- [`GAME-0220` — Battlefield V](../games/a-f/battlefield-v.md)
- [`GAME-0200` — Delta Force](../games/a-f/delta-force.md)

## ACT-241

- Назва: Оживити або перемістити одного збитого з ніг союзника, коли це дозволено
- Переглянуто: `2026-08-27`

### Операційне визначення

Гравець взаємодіє з одним досяжним союзником, збитим із ніг, за наявності відповідного правила може перемістити його тіло та починає й підтримує потрібний процес оживлення або застосовує миттєвий засіб, поки ще є можливість оживлення.

### Включає

Оживлення бійця свого загону будь-яким класом, командне оживлення класом Support, перетягування в укриття й завершене застосування Defibrillator у Battlefield 6; оживлення збитого з ніг союзника в Apex Legends; оживлення союзника з допустимого пораненого стану в Rainbow Six Siege.

### Виключає

Самолікування; звичайне повторне розгортання після смерті; перенесення предмета цілі; воскресіння персонажа після смерті в кампанії.

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

Гравець викликає постійного їздового супутника на місцевості, сідає на нього або спішується й може задати одну поточну відстежувану ціль для його самостійного руху до неї, зберігаючи можливість керувати рухом вручну.

### Включає

Виклик і їзду на Seikret у Monster Hunter Wilds до цілі завдання, позначки мапи чи відстежуваного монстра.

### Виключає

Безпосереднє пересування мисливця; неінтерактивний перехід швидкого переміщення; супутника, який діє самостійно, але на якому не можна їхати.

### Ігри-носії

- [`GAME-0151` — Monster Hunter Wilds](../games/m-r/monster-hunter-wilds.md)

## ACT-244

- Назва: Поміняти активну зброю на запасну з Seikret
- Переглянуто: `2026-08-24`

### Операційне визначення

Перебуваючи верхи на відповідному їздовому супутнику, гравець міняє місцями поточну активну зброю та рівно одну запасну зброю, призначену цьому супутнику.

### Включає

Зміну зброї на Seikret у Monster Hunter Wilds.

### Виключає

Вибір будь-якої зброї зі сховища табору; перезаряджання боєприпасів; зміну лише вигляду зброї.

### Ігри-носії

- [`GAME-0151` — Monster Hunter Wilds](../games/m-r/monster-hunter-wilds.md)

## ACT-245

- Назва: Зібрати або вирізати одну досяжну порцію матеріалу
- Переглянуто: `2026-10-13`

### Операційне визначення

Гравець взаємодіє з одним досяжним польовим джерелом або тілом переможеної цілі, що відповідає умовам, щоб перенести одну обмежену порцію матеріалу до переносного інвентарю.

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
- [`GAME-0604` — "The Alters"](../games/s-z/the-alters.md)
- [`GAME-0292` — The Forest](../games/s-z/the-forest.md)
- [`GAME-0205` — "The Witcher 3: Wild Hunt"](../games/s-z/the-witcher-3-wild-hunt.md)

## ACT-246

- Назва: Спрямувати й виконати Focus Strike поточної зброї
- Переглянуто: `2026-08-24`

### Операційне визначення

У Focus Mode гравець спрямовує поточну зброю на один підсвічений сумісний стан тіла й виконує властивий цій зброї Focus Strike.

### Включає

Focus Strikes у Monster Hunter Wilds, спрямовані на відкриту рану чи відповідну ламку частину монстра.

### Виключає

Звичайні повторювані атаки; саме підсвічування ран; Focus Strike без допустимого стану тіла в межах досяжності.

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

Біля допустимої контрольної точки гравець вибирає один атрибут персонажа й витрачає показану кількість рун, щоб підвищити його на один рівень.

### Включає

Підвищення Vigor, Mind або іншого атрибута біля Grace в Elden Ring.

### Виключає

Автоматичне підвищення рівня за досвід; придбання навички; поліпшення зброї.

### Ігри-носії

- [`GAME-0152` — Elden Ring](../games/a-f/elden-ring.md)

## ACT-249

- Назва: Повернути валюту з активної позначки смерті
- Переглянуто: `2026-09-05`

### Операційне визначення

Гравець дістається поточної активної позначки смерті й торкається її, щоб повернути збережений у ній запас валюти, яку можна витрачати, живому персонажеві.

### Включає

Повернення рун в Elden Ring до того, як наступна смерть замінить цю позначку; дотик до кривавої плями в дослідженому маршруті DARK SOULS III, щоб забрати залишені там душі.

### Виключає

Звичайне підбирання здобичі; інвентар трупа; повернення Rosaries із Cocoon.

### Ігри-носії

- [`GAME-0308` — Bloodborne™](../games/a-f/bloodborne.md)
- [`GAME-0262` — DARK SOULS™ III](../games/a-f/dark-souls-iii.md)
- [`GAME-0295` — DARK SOULS™: REMASTERED](../games/a-f/dark-souls-remastered.md)
- [`GAME-0152` — Elden Ring](../games/a-f/elden-ring.md)
- [`GAME-0290` — Lies of P](../games/g-l/lies-of-p.md)
- [`GAME-0299` — Nioh 2](../games/m-r/nioh-2.md)

## ACT-250

- Назва: Викликати одну групу духів зі спорядженого Spirit Ash
- Переглянуто: `2026-10-13`

### Операційне визначення

У зоні з відповідним пам’ятником гравець витрачає передбачений ресурс, щоб викликати одну споряджену автономну групу духів.

### Включає

Раннє використання Spirit Ash у допустимих польових зонах і зонах босів Elden Ring.

### Виключає

Союзників онлайн; знаки виклику NPC; безпосередньо керованих супутників.

### Ігри-носії

- [`GAME-0152` — Elden Ring](../games/a-f/elden-ring.md)

## ACT-251

- Назва: Призначити зброї Ash of War і доступну властивість
- Переглянуто: `2026-08-24`

### Операційне визначення

У допустимому меню гравець вибирає сумісний здобутий Ash of War і одну доступну властивість для наявної зброї.

### Включає

Раннє налаштування зброї за допомогою Whetstone Knife в Elden Ring.

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

Повернення через контейнер смерті в Apex Legends або активація допустимого Respawn Beacon із Legend Banner, який гравець переносить або виготовив у Replicator; у Helldivers 2 — набір команди Reinforce та кидок її маяка учасником загону, що вижив, для повернення загиблого союзника.

### Виключає

Оживлення союзника, якого лише збили з ніг; автоматичне повернення між раундами; воскресіння на рівні облікового запису.

### Ігри-носії

- [`GAME-0154` — Apex Legends](../games/a-f/apex-legends.md)
- [`GAME-0159` — Helldivers 2](../games/g-l/helldivers-2.md)

## ACT-254

- Назва: Вибрати одне обов’язкове благословення Ancient на початку акту
- Переглянуто: `2026-08-27`

### Операційне визначення

Перед початком маршруту акту гравець вибирає рівно один предмет з обмеженої пропозиції поточного Ancient і закріплює його ефект, що зберігається в межах забігу, перш ніж просування може продовжитися.

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

Прокладання й надсилання в Strands тематичного слова, spangram або допустимого нетематичного слова через сусідні по горизонталі, вертикалі чи діагоналі клітинки.

### Виключає

Введення слова без вибору його просторового маршруту; шлях від незмінної стартової точки; вибір роз’єднаних літер; просте підсвічування маршруту, який відкрила система.

### Ігри-носії

- [`GAME-0156` — Strands](../games/s-z/strands.md)

## ACT-256

- Назва: Виконати свою половину парної кооперативної взаємодії
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

Гравець вибирає активного постійного мешканця, вказує на допустимого мешканця, об’єкт або ділянку землі й підтверджує одну запропоновану соціальну взаємодію, дію догляду за собою або взаємодію зі світом для автономного виконання.

### Включає

Спрямування Farrah Nouvel познайомитися, поговорити, запросити Sim, скористатися побутовим об’єктом або виконати іншу запропоновану взаємодію базової гри The Sims 4.

### Виключає

Безпосереднє керування кожним кроком; загальний пріоритет роботи колонії; вибір авторської репліки без симульованого стану актора.

### Ігри-носії

- [`GAME-0383` — The Sims 2: Legacy Collection](../games/s-z/the-sims-2-legacy-collection.md)
- [`GAME-0158` — The Sims 4](../games/s-z/the-sims-4.md)
- [`GAME-0461` — The Sims](../games/s-z/the-sims.md)

## ACT-258

- Назва: Перемкнути активного бойового компаньйона з команди
- Переглянуто: `2026-08-27`

### Операційне визначення

Під час бою гравець вибирає іншого допустимого живого члена команди, який замінює єдиного поточного керованого компаньйона, тоді як обидва зберігають власні здоров’я, стан, рівень і вивчені прийоми.

### Включає

Добровільну або вимушену після непритомності заміну Pokémon у Pokémon Legends: Z-A та Pokémon Red Version.

### Виключає

Перенесення компаньйона між сховищем Boxes і командою; відкликання без заміни; перемикання прямого керування між людськими головними героями.

### Ігри-носії

- [`GAME-0463` — "Pokémon Gold Version"](../games/m-r/pokemon-gold-version.md)
- [`GAME-0160` — "Pokémon Legends: Z-A"](../games/m-r/pokemon-legends-z-a.md)
- [`GAME-0336` — "Pokémon Red Version"](../games/m-r/pokemon-red-version.md)

## ACT-259

- Назва: Обрати одного постійного стартового супутника
- Переглянуто: `2026-08-27`

### Операційне визначення

На початку кампанії гравець приймає рівно одного супутника з обмеженого набору запропонованих. Обраний супутник із власним початковим набором можливостей стає постійним членом команди й належить гравцеві.

### Включає

Вибір Chikorita, Tepig або Totodile як першого партнера в Pokémon Legends: Z-A; вибір Bulbasaur, Charmander або Squirtle у Pokémon Red Version.

### Виключає

Вибір героя лише на матч; вибір косметичного оформлення; захоплення істоти у світі пізніше впродовж гри.

### Ігри-носії

- [`GAME-0160` — "Pokémon Legends: Z-A"](../games/m-r/pokemon-legends-z-a.md)
- [`GAME-0336` — "Pokémon Red Version"](../games/m-r/pokemon-red-version.md)

## ACT-260

- Назва: Утримувати одну доступну взаємодію вцілілого
- Переглянуто: `2026-08-27`

### Операційне визначення

Безпосередньо керований вцілілий утримує контекстну взаємодію з досяжною ціллю або союзником, а поступ зростає лише за сумісного стану й неперерваної дії.

### Включає

Ремонт генератора, лікування іншого вцілілого, виведення іншого вцілілого зі стану Dying, зняття союзника з гака та робота з перемикачем заживлених воріт виходу в дослідженому Trial з порожнім комплектом спорядження в Dead by Daylight.

### Виключає

Пересування пішки або перелізання; одне миттєве натискання перемикача; взаємодії вбивці з підніманням, перенесенням чи пошкодженням; наказ автономному працівникові.

### Ігри-носії

- [`GAME-0161` — Dead by Daylight](../games/a-f/dead-by-daylight.md)
- [`GAME-0192` — Left 4 Dead 2](../games/g-l/left-4-dead-2.md)

## ACT-261

- Назва: Вчасно натиснути, поки рухомий покажчик у показаному проміжку успіху
- Переглянуто: `2026-09-06`

### Операційне визначення

Під час допустимої взаємодії зі світом, яка вже триває, гравець подає одну відповідь, коли рухомий покажчик перекриває показаний проміжок успіху, й отримує градуйований результат вчасності, не вибираючи нової цілі.

### Включає

Добрі, відмінні й невдалі відповіді на перевірку навички під час ремонту генератора або лікування іншого вцілілого в Dead by Daylight; підсічка в мить, коли рухома позначка перетинає показаний проміжок, у визначеному першому дні DREDGE.

### Виключає

Захисну дію з часовою вимогою в межах вибраної бойової дії; ритмічні послідовності, ноти яких становлять повну мету; пасивне випадкове визначення результату без введення гравця.

### Ігри-носії

- [`GAME-0161` — Dead by Daylight](../games/a-f/dead-by-daylight.md)
- [`GAME-0269` — DREDGE](../games/a-f/dredge.md)

## ACT-262

- Назва: Опустити одну підняту палету під час переслідування
- Переглянуто: `2026-08-27`

### Операційне визначення

Безпосередньо керований утікач переводить одну досяжну підняту палету в опущений стан, створюючи сталу місцеву перешкоду та проміжок можливого удару, а не лише перелазячи через наявну геометрію.

### Включає

Опускання піднятої палети вцілілим під час переслідування в Dead by Daylight, з оглушенням убивці або без нього.

### Виключає

Перестрибування опущеної палети; її руйнування вбивцею; розміщення переносної будівельної деталі; зміна стану багаторазового перемикача дверей.

### Ігри-носії

- [`GAME-0161` — Dead by Daylight](../games/a-f/dead-by-daylight.md)

## ACT-263

- Назва: Вигравіювати вибране вміння або підтримку з одного необробленого каменю
- Переглянуто: `2026-08-27`

### Операційне визначення

Гравець обирає одне допустиме запропоноване активне вміння або одну підтримку для одного необробленого каменю, який має при собі; необроблений камінь витрачається, а натомість створюється вибраний придатний до використання камінь.

### Включає

Гравіювання каменів умінь і підтримки з необроблених каменів у Path of Exile 2.

### Виключає

Вставлення вже створеного каменю підтримки; випадкове розпізнавання предмета; автоматичне вивчення вміння під час підвищення рівня.

### Ігри-носії

- [`GAME-0162` — Path of Exile 2](../games/m-r/path-of-exile-2.md)

## ACT-264

- Назва: Вставити сумісний камінь підтримки в активне вміння або вийняти його
- Переглянуто: `2026-08-27`

### Операційне визначення

Гравець переносить один камінь підтримки, який має при собі, у вільне допустиме гніздо одного вибраного активного вміння або виймає його. Це змінює складену поведінку вміння, зберігаючи ідентичність обох каменів.

### Включає

Керування гніздами каменів підтримки на панелі вмінь у Path of Exile 2.

### Виключає

Гравіювання каменю підтримки; екіпірування броні; постійне поліпшення вузла вміння.

### Ігри-носії

- [`GAME-0162` — Path of Exile 2](../games/m-r/path-of-exile-2.md)

## ACT-265

- Назва: Застосувати один валютний предмет для виготовлення до допустимої речі
- Переглянуто: `2026-08-27`

### Операційне визначення

Гравець вибирає один предмет валюти для виготовлення, який має при собі, й застосовує його до одного допустимого цільового предмета, витрачаючи цю валюту для запиту визначеної зміни рідкості, афікса або гнізда.

### Включає

Одна звичайна операція виготовлення за допомогою валютного предмета у Path of Exile 2.

### Виключає

Купівлю у торговця; заміну спорядження; багатоетапний зовнішній калькулятор виготовлення.

### Ігри-носії

- [`GAME-0162` — Path of Exile 2](../games/m-r/path-of-exile-2.md)

## ACT-266

- Назва: Активувати заряджений флакон відновлення
- Переглянуто: `2026-08-27`

### Операційне визначення

Під час допустимого безпосереднього керування гравець активує споряджений флакон здоров’я або мани, негайно витрачаючи визначену кількість його зарядів і запускаючи ефект відновлення без витрачання самого флакона.

### Включає

Використання флаконів здоров’я й мани під час бою в кампанії Path of Exile 2.

### Виключає

Перериване споживання їжі, яку гравець має при собі; пасивне відновлення; одноразове зілля, яке вилучається з інвентарю.

### Ігри-носії

- [`GAME-0162` — Path of Exile 2](../games/m-r/path-of-exile-2.md)

## ACT-267

- Назва: Спрямувати передачу м’яча до допустимого партнера
- Переглянуто: `2026-08-27`

### Операційне визначення

Безпосередньо керуючи поточним гравцем із м’ячем, гравець задає передачу низом, верхом або навісну подачу. Її наміченого адресата та траєкторію визначають за керувальними даними про напрям, силу й контекст.

### Включає

Короткі й сильні низові передачі, розрізні передачі, верхові передачі та навісні подачі у футбольному матчі EA SPORTS FC 26.

### Виключає

Удар, спрямований насамперед у ворота суперника; винесення м’яча партнером під керуванням ШІ без команди гравця; вибір віддаленого пункту переміщення.

### Ігри-носії

- [`GAME-0163` — EA SPORTS FC 26](../games/a-f/ea-sports-fc-26.md)
- [`GAME-0665` — "Sega Worldwide Soccer '97"](../games/s-z/sega-worldwide-soccer-97.md)

## ACT-268

- Назва: Спрямувати удар по воротах суперника
- Переглянуто: `2026-08-27`

### Операційне визначення

Керуючи допустимим учасником атаки, гравець виконує удар, покликаний спрямувати м’яч у грі за лінію воріт суперника.

### Включає

Звичайні, обвідні, перекидні удари й удари головою у дослідженому матчі EA SPORTS FC 26.

### Виключає

Передачу, спрямовану партнерові; вибір під час серії пенальті; автономне винесення м’яча воротарем.

### Ігри-носії

- [`GAME-0163` — EA SPORTS FC 26](../games/a-f/ea-sports-fc-26.md)
- [`GAME-0665` — "Sega Worldwide Soccer '97"](../games/s-z/sega-worldwide-soccer-97.md)

## ACT-269

- Назва: Виконати допустиму спробу відбору
- Переглянуто: `2026-08-27`

### Операційне визначення

Безпосередньо керуючи допустимим захисником, гравець задає відбір стоячи, плечем або підкат, щоб вибити чи перехопити м’яч суперника, який перебуває в грі, без попереднього переходу до прямого керування цим м’ячем.

### Включає

Вибір моменту для відбору стоячи або підкату проти поточного гравця з м’ячем у EA SPORTS FC 26.

### Виключає

Автоматичну опіку гравця без м’яча; простий біг у вільний простір; ворожий бій, результат якого визначає вичерпання здоров’я.

### Ігри-носії

- [`GAME-0163` — EA SPORTS FC 26](../games/a-f/ea-sports-fc-26.md)
- [`GAME-0665` — "Sega Worldwide Soccer '97"](../games/s-z/sega-worldwide-soccer-97.md)

## ACT-270

- Назва: Установити одну доступну бомбу із запалом
- Переглянуто: `2026-10-04`

### Операційне визначення

Коли керований персонаж перебуває у стані, що дозволяє встановлення, гравець розміщує одну готову до вибуху бомбу в поточному місці зі скінченного запасу при собі або за допомогою збереженої багаторазової здібності й запускає відлік до вибуху.

### Включає

Установлення звичайної бомби для шкоди ворогам, руйнування каміння або відкриття сумісних стін таємних кімнат у базовій The Binding of Isaac: Rebirth; установлення багаторазової бомби у формі Morphing Ball у Super Metroid.

### Виключає

Кидання тактичної гранати; постріл вибуховим снарядом; автоматичний вибух від предмета без витрати бомби при собі.

### Ігри-носії

- [`GAME-0490` — Comix Zone](../games/a-f/comix-zone.md)
- [`GAME-0584` — Saturn Bomberman](../games/s-z/saturn-bomberman.md)
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

Посадку верхи, безпосередню їзду чи спішування (ACT-348); виклик спектрального скакуна з переходом до їзди однією активацією (ACT-247); рух верхи за маршрутом до цілі (ACT-243); відкликання звичайного автономного супутника; швидку подорож.

### Ігри-носії

- [`GAME-0165` — Red Dead Redemption 2](../games/m-r/red-dead-redemption-2.md)
- [`GAME-0356` — Shadow of the Colossus](../games/s-z/shadow-of-the-colossus.md)

## ACT-272

- Назва: Чистити власну вогнепальну зброю збройовою оливою
- Переглянуто: `2026-08-27`

### Операційне визначення

Гравець оглядає одну власну одиницю вогнепальної зброї й витрачає одну доступну одиницю збройової оливи, щоб відновити її поточну справність перед подальшим використанням.

### Включає

Польове чищення забрудненої вогнепальної зброї через інтерфейс зброї під час розділу 2 Red Dead Redemption 2.

### Виключає

Перезаряджання зброї набоями; купівлю послуги чищення у зброяра; ремонт збереженої зброї на верстаку безпечного осередку; установлення косметичного компонента.

### Ігри-носії

- [`GAME-0165` — Red Dead Redemption 2](../games/m-r/red-dead-redemption-2.md)

## ACT-273

- Назва: Передавати придатні цінності спільному табору банди
- Переглянуто: `2026-08-27`

### Операційне визначення

Гравець вибирає особисті гроші або цінність, припаси чи тушу при собі, що відповідають умовам пожертви, й передає вибране до спільних коштів або запасів табору банди. Пожертвувана цінність назавжди вилучається з особистого володіння.

### Включає

Скринька пожертв у Horseshoe Overlook та передавання Пірсону придатного м’яса або туш під час розділу 2.

### Виключає

Придбання вдосконалення через журнал за спільні кошти; продаж торговцеві з отриманням особистої готівки; суто косметичний подарунок без зміни стану табору.

### Ігри-носії

- [`GAME-0165` — Red Dead Redemption 2](../games/m-r/red-dead-redemption-2.md)

## ACT-274

- Назва: Обирати одну контекстну соціальну відповідь
- Переглянуто: `2026-08-27`

### Операційне визначення

Зосередившись на живій людині поблизу, гравець вибирає одну наразі запропоновану контекстну відповідь — наприклад, привітатися, вороже звернутися, заспокоїти, погрожувати або здатися, — після чого стан цієї людини визначає її реакцію.

### Включає

Вітання або вороже звертання до цивільних, спроба зупинити свідка й здавання правоохоронцям у дослідженому Story Mode Red Dead Redemption 2.

### Виключає

Вибір фіксованої авторської гілки завдання; атаку поточною зброєю; пасивне слухання діалогу без відповіді гравця.

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
- Переглянуто: `2026-10-13`

### Операційне визначення

Гравець призначає доступного торговця одній дозволеній парі місць відправлення й призначення та підтверджує для цієї одиниці показаний маршрут і надходження за хід.

### Включає

Внутрішній маршрут між двома римськими містами або міжнародний маршрут до знайомого суперника.

### Виключає

Разову дипломатичну угоду про ресурси; ручне керування одиницею по одному гексу за раз; пасивне отримання міського доходу.

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

Гравець завершує поточний відкритий стратегічний хід держави після будь-якої допустимої підмножини доступних наказів одиницям, героям, поселенням, економіці або дипломатії. Це дозволяє розпочати підбиття підсумків і хід наступної держави, а невикористані повноваження щодо необов’язкових дій втрачають чинність для цього ходу.

### Включає

Завершення ходу в дослідженій одиночній грі Civilization VI та в кампанії Heroes of Might and Magic III: Complete — сценарії Homecoming.

### Виключає

Витрачання однієї дії одиниці; призупинення реального часу; подання одного прихованого наказу в системі одночасних наказів.

### Ігри-носії

- [`GAME-0332` — "Heroes of Might and Magic III: Complete"](../games/g-l/heroes-of-might-and-magic-iii-complete.md)
- [`GAME-0166` — Sid Meier’s Civilization VI](../games/s-z/sid-meiers-civilization-vi.md)
- [`GAME-0191` — "Total War: WARHAMMER III"](../games/s-z/total-war-warhammer-iii.md)

## ACT-282

- Назва: Керувати висотою однією командою, значення якої залежить від форми
- Переглянуто: `2026-08-27`

### Операційне визначення

Поки горизонтальний рух залишається автоматичним, гравець натискає, утримує або відпускає один елемент керування; поточний режим аватара визначає запитувану вертикальну реакцію без задавання горизонтального напрямку.

### Включає

Натискання або утримування для стрибка куба та утримування або відпускання того самого елемента керування, щоб підняти або знизити траєкторію польоту корабля у Stereo Madness.

### Виключає

Вільне керування у двох осях; вибір місця призначення; безпосередню зміну режиму аватара; декоративне введення без наслідків для зіткнень.

### Ігри-носії

- [`GAME-0167` — Geometry Dash](../games/g-l/geometry-dash.md)

## ACT-283

- Назва: Установити або зняти сумісний Мод зі спорядження
- Переглянуто: `2026-08-27`

### Операційне визначення

Під час налаштування спорядження помістити один власний сумісний Мод у допустимий слот або зняти його перед поверненням до активної гри.

### Включає

Налаштування вибраного Warframe або стартової зброї в Арсеналі під час Awakening і Vor’s Prize.

### Виключає

Отримання Мода зі здобичі; підвищення рівня спорядження; зміну зброї в ширшому комплекті спорядження; застосування здібності під час місії.

### Ігри-носії

- [`GAME-0168` — Warframe](../games/s-z/warframe.md)

## ACT-284

- Назва: Повернути вузли термінала й утворити зв’язний шифр
- Переглянуто: `2026-08-27`

### Операційне визначення

Поки працює таймер термінала, гравець повертає показані вузли, доки їхні шляхи не утворять прийнятий зв’язний рисунок, а потім подає результат або дозволяє терміналу перевірити його.

### Включає

Навчальний злам термінала у стилі Grineer у вступному маршруті Warframe.

### Виключає

Введення запам’ятованого пароля; витрачання предмета Cipher для обходу головоломки; довільне пересування або бій біля консолі.

### Ігри-носії

- [`GAME-0168` — Warframe](../games/s-z/warframe.md)

## ACT-285

- Назва: Прийняти одне вантажне замовлення з транспортом роботодавця
- Переглянуто: `2026-08-27`

### Операційне визначення

На поточному ринку прийняти одну пропозицію, яка фіксує вантаж, початковий і кінцевий пункти, строк доставки й оплату та надає завантажений транспорт на час рейсу.

### Включає

Прийняття визначеного замовлення Quick Job у Euro Truck Simulator 2.

### Виключає

Забирання вантажу власною вантажівкою, зокрема через Freight Market; купівлю транспортного засобу; доручення замовлення автономному працівникові; лише попередній перегляд пропозиції.

### Ігри-носії

- [`GAME-0289` — American Truck Simulator](../games/a-f/american-truck-simulator.md)
- [`GAME-0169` — Euro Truck Simulator 2](../games/a-f/euro-truck-simulator-2.md)

## ACT-286

- Назва: Вибрати тривалість відпочинку на дозволеній стоянці
- Переглянуто: `2026-08-27`

### Операційне визначення

Зупинившись у придатному місці відпочинку, гравець вибирає дозволену тривалість сну й переводить годинники поточного замовлення та світу вперед на цей проміжок; при цьому відновлюється стан відпочинку водія.

### Включає

Вибір часу пробудження за правилами Euro Truck Simulator 2 1.60.

### Виключає

Призупинення часу симуляції; сон протягом фіксованого системою проміжку; відпочинок біля контрольної точки з повторною появою ворогів або відновленням бойових ресурсів.

### Ігри-носії

- [`GAME-0289` — American Truck Simulator](../games/a-f/american-truck-simulator.md)
- [`GAME-0169` — Euro Truck Simulator 2](../games/a-f/euro-truck-simulator-2.md)

## ACT-287

- Назва: Вибрати спосіб здачі причепа
- Переглянуто: `2026-08-27`

### Операційне визначення

У пункті призначення вантажу гравець вибирає один наразі запропонований спосіб здачі причепа. Геометрія відповідного паркувального місця або правило пропуску визначає потрібний маневр паркування та досвід, який може бути зарахований.

### Включає

Вибір звичайного або простішого місця для паркування причепа в Euro Truck Simulator 2 або прийняття доступного варіанта автоматичного паркування з пропуском ручного маневру.

### Виключає

Керування самим транспортним засобом і рух заднім ходом; прийняття вантажного замовлення; вибір довільного місця паркування у світі без наслідків для доставлення.

### Ігри-носії

- [`GAME-0289` — American Truck Simulator](../games/a-f/american-truck-simulator.md)
- [`GAME-0169` — Euro Truck Simulator 2](../games/a-f/euro-truck-simulator-2.md)

## ACT-288

- Назва: Кинути болт, щоб перевірити шлях крізь аномалію
- Переглянуто: `2026-08-27`

### Операційне визначення

Гравець кидає один болт, який має при собі, у досяжному напрямку, щоб викликати спрацювання аномалії й спостерігати, чи відкриється короткий проміжок для проходження.

### Включає

Перевірка аномалій і проходження крізь них у Малій Зоні після прологу S.T.A.L.K.E.R. 2.

### Виключає

Завдавання шкоди ворогові гранатою; постійне вимкнення небезпеки; проявлення артефакту за допомогою детектора.

### Ігри-носії

- [`GAME-0170` — "S.T.A.L.K.E.R. 2: Heart of Chornobyl"](../games/s-z/stalker-2-heart-of-chornobyl.md)

## ACT-289

- Назва: Знайти й забрати артефакт за допомогою детектора
- Переглянуто: `2026-08-27`

### Операційне визначення

Гравець споряджається детектором артефактів, рухається за його мінливим сигналом у межах аномального поля й забирає артефакт після того, як наближення робить його видимим і досяжним.

### Включає

Артефакт у пролозі та Mold у Piece of Cake.

### Виключає

Спостереження звичайної здобичі на землі; читання зовнішньої мапи; оснащення контейнера костюма артефактом, який уже належить гравцеві.

### Ігри-носії

- [`GAME-0170` — "S.T.A.L.K.E.R. 2: Heart of Chornobyl"](../games/s-z/stalker-2-heart-of-chornobyl.md)

## ACT-290

- Назва: Безпосередньо керувати призначеним транспортним засобом
- Переглянуто: `2026-10-03`

### Операційне визначення

Поки гравцеві призначено один транспортний засіб, він безпосередньо керує напрямком, тягою, гальмуванням, вибором передачі та передбаченим ручним гальмом без попередньої посадки на місце водія або подальшого виходу з нього.

### Включає

Керування кожним призначеним дорожнім, ґрунтовим, позашляховим автомобілем і авто для Time Attack у визначеному вступі Forza Horizon 6; кермування, прискорення, задній хід, гальмування й керовані заноси одного призначеного авто Rocket League; керування фіксованим початковим авто Story у Shopping Spree в Need for Speed Unbound; керування фіксованим Mustang, а після заданого сценарієм переходу керування — Regera у The Highway Heist в Need for Speed Payback; кермування, прискорення й гальмування призначеного CarSport на Summer 2026 - 01 у Trackmania; кермування, прискорення, гальмування й ручне гальмо фіксованого початкового авто без змін у вступному Circuit Need for Speed Underground.

### Виключає

Посадку й вихід із постійного транспорту світу; призначення автономного транспортного маршруту; вибір власного авто, яке стане активним.

### Ігри-носії

- [`GAME-0195` — BeamNG.drive](../games/a-f/beamng-drive.md)
- [`GAME-0470` — "Burnout 3: Takedown"](../games/a-f/burnout-3-takedown.md)
- [`GAME-0374` — Burnout Paradise](../games/a-f/burnout-paradise.md)
- [`GAME-0415` — Crazy Taxi](../games/a-f/crazy-taxi.md)
- [`GAME-0542` — Excite Truck](../games/a-f/excite-truck.md)
- [`GAME-0384` — F-Zero GX](../games/a-f/f-zero-gx.md)
- [`GAME-0276` — Forza Horizon 5](../games/a-f/forza-horizon-5.md)
- [`GAME-0171` — Forza Horizon 6](../games/a-f/forza-horizon-6.md)
- [`GAME-0316` — Gran Turismo](../games/g-l/gran-turismo.md)
- [`GAME-0712` — "JellyCar Worlds"](../games/g-l/jellycar-worlds.md)
- [`GAME-0309` — "Mario Kart 8 Deluxe"](../games/m-r/mario-kart-8-deluxe.md)
- [`GAME-0507` — MotorStorm](../games/m-r/motorstorm.md)
- [`GAME-0244` — "Need for Speed Heat"](../games/m-r/need-for-speed-heat.md)
- [`GAME-0226` — "Need for Speed: Most Wanted (2005)"](../games/m-r/need-for-speed-most-wanted-2005.md)
- [`GAME-0208` — 'Need for Speed Payback'](../games/m-r/need-for-speed-payback.md)
- [`GAME-0235` — "Need for Speed: The Run"](../games/m-r/need-for-speed-the-run.md)
- [`GAME-0199` — "Need for Speed Unbound"](../games/m-r/need-for-speed-unbound.md)
- [`GAME-0217` — "Need for Speed Underground"](../games/m-r/need-for-speed-underground.md)
- [`GAME-0481` — Out Run](../games/m-r/out-run.md)
- [`GAME-0578` — OutRun 2](../games/m-r/outrun-2.md)
- [`GAME-0420` — Project Gotham Racing 2](../games/m-r/project-gotham-racing-2.md)
- [`GAME-0710` — "Racing Destruction Set"](../games/m-r/racing-destruction-set.md)
- [`GAME-0551` — "R4: Ridge Racer Type 4"](../games/m-r/ridge-racer-type-4.md)
- [`GAME-0177` — Rocket League](../games/m-r/rocket-league.md)
- [`GAME-0457` — Sega Rally Championship](../games/s-z/sega-rally-championship.md)
- [`GAME-0621` — "Sonic Racing: CrossWorlds"](../games/s-z/sonic-racing-crossworlds.md)
- [`GAME-0632` — "Star Wars Episode I: Racer"](../games/s-z/star-wars-episode-i-racer.md)
- [`GAME-0677` — "Stunt Car Racer"](../games/s-z/stunt-car-racer.md)
- [`GAME-0590` — Tokyo Xtreme Racer](../games/s-z/tokyo-xtreme-racer.md)
- [`GAME-0216` — Trackmania](../games/s-z/trackmania.md)
- [`GAME-0409` — 'Twisted Metal: Black'](../games/s-z/twisted-metal-black.md)
- [`GAME-0184` — War Thunder](../games/s-z/war-thunder.md)
- [`GAME-0524` — Wave Race 64](../games/s-z/wave-race-64.md)
- [`GAME-0674` — "Wave Race: Blue Storm"](../games/s-z/wave-race-blue-storm.md)
- [`GAME-0488` — wipEout](../games/s-z/wipeout.md)
- [`GAME-0211` — World of Tanks](../games/s-z/world-of-tanks.md)

## ACT-291

- Назва: Обрати поточний автомобіль із придатної колекції
- Переглянуто: `2026-08-27`

### Операційне визначення

Поза подією, у якій уже зафіксовано склад автомобілів, гравець вибирає один автомобіль, який наразі йому належить і відповідає умовам, щоб він став активним автомобілем під безпосереднім керуванням.

### Включає

Вибір одного з трьох стартових автомобілів Forza Horizon 6 та подальше перемикання між власними автомобілями через Car Collection перед подією.

### Виключає

Купівлю транспортного засобу; прийняття вантажного замовлення з наданим транспортом; зміну автомобілів після фіксації складу події.

### Ігри-носії

- [`GAME-0171` — Forza Horizon 6](../games/a-f/forza-horizon-6.md)
- [`GAME-0235` — "Need for Speed: The Run"](../games/m-r/need-for-speed-the-run.md)

## ACT-292

- Назва: Налаштувати допомогу з водінням і складність суперників
- Переглянуто: `2026-09-04`

### Операційне визначення

Гравець фіксує сумісний профіль допомоги з водінням і складності суперників, який змінює опрацювання прямого керування, підказок та автономних суперників у допустимих транспортних подіях.

### Включає

Налаштування кермування, гальмування, коробки передач, протибуксувальної системи, системи стабілізації, показу лінії руху, Rewind і складності Drivatar у Forza Horizon 6; профіль суперників і поліції Relaxed у Story та автоматичну коробку передач Need for Speed Unbound; суперників Easy й автоматичну коробку передач Need for Speed Payback; суперників Easy для окремої події й автоматичну коробку передач Need for Speed Underground.

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
- [`GAME-0420` — Project Gotham Racing 2](../games/m-r/project-gotham-racing-2.md)

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
- [`GAME-0470` — "Burnout 3: Takedown"](../games/a-f/burnout-3-takedown.md)
- [`GAME-0374` — Burnout Paradise](../games/a-f/burnout-paradise.md)
- [`GAME-0384` — F-Zero GX](../games/a-f/f-zero-gx.md)
- [`GAME-0171` — Forza Horizon 6](../games/a-f/forza-horizon-6.md)
- [`GAME-0309` — "Mario Kart 8 Deluxe"](../games/m-r/mario-kart-8-deluxe.md)
- [`GAME-0507` — MotorStorm](../games/m-r/motorstorm.md)
- [`GAME-0244` — "Need for Speed Heat"](../games/m-r/need-for-speed-heat.md)
- [`GAME-0208` — 'Need for Speed Payback'](../games/m-r/need-for-speed-payback.md)
- [`GAME-0199` — "Need for Speed Unbound"](../games/m-r/need-for-speed-unbound.md)
- [`GAME-0217` — "Need for Speed Underground"](../games/m-r/need-for-speed-underground.md)
- [`GAME-0420` — Project Gotham Racing 2](../games/m-r/project-gotham-racing-2.md)

## ACT-294

- Назва: Призначити бійця, сторону й тип керування для дуелі
- Переглянуто: `2026-10-04`

### Операційне визначення

Перед початком фіксованого бойового матчу гравець призначає кожному визначеному учаснику одного доступного бійця, сторону й підтримувану схему введення.

### Включає

Призначення базового Ryu стороні P1, базового Luke стороні CPU та керування Classic обом у Fighting Ground Versus у Street Fighter 6.

### Виключає

Зміну бійця під час активного раунду; налаштування постійного персонажа кампанії; вибір багаточленної команди або черги мережевого рейтингу.

### Ігри-носії

- [`GAME-0198` — Brawlhalla](../games/a-f/brawlhalla.md)
- [`GAME-0494` — Dead or Alive 2](../games/a-f/dead-or-alive-2.md)
- [`GAME-0393` — Mortal Kombat II](../games/m-r/mortal-kombat-ii.md)
- [`GAME-0519` — Power Stone](../games/m-r/power-stone.md)
- [`GAME-0455` — Soulcalibur](../games/s-z/soulcalibur.md)
- [`GAME-0172` — Street Fighter 6](../games/s-z/street-fighter-6.md)
- [`GAME-0351` — "Street Fighter II: The World Warrior"](../games/s-z/street-fighter-ii-the-world-warrior.md)
- [`GAME-0366` — Tekken 3](../games/s-z/tekken-3.md)
- [`GAME-0283` — TEKKEN 8](../games/s-z/tekken-8.md)

## ACT-295

- Назва: Ввести атаку безпосередньо керованого персонажа
- Переглянуто: `2026-10-04`

### Операційне визначення

Коли безпосередньо керований персонаж може діяти, гравець вводить один допустимий власний стан атаки через оголошену послідовність напрямку, пози й кнопки: звичайний удар, бойову команду, снаряд, стрибок-клубок, перекат або колесо.

### Включає

Звичайні атаки Ryu, Hadoken і Super Art із наявним запасом під час дослідженої дуелі Street Fighter 6 із керуванням Classic; стрибок-клубок і рухомий перекат Соніка в оригінальній Sonic the Hedgehog.

### Виключає

Рух без атаки; автоматичне розв’язання контакту; споряджену вогнепальну зброю чи інструмент; тактичну покрокову команду.

### Ігри-носії

- [`GAME-0719` — "Alisia Dragoon"](../games/a-f/alisia-dragoon.md)
- [`GAME-0456` — Alone in the Dark](../games/a-f/alone-in-the-dark.md)
- [`GAME-0318` — Battletoads](../games/a-f/battletoads.md)
- [`GAME-0198` — Brawlhalla](../games/a-f/brawlhalla.md)
- [`GAME-0641` — "Bushido Blade"](../games/a-f/bushido-blade.md)
- [`GAME-0490` — Comix Zone](../games/a-f/comix-zone.md)
- [`GAME-0326` — Crash Bandicoot](../games/a-f/crash-bandicoot.md)
- [`GAME-0494` — Dead or Alive 2](../games/a-f/dead-or-alive-2.md)
- [`GAME-0495` — Donkey Kong Country Returns](../games/a-f/donkey-kong-country-returns.md)
- [`GAME-0329` — "Donkey Kong Country"](../games/a-f/donkey-kong-country.md)
- [`GAME-0501` — F.E.A.R.](../games/a-f/fear.md)
- [`GAME-0468` — Gravity Rush](../games/g-l/gravity-rush.md)
- [`GAME-0560` — Gunstar Heroes](../games/g-l/gunstar-heroes.md)
- [`GAME-0720` — "Kaze and the Wild Masks"](../games/g-l/kaze-and-the-wild-masks.md)
- [`GAME-0393` — Mortal Kombat II](../games/m-r/mortal-kombat-ii.md)
- [`GAME-0500` — Pacific Drive](../games/m-r/pacific-drive.md)
- [`GAME-0640` — "Pizza Tower"](../games/m-r/pizza-tower.md)
- [`GAME-0561` — Psychonauts 2](../games/m-r/psychonauts-2.md)
- [`GAME-0447` — Punch-Out!!](../games/m-r/punch-out.md)
- [`GAME-0722` — "QuackShot Starring Donald Duck"](../games/m-r/quackshot-starring-donald-duck.md)
- [`GAME-0691` — "REPLACED"](../games/m-r/replaced.md)
- [`GAME-0643` — "Rocket Knight Adventures"](../games/m-r/rocket-knight-adventures.md)
- [`GAME-0690` — "Sonic Advance"](../games/s-z/sonic-advance.md)
- [`GAME-0472` — Sonic Adventure](../games/s-z/sonic-adventure.md)
- [`GAME-0333` — "Sonic the Hedgehog"](../games/s-z/sonic-the-hedgehog.md)
- [`GAME-0455` — Soulcalibur](../games/s-z/soulcalibur.md)
- [`GAME-0172` — Street Fighter 6](../games/s-z/street-fighter-6.md)
- [`GAME-0351` — "Street Fighter II: The World Warrior"](../games/s-z/street-fighter-ii-the-world-warrior.md)
- [`GAME-0466` — Streets of Rage 2](../games/s-z/streets-of-rage-2.md)
- [`GAME-0354` — Super Mario World](../games/s-z/super-mario-world.md)
- [`GAME-0366` — Tekken 3](../games/s-z/tekken-3.md)
- [`GAME-0283` — TEKKEN 8](../games/s-z/tekken-8.md)
- [`GAME-0580` — Viewtiful Joe](../games/s-z/viewtiful-joe.md)
- [`GAME-0645` — Wario Land 3](../games/s-z/wario-land-3.md)
- [`GAME-0497` — Wario Land 4](../games/s-z/wario-land-4.md)

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

- [`GAME-0490` — Comix Zone](../games/a-f/comix-zone.md)
- [`GAME-0494` — Dead or Alive 2](../games/a-f/dead-or-alive-2.md)
- [`GAME-0510` — Indiana Jones and the Great Circle](../games/g-l/indiana-jones-and-the-great-circle.md)
- [`GAME-0393` — Mortal Kombat II](../games/m-r/mortal-kombat-ii.md)
- [`GAME-0447` — Punch-Out!!](../games/m-r/punch-out.md)
- [`GAME-0455` — Soulcalibur](../games/s-z/soulcalibur.md)
- [`GAME-0172` — Street Fighter 6](../games/s-z/street-fighter-6.md)
- [`GAME-0351` — "Street Fighter II: The World Warrior"](../games/s-z/street-fighter-ii-the-world-warrior.md)
- [`GAME-0366` — Tekken 3](../games/s-z/tekken-3.md)
- [`GAME-0283` — TEKKEN 8](../games/s-z/tekken-8.md)

## ACT-297

- Назва: Спробувати близький кидок або відповідне звільнення від кидка
- Переглянуто: `2026-10-04`

### Операційне визначення

На близькій дистанції ввести команду кидка для захоплення допустимого суперника або команду звільнення від звичайного кидка суперника у визначений час відповіді.

### Включає

Звичайний кидок і звільнення від нього (Throw Escape) у режимі Versus Street Fighter 6.

### Виключає

Спеціальний командний захват як параметр бійця; захоплення цілі у світі зі скритного положення; перенесення непритомного тіла; автоматичне відштовхування.

### Ігри-носії

- [`GAME-0490` — Comix Zone](../games/a-f/comix-zone.md)
- [`GAME-0494` — Dead or Alive 2](../games/a-f/dead-or-alive-2.md)
- [`GAME-0393` — Mortal Kombat II](../games/m-r/mortal-kombat-ii.md)
- [`GAME-0519` — Power Stone](../games/m-r/power-stone.md)
- [`GAME-0455` — Soulcalibur](../games/s-z/soulcalibur.md)
- [`GAME-0172` — Street Fighter 6](../games/s-z/street-fighter-6.md)
- [`GAME-0351` — "Street Fighter II: The World Warrior"](../games/s-z/street-fighter-ii-the-world-warrior.md)
- [`GAME-0366` — Tekken 3](../games/s-z/tekken-3.md)
- [`GAME-0283` — TEKKEN 8](../games/s-z/tekken-8.md)

## ACT-298

- Назва: Застосувати одну допустиму техніку Drive
- Переглянуто: `2026-08-31`

### Операційне визначення

Гравець запитує одну зі спільних технік Drive System з допустимого бойового стану, погоджуючись на її поточну витрату запасу ресурсу та відповідний перехід бойового стану.

### Включає

Drive Impact, Drive Parry, Drive Rush, Drive Reversal і атаки Overdrive у Street Fighter 6.

### Виключає

Звичайний захист; витрачання запасу Super Art; пасивне відновлення Drive; атаку, властиву окремому персонажеві, яка не витрачає Drive.

### Ігри-носії

- [`GAME-0172` — Street Fighter 6](../games/s-z/street-fighter-6.md)

## ACT-299

- Назва: Вибрати один запропонований план кімнати за вказаними дверима
- Переглянуто: `2026-08-28`

### Операційне визначення

Біля одних невідчинених дверей гравець вибирає рівно один показаний план кімнати з обмеженого переліку пропозицій і фіксує його як варіант кімнати за цими дверима.

### Включає

Вибір одного з трьох планів кімнат у Blue Prince.

### Виключає

Одержання плану кімнати без його вибору; переставляння вже наявної плитки мапи; купівлю товару в крамниці; довільне будівництво.

### Ігри-носії

- [`GAME-0173` — Blue Prince](../games/a-f/blue-prince.md)

## ACT-300

- Назва: Завершити поточний день у маєтку й запросити нове планування
- Переглянуто: `2026-08-28`

### Операційне визначення

Явно закінчити поточну спробу в маєтку, прийняти втрату щоденного стану й почати наступний ранок з новим планом.

### Включає

Call it a Day у Blue Prince.

### Виключає

Автоматичне завершення через сплив часу; перезапуск після смерті; завантаження попереднього збереження; вихід з однієї кімнати зі збереженням поточного плану маєтку.

### Ігри-носії

- [`GAME-0173` — Blue Prince](../games/a-f/blue-prince.md)

## ACT-301

- Назва: Заборонити одного допустимого оператора протилежної ролі
- Переглянуто: `2026-08-28`

### Операційне визначення

Під час запланованої фази обмеження складу одна команда вибирає допустимого оператора протилежної ролі й додає його до спільного списку недоступних.

### Включає

Заборони операторів нападу й захисту в Rainbow Six Siege Pro League.

### Виключає

Вибір власного оператора; вимкнення косметичного елемента; турнірне вето мапи поза ігровим матчем.

### Ігри-носії

- [`GAME-0174` — Tom Clancy’s Rainbow Six Siege](../games/s-z/tom-clancys-rainbow-six-siege.md)

## ACT-302

- Назва: Керувати активним пристроєм спостереження або його каналом
- Переглянуто: `2026-08-28`

### Операційне визначення

Увійти до каналу справного віддаленого пристрою та, якщо можливо, рухати чи повертати його, сканувати або ставити позначку.

### Включає

Дрони нападників, камери захисників і сумісні інструменти спостереження у Rainbow Six Siege.

### Виключає

Огляд із центром на персонажі; статичну мінімапу; перегляд післяматчевого повтору; автоматичне виявлення без керування пристроєм.

### Ігри-носії

- [`GAME-0174` — Tom Clancy’s Rainbow Six Siege](../games/s-z/tom-clancys-rainbow-six-siege.md)

## ACT-303

- Назва: Проламати допустиму поверхню
- Переглянуто: `2026-10-13`

### Операційне визначення

Гравець обирає стіну, підлогу, стелю, двері чи вікно, що відповідає умовам, і підтверджує застосування сумісного удару, вибухівки або засобу проламування укріплень, щоб відкрити чи розширити геометрію проходу, огляду або пробиття.

### Включає

Пролом звичайних поверхонь і сумісний пролом укріпленої стіни у Rainbow Six Siege.

### Виключає

Звичайне проникнення кулі без корисного отвору; встановлення укріплення; косметичні уламки; довільний видобуток рельєфу до інвентарю.

### Ігри-носії

- [`GAME-0508` — Ready or Not](../games/m-r/ready-or-not.md)
- [`GAME-0568` — Teardown](../games/s-z/teardown.md)
- [`GAME-0174` — Tom Clancy’s Rainbow Six Siege](../games/s-z/tom-clancys-rainbow-six-siege.md)

## ACT-304

- Назва: Налаштувати склад автономної футбольної команди й двофазний тактичний план
- Переглянуто: `2026-08-31`

### Операційне визначення

Перед матчем або під час нього гравець у ролі менеджера призначає допустимих футболістів команди на дозволені позиції складу та налаштовує окремі формації, ролі й командні вказівки для гри у володінні м’ячем і без нього, за якими команда діє автономно.

### Включає

Вибір складу команди й окремих тактичних формацій для гри у володінні м’ячем і без нього у Football Manager 26.

### Виключає

Безпосереднє пересування футболіста; підписання контракту з футболістом; вибір лише декоративного зображення формації.

### Ігри-носії

- [`GAME-0175` — Football Manager 26](../games/a-f/football-manager-26.md)

## ACT-305

- Назва: Підтвердити менеджерську заміну або тактичну зміну під час матчу
- Переглянуто: `2026-10-13`

### Операційне визначення

Поки автономний футбольний матч триває, гравець підтверджує одну дозволену зміну футболіста, ролі, формації чи командної вказівки, яку команда застосовує з наступного стану матчу, що допускає цю зміну.

### Включає

Заміни й тактичні зміни під час матчу у Football Manager 26.

### Виключає

Безпосереднє керування футболістом або м’ячем; редагування складу після матчу; непідтверджені експерименти на екрані аналізу.

### Ігри-носії

- [`GAME-0175` — Football Manager 26](../games/a-f/football-manager-26.md)

## ACT-306

- Назва: Підготувати бійця до реакції на рух у звичайній ворожій фазі
- Переглянуто: `2026-08-31`

### Операційне визначення

У межах визначеної гілки звичайної ворожої фази гравець витрачає залишок доступних дій уже викритого керованого бійця, щоб підготувати одну дистанційну атаку, яка може спрацювати після завершення фази загону, коли допустимий ворог рухається там, де цей боєць може його обстріляти. Ця межа не моделює реакцій на активаційний рух ворогів у фазі гравця й не стверджує, що гра їх забороняє.

### Включає

Звичайний Overwatch у ворожій фазі, підготовлений після викриття в досліджуваній місії Operation Gatecrasher у XCOM 2.

### Виключає

Реакції на активаційний рух ворогів у фазі гравця з цієї звуженої гілки; негайний постріл по вибраній цілі; постійну атаку по зоні; реакцію ворога, яку не підготував гравець.

### Ігри-носії

- [`GAME-0176` — XCOM 2](../games/s-z/xcom-2.md)

## ACT-307

- Назва: Підтвердити одну тактичну взаємодію бійця з об’єктом місії поруч
- Переглянуто: `2026-08-31`

### Операційне визначення

Гравець наказує керованому бійцеві, який стоїть поруч із допустимим об’єктом, виконати визначену взаємодію місії, витрачаючи потрібні для цього дії та змінюючи стан цілі.

### Включає

Встановлення заряду X4 на монументі ADVENT у місії Operation Gatecrasher гри XCOM 2.

### Виключає

Звичайний рух; підбирання декоративних елементів оточення; автоматичне завершення місії лише через вхід у певну зону.

### Ігри-носії

- [`GAME-0176` — XCOM 2](../games/s-z/xcom-2.md)

## ACT-308

- Назва: Виконати стрибок, ухильний маневр або зміну орієнтації транспорту в повітрі
- Переглянуто: `2026-10-03`

### Операційне визначення

Під час прямого керування поточним транспортним засобом гравець виконує дозволений стрибок, напрямковий ухильний маневр або безперервну команду зміни орієнтації в повітрі, що змінює його положення й напрям поза самим наземним кермуванням.

### Включає

Стрибок, подвійний стрибок, напрямковий переворот, обертання навколо поздовжньої осі та повітряне керування нахилом чи поворотом у Rocket League.

### Виключає

Звичайне наземне кермування; тягу прискорення без можливості стрибка; автоматичну анімацію трюку.

### Ігри-носії

- [`GAME-0542` — Excite Truck](../games/a-f/excite-truck.md)
- [`GAME-0712` — "JellyCar Worlds"](../games/g-l/jellycar-worlds.md)
- [`GAME-0655` — "Kirby Air Riders"](../games/g-l/kirby-air-riders.md)
- [`GAME-0507` — MotorStorm](../games/m-r/motorstorm.md)
- [`GAME-0177` — Rocket League](../games/m-r/rocket-league.md)
- [`GAME-0488` — wipEout](../games/s-z/wipeout.md)

## ACT-309

- Назва: Витрачати скінченний запас машини на спрямоване прискорення
- Переглянуто: `2026-09-06`

### Операційне визначення

Під час прямого керування машиною гравець вмикає, утримує або відпускає її скінченний запас прискорення, витрачаючи весь поточний обсяг або його частину, щоб додати спрямовану тягу вздовж поточної орієнтації машини в наземному чи повітряному русі; сама команда не володіє правилом, за яким той запас поповнюють, обмежують або відновлюють.

### Включає

Наземне прискорення, набір висоти в повітрі й відновлення руху за допомогою збереженого запасу прискорення в Rocket League; звичайне прискорення нітро під час дослідженої погоні за автовозом у Need for Speed Payback; увімкнення Burst Nitrous у дослідженому заїзді або обов’язковій погоні Need for Speed Unbound.

### Виключає

Пасивну тягу двигуна; постійний необмежений приріст швидкості; витрату носимого лікувального підсилювача; особливу бойову чи водійську форму героя; системну поведінку, що поповнює, обмежує або відновлює цей запас.

### Ігри-носії

- [`GAME-0242` — "Asphalt Legends"](../games/a-f/asphalt-legends.md)
- [`GAME-0470` — "Burnout 3: Takedown"](../games/a-f/burnout-3-takedown.md)
- [`GAME-0374` — Burnout Paradise](../games/a-f/burnout-paradise.md)
- [`GAME-0384` — F-Zero GX](../games/a-f/f-zero-gx.md)
- [`GAME-0226` — "Need for Speed: Most Wanted (2005)"](../games/m-r/need-for-speed-most-wanted-2005.md)
- [`GAME-0208` — 'Need for Speed Payback'](../games/m-r/need-for-speed-payback.md)
- [`GAME-0235` — "Need for Speed: The Run"](../games/m-r/need-for-speed-the-run.md)
- [`GAME-0199` — "Need for Speed Unbound"](../games/m-r/need-for-speed-unbound.md)
- [`GAME-0177` — Rocket League](../games/m-r/rocket-league.md)
- [`GAME-0677` — "Stunt Car Racer"](../games/s-z/stunt-car-racer.md)
- [`GAME-0409` — 'Twisted Metal: Black'](../games/s-z/twisted-metal-black.md)
- [`GAME-0603` — "Wheel World"](../games/s-z/wheel-world.md)

## ACT-310

- Назва: Обрати точку повторної появи відносно своїх воріт після знищення авто
- Переглянуто: `2026-08-31`

### Операційне визначення

У короткому вікні після знищення авто його гравець обирає одну з наразі запропонованих точок появи відносно воріт власної команди, перш ніж авто повернеться до активного керування.

### Включає

Вибір точки повторної появи після знищення авто в мережевому матчі Rocket League v2.72.

### Виключає

Вибір початкової позиції стартового розіграшу; постійне місце появи; повернення вибулого гравця лише в наступному раунді.

### Ігри-носії

- [`GAME-0177` — Rocket League](../games/m-r/rocket-league.md)

## ACT-311

- Назва: Спожити напій, який персонаж має при собі, для відновлення водного запасу
- Переглянуто: `2026-08-28`

### Операційне визначення

Гравець споживає один допустимий напій, який персонаж має при собі, щоб збільшити його поточний водний запас на визначене для цього напою значення.

### Включає

Вживання фільтрованої води чи іншого дослідженого предмета з водою в режимі виживання Subnautica.

### Виключає

Їжу для відновлення ситості; автоматичне пиття з довкілля; виготовлення напою.

### Ігри-носії

- [`GAME-0210` — DayZ](../games/a-f/dayz.md)
- [`GAME-0178` — Subnautica](../games/s-z/subnautica.md)
- [`GAME-0285` — "The Long Dark"](../games/s-z/the-long-dark.md)

## ACT-312

- Назва: Спіймати одну досяжну істоту, що вільно плаває
- Переглянуто: `2026-08-28`

### Операційне визначення

Гравець простягає руку до однієї допустимої малої істоти, що вільно рухається, і забирає її безпосередньо до інвентарю при собі, доки вона не вийшла за межі досяжності.

### Включає

Ловлю рукою доступного піпера чи риби-міхура в Subnautica.

### Виключає

Збирання нерухомої сировини; подолання істоти за допомогою зброї; автоматичне збирання пасткою.

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

Вибір готового креслення в інтерфейсі виготовлення; автономний пошук ресурсів по всій кімнаті; миттєве підбирання або одноімпульсне обстеження цілі; типізований результат після завершення сканування.

### Ігри-носії

- [`GAME-0243` — Battlefield Hardline](../games/a-f/battlefield-hardline.md)
- [`GAME-0678` — "Metroid Prime 4: Beyond"](../games/m-r/metroid-prime-4-beyond.md)
- [`GAME-0355` — Metroid Prime](../games/m-r/metroid-prime.md)
- [`GAME-0500` — Pacific Drive](../games/m-r/pacific-drive.md)
- [`GAME-0178` — Subnautica](../games/s-z/subnautica.md)

## ACT-314

- Назва: Збудувати або розібрати модуль бази
- Переглянуто: `2026-08-28`

### Операційне визначення

Гравець спрямовує будівельний інструмент із живленням на допустимі положення й орієнтацію одного підводного модуля або на вже наявний модуль і утримує команду будівництва чи розбирання до завершення поступу, забезпеченого матеріалами.

### Включає

Будівництво або демонтаж I-відсіку, люка чи сонячної панелі за допомогою Habitat Builder у Subnautica.

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

Гравець вибирає власний виробничий об’єкт або спільну панель такого об’єкта й додає одну наразі доступну одиницю чи споруду до його скінченної активної черги або виробничого каналу.

### Включає

Додавання селян або військових одиниць до черги у придатних спорудах Age of Empires II: Definitive Edition; додавання споруди або піхотної одиниці до черги через відповідний виробничий об’єкт Command & Conquer Remastered Collection.

### Виключає

Вибір однієї міської цілі виробництва, результат якої підбивається за ходами; появу безкоштовної сценарної одиниці; вибір технології замість одиниці.

### Ігри-носії

- [`GAME-0179` — Age of Empires II: Definitive Edition](../games/a-f/age-of-empires-ii-definitive-edition.md)
- [`GAME-0453` — Age of Mythology](../games/a-f/age-of-mythology.md)
- [`GAME-0397` — 'Command & Conquer: Red Alert 2'](../games/a-f/command-and-conquer-red-alert-2.md)
- [`GAME-0275` — Command & Conquer Remastered Collection](../games/a-f/command-and-conquer-remastered-collection.md)
- [`GAME-0209` — Cossacks 3](../games/a-f/cossacks-3.md)
- [`GAME-0410` — Halo Wars](../games/g-l/halo-wars.md)
- [`GAME-0517` — Homeworld](../games/g-l/homeworld.md)
- [`GAME-0469` — StarCraft](../games/s-z/starcraft.md)
- [`GAME-0287` — Stellaris](../games/s-z/stellaris.md)
- [`GAME-0701` — "Warcraft II: Tides of Darkness"](../games/s-z/warcraft-ii-tides-of-darkness.md)

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
- [`GAME-0453` — Age of Mythology](../games/a-f/age-of-mythology.md)
- [`GAME-0209` — Cossacks 3](../games/a-f/cossacks-3.md)
- [`GAME-0517` — Homeworld](../games/g-l/homeworld.md)
- [`GAME-0194` — "Mount & Blade II: Bannerlord"](../games/m-r/mount-and-blade-ii-bannerlord.md)
- [`GAME-0191` — "Total War: WARHAMMER III"](../games/s-z/total-war-warhammer-iii.md)

## ACT-318

- Назва: Призначити працівника на доступну господарську роботу
- Переглянуто: `2026-10-14`

### Операційне визначення

Гравець наказує одному чи кільком вибраним господарським працівникам збирати ресурс із досяжного джерела, будувати поставлений фундамент або ремонтувати дозволений пошкоджений власний об’єкт.

### Включає

Призначення селянам збирання харчів, деревини, золота чи каменю, будівництва або ремонту в Age of Empires II: Definitive Edition; призначення терранському SCV видобування мінералів, будівництва чи ремонту в оригінальній StarCraft.

### Виключає

Автоматичні кроки роботи після призначення; налаштування глобальної політики пріоритетів працівників; прямі накази військової атаки.

### Ігри-носії

- [`GAME-0179` — Age of Empires II: Definitive Edition](../games/a-f/age-of-empires-ii-definitive-edition.md)
- [`GAME-0453` — Age of Mythology](../games/a-f/age-of-mythology.md)
- [`GAME-0209` — Cossacks 3](../games/a-f/cossacks-3.md)
- [`GAME-0570` — Cult of the Lamb](../games/a-f/cult-of-the-lamb.md)
- [`GAME-0517` — Homeworld](../games/g-l/homeworld.md)
- [`GAME-0469` — StarCraft](../games/s-z/starcraft.md)
- [`GAME-0701` — "Warcraft II: Tides of Darkness"](../games/s-z/warcraft-ii-tides-of-darkness.md)

## ACT-319

- Назва: Налаштувати й запустити обмежений план Free Flight
- Переглянуто: `2026-08-30`

### Операційне визначення

До отримання керування гравець вибирає один літак, пункти вильоту й прибуття, маршрут, налаштування умов середовища й допомоги, а потім запускає цей визначений політ у режимі Free Flight.

### Включає

Політ Cessna 172 G1000 від стоянки KBFI до стоянки KTIW за фіксованого денного часу й погодних умов Clear Skies у межах аналізу Microsoft Flight Simulator 2024.

### Виключає

Прийняття завдання Career; зміну погоди в реальному часі після запуску; подання розкладу автономних перевезень; вибір лише дорожньої маршрутної точки.

### Ігри-носії

- [`GAME-0180` — Microsoft Flight Simulator 2024](../games/m-r/microsoft-flight-simulator-2024.md)

## ACT-320

- Назва: Керувати живленням, двигуном і конфігурацією літака
- Переглянуто: `2026-08-30`

### Операційне визначення

Гравець перемикає тумблери й важелі в кабіні, які встановлюють або змінюють подачу пального, електроживлення, роботу двигуна, освітлення й аеродинамічну конфігурацію, не делегуючи системі керування польотом.

### Включає

Перемикач подачі пального, акумулятор і генератор, авіоніка, регулятор складу суміші, магнето й стартер, важіль тяги, освітлення, тример і закрилки Cessna 172 у дослідженому вільному польоті (Free Flight) Microsoft Flight Simulator 2024.

### Виключає

Рух штурвала або керма напрямку для керування просторовою орієнтацією; автоматичний запуск однією клавішею; налаштування літака до створення екземпляра симуляції.

### Ігри-носії

- [`GAME-0180` — Microsoft Flight Simulator 2024](../games/m-r/microsoft-flight-simulator-2024.md)

## ACT-321

- Назва: Безпосередньо пілотувати літак із фіксованим крилом
- Переглянуто: `2026-08-30`

### Операційне визначення

Гравець безперервно задає тангаж, крен, рискання, тягу й колісне гальмування літака з фіксованим крилом, щоб рулити, злітати, летіти, сідати й зупинятися, замість вибору пункту призначення для автономного руху.

### Включає

Ручне пілотування й наземне керування Cessna 172 G1000 без автопілота в межах аналізованого польоту Free Flight у Microsoft Flight Simulator 2024.

### Виключає

Перемикання режимів меха; керування парашутом; автономне пілотування ШІ; керування дорожнім транспортом без причинної моделі підіймальної сили й допустимих режимів польоту.

### Ігри-носії

- [`GAME-0180` — Microsoft Flight Simulator 2024](../games/m-r/microsoft-flight-simulator-2024.md)

## ACT-322

- Назва: Зафіксувати одне місце в рольовій черзі до пошуку матчу
- Переглянуто: `2026-08-31`

### Операційне визначення

До пошуку матчу гравець фіксує одну із запропонованих бойових ролей, резервуючи її командне місце й відповідний набір доступних героїв для майбутнього матчу.

### Включає

Вибір ролі Tank, Damage або Support у звичайній черзі Overwatch 5v5 Role Queue перед початком пошуку матчу Quick Play.

### Виключає

Вибір героя після створення лобі; побажання у відкритій черзі Open Queue; автономну роль у групі; позначки профілю облікового запису.

### Ігри-носії

- [`GAME-0181` — Overwatch](../games/m-r/overwatch.md)

## ACT-323

- Назва: Проголосувати за одну із запропонованих мап або випадковий варіант
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

Гравець створює або змінює розблоковану лінію виробництва спорядження й призначає обрану кількість військових фабрик країни для подальшого випуску її продукції.

### Включає

Розподіл італійських військових фабрик між піхотним спорядженням, артилерією та літаками підтримки у визначених правилах Hearts of Iron IV.

### Виключає

Вибір будівельного проєкту; ручне виготовлення одного предмета; зміну шаблону дивізії поза межами навчального пакета.

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
- Переглянуто: `2026-10-13`

### Операційне визначення

Гравець призначає одне доступне авіакрило повітряному регіону, що відповідає умовам, і вмикає або вимикає одне з його підтримуваних зараз завдань.

### Включає

Призначення винищувачів або літаків безпосередньої підтримки до Східної Африки та ввімкнення завдань переваги в повітрі чи підтримки наземних сил.

### Виключає

Ручне пілотування; виробнича лінія літака; наказ флоту.

### Ігри-носії

- [`GAME-0182` — Hearts of Iron IV](../games/g-l/hearts-of-iron-iv.md)

## ACT-330

- Назва: Вибрати придатну до появи машину зі складу для наступного наземного виїзду
- Переглянуто: `2026-08-31`

### Операційне визначення

У стані вибору перед появою або після втрати техніки гравець вибирає один наразі допустимий транспортний засіб зі складу, зафіксованого на матч, і призначає його наступною наземною машиною під безпосереднім керуванням.

### Включає

Вибір M2A4, LVT(A)(1) або M2A2 для однієї з досліджених появ у Ground Arcade War Thunder, коли резервне повторне використання техніки недоступне.

### Виключає

Купівлю чи дослідження машини; зміну вже наявної машини поза матчем; вхід до машини, яка вже є у світі; тимчасові літакові вильоти.

### Ігри-носії

- [`GAME-0184` — War Thunder](../games/s-z/war-thunder.md)

## ACT-331

- Назва: Лишити або замінити початкову руку
- Переглянуто: `2026-08-31`

### Операційне визначення

До першого ходу гравець або приймає поточну показану початкову руку, або запитує руку на заміну, а згодом кладе потрібну кількість карт униз бібліотеки.

### Включає

Збереження початкової руки або лондонський муліган (London mulligan) у визначеній партії Starter Deck Duel гри MTG Arena.

### Виключає

Скидання карт під час поточного ходу; вибір карт під час конструювання колоди; повторний добір усієї руки як бойова дія, яку можна виконувати знову.

### Ігри-носії

- [`GAME-0185` — "Magic: The Gathering Arena"](../games/m-r/magic-the-gathering-arena.md)

## ACT-332

- Назва: Зіграти одну землю з руки
- Переглянуто: `2026-08-31`

### Операційне визначення

Активний гравець кладе карту землі з руки на поле бою під час допустимої головної фази, не розігруючи її як закляття.

### Включає

Розігрування Plains, Island, Tranquil Cove або Temple of Enlightenment із колоди Arcane Aerialists.

### Виключає

Розігрування закляття постійного об’єкта; активацію манової здібності землі; введення землі на поле бою за вказівкою іншої карти.

### Ігри-носії

- [`GAME-0185` — "Magic: The Gathering Arena"](../games/m-r/magic-the-gathering-arena.md)

## ACT-333

- Назва: Розіграти закляття з видимої руки
- Переглянуто: `2026-08-31`

### Операційне визначення

Гравець вибирає одну придатну для розігрування карту у видимій руці, оголошує всі потрібні режими, цілі та значення змінних, а потім підтверджує оплату вартості, яку може сплатити, щоб утворене закляття увійшло до стосу.

### Включає

Розігрування істоти, миттєвого закляття, чаклунства, артефакту або чарів з Arcane Aerialists згідно з поточними правилами допустимого моменту й цілей для відповідної карти.

### Виключає

Розігрування землі; активацію тексту постійного об’єкта, який уже перебуває на полі бою; негайне розв’язання закляття без вікна пріоритету.

### Ігри-носії

- [`GAME-0185` — "Magic: The Gathering Arena"](../games/m-r/magic-the-gathering-arena.md)

## ACT-334

- Назва: Активувати уміння контрольованої карти
- Переглянуто: `2026-10-13`

### Операційне визначення

Гравець обирає одне активоване уміння контрольованої карти, задає потрібні варіанти й цілі та сплачує вартість активації, після чого уміння потрапляє до стеку, якщо воно не є умінням мани.

### Включає

Активацію Goldvein Pick або іншого дозволеного активованого уміння в дослідженій партії готовою колодою.

### Виключає

Розігрування самої карти-джерела; автоматичні спрацьовувані уміння; звичайне розігрування землі; системне розв’язання тексту активованого уміння.

### Ігри-носії

- [`GAME-0185` — "Magic: The Gathering Arena"](../games/m-r/magic-the-gathering-arena.md)

## ACT-335

- Назва: Передати пріоритет без нового об’єкта
- Переглянуто: `2026-08-31`

### Операційне визначення

Гравець із пріоритетом відмовляється від закляття, уміння чи особливої дії та надає супернику можливість відповісти.

### Включає

Явне або автоматичне передавання пріоритету в Arena, коли закляття, здібність, фаза чи крок очікують відповіді обох гравців.

### Виключає

Одностороннє завершення ходу; здачу; виконання об’єкта до можливості відповісти.

### Ігри-носії

- [`GAME-0185` — "Magic: The Gathering Arena"](../games/m-r/magic-the-gathering-arena.md)

## ACT-336

- Назва: Оголошувати допустимий набір істот-нападників
- Переглянуто: `2026-08-31`

### Операційне визначення

На кроці оголошення нападників активний гравець обирає будь-яку допустиму підмножину контрольованих істот і призначає кожну з них нападником проти суперника або іншого дозволеного захисника.

### Включає

Атака неповернутими істотами з наданої колоди Arcane Aerialists, яких гравець контролює від початку цього ходу або які мають прискорення.

### Виключає

Завдання бойової шкоди; вибір блокувальників; розігрування закляття у вікні пріоритету під час бою.

### Ігри-носії

- [`GAME-0185` — "Magic: The Gathering Arena"](../games/m-r/magic-the-gathering-arena.md)

## ACT-337

- Назва: Оголошувати допустимих істот-блокувальників
- Переглянуто: `2026-08-31`

### Операційне визначення

На кроці оголошення блокувальників гравець, який захищається, призначає будь-яких допустимих неповернутих істот під своїм контролем блокувати атакувальних істот за чинними правилами обходу блокування, обмеженнями та вимогами.

### Включає

Призначення придатних істот Arcane Aerialists блокувальниками, зокрема блокування нападника з польотом летючою істотою.

### Виключає

Вибір нападників; призначення бойової шкоди; розігрування миттєвого закляття після оголошення блокувальників.

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

- Назва: Передати виготовлений предмет відродження привиду напарника
- Переглянуто: `2026-08-31`

### Операційне визначення

Один живий гравець спрямовує предмет відродження, який має при собі, на привида загиблого напарника поблизу й застосовує цей предмет, щоб повернути напарника до гри в тілесній формі.

### Включає

Передавання Telltale Heart привиду іншого вцілілого Wilson у дослідженій межі.

### Виключає

Самовідродження привида; дотик до Florid Postern у режимі Endless; автоматичну повторну появу; лікування живого напарника.

### Ігри-носії

- [`GAME-0186` — "Don’t Starve Together"](../games/a-f/dont-starve-together.md)

## ACT-340

- Назва: Вибрати або змінити клас у командній зоні появи
- Переглянуто: `2026-08-31`

### Операційне визначення

Коли правила дозволяють вибір класу для командної появи, гравець вибирає один доступний для гри клас і призначає його поточному керованому тілу або тілу наступного життя разом із відповідним базовим стандартним комплектом.

### Включає

Вибір або зміна одного з дев’яти звичайних класів Team Fortress 2 під час командної появи в Casual Payload, із дозволеними повтореннями класів у товаришів по команді.

### Виключає

Вибір героя на весь матч; фіксацію місця в рольовій черзі; вибір напарника Team-Up; налаштування альтернативної зброї; косметичну зовнішність.

### Ігри-носії

- [`GAME-0187` — Team Fortress 2](../games/s-z/team-fortress-2.md)

## ACT-341

- Назва: Виконати контекстну взаємодію зі станом сутності світу
- Переглянуто: `2026-10-02`

### Операційне визначення

Гравець звертається до одного досяжного заданого автором актора, пристрою або створеного гравцем об’єкта світу зі змінним станом і підтверджує його поточну допустиму взаємодію: допомогу, читання, активацію, збирання, встановлення, ремонт, відмикання або відкриття. Це змінює місцевий стан цілі, актора, пристрою, інвентарю чи маршруту.

### Включає

Читання Bloody Memo у Sastasha, активація відповідного корала й відкритого перемикача, збирання та використання ключів Captain's Quarters і Waverider Gate, відкриття їхніх брам і включеної до дослідження скрині.

### Виключає

Звичайну атаку зброєю; довільне виготовлення предметів; вибір репліки; взаємодію поза поточним обмеженим маршрутом або ціллю.

### Ігри-носії

- [`GAME-0718` — "A Highland Song"](../games/a-f/a-highland-song.md)
- [`GAME-0653` — "A Quiet Place: The Road Ahead"](../games/a-f/a-quiet-place-the-road-ahead.md)
- [`GAME-0228` — A Way Out](../games/a-f/a-way-out.md)
- [`GAME-0223` — Aion Classic](../games/a-f/aion-classic.md)
- [`GAME-0257` — "Alien: Isolation"](../games/a-f/alien-isolation.md)
- [`GAME-0456` — Alone in the Dark](../games/a-f/alone-in-the-dark.md)
- [`GAME-0320` — "Animal Crossing: New Horizons"](../games/a-f/animal-crossing-new-horizons.md)
- [`GAME-0520` — Animal Well](../games/a-f/animal-well.md)
- [`GAME-0312` — ASTRO BOT](../games/a-f/astro-bot.md)
- [`GAME-0506` — Avowed](../games/a-f/avowed.md)
- [`GAME-0386` — Banjo-Kazooie](../games/a-f/banjo-kazooie.md)
- [`GAME-0255` — "Batman: Arkham Asylum Game of the Year Edition"](../games/a-f/batman-arkham-asylum-game-of-the-year-edition.md)
- [`GAME-0256` — "BioShock™ Remastered"](../games/a-f/bioshock-remastered.md)
- [`GAME-0557` — "Boktai: The Sun Is in Your Hand"](../games/a-f/boktai-the-sun-is-in-your-hand.md)
- [`GAME-0736` — "Bomb Rush Cyberfunk"](../games/a-f/bomb-rush-cyberfunk.md)
- [`GAME-0546` — Burning Rangers](../games/a-f/burning-rangers.md)
- [`GAME-0347` — "Castlevania: Symphony of the Night"](../games/a-f/castlevania-symphony-of-the-night.md)
- [`GAME-0346` — Chrono Trigger](../games/a-f/chrono-trigger.md)
- [`GAME-0490` — Comix Zone](../games/a-f/comix-zone.md)
- [`GAME-0429` — Commandos: Behind Enemy Lines](../games/a-f/commandos-behind-enemy-lines.md)
- [`GAME-0254` — CONTROL Ultimate Edition](../games/a-f/control-ultimate-edition.md)
- [`GAME-0359` — "Crimson Skies: High Road to Revenge"](../games/a-f/crimson-skies-high-road-to-revenge.md)
- [`GAME-0725` — "Crypt Custodian"](../games/a-f/crypt-custodian.md)
- [`GAME-0570` — Cult of the Lamb](../games/a-f/cult-of-the-lamb.md)
- [`GAME-0596` — "Custom Robo"](../games/a-f/custom-robo.md)
- [`GAME-0738` — "Dandara: Trials of Fear Edition"](../games/a-f/dandara-trials-of-fear-edition.md)
- [`GAME-0629` — "Dark Cloud"](../games/a-f/dark-cloud.md)
- [`GAME-0281` — Darkest Dungeon](../games/a-f/darkest-dungeon.md)
- [`GAME-0459` — Daxter](../games/a-f/daxter.md)
- [`GAME-0282` — Dead Cells](../games/a-f/dead-cells.md)
- [`GAME-0368` — Dead Rising](../games/a-f/dead-rising.md)
- [`GAME-0259` — "Dead Space (2023 remake)"](../games/a-f/dead-space-2023.md)
- [`GAME-0266` — Deep Rock Galactic](../games/a-f/deep-rock-galactic.md)
- [`GAME-0193` — Destiny 2](../games/a-f/destiny-2.md)
- [`GAME-0252` — "Detroit: Become Human"](../games/a-f/detroit-become-human.md)
- [`GAME-0353` — "Deus Ex: Game of the Year Edition"](../games/a-f/deus-ex-game-of-the-year-edition.md)
- [`GAME-0437` — Diner Dash](../games/a-f/diner-dash.md)
- [`GAME-0515` — Dino Crisis](../games/a-f/dino-crisis.md)
- [`GAME-0264` — Disco Elysium - The Final Cut](../games/a-f/disco-elysium-the-final-cut.md)
- [`GAME-0247` — Dishonored (2012)](../games/a-f/dishonored-2012.md)
- [`GAME-0301` — "Divinity: Original Sin 2 - Definitive Edition"](../games/a-f/divinity-original-sin-2-definitive-edition.md)
- [`GAME-0565` — Dome Keeper](../games/a-f/dome-keeper.md)
- [`GAME-0352` — DOOM (1993)](../games/a-f/doom-1993.md)
- [`GAME-0245` — DOOM (2016)](../games/a-f/doom-2016.md)
- [`GAME-0286` — DOOM Eternal](../games/a-f/doom-eternal.md)
- [`GAME-0608` — "Dosa Divas"](../games/a-f/dosa-divas.md)
- [`GAME-0269` — DREDGE](../games/a-f/dredge.md)
- [`GAME-0597` — "Duck Detective: The Ghost of Glamping"](../games/a-f/duck-detective-the-ghost-of-glamping.md)
- [`GAME-0592` — Dungeons of Hinterberg](../games/a-f/dungeons-of-hinterberg.md)
- [`GAME-0473` — "Eternal Darkness: Sanity's Requiem"](../games/a-f/eternal-darkness-sanitys-requiem.md)
- [`GAME-0405` — Fable II](../games/a-f/fable-ii.md)
- [`GAME-0231` — Fallout 4](../games/a-f/fallout-4.md)
- [`GAME-0361` — Fallout: New Vegas](../games/a-f/fallout-new-vegas.md)
- [`GAME-0271` — Far Cry 5](../games/a-f/far-cry-5.md)
- [`GAME-0591` — Fatal Frame](../games/a-f/fatal-frame.md)
- [`GAME-0501` — F.E.A.R.](../games/a-f/fear.md)
- [`GAME-0338` — Final Fantasy VII](../games/a-f/final-fantasy-vii.md)
- [`GAME-0188` — FINAL FANTASY XIV Online](../games/a-f/final-fantasy-xiv-online.md)
- [`GAME-0321` — Gears of War](../games/g-l/gears-of-war.md)
- [`GAME-0533` — "Ghost Trick: Phantom Detective"](../games/g-l/ghost-trick-phantom-detective.md)
- [`GAME-0381` — GoldenEye 007](../games/g-l/goldeneye-007.md)
- [`GAME-0314` — Grounded](../games/g-l/grounded.md)
- [`GAME-0560` — Gunstar Heroes](../games/g-l/gunstar-heroes.md)
- [`GAME-0532` — Hades II](../games/g-l/hades-ii.md)
- [`GAME-0239` — Half-Life (1998)](../games/g-l/half-life-1998.md)
- [`GAME-0212` — Half-Life 2](../games/g-l/half-life-2.md)
- [`GAME-0315` — Halo 3](../games/g-l/halo-3.md)
- [`GAME-0581` — "Hardspace: Shipbreaker"](../games/g-l/hardspace-shipbreaker.md)
- [`GAME-0516` — Hi-Fi RUSH](../games/g-l/hi-fi-rush.md)
- [`GAME-0248` — HITMAN World of Assassination](../games/g-l/hitman-world-of-assassination.md)
- [`GAME-0654` — "Hotel Dusk: Room 215"](../games/g-l/hotel-dusk-room-215.md)
- [`GAME-0399` — Ico](../games/g-l/ico.md)
- [`GAME-0484` — Impossible Mission](../games/g-l/impossible-mission.md)
- [`GAME-0510` — Indiana Jones and the Great Circle](../games/g-l/indiana-jones-and-the-great-circle.md)
- [`GAME-0585` — Into the Radius](../games/g-l/into-the-radius.md)
- [`GAME-0464` — "Jet Set Radio Future"](../games/g-l/jet-set-radio-future.md)
- [`GAME-0552` — Jusant](../games/g-l/jusant.md)
- [`GAME-0240` — "Kingdom Come: Deliverance II"](../games/g-l/kingdom-come-deliverance-ii.md)
- [`GAME-0583` — "Kunitsu-Gami: Path of the Goddess"](../games/g-l/kunitsu-gami-path-of-the-goddess.md)
- [`GAME-0388` — L.A. Noire](../games/g-l/la-noire.md)
- [`GAME-0683` — "Last Window: The Secret of Cape West"](../games/g-l/last-window-the-secret-of-cape-west.md)
- [`GAME-0192` — Left 4 Dead 2](../games/g-l/left-4-dead-2.md)
- [`GAME-0394` — LittleBigPlanet 2](../games/g-l/littlebigplanet-2.md)
- [`GAME-0563` — Lorelei and the Laser Eyes](../games/g-l/lorelei-and-the-laser-eyes.md)
- [`GAME-0403` — "Luigi's Mansion"](../games/g-l/luigis-mansion.md)
- [`GAME-0686` — "Maniac Mansion"](../games/m-r/maniac-mansion.md)
- [`GAME-0367` — Mass Effect 2 (Legendary Edition)](../games/m-r/mass-effect-2-legendary-edition.md)
- [`GAME-0238` — "Max Payne (2001)"](../games/m-r/max-payne-2001.md)
- [`GAME-0273` — Max Payne 3](../games/m-r/max-payne-3.md)
- [`GAME-0339` — Metal Gear Solid](../games/m-r/metal-gear-solid.md)
- [`GAME-0260` — Metro Exodus](../games/m-r/metro-exodus.md)
- [`GAME-0727` — "Miniatures"](../games/m-r/miniatures.md)
- [`GAME-0558` — Moss](../games/m-r/moss.md)
- [`GAME-0244` — "Need for Speed Heat"](../games/m-r/need-for-speed-heat.md)
- [`GAME-0588` — Neva](../games/m-r/neva.md)
- [`GAME-0527` — Nine Sols](../games/m-r/nine-sols.md)
- [`GAME-0341` — "Ninja Gaiden Black"](../games/m-r/ninja-gaiden-black.md)
- [`GAME-0483` — "Oddworld: Stranger's Wrath"](../games/m-r/oddworld-strangers-wrath.md)
- [`GAME-0382` — Ōkami HD](../games/m-r/okami-hd.md)
- [`GAME-0224` — Once Human](../games/m-r/once-human.md)
- [`GAME-0431` — Ori and the Blind Forest](../games/m-r/ori-and-the-blind-forest.md)
- [`GAME-0293` — Ori and the Will of the Wisps](../games/m-r/ori-and-the-will-of-the-wisps.md)
- [`GAME-0500` — Pacific Drive](../games/m-r/pacific-drive.md)
- [`GAME-0562` — Parasite Eve](../games/m-r/parasite-eve.md)
- [`GAME-0201` — PAYDAY 2](../games/m-r/payday-2.md)
- [`GAME-0232` — PAYDAY 3](../games/m-r/payday-3.md)
- [`GAME-0731` — "Pengo"](../games/m-r/pengo.md)
- [`GAME-0523` — Pentiment](../games/m-r/pentiment.md)
- [`GAME-0622` — "Pepper Grinder"](../games/m-r/pepper-grinder.md)
- [`GAME-0291` — Persona 5 Royal](../games/m-r/persona-5-royal.md)
- [`GAME-0518` — Pokémon Pokopia](../games/m-r/pokemon-pokopia.md)
- [`GAME-0258` — "Prey (2017)"](../games/m-r/prey-2017.md)
- [`GAME-0344` — "Prince of Persia: The Sands of Time"](../games/m-r/prince-of-persia-the-sands-of-time.md)
- [`GAME-0561` — Psychonauts 2](../games/m-r/psychonauts-2.md)
- [`GAME-0358` — Psychonauts](../games/m-r/psychonauts.md)
- [`GAME-0722` — "QuackShot Starring Donald Duck"](../games/m-r/quackshot-starring-donald-duck.md)
- [`GAME-0404` — Ratchet & Clank](../games/m-r/ratchet-and-clank.md)
- [`GAME-0508` — Ready or Not](../games/m-r/ready-or-not.md)
- [`GAME-0684` — "REANIMAL"](../games/m-r/reanimal.md)
- [`GAME-0280` — Resident Evil 2 (2019 remake)](../games/m-r/resident-evil-2-2019.md)
- [`GAME-0249` — Resident Evil 4 (2023 remake)](../games/m-r/resident-evil-4-2023.md)
- [`GAME-0348` — "Resident Evil: Director’s Cut"](../games/m-r/resident-evil-directors-cut.md)
- [`GAME-0512` — Resident Evil Requiem](../games/m-r/resident-evil-requiem.md)
- [`GAME-0522` — Returnal](../games/m-r/returnal.md)
- [`GAME-0270` — Risk of Rain 2](../games/m-r/risk-of-rain-2.md)
- [`GAME-0549` — Roto Force](../games/m-r/roto-force.md)
- [`GAME-0667` — "SAROS"](../games/s-z/saros.md)
- [`GAME-0440` — Scribblenauts](../games/s-z/scribblenauts.md)
- [`GAME-0319` — Sea of Thieves](../games/s-z/sea-of-thieves.md)
- [`GAME-0485` — Shenmue](../games/s-z/shenmue.md)
- [`GAME-0330` — Silent Hill 2 (2024 remake)](../games/s-z/silent-hill-2-2024.md)
- [`GAME-0430` — Silent Hill](../games/s-z/silent-hill.md)
- [`GAME-0615` — "Skate Story"](../games/s-z/skate-story.md)
- [`GAME-0305` — Sons Of The Forest](../games/s-z/sons-of-the-forest.md)
- [`GAME-0502` — South of Midnight](../games/s-z/south-of-midnight.md)
- [`GAME-0230` — "STAR WARS Battlefront II (2017)"](../games/s-z/star-wars-battlefront-ii-2017.md)
- [`GAME-0213` — "STAR WARS Jedi: Fallen Order"](../games/s-z/star-wars-jedi-fallen-order.md)
- [`GAME-0331` — Starfield](../games/s-z/starfield.md)
- [`GAME-0617` — Strange Antiquities](../games/s-z/strange-antiquities.md)
- [`GAME-0599` — "Sword of the Sea"](../games/s-z/sword-of-the-sea.md)
- [`GAME-0568` — Teardown](../games/s-z/teardown.md)
- [`GAME-0695` — "Terranigma"](../games/s-z/terranigma.md)
- [`GAME-0648` — Thank Goodness You're Here!](../games/s-z/thank-goodness-youre-here.md)
- [`GAME-0604` — "The Alters"](../games/s-z/the-alters.md)
- [`GAME-0613` — "The Drifter"](../games/s-z/the-drifter.md)
- [`GAME-0362` — "The Elder Scrolls III: Morrowind"](../games/s-z/the-elder-scrolls-iii-morrowind.md)
- [`GAME-0292` — The Forest](../games/s-z/the-forest.md)
- [`GAME-0729` — "The Last Campfire"](../games/s-z/the-last-campfire.md)
- [`GAME-0559` — The Last Guardian](../games/s-z/the-last-guardian.md)
- [`GAME-0261` — The Last of Us Part I](../games/s-z/the-last-of-us-part-i.md)
- [`GAME-0458` — The Legend of Zelda: Link's Awakening](../games/s-z/the-legend-of-zelda-links-awakening.md)
- [`GAME-0395` — "The Legend of Zelda: Majora’s Mask"](../games/s-z/the-legend-of-zelda-majoras-mask.md)
- [`GAME-0363` — "The Legend of Zelda: Ocarina of Time"](../games/s-z/the-legend-of-zelda-ocarina-of-time.md)
- [`GAME-0593` — "The Legend of Zelda: The Minish Cap"](../games/s-z/the-legend-of-zelda-the-minish-cap.md)
- [`GAME-0553` — The Lost Vikings](../games/s-z/the-lost-vikings.md)
- [`GAME-0531` — The Midnight Walk](../games/s-z/the-midnight-walk.md)
- [`GAME-0528` — The Neverhood](../games/s-z/the-neverhood.md)
- [`GAME-0606` — "The Séance of Blake Manor"](../games/s-z/the-seance-of-blake-manor.md)
- [`GAME-0513` — Thief: The Dark Project](../games/s-z/thief-the-dark-project.md)
- [`GAME-0696` — "Tides of Tomorrow"](../games/s-z/tides-of-tomorrow.md)
- [`GAME-0253` — "Titanfall 2"](../games/s-z/titanfall-2.md)
- [`GAME-0732` — "TOEM"](../games/s-z/toem.md)
- [`GAME-0590` — Tokyo Xtreme Racer](../games/s-z/tokyo-xtreme-racer.md)
- [`GAME-0349` — "Tom Clancy’s Splinter Cell"](../games/s-z/tom-clancys-splinter-cell.md)
- [`GAME-0451` — Tomb Raider (1996)](../games/s-z/tomb-raider-1996.md)
- [`GAME-0250` — Tomb Raider (2013)](../games/s-z/tomb-raider-2013.md)
- [`GAME-0668` — "Tomba!"](../games/s-z/tomba.md)
- [`GAME-0498` — Transport Fever 2](../games/s-z/transport-fever-2.md)
- [`GAME-0268` — Undertale](../games/s-z/undertale.md)
- [`GAME-0294` — V Rising](../games/s-z/v-rising.md)
- [`GAME-0499` — Vagrant Story](../games/s-z/vagrant-story.md)
- [`GAME-0496` — "Warhammer 40,000: Space Marine 2"](../games/s-z/warhammer-40000-space-marine-2.md)
- [`GAME-0603` — "Wheel World"](../games/s-z/wheel-world.md)
- [`GAME-0669` — "Wilmot Works It Out"](../games/s-z/wilmot-works-it-out.md)
- [`GAME-0221` — World of Warcraft](../games/s-z/world-of-warcraft.md)

## ACT-342

- Назва: Повернути розподілені очки розвитку на контрольній точці
- Переглянуто: `2026-08-31`

### Операційне визначення

На допустимій контрольній точці кампанії гравець вибирає один або кілька раніше розподілених вузлів розвитку персонажа й підтверджує дозволене повернення вкладень, щоб їхні очки знову стали нерозподіленими.

### Включає

Reignite the Sparks у Black Myth: Wukong для одного вузла, гілки або всіх наразі розподілених Sparks у Keeper's Shrine без плати Will.

### Виключає

Витрату доступного очка; купівлю платного скидання характеристик; повернення предмета чи розвитку всього облікового запису.

### Ігри-носії

- [`GAME-0189` — "Black Myth: Wukong"](../games/a-f/black-myth-wukong.md)

## ACT-343

- Назва: Підтвердити походження й тілесну зовнішність
- Переглянуто: `2026-08-31`

### Операційне визначення

На обов’язковому етапі створення нового персонажа гравець обирає доступне походження та фіксує дозволені тіло, обличчя, стать й ім’я як сталу особу для кампанії.

### Включає

Вибір Nord і підтвердження параметрів тіла, обличчя та імені в Helgen під час дослідженого нового початку The Elder Scrolls V: Skyrim Special Edition.

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

Відчинення одного визначеного замка тюремної камери рівня Novice під час дослідженого маршруту Hadvar через Helgen Keep у Skyrim Special Edition.

### Виключає

Використання правильного ключа, який гравець має при собі; введення числового коду; автоматичне розв’язання перевірки навички; силове відчинення дверей атакою.

### Ігри-носії

- [`GAME-0190` — "The Elder Scrolls V: Skyrim Special Edition"](../games/s-z/the-elder-scrolls-v-skyrim-special-edition.md)
- [`GAME-0349` — "Tom Clancy’s Splinter Cell"](../games/s-z/tom-clancys-splinter-cell.md)

## ACT-345

- Назва: Замовити допустиму будівлю у власному поселенні
- Переглянуто: `2026-09-21`

### Операційне визначення

Гравець обирає поточно допустиму будівлю або рівень ланцюга у власному поселенні й сплачує зазначені ресурси незалежно від того, чи результат негайний, чи входить до обмеженої черги кампанії.

### Включає

Поставлений у чергу Store House у Kislev Refuge та одна допустима споруда за день у місті Heroes of Might and Magic III: Complete.

### Виключає

Вільне розміщення споруди в реальному часі; вибір цілі міського виробництва з оплатою міським виробітком; найм одиниці; миттєву сценарну декорацію.

### Ігри-носії

- [`GAME-0332` — "Heroes of Might and Magic III: Complete"](../games/g-l/heroes-of-might-and-magic-iii-complete.md)
- [`GAME-0191` — "Total War: WARHAMMER III"](../games/s-z/total-war-warhammer-iii.md)

## ACT-346

- Назва: Розташувати підрозділи в передбойовій зоні розгортання
- Переглянуто: `2026-08-31`

### Операційне визначення

До початку бою в реальному часі гравець вибирає керовані підрозділи й фіксує їхні позиції, напрямки, ширину та групування в межах поточної допустимої області розгортання своєї сторони.

### Включає

Розташування допустимих шикувань Kislev Expedition перед першою битвою біля Beacon у визначеному пролозі Total War: WARHAMMER III.

### Виключає

Подання наказу рухатися після початку бою; вибір місця появи підкріплень; розміщення підрозділів поза межею розгортання; косметичне показування армії.

### Ігри-носії

- [`GAME-0191` — "Total War: WARHAMMER III"](../games/s-z/total-war-warhammer-iii.md)

## ACT-347

- Назва: Найняти доступних у поселенні новобранців до війська, що зберігається в кампанії
- Переглянуто: `2026-09-21`

### Операційне визначення

У власному або відвіданому поселенні гравець вибирає наразі доступні тип і кількість новобранців та сплачує показану ціну, щоб вибрані новобранці потрапили до сумісних комірок або стосів війська, що зберігається в кампанії.

### Включає

Найм новобранців у Tevea в Bannerlord і найм істот за вказану ціну з житла у власному місті Heroes III.

### Виключає

Тренування поставленої в чергу одиниці в стратегії реального часу; поступове переконування полоненого; найм іменного супутника через завдання; автоматичне зростання населення.

### Ігри-носії

- [`GAME-0332` — "Heroes of Might and Magic III: Complete"](../games/g-l/heroes-of-might-and-magic-iii-complete.md)
- [`GAME-0194` — "Mount & Blade II: Bannerlord"](../games/m-r/mount-and-blade-ii-bannerlord.md)

## ACT-348

- Назва: Сісти верхи, безпосередньо вести доступного скакуна й спішитися
- Переглянуто: `2026-09-10`

### Операційне визначення

Гравець дістається придатного доступного скакуна, переходить до їзди або виходить із неї, а верхи безпосередньо керує темпом, напрямком, стрибком і зупинкою, не доручаючи маршрут автоматичному руху.

### Включає

Посадка верхи на поточного осідланого коня Артура Моргана, їзда на ньому та спішування під час дослідженого маршруту розділу 2 Red Dead Redemption 2; такі самі дії із зафіксованим стартовим конем під час досліджених навчальних польових боїв Mount & Blade II: Bannerlord.

### Виключає

Дистанційне підкликання збережуваного скакуна до персонажа (ACT-271); виклик відсутнього спектрального скакуна з переходом до їзди однією активацією (ACT-247); запуск руху верхи за маршрутом до цілі (ACT-243); активацію особливої партнерської здібності супутника (ACT-197); вхід до дорожнього транспорту й керування ним (ACT-201).

### Ігри-носії

- [`GAME-0318` — Battletoads](../games/a-f/battletoads.md)
- [`GAME-0329` — "Donkey Kong Country"](../games/a-f/donkey-kong-country.md)
- [`GAME-0194` — "Mount & Blade II: Bannerlord"](../games/m-r/mount-and-blade-ii-bannerlord.md)
- [`GAME-0165` — Red Dead Redemption 2](../games/m-r/red-dead-redemption-2.md)
- [`GAME-0356` — Shadow of the Colossus](../games/s-z/shadow-of-the-colossus.md)
- [`GAME-0354` — Super Mario World](../games/s-z/super-mario-world.md)

## ACT-349

- Назва: Утримувати блок зброєю в напрямку однієї атаки, що наближається
- Переглянуто: `2026-10-13`

### Операційне визначення

У поточному ближньому бою гравець наводить і утримує захист спорядженою зброєю або щитом у напрямку однієї поточної атаки чи відпускає його, щоб вибрана геометрія захисту могла протистояти удару, що наближається.

### Включає

Напрямлені блоки зброєю та щитом під час дослідженого навчального бою Mount & Blade II: Bannerlord.

### Виключає

Верхній або нижній захист відносно суперника у Street Fighter; підказку парирування з часовою вимогою без вибору напрямку; пасивну броню; покрокову команду захисту Defend.

### Ігри-носії

- [`GAME-0194` — "Mount & Blade II: Bannerlord"](../games/m-r/mount-and-blade-ii-bannerlord.md)

## ACT-350

- Назва: Запросити дозволене місією відновлення виданої машини
- Переглянуто: `2026-08-31`

### Операційне визначення

Під час безпосереднього керування виданою місією машиною гравець запитує передбачене поточними правилами відновлення, ремонт або перехід до позиції відновлення, щоб пошкоджена, розвернута чи застрягла машина могла продовжити спробу. Сама ця команда не зараховує пропущений поступ маршрутом.

### Включає

Звичайне застосування Recover Vehicle під час дослідженої Road Master у BeamNG.drive; перезапуск поточної місії з початку залишається визначеною межею повторної спроби.

### Виключає

Кероване гравцем перемотування з можливістю обрати інше продовження; завантаження збереження кампанії; телепортацію через вільну камеру; ручне збереження й завантаження довільної домашньої позиції.

### Ігри-носії

- [`GAME-0195` — BeamNG.drive](../games/a-f/beamng-drive.md)
- [`GAME-0507` — MotorStorm](../games/m-r/motorstorm.md)
- [`GAME-0235` — "Need for Speed: The Run"](../games/m-r/need-for-speed-the-run.md)

## ACT-351

- Назва: Прийняти польовий контракт із позиченою технікою
- Переглянуто: `2026-08-31`

### Операційне визначення

Із поточного списку польових контрактів гравець приймає одну пропозицію, яка фіксує завдання, призначене поле, показану винагороду й межу поступу, та погоджується на оголошене відрахування за сумісну техніку роботодавця протягом цього контракту.

### Включає

Прийняття дослідженого контракту Fertilizing у Farming Simulator 25 із вибором Borrow Items.

### Виключає

Прийняття дорожнього вантажного замовлення з уже завантаженим транспортом; лізинг машини для загального користування на фермі; купівлю спорядження; призначення автономного працівника; перегляд пропозиції без її прийняття.

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

- Назва: З’їсти страву іншого типу й зайняти комірку їжі для виживання на певний час
- Переглянуто: `2026-08-31`

### Операційне визначення

Гравець споживає одну страву, яку має при собі й тип якої відрізняється від типів у поточному активному наборі, додаючи або поновлюючи її обмежений у часі внесок у допустимій комірці їжі, щоб цей внесок міг змінити межі особистих показників виживання.

### Включає

Надходження однієї дослідженої страви з біому Meadows до однієї з трьох активних комірок Valheim.

### Виключає

Споживання їжі для запобігання голодній смерті; пиття лікувального зілля; пасивне живлення з інвентарю; заміну їжі до того, як це дозволить травлення.

### Ігри-носії

- [`GAME-0197` — Valheim](../games/s-z/valheim.md)

## ACT-354

- Назва: Прочитати світовий дороговказ, щоб відкрити розташування вівтаря боса
- Переглянуто: `2026-08-31`

### Операційне визначення

Взаємодіяти з дороговказом, прив’язаним до певного боса, щоб позначити на особистій мапі найближчий відповідний згенерований вівтар.

### Включає

Взаємодія з дослідженим Вегвізиром Ейктюра на початкових Жертовних Каменях у Valheim.

### Виключає

Рух за вже наявною позначкою мапи; кидання витратного покажчика напрямку; виявлення орієнтира лише входом до його локального радіуса.

### Ігри-носії

- [`GAME-0197` — Valheim](../games/s-z/valheim.md)

## ACT-355

- Назва: Підібрати, кинути або відкинути зброю, що з’явилася на арені
- Переглянуто: `2026-10-13`

### Операційне визначення

Під час поточного матчу на арені гравець взаємодіє з досяжною нейтральною зброєю, щоб зробити її активною зброєю бійця, або підтверджує команду кинути чи відкинути її, яка повертає бійця до набору команд без зброї.

### Включає

Підбирання й кидання бійцем Bödvar зброї Sword або Hammer, що з’явилася у визначеному матчі Stock у Brawlhalla.

### Виключає

Вибір переносної зброї в швидкій комірці; здобуття предмета в постійний інвентар; запуск метального пристрою; косметичні вигляди зброї.

### Ігри-носії

- [`GAME-0198` — Brawlhalla](../games/a-f/brawlhalla.md)
- [`GAME-0681` — "Power Stone 2"](../games/m-r/power-stone-2.md)
- [`GAME-0519` — Power Stone](../games/m-r/power-stone.md)

## ACT-356

- Назва: Виконати ухилення на місці або в напрямку
- Переглянуто: `2026-08-31`

### Операційне визначення

Коли боєць під час гри має змогу виконати дію, гравець подає команду ухилення на місці або в одному напрямку, щоб запросити захищене переміщення й прийняти подальший стан часу відновлення або скидання готовності до ухилення.

### Включає

Наземне ухилення на місці та повітряне ухилення на місці або в напрямку у визначеному матчі Stock у Brawlhalla.

### Виключає

Пасивну ймовірність ухилення; утримування захисту відносно суперника; підказану захисну дію в покроковому бою; переворот транспортного засобу без невразливості.

### Ігри-носії

- [`GAME-0198` — Brawlhalla](../games/a-f/brawlhalla.md)
- [`GAME-0282` — Dead Cells](../games/a-f/dead-cells.md)
- [`GAME-0532` — Hades II](../games/g-l/hades-ii.md)
- [`GAME-0251` — Hades](../games/g-l/hades.md)
- [`GAME-0516` — Hi-Fi RUSH](../games/g-l/hi-fi-rush.md)
- [`GAME-0202` — "NARAKA: BLADEPOINT"](../games/m-r/naraka-bladepoint.md)
- [`GAME-0561` — Psychonauts 2](../games/m-r/psychonauts-2.md)
- [`GAME-0447` — Punch-Out!!](../games/m-r/punch-out.md)
- [`GAME-0330` — Silent Hill 2 (2024 remake)](../games/s-z/silent-hill-2-2024.md)
- [`GAME-0502` — South of Midnight](../games/s-z/south-of-midnight.md)

## ACT-358

- Назва: Підкорити, зв’язати або перемістити досяжного цивільного
- Переглянуто: `2026-08-31`

### Операційне визначення

Гравець звертається до одного досяжного цивільного дозволеною командою пограбування: наказує підкоритися, застосовує одну обмежену стяжку або спрямовує вже покірного заручника йти чи зупинитися.

### Включає

Наказ криком цивільному в Bank Heist гри PAYDAY 2 лягти на підлогу, зв’язування цього цивільного кабельною стяжкою та команди йти слідом або залишатися на місці.

### Виключає

Постріл у ворога; передавання плану людині-союзнику; автоматична паніка; обмін заручника після арешту.

### Ігри-носії

- [`GAME-0201` — PAYDAY 2](../games/m-r/payday-2.md)
- [`GAME-0232` — PAYDAY 3](../games/m-r/payday-3.md)

## ACT-359

- Назва: Підняти, нести, кинути або здати важку сумку
- Переглянуто: `2026-09-03`

### Операційне визначення

Гравець переводить один допустимий цільовий вантаж у сумці до спеціального стану перенесення, переміщує або кидає його у світі й залишає всередині сумісної зони зарахування.

### Включає

Пакування пакунка готівки в Bank Heist гри PAYDAY 2 у сумку, перенесення або кидання цієї грошової сумки й завантаження її до фургона для втечі; пакування, передавання та здавання рідкісноземельних вантажів під час Road Rage у PAYDAY 3.

### Виключає

Підбирання окремої готівки з негайним зарахуванням; спорядження зброї; переміщення фізичного реквізиту без обмежень; подальший розрахунок виплати.

### Ігри-носії

- [`GAME-0201` — PAYDAY 2](../games/m-r/payday-2.md)
- [`GAME-0232` — PAYDAY 3](../games/m-r/payday-3.md)

## ACT-360

- Назва: Вибрати допустиму область появи перед матчем
- Переглянуто: `2026-08-31`

### Операційне визначення

Під час обмеженої підготовки гравець вибирає одну доступну область мапи як початкову позицію керованого учасника й приймає цей вибір після завершення відліку.

### Включає

Вибір точки появи для Viper Ning перед дослідженим матчем Solo BOT Mode на Wanchu.

### Виключає

Вихід із літака в русі; вибір пізнішої повторної появи; випадкове введення в гру без вибору гравця; домашнє місце на рівні облікового запису.

### Ігри-носії

- [`GAME-0202` — "NARAKA: BLADEPOINT"](../games/m-r/naraka-bladepoint.md)

## ACT-361

- Назва: Спрямувати себе до цілі тросом із гаком
- Переглянуто: `2026-09-10`

### Операційне визначення

Гравець наводить багаторазову здібність або заряд гака, який має при собі, на допустиму поверхню чи активного учасника бою та підтверджує зближення вздовж троса до вибраної цілі.

### Включає

Пересування, переслідування та втеча з Grappling Hook у NARAKA: BLADEPOINT; підтягування гаком до позначених опор на поверхні в Sekiro.

### Виключає

Підтягування предмета до гравця; телепортацію без зближення вздовж троса; тихе знешкодження цілі, яка не помічає гравця.

### Ігри-носії

- [`GAME-0202` — "NARAKA: BLADEPOINT"](../games/m-r/naraka-bladepoint.md)
- [`GAME-0288` — "Sekiro™: Shadows Die Twice - GOTY Edition"](../games/s-z/sekiro-shadows-die-twice.md)

## ACT-362

- Назва: Утримувати або відпускати досяжний хват
- Переглянуто: `2026-09-22`

### Операційне визначення

Коли кероване тіло дістає до придатної нерухомої або рухомої поверхні й має доступний запас хвату, гравець утримує команду для зчеплення та спрямованого руху тіла або відпускає її.

### Включає

Хват за поверхню, лазіння, перехід на уступ і навмисне відпускання в PEAK; хват за хутро й виступи першого рухомого колоса у Shadow of the Colossus.

### Виключає

Звичайну ходьбу; пересування драбиною, яке є лише анімацією; необмежене автоматичне лазіння по стінах; незалежне керування кожною з двох рук окремою кнопкою.

### Ігри-носії

- [`GAME-0203` — "PEAK"](../games/m-r/peak.md)
- [`GAME-0356` — Shadow of the Colossus](../games/s-z/shadow-of-the-colossus.md)

## ACT-363

- Назва: Установити на місцевості один альпіністський засіб, узятий із собою
- Переглянуто: `2026-08-31`

### Операційне визначення

Гравець вибирає один альпіністський засіб з обмеженого запасу при собі й застосовує його до сумісної досяжної поверхні, щоб запросити створення опори, лінії або місця відпочинку, які зберігатимуться протягом поточної експедиції.

### Включає

Прокладання лінії з Rope Spool або встановлення Piton у PEAK для подальшої опори під час лазіння.

### Виключає

Постріл гаком, який одразу переміщує користувача; постійне будівництво; викидання інертного предмета; задану авторами драбину.

### Ігри-носії

- [`GAME-0646` — Cairn](../games/a-f/cairn.md)
- [`GAME-0552` — Jusant](../games/g-l/jusant.md)
- [`GAME-0203` — "PEAK"](../games/m-r/peak.md)

## ACT-364

- Назва: Активувати сигнальний предмет, який гравець має при собі, у допустимій зоні
- Переглянуто: `2026-09-09`

### Операційне визначення

Маючи придатний для використання сигнальний предмет у визначеній для нього зоні активації, гравець запалює або запускає його, щоб запросити пов’язану реакцію порятунку чи завершення. Це витрачає можливість подальшого звичайного використання предмета.

### Включає

Запалення Flare в області PEAK для виклику гелікоптера; постріл із зарядженого Distress Pistol з верхівки Lighthouse у випробуванні The Long Dark.

### Виключає

Постріл тим самим предметом лише як бойову атаку; вхід до вже відкритого виходу; суто косметичну емоцію; порятунок, що автоматично запускається від самого прибуття.

### Ігри-носії

- [`GAME-0203` — "PEAK"](../games/m-r/peak.md)
- [`GAME-0285` — "The Long Dark"](../games/s-z/the-long-dark.md)

## ACT-365

- Назва: Обрати доступне спрямування способу життя
- Переглянуто: `2026-08-31`

### Операційне визначення

Гравець обирає одне наразі доступне спрямування в межах способу життя керованого персонажа, замінює пов’язані зі спрямуванням пасивні ефекти та зберігає загальний стан персонажа.

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

- Назва: Виконувати звичайний виклик (Normal Summon) або звичайне встановлення (Normal Set) одного монстра
- Переглянуто: `2026-09-01`

### Операційне визначення

Під час допустимої власної головної фази гравець викладає одного допустимого монстра з руки горілиць у позицію атаки як Normal Summon або долілиць у позицію захисту як Normal Set і витрачає спільне для цих двох процедур право на цей хід.

### Включає

Звичайний випадок із монстром 4-го або нижчого рівня в навчальному розділі Tutorial 10003.

### Виключає

Особливий чи переворотний виклик; виклик за дією ефекту; розв’язання атаки.

### Ігри-носії

- [`GAME-0206` — "Yu-Gi-Oh! Master Duel"](../games/s-z/yu-gi-oh-master-duel.md)

## ACT-372

- Назва: Виконати один особливий виклик за процедурою
- Переглянуто: `2026-10-13`

### Операційне визначення

Гравець оголошує одну зараз дозволену процедуру особливого виклику, вибирає всі потрібні матеріали або джерело й підтверджує використання цих об’єктів за процедурою, щоб відповідний монстр увійшов до дозволеної зони поля та позиції.

### Включає

Доступні особливі виклики Synchro, Xyz або Link із додаткової колоди розділу 10003, яка містить п’ять карт.

### Виключає

Звичайний виклик або виклик із жертвою; автоматичний виклик ефектом карти без обраної гравцем процедури; створення колоди.

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

Гравець оголошує активацію однієї карти Spell або Trap чи одного ефекту монстра, які зараз можна активувати, сплачує визначену вартість і вибирає потрібні цілі, щоб активація стала першою нерозв’язаною ланкою ланцюга.

### Включає

Активацію звичайної Spell, раніше встановленої Trap або допустимого ефекту монстра з незмінного пакета.

### Виключає

Негайне розв’язання тексту; відповідь пізнішою ланкою; сталий текст без активації.

### Ігри-носії

- [`GAME-0206` — "Yu-Gi-Oh! Master Duel"](../games/s-z/yu-gi-oh-master-duel.md)

## ACT-375

- Назва: Додати допустиму відповідь наступною ланкою ланцюга
- Переглянуто: `2026-10-13`

### Операційне визначення

Після активації іншого ефекту гравець, який відповідає, вибирає одну дозволену відповідь такої самої або вищої швидкості, сплачує її витрати й додає її наступною пронумерованою ланкою ланцюга до розв’язання будь-якого пов’язаного ефекту.

### Включає

Додавання допустимої Trap, Quick-Play Spell або Quick Effect до ланцюга в дослідженому двобої.

### Виключає

Відповідь із Spell Speed 1; нову ланку під час розв’язання завершеного ланцюга; передачу пріоритету за правилами MTG.

### Ігри-носії

- [`GAME-0206` — "Yu-Gi-Oh! Master Duel"](../games/s-z/yu-gi-oh-master-duel.md)

## ACT-376

- Назва: Оголосити атаку одного допустимого монстра
- Переглянуто: `2026-09-01`

### Операційне визначення

Під час допустимої фази бою гравець вибирає одного придатного монстра горілиць у позиції атаки й оголошує його звичайну атаку на одного допустимого монстра суперника або безпосередньо на суперника, якщо стан поля це дозволяє.

### Включає

Кожне окреме оголошення атаки в розділі 10003.

### Виключає

Одночасний вибір групи нападників; вибір блокувальника; визначення та застосування бойової шкоди.

### Ігри-носії

- [`GAME-0206` — "Yu-Gi-Oh! Master Duel"](../games/s-z/yu-gi-oh-master-duel.md)

## ACT-377

- Назва: Змінити бойову позицію одного допустимого монстра
- Переглянуто: `2026-09-01`

### Операційне визначення

У допустимій власній головній фазі гравець переводить одного монстра між позиціями атаки горілиць і захисту горілиць або здійснює Flip Summon — переворотний виклик допустимого монстра з позиції захисту долілиць.

### Включає

Законну ручну зміну позиції або Flip Summon у розділі 10003.

### Виключає

Зміну позиції ефектом; звичайне встановлення з руки; оголошення атаки.

### Ігри-носії

- [`GAME-0206` — "Yu-Gi-Oh! Master Duel"](../games/s-z/yu-gi-oh-master-duel.md)

## ACT-378

- Назва: Обслуговувати споряджену зброю ближнього бою в польових умовах
- Переглянуто: `2026-10-13`

### Операційне визначення

Гравець починає незахищену дію з багаторазовим засобом обслуговування спорядженої зброї ближнього бою; після завершення анімації її поточна циклічна шкала гостроти або міцності відновлюється, а бій і час маршруту весь цей час тривають.

### Включає

Заточування Hunter's Knife I точильним каменем під час дослідженого завдання з Great Jagras у Monster Hunter: World; відновлення додатної міцності зброї багаторазовим Grinder у дослідженому вступі Lies of P.

### Виключає

Витрачання скінченного лікувального предмета; поліпшення в кузні; автоматичне відновлення гостроти після бою; ремонт постійного зношення зброї.

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

Таран автомобіля охорони House під час досліджених етапів знищення ворожих автомобілів у The Highway Heist гри Need for Speed Payback.

### Виключає

Випадкове зіткнення з дорожнім транспортом; постріл зі встановленої зброї; поштовх автомобіля в Rocket League, після якого знищена ціль відроджується через заданий час; постановочну аварію без керованого гравцем зближення.

### Ігри-носії

- [`GAME-0470` — "Burnout 3: Takedown"](../games/a-f/burnout-3-takedown.md)
- [`GAME-0542` — Excite Truck](../games/a-f/excite-truck.md)
- [`GAME-0507` — MotorStorm](../games/m-r/motorstorm.md)
- [`GAME-0208` — 'Need for Speed Payback'](../games/m-r/need-for-speed-payback.md)

## ACT-380

- Назва: Завантажити або вивантажити вибрані одиниці через транспорт
- Переглянуто: `2026-09-01`

### Операційне визначення

Гравець вибирає допустимі наземні одиниці й наказує їм увійти до одного досяжного транспортного засобу або вибирає зайнятий транспорт і наказує пасажирам, що перебувають на борту, повернутися на прохідну наземну поверхню в допустимому місці призначення.

### Включає

Завантаження шведських селян і солдатів на пором та їх вивантаження на протилежному березі річки в Cossacks 3: War Ruse — Peace.

### Виключає

Рух самого порома; автоматичну висадку підкріплення; транспортний засіб, у який сідає один безпосередньо керований аватар; одиниці, телепортовані між фіксованими кінцевими точками.

### Ігри-носії

- [`GAME-0429` — Commandos: Behind Enemy Lines](../games/a-f/commandos-behind-enemy-lines.md)
- [`GAME-0209` — Cossacks 3](../games/a-f/cossacks-3.md)

## ACT-381

- Назва: Застосувати одну контекстну дію предмета в руках до іншого предмета
- Переглянуто: `2026-10-05`

### Операційне визначення

Гравець вибирає один предмет, який тримає в руках, і один сумісний предмет в інвентарі або світі, обирає доступну контекстну операцію та підтверджує їх поєднання, поділ, заряджання, ремонт або просте виготовлення.

### Включає

Дії Combine в інвентарі, поділ стосу, заряджання набоями, ремонт і ручне виготовлення з двох предметів у DayZ протягом одного життя новоствореного персонажа в Chernarus.

### Виключає

Вибір абстрактного рецепта з окремої черги виготовлення; спорядження незміненої здобичі; безпосереднє споживання предмета; автоматичне підбирання через контакт; довільні поєднання, яких поточна пара предметів не пропонує.

### Ігри-носії

- [`GAME-0210` — DayZ](../games/a-f/dayz.md)
- [`GAME-0500` — Pacific Drive](../games/m-r/pacific-drive.md)

## ACT-382

- Назва: Звернутися до вцілілих поблизу через місцевий голосовий канал або жест
- Переглянуто: `2026-10-13`

### Операційне визначення

Гравець навмисно говорить через поточний локальний голосовий канал або виконує видимий жест до вцілілих людей поблизу, поки триває керування у спільному світі.

### Включає

Голос поблизу та жести DayZ для привітання, попередження, переговорів, здачі або введення в оману поміченого поблизу незнайомця.

### Виключає

Обмежений тактичний канал лише для союзників команди; зовнішній голосовий сервіс; автоматичні звуки болю чи хвороби; спілкування, яке гарантує правду, союз або відповідь.

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

- [`GAME-0506` — Avowed](../games/a-f/avowed.md)
- [`GAME-0288` — "Sekiro™: Shadows Die Twice - GOTY Edition"](../games/s-z/sekiro-shadows-die-twice.md)
- [`GAME-0303` — Sifu](../games/s-z/sifu.md)
- [`GAME-0213` — "STAR WARS Jedi: Fallen Order"](../games/s-z/star-wars-jedi-fallen-order.md)

## ACT-384

- Назва: Перемикати обмежувач швидкості автомобіля
- Переглянуто: `2026-09-01`

### Операційне визначення

Під час безпосереднього керування дорожнім автомобілем гравець вмикає або вимикає верхню межу швидкості, яка обмежує подальше прискорення, але залишає ручними кермо, гальма й вибір маршруту.

### Включає

Перемикання обмежувача швидкості клавішею F5 у дослідженому відрізку поїздок таксі розділу 2 Mafia (2002) для зменшення спостереженого ризику перевищення швидкості.

### Виключає

Автономний рух за маршрутом; постійне вдосконалення двигуна; налаштування складності події; звичайне гальмування; ціль круїз-контролю, який активно підтримує довільну вибрану швидкість.

### Ігри-носії

- [`GAME-0214` — "Mafia (2002)"](../games/m-r/mafia-2002.md)

## ACT-385

- Назва: Кидати або відкликати багаторазовий ручний інструмент
- Переглянуто: `2026-09-05`

### Операційне визначення

Гравець наводить один наразі доступний багаторазовий ручний інструмент на досяжну сумісну ціль у світі й кидає його або наказує вже розміщеному інструменту від’єднатися й повернутися в руку, де він знову доступний.

### Включає

Кидання й миттєве відкликання обмеженого набору цвяхів Коді під час відрізка з молотком і цвяхами в The Shed гри It Takes Two; наведення, кидок і відкликання Leviathan Axe у дослідженому початковому маршруті God of War.

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

Удари Мей по позначених кнопках, замках маршрутів, замках Toolbox і заданому авторами механізму запуску у визначеному відрізку The Shed гри It Takes Two.

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

Боєць Battlefield V використовує набір інструментів, щоб збудувати або полагодити траншею, мішки з піском, перешкоду, протитанкове загородження чи станцію постачання на Arras.

### Виключає

Необмежене довільне будівництво; укріплення стіни зі скінченного командного запасу Siege; ремонт транспортного засобу; руйнування вже наявної геометрії.

### Ігри-носії

- [`GAME-0220` — Battlefield V](../games/a-f/battlefield-v.md)

## ACT-389

- Назва: Витратити очки загону на виклик підкріплення
- Переглянуто: `2026-09-01`

### Операційне визначення

Поточний командир загону вибирає одне доступне підкріплення, визначає потрібну ціль на полі бою й підтверджує витрату спільно зароблених очок загону, щоб запросити його доставлення.

### Включає

Виклики командиром загону скидання припасів, димового обстрілу або допустимого удару в Battlefield V після того, як загін заробив достатньо очок постачання.

### Виключає

Кидання гранати, яку гравець має при собі; використання спорядженого особистого пристрою; витрачання особистої валюти облікового запису; автоматичний сценарний авіаудар.

### Ігри-носії

- [`GAME-0220` — Battlefield V](../games/a-f/battlefield-v.md)

## ACT-390

- Назва: Готувати приціл і руку, тоді вихоплювати зброю в дуелі
- Переглянуто: `2026-09-02`

### Операційне визначення

Перед дуеллю на вогнепальній зброї з визначеним суперником гравець одночасно утримує один прицільний маркер зосередження на суперникові й зображену руку біля зброї в кобурі, а потім підтверджує вихоплювання раніше за суперника або у відповідь на його видиме вихоплювання.

### Включає

Підготовка Сайласом зосередження й швидкості руки проти Пата Ґарретта в першій сюжетній дуелі Call of Juarez: Gunslinger.

### Виключає

Звичайне вільне прицілювання з уже вихопленою зброєю; вибір бійця перед матчем проти іншого бійця; підказку на одне натискання кнопки з часовою вимогою; автоматичне вихоплювання у вставній сцені.

### Ігри-носії

- [`GAME-0222` — "Call of Juarez: Gunslinger"](../games/a-f/call-of-juarez-gunslinger.md)

## ACT-391

- Назва: Ударяти по вдосконалюваному джерелу нагороди перед отриманням
- Переглянуто: `2026-09-02`

### Операційне визначення

Після того як обмежена сутичка створює небойовий об’єкт нагороди, гравець спрямовує на нього звичайні атаки, щоб спробувати змінити рівень нагороди, перш ніж виконати окрему взаємодію для її отримання.

### Включає

Удари по Mystic Cube of Light and Darkness в Aion Classic перед окремою взаємодією для отримання його нагороди — посиленого спорядження.

### Виключає

Атаку ворога; відкривання незміненої скрині; пошкодження пристрою для звільнення маршруту; витрату валюти на поліпшення з наперед визначеним результатом.

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

- Назва: Розподіляти обмежену потужність апарата між його поточними підсистемами
- Переглянуто: `2026-09-21`

### Операційне визначення

Під час польоту перерозподіляти єдину спільну обмежену потужність апарата між поточними підсистемами рушіїв, захисту, озброєння або переміщення чи відновлювати збалансований розподіл.

### Включає

Керування двигунами, лазерами й щитами X-wing, якого навчають у Form the Vanguard; розподіл потужності між двигунами, щитами, озброєнням і гравітаційним двигуном Frontier.

### Виключає

Витрачання валюти на поліпшення; вибір постійного компонента; перенесення заряду щита між напрямками; застосування одного вміння з часом відновлення.

### Ігри-носії

- [`GAME-0418` — 'FTL: Faster Than Light'](../games/a-f/ftl-faster-than-light.md)
- [`GAME-0225` — "STAR WARS: Squadrons"](../games/s-z/star-wars-squadrons.md)
- [`GAME-0331` — Starfield](../games/s-z/starfield.md)

## ACT-394

- Назва: Спрямовувати заряд щита до одного боку винищувача
- Переглянуто: `2026-09-02`

### Операційне визначення

Переносити наявний заряд захисного поля до передньої або задньої півсфери чи знову врівноважувати його під час польоту.

### Включає

Спрямування щитів X-wing уперед або назад у Form the Vanguard.

### Виключає

Розподіл енергії реактора на щити; поворот корабля, щоб зустріти атаку; ремонт корпусу; підняття одного неспрямованого тимчасового бар’єра.

### Ігри-носії

- [`GAME-0225` — "STAR WARS: Squadrons"](../games/s-z/star-wars-squadrons.md)

## ACT-395

- Назва: Випускати готовий протиракетний засіб винищувача
- Переглянуто: `2026-09-02`

### Операційне визначення

У відповідь на попередження про керовану ракету витратити один готовий протиракетний заряд у вибраний момент, щоб спробувати зірвати наведення або перехопити загрозу.

### Включає

Використання Seeker Warheads із фіксованого спорядження X-wing у першій місії.

### Виключає

Ухилення лише кермуванням; постріл ракетою по цілі; пасивне перехоплення щитом; зміну спорядженого протиракетного засобу поза місією.

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

Одержання модифікатора через Override Console у Fortnite v42.00 Zero Build Solo.

### Виключає

Введення Lobby Hack до пошуку матчу; налаштування правил приватного сервера; підбирання пасивного предмета; придбання поліпшення облікового запису.

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
- Переглянуто: `2026-10-05`

### Операційне визначення

Гравець вибирає одне пошкоджене або заряджуване технологічне гніздо й подає сумісний матеріал або складник, який несе із собою, щоб просунути його ремонт або поповнити заряд, який можна використати.

### Включає

Заповнення поясненої вимоги Scanner, Analysis Visor, Mining Beam, Pulse Engine, Launch Thruster, захисту від небезпек або життєзабезпечення у визначеному вступі No Man’s Sky.

### Виключає

Виготовлення поданого предмета; ремонт будівельного блока; застосування витратного предмета до здоров’я персонажа; встановлення необов’язкового неушкодженого поліпшення.

### Ігри-носії

- [`GAME-0229` — "No Man’s Sky"](../games/m-r/no-mans-sky.md)
- [`GAME-0500` — Pacific Drive](../games/m-r/pacific-drive.md)

## ACT-400

- Назва: Запустити локальний оглядовий імпульс із відновленням
- Переглянуто: `2026-09-02`

### Операційне визначення

Активувати справний локальний оглядовий пристрій, щоб один обмежений імпульс запросив показ придатних ресурсів поблизу.

### Включає

Запуск відремонтованого Exosuit Scanner під час дослідженого навчання No Man’s Sky.

### Виключає

Утримання аналізатора на одній цілі; завантаження швидкого зламу; вибір сектора мапи для віддаленого сканування; пасивні позначки, видимі постійно.

### Ігри-носії

- [`GAME-0229` — "No Man’s Sky"](../games/m-r/no-mans-sky.md)

## ACT-401

- Назва: Розподілити фіксований початковий запас очок характеристик персонажа
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

- Назва: Забрати нагороду за одне завершене відстежуване випробування
- Переглянуто: `2026-09-03`

### Операційне визначення

Коли для видимого відстежуваного випробування вже зафіксовано виконання, гравець вибирає цей завершений запис і подає окрему команду одержання нагороди, яка зараховує визначену нагороду й позначає запис як такий, за яким нагороду вже забрано.

### Включає

Окреме забирання кожного зеленого запису Basics of Survival під час дослідженого ознайомлювального відрізка 7 Days to Die.

### Виключає

Саме виконання умови випробування; автоматичну виплату за завдання; вибір між кількома взаємовиключними предметами нагороди; одержання досягнення поза поточним світом; забирання предмета зі світу; здавання завдання NPC.

### Ігри-носії

- [`GAME-0233` — 7 Days to Die](../games/0-9/7-days-to-die.md)

## ACT-403

- Назва: Замінити один доступний сумісний модуль чинної зброї в бою
- Переглянуто: `2026-09-03`

### Операційне визначення

Зберігаючи керування поточним бійцем, гравець відкриває обмежену панель модулів, вибирає один доступний варіант однієї сумісної категорії для зброї в руках і підтверджує заміну без повернення до стану висадження або підготовки.

### Включає

Заміна через Plus Menu у Battlefield 2042 одного доступного варіанта прицілу, ствола, боєприпасів або підствольного модуля на поточній зброї.

### Виключає

Налаштування спорядження наступного життя; перемикання зброї в руках; підбирання модуля зі світу; косметичну обгортку зброї.

### Ігри-носії

- [`GAME-0234` — Battlefield 2042](../games/a-f/battlefield-2042.md)
- [`GAME-0246` — Crysis Remastered](../games/a-f/crysis-remastered.md)

## ACT-404

- Назва: Замовити одну доступну машину підтримки до допустимої позиції
- Переглянуто: `2026-09-03`

### Операційне визначення

Під живим керуванням обрати доступну машину на спільній панелі, указати допустиму позицію доставлення у світі й підтвердити запит.

### Включає

Запит наземної машини в Battlefield 2042 через планшет виклику з допустимою близькою позицією доставлення.

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

Позначення камерою одного пірата або сторожового собаки під час дослідженої місії першого аванпосту Far Cry 3.

### Виключає

Саме лише бачення учасника; довільну позначку на мапі; автоматичне командне виявлення; огляд ресурсів місцевості замість живого учасника.

### Ігри-носії

- [`GAME-0243` — Battlefield Hardline](../games/a-f/battlefield-hardline.md)
- [`GAME-0246` — Crysis Remastered](../games/a-f/crysis-remastered.md)
- [`GAME-0236` — Far Cry 3](../games/a-f/far-cry-3.md)
- [`GAME-0306` — METAL GEAR SOLID V: THE PHANTOM PAIN](../games/m-r/metal-gear-solid-v-the-phantom-pain.md)

## ACT-406

- Назва: Кинути один інертний відволікальний предмет до досяжної точки світу
- Переглянуто: `2026-09-03`

### Операційне визначення

Гравець обирає досяжний напрямок або місце падіння й кидає неушкоджувальний предмет, чия правилами визначена мета — створити помітний подразник, а не поранити ціль.

### Включає

Кидання каменя, щоб відвернути допустимого пірата під час дослідженої місії першого аванпосту Far Cry 3.

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

- Назва: Спожити взятий із собою відновлювальний засіб без призупинення керування під час гри
- Переглянуто: `2026-09-03`

### Операційне визначення

Поки керований боєць зберігає можливість рухатися й атакувати під час гри, гравець витрачає одну одиницю з обмеженого запасу відновлювальних засобів при собі, щоб запросити відкладене відновлення замість переходу до лікувального процесу, який можна перервати.

### Включає

Використання одного знеболювального під час дослідженого розділу Roscoe Street Station у Max Payne (2001), поки рух, прицілювання й ворожі дії лишаються доступними.

### Виключає

Лікування бинтом або шприцом, що потребує безперервного виконання протягом заданого часу; пасивне відновлення здоров’я; покроковий предмет із миттєвим повним ефектом; лікування іншого учасника.

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

Розгортання власного супутника з інвентарю; наказ рухатися до місця призначення або рухатися з атакою; вибір відповіді в діалозі; безпосереднє керування союзним тілом; заданий супровід, який не можна перемикати.

### Ігри-носії

- [`GAME-0239` — Half-Life (1998)](../games/g-l/half-life-1998.md)
- [`GAME-0700` — "Planet of Lana II: Children of the Leaf"](../games/m-r/planet-of-lana-ii.md)
- [`GAME-0518` — Pokémon Pokopia](../games/m-r/pokemon-pokopia.md)

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
- [`GAME-0501` — F.E.A.R.](../games/a-f/fear.md)
- [`GAME-0239` — Half-Life (1998)](../games/g-l/half-life-1998.md)
- [`GAME-0340` — "Halo: Combat Evolved Anniversary"](../games/g-l/halo-combat-evolved-anniversary.md)
- [`GAME-0260` — Metro Exodus](../games/m-r/metro-exodus.md)
- [`GAME-0508` — Ready or Not](../games/m-r/ready-or-not.md)
- [`GAME-0492` — "Resistance: Fall of Man"](../games/m-r/resistance-fall-of-man.md)
- [`GAME-0430` — Silent Hill](../games/s-z/silent-hill.md)
- [`GAME-0261` — The Last of Us Part I](../games/s-z/the-last-of-us-part-i.md)

## ACT-410

- Назва: Виконувати один ручний крок рецепта на робочій станції
- Переглянуто: `2026-09-03`

### Операційне визначення

На досяжній ручній станції гравець обирає й безпосередньо застосовує один сумісний складник або орган керування, змінюючи незавершену суміш замість одноразового замовлення всього рецепта.

### Включає

Додавання основи або складника, керування нагріванням, використання видимого піскового годинника, подрібнення складника та перенесення суміші у вихідну посудину під час дослідженого варіння Kingdom Come: Deliverance II.

### Виключає

Вибір одного відомого рецепта для негайного розв’язання або виконання в черзі; розкладання складників у сітці виготовлення; автономне виробництво; декоративну взаємодію.

### Ігри-носії

- [`GAME-0240` — "Kingdom Come: Deliverance II"](../games/g-l/kingdom-come-deliverance-ii.md)
- [`GAME-0300` — Overcooked! 2](../games/m-r/overcooked-2.md)

## ACT-411

- Назва: Підтвердити команди й параметри одного очного матчу
- Переглянуто: `2026-09-03`

### Операційне визначення

Перед початком обмеженого змагання гравець підтверджує одну допустиму керовану сторону, суперника й відкриті параметри, що визначають цю окрему спробу.

### Включає

Вибір Oklahoma City Thunder, New York Knicks, локальної гри проти CPU, складності Pro та п’ятихвилинних чвертей для дослідженого показового матчу Play Now у NBA 2K26.

### Виключає

Формування збережуваного складу; пошук матчу; драфт; вибір цілого сезону; зміну правил під час гри; трактування точних назв команд або числових значень як генів.

### Ігри-носії

- [`GAME-0241` — NBA 2K26](../games/m-r/nba-2k26.md)
- [`GAME-0600` — "NBA Street Vol. 2"](../games/m-r/nba-street-vol-2.md)

## ACT-412

- Назва: Спрямувати пас утримуваного м’яча допустимому партнерові
- Переглянуто: `2026-09-03`

### Операційне визначення

Коли керований гравець володіє спільним м’ячем у руках, гравець задає ціль, напрям і вид пасу, що випускає м’яч до допустимого партнера.

### Включає

Прямі, відскокові, навісні й випереджальні паси в дослідженому показовому матчі NBA 2K26.

### Виключає

Передачу м’яча ударом ноги; нецільове викидання; кидок у ціль для набирання очок; автономний пас партнера; вибір адресата в меню.

### Ігри-носії

- [`GAME-0241` — NBA 2K26](../games/m-r/nba-2k26.md)
- [`GAME-0600` — "NBA Street Vol. 2"](../games/m-r/nba-street-vol-2.md)

## ACT-413

- Назва: Виконати кидок у кошик із керованим моментом випуску
- Переглянуто: `2026-09-03`

### Операційне визначення

Гравець починає й відпускає допустимий кидок у кошик, фіксуючи напрям, вид спроби й момент випуску для негайного оцінювання просторового та захисного контексту.

### Включає

Кидки у стрибку кнопкою або стіком, а також контекстні спроби кидка з-під кошика чи данка в дослідженому показовому матчі NBA 2K26.

### Виключає

Удар у футбольні ворота; штрафний, започаткований лише суддівською послідовністю; автоматичний результат симуляції; пас біля кошика.

### Ігри-носії

- [`GAME-0241` — NBA 2K26](../games/m-r/nba-2k26.md)

## ACT-414

- Назва: Виконати спробу перехоплення, блокування або протидії кидку
- Переглянуто: `2026-09-03`

### Операційне визначення

Захищаючись під час одного ігрового володіння м’ячем, гравець виконує одне втручання визначеного типу проти власника м’яча, лінії пасу або спроби кидка в кошик, ризикуючи позицією й контактом заради можливого відхилення м’яча, втрати володіння або промаху.

### Включає

Відбирання м’яча у власника, перехоплення в лінії пасу, блокування та протидія кидку піднятими руками або зі стрибком під час дослідженого показового матчу NBA 2K26.

### Виключає

Саму пасивну близькість; футбольний підкат; вибір схеми в меню; автоматичне втручання партнера; навмисний фол як окрему стратегію.

### Ігри-носії

- [`GAME-0241` — NBA 2K26](../games/m-r/nba-2k26.md)
- [`GAME-0600` — "NBA Street Vol. 2"](../games/m-r/nba-street-vol-2.md)

## ACT-415

- Назва: Викликати заслін партнера для поточного носія м’яча
- Переглянуто: `2026-09-03`

### Операційне визначення

Керуючи поточним власником м’яча, гравець просить допустимого партнера підійти й поставити тимчасовий дозволений заслін, а потім обирає, чи використовувати й як використати утворене розгалуження маршруту.

### Включає

Виклик і використання заслону для проходу, пасу або кидка під час дослідженого показового матчу NBA 2K26.

### Виключає

Розміщення постійної перешкоди; керування повним набором тактичних схем; автономний заслін, якого гравець не викликав; недозволений контакт у русі.

### Ігри-носії

- [`GAME-0241` — NBA 2K26](../games/m-r/nba-2k26.md)

## ACT-416

- Назва: Підтвердити один підказаний маневр за допоміжного кермування
- Переглянуто: `2026-09-03`

### Операційне визначення

Поки допоміжна система безперервно рухає транспорт і кермує ним, гравець підтверджує один наразі запропонований варіант маршруту, дрифту чи повітряного маневру, щоб керований системою рух міг відбутися відповідно до цього вибору.

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

Пред’являючи законні повноваження й підтримуючи достатню прицільну загрозу, гравець наказує одному чи кільком допустимим противникам підкоритися, а потім завершує взяття під варту однієї живої контрольованої досяжної цілі, поки вона ще підкоряється.

### Включає

Команду Freeze й арешт підкореного підозрюваного у визначеному першому сюжетному епізоді Battlefield Hardline.

### Виключає

Сюжетне затримання в діалозі; залякування нейтрального цивільного; смертельне усунення противника; автоматичний арешт після вичерпання здоров’я.

### Ігри-носії

- [`GAME-0243` — Battlefield Hardline](../games/a-f/battlefield-hardline.md)

## ACT-418

- Назва: Погодитися сплатити запропоновану суму за негайне припинення переслідування
- Переглянуто: `2026-09-04`

### Операційне визначення

Під час придатної поточної сутички гравець приймає чинну й посильну пропозицію заплатити за негайне припинення переслідування противником, не втрачаючи накопиченого множника нагороди сесії.

### Включає

Прийняття пропозиції дати хабар поліції за низького HEAT під час дослідженої першої ночі Heat.

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

Glory Kill у DOOM (2016) і DOOM Eternal; наземне добивання у Batman: Arkham Asylum; близькі страти у God of War і Sekiro; показану ближню атаку в Resident Evil 4 (ремейк 2023 року).

### Виключає

Звичайний удар ближнього бою; усунення необізнаної цілі; постріл по приголомшеному ворогу здалеку; автоматичний результат без окремої команди гравця; вимогу, щоб ближня дія неодмінно перемагала ціль.

### Ігри-носії

- [`GAME-0506` — Avowed](../games/a-f/avowed.md)
- [`GAME-0255` — "Batman: Arkham Asylum Game of the Year Edition"](../games/a-f/batman-arkham-asylum-game-of-the-year-edition.md)
- [`GAME-0308` — Bloodborne™](../games/a-f/bloodborne.md)
- [`GAME-0245` — DOOM (2016)](../games/a-f/doom-2016.md)
- [`GAME-0286` — DOOM Eternal](../games/a-f/doom-eternal.md)
- [`GAME-0473` — "Eternal Darkness: Sanity's Requiem"](../games/a-f/eternal-darkness-sanitys-requiem.md)
- [`GAME-0263` — God of War](../games/g-l/god-of-war.md)
- [`GAME-0290` — Lies of P](../games/g-l/lies-of-p.md)
- [`GAME-0323` — "Marvel’s Spider-Man 2"](../games/m-r/marvels-spider-man-2.md)
- [`GAME-0299` — Nioh 2](../games/m-r/nioh-2.md)
- [`GAME-0536` — PRAGMATA](../games/m-r/pragmata.md)
- [`GAME-0249` — Resident Evil 4 (2023 remake)](../games/m-r/resident-evil-4-2023.md)
- [`GAME-0288` — "Sekiro™: Shadows Die Twice - GOTY Edition"](../games/s-z/sekiro-shadows-die-twice.md)
- [`GAME-0303` — Sifu](../games/s-z/sifu.md)
- [`GAME-0496` — "Warhammer 40,000: Space Marine 2"](../games/s-z/warhammer-40000-space-marine-2.md)

## ACT-420

- Назва: Вибрати один посилений режим особистої спроможності під час живого керування
- Переглянуто: `2026-09-04`

### Операційне визначення

Під час безпосереднього керування гравець вибирає один доступний режим із взаємовиключної множини особистих спроможностей, замінюючи чинний режим до наступної сумісної дії руху, захисту або маскування.

### Включає

Вибір Speed, Strength, Armor або Cloak через класичне меню Nanosuit у визначеній першій місії Crysis Remastered.

### Виключає

Вибір переносної зброї; одночасне накладання кількох незалежних перемикачів; безперервний розподіл потужності між одночасними системами транспорту; придбання постійної навички; автоматично запущений пасивний ефект.

### Ігри-носії

- [`GAME-0246` — Crysis Remastered](../games/a-f/crysis-remastered.md)

## ACT-421

- Назва: Націлити й підтвердити переміщення у світі на коротку відстань
- Переглянуто: `2026-09-04`

### Операційне визначення

Під час безпосереднього керування у світі гравець націлює точку в межах обмеженої здатності переміщення й одразу переносить кероване тіло до прийнятої точки, не проходячи кожну проміжну позицію.

### Включає

Прицілювання та виконання Blink I до допустимої точки підлоги, даху чи уступу у визначеній місії Dishonored.

### Виключає

Звичайну безперервну ходьбу чи стрибок; переміщення вибраної фігури на полі; перенесення керування в інше тіло; телепортацію до контрольної точки; перехід у сцені без попереднього показу.

### Ігри-носії

- [`GAME-0247` — Dishonored (2012)](../games/a-f/dishonored-2012.md)
- [`GAME-0735` — "Toki Tori"](../games/s-z/toki-tori.md)

## ACT-422

- Назва: Одягнути здобуте вбрання з рольовою ознакою під час проникнення
- Переглянуто: `2026-09-04`

### Операційне визначення

Після нейтралізації одного допустимого учасника світу гравець забирає та вдягає його доступне вбрання, щоб замінити поточну представлену соціальну роль керованого учасника під час того самого активного проникнення.

### Включає

Забрати й одягнути одне сумісне маскування у визначеній сюжетній місії Paris у HITMAN World of Assassination.

### Виключає

Вибір косметичного гардероба; вибір бойового класу під час появи; спорядження обладунку лише заради характеристик; вселення в іншого учасника; зміну постійної ідентичності поза поточною місією.

### Ігри-носії

- [`GAME-0248` — HITMAN World of Assassination](../games/g-l/hitman-world-of-assassination.md)

## ACT-423

- Назва: Викликати місцевий огляд ситуації поверх зображення під час керування у грі
- Переглянуто: `2026-09-04`

### Операційне визначення

Під час безпосереднього керування втіленим учасником гравець утримує одну команду огляду, щоб замінити звичайний вигляд обмеженим накладеним показом станів учасників, цілей та інтерактивних об’єктів поблизу, а потім відпускає її, повертаючись до тієї самої незміненої ролі під час гри.

### Включає

Утримування Instinct для огляду цілей, учасників та інтерактивних об’єктів поблизу в дослідженій місії Paris у HITMAN World of Assassination.

### Виключає

Нанесення постійної позначки на учасника через оптичний пристрій; призупинення гри на повній тактичній мапі; активацію нічного бачення; звернення до зовнішнього посібника з проходження; сканування ресурсу зі збереженням відомостей про нього в інвентарі.

### Ігри-носії

- [`GAME-0248` — HITMAN World of Assassination](../games/g-l/hitman-world-of-assassination.md)
- [`GAME-0261` — The Last of Us Part I](../games/s-z/the-last-of-us-part-i.md)
- [`GAME-0250` — Tomb Raider (2013)](../games/s-z/tomb-raider-2013.md)

## ACT-424

- Назва: Пересувати й обертати предмети в обмеженій сітці інвентарю
- Переглянуто: `2026-10-05`

### Операційне визначення

В інтерфейсі інвентарю предметів при собі гравець вибирає один збережений предмет, змінює його позицію або дозволену орієнтацію й підтверджує розміщення лише там, де отриманий контур уміщується в поточних вільних клітинках.

### Включає

Пересування й обертання зброї або припасів у кейсі в межах визначеної першої глави Resident Evil 4.

### Виключає

Розкладання складників у сітці рецепта; спорядження незміненого предмета з комірки швидкого доступу; пересування об’єкта світу; сортування необмеженого списку; зміну загальних розмірів інвентарю.

### Ігри-носії

- [`GAME-0511` — Animal Crossing: New Leaf](../games/a-f/animal-crossing-new-leaf.md)
- [`GAME-0353` — "Deus Ex: Game of the Year Edition"](../games/a-f/deus-ex-game-of-the-year-edition.md)
- [`GAME-0269` — DREDGE](../games/a-f/dredge.md)
- [`GAME-0500` — Pacific Drive](../games/m-r/pacific-drive.md)
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

- [`GAME-0506` — Avowed](../games/a-f/avowed.md)
- [`GAME-0282` — Dead Cells](../games/a-f/dead-cells.md)
- [`GAME-0290` — Lies of P](../games/g-l/lies-of-p.md)
- [`GAME-0249` — Resident Evil 4 (2023 remake)](../games/m-r/resident-evil-4-2023.md)
- [`GAME-0288` — "Sekiro™: Shadows Die Twice - GOTY Edition"](../games/s-z/sekiro-shadows-die-twice.md)
- [`GAME-0496` — "Warhammer 40,000: Space Marine 2"](../games/s-z/warhammer-40000-space-marine-2.md)

## ACT-427

- Назва: Прокручувати фіксовану реконструкцію події до причинного моменту
- Переглянуто: `2026-10-13`

### Операційне визначення

У заданій автором реконструкції вже сталої минулої події гравець переміщує часовий вказівник у межах її скінченного інтервалу й підтверджує огляд у допустимий причинний момент, щоб зареєструвати пов’язаний доказ, не змінюючи представлену подію чи історію живого світу.

### Включає

Прокручування реконструкції тіла або місця події у вступному інциденті Detroit: Become Human для знаходження траєкторії зброї, послідовності нападу чи іншого авторського причинного моменту.

### Виключає

Повернення стану живої симуляції назад; редагування команд на часових позначках; відтворення аудіовізуального доказу без причинного моменту, який можна оглянути; вільне вигадування минулого; вибір однієї деталі застиглої сцени.

### Ігри-носії

- [`GAME-0252` — "Detroit: Become Human"](../games/a-f/detroit-become-human.md)

## ACT-428

- Назва: Увійти до пов’язаної союзної бойової платформи для безпосереднього керування
- Переглянуто: `2026-09-05`

### Операційне визначення

Піший оператор входить до однієї досяжної відновленої союзної бойової платформи й підтверджує заміну особистих команд руху, атаки та здібностей безпосереднім керуванням цією платформою, продовжуючи перебувати в ній.

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
- [`GAME-0662` — "Batman: Arkham Shadow"](../games/a-f/batman-arkham-shadow.md)
- [`GAME-0299` — Nioh 2](../games/m-r/nioh-2.md)
- [`GAME-0691` — "REPLACED"](../games/m-r/replaced.md)

## ACT-430

- Назва: Переміститися гаком до допустимої висотної точки
- Переглянуто: `2026-09-05`

### Операційне визначення

Під час безпосереднього керування тілом гравець обирає одну наразі допустиму висотну точку світу й підтверджує переміщення гаком від поточної позиції до неї.

### Включає

Переміщення гаком до позначеного верхнього виступу чи спостережної точки в приміщенні з озброєними ворогами в обмеженому вступному маршруті Story Mode гри Batman: Arkham Asylum Game of the Year Edition.

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

Під час безпосереднього керування тілом гравець піднімає один узятий із собою датчик руху малого радіуса дії для перегляду його активних показань або знову опускає його, зберігаючи звичайну можливість пересування.

### Включає

Піднімання й опускання детектора руху у визначеній лікарняній місії Alien: Isolation.

### Виключає

Встановлення датчика, що залишається у світі; позначення одного видимого учасника; відкриття всезнаючої мапи; сканування нерухомого ресурсу чи доказу; саме лише слухання пасивного попередження про близькість, для якого не потрібна команда датчика.

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
- [`GAME-0531` — The Midnight Walk](../games/s-z/the-midnight-walk.md)

## ACT-434

- Назва: Переорієнтовувати лінійний рисунок пострілу готового інструмента
- Переглянуто: `2026-09-05`

### Операційне визначення

Поки один сумісний інструмент лишається готовим, гравець повертає або перемикає його видовжений рисунок пострілу між визначеними просторовими орієнтаціями перед наступним прицільним пострілом.

### Включає

Зміна орієнтації лінії з трьох променів Plasma Cutter між горизонтальною та вертикальною під час дослідженого вступного розділу Dead Space (2023).

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

- Назва: Виконати один ухильний перекат за витрату запасу зусиль
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

- Назва: Утримувати й відпускати захист за поворотом персонажа без окремого наведення
- Переглянуто: `2026-09-06`

### Операційне визначення

Під час бою в реальному часі гравець піднімає й утримує споряджений захисний предмет у напрямку, куди повернений персонаж, щоб допустимі вхідні атаки послаблювалися або поглиналися, а не повністю завдавали шкоди здоров’ю, і відпускає його, щоб повернутися до звичайних дій. Сама команда захисту не визначає, чи потребує це поглинання витрат і за яким правилом вони нараховуються.

### Включає

Утримування щита проти атак Grave Warden і стража в межах дослідженого маршруту Cemetery of Ash у DARK SOULS III; утримування Guardian Shield у межах дослідженого початкового маршруту God of War.

### Виключає

Наведення захисту в одному вибраному напрямку вхідної атаки; захист стоячи або навприсядки відносно суперника у бійцівській грі, який задається напрямком руху; тривалий захист зброєю, вичерпання власної окремої шкали якого залишає захисника вразливим; вікно парирування або відбиття, що потребує вчасної дії; тимчасовий запас поглинання шкоди, який застосовується до втрати здоров’я; постійне зменшення шкоди обладунком, що не потребує утримання команди.

### Ігри-носії

- [`GAME-0347` — "Castlevania: Symphony of the Night"](../games/a-f/castlevania-symphony-of-the-night.md)
- [`GAME-0262` — DARK SOULS™ III](../games/a-f/dark-souls-iii.md)
- [`GAME-0295` — DARK SOULS™: REMASTERED](../games/a-f/dark-souls-remastered.md)
- [`GAME-0282` — Dead Cells](../games/a-f/dead-cells.md)
- [`GAME-0327` — Fable](../games/a-f/fable.md)
- [`GAME-0550` — Ghost of Yōtei](../games/g-l/ghost-of-yotei.md)
- [`GAME-0263` — God of War](../games/g-l/god-of-war.md)
- [`GAME-0290` — Lies of P](../games/g-l/lies-of-p.md)
- [`GAME-0341` — "Ninja Gaiden Black"](../games/m-r/ninja-gaiden-black.md)
- [`GAME-0625` — "Ninja Gaiden Dragon Sword"](../games/m-r/ninja-gaiden-dragon-sword.md)
- [`GAME-0299` — Nioh 2](../games/m-r/nioh-2.md)
- [`GAME-0344` — "Prince of Persia: The Sands of Time"](../games/m-r/prince-of-persia-the-sands-of-time.md)
- [`GAME-0458` — The Legend of Zelda: Link's Awakening](../games/s-z/the-legend-of-zelda-links-awakening.md)
- [`GAME-0363` — "The Legend of Zelda: Ocarina of Time"](../games/s-z/the-legend-of-zelda-ocarina-of-time.md)

## ACT-438

- Назва: Прив’язати огляд і напрямок атак до однієї вибраної ворожої цілі
- Переглянуто: `2026-09-05`

### Операційне визначення

Гравець обирає одну наразі допустиму ворожу ціль поблизу й прив’язує до неї камеру та напрямок атак персонажа, тож подальший рух стає відносним до цього учасника, доки гравець не зніме прив’язку або ціль не втратить допустимість.

### Включає

Прив’язка до Grave Warden або стража маршруту під час дослідженого маршруту Cemetery of Ash гри DARK SOULS III.

### Виключає

Збережену тактичну позначку, що переживає перешкоди чи сутичку; автоматичну допомогу з наведенням, яку гравець не обирає; вибір абстрактної картки чи пункту меню; наказ іншому актору атакувати ціль.

### Ігри-носії

- [`GAME-0308` — Bloodborne™](../games/a-f/bloodborne.md)
- [`GAME-0262` — DARK SOULS™ III](../games/a-f/dark-souls-iii.md)
- [`GAME-0295` — DARK SOULS™: REMASTERED](../games/a-f/dark-souls-remastered.md)
- [`GAME-0327` — Fable](../games/a-f/fable.md)
- [`GAME-0290` — Lies of P](../games/g-l/lies-of-p.md)
- [`GAME-0299` — Nioh 2](../games/m-r/nioh-2.md)
- [`GAME-0670` — "Phantom Dust"](../games/m-r/phantom-dust.md)
- [`GAME-0561` — Psychonauts 2](../games/m-r/psychonauts-2.md)
- [`GAME-0288` — "Sekiro™: Shadows Die Twice - GOTY Edition"](../games/s-z/sekiro-shadows-die-twice.md)
- [`GAME-0502` — South of Midnight](../games/s-z/south-of-midnight.md)

## ACT-440

- Назва: Підтвердити одну перевірку характеристики з показаними шансами для запропонованого варіанта
- Переглянуто: `2026-09-05`

### Операційне визначення

Гравець вибирає один наразі запропонований варіант із перевіркою характеристики, читає показані шанси на успіх та модифікатори, що на них впливають, і підтверджує його, знаючи, що результат визначить випадковий розрахунок, а не виконання команди.

### Включає

Підтвердження активної білої або червоної перевірки у варіанті діалогу або взаємодії з об’єктом під час дослідженого початкового епізоду Disco Elysium - The Final Cut.

### Виключає

Звичайну авторську відповідь із наперед визначеним наслідком; вчасне натискання, успіх якого залежить від миті; здібність, обмежену лише ресурсом чи часом відновлення; приховану перевірку, яку гравець не обирає.

### Ігри-носії

- [`GAME-0264` — Disco Elysium - The Final Cut](../games/a-f/disco-elysium-the-final-cut.md)

## ACT-441

- Назва: Розмістити платного постійного захисника, щоб охопити фіксований маршрут ворогів
- Переглянуто: `2026-09-06`

### Операційне визначення

Гравець вибирає один тип із платного каталогу й ставить його на обрану допустиму позицію на мапі, де маршрут ворогів незмінний і відомий заздалегідь, тож обрана позиція визначає, яку ділянку цього маршруту новий постійний захисник зможе опрацьовувати до кінця спроби.

### Включає

Розміщення купленої мавпи на суходолі початкової мапи в дослідженому легкому стандартному маршруті Bloons TD 6.

### Виключає

Розміщення споруди, чия позиція змінює покриття міських послуг; розміщення чи поворот об’єкта в робочому виробничому плануванні; купівлю активу без вибору позиції у світі; висадку загону, який потім рухається або отримує прямі накази.

### Ігри-носії

- [`GAME-0265` — Bloons TD 6](../games/a-f/bloons-td-6.md)
- [`GAME-0407` — Plants vs. Zombies](../games/m-r/plants-vs-zombies.md)

## ACT-442

- Назва: Задати поставленому захисникові правило вибору цілі
- Переглянуто: `2026-09-06`

### Операційне визначення

Для одного вже поставленого автономного захисника гравець вибирає серед оголошених правил те, яке вирішуватиме, кого з допустимих ворогів у межах досяжності він атакуватиме наступним, змінюючи майбутні автоматичні вибори цього захисника й не наказуючи жодної окремої сутички.

### Включає

Перемикання поставленої мавпи між оголошеними пріоритетами цілі «перший», «останній», «найближчий» і «найсильніший» під час дослідженого стандартного маршруту режиму Easy у Bloons TD 6.

### Виключає

Призначення шикування та бойової постави загону під прямим керуванням; вибір здібності та її цілі; наведення удару; поставу, що змінює, рухається актор чи тримає позицію.

### Ігри-носії

- [`GAME-0265` — Bloons TD 6](../games/a-f/bloons-td-6.md)

## ACT-443

- Назва: Прорізати досяжний об’єм місцевості й забрати вміщений у ньому видобуток
- Переглянуто: `2026-09-06`

### Операційне визначення

Гравець наводить різальний інструмент на досяжний твердий матеріал місцевості й усуває певний суцільний об’єм цього матеріалу, назавжди перетворюючи цей об’єм на прохідний простір. Якщо в усунутому об’ємі містилося родовище, та сама дія переносить його визначений матеріал до інвентарю при собі.

### Включає

Удари спільним кайлом або моторизованими свердлами класу Driller крізь печерну породу й родовища мінералів під час дослідженої одиночної місії Mining Expedition у Deep Rock Galactic.

### Виключає

Руйнування однієї окремої комірки, блока чи стіни світу; усунення обмеженого об’єму ґрунту лише для створення виїмки для стрільби або краю укриття; утримування команди видобутку на окремому ресурсному об’єкті, який не є рельєфом; збирання з польового джерела чи переможеного тіла; руйнування матеріалу місцевості винятково заради появи окремої здобичі.

### Ігри-носії

- [`GAME-0694` — "A Game About Digging A Hole"](../games/a-f/a-game-about-digging-a-hole.md)
- [`GAME-0266` — Deep Rock Galactic](../games/a-f/deep-rock-galactic.md)

## ACT-444

- Назва: Розподілити частини по впорядкованому списку запусків і просувати його
- Переглянуто: `2026-09-06`

### Операційне визначення

Під час складання гравець розподіляє частини побудованого апарата по впорядкованому списку кроків запуску й може вільно міняти порядок цього списку; під час роботи одна повторювана команда просуває список рівно на один крок, безповоротно запалюючи або відділяючи кожну частину цього кроку.

### Включає

Укладання списку запусків у складальному ангарі та його просування по одному кроку в польоті під час дослідженого орбітального завдання режиму Sandbox гри Kerbal Space Program.

### Виключає

Розміщення чи орієнтування складника; редагування місцевого правила роботи окремого об’єкта або просторового поля команд; вибір однієї здібності та її цілі; час відновлення, що повертає використану дію; активацію, яку система виконує за власним розкладом.

### Ігри-носії

- [`GAME-0267` — Kerbal Space Program](../games/g-l/kerbal-space-program.md)

## ACT-445

- Назва: Вести керовану фішку всередині обмеженого поля, уникаючи фігур, що надходять у нього
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

- Назва: Спрямувати інструмент безперервної подачі на досяжну поверхню
- Переглянуто: `2026-09-08`

### Операційне визначення

Гравець наводить утримуваний у руках інструмент безперервної подачі на досяжну поверхню й утримує або перемикає подачу на неї. Ефектом дії є площа, яку струмінь покриває з часом, а не окремий підтверджений удар.

### Включає

Ведення мийного струменя по панелях автомобіля в дослідженому першому завданні кар’єри PowerWash Simulator.

### Виключає

Прицільний постріл або удар по ворогові; вилучення скінченної здобичі з джерела; окрему дію догляду за одним власним предметом; встановлення постійного об’єкта; знаряддя, дія якого спрацьовує на відпусканні, а не під час дотику.

### Ігри-носії

- [`GAME-0296` — Noita](../games/m-r/noita.md)
- [`GAME-0534` — PowerWash Simulator 2](../games/m-r/powerwash-simulator-2.md)
- [`GAME-0279` — PowerWash Simulator](../games/m-r/powerwash-simulator.md)
- [`GAME-0412` — Splatoon 3](../games/s-z/splatoon-3.md)
- [`GAME-0568` — Teardown](../games/s-z/teardown.md)

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

Після смертельної шкоди, але до настання остаточної смерті, гравець підтверджує витрату одного наразі готового заряду самовідновлення, щоб відновити кероване тіло на місці й продовжити ту саму поточну сутичку.

### Включає

Вибір Resurrection після смертельної поразки в обмеженому початковому маршруті Sekiro.

### Виключає

Оживлення іншого учасника; автоматичне застосування додаткового життя; повернення до контрольної точки; повторну появу в новому тілі; пасивне виживання, для якого не потрібна команда після поразки.

### Ігри-носії

- [`GAME-0288` — "Sekiro™: Shadows Die Twice - GOTY Edition"](../games/s-z/sekiro-shadows-die-twice.md)

## ACT-453

- Назва: Витратити одну одиницю зі скінченного запасу при собі на поповнення переносного пристрою
- Переглянуто: `2026-09-10`

### Операційне визначення

Поки заряд одного сумісного переносного пристрою нижчий за його робочу верхню межу, гравець наказує безповоротно перенести до цього пристрою одну змінну одиницю зі скінченного запасу при собі, не вибираючи іншого спорядженого інструмента.

### Включає

Ручне витрачання однієї батарейки, яку гравець має при собі, на поповнення переносного ліхтарика під час дослідженої лікарняної місії Alien: Isolation.

### Виключає

Перемикання пристрою (ACT-409); автоматичне відновлення заряду в неактивному стані; перезарядження магазинної зброї (ACT-183); заміну дихального фільтра (ACT-435); підбирання змінної одиниці; виготовлення чи спорядження іншого пристрою.

### Ігри-носії

- [`GAME-0427` — Alan Wake](../games/a-f/alan-wake.md)
- [`GAME-0257` — "Alien: Isolation"](../games/a-f/alien-isolation.md)
- [`GAME-0456` — Alone in the Dark](../games/a-f/alone-in-the-dark.md)

## ACT-454

- Назва: Живитися кров’ю однієї ослабленої цілі, утримуючи команду
- Переглянуто: `2026-09-13`

### Операційне визначення

Гравець звертається до однієї досяжної ослабленої живої цілі й утримує контекстну команду живлення до завершення процесу або застосовує дозволений укус для раннього завершення, щоб забрати кров цієї цілі.

### Включає

Feed і завершальний Bite по придатній людині чи істоті на початку V Rising.

### Виключає

Звичайну шкоду від ударів зблизька чи заклять; пиття витратного предмета, який гравець має при собі; збирання Blood Essence з переможеної цілі; автоматичний ефект викрадення здоров’я; взаємодію з мертвим тілом.

### Ігри-носії

- [`GAME-0294` — V Rising](../games/s-z/v-rising.md)

## ACT-455

- Назва: Редагувати збережуваний граф пішохідних і службових стежок
- Переглянуто: `2026-09-18`

### Операційне визначення

Гравець прокладає, подовжує або прибирає з'єднані ділянки пішохідних стежок; їхня розгалужена мережа визначає, куди можуть самостійно дістатися відвідувачі та працівники.

### Включає

З'єднання воріт вольєра страусів з наявною стежкою в Goodwin House гри Planet Zoo: Console Edition.

### Виключає

Мережу автомобільних доріг (ACT-068); один фіксований нерозгалужений маршрут головоломки; декоративне фарбування землі; безпосереднє керування відвідувачем або доглядачем.

### Ігри-носії

- [`GAME-0298` — 'Planet Zoo: Console Edition'](../games/m-r/planet-zoo-console-edition.md)
- [`GAME-0335` — RollerCoaster Tycoon Deluxe](../games/m-r/rollercoaster-tycoon-deluxe.md)

## ACT-456

- Назва: Побудувати замкнену огорожу вольєра та його ворота
- Переглянуто: `2026-09-18`

### Операційне визначення

Гравець розміщує або змінює суміжні секції огорожі й одні службові ворота, утворюючи вольєр для тварин, на який можна окремо спрямовувати дії. Його межа та вхід залишаються частиною поточного стану зоопарку.

### Включає

Завершення замкненого контуру вольєра Common Ostrich, воріт і скляної оглядової секції у Goodwin House.

### Виключає

Звичайну стіну кімнати без функції утримання тварин; з’єднання стежки поза вольєром (ACT-455); автоматичне визначення допустимості (CON-635); розміщення об’єктів для годування чи огляду (ACT-457).

### Ігри-носії

- [`GAME-0298` — 'Planet Zoo: Console Edition'](../games/m-r/planet-zoo-console-edition.md)

## ACT-457

- Назва: Розмістити окремий об’єкт для догляду за тваринами чи огляду
- Переглянуто: `2026-09-18`

### Операційне визначення

Гравець розміщує вибраний окремий об’єкт у допустимому місці зоопарку, надаючи поточному вольєру або прилеглій оглядовій ділянці його визначену функцію догляду чи можливість для відвідувачів.

### Включає

Станції годування й напування, ігрові або харчові засоби збагачення середовища та скринька для пожертв біля оглядової секції страусів у Goodwin House.

### Виключає

Прокладання огорожі вольєра (ACT-456); редагування ділянок стежки (ACT-455); звичайну власну виробничу споруду (ACT-139); фактичне годування тварини доглядачем.

### Ігри-носії

- [`GAME-0298` — 'Planet Zoo: Console Edition'](../games/m-r/planet-zoo-console-edition.md)

## ACT-458

- Назва: Призначити тварині зі сховища обраний придатний вольєр
- Переглянуто: `2026-09-18`

### Операційне визначення

Гравець вибирає тварину, що вже перебуває у сховищі зоопарку, і наказує перевезти її до одного обраного придатного вольєра, залишаючи переміщення й доставлення доступним працівникам.

### Включає

Призначення прийнятих у зоопарк бородавочників і страусів із Trade Centre до відповідних вольєрів Goodwin House.

### Виключає

Купівлю тварини (ACT-130); безпосереднє перенесення її зоопарком; автономне доставлення працівниками (SYS-866); призначення непридатного вольєра так, ніби наказ уже було успішно виконано.

### Ігри-носії

- [`GAME-0298` — 'Planet Zoo: Console Edition'](../games/m-r/planet-zoo-console-edition.md)

## ACT-459

- Назва: Обирати бойову стійку зі зброєю
- Переглянуто: `2026-09-18`

### Операційне визначення

Під час безпосереднього керування боєм гравець перемикає споряджену ближню зброю між передбаченими стійками, одразу обираючи інший набір швидкості, досяжності й тривалості наступних ударів.

### Включає

Вибір високої, середньої чи низької стійки для спорядженої зброї під час дослідженої першої місії Nioh 2 для PS4.

### Виключає

Зміну самої зброї; призначення бойового шикування автономним підрозділам; одноразове парирування; стійку, вибрану лише перед боєм.

### Ігри-носії

- [`GAME-0308` — Bloodborne™](../games/a-f/bloodborne.md)
- [`GAME-0641` — "Bushido Blade"](../games/a-f/bushido-blade.md)
- [`GAME-0299` — Nioh 2](../games/m-r/nioh-2.md)
- [`GAME-0455` — Soulcalibur](../games/s-z/soulcalibur.md)

## ACT-460

- Назва: Виконати імпульс відновлення запасу після атаки у часовому вікні
- Переглянуто: `2026-09-18`

### Операційне визначення

Після придатного удару гравець виконує імпульс у короткому видимому проміжку відновлення, повертаючи доступну частину щойно витраченого запасу сили та застосовуючи передбачене локальне очищення.

### Включає

Вчасний Ki Pulse після удару зброєю з очищенням ділянки світу йокаїв, якщо гравець достатньо близько, у першій місії Nioh 2.

### Виключає

Пасивне відновлення з часом; поповнення витратним предметом; виконання імпульсу до будь-якої атаки, що відповідає умовам; захист щитом або Burst Counter.

### Ігри-носії

- [`GAME-0299` — Nioh 2](../games/m-r/nioh-2.md)

## ACT-461

- Назва: Подати готову страву, яку гравець несе, через вікно видачі
- Переглянуто: `2026-09-18`

### Операційне визначення

Гравець переносить готову страву на тарілці до спільного вікна видачі й підтверджує її передавання для звірення з поточною чергою замовлень; після цього страва більше не перебуває в руках кухаря.

### Включає

Подача тарілки із сашимі з нарізаної риби або креветки через вікно видачі першої сюжетної кухні Story у Overcooked! 2.

### Виключає

Передавання вибраного предмета конкретному неігровому персонажеві (ACT-091); саме викладання їжі на тарілку; автоматичне виконання замовлення без подання страви, яку кухар переносив; подання непідготовленого складника.

### Ігри-носії

- [`GAME-0300` — Overcooked! 2](../games/m-r/overcooked-2.md)

## ACT-462

- Назва: Націлити й виконати прийом по вразливій точці з витратою заряду
- Переглянуто: `2026-09-18`

### Операційне визначення

Коли бойовий заряд готовий, гравець у сповільненому виборі вказує вразливу точку доступного супротивника й підтверджує особливий ближній прийом, який витрачає заряд.

### Включає

Вибір цілі Focus у Sifu та витрату заряду Focus у межах першого сховку на складності Disciple.

### Виключає

Звичайні удари ближнього бою; автоматичну зміну цілі; властивий конкретній зброї Focus Strike у Monster Hunter Wilds (ACT-246); здібність, обмежену лише часом відновлення; прийом без окремого проміжку прицільного вибору.

### Ігри-носії

- [`GAME-0303` — Sifu](../games/s-z/sifu.md)

## ACT-463

- Назва: Підтвердити продовження за допомогою талісмана після смертельної поразки
- Переглянуто: `2026-09-18`

### Операційне визначення

У проміжку вибору після поразки гравець підтверджує негайне продовження за допомогою придатного талісмана, що відновлює життя, замість того щоб дозволити поточній спробі завершитися.

### Включає

Підняття після смерті в першому Hideout на складності Disciple у Sifu, коли талісман ще може відновити бійця.

### Виключає

Автоматичну повторну появу на контрольній точці; відродження Resurrection з готовим зарядом у Sekiro (ACT-452); оживлення гравця товаришем по команді; вибір навички на тому самому екрані смерті; автоматичне збільшення віку після підтвердження.

### Ігри-носії

- [`GAME-0303` — Sifu](../games/s-z/sifu.md)

## ACT-464

- Назва: Взяти всі плитки одного кольору з однієї відкритої пропозиції
- Переглянуто: `2026-09-18`

### Операційне визначення

У свій хід гравець обирає одне видиме джерело та колір і мусить забрати з нього всі плитки цього кольору, а не довільну кількість.

### Включає

Вибір однієї з п’яти майстерень або спільного центру в оригінальній базовій грі Azul на двох.

### Виключає

Витягування невидимої плитки з мішка; забирання різних кольорів за один вибір; залишення плиток вибраного кольору; призначення партії підготовчому рядку (ACT-465).

### Ігри-носії

- [`GAME-0304` — Azul](../games/a-f/azul.md)

## ACT-465

- Назва: Призначити набрану партію одного кольору одному підготовчому рядку
- Переглянуто: `2026-09-18`

### Операційне визначення

Після набору гравець обирає один придатний підготовчий рядок для всіх прийнятих плиток цього кольору; відхилені та зайві плитки йдуть на штрафну лінію, а не розподіляються між рядками.

### Включає

Розміщення партії справа наліво в одному підготовчому рядку Azul або вибір відправити її на штрафну лінію.

### Виключає

Вибір відкритої пропозиції (ACT-464); автоматичне перенесення заповненого рядка на стіну (SYS-881); заповнення двох рядків однією набраною партією.

### Ігри-носії

- [`GAME-0304` — Azul](../games/a-f/azul.md)

## ACT-466

- Назва: Перенести живу ціль місії до евакуаційного транспорту
- Переглянуто: `2026-09-18`

### Операційне визначення

Гравець піднімає одну допустиму живу ціль місії, що втратила здатність діяти, фізично переносить її світом в окремому стані перенесення й розміщує в сумісному евакуаційному транспорті, перш ніж відбуття самого гравця зможе завершити порятунок.

### Включає

Винести пораненого Казухіру Міллера з Da Ghwandai Khar і посадити його в другий вертоліт під час першої спроби Phantom Limbs у METAL GEAR SOLID V: THE PHANTOM PAIN.

### Виключає

Приховування тіла знешкодженого противника; наказ автономним носіям доставити ціль; застосування Fulton; перенесення або кидання сумки зі здобиччю; посадку самого гравця до гелікоптера після завантаження цілі.

### Ігри-носії

- [`GAME-0306` — METAL GEAR SOLID V: THE PHANTOM PAIN](../games/m-r/metal-gear-solid-v-the-phantom-pain.md)

## ACT-467

- Назва: Всмоктувати або вистрілювати один досяжний об’єкт через активний бак
- Переглянуто: `2026-09-19`

### Операційне визначення

Гравець націлює переносний всмоктувальний інструмент і або втягує один досяжний сумісний незакріплений об’єкт з ігрового світу до вибраного бака відповідного типу, або випускає запасені одиниці з цього бака назад у ділянку світу чи приймальний пристрій, на які націлено інструмент.

### Включає

Всмоктувати Pink Slime, їжу та Pink Plort у вибраний бак Vacpack, а потім запускати слаймів чи їжу в стартовий загін і plort’и в Plort Market у новому збереженні Adventure.

### Виключає

Контактне підбирання без прицільного всмоктування; спорядження бака (ACT-164); продаж випущеного plort’а (ACT-219); автоматичне поїдання їжі або створення plort’а; притягування закріпленого об’єкта середовища.

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

Витрачання запасу прискорення, який можна зберігати після маневру; оцінювання тривалості дрифту; допоміжне кермування з окремою підказкою дрифту; звичайний розворот ручним гальмом без результату накопичення заряду та відпускання.

### Ігри-носії

- [`GAME-0309` — "Mario Kart 8 Deluxe"](../games/m-r/mario-kart-8-deluxe.md)
- [`GAME-0621` — "Sonic Racing: CrossWorlds"](../games/s-z/sonic-racing-crossworlds.md)

## ACT-469

- Назва: Перерозподілити стос вантажу, який персонаж несе на тілі
- Переглянуто: `2026-09-19`

### Операційне визначення

Гравець переміщує пакунки, які має при собі, між сумісними місцями на тілі, костюмі чи наплічнику або запускає автоматичне впорядкування, щоб змінити поточний розподіл вантажу без зміни ідентичності пакунків для їх доставлення.

### Включає

Ручне й автоматичне впорядкування вантажу в першому замовленні DEATH STRANDING DIRECTOR'S CUT.

### Виключає

Підбирання вантажу зі світу (ACT-199); зберігання вантажу в транспорті; скидання всього вантажу; косметичне налаштування наплічника.

### Ігри-носії

- [`GAME-0310` — "DEATH STRANDING DIRECTOR’S CUT"](../games/a-f/death-stranding-directors-cut.md)

## ACT-470

- Назва: Стабілізувати один бік вантажу, що зміщується під час перенесення
- Переглянуто: `2026-09-19`

### Операційне визначення

Під час руху з вантажем на тілі гравець утримує ліве, праве або обидва визначені захоплення, щоб протидіяти поточному боковому зміщенню й стабілізувати носія до розв’язання рівноваги.

### Включає

Стабілізацію одного або двох боків у першій доставці DEATH STRANDING DIRECTOR'S CUT.

### Виключає

Пасивну стійкість спорядження; блокування бойової атаки; керування транспортом; автоматичне коригування вантажу без команди гравця.

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

Імпульс обстеження лише ресурсів; постійне відкриття всієї мапи; автоматичне виявлення ворогів; обчислення маршруту.

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

Одну позначку місця призначення з автоматично розрахованим дорожнім маршрутом; малювання рельєфу; задавання проміжних точок маршруту автономній одиниці.

### Ігри-носії

- [`GAME-0310` — "DEATH STRANDING DIRECTOR’S CUT"](../games/a-f/death-stranding-directors-cut.md)

## ACT-473

- Назва: Надувати кероване тіло для вертикального підйому
- Переглянуто: `2026-09-19`

### Операційне визначення

Поки доступна оголошена тимчасова здатність до надування, гравець утримує її окрему команду, щоб збільшити безпосередньо кероване тіло й спрямувати плавучий підйом до досяжного простору в повітрі або водному маршруті.

### Включає

Утримування команди Inflate у Sky Garden гри ASTRO BOT, щоб підніматися до фрагмента пазла біля фламінго, платформ вежі й верхнього маршруту водною трубою.

### Виключає

Звичайний стрибок або скінченне лазерне зависання; пасивну плавучість повітряної кулі; плавання без тимчасової форми; вибір далекої цілі для автоматичного польоту.

### Ігри-носії

- [`GAME-0312` — ASTRO BOT](../games/a-f/astro-bot.md)

## ACT-474

- Назва: Керувати одним досяжним постом судна
- Переглянуто: `2026-09-20`

### Операційне визначення

Гравець фізично дістається одного поста керування судном і змінює налаштування цього поста, що зберігається, тоді як решта постів і саме судно продовжують перебувати у своєму поточному стані під час гри.

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

Усунення матеріалу місцевості для створення тактичного укриття; видобування з видимого ресурсного вузла; відкривання вже оголеного контейнера; вибір позначки мапи, який автоматично виконує розкопування.

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

Безпосереднє хапання вільно плаваючої істоти; одна автоматична команда риболовлі; мінігра на влучність у часі, яка починається лише після того, як риба вже опинилася на гачку; ловля комахи сачком.

### Ігри-носії

- [`GAME-0320` — "Animal Crossing: New Horizons"](../games/a-f/animal-crossing-new-horizons.md)
- [`GAME-0511` — Animal Crossing: New Leaf](../games/a-f/animal-crossing-new-leaf.md)

## ACT-477

- Назва: Змахнути сачком у руках крізь одну досяжну істоту
- Переглянуто: `2026-09-26`

### Операційне визначення

Гравець розташовує безпосередньо керованого персонажа й виконує один короткий змах сачком у руках крізь обраний досяжний об’єм світу, перевіряючи дотик до наявної зараз істоти.

### Включає

Наближення й змах хистким сачком по видимій комасі протягом першого повного дня на острові в Animal Crossing: New Horizons; проведення Time Net крізь досяжну мавпу під час першого відвідування Fossil Field в Ape Escape.

### Виключає

Закидання вудки; встановлення автономної пастки; безпосереднє ловлення рукою; атаку на ворожу істоту заради здобичі; автоматичне збирання від дотику.

### Ігри-носії

- [`GAME-0320` — "Animal Crossing: New Horizons"](../games/a-f/animal-crossing-new-horizons.md)
- [`GAME-0413` — Ape Escape](../games/a-f/ape-escape.md)

## ACT-478

- Назва: Виконати друге натискання активного перезарядження
- Переглянуто: `2026-09-20`

### Операційне визначення

Після початку перезарядження магазина гравець навмисно вдруге натискає кнопку перезарядження в обраний момент, доки активний заданий авторами часовий індикатор. Він просить систему оцінити це втручання, а не погоджується на звичайну тривалість перезарядження.

### Включає

Друге натискання правого бампера під час активного перезарядження в дослідженому навчальному маршруті Training оригінальної Gears of War для Xbox 360.

### Виключає

Початок звичайного перезарядження; вибір моменту атаки; охолодження зброї з нагріванням без перенесення запасних набоїв; пасивну характеристику швидкості перезарядження.

### Ігри-носії

- [`GAME-0321` — Gears of War](../games/g-l/gears-of-war.md)

## ACT-479

- Назва: Чергувати розгойдування на прив’язі й аеродинамічне планерування під час поточного пересування
- Переглянуто: `2026-09-20`

### Операційне визначення

Під час безпосереднього керування втіленим персонажем у безперервному тривимірному світі гравець неодноразово прикріплює лінію пересування до допустимої навколишньої геометрії або розкриває аеродинамічну поверхню, яку має при собі. Потім він керує отриманим розгойдуванням чи планеруванням, зберігаючи поточний імпульс руху між цими двома режимами пересування.

### Включає

Поєднання Пітером або Майлзом розгойдування на павутині з Web Wings під час дослідженого маршруту Surface Tension у Marvel’s Spider-Man 2.

### Виключає

Підтягування гаком до однієї вибраної кінцевої точки; сценарний кінематографічний політ; звичайні стрибки; розкриття парашута, що завершує попередній стан перебування в транспорті; телепортацію між позначками мапи.

### Ігри-носії

- [`GAME-0323` — "Marvel’s Spider-Man 2"](../games/m-r/marvels-spider-man-2.md)

## ACT-480

- Назва: Застосувати виділений рівень особистої шкали підсилень
- Переглянуто: `2026-09-20`

### Операційне визначення

Після того як зібрані підсилення просунули впорядковану шкалу одного безпосередньо керованого персонажа, гравець навмисно застосовує поточний виділений рівень і обирає його зброю або рухову можливість замість очікування пізнішого рівня.

### Включає

Натискання SELECT, коли в ряду зброї Burn, Iron, Smith або Beans виділено потрібний рівень, у дослідженій першій місії Contra Force.

### Виключає

Підбирання об’єкта, який просуває шкалу; передавання безпосереднього керування іншому героєві; активацію підсилення, що очищує поле; купівлю в меню постійного поліпшення спорядження.

### Ігри-носії

- [`GAME-0324` — Contra Force](../games/a-f/contra-force.md)

## ACT-481

- Назва: Сканувати одну доступну місцеву ціль для даних огляду
- Переглянуто: `2026-09-21`

### Операційне визначення

Коли режим обстеження пристроєм у руках активний, гравець спрямовує його на одну допустиму ціль у межах досяжності й записує один збережуваний зразок до поступу обстеження класу цієї цілі або її місцевості.

### Включає

Сканування однієї рослини, тварини або мінералу на Kreet у Starfield.

### Виключає

Утримання сканера до завершення технологічного креслення; пасивний імпульс ресурсів; вибір віддаленої планети; підбирання цілі.

### Ігри-носії

- [`GAME-0331` — Starfield](../games/s-z/starfield.md)

## ACT-482

- Назва: Обрати досяжну ціль на зоряній мапі й підтвердити подорож корабля
- Переглянуто: `2026-10-04`

### Операційне визначення

На навігаційному екрані корабля гравець обирає одну поточно досяжну систему, планету, орбіту чи місце посадки й підтверджує допустимий маршрут.

### Включає

Подорожі Frontier з Vectera до Kreet, із Kreet до Jemison і вибір посадки в New Atlantis у завданні One Small Step гри Starfield.

### Виключає

Безпосереднє керування польотом у місцевому просторі; швидке переміщення персонажа в межах одного дослідженого місця; маршрут автономного каравану; необмежену телепортацію.

### Ігри-носії

- [`GAME-0491` — Elite](../games/a-f/elite.md)
- [`GAME-0418` — 'FTL: Faster Than Light'](../games/a-f/ftl-faster-than-light.md)
- [`GAME-0331` — Starfield](../games/s-z/starfield.md)

## ACT-483

- Назва: Ділити, об'єднувати або передавати одновидовий загін істот
- Переглянуто: `2026-09-21`

### Операційне визначення

Переміщувати вибрану кількість одного виду істот між допустимими комірками армії героя чи гарнізону міста, ділячи загін, об'єднуючи сумісні загони або передаючи його повністю без зміни виду.

### Включає

Перебудову армії Christian із сімома комірками та гарнізону Caryatid під час Homecoming у Heroes of Might and Magic III: Complete.

### Виключає

Найм нових істот; переміщення героя на мапі пригод; передавання предметів інвентарю; об’єднання різних типів істот в один загін.

### Ігри-носії

- [`GAME-0332` — "Heroes of Might and Magic III: Complete"](../games/g-l/heroes-of-might-and-magic-iii-complete.md)

## ACT-484

- Назва: Підтвердити одну допустиму дію активного загону в бою
- Переглянуто: `2026-09-21`

### Операційне визначення

Під час бойового ходу поточного активного загону гравець підтверджує одну допустиму команду: переміститися на досяжний гекс, атакувати в ближньому або дальньому бою, зачекати чи захищатися.

### Включає

Ручне керування загоном у межах дослідженого бою Homecoming у Heroes of Might and Magic III: Complete.

### Виключає

Переміщення героя кампанії; віддавання наказу бойовому шикуванню в реальному часі; вибір закляття; автоматичну контратаку.

### Ігри-носії

- [`GAME-0332` — "Heroes of Might and Magic III: Complete"](../games/g-l/heroes-of-might-and-magic-iii-complete.md)

## ACT-485

- Назва: Редагувати платні колію й станцію атракціону власної конструкції
- Переглянуто: `2026-09-21`

### Операційне визначення

Розміщувати або прибирати типізовані сегменти колії та станції, а тоді ставити вхід і вихід атракціону, створюючи одну сталу прохідну геометрію з оплатою кожного сегмента.

### Включає

Будівництво колії, станції, входу й виходу Steel Mini Roller Coaster у Forest Frontiers RollerCoaster Tycoon Deluxe.

### Виключає

Розміщення атракціону чи кіоску з фіксованим контуром розміщення (ACT-139); прокладання гостьових стежок (ACT-455); тестування, відкриття або встановлення ціни готового атракціону (ACT-486); безпосереднє керування транспортом на створеній колії.

### Ігри-носії

- [`GAME-0335` — RollerCoaster Tycoon Deluxe](../games/m-r/rollercoaster-tycoon-deluxe.md)

## ACT-486

- Назва: Налаштувати й запустити один гостьовий атракціон
- Переглянуто: `2026-09-21`

### Операційне визначення

Перемикати збудований атракціон між закритим, тестовим і відкритим станами та задавати його ціну, умову відправлення, найменший і найбільший час очікування й інтервал огляду без зміни геометрії.

### Включає

Тестування й відкриття атракціонів Forest Frontiers, установлення плати за вхід на атракціон, вибір очікування заповнення та мінімального й максимального часу очікування на станції, а також налаштування частоти оглядів механіком у RollerCoaster Tycoon Deluxe.

### Виключає

Будівництво колії (ACT-485); відкриття всього парку (ACT-487); автономну посадку або відправлення транспорту (SYS-950); безпосереднє керування транспортом.

### Ігри-носії

- [`GAME-0335` — RollerCoaster Tycoon Deluxe](../games/m-r/rollercoaster-tycoon-deluxe.md)

## ACT-487

- Назва: Задати відкритість і вхідну ціну керованого закладу
- Переглянуто: `2026-09-21`

### Операційне визначення

Гравець відкриває або закриває один керований громадський заклад і, коли правила це дозволяють, змінює ціну входу, на яку відвідувачі, що прибувають, мають погодитися перед входом.

### Включає

Відкриття Forest Frontiers і налаштування ціни входу до парку в RollerCoaster Tycoon Deluxe.

### Виключає

Тестовий або відкритий стан окремого атракціону чи його ціну (ACT-486); розміщення входу до закладу; купівлю особистого квитка як відвідувач; маркетинг.

### Ігри-носії

- [`GAME-0335` — RollerCoaster Tycoon Deluxe](../games/m-r/rollercoaster-tycoon-deluxe.md)
- [`GAME-0370` — Theme Hospital](../games/s-z/theme-hospital.md)

## ACT-488

- Назва: Найняти й обмежити автономного працівника сервісу
- Переглянуто: `2026-09-21`

### Операційне визначення

Наймати одного працівника в оголошену автономну сервісну роль, розміщувати його на досяжній керованій території та за потреби обмежувати зону патрулювання чи дозволені класи робіт без керування кожним кроком.

### Включає

Найм, розміщення й визначення зони роботи механіка у Forest Frontiers гри RollerCoaster Tycoon Deluxe; ширші правила також підтримують різноробів, охоронців і розважальників поза мінімальним маршрутом із механіком.

### Виключає

Безпосереднє керування ходьбою працівника; призначення одного негайного місця призначення для руху; автономного працівника, наданого заздалегідь; виплату регулярної зарплати (SYS-154).

### Ігри-носії

- [`GAME-0335` — RollerCoaster Tycoon Deluxe](../games/m-r/rollercoaster-tycoon-deluxe.md)
- [`GAME-0370` — Theme Hospital](../games/s-z/theme-hospital.md)

## ACT-489

- Назва: Стукнути по сусідній поверхні, щоб створити приманку
- Переглянуто: `2026-09-21`

### Операційне визначення

Перебуваючи біля сумісної поверхні, гравець виконує окрему контекстну дію, яка не пошкоджує її, а створює локалізований звук у світі, на чиє положення можуть відреагувати придатні автономні актори поблизу.

### Включає

Стук Solid Snake по стіні чи іншій сумісній поверхні, щоб відвернути допустимого Genome Soldier під час вступного проникнення Metal Gear Solid.

### Виключає

Випадковий шум кроків або калюжі; кидання приманки; стрільбу зі зброї; удар по учаснику; руйнування чи зміну поверхні, по якій стукають.

### Ігри-носії

- [`GAME-0557` — "Boktai: The Sun Is in Your Hand"](../games/a-f/boktai-the-sun-is-in-your-hand.md)
- [`GAME-0575` — Metal Gear Acid](../games/m-r/metal-gear-acid.md)
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
- [`GAME-0475` — The House of the Dead](../games/s-z/the-house-of-the-dead.md)
- [`GAME-0443` — Time Crisis](../games/s-z/time-crisis.md)

## ACT-491

- Назва: Переносити й розміщувати одне мертве або непритомне тіло у світі
- Переглянуто: `2026-09-21`

### Операційне визначення

Гравець піднімає тіло одного допустимого мертвого або непритомного персонажа з досяжного місця у світі й переходить у стан перенесення лише цього тіла. Він рухається з тілом і відпускає його в обраному досяжному місці; тіло лишається об’єктом ігрового світу, який можна виявити, а не перетворюється на предмет інвентарю.

### Включає

Sam Fisher підіймає непритомного охоронця, переносить його в тінь і тихо кладе під час обмеженого маршруту Training Course та Police Station в оригінальній Xbox-версії Splinter Cell.

### Виключає

Підбирання предмета в інвентар; перенесення або кидання мішка зі здобиччю, яка є ціллю завдання; евакуацію живого персонажа завдання транспортним засобом; тягнення притомного персонажа, якого гравець утримує, до потрібного пристрою; автоматичний рух тіла за фізичною моделлю «ганчіркової ляльки»; остаточне вилучення переможеного персонажа з ігрового світу.

### Ігри-носії

- [`GAME-0429` — Commandos: Behind Enemy Lines](../games/a-f/commandos-behind-enemy-lines.md)
- [`GAME-0513` — Thief: The Dark Project](../games/s-z/thief-the-dark-project.md)
- [`GAME-0349` — "Tom Clancy’s Splinter Cell"](../games/s-z/tom-clancys-splinter-cell.md)

## ACT-492

- Назва: Виконати показану послідовність графіті на позначеній поверхні
- Переглянуто: `2026-09-21`

### Операційне визначення

Перебуваючи біля однієї допустимої позначеної поверхні світу, гравець починає нанесення графіті й, коли для цієї поверхні потрібна послідовність рухів, вводить показані напрямки в заданому порядку, перш ніж поточну спробу буде перервано.

### Включає

Початок нанесення графіті великого чи надвеликого розміру на обов’язковій червоній точці й відтворення команд за її значками напрямків у дослідженому вступі Jet Set Radio для Xbox 360.

### Виключає

Вибір зображення в редакторі; довільне малювання; вибір покрокової бойової команди; автоматичну заміну поверхні від дотику; системне списання фарби й зарахування завершення.

### Ігри-носії

- [`GAME-0350` — "Jet Set Radio"](../games/g-l/jet-set-radio.md)

## ACT-493

- Назва: Наказати супутнику, на якому їде гравець, взяти до рота або виплюнути одне допустиме тіло
- Переглянуто: `2026-10-13`

### Операційне визначення

Під час безпосередньої їзди на сумісному супутнику гравець наказує йому простягнути механізм поглинання до одного досяжного допустимого тіла у світі, взяти це тіло до рота й утримувати його там або виплюнути поточне утримуване тіло до автоматичного розв’язання його стану.

### Включає

Йоші простягає язик, щоб з’їсти ягоду чи придатний панцир Купи, та випльовує утримуваний панцир у межах Yoshi's Island 2 із Super Mario World.

### Виключає

Посадку на супутника, керування ним або спішування; системний ефект, що походить від типу тіла; автоматичне ковтання після спливу таймера; збирання предмета безпосередньо до інвентарю вершника; атаку супутника без команди гравця.

### Ігри-носії

- [`GAME-0354` — Super Mario World](../games/s-z/super-mario-world.md)

## ACT-494

- Назва: Утримувати ціль світу у фіксації та рухатися відносно неї
- Переглянуто: `2026-09-22`

### Операційне визначення

Гравець утримує одну придатну ціль світу поточною зафіксованою ціллю, зберігає напрям погляду на неї та задає рух або окремий ривок навколо неї, до неї чи від неї.

### Включає

Рух по орбіті та бічний ривок навколо Parasite Queen із фіксацією цілі в Combat Visor у межах визначеного прологу на Frigate Orpheon гри Metroid Prime.

### Виключає

Вільне прицілювання без утримуваної цілі; наведений снаряд після пострілу; обертання оглядової камери; вибір цілі лише в меню; автоматичний вибір цілі для атаки.

### Ігри-носії

- [`GAME-0355` — Metroid Prime](../games/m-r/metroid-prime.md)
- [`GAME-0363` — "The Legend of Zelda: Ocarina of Time"](../games/s-z/the-legend-of-zelda-ocarina-of-time.md)
- [`GAME-0496` — "Warhammer 40,000: Space Marine 2"](../games/s-z/warhammer-40000-space-marine-2.md)

## ACT-495

- Назва: Сфокусувати відбите сонячне світло для запиту напряму у світі
- Переглянуто: `2026-09-22`

### Операційне визначення

Коли перенесений відбивний інструмент перебуває під достатнім прямим світлом, гравець утримує його команду фокусування й спрямовує інструмент, доки відбиті промені не зійдуться, запитуючи напрям до поточної авторської цілі світу.

### Включає

Підняття й спрямування Ancient Sword під прямим сонячним світлом, щоб сфокусувати промінь, який указує напрям до першого колоса, у дослідженому вступі Shadow of the Colossus.

### Виключає

Постійний компас; кинутий визначник напряму; читання готової позначки на мапі; виявлення слабкого місця на тілі; звичайне прицілювання зброєю.

### Ігри-носії

- [`GAME-0356` — Shadow of the Colossus](../games/s-z/shadow-of-the-colossus.md)

## ACT-496

- Назва: Запустити один заданий авторами маневр літака або турборивок
- Переглянуто: `2026-10-15`

### Операційне визначення

Під час безпосереднього керування допустимим літаком гравець виконує один доступний запрограмований маневр зміни просторової орієнтації або обмежений турборивок, запитуючи передбачену авторами зміну орієнтації чи швидкості з поточного стану польоту під час гри.

### Включає

Запуск маневру Immelmann, «бочки» або турборивка в обмеженій першій місії The Morning After оригінальної Xbox-версії Crimson Skies: High Road to Revenge.

### Виключає

Звичайне безперервне кермування; перерозподіл потужності між підсистемами літального апарата під час гри; вивільнення прискорення, накопиченого під час дрифту; вибір місця призначення на мапі; кінематографічний маневр без команди гравця.

### Ігри-носії

- [`GAME-0623` — "Blue Lightning"](../games/a-f/blue-lightning.md)
- [`GAME-0359` — "Crimson Skies: High Road to Revenge"](../games/a-f/crimson-skies-high-road-to-revenge.md)
- [`GAME-0424` — "Star Fox 64"](../games/s-z/star-fox-64.md)

## ACT-497

- Назва: Підтвердити фіксований набір різних стартових профільних навичок
- Переглянуто: `2026-09-22`

### Операційне визначення

До початку кампанії гравець обирає й підтверджує точно оголошену кількість різних навичок із ширшого списку; кожна вибрана навичка отримує початковий профільний бонус без витрати числового запасу очок.

### Включає

Вибір Explosives, Medicine та Speech як трьох профільних навичок Fallout: New Vegas перед виходом із послідовності створення персонажа у доктора Мітчелла.

### Виключає

Розподіл числових очок характеристик (ACT-401); вибір класу; вибір необов’язкових рис; витрачання очка навички або особливої здібності на пізнішому етапі; тренування одного активного агента; тимчасовий бонус спорядження.

### Ігри-носії

- [`GAME-0361` — Fallout: New Vegas](../games/a-f/fallout-new-vegas.md)

## ACT-498

- Назва: Налаштувати місце та напрям перед кидком
- Переглянуто: `2026-09-22`

### Операційне визначення

Перед випуском кулі на доріжку гравець перемикається між керуванням бічною позицією стояння та кутом прицілювання й налаштовує заплановану лінію подачі, ще не запускаючи кулю в рух.

### Включає

Вибір місця та напряму за допомогою хрестовини й кнопки A в оригінальному боулінгу Wii Sports.

### Виключає

Прицілювання з нерухомої пускової установки (ACT-113); керування кулею після випуску; вибір напряму вільного кидка без окремого вирівнювання за доріжкою.

### Ігри-носії

- [`GAME-0364` — Wii Sports](../games/s-z/wii-sports.md)

## ACT-499

- Назва: Випустити кулю рухом руки у вибрану мить
- Переглянуто: `2026-09-22`

### Операційне визначення

Утримуючи елемент керування подачею, гравець виконує фізичний замах; відпускання цього елемента у певну мить, зафіксовану системою, запускає кулю на доріжку, а поворот зап’ястка може змінити її обертання.

### Включає

Утримування B, помах пультом Wii Remote, відпускання B поблизу нижньої точки та необов’язковий поворот зап’ястка в оригінальному боулінгу Wii Sports.

### Виключає

Клацання по нерухомій пусковій установці (ACT-113); заряджений постріл лише кнопкою; безпосереднє керування кулею після її випуску; автоматичний випуск у нижній точці жесту.

### Ігри-носії

- [`GAME-0364` — Wii Sports](../games/s-z/wii-sports.md)

## ACT-500

- Назва: Обирати скейтбордичний трюк за поточним станом і продовжувати ланцюг трюків
- Переглянуто: `2026-09-23`

### Операційне визначення

Керуючи рухомим скейтером, гравець вибирає допустиму команду трюку з напрямками відповідно до поточного стану в повітрі, на рейці чи при контакті із землею та може через мануал або прийом Revert перейти до іншого допустимого трюку, не підсумувавши спершу весь поєднаний ланцюг.

### Включає

Керування трюками з переворотом дошки, захватом і ковзанням рейкою на PlayStation, напрямленими Manual і Nose Manual, обертанням у повітрі та продовженням через Revert у стандартному наборі рухів Tony Hawk's Pro Skater 1 + 2 в Warehouse Tour.

### Виключає

Зміну постійних комірок трюків скейтера; автоматичний вибір трюку; фіксовану бойову серію атак; очки без трюку, що завершився приземленням; застосування застарілих наборів рухів Classic THPS1 або Classic THPS2.

### Ігри-носії

- [`GAME-0687` — "Denshattack!"](../games/a-f/denshattack.md)
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

Знімок возз’єднання Джеффа й Наталі на даху за оригінальними правилами режиму «72 години» Dead Rising, з перевіркою стану сцени й камери саме в момент натискання спуску, а не на початку наведення; фотографування Пікачу зі скінченного запасу кадрів під час автоматичного руху маршрутом Beach у Pokémon Snap.

### Виключає

Пасивний перегляд сцени; кінематографічні знімки екрана поза грою; розміщення камери, що змінює фізичну геометрію світу; наближення без зробленого знімка; подальше оцінювання фотографії та порівняння із записаними результатами (SYS-1001, SYS-1009).

### Ігри-носії

- [`GAME-0368` — Dead Rising](../games/a-f/dead-rising.md)
- [`GAME-0591` — Fatal Frame](../games/a-f/fatal-frame.md)
- [`GAME-0371` — Pokémon Snap](../games/m-r/pokemon-snap.md)
- [`GAME-0732` — "TOEM"](../games/s-z/toem.md)

## ACT-503

- Назва: Зайняти об’єкт щойно викладеного тайла підданим
- Переглянуто: `2026-09-23`

### Операційне визначення

Після розміщення поточного ландшафтного тайла гравець може поставити одного доступного підданого на один допустимий об’єкт цього нового тайла, призначивши його відповідній зв’язаній дорозі, місту чи монастирю, або покласти його як селянина на відповідне зв’язане поле.

### Включає

Розміщення одного міпла на щойно викладеному тайлі Carcassonne: у вертикальному положенні на дорозі, у місті чи монастирі або лежачи як селянина на полі.

### Виключає

Розміщення підданого на старішому тайлі; розміщення двох за один хід; підрахунок очок або повернення цього підданого.

### Ігри-носії

- [`GAME-0369` — Carcassonne](../games/a-f/carcassonne.md)

## ACT-504

- Назва: Спроєктувати й обладнати приміщення для надання послуг перед відкриттям
- Переглянуто: `2026-09-23`

### Операційне визначення

Гравець накреслює допустимий контур приміщення, фіксує його двері й необхідні меблі в допустимих позиціях, а потім відкриває обладнане приміщення для послуги, пов’язаної з його визначеним типом.

### Включає

Будівництво кабінету терапевта, загальної діагностики, аптеки, психіатричного кабінету або клініки лікування роздутої голови в першій лікарні Theme Hospital.

### Виключає

Лише розміщення фіксованого предмета в коридорі (ACT-139); лікування пацієнта; роботу приміщення без допустимого працівника (CON-672).

### Ігри-носії

- [`GAME-0370` — Theme Hospital](../games/s-z/theme-hospital.md)

## ACT-505

- Назва: Змінювати черги й правила діагностики пацієнтів
- Переглянуто: `2026-09-23`

### Операційне визначення

Гравець змінює збережуване правило лікарні для роботи з пацієнтами з частковим діагнозом або відпочинку персоналу чи змінює місце пацієнта в допустимій черзі або переводить його між допустимими чергами тієї самої послуги до початку наступного обслуговування.

### Включає

Обмеження черг та переведення пацієнтів між ними, пороги діагностики для команд Send Home і Guess at Cure, а також поріг відпочинку персоналу в першій лікарні Theme Hospital.

### Виключає

Безпосереднє керування кожним кроком пацієнта; переведення до несумісного приміщення; сам результат лікування (SYS-1006); створення приміщення.

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

Вибір однієї фотографії Пікачу в Camera Check та позначення її знаком професора Оука перед його оцінюванням після завершення маршруту в Pokémon Snap.

### Виключає

Саме фотографування; окрему позначку тільки для альбому; одночасне подання всіх знімків виду; результат оцінювання.

### Ігри-носії

- [`GAME-0371` — Pokémon Snap](../games/m-r/pokemon-snap.md)

## ACT-508

- Назва: Затиснути лади й ударити по струнах для заданої ноти на лінії оцінювання
- Переглянуто: `2026-09-23`

### Операційне визначення

Гравець утримує кнопки ладів, що відповідають показаній окремій ноті або одночасному акорду, а потім б’є по струнах, коли ця подія досягає лінії оцінювання; виконане введення перевіряється за відповідною подією заданої авторами карти нот.

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

Коли зароблений показник шкали підсилення сягає оголошеного мінімуму, гравець навмисно активує його під час гри за картою нот і витрачає накопичений заряд протягом тимчасового періоду посиленого нарахування очок.

### Включає

Активацію щонайменше напівзаповненого Star Power нахилом гітарного контролера Les Paul або кнопкою SELECT в одиночній пісні Guitar Hero III для PS3.

### Виключає

Саме здобуття заряду за послідовність нот; постійно активний множник; атаки на іншого гравця в режимі Battle.

### Ігри-носії

- [`GAME-0372` — "Guitar Hero III: Legends of Rock"](../games/g-l/guitar-hero-iii-legends-of-rock.md)

## ACT-510

- Назва: Покликати партнера й дістатися до нього для входу до редактора тіла під час активного етапу
- Переглянуто: `2026-09-23`

### Операційне визначення

Керуючи живим учасником активного етапу, гравець подає шлюбний поклик і дістається партнера, який відповів на нього, щоб перейти з поточного ігрового світу до редактора наступної версії цього учасника.

### Включає

Поклик на етапі клітини Spore, заплив до партнера й вхід до Cell Creator після того, як перша знайдена частина робить поклик доступним.

### Виключає

Відкриття незалежного редактора в галереї без партнера в активному етапі; автоматичне зростання без відвідування редактора; зміну частин під час плавання.

### Ігри-носії

- [`GAME-0373` — Spore](../games/s-z/spore.md)

## ACT-511

- Назва: Змінити тіло живої лінії істот розміщенням або вилученням частин
- Переглянуто: `2026-09-23`

### Операційне визначення

У редакторі, до якого переходять з активного етапу життя, гравець розміщує доступну функціональну частину на тілі керованої лінії або прибирає її, а тоді зберігає змінену форму для продовження гри.

### Включає

Розміщення, налаштування або вилучення ротів, частин для пересування й зброї в Cell Creator гри Spore перед збереженням клітини та поверненням у воду.

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

Прибирання сміття першою лопатою від Leafos під час навчання в саду оригінальної Viva Piñata.

### Виключає

Пошук закопаного предмета, збирання врожаю, знищення мешканця або оплата роботи помічника.

### Ігри-носії

- [`GAME-0444` — "Harvest Moon: Back to Nature"](../games/g-l/harvest-moon-back-to-nature.md)
- [`GAME-0375` — Viva Piñata](../games/s-z/viva-pinata.md)

## ACT-513

- Назва: Домовитися про обмін ресурсами за участі активного гравця
- Переглянуто: `2026-09-23`

### Операційне визначення

Активний гравець домовляється з іншим учасником про обмін картками ресурсів визначених видів; будь-хто з цих двох може запропонувати умови, але обидва передають картки лише тоді, коли гравець, чий зараз хід, приймає погоджену пропозицію.

### Включає

Обмін між гравцями під час фази торгівлі CATAN, зокрема зустрічна пропозиція суперника активному гравцеві.

### Виключає

Односторонній подарунок; обмін із банком (ACT-514); торгівлю картками розвитку; пропозицію, яку інший учасник відхиляє.

### Ігри-носії

- [`GAME-0377` — CATAN](../games/a-f/catan.md)

## ACT-514

- Назва: Обмінювати однакові ресурси з банком
- Переглянуто: `2026-09-23`

### Операційне визначення

Гравець повертає до спільного запасу допустиму кількість карток ресурсу одного типу й вибирає одну картку ресурсу іншого типу за курсом, дозволеним поточними правами, що зумовлені розташуванням.

### Включає

Морський обмін у CATAN за звичайним курсом 4:1 або за знижкою відповідної гавані 3:1 чи 2:1.

### Виключає

Двосторонні переговори між гравцями (ACT-513); безкоштовне отримання карток унаслідок ефекту розвитку; обмін без достатньої кількості карток одного типу.

### Ігри-носії

- [`GAME-0377` — CATAN](../games/a-f/catan.md)

## ACT-515

- Назва: Оплатити й розмістити одну допустиму споруду мережі
- Переглянуто: `2026-09-23`

### Операційне визначення

Гравець сплачує вартість ресурсами потрібних типів і бере одну доступну власну фігуру, щоб зайняти допустиме ребро чи вершину поля або замінити власну споруду нижчого рівня її дозволеним поліпшенням на тому самому місці.

### Включає

Будівництво дороги чи поселення та заміну свого поселення містом у CATAN.

### Виключає

Безкоштовне розміщення доріг карткою Road Building; розміщення за браком ресурсів або в недопустимій позиції; купівлю картки розвитку (ACT-516).

### Ігри-носії

- [`GAME-0377` — CATAN](../games/a-f/catan.md)

## ACT-516

- Назва: Купити приховану картку розвитку
- Переглянуто: `2026-10-13`

### Операційне визначення

Гравець сплачує оголошену трійку ресурсів під час фази будівництва й бере верхню картку долілиць зі скінченної колоди розвитку до приватної руки, не вибираючи, яка саме картка йому дістанеться.

### Включає

Купівлю картки розвитку за руду, вовну й зерно у CATAN.

### Виключає

Розіграш картки (ACT-517); вибір відкритої пропозиції; купівлю, коли колоду вичерпано.

### Ігри-носії

- [`GAME-0377` — CATAN](../games/a-f/catan.md)

## ACT-517

- Назва: Зіграти дозволену картку розвитку
- Переглянуто: `2026-09-23`

### Операційне визначення

У власний хід гравець вибирає допустиму картку розвитку, яку має при собі, відкриває її й застосовує для оголошеного правилами ефекту з дотриманням обмеження однієї картки за хід та обмеження, пов’язаного з ходом її купівлі.

### Включає

Розіграш лицаря або картки прогресу в CATAN; для відкриття картки переможного очка, щоб установити переможну суму очок, діє окреме правило.

### Виключає

Купівлю картки (ACT-516); торгівлю нею; розіграш двох карток із категорій лицарів або карток прогресу за той самий хід.

### Ігри-носії

- [`GAME-0377` — CATAN](../games/a-f/catan.md)

## ACT-518

- Назва: Пересунути розбійника й обрати сусіда для крадіжки
- Переглянуто: `2026-09-23`

### Операційне визначення

Після події, що запускає дію розбійника, активний гравець вибирає для нього інший гекс місцевості й, якщо суперники мають прилеглі споруди, вибирає одного з них для випадкового викрадення картки ресурсу.

### Включає

Переміщення розбійника після сімки або зіграного лицаря у CATAN.

### Виключає

Примусове скидання карток через перевищення ліміту; вибір відомої конкретної картки з прихованої руки жертви; залишення розбійника на його поточному гексі.

### Ігри-носії

- [`GAME-0377` — CATAN](../games/a-f/catan.md)

## ACT-519

- Назва: Безперервно нахиляти поле, щоб керувати тілом, яке котиться
- Переглянуто: `2026-10-02`

### Операційне визначення

Гравець змінює кут прохідного ігрового поля безперервним напрямленим введенням, щоб сила тяжіння скеровувала рухоме тіло заданою авторами поверхнею без безпосереднього задавання позиції тіла чи фіксованого ходу.

### Включає

Нахил Simple — першого рівня Jungle Island у сюжетному режимі Super Monkey Ball 2 — за допомогою Control Stick контролера GameCube, щоб спрямовувати кулю з мавпочкою до фінішу.

### Виключає

Безпосереднє пересування аватара (ACT-008); дискретний вибір нової нижньої грані для напрямку сили тяжіння (ACT-097); переміщення камери без зміни поля; вибір цілі для автоматичного пошуку шляху.

### Ігри-носії

- [`GAME-0537` — Kirby Tilt 'n' Tumble](../games/g-l/kirby-tilt-n-tumble.md)
- [`GAME-0717` — "LocoRoco 2"](../games/g-l/locoroco-2.md)
- [`GAME-0482` — LocoRoco](../games/g-l/locoroco.md)
- [`GAME-0378` — Super Monkey Ball 2](../games/s-z/super-monkey-ball-2.md)

## ACT-520

- Назва: Прицілитися й вистрілити зброєю чергового черв’яка
- Переглянуто: `2026-09-24`

### Операційне визначення

Протягом ходу активної команди гравець вибирає доступну зброю, яку має при собі, задає відповідні налаштування наведення, заряду або запалу з поточної позиції черв’яка, який може пересуватися, а потім виконує один постріл із подальшим фізичним розв’язанням.

### Включає

Прицілювання та постріл із базуки або гранати з налаштованими запалом і відскоком у дослідженому офлайновому артилерійському матчі Worms Armageddon.

### Виключає

Нерухому пускову установку (ACT-113); стрільбу з кількох не пов’язаних між собою одиниць зброї за один хід; безпосереднє керування снарядом після його випуску.

### Ігри-носії

- [`GAME-0379` — Worms Armageddon](../games/s-z/worms-armageddon.md)

## ACT-521

- Назва: Обвести й подати як відповідь одне місце на ілюстрації
- Переглянуто: `2026-09-24`

### Операційне визначення

У заданій авторами візуальній головоломці гравець обводить замкненою лінією одну з можливих ділянок наданої ілюстрації й окремо подає позначену ділянку як відповідь для оцінювання.

### Включає

Обведення стилусом вибраного села на початковій карті Professor Layton and the Curious Village та натискання Submit.

### Виключає

Змінювану захисну позначку-гіпотезу (ACT-004); заповнення всієї сітки відповідей; вибір місця призначення у світі для подорожі персонажа; звичайний дотик до екрана без подання відповіді.

### Ігри-носії

- [`GAME-0380` — Professor Layton and the Curious Village](../games/m-r/professor-layton-and-the-curious-village.md)

## ACT-522

- Назва: Купити наступну підказку за монету
- Переглянуто: `2026-09-24`

### Операційне визначення

Під час нерозв’язаної авторської загадки гравець свідомо витрачає одну наявну монету підказок, щоб відкрити наступне заздалегідь написане уточнення, не подаючи відповіді.

### Включає

Купівля наступної з максимум трьох підказок до дослідженої початкової загадки Professor Layton and the Curious Village.

### Виключає

Автоматичну навчальну пораду, пошук прихованої монети в сцені, купівлю стороннього предмета й відкриття всіх підказок одним платежем.

### Ігри-носії

- [`GAME-0380` — Professor Layton and the Curious Village](../games/m-r/professor-layton-and-the-curious-village.md)

## ACT-523

- Назва: Нанести на ігровий світ мазок Небесним пензлем
- Переглянуто: `2026-09-24`

### Операційне визначення

Гравець відкриває окремий режим огляду поточного світу для роботи пензлем, проводить просторову позначку поверх допустимого видимого об’єкта чи прогалини й закриває цей огляд, подаючи позначку на перевірку для дії вивченої техніки на стан світу.

### Включає

Домалювання штрихом пензля відсутньої частини Небесної ріки чи меча статуї Наґі та розрізання валуна, перегороди або ніжки плоду в Камікі в дослідженому початку Ōkami HD.

### Виключає

Малювання статичної відповіді на сторінці головоломки (ACT-521); удар спорядженим відбивачем (ACT-161); суто декоративний слід курсора; техніку, яку ще не вивчено.

### Ігри-носії

- [`GAME-0382` — Ōkami HD](../games/m-r/okami-hd.md)

## ACT-524

- Назва: Перемикати вибраного члена постійної сім’ї
- Переглянуто: `2026-09-24`

### Операційне визначення

Гравець вибирає іншого мешканця тієї самої збережуваної сім’ї як поточного одержувача контекстних команд, а раніше вибраний мешканець залишається присутнім, і симуляція й далі обробляє його стан.

### Включає

Перемикання між двома дорослими в дослідженій сім’ї The Sims 2: Legacy Collection через портрети в режимі життя.

### Виключає

Заміну сім’ї; безпосереднє керування кожним рухом головного персонажа (ACT-228); вибір об’єкта без зміни активного учасника.

### Ігри-носії

- [`GAME-0383` — The Sims 2: Legacy Collection](../games/s-z/the-sims-2-legacy-collection.md)
- [`GAME-0461` — The Sims](../games/s-z/the-sims.md)

## ACT-525

- Назва: Запросити бічну або обертальну атаку гоночної машини
- Переглянуто: `2026-09-24`

### Операційне визначення

Під час безпосереднього керування гоночною машиною поблизу машин суперників гравець подає команду напрямленого бічного або обертального удару, контакт якого може змістити чи вибити суперників із поточного заїзду.

### Включає

Бічні й обертальні атаки в оригінальній GameCube-версії F-Zero GX під час дослідженого заїзду Grand Prix на Twist Road — першого заїзду Ruby Cup.

### Виключає

Звичайне зіткнення під час кермування; застосування випадково отриманого предмета; удар персонажа поза гоночною машиною.

### Ігри-носії

- [`GAME-0384` — F-Zero GX](../games/a-f/f-zero-gx.md)

## ACT-526

- Назва: Запросити пояснення одного вибраного твердження свідка
- Переглянуто: `2026-09-24`

### Операційне визначення

Під час судового перехресного допиту гравець вибирає один наразі доступний рядок заданих авторами свідчень і просить свідка роз’яснити його; це може відкрити уточнення або нову версію рядка.

### Включає

Запит пояснення вибраного твердження Френка Соуіта в першій справі The First Turnabout у Phoenix Wright: Ace Attorney.

### Виключає

Просування пасивного діалогу; подання окремого доказу проти рядка (ACT-527); довільний допит персонажа поза інтерфейсом свідчень; припущення, що кожен запит пояснення змінює матеріали справи.

### Ігри-носії

- [`GAME-0385` — 'Phoenix Wright: Ace Attorney'](../games/m-r/phoenix-wright-ace-attorney.md)

## ACT-527

- Назва: Подати один матеріал справи проти вибраного твердження свідка
- Переглянуто: `2026-09-24`

### Операційне визначення

Коли вибрано один рядок заданих авторами свідчень, гравець обирає наявний на цей момент матеріал справи й подає його до суду як доказ суперечності саме цьому рядку.

### Включає

Подання звіту про розтин проти твердження Соуіта про час або запису про відключення електрики проти його слів про телевізор у першій справі.

### Виключає

Запит роз’яснення (ACT-526); саме читання доказів; виділення двох фактів, які можна редагувати, в інтерфейсі огляду (ACT-104); особисте затвердження вироку для всієї справи штампом (ACT-105).

### Ігри-носії

- [`GAME-0385` — 'Phoenix Wright: Ace Attorney'](../games/m-r/phoenix-wright-ace-attorney.md)

## ACT-528

- Назва: Оглядати предмет із місця події, який гравець тримає, доки не відкриється його доказова деталь
- Переглянуто: `2026-09-24`

### Операційне визначення

Після звернення до досяжного предмета на місці події гравець змінює його орієнтацію під час огляду або фокус, доки не відкриється значуща для механіки гри мітка, напис чи прихована поверхня й не буде зареєстрована як доказ справи.

### Включає

Поворот окулярів з вантажного депо до позначки виробника та огляд даних про особу з гаманця у справі The Driver’s Seat гри L.A. Noire.

### Виключає

Підбирання декоративного дріб’язку без зарахованого доказу; пасивне одержання факту з діалогу; збирання збережуваного інструмента до інвентарю (ACT-089); вибір матеріалу судової справи як суперечності (ACT-527).

### Ігри-носії

- [`GAME-0388` — L.A. Noire](../games/g-l/la-noire.md)

## ACT-529

- Назва: Подати записаний доказ проти однієї відповіді на допиті
- Переглянуто: `2026-09-24`

### Операційне визначення

Після вибору звинувачення співрозмовника щодо поточної відповіді гравець вибирає один наразі доступний доказ із записника справи як суперечність, пред’явлену цьому співрозмовникові саме щодо цієї теми.

### Включає

Вибір знайденого доказу після команди Accuse в допиті першої справи дорожнього відділу у версії L.A. Noire для PS4.

### Виключає

Вибір Good Cop або Bad Cop без доказу (ACT-232); подання доказу проти окремо доступного для вибору рядка судових свідчень (ACT-527); виділення двох фактів у документах (ACT-104).

### Ігри-носії

- [`GAME-0388` — L.A. Noire](../games/g-l/la-noire.md)

## ACT-530

- Назва: Вибрати вихідний маршрут на досягнутій розвилці ігрового поля
- Переглянуто: `2026-09-24`

### Операційне визначення

Коли фішка проходить фіксованим зв’язаним маршрутом на кількість клітинок, визначену кубиком, активний гравець на розвилці обирає один допустимий вихідний напрям. Фішка далі витрачає решту того самого кидка на обрану гілку.

### Включає

Спрямування персонажа на розвилці шляху поля Pirate Land у Mario Party 2 після того, як Dice Block визначив кількість клітинок для руху.

### Виключає

Вибір результату кубика SYS-004; редагування мережі поля; вибір вузла наступного поверху в Slay the Spire ACT-127; необмежене переміщення до віддаленої клітинки; вибір результату мінігри.

### Ігри-носії

- [`GAME-0392` — Mario Party 2](../games/m-r/mario-party-2.md)

## ACT-531

- Назва: Зачепитися тросом, змінити його довжину й відпустити
- Переглянуто: `2026-09-24`

### Операційне визначення

Гравець спрямовує багаторазовий трос на сумісну досяжну опору, утримує зачеплення, керує тілом у підвішеному стані й змінює довжину троса, а потім у вибраний момент відпускає його для вільного руху.

### Включає

Гак у дослідженому маршруті Grab and Swing гри LittleBigPlanet 2: зачеплення за губку, розгойдування вбік, скорочення або подовження троса та відпускання у вибраний момент.

### Виключає

Односпрямоване підтягування до вибраної опори, де завершується рух (ACT-361); лазіння закріпленою мотузкою без прицільного зачеплення; хапання вільного предмета для перенесення; автоматичне сценарне розгойдування без рішення гравця про відпускання.

### Ігри-носії

- [`GAME-0552` — Jusant](../games/g-l/jusant.md)
- [`GAME-0394` — LittleBigPlanet 2](../games/g-l/littlebigplanet-2.md)

## ACT-532

- Назва: Увести вивчену впорядковану послідовність символів до вибраного інтерфейсу
- Переглянуто: `2026-09-24`

### Операційне визначення

Гравець звертається до інтерфейсу, що приймає команди, і по черзі вводить скінченну вивчену послідовність символів, які не є напрямками, не пересуваючи персонажа відповідним маршрутом.

### Включає

Уведення вивченого числового пароля Бомберів у проході до обсерваторії Clock Town та відтворення з пам’яті послідовності нот Пісні часу на повернутій окарині в пролозі першого циклу Majora’s Mask.

### Виключає

Послідовності команд основних напрямків (ACT-106); проходження маршруту пішки; довільне музикування; вибір відповіді в діалозі; скидання, запущене системою без поданої послідовності.

### Ігри-носії

- [`GAME-0395` — "The Legend of Zelda: Majora’s Mask"](../games/s-z/the-legend-of-zelda-majoras-mask.md)

## ACT-533

- Назва: Повторити фразу викладача натисканнями кнопок у заданому ритмі
- Переглянуто: `2026-09-25`

### Операційне визначення

Після того як викладач демонструє коротку задану авторами музичну фразу, гравець натискає відповідні її символам кнопки контролера в заданому порядку на відповідних долях пізнішого проміжку відповіді гравця.

### Включає

Відповіді на фрази першого уроку в додзьо на складності Normal у PaRappa the Rapper Remastered.

### Виключає

Одночасні події карти нот із затисканням ладів та ударом по струнах (ACT-508); уведення вивченого пароля без запланованого звернення викладача (ACT-532); непов’язане довільне музикування.

### Ігри-носії

- [`GAME-0396` — "PaRappa the Rapper Remastered"](../games/m-r/parappa-the-rapper-remastered.md)
- [`GAME-0544` — Space Channel 5](../games/s-z/space-channel-5.md)

## ACT-534

- Назва: Виконати дію поточної короткої мікрогри
- Переглянуто: `2026-09-25`

### Операційне визначення

Після появи короткої вказівки гравець вибирає й виконує наразі відповідну їй просту реакцію контролером упродовж короткого поточного проміжку цієї мікрогри, не переносячи значення цього введення на наступне завдання.

### Включає

Натиснути A, щоб перестрибнути машину в Crazy Cars, або скеровувати персонажа хрестовиною в Diamond Dig під час вступного курсу WarioWare.

### Виключає

Пересування збережуваного персонажа в межах цілого рівня (ACT-008); повторення заданої музичної фрази доля за долею (ACT-533); захисну відповідь саме на ворожу атаку з попереднім сигналом (ACT-223).

### Ігри-носії

- [`GAME-0398` — 'WarioWare, Inc.: Mega Microgame$!'](../games/s-z/warioware-inc-mega-microgame.md)

## ACT-535

- Назва: Звернутися до залежної супутниці покликом, узяттям за руку або допомогою піднятися на уступ
- Переглянуто: `2026-09-25`

### Операційне визначення

Гравець звертається до однієї залежної супутниці поблизу й контекстною командою кличе її, бере за руку або допомагає піднятися на уступ. Це запитує її наступний рух чи відновлення положення, а не передає гравцеві безпосереднє керування нею.

### Включає

Поклик до Йорди підійти до Іко, узяття її за руку для ведення й підтягування на досяжний вищий уступ під час першої втечі з вежі у грі Ico.

### Виключає

Перемикання самостійно здатного діяти охоронця між слідуванням і очікуванням (ACT-408); вибір одиниці загону для безпосереднього керування; автоматичну телепортацію супутниці, до якої не зверталися командою, до гравця; відкриття дверей Ідолів — окрему дозволену взаємодію Йорди.

### Ігри-носії

- [`GAME-0399` — Ico](../games/g-l/ico.md)
- [`GAME-0588` — Neva](../games/m-r/neva.md)
- [`GAME-0559` — The Last Guardian](../games/s-z/the-last-guardian.md)

## ACT-536

- Назва: Витратити одну бомбу під час бою на арені
- Переглянуто: `2026-09-25`

### Операційне визначення

Під час поточного руху й бою гравець витрачає один доступний заряд екстреної бомби зі скінченного запасу, щоб запросити негайне очищення локальної ділянки, не прицілюючись у конкретного противника.

### Включає

Натискання будь-якого курка для застосування однієї розумної бомби під час спроби набору очок Evolved в оригінальній Xbox 360-версії Geometry Wars: Retro Evolved.

### Виключає

Розміщення відкладеної бомби на клітинці (ACT-270); реакцію засобом протидії на наближення ракети, наведеної на захоплену ціль (ACT-395); звичайну напрямлену стрільбу зі зброї (ACT-161); системний результат вибуху й нарахування очок (SYS-1070).

### Ігри-носії

- [`GAME-0400` — "Geometry Wars: Retro Evolved"](../games/g-l/geometry-wars-retro-evolved.md)

## ACT-537

- Назва: Провести один безперервний різальний рух крізь активні об’єкти
- Переглянуто: `2026-09-25`

### Операційне визначення

Гравець утримує дотик і рухає його одним безперервним шляхом на екрані, а потім відпускає; кожен допустимий рухомий об’єкт, який цей шлях перетнув, належить до цього одного виконаного штриха.

### Включає

Один змах пальцем крізь кілька фруктів у повітрі в режимі Classic оригінальної iPhone-версії Fruit Ninja 1.2.

### Виключає

Окремі натискання на цілі; шлях сіткою з фіксованими кінцями (ACT-016); перерізання вибраного мотузкового з’єднання (ACT-027); малювання вивченої техніки пензлем на застиглому зображенні (ACT-523); системний результат перетину (SYS-1072).

### Ігри-носії

- [`GAME-0401` — "Fruit Ninja"](../games/a-f/fruit-ninja.md)

## ACT-538

- Назва: Задати збережувані налаштування темпу експедиції та пайків
- Переглянуто: `2026-09-25`

### Операційне визначення

У меню подорожі гравець вибирає налаштування подальшої швидкості руху й добових порцій їжі; обидва зберігаються, доки гравець свідомо їх не змінить.

### Включає

Вибір темпу steady (рівний), strenuous (напружений) або grueling (виснажливий) та пайків filling (ситні), meager (мізерні) або bare-bones (мінімальні) перед Канзасом у шкільному виданні The Oregon Trail A-157.

### Виключає

Негайне з’їдання їжі; один тактичний хід; зміну швидкості погодою без рішення гравця.

### Ігри-носії

- [`GAME-0402` — "The Oregon Trail"](../games/s-z/the-oregon-trail.md)

## ACT-539

- Назва: Обрати дію на переправі за станом річки
- Переглянуто: `2026-09-25`

### Операційне визначення

Діставшись річки й побачивши її виміри та запропоновані варіанти, гравець підтверджує один із них: перейти вбрід, законопатити фургон і перепливти, найняти доступний пором або зачекати.

### Включає

Рішення на переправі через Канзас після перегляду глибини й ширини у виданні A-157.

### Виключає

Керування плотом на Колумбії; звичайну подорож; припущення про успіх обраної переправи ще до визначення результату ризикового переходу.

### Ігри-носії

- [`GAME-0402` — "The Oregon Trail"](../games/s-z/the-oregon-trail.md)

## ACT-540

- Назва: Витратити день на полювання заради харчів
- Переглянуто: `2026-09-25`

### Операційне визначення

Гравець перериває рух, прицілюється й витрачає обмежені набої на доступну дичину, сподіваючись принести їжу ціною одного дня.

### Включає

Необов’язкове полювання до Канзасу у виданні The Oregon Trail A-157.

### Виключає

Бій із противником; купівлю їжі; неявне зарахування повної ваги тварини замість обмеженої кількості, яку принесли назад.

### Ігри-носії

- [`GAME-0402` — "The Oregon Trail"](../games/s-z/the-oregon-trail.md)

## ACT-541

- Назва: Запропонувати речі при собі для обміну на шляху
- Переглянуто: `2026-09-25`

### Операційне визначення

На допустимій зупинці подорожі гравець пропонує речі, які має при собі, в обмін на бажаний припас; прийнятий обмін змінює запаси експедиції та витрачає день.

### Включає

Команда Attempt to trade на першому відрізку шляху The Oregon Trail A-157.

### Виключає

Купівлю за сталою ціною в крамниці Метта до початку аналізу; пасивну знахідку; автоматичний прибуток торгового маршруту.

### Ігри-носії

- [`GAME-0402` — "The Oregon Trail"](../games/s-z/the-oregon-trail.md)

## ACT-542

- Назва: Спрямувати всмоктування пилососа на досяжний закріплений об’єкт світу
- Переглянуто: `2026-09-25`

### Операційне визначення

Гравець наводить і утримує всмоктування переносного пилососа на сумісному закріпленому об’єкті світу, щоб той змінив стан, не забираючи його до інвентарю при собі й не трактуючи введення як удар, що завдає шкоди.

### Включає

Гасіння запалених свічок у Parlor за допомогою Poltergust до появи перших звичайних привидів в оригінальній Luigi’s Mansion.

### Виключає

Збирання вільних слизів у типізований резервуар (ACT-467); всмоктування привида з відкритим серцем, який чинить опір (ACT-544); звичайне контекстне використання скрині чи дверей (ACT-341).

### Ігри-носії

- [`GAME-0403` — "Luigi's Mansion"](../games/g-l/luigis-mansion.md)
- [`GAME-0707` — "The Gunk"](../games/s-z/the-gunk.md)

## ACT-543

- Назва: Тримати переносне світло вимкненим і спрямувати його на ворога поблизу, щоб відкрити вразливість
- Переглянуто: `2026-09-25`

### Операційне визначення

Гравець навмисно не дає світити напрямленому джерелу, яке має при собі, поки наближається до чутливого до світла противника, а потім наводить його промінь на противника поблизу, щоб запросити тимчасове відкриття вразливості.

### Включає

Утримування B, щоб ліхтарик Луїджі не світив, а потім освітлення привида зблизька в Parlor за оригінальними правилами GameCube-версії.

### Виключає

Увімкнення загального освітлення кімнати; постріл снарядом, що завдає шкоди; постійне сканування, яке позначає майбутні цілі; системну реакцію вразливості (SYS-1080).

### Ігри-носії

- [`GAME-0403` — "Luigi's Mansion"](../games/g-l/luigis-mansion.md)

## ACT-544

- Назва: Втримувати привида пилососом і протидіяти його втечі
- Переглянуто: `2026-09-25`

### Операційне визначення

Гравець утримує наведене всмоктування пилососа на досяжному привиді з наразі відкритою вразливістю й безперервно керує в напрямку, протилежному напрямку його втечі, щоб опір міг вичерпуватися на шляху до захоплення.

### Включає

Утримування R й відхилення Control Stick та C Stick у напрямку від привида в Parlor під час захоплення за оригінальними правилами GameCube.

### Виключає

Збирання вільного предмета одним натисканням; оборотне зберігання істоти в резервуарі Vacpack (ACT-467); освітлення ліхтариком (ACT-543); фактичне зменшення сили та системну реакцію захоплення (SYS-1081).

### Ігри-носії

- [`GAME-0403` — "Luigi's Mansion"](../games/g-l/luigis-mansion.md)

## ACT-545

- Назва: Наступити на напрямні панелі підлоги за показаними стрілками у відповідну долю ритму
- Переглянуто: `2026-09-26`

### Операційне визначення

Коли показана напрямлена подія карти кроків досягає фіксованої зони кроку, гравець фізично наступає на відповідну панель підлоги або одночасно на пару панелей, якщо подія парна.

### Включає

Сольна гра ногами на чотирьох панелях зі стрілками аркадного автомата Konami GN845-UC DanceDanceRevolution.

### Виключає

Затискання ладів і удар по струнах (ACT-508); відповідь на фразу викладача (ACT-533); загальну перевірку вміння з рухомим покажчиком (ACT-261); пізніші в серії механіки утримування або Freeze Arrow.

### Ігри-носії

- [`GAME-0406` — "DanceDanceRevolution"](../games/a-f/dancedancerevolution.md)

## ACT-546

- Назва: Клацанням зібрати тимчасовий жетон виробленого ресурсу
- Переглянуто: `2026-09-26`

### Операційне визначення

Гравець явно клацає по видимій одиниці ресурсу, що існує недовго, до спливу її часу існування, зараховуючи її значення до спільного балансу, який можна витрачати; саме генерування без клацання нічого не надає.

### Включає

Збирання сонця, що падає вдень або утворюється соняшниками, на звичайному денному рівні Adventure у Plants vs. Zombies.

### Виключає

Проходження персонажем через предмет для підбирання; періодичне поповнення, надане автоматично; зарахування після хвилі; збирання врожаю, який зберігається у світі, до інвентарю при собі.

### Ігри-носії

- [`GAME-0407` — Plants vs. Zombies](../games/m-r/plants-vs-zombies.md)

## ACT-547

- Назва: Лопатою звільнити клітинку, зайняту захисником
- Переглянуто: `2026-09-26`

### Операційне визначення

Гравець застосовує багаторазовий інструмент вилучення до одного вже розміщеного захисника, прибирає його й звільняє зайняту клітинку для подальшого розміщення, не переносячи захисника до інвентарю.

### Включає

Використання лопати на зайнятій клітинці газону після рівня 1-4 під час гри Adventure в оригінальній Plants vs. Zombies.

### Виключає

Продаж із зарахуванням відомого відшкодування; команду вилучення, що повертає предмет (ACT-122); знищення противника; одноразову атакувальну рослину, що автоматично витрачає саму себе.

### Ігри-носії

- [`GAME-0407` — Plants vs. Zombies](../games/m-r/plants-vs-zombies.md)

## ACT-548

- Назва: Надути звичайне кероване тіло й рухатися рівнем змахами
- Переглянуто: `2026-09-26`

### Операційне визначення

Поки безпосередньо кероване тіло перебуває у звичайній формі, гравець навмисно надуває його, повторює команду польоту для набору висоти й може випустити утримуване повітря як атаку, завершуючи цю повітряну форму до наступного надування тіла.

### Включає

Кірбі у звичайній формі натискає вгору, виконує змахи кнопкою A й за бажанням випускає повітряний снаряд кнопкою B під час маршруту Vegetable Valley 1-1 в оригінальній NES-версії Kirby’s Adventure.

### Виключає

Постійно летючого персонажа; окремо здобуту тимчасову здібність до надування; звичайний одинарний стрибок; пасивну плавучість без повторного керування; скопійовану здібність ворога.

### Ігри-носії

- [`GAME-0408` — Kirby's Adventure](../games/g-l/kirbys-adventure.md)

## ACT-549

- Назва: Вдихнути й розв’язати долю втриманого в роті об’єкта
- Переглянуто: `2026-09-26`

### Операційне визначення

Безпосередньо керований персонаж вдихає одного допустимого ворога або блок поблизу й переходить до стану утримування єдиного тіла в роті, а потім дає команду виплюнути його як зірку-снаряд або проковтнути; виконання обраної команди звільняє рот.

### Включає

Кірбі вдихає Ваддл Ду у першому етапі Долини овочів і натискає вниз, щоб проковтнути його; видих кнопкою B лишається не обраною на цьому маршруті альтернативою.

### Виключає

Язик і рот супутника, на якому їде гравець (ACT-493); автоматичне ковтання за таймером; предмет, зібраний до інвентарю; саму скопійовану здібність, яку надає ковтання ворога визначеного типу.

### Ігри-носії

- [`GAME-0408` — Kirby's Adventure](../games/g-l/kirbys-adventure.md)

## ACT-550

- Назва: Циклічно перемикати зброю в запасі машини, щоб активувати один тип
- Переглянуто: `2026-10-13`

### Операційне визначення

Керуючи бойовою машиною, що несе кілька видів зброї, гравець перемикає доступний арсенал і робить один вид активним для наступної команди пострілу, не витрачаючи боєприпасів самим вибором.

### Включає

Перемикання з поточної зброї на тип підібраних ракет у першій сюжетній арені Junkyard оригінальної PS2-версії Twisted Metal: Black.

### Виключає

Збирання зброї; постріл із витратою її боєприпасів; вибір машини до входу на арену; загальну комірку швидкого доступу до інвентарю предметів, які тримають у руках; автоматичну підміну після вичерпання боєприпасів, якщо правила прямо не передбачають такої підміни.

### Ігри-носії

- [`GAME-0509` — MechAssault](../games/m-r/mechassault.md)
- [`GAME-0409` — 'Twisted Metal: Black'](../games/s-z/twisted-metal-black.md)

## ACT-551

- Назва: Подати другу команду вже випущеній зброї у вибрану мить
- Переглянуто: `2026-09-26`

### Операційне визначення

Після запуску одного снаряда чи пристрою гравець повторною командою під час його руху визначає момент або місце дії того самого об’єкта, а не випускає новий.

### Включає

Junkyard Dog випускає шиповану кулю й дає команду вистрілити ще раз, щоб опустити ту саму кулю на прицільну позначку в оригінальній PS2-версії Twisted Metal: Black.

### Виключає

Звичайний одиничний пуск ракети; автоматичне влучання при дотику; постріл другим незалежним снарядом; підрив постійного джерела небезпеки на мапі.

### Ігри-носії

- [`GAME-0409` — 'Twisted Metal: Black'](../games/s-z/twisted-metal-black.md)

## ACT-552

- Назва: Вибрати союзне місце приземлення на мапі й підтвердити стрибок
- Переглянуто: `2026-09-26`

### Операційне визначення

З активної командної мапи гравець вибирає одного наразі допустимого союзного учасника або місце появи команди й підтверджує швидке переміщення до цього поточного місця приземлення, а не вільно вибирає будь-яку координату світу.

### Включає

Super Jump від місця появи своєї команди до союзника, який перебуває ближче до спірної території, у Regular Battle гри Splatoon 3.

### Виключає

Звичайну ходьбу чи плавання у власному чорнилі; телепортацію на довільне місце на землі; автоматичну повторну появу після вибивання з бою без вибору місця призначення; пізніші модифікатори балансу Stealth Jump.

### Ігри-носії

- [`GAME-0412` — Splatoon 3](../games/s-z/splatoon-3.md)

## ACT-553

- Назва: Закрити видиме протікання відстежуваною частиною тіла
- Переглянуто: `2026-09-26`

### Операційне визначення

Гравець переміщує допустиму частину тіла, яку безперервно відстежують, до поточного видимого просторового місця протікання й утримує її там для підтримання контакту, а не подає одноразову команду контролером.

### Включає

Прикладання кисті, стопи, коліна або голови до одного отвору в склі в завданні 20,000 Leaks оригінальної Xbox 360-версії Kinect Adventures!.

### Виключає

Напрямлений змах віртуальним сачком (ACT-477); зчитаний випуск кулі в боулінгу (ACT-499); крок на окрему танцювальну панель (ACT-545); декоративне віддзеркалення персонажа без контакту з протіканням.

### Ігри-носії

- [`GAME-0414` — Kinect Adventures!](../games/g-l/kinect-adventures.md)

## ACT-554

- Назва: Завершити день армії та передати хід
- Переглянуто: `2026-09-26`

### Операційне визначення

Гравець явно завершує поточний тактичний день керованої сторони, відмовляючись від будь-яких необов’язкових наказів, які ще можна було б віддати підрозділам, і передає командування супротивній стороні, а не віддає наказ очікувати лише одній одиниці.

### Включає

Команда End після будь-якої кількості наказів піхоті Orange Star у навчальному завданні Advance Wars «Terrain Intel».

### Виключає

Наказ Wait одній піхотній одиниці; автоматичну відповідь ворога одразу після кожного переміщення; паузу в реальному часі; обов’язковий наказ кожній союзній одиниці, перш ніж сторона зможе завершити день.

### Ігри-носії

- [`GAME-0416` — Advance Wars](../games/a-f/advance-wars.md)

## ACT-555

- Назва: Наказати члену екіпажу перейти до кімнати корабля
- Переглянуто: `2026-09-27`

### Операційне визначення

Гравець обирає доступного члена екіпажу й наказує йому перейти до досяжної кімнати свого корабля. Там він може обслуговувати систему, ремонтувати пошкодження або долати небезпеку, поки решта корабля продовжує діяти.

### Включає

Переведення одного з початкових членів екіпажу «Боривітра» (Kestrel) з поста до пошкодженого системного відсіку під час ворожої сутички біля маяка в FTL.

### Виключає

Безпосереднє керування кораблем; постійне призначення праці в колонії; телепортацію на ворожий корабель; ремонт без прибуття екіпажу до кімнати.

### Ігри-носії

- [`GAME-0418` — 'FTL: Faster Than Light'](../games/a-f/ftl-faster-than-light.md)

## ACT-556

- Назва: Націлити заряджену корабельну зброю на кімнату ворога
- Переглянуто: `2026-09-27`

### Операційне визначення

Гравець вибирає корабельну зброю з поданим живленням і позначає один наразі доступний для наведення відсік ворожого корабля як ціль її наступного пострілу, підтверджуючи витрату заряду цієї зброї та сумісних боєприпасів, коли відбувається постріл.

### Включає

Націлювання Burst Laser II або ракетниці Artemis «Боривітра» (Kestrel) на ворожий відсік зброї чи щитів під час сутички базової гри.

### Виключає

Безпосереднє пілотування снаряда; саме подання живлення зброї; гарантоване влучання у відсік попри ухилення; атаки по єдиному запасу здоров’я всього корабля без цілі у вигляді відсіку.

### Ігри-носії

- [`GAME-0418` — 'FTL: Faster Than Light'](../games/a-f/ftl-faster-than-light.md)

## ACT-557

- Назва: Погладити здатне реагувати цуценя сенсорним дотиком
- Переглянуто: `2026-09-27`

### Операційне визначення

Гравець торкається сенсорного екрана в області цуценяти поблизу й рухає дотик, щоб погладити його, вибираючи, де і як довго продовжувати взаємодію, поки цуценя може реагувати.

### Включає

Гладіння першого цуценяти, якому вже дали ім’я, на сенсорному екрані Nintendo DS під час домашнього сеансу оригінальної Nintendogs.

### Виключає

Перетягування цуценяти як керованої фігури; вибір команди меню без дотику до тварини; розчісування засобом догляду; припущення, що позитивна реакція триватиме без обмежень.

### Ігри-носії

- [`GAME-0419` — Nintendogs](../games/m-r/nintendogs.md)

## ACT-558

- Назва: Звернутися до навченого цуценяти через мікрофон
- Переглянуто: `2026-09-27`

### Операційне визначення

Вимовити ім’я або команду в мікрофон, щоб покликати цуценя, пов’язати нову команду з дією під час навчання або попросити виконати вже вивчений трюк. Вимовлене слово не працює як гарантоване натискання кнопки.

### Включає

Надання імені першому цуценяті Nintendogs і навчання його першому сигналу для дії «сидіти» або вимовляння цього сигналу пізніше.

### Виключає

Лише введення імені текстом; запис повідомлення Bark Mode; вибір сценарної репліки діалогу; безпосереднє переміщення цуценяти стиком керування.

### Ігри-носії

- [`GAME-0419` — Nintendogs](../games/m-r/nintendogs.md)

## ACT-559

- Назва: Вибрати й застосувати засіб догляду за цуценям
- Переглянуто: `2026-09-27`

### Операційне визначення

Відкрити доступну категорію засобів догляду, вибрати власний предмет для годування чи догляду за шерстю і застосувати його до цуценяти через сенсорний екран.

### Включає

Застосування одного доступного засобу годування, напування чи догляду за шерстю в першому домашньому сеансі оригінальної Nintendogs після розблокування Supplies.

### Виключає

Купівлю засобу в крамниці; кидання іграшки для гри; автоматичний наказ із догляду за тваринами в усьому зоопарку; твердження, що певний предмет є в запасі кожного початкового файлу.

### Ігри-носії

- [`GAME-0419` — Nintendogs](../games/m-r/nintendogs.md)

## ACT-560

- Назва: Передати строю наказ барабанною фразою на чотири долі
- Переглянуто: `2026-09-27`

### Операційне визначення

У поточному ритмічному проміжку під час гри гравець відтворює кнопками чотири впорядковані барабанні звуки; розпізнана фраза вибирає наказ руху чи бойовий наказ для наявного строю, а не безпосередньо керує одним його учасником.

### Включає

PATA PATA PATA PON наказує марширувати, а PON PON PATA PON — атакувати під час першого полювання на Patata Plain в оригінальній PSP-версії Patapon.

### Виключає

Повторення щойно продемонстрованої викладачем фрази (ACT-533); узгодження кроків на панелях зі стрілками, що прокручуються (ACT-545); задання окремому солдатові позиції або команди удару; декоративне барабанення, яке не віддає наказу.

### Ігри-носії

- [`GAME-0422` — Patapon](../games/m-r/patapon.md)

## ACT-561

- Назва: Зібрати й переробити безпосередньо керований транспортний засіб із доступних деталей
- Переглянуто: `2026-09-27`

### Операційне визначення

У майстерні транспортних засобів гравець вибирає доступні функціональні деталі, приєднує, пересуває або вилучає їх у зв’язаній конструкції транспортного засобу, а потім зберігає або вибирає цю конструкцію для безпосереднього керування під час випробування.

### Включає

Збирання компактного колісного бульдозера з широким переднім ковшем із доступних деталей Mumbo’s Motors, випробування й вибір цієї конструкції для Great Balls of Fire у другому акті Nutty Acres.

### Виключає

Вибір незмінного готового серійного транспортного засобу; косметичне фарбування; заміну спорядження у фіксованій комірці під час перегонів; збирання автономної фабрики; вимогу саме цієї власної конструкції, коли початковий візок може завершити випробування.

### Ігри-носії

- [`GAME-0423` — "Banjo-Kazooie: Nuts & Bolts"](../games/a-f/banjo-kazooie-nuts-and-bolts.md)

## ACT-562

- Назва: Керувати засобом польоту в коридорі, що автоматично просувається вперед
- Переглянуто: `2026-09-27`

### Операційне визначення

Гравець безперервно змінює положення безпосередньо керованого засобу польоту за двома поперечними осями екрана, поки просування заданим авторами маршрутом відбувається автоматично, коригуючи локальну траєкторію між загрозами й проходами без вибору місця призначення у вільному просторі.

### Включає

Пілотування Arwing Фокса під сімома кам’яними арками Corneria з одночасним кермуванням в обхід видимих небезпек в оригінальній Nintendo 64-версії Star Fox 64 у режимі 3D Scroll Mode.

### Виключає

Керування необмеженим космічним польотом за трьома осями (ACT-392); поворот камери для зміни геометрії; скеровування автономного засобу польоту; гру з автоматичним бігом і лише однією кнопкою вертикального керування; вибір вузла маршруту на мапі.

### Ігри-носії

- [`GAME-0623` — "Blue Lightning"](../games/a-f/blue-lightning.md)
- [`GAME-0650` — Einhänder](../games/a-f/einhander.md)
- [`GAME-0587` — Panzer Dragoon II Zwei](../games/m-r/panzer-dragoon-ii-zwei.md)
- [`GAME-0505` — Panzer Dragoon](../games/m-r/panzer-dragoon.md)
- [`GAME-0697` — "Radiant Silvergun"](../games/m-r/radiant-silvergun.md)
- [`GAME-0424` — "Star Fox 64"](../games/s-z/star-fox-64.md)

## ACT-563

- Назва: Застосувати одне диво божественною рукою до обраної цілі
- Переглянуто: `2026-10-13`

### Операційне визначення

Гравець активує доступне божественне диво, розташовує Руку над обраним допустимим одержувачем у світі й підтверджує ефект саме там, замість безпосередніх дій зі створеним ресурсом або наказу агентові.

### Включає

Розкриття бульбашки одноразового Food Miracle та застосування його їжі над Guide’s Aztec Village Store на першому острові оригінальної Windows-версії Black & White, поки істота на навчальному повідку спостерігає.

### Виключає

Розіграш карти закляття з руки під час покрокової гри (ACT-333); самостійне застосування істотою дива після навчання; розміщення зібраного зерна безпосереднім підбиранням; надання можливості застосувати диво без наявного доступного дива.

### Ігри-носії

- [`GAME-0425` — "Black & White"](../games/a-f/black-and-white.md)

## ACT-564

- Назва: Відгорнути покривний папір дотиком до переднього екрана
- Переглянуто: `2026-09-27`

### Операційне визначення

Гравець тягне видимий край паперу на передньому сенсорному екрані, щоб покривний шар піднявся з опори в ігровому світі й відкрив поверхню під ним, а не вибирає пункт інтерфейсу.

### Включає

Відгорнути паперове покриття платформи й відкрити пружну ділянку в оригінальній Tearaway для PS Vita.

### Виключає

Малювання й вирізання декоративної паперової форми; переставляння фрагмента мапи; автоматичне складання цілого моста; дотик задньою панеллю до вже відкритого барабана.

### Ігри-носії

- [`GAME-0426` — Tearaway](../games/s-z/tearaway.md)

## ACT-565

- Назва: Вдарити по барабану під посланцем задньою сенсорною панеллю
- Переглянуто: `2026-09-27`

### Операційне визначення

Гравець торкається ділянки задньої сенсорної панелі, що відповідає паперовому барабану, поки керований посланець перебуває на поверхні цього барабана, навмисно запитуючи підкидання замість покладання на автоматичний відскок від контакту.

### Включає

Гра на барабані дотиком до задньої сенсорної панелі, яка підкидає Iota або Atoi з позначеної барабанної мембрани в оригінальній Tearaway для PS Vita.

### Виключає

Автоматичний відскок від контакту (SYS-1056); незалежно доступну кнопку стрибка; поштовх заднім дотиком, що пересуває перешкоду; накази строю ритмічними фразами (ACT-560).

### Ігри-носії

- [`GAME-0426` — Tearaway](../games/s-z/tearaway.md)

## ACT-566

- Назва: Спрямовувати й за бажанням посилювати промінь переносного джерела світла проти захищеного темрявою ворога
- Переглянуто: `2026-09-27`

### Операційне визначення

Гравець наводить уже доступний промінь джерела світла в руках на захищеного темрявою противника й вибирає, чи утримувати посилення променя з витратою заряду, підтримуючи контакт променя з ціллю.

### Включає

Наведення та посилення ліхтарика Алана на Темного в оригінальній Xbox 360-версії Alan Wake.

### Виключає

Приховування світла перед разовим несподіваним викриттям (ACT-543); перемикання переносного джерела світла (ACT-409); стрільбу зі зброї (ACT-161); системний результат зняття покриву темряви світлом (SYS-1126).

### Ігри-носії

- [`GAME-0427` — Alan Wake](../games/a-f/alan-wake.md)

## ACT-567

- Назва: Розмістити або стерти елемент рівня в редакторі поза активною грою
- Переглянуто: `2026-09-27`

### Операційне визначення

У редакторі, де гравець сам визначає темп роботи, він вибирає доступний елемент рівня й розміщує його в обраній клітинці сітки або стирає вже розміщений елемент. Це змінює компонування для подальшого випробування, а не поточний світ керованого персонажа під час гри.

### Включає

Сенсорне розміщення звичайного блока ґрунту через палітру редактора або стирання такого блока за допомогою Wii U GamePad в оригінальній Super Mario Maker.

### Виключає

Розміщення утримуваного блока, підкріпленого запасом матеріалів, у межах досяжності персонажа в Minecraft Survival або Terraria (ACT-162); зміну зіткнень, поки триває активне пробне проходження; вільне редагування завантаженого рівня іншого автора для публікації.

### Ігри-носії

- [`GAME-0428` — Super Mario Maker](../games/s-z/super-mario-maker.md)

## ACT-568

- Назва: Перемкнути поточний створений рівень у пробну гру
- Переглянуто: `2026-09-27`

### Операційне визначення

Гравець свідомо перемикає поточний редагований рівень у режим пробного проходження з безпосереднім керуванням і, поки повернення ще доступне, повертається до редагування того самого рівня, не підтверджуючи завантаження в мережу.

### Включає

Елемент керування Trial Play на GamePad в оригінальній Wii U-версії Super Mario Maker.

### Виключає

Виконання зафіксованої автономної програми машини (TIM-006); вхід до не пов’язаного з поточним опублікованого рівня; твердження, що проба із середини рівня вже задовольняє окрему вимогу підтвердити його проходження автором перед публікацією.

### Ігри-носії

- [`GAME-0428` — Super Mario Maker](../games/s-z/super-mario-maker.md)

## ACT-569

- Назва: Націлити й виконати ривок Bash від допустимої опори
- Переглянуто: `2026-09-27`

### Операційне визначення

Коли поблизу є допустимий ворог, снаряд або створена рівнем опора, гравець утримує кнопку Bash, обирає напрям і відпускає її, щоб відштовхнути керованого персонажа від цієї цілі.

### Включає

Спрямувати ривок Орі від ліхтаря, ворога або ворожого снаряда під час підйому й втечі в дереві Ginso в оригінальній версії для Xbox One.

### Виключає

Звичайний стрибок чи стрибок від стіни; випуск нового снаряда; вибір далекої цілі для автоматичного пошуку шляху; окремий рух зачепленого снаряда в протилежний бік (`SYS-1131`).

### Ігри-носії

- [`GAME-0431` — Ori and the Blind Forest](../games/m-r/ori-and-the-blind-forest.md)

## ACT-570

- Назва: Створити Soul Link у вибраному місці
- Переглянуто: `2026-09-27`

### Операційне визначення

Гравець просить установити нову точку повернення в нинішньому допустимому місці персонажа й свідомо витрачає потрібний ресурс, а не чекає на фіксовану або автоматичну контрольну точку.

### Включає

Створити Soul Link для Орі в безпечному місці під час підйому деревом Ginso в оригінальній версії для Xbox One.

### Виключає

Використання фіксованого Духовного колодязя (`ACT-341`); автоматичний запис контрольної точки; історію збережень через меню з можливістю зберігатися будь-де; твердження, що точку можна створити без енергії чи в кожному небезпечному місці (`CON-708`).

### Ігри-носії

- [`GAME-0431` — Ori and the Blind Forest](../games/m-r/ori-and-the-blind-forest.md)

## ACT-571

- Назва: Подати спрямовану пісню дельфіна для обстеження чи відгуку гліфа
- Переглянуто: `2026-09-27`

### Операційне визначення

Гравець подає спрямовану пісню керованого дельфіна. Короткий імпульс спрямовується на сумісний гліф чи істоту поблизу, а відлуння утримуваного сигналу, що повернулося, можна читати як локальну сонарну мапу області перед дельфіном.

### Включає

Кнопка A для пісні Екко та карта за утримання кнопки в оригінальній Ecco the Dolphin для Genesis.

### Виключає

Сканування місцевості й вантажу Odradek (ACT-471); глобальну мапу, автоматично відкриту без введення гравця; звичайний атакувальний снаряд; припущення, що будь-яка пісня відкриває кожен гліф.

### Ігри-носії

- [`GAME-0656` — "Ecco the Dolphin: Defender of the Future"](../games/a-f/ecco-the-dolphin-defender-of-the-future.md)
- [`GAME-0433` — Ecco the Dolphin](../games/a-f/ecco-the-dolphin.md)

## ACT-572

- Назва: Виконувати вказаний кухонний жест на сенсорному екрані
- Переглянуто: `2026-09-27`

### Операційне визначення

Під час поточної кухонної мінігри гравець торкається продукту чи знаряддя або веде по ньому стилусом відповідно до вказівки. Це змінює стан підготовки одного кроку перед його оцінюванням.

### Включає

Натискання на ніж для рубання, проведення вздовж показаних ліній для нарізання тофу, нахиляння каструлі для бульйону стилусом і керування показаними елементами готування під час рецепта місо-супу в оригінальній DS-версії Cooking Mama.

### Виключає

Вибір цілого рецепта для виготовлення однією неподільною дією; роботу втіленого персонажа біля постійної алхімічної робочої станції (ACT-410); прикрашання без оцінюваного впливу на підготовку; припущення, що кожен жест використовує мікрофон.

### Ігри-носії

- [`GAME-0434` — Cooking Mama](../games/a-f/cooking-mama.md)

## ACT-573

- Назва: Подавати місцевий невербальний поклик тканині чи мандрівникові
- Переглянуто: `2026-09-27`

### Операційне визначення

Гравець свідомо подає від керованого мандрівника невербальний імпульс обмеженої дальності в навколишній простір, щоб допустима тканина могла відгукнутися, а інший мандрівник — сприйняти сигнал без використання текстового чи голосового каналу.

### Включає

Поклик біля тканини, яка опинилася в пастці, чи необов’язкового анонімного супутника в розділі Bridge оригінальної PlayStation 3-версії Journey.

### Виключає

Спрямований ехолот Екко та вивчену пісню для гліфа (ACT-571); розмову з партнером, який має ім’я; наказ партнерові рухатися; поповнення заряду від контакту без поклику.

### Ігри-носії

- [`GAME-0436` — Journey](../games/g-l/journey.md)

## ACT-574

- Назва: Саджати компанію гостей за вибраний придатний столик
- Переглянуто: `2026-09-28`

### Операційне визначення

Гравець обирає одну компанію, що зараз чекає, і переводить її до вибраного чистого, незайнятого столика з достатньою кількістю місць. Цей столик стає недоступним для інших компаній, доки посаджені гості не підуть і посуд не буде прибрано.

### Включає

Перетягування компанії від входу Flo's Diner до придатного столика в ранній зміні 1-2 режиму Career оригінальної Diner Dash для PC.

### Виключає

Автоматичне призначення місця системою; безпосереднє готування страви для компанії; пересаджування вже посаджених гостей; посадку за зайнятий, брудний або замалий столик.

### Ігри-носії

- [`GAME-0437` — Diner Dash](../games/a-f/diner-dash.md)

## ACT-575

- Назва: Керувати безперервним перенесенням ваги на дошці з датчиками
- Переглянуто: `2026-09-28`

### Операційне визначення

Стоячи на платформі з датчиками тиску, гравець навмисно переносить вагу вбік або вперед і назад. Дошка безперервно вимірює рівновагу, а її показник слугує вхідною командою для напряму або темпу поточної активності.

### Включає

Перенесення ваги ліворуч і праворуч, уперед і назад на зареєстрованій Wii Balance Board під час початкового лижного слалому в оригінальній Wii Fit.

### Виключає

Натискання кнопки напряму; змах пультом Wii Remote у руці; нахил віртуального ігрового поля стиком (ACT-519); вимірювання ваги лише для Body Test перед початком активності; стрибок на дошці.

### Ігри-носії

- [`GAME-0439` — Wii Fit](../games/s-z/wii-fit.md)

## ACT-576

- Назва: Подати обраний іменник для створення предмета у світі
- Переглянуто: `2026-09-28`

### Операційне визначення

Гравець вводить допустимий іменник у текстовому інтерфейсі гри й підтверджує цей вибір як запит на відповідний предмет у поточному світі, яким можна маніпулювати, а не вибирає його з фіксованого місцевого інвентарю.

### Включає

Уведення Lemonade в Notepad оригінальної DS-версії Scribblenauts, щоб створити напій для мандрівника в пустелі в головоломці 1-5 області The Gardens.

### Виключає

Пересувати готові текстові плитки, щоб переписати правило; обирати рецепт із меню; друкувати діалог без створення предмета; додавати прикметники з пізніших частин серії.

### Ігри-носії

- [`GAME-0440` — Scribblenauts](../games/s-z/scribblenauts.md)

## ACT-577

- Назва: Фізично переміщатися, змінюючи місце на ігровій карті
- Переглянуто: `2026-09-28`

### Операційне визначення

Гравець навмисно йде реальним світом, маючи при собі активний ігровий пристрій із визначенням місцеперебування. Фізична позиція стає введенням для ігрової мапи й доступних можливостей зустрічей поблизу.

### Включає

Безпечне пересування пішки з відкритим оригінальним Android-застосунком Pokémon GO станом на липень 2016 року, доки поблизу тренера на його карті не з’явиться дикий покемон.

### Виключає

Керування віртуальним персонажем стиком або сенсорним екраном (ACT-008); вибір місця призначення на мапі без подорожі; підміну координат пристрою; сам лише підрахунок кроків без просторово обмеженої доступності зустрічей.

### Ігри-носії

- [`GAME-0441` — Pokémon GO](../games/m-r/pokemon-go.md)

## ACT-578

- Назва: Розпушувати мотикою очищену клітину поля
- Переглянуто: `2026-09-28`

### Операційне визначення

Гравець спрямовує мотику на досяжну очищену клітину поля й перетворює звичайну землю на підготовлену для посіву клітину, стан якої зберігається.

### Включає

Підготовка клітинок для весняних культур на полі оригінальної PlayStation-версії Harvest Moon: Back to Nature після усунення бур’янів та уламків, що заважали.

### Виключає

Розсипання пакета насіння; полив наявної культури; видобування руди або об’єму місцевості; саме прибирання перешкоди.

### Ігри-носії

- [`GAME-0444` — "Harvest Moon: Back to Nature"](../games/g-l/harvest-moon-back-to-nature.md)

## ACT-579

- Назва: Розсипати один пакет насіння на фіксовану ділянку
- Переглянуто: `2026-09-28`

### Операційне визначення

Гравець застосовує один пакет насіння, який має при собі, у вибраній позиції поля; пакет одразу розподіляє насіння на своїй фіксованій навколишній ділянці замість послідовного засівання по одній вибраній клітинці.

### Включає

Розсипання пакета з дев’ятьма насінинами на ділянці 3 × 3 у весняному полі оригінальної PlayStation-версії Harvest Moon: Back to Nature.

### Виключає

Підготовку ґрунту мотикою; полив або збирання окремих рослин (ACT-213); вільний вибір окремого місця для насіння в кожній із дев’яти позицій; припущення, що насіння на необробленому мотикою ґрунті приживеться.

### Ігри-носії

- [`GAME-0444` — "Harvest Moon: Back to Nature"](../games/g-l/harvest-moon-back-to-nature.md)

## ACT-580

- Назва: Замикати траєкторію польоту навколо предметів
- Переглянуто: `2026-09-28`

### Операційне визначення

Гравець скеровує керованого летючого персонажа по замкненій траєкторії, яка охоплює доступні предмети й збирає їх без окремого дотику до кожного.

### Включає

Петлю Paraloop навколо синіх або зоряних фішок у першому етапі (Mare) сну Spring Valley оригінальної NiGHTS into Dreams для Sega Saturn.

### Виключає

Простий проліт крізь кільце; прямий дотик до однієї фішки (SYS-037); малювання довільної постійної перешкоди; петлю, призначену лише для бою.

### Ігри-носії

- [`GAME-0445` — "NiGHTS into Dreams"](../games/m-r/nights-into-dreams.md)

## ACT-581

- Назва: Витрачати запас шкали польоту, утримуючи свердлильний ривок
- Переглянуто: `2026-09-28`

### Операційне визначення

Під час польоту гравець утримує команду свердління, прискорюючи кероване тіло й витрачаючи скінченний запас шкали атаки, доки відпускання команди або вичерпання запасу не припинить цей прискорений свердлильний рух.

### Включає

Утримування Drill Attack Найтса під час першого Mare у Spring Valley на оригінальному диску для Saturn.

### Виключає

Звичайне напрямлене пересування в польоті (ACT-008); постійний режим швидкості; поповнення шкали кільцем (SYS-1168).

### Ігри-носії

- [`GAME-0445` — "NiGHTS into Dreams"](../games/m-r/nights-into-dreams.md)

## ACT-582

- Назва: Прокладати оплачувану колію з урахуванням ухилу
- Переглянуто: `2026-10-05`

### Операційне визначення

Гравець прокладає зв’язані відрізки колії обраною місцевістю, сплачуючи за рейки й мости; отриманий ухил згодом впливає на рух поїзда.

### Включає

Першу лінію Слау—Оксфорд у вступному сценарії оригінальної Railroad Tycoon II для ПК.

### Виключає

Задання впорядкованих зупинок поїзда (ACT-584); розміщення станції (ACT-583); абстрактні транспортні лінії, прокладені між наперед наявними вузлами.

### Ігри-носії

- [`GAME-0446` — Railroad Tycoon II](../games/m-r/railroad-tycoon-ii.md)
- [`GAME-0498` — Transport Fever 2](../games/s-z/transport-fever-2.md)

## ACT-583

- Назва: Розміщувати станцію на колії із зоною обслуговування
- Переглянуто: `2026-09-28`

### Операційне визначення

Гравець розміщує станцію вибраного розміру на зв’язаній колії й створює показану зону обслуговування навколишніх виробників, споживачів і будинків.

### Включає

Станції Слау й Оксфорда у вступному сценарії оригінальної Railroad Tycoon II для ПК.

### Виключає

Саме прокладання колії повз підприємство; подальше підбирання вантажу транспортом; станційні поліпшення водопостачання, подачі піску або обслуговування в локомотивному депо.

### Ігри-носії

- [`GAME-0446` — Railroad Tycoon II](../games/m-r/railroad-tycoon-ii.md)

## ACT-584

- Назва: Задавати послідовність зупинок і склад поїзда
- Переглянуто: `2026-09-28`

### Операційне визначення

Гравець призначає поїзду впорядковані станції та окремо для кожної задає дозволені вантажні й пасажирські вагони й умову очікування перед відправленням для повторюваного автоматичного рейсу.

### Включає

Вовну й пасажирів у Слау, пасажирів і товари в Оксфорді та жовтий і зелений сигнали очікування у вступному сценарії.

### Виключає

Ручне керування поїздом; купівлю паровоза; зміну колії чи зони станції; гарантію товару на першому поверненні.

### Ігри-носії

- [`GAME-0446` — Railroad Tycoon II](../games/m-r/railroad-tycoon-ii.md)

## ACT-585

- Назва: Засновувати компанію з власним і зовнішнім капіталом
- Переглянуто: `2026-09-28`

### Операційне визначення

Гравець вкладає особисті кошти та залучає зовнішніх інвесторів, щоб утворити скарбницю керованої компанії; частка власності засновника залежить від розподілу внесків.

### Включає

Заснування залізниці до будівництва колії у вступному сценарії оригінальної Railroad Tycoon II для ПК.

### Виключає

Подальшу виплату дивідендів; купівлю локомотива з уже наявних коштів компанії; прирівнювання всього залученого капіталу компанії до особистого статку засновника.

### Ігри-носії

- [`GAME-0446` — Railroad Tycoon II](../games/m-r/railroad-tycoon-ii.md)

## ACT-586

- Назва: Багаторазово натискати кнопки, щоб підвестися під відлік рефері
- Переглянуто: `2026-09-28`

### Операційне визначення

Після того як керованого боксера збили з ніг, гравець багаторазово натискає кнопки відновлення, щоб той підвівся, перш ніж рефері дорахує до десяти.

### Включає

Повторне натискання A і B після падіння Малого Мака у версії Punch-Out!! Featuring Mr. Dream для NES.

### Виключає

Звичайний удар стоячи; автоматичне підведення без дій гравця; перемогу в бою самим лише підведенням.

### Ігри-носії

- [`GAME-0447` — Punch-Out!!](../games/m-r/punch-out.md)

## ACT-587

- Назва: Один раз відновити витривалість між раундами
- Переглянуто: `2026-09-28`

### Операційне визначення

Під час допустимої перерви між раундами гравець подає команду на часткове відновлення витривалості; це відновлення доступне лише один раз за весь бій.

### Включає

Натискання SELECT між раундами за Малого Мака у версії Punch-Out!! Featuring Mr. Dream для NES.

### Виключає

Повторне натискання A й B, щоб підвестися під відлік рефері; відновлення сердець; необмежене відновлення після кожного раунду.

### Ігри-носії

- [`GAME-0447` — Punch-Out!!](../games/m-r/punch-out.md)

## ACT-588

- Назва: Проводити пальцем для повороту, стрибка або підкату під час автоматичного бігу
- Переглянуто: `2026-09-28`

### Операційне визначення

Поки рух уперед триває без команди пересування, гравець виконує один напрямлений сенсорний змах, який контекст поточного шляху тлумачить як поворот на чверть оберту, стрибок або підкат.

### Включає

Повороти ліворуч і праворуч на кутах та змахи вгору й униз для стрибка й підкату протягом однієї спроби оригінальної iPhone-версії Temple Run.

### Виключає

Нахил для поперечного вирівнювання за лінією монет (ACT-589); зупинку бігуна; необмежене пересування довільною геометрією світу (ACT-008); пізніше керування геймпадом.

### Ігри-носії

- [`GAME-0448` — Temple Run](../games/s-z/temple-run.md)

## ACT-589

- Назва: Нахилом зміщувати героя поперек шляху під час автоматичного бігу
- Переглянуто: `2026-09-28`

### Операційне визначення

Гравець змінює бічний нахил телефона, щоб зміщувати бігуна, який автоматично просувається вперед, у межах ширини поточного коридору, не вибираючи нового напрямку й не перериваючи руху вперед.

### Включає

Вирівнювання бігуна оригінальної iPhone-версії Temple Run за необов’язковим рядом монет, поки він ще наближається до кута.

### Виключає

Дискретний змах ліворуч чи праворуч для повороту на 90 градусів (ACT-588); нахил цілого фізичного ігрового поля (ACT-519); перемикання між трьома смугами змахами в пізніших іграх із бігом.

### Ігри-носії

- [`GAME-0448` — Temple Run](../games/s-z/temple-run.md)

## ACT-590

- Назва: Замінити єдиного активного помічника поруч із незмінним головним персонажем
- Переглянуто: `2026-09-28`

### Операційне визначення

Під час бою з незмінним головним персонажем гравець вибирає іншого залученого допустимого помічника для єдиної активної комірки партнера, змінюючи команди помічника без заміни головного персонажа.

### Включає

Перемикання між Купером і Гумбаріо поруч із Маріо в сутичці з чотирма Fuzzy в оригінальній Nintendo 64-версії Paper Mario.

### Виключає

Заміну єдиного покемона, який б’ється (ACT-258); додавання ще одного одночасного помічника; спорядження значка.

### Ігри-носії

- [`GAME-0449` — Paper Mario](../games/m-r/paper-mario.md)

## ACT-591

- Назва: Поміняти порядок двох союзних дій до їх виконання
- Переглянуто: `2026-09-28`

### Операційне визначення

Перш ніж будь-хто з двох союзних учасників витратить свою дію поточного ходу, гравець міняє, хто з них діє першим, не змінюючи дозволеної кількості їхніх дій.

### Включає

Натискання Z, щоб Купер діяв перед Маріо в оригінальній Paper Mario для Nintendo 64.

### Виключає

Зміну порядку після дії будь-кого з цих двох учасників; надання додаткового ходу; упорядкування всіх бійців показниками ініціативи.

### Ігри-носії

- [`GAME-0449` — Paper Mario](../games/m-r/paper-mario.md)

## ACT-592

- Назва: Натиснути перед самим влучанням, щоб зменшити шкоду в покроковому бою
- Переглянуто: `2026-09-28`

### Операційне визначення

Після того як ворог зафіксував атаку в покроковому бою, гравець натискає захисну кнопку безпосередньо перед контактом, щоб запросити зменшення вхідної шкоди.

### Включає

Натискання A безпосередньо перед ударом Fuzzy по Маріо в оригінальній Nintendo 64-версії Paper Mario.

### Виключає

Атакувальні Action Commands (ACT-222); ухилення, парирування або стрибок для нейтралізації атаки й контратаки (ACT-223); пасивний захист.

### Ігри-носії

- [`GAME-0449` — Paper Mario](../games/m-r/paper-mario.md)
- [`GAME-0714` — "Thirsty Suitors"](../games/s-z/thirsty-suitors.md)

## ACT-593

- Назва: Виконати й завершити повітряний трюк на сноуборді
- Переглянуто: `2026-09-28`

### Операційне визначення

Після стрибка на сноуборді гравець обирає та утримує допустимий захват дошки або обертання в повітрі, а потім відпускає прийом перед запланованим приземленням, щоб гра могла оцінити трюк.

### Включає

Захват дошки чи обертання в межах заїзду Race на Garibaldi в оригінальній SSX Tricky.

### Виключає

Керування наземною траєкторією; автоматичний трюк; продовження зв’язаного скейтбордного ланцюга з балансуванням типу Manual, зокрема Nose Manual, чи ковзанням по поручню (ACT-500); очки без приземлення.

### Ігри-носії

- [`GAME-0450` — SSX Tricky](../games/s-z/ssx-tricky.md)

## ACT-594

- Назва: Витратити адреналін на швидкість спуску
- Переглянуто: `2026-09-28`

### Операційне визначення

Під час спуску гравець запитує додаткову швидкість уперед із поточного скінченного запасу адреналіну; сама команда не нараховує цей запас і не визначає його вичерпання.

### Включає

Витрачання заробленого адреналіну в заїзді Race на Garibaldi в оригінальній SSX Tricky.

### Виключає

Звичайне прискорення на схилі; нарахування запасу шкали за трюки; постійно активний модифікатор; прискорення транспортного засобу з витратою запасу шкали виживання при пошкодженнях (ACT-309 разом із SYS-1040).

### Ігри-носії

- [`GAME-0450` — SSX Tricky](../games/s-z/ssx-tricky.md)

## ACT-595

- Назва: Дістати чи сховати обрану зброю
- Переглянуто: `2026-09-30`

### Операційне визначення

Гравець явно переводить поточну вибрану зброю між готовим станом у руках і прибраним станом, не підмінюючи її іншою зброєю з інвентарю; це займає або звільняє руки для інших завдань.

### Включає

Дістати чи сховати пістолети Лари на рівні Caves оригінальної Tomb Raider для PlayStation.

### Виключає

Вибір іншої зброї з інвентарю; автоматичну готовність; прицілювання чи постріл; суто декоративне спорядження без зміни допустимих взаємодій.

### Ігри-носії

- [`GAME-0501` — F.E.A.R.](../games/a-f/fear.md)
- [`GAME-0451` — Tomb Raider (1996)](../games/s-z/tomb-raider-1996.md)
- [`GAME-0499` — Vagrant Story](../games/s-z/vagrant-story.md)

## ACT-596

- Назва: Вручну утримуватися за уступ і вибрати пересування вбік, підтягування або відпускання
- Переглянуто: `2026-09-30`

### Операційне визначення

Біля досяжного сумісного краю гравець утримує команду прикріплення, щоб зачепитися й утримувати тіло у висі, подає команду пересування вбік або підтягування чи відпускає захоплення, щоб від’єднатися. Правило не вимагає захоплення з витратою витривалості.

### Включає

Захоплення уступу Ларою з утриманням команди дії, пересування вбік, підтягування й навмисне падіння в оригінальній Tomb Raider.

### Виключає

Захоплення довільної поверхні з витратою витривалості (ACT-362); автоматичну анімацію драбини; дві незалежно прив’язані до керування руки (ACT-114); пристрій для зачеплення й підтягування.

### Ігри-носії

- [`GAME-0451` — Tomb Raider (1996)](../games/s-z/tomb-raider-1996.md)

## ACT-597

- Назва: Повернути камеру за героя й тимчасово оглянути оточення
- Переглянуто: `2026-09-30`

### Операційне визначення

Гравець запитує ракурс безпосередньо позаду керованого тіла або утримує команду огляду й спрямовує огляд на геометрію поблизу. Відпускання повертає звичайний ракурс стеження, не змінюючи геометрії ігрового світу.

### Включає

Повернення камери за Лару та спрямований огляд з утриманням команди в оригінальній Tomb Raider.

### Виключає

Обертання камери, проєкція якого визначає правила (ACT-095); зміну світу залежно від видимості (ACT-098); команду прицілювання для атаки; курсор у застиглій сцені доказів.

### Ігри-носії

- [`GAME-0485` — Shenmue](../games/s-z/shenmue.md)
- [`GAME-0451` — Tomb Raider (1996)](../games/s-z/tomb-raider-1996.md)

## ACT-598

- Назва: Призначити працівників на поклоніння для виробництва ресурсу
- Переглянуто: `2026-09-30`

### Операційне визначення

Гравець наказує допустимим власним працівникам залишатися біля сумісного місця поклоніння замість збирання з родовища на мапі, виділяючи робочу силу для процесу надходження ресурсу божества.

### Включає

Грецькі селяни моляться біля храму в оригінальній Age of Mythology.

### Виключає

Пасивний дохід самої будівлі; збирання вичерпного матеріалу на місцевості; вибір покровителя нової доби.

### Ігри-носії

- [`GAME-0453` — Age of Mythology](../games/a-f/age-of-mythology.md)
- [`GAME-0570` — Cult of the Lamb](../games/a-f/cult-of-the-lamb.md)

## ACT-599

- Назва: Застосовувати відкриту силу на рівні цивілізації
- Переглянуто: `2026-09-30`

### Операційне визначення

Гравець вибирає доступну силу рівня цивілізації й підтверджує її дозволену локальну ціль або глобальну активацію, не наказуючи окремому керованому бійцеві застосувати здібність.

### Включає

Блискавка Зевса або сила обраного молодшого бога, доступна один раз за матч в оригінальній Age of Mythology.

### Виключає

Здібність окремого героя; звичайна атака; пасивна властивість бога; вибір наступного покровителя.

### Ігри-носії

- [`GAME-0453` — Age of Mythology](../games/a-f/age-of-mythology.md)
- [`GAME-0480` — Populous](../games/m-r/populous.md)

## ACT-600

- Назва: Розмістити одиниці в гарнізоні придатної будівлі або вивести їх
- Переглянуто: `2026-09-30`

### Операційне визначення

Гравець наказує допустимим власним одиницям увійти до гарнізону будівлі, яка може їх прийняти й утримувати, або запитує їх вихід у досяжний зовнішній простір.

### Включає

Укриття селян чи піхоти й виведення їх із будівлі в оригінальній Age of Mythology.

### Виключає

Посадку в рухомий транспорт; зведення будівлі; автоматичне укриття без команди; внесення артефакту.

### Ігри-носії

- [`GAME-0453` — Age of Mythology](../games/a-f/age-of-mythology.md)

## ACT-601

- Назва: Внести артефакт, який переносять, до установи, що його приймає
- Переглянуто: `2026-09-30`

### Операційне визначення

Гравець наказує допустимому носієві окремого артефакту, який той несе, помістити його до сумісної власної установи, а не залишати при носієві.

### Включає

Грецький герой в оригінальній Age of Mythology приносить реліквію до храму.

### Виключає

Підбирання артефакту; передачу предмета персонажу на його прохання; оплату дослідження; просте наближення до будівлі.

### Ігри-носії

- [`GAME-0453` — Age of Mythology](../games/a-f/age-of-mythology.md)

## ACT-602

- Назва: Призначити торговця на маршрут повернення від установи до бази під час гри
- Переглянуто: `2026-09-30`

### Операційне визначення

Гравець призначає власну торгову одиницю з допустимої торгової установи до сумісного пункту призначення на базі, задаючи повторювану подорож із поверненням, що відбувається безпосередньо під час гри.

### Включає

Призначення караванів на маршрут між ринком і центром міста в оригінальній Age of Mythology.

### Виключає

Покрокові міські торгові маршрути з обмеженою кількістю комірок імперії; складені накази щодо корабельного вантажу для кожного порту; миттєву купівлю товару.

### Ігри-носії

- [`GAME-0453` — Age of Mythology](../games/a-f/age-of-mythology.md)

## ACT-603

- Назва: Виконувати швидкий жест із відривом для ритмічної відповіді
- Переглянуто: `2026-09-30`

### Операційне визначення

Гравець готує сенсорний контакт, виконує швидкий напрямлений рух і відпускає дотик, щоб подати відповідь на задану авторами музичну подію, яка наближається, вибираючи її час, а не довільну ціль у світі.

### Включає

Змах стилусом угору, який посилає стрижень до двох пластин, що наближаються, у першій звичайній мінігрі Built to Scale оригінальної DS-версії Rhythm Heaven.

### Виключає

Сам дотик, який не супроводжується рухом і відривом; контекстний навігаційний змах; проведення ліній для завдання з їжею чи кухонним знаряддям; відтворення кнопкових символів викладача; довільне прицілювання снарядом.

### Ігри-носії

- [`GAME-0454` — Rhythm Heaven](../games/m-r/rhythm-heaven.md)

## ACT-604

- Назва: Починати заряджання зброї чи обирати альтернативне скасування
- Переглянуто: `2026-09-30`

### Операційне визначення

Гравець починає заряджання зброї на місці комбінованою командою й вибирає тривале заряджання або оголошену гілку його скасування, щоб запросити різні подальші ефекти атаки, а не негайно вдарити чи витратити накопичений запас шкали.

### Включає

Утримання Soul Charge та його скасування кнопкою захисту, описані в оригінальному посібнику Namco для Dreamcast.

### Виключає

Удар самого персонажа; вибір звичайної стійки зброї; витрачання сучасної шкали потужного прийому; заряджання снаряда для вибору сили пострілу; пасивне посилення від спорядження.

### Ігри-носії

- [`GAME-0455` — Soulcalibur](../games/s-z/soulcalibur.md)

## ACT-605

- Назва: Просити допустиме відновлення після падіння чи хитання
- Переглянуто: `2026-09-30`

### Операційне визначення

Коли боєць лежить, летить до приземлення або хитається від удару, гравець просить допустиме в цьому стані швидке підведення, перекат на землі чи повторює введення для відновлення, щоб раніше повернути керування або змінити форму підведення.

### Включає

Перекати лежачи, підготовка Quick Roll утриманням захисту й повторні команди виходу з хитання в оригінальній Soulcalibur для Dreamcast.

### Виключає

Звичайну ходьбу чи напрямлене переміщення в повітрі; присідання вже керованого бійця; сам удар під час підведення; пасивне очікування підведення; відновлення здоров’я предметом.

### Ігри-носії

- [`GAME-0546` — Burning Rangers](../games/a-f/burning-rangers.md)
- [`GAME-0494` — Dead or Alive 2](../games/a-f/dead-or-alive-2.md)
- [`GAME-0455` — Soulcalibur](../games/s-z/soulcalibur.md)

## ACT-606

- Назва: Обирати сталу дію для спільної кнопки
- Переглянуто: `2026-09-30`

### Операційне визначення

Гравець обирає доступну дію персонажа або перенесеного предмета; вона лишається значенням спільної кнопки дії у світі до вибору іншої допустимої дії чи предмета. Вибір відокремлений від подальшого виконання щодо світу.

### Включає

Вибір Fight, Open/Search, Push або допустимої операції з перенесеним предметом через Options у DOS-грі Alone in the Dark.

### Виключає

Негайне виконання одноразового пункту меню; лише вибір предмета зі швидкої комірки; редагування програми віддаленого агента.

### Ігри-носії

- [`GAME-0456` — Alone in the Dark](../games/a-f/alone-in-the-dark.md)

## ACT-607

- Назва: Випускати перенесену річ назад у світ
- Переглянуто: `2026-09-30`

### Операційне визначення

Гравець явно кладе або кидає окрему перенесену річ, прибираючи її з інвентарю й просячи розміщення в доступному навколишньому просторі; це саме по собі не знищує її тотожність.

### Включає

Вибір Drop або Throw для листа, книги, покривала чи порожньої каністри для оливи, які персонаж несе із собою, у грі Alone in the Dark.

### Виключає

Знищення чи споживання предмета; кидання атакувального знаряддя, яке повертається; скидання командного спорядження в межах раунду; постріл боєприпасом зі зброї.

### Ігри-носії

- [`GAME-0456` — Alone in the Dark](../games/a-f/alone-in-the-dark.md)
- [`GAME-0500` — Pacific Drive](../games/m-r/pacific-drive.md)

## ACT-608

- Назва: Обирати наданий автомобіль і режим коробки передач
- Переглянуто: `2026-09-30`

### Операційне визначення

Перед скінченною спробою водіння гравець підтверджує один наданий варіант автомобіля та трансмісії з відкритого фіксованого набору. Вибір призначає цей автомобіль і ручний або автоматичний профіль керування без купівлі чи володіння гаражною колекцією.

### Включає

Вибір Celica або Delta з ручним чи автоматичним перемиканням в оригінальній Sega Rally Championship.

### Виключає

Вибір активного автомобіля з власної колекції; зміну складності суперників оператором; перемикання передачі під час активного водіння; купівлю або налаштування транспортного засобу.

### Ігри-носії

- [`GAME-0551` — "R4: Ridge Racer Type 4"](../games/m-r/ridge-racer-type-4.md)
- [`GAME-0457` — Sega Rally Championship](../games/s-z/sega-rally-championship.md)

## ACT-609

- Назва: Перемикати сталі ракурси водіння
- Переглянуто: `2026-10-03`

### Операційне визначення

Під час прямого керування транспортом гравець перемикає визначені вид із кабіни й зовнішній вид позаду, зберігаючи стан транспорту та керування рухом; це вибір видимості, а не зміна правил світу.

### Включає

Перемикання View Change між Driver’s Eye та View from Behind в оригінальній Sega Rally Championship.

### Виключає

Обертання ракурсу, що змінює фізичну можливість; зміну керованих суб’єктів; автоматичне стеження камери; вільне переміщення камери світу.

### Ігри-носії

- [`GAME-0507` — MotorStorm](../games/m-r/motorstorm.md)
- [`GAME-0551` — "R4: Ridge Racer Type 4"](../games/m-r/ridge-racer-type-4.md)
- [`GAME-0457` — Sega Rally Championship](../games/s-z/sega-rally-championship.md)
- [`GAME-0488` — wipEout](../games/s-z/wipeout.md)

## ACT-610

- Назва: Змінювати ракурс камери навколо безпосередньо керованого актора
- Переглянуто: `2026-10-13`

### Операційне визначення

Продовжуючи безпосередньо керувати актором світу, гравець наказує камері слідування змінити відстань або кут огляду, щоб раніше закриті близькі геометрія чи загрози стали видимими перед наступним вибором руху.

### Включає

Кнопки C для камери Лакіту під час першого підйому в Bob-omb Battlefield оригінальної Super Mario 64 для Nintendo 64.

### Виключає

Обертання ракурсу, що змінює допустимий шлях у світі через проєкційне суміщення (ACT-095); автоматичний ракурс катсцени; сталі альтернативні ракурси водіння (ACT-609); переміщення карти чи ігрового предмета, а не кадру камери.

### Ігри-носії

- [`GAME-0539` — Blast Corps](../games/a-f/blast-corps.md)
- [`GAME-0546` — Burning Rangers](../games/a-f/burning-rangers.md)
- [`GAME-0552` — Jusant](../games/g-l/jusant.md)
- [`GAME-0507` — MotorStorm](../games/m-r/motorstorm.md)
- [`GAME-0505` — Panzer Dragoon](../games/m-r/panzer-dragoon.md)
- [`GAME-0472` — Sonic Adventure](../games/s-z/sonic-adventure.md)
- [`GAME-0548` — Space Station Silicon Valley](../games/s-z/space-station-silicon-valley.md)
- [`GAME-0460` — Super Mario 64](../games/s-z/super-mario-64.md)

## ACT-611

- Назва: Підняти й кинути живого супротивника
- Переглянуто: `2026-09-30`

### Операційне визначення

Гравець наближається до допустимого активного супротивника з потрібного боку, піднімає його в утримуваний стан і окремою командою кидає назад на арену, де той і далі є учасником бою.

### Включає

Підійти до Великого Боб-омба ззаду, підняти його й кинути на вершині в оригінальній Super Mario 64.

### Виключає

Підбирання неживого вільного предмета; миттєвий кидок у файтингу без фази утримання; перенесення непритомного тіла; пізніше розкручування Боузера за хвіст.

### Ігри-носії

- [`GAME-0560` — Gunstar Heroes](../games/g-l/gunstar-heroes.md)
- [`GAME-0607` — "Mischief Makers"](../games/m-r/mischief-makers.md)
- [`GAME-0460` — Super Mario 64](../games/s-z/super-mario-64.md)
- [`GAME-0497` — Wario Land 4](../games/s-z/wario-land-4.md)

## ACT-612

- Назва: Зорієнтувати й розмістити придбаний предмет домашньої обстановки
- Переглянуто: `2026-09-30`

### Операційне визначення

У призупиненому режимі облаштування будинку гравець обирає просторовий поворот і місце придбаного предмета, змінюючи можливі подальші дії мешканців і шляхи до нього, але не виконуючи ці дії.

### Включає

Розміщення доступного за ціною стільця після вибору в режимі купівлі оригінальної The Sims і повернення до режиму життя, щоб перевірити доступ до нього й відновлення комфорту.

### Виключає

Сплату купівельної ціни (ACT-130); наказ мешканцеві використати стілець (ACT-257); спорудження стін у Build Mode; автоматичне розміщення без вибору місця гравцем.

### Ігри-носії

- [`GAME-0461` — The Sims](../games/s-z/the-sims.md)

## ACT-613

- Назва: Увійти у фізичну гілку маршруту під час гри
- Переглянуто: `2026-10-01`

### Операційне визначення

Керуючи персонажем біля видимого розгалуження, гравець заходить у один із доступних проходів або транспортних входів і цим обирає наступну авторську частину етапу без окремої мапи вузлів.

### Включає

Стрибок у човен замість входу на корабель на розгалуженні Metal Slug 3; далі човен везе персонажа вниз за течією.

### Виключає

Вибір відкритого вузла мапи (ACT-127); вибір вихідного ребра ігрового поля під час руху на кількість клітинок, визначену кубиком (ACT-530); керування транспортом після входу; невидимий автоматичний перехід етапу без вибору гілки гравцем.

### Ігри-носії

- [`GAME-0462` — Metal Slug 3](../games/m-r/metal-slug-3.md)
- [`GAME-0587` — Panzer Dragoon II Zwei](../games/m-r/panzer-dragoon-ii-zwei.md)

## ACT-614

- Назва: Пожертвувати зайнятою гравцем бойовою машиною в спрямованій атаці
- Переглянуто: `2026-10-01`

### Операційне визначення

Перебуваючи в допустимій бойовій машині, гравець подає окрему комбіновану команду й спрямовує цю машину в атаку зі шкодою та самознищенням. Він назавжди втрачає її поточний стан замість збереження керування після влучання.

### Включає

Атака Metal Slug Attack командою A+B в оригінальній Metal Slug 3 проти досяжного ворожого згруповання або охоронця першого етапу.

### Виключає

Звичайну стрільбу з установленої вогнепальної зброї; випадковий вибух машини після ворожих влучань; таран із можливістю відновлення (ACT-379); дистанційний підрив залишеного без нагляду об’єкта.

### Ігри-носії

- [`GAME-0462` — Metal Slug 3](../games/m-r/metal-slug-3.md)

## ACT-615

- Назва: Відпускати прицільний кидок після руху контролером
- Переглянуто: `2026-10-01`

### Операційне визначення

Гравець указує на ціль в ігровому світі, утримує кнопку кидка, фізично змахує контролером і відпускає кнопку, щоб кинути один предмет. Початкова сила його удару залежить від виміряного руху контролера.

### Включає

У Boom Blox для оригінальної Wii гравець указує на опору, утримує A, змахує Wii Remote вперед і відпускає A, щоб кинути бейсбольний м’яч.

### Виключає

Запуск із нерухомої рогатки чи верхньої пускової установки відпусканням натиснення (ACT-113); подачу кулі в боулінгу для котіння доріжкою (ACT-499); керування м’ячем після випуску; захоплення й перетягування вже розміщеного блока.

### Ігри-носії

- [`GAME-0465` — Boom Blox](../games/a-f/boom-blox.md)

## ACT-616

- Назва: Обходити камерою нерухому споруду для вибору лінії кидка
- Переглянуто: `2026-10-01`

### Операційне визначення

Перед спрямованою фізичною дією гравець обертає ракурс навколо нерухомої тривимірної споруди, щоб відкрити іншу поверхню й вибрати іншу незакриту лінію атаки. Сам рух камери не переміщує споруду.

### Включає

У пазлі Warrior гри Boom Blox утримання B та рух Wii Remote дають оглянути опору спереду або ззаду перед прицільним кидком.

### Виключає

Обертання перспективи для переписування геометрії допустимого пересування (ACT-095); зміну ракурсу камери, що супроводжує безпосередньо керованого учасника (ACT-610); перемикання між фіксованими ракурсами з кабіни та камери стеження (ACT-609); обертання самої конструкції з блоків.

### Ігри-носії

- [`GAME-0465` — Boom Blox](../games/a-f/boom-blox.md)
- [`GAME-0657` — "Spire Blast"](../games/s-z/spire-blast.md)

## ACT-617

- Назва: Вчасно відповідати на перешкоду стрічки кнопкою чи парою
- Переглянуто: `2026-10-13`

### Операційне визначення

Поки безперервний маршрут несе персонажа до видимої перешкоди певного типу, гравець у мить зустрічі натискає прив’язану до цього типу кнопку контролера або одночасну пару прив’язаних кнопок для однієї складеної перешкоди, щоб спробувати пройти її.

### Включає

В оригінальній Vib-Ribbon для PlayStation блок потребує L1, петля — R1, провалля — напрямку вниз, хвиля — X, а сполучення блока з проваллям — L1 і напрямку вниз разом.

### Виключає

Повторення фрази викладача (ACT-533); кроки по панелях підлоги за картою кроків (ACT-545); відповідь для складання конструкції швидким дотиковим змахом із відривом (ACT-603); дві окремо розташовані перешкоди, що потребують послідовних, а не одночасних введень.

### Ігри-носії

- [`GAME-0467` — Vib-Ribbon](../games/s-z/vib-ribbon.md)

## ACT-618

- Назва: Націлити й почати падіння за власним напрямком тяжіння
- Переглянуто: `2026-10-01`

### Операційне визначення

Керуючи персонажем у повітрі, гравець звільняє його від звичної сили тяжіння, наводить новий особистий напрямок униз на видиму поверхню й починає падіння в цей бік. До приземлення зміну можна призупинити або скасувати.

### Включає

Кет зависає, наводиться стиком або рухом консолі, падає до бічної поверхні вежі й скасовує зміну, повертаючись до звичайного напрямку вниз, в оригінальній PS Vita-версії Gravity Rush.

### Виключає

Вибір однієї ортогональної поверхні для переорієнтації системи відліку тяжіння всього світу (ACT-097); пасивний стрибок або звичайний біг уперед; рух камери без зміни падіння персонажа.

### Ігри-носії

- [`GAME-0468` — Gravity Rush](../games/g-l/gravity-rush.md)

## ACT-619

- Назва: Почати удар ногою за допомогою націленого гравітаційного падіння
- Переглянуто: `2026-10-01`

### Операційне визначення

Після входу в стан гравітаційного зависання з наведенням гравець вирівнює персонажа в повітрі з ворожою ціллю й підтверджує удар самого персонажа ногою, що використовує спрямоване падіння для наближення та зіткнення.

### Включає

Кет наводиться на неві із зависання й натискає кнопку атаки, щоб почати гравітаційний удар в оригінальній Gravity Rush для PS Vita.

### Виключає

Звичайний удар ногою стоячи (ACT-295); зміну тяжіння лише для пересування (ACT-618); автоматично випущений самонавідний снаряд; припущення про гарантоване влучання за невдалого наведення.

### Ігри-носії

- [`GAME-0468` — Gravity Rush](../games/g-l/gravity-rush.md)

## ACT-620

- Назва: Керувати уламком власного авто під час Impact Time після аварії
- Переглянуто: `2026-10-01`

### Операційне визначення

Після аварії автомобіля, яким гравець безпосередньо керував, коли звичайне кермування вже завершилося, він утримує доступну лише після аварії команду сповільнення й спрямовує уламок, що ще рухається, до досяжного суперника, перш ніж короткий стан зіткнення завершиться.

### Включає

Утримування R1 і керування уламком лівим стиком PS2 для спроби Aftertouch Takedown у першому заїзді Race на Silver Lake оригінальної Burnout 3: Takedown.

### Виключає

Керування неушкодженим гоночним автомобілем (ACT-290); звичайну витрату Boost (ACT-309); підрив уламка в Crash Mode; гарантію Takedown без контакту.

### Ігри-носії

- [`GAME-0470` — "Burnout 3: Takedown"](../games/a-f/burnout-3-takedown.md)

## ACT-621

- Назва: Провести вибраним хірургічним інструментом по цільовому шляху на тканині
- Переглянуто: `2026-10-02`

### Операційне визначення

Гравець вибирає доступний хірургічний інструмент і проводить стилусом відповідний цьому інструментові рух по поточній цільовій тканині, щоб спробувати лікування або закриття.

### Включає

Зигзагоподібне накладання швів голкою, нанесення гелю, розріз скальпелем за напрямною лінією та рух для накладання пов’язки в першій операції оригінальної DS-версії Trauma Center: Under the Knife.

### Виключає

Довільне малювання без інструмента; реальну медичну практику; сенсорні жести приготування їжі (ACT-572); перенесення щипцями (ACT-622).

### Ігри-носії

- [`GAME-0471` — 'Trauma Center: Under the Knife'](../games/s-z/trauma-center-under-the-knife.md)

## ACT-622

- Назва: Вийняти застряглий об’єкт щипцями й покласти в лоток
- Переглянуто: `2026-10-02`

### Операційне визначення

Захопити щипцями відкритий застряглий об’єкт, перетягнути його допустимим шляхом виймання й покласти в призначений лоток, щоб завершити вилучення.

### Включає

Видалення зовнішніх і внутрішніх уламків скла в першій операції оригінальної Trauma Center для DS.

### Виключає

Автоматичне підбирання дотиком; витягування проти напрямку входження; обробку рани після уламка; реальну медичну пораду.

### Ігри-носії

- [`GAME-0471` — 'Trauma Center: Under the Knife'](../games/s-z/trauma-center-under-the-knife.md)

## ACT-623

- Назва: У повітрі атакувати допустиму ціль або виконати ривок уперед
- Переглянуто: `2026-10-02`

### Операційне визначення

Поки керований персонаж уже перебуває в повітрі, гравець натисканням викликає передбачену команду атаки чи стрибка, щоб запросити спрямований удар по одній близькій допустимій цілі; без допустимої цілі та сама команда натомість запитує ривок уперед у повітрі.

### Включає

Homing Attack Соніка проти близького робота під час першого сюжетного відвідування Emerald Coast та альтернативний Jump Dash, коли жодного робота немає в межах досяжності, в оригінальній Dreamcast-версії Sonic Adventure.

### Виключає

Завжди націлений снаряд; звичайний перший стрибок або наземне обертання (ACT-295); поліпшений Light Speed Dash уздовж кілець; гарантоване влучання без системного опрацювання цілі.

### Ігри-носії

- [`GAME-0472` — Sonic Adventure](../games/s-z/sonic-adventure.md)

## ACT-624

- Назва: Стрибати з кожної досягнутої пронумерованої панелі маршруту
- Переглянуто: `2026-10-02`

### Операційне визначення

Діставшись поточної допустимої пронумерованої панелі в заданому авторами ланцюгу пересування, гравець вчасно подає команду стрибка для наступного допоміжного підкидання, а не просто стоїть на панелі чи погоджується на одну безперервну автоматичну поїздку.

### Включає

Послідовні стрибки Соніка з п’яти пронумерованих панелей під час першого сюжетного відвідування Emerald Coast в оригінальній Dreamcast-версії.

### Виключає

Звичайний стрибок без стану панелі (ACT-008); автоматичне спрацювання пружини від контакту (SYS-1056); вибір довільного пронумерованого пункту призначення поза чергою; покрокову числову головоломку.

### Ігри-носії

- [`GAME-0472` — Sonic Adventure](../games/s-z/sonic-adventure.md)

## ACT-625

- Назва: Стріляти поза екраном, щоб поповнити магазин
- Переглянуто: `2026-10-13`

### Операційне визначення

Тримаючи аркадний пістолет, який визначає наведення за дисплеєм, гравець навмисно наводить його поза активним екраном і натискає на гачок, щоб запросити повне перезарядження магазина незалежно від влучання в ціль світу чи витрачання переносного запасу набоїв.

### Включає

Перезаряджання натисканням на гачок поза екраном оригінального аркадного пістолета Model 2 The House of the Dead у Tragedy.

### Виключає

Прицільний постріл на екрані (ACT-490); перенесення набоїв із запасу до магазина (ACT-183); автоматичне поповнення за захисної педалі (SYS-1160); перезаряджання клавіатурою чи мишею на PC або зброю пізнішої гри серії.

### Ігри-носії

- [`GAME-0475` — The House of the Dead](../games/s-z/the-house-of-the-dead.md)

## ACT-626

- Назва: Бігти на місці для руху маршрутом
- Переглянуто: `2026-10-02`

### Операційне визначення

Повторювати бігові рухи ногою із закріпленим датчиком, щоб гра приймала їх як команду просувати персонажа вперед поточним авторським курсом.

### Включає

Проходження раннього маршруту в стандартному режимі оригінальної Nintendo Switch-версії Ring Fit Adventure.

### Виключає

Натискання кнопки напряму для ходьби; перенесення ваги стоячи на Balance Board (ACT-575); пересування присіданнями в Silent Mode; припущення, що персонаж просувається, поки гравець стоїть нерухомо.

### Ігри-носії

- [`GAME-0476` — Ring Fit Adventure](../games/m-r/ring-fit-adventure.md)

## ACT-627

- Назва: Стискати або розтягувати кільце для дії на маршруті
- Переглянуто: `2026-10-02`

### Операційне визначення

Гравець наводить гнучке кільце, яке тримає в руках, на допустиму локальну особливість маршруту й фізично стискає або розтягує його, запитуючи повітряний струмінь чи всмоктування, а не бойову вправу Fit Skill.

### Включає

Прицілений повітряний струмінь Ring-Con для стрибка чи взаємодії з допустимою перешкодою та потягування для всмоктування предметів поблизу під час маршруту оригінальної Ring Fit Adventure.

### Виключає

Абстрактний постріл снарядом кнопкою; бойову вправу за вказівками (ACT-628); Ab Guard (ACT-629); гарантію наявності кожної перешкоди чи предмета в дослідженому маршруті.

### Ігри-носії

- [`GAME-0476` — Ring Fit Adventure](../games/m-r/ring-fit-adventure.md)

## ACT-628

- Назва: Виконувати показані повтори вибраної бойової вправи
- Переглянуто: `2026-10-02`

### Операційне визначення

Після вибору доступної бойової вправи гравець дотримується показаної пози тіла й виконує потрібний рух або утримання протягом повторів із підказками, щоб подати одну атаку Fit Skill.

### Включає

Перша звичайна сутичка в ранній частині режиму Adventure оригінальної Ring Fit Adventure з рухами тіла, які зчитуються через Ring-Con та Leg Strap.

### Виключає

Сам вибір вправи без її виконання; покрокові атаки лише кнопкою; твердження про фіксовану кількість повторів або про конкретну пізніше розблоковану вправу для першої сутички.

### Ігри-носії

- [`GAME-0476` — Ring Fit Adventure](../games/m-r/ring-fit-adventure.md)

## ACT-629

- Назва: Тримати стиснуте кільце біля живота для захисту
- Переглянуто: `2026-10-02`

### Операційне визначення

На час ворожої атаки прикласти гнучке кільце до живота, стиснути та не відпускати до завершення удару, щоб виконати захист Ab Guard.

### Включає

Захист під час ходів ворога на ранньому етапі режиму Adventure Mode в оригінальній Ring Fit Adventure.

### Виключає

Постійний пасивний щит; захист тільки кнопкою (`ACT-437`); повний захист після передчасного відпускання; гарантовану відсутність шкоди.

### Ігри-носії

- [`GAME-0476` — Ring Fit Adventure](../games/m-r/ring-fit-adventure.md)

## ACT-630

- Назва: Витягнути до себе один сусідній блок
- Переглянуто: `2026-10-02`

### Операційне визначення

Із досяжного боку одного рухомого блока гравець хапає його й кроком або спрямуванням переміщує до керованого тіла на одну локальну позицію, відкриваючи чи переміщуючи поверхню, придатну для наступного просторового рішення.

### Включає

Вінсент витягує звичайний блок із вежі першого Nightmare — Underground Cemetery, щоб створити сходинку заввишки в один блок, в оригінальній Catherine.

### Виключає

Штовхання блока від себе (ACT-009); перетягування предмета інвентарю без зміни топології лазіння; твердження про те, які типи особливих блоків з’являються в цьому першому рівні.

### Ігри-носії

- [`GAME-0477` — Catherine](../games/a-f/catherine.md)

## ACT-631

- Назва: Скасувати один допустимий нещодавній рух у Nightmare
- Переглянуто: `2026-10-02`

### Операційне визначення

За налаштування складності, яке дозволяє команду, гравець запитує скасування одного допустимого нещодавнього локального руху або дії з блоком, щоб одразу спробувати інше продовження.

### Включає

Скасування ходу на складності Normal, описане в посібнику Atlus для оригінальної Catherine під час нічного підйому.

### Виключає

Перезапуск усього етапу; необмежене перемотування вздовж неперервної часової шкали (ACT-044); твердження про виміряне повернення минулого часу руйнування або про прив’язку кнопки певної платформи.

### Ігри-носії

- [`GAME-0477` — Catherine](../games/a-f/catherine.md)

## ACT-632

- Назва: Обрати доступний рейс між містами
- Переглянуто: `2026-10-02`

### Операційне визначення

У поточному місті вибрати один відомий і запропонований рейс до іншого міста, погодившись із пунктом прибуття, умовами відправлення й ціною замість покроково керувати пересуванням.

### Включає

Вибір доступного рейсу з Парижа в оригінальній 80 Days для iOS.

### Виключає

Вибір вузла з позначеним видом сутички на карті серії забігів (`ACT-127`); місцеве прокладання шляху персонажу (`ACT-096`); малювання сполучень між довільними містами; припущення, що всі рейси відомі відразу.

### Ігри-носії

- [`GAME-0478` — 80 Days](../games/0-9/80-days.md)

## ACT-633

- Назва: Схопити рухому ліану й відпустити її
- Переглянуто: `2026-10-02`

### Операційне визначення

Стрибком із досяжної землі прикріпити кероване тіло до ліани, що вже гойдається, а окремою командою відпустити її та повернутися до руху без прикріплення у вибраному положенні гойдання.

### Включає

Захоплення ліани Гаррі стрибком із розбігу та відпускання рухом джойстика вниз в оригінальній Pitfall! для Atari 2600.

### Виключає

Створення чи наведення троса; зміну його довжини; планерування (`ACT-479`); автоматичне перенесення без вибору моменту захоплення чи відпускання.

### Ігри-носії

- [`GAME-0479` — Pitfall!](../games/m-r/pitfall.md)

## ACT-634

- Назва: Підняти або опустити одну вказану точку землі
- Переглянуто: `2026-10-02`

### Операційне визначення

гравець обирає дозволену місцеву точку землі й піднімає або опускає її на один дозволений крок, змінюючи зв’язану землю для автономних поселенців, а не добуваючи матеріал.

### Включає

зміни висоти кнопками миші біля дружніх людей в оригінальній Populous для Amiga.

### Виключає

видобування матеріалу (`ACT-443`); руйнування бойового укриття; силу зміни рівня моря в усьому світі.

### Ігри-носії

- [`GAME-0480` — Populous](../games/m-r/populous.md)

## ACT-635

- Назва: Задати одну поведінкову настанову всій автономній людності
- Переглянуто: `2026-10-02`

### Операційне визначення

гравець задає всій дружній автономній людності настанову оселятися, збиратися й потім оселятися, битися й потім оселятися або йти до свого притягувача, разом із зазначеною запасною поведінкою, замість окремих маршрутів кожному.

### Включає

чотири настанови Populous; під час руху до магніту люди не оселяються.

### Виключає

роль одного вибраного агента (`ACT-036`); стрій чи бойову позицію (`ACT-317`); безпосереднє керування вождем.

### Ігри-носії

- [`GAME-0480` — Populous](../games/m-r/populous.md)

## ACT-636

- Назва: Перенести притягувач людності за наявності вождя
- Переглянуто: `2026-10-02`

### Операційне визначення

за наявності придатного єдиного вождя гравець переносить притягувач людності до обраного місця, змінюючи напрям руху вождя й послідовників за чинною настановою збору, без безпосереднього пересування людей.

### Включає

перенесення папського магніту в оригінальній Populous.

### Виключає

рух власного персонажа; необмежене перенесення без вождя; системну зміну вождя після втрати.

### Ігри-носії

- [`GAME-0480` — Populous](../games/m-r/populous.md)

## ACT-637

- Назва: Підштовхувати весь ґрунт, щоб підкинути його мешканців
- Переглянуто: `2026-10-02`

### Операційне визначення

гравець подає загальний поштовх ґрунту, який підкидає фізичних мешканців на ньому, замість прямої команди стрибка вибраному персонажу.

### Включає

Одночасне натискання плечових кнопок у LocoRoco.

### Виключає

прямий стрибок персонажа; запуск одного приціленого снаряда; виміряну силу поштовху.

### Ігри-носії

- [`GAME-0717` — "LocoRoco 2"](../games/g-l/locoroco-2.md)
- [`GAME-0482` — LocoRoco](../games/g-l/locoroco.md)

## ACT-638

- Назва: Просити поділ живої сукупності або возз’єднання сусідніх істот
- Переглянуто: `2026-10-02`

### Операційне визначення

гравець просить живу сукупність поділитися на окремі фізичні тіла або сусідніх істот возз’єднатися в одне тіло, змінюючи прохідну форму без розподілу місць військового загону.

### Включає

Коротке натискання для поділу та утримання для возз’єднання в LocoRoco.

### Виключає

автоматичне числове злиття лише від зіткнення; віддалене перенесення; призначення складу загону.

### Ігри-носії

- [`GAME-0717` — "LocoRoco 2"](../games/g-l/locoroco-2.md)
- [`GAME-0482` — LocoRoco](../games/g-l/locoroco.md)

## ACT-639

- Назва: Окремо призначати боєприпаси двом стріляючим стволам
- Переглянуто: `2026-10-02`

### Операційне визначення

гравець окремо призначає доступний тип боєприпасів кожному з двох незалежно стріляючих стволів, зберігаючи обидва призначення замість заміни одного загального активного предмета.

### Включає

Ліве й праве заряджання арбалета в оригінальній Xbox-грі Stranger's Wrath.

### Виключає

вибір одного активного предмета; поліпшення зброї; постріл із уже зарядженого ствола.

### Ігри-носії

- [`GAME-0483` — "Oddworld: Stranger's Wrath"](../games/m-r/oddworld-strangers-wrath.md)

## ACT-640

- Назва: Змінювати тілесну перспективу разом із можливостями бою й пересування
- Переглянуто: `2026-10-02`

### Операційне визначення

гравець перемикається між режимами від першої та третьої особи, у яких різні дозволені способи використання зброї, огляду й швидкого пересування змінюють доступні рішення для того самого персонажа.

### Включає

Огляд з арбалетом проти швидкого руху й близького захоплення від третьої особи в оригінальній Stranger's Wrath.

### Виключає

лише декоративне обертання камери; зміну керованого персонажа; саму зміну пози.

### Ігри-носії

- [`GAME-0483` — "Oddworld: Stranger's Wrath"](../games/m-r/oddworld-strangers-wrath.md)

## ACT-641

- Назва: Утримувати команду близького забирання тіла заради винагороди
- Переглянуто: `2026-10-02`

### Операційне визначення

гравець повертається до допустимого близького знешкодженого або мертвого тіла й утримує команду забирання, доки процес захоплення не завершиться або спроба не втратить допустимість.

### Включає

Утримання команди Bounty Can в оригінальній грі про Незнайомця.

### Виключає

кидання пристрою ймовірнісного приєднання істоти; перенесення цілого тіла в інше місце; лише оглушення цілі.

### Ігри-носії

- [`GAME-0483` — "Oddworld: Stranger's Wrath"](../games/m-r/oddworld-strangers-wrath.md)

## ACT-642

- Назва: Просити особисте лікування коштом сил, а не запасеного засобу
- Переглянуто: `2026-10-02`

### Операційне визначення

гравець просить дію особистого відновлення на місці, система якої перетворює поточний запас сил на здоров’я замість споживання запасеного лікувального засобу чи очікування автоматичного відновлення здоров’я.

### Включає

Оригінальну команду Незнайомця струсити ушкодження.

### Виключає

витратний лікувальний засіб; обробку вибраної рани; автоматичне відновлення здоров’я в тихий проміжок.

### Ігри-носії

- [`GAME-0483` — "Oddworld: Stranger's Wrath"](../games/m-r/oddworld-strangers-wrath.md)

## ACT-643

- Назва: Прицілюватися й запускати заряджену живу істоту у світ
- Переглянуто: `2026-10-02`

### Операційне визначення

гравець прицілюється й вистрілює зарядженою живою істотою у ворога, дику істоту, сумісний пристрій або поверхню розміщення, обираючи просторовий ефект істоти замість обмеження всіх запусків ушкодженням ворога.

### Включає

Прицілені запуски Zappfly, Chippunk, Bolamite, Stunkz і Fuzzle в оригінальній Stranger's Wrath.

### Виключає

кидання інертного каменя чи підготовленої гранати; автоматичні укуси після розміщення; окрему ручну команду на кожен подальший укус.

### Ігри-носії

- [`GAME-0483` — "Oddworld: Stranger's Wrath"](../games/m-r/oddworld-strangers-wrath.md)

## ACT-644

- Назва: Маніпулювати копіями фрагментів у просторі віддзеркалення, зміни кольору й накладання
- Переглянуто: `2026-10-02`

### Операційне визначення

гравець обирає збережений фрагмент чи часткове поєднання, пересуває робочу копію, віддзеркалює її горизонтально або вертикально, змінює колір, накладає на іншу чи прибирає з показу без стирання збереженої пам’яті.

### Включає

Маніпулювання фрагментами перфокарт у кишеньковому комп’ютері Impossible Mission.

### Виключає

переставляння мапи світу; пакування інвентарю з обмеженою місткістю; вільне обертання предмета у світі.

### Ігри-носії

- [`GAME-0484` — Impossible Mission](../games/g-l/impossible-mission.md)

## ACT-645

- Назва: Скасовувати останнє допустиме прибирання чи поєднання фрагментів
- Переглянуто: `2026-10-02`

### Операційне визначення

гравець просить скасувати останнє допустиме прибирання або поєднання в просторі головоломки, повертаючи попереднє місцеве розміщення фрагментів, а не відмотуючи перебіг місії.

### Включає

Виправлення недавнього прибирання чи поєднання клавішею зі знаком оклику в Impossible Mission.

### Виключає

безперервне обернення симуляції; перезапуск усієї місії; довільні давніші зміни.

### Ігри-носії

- [`GAME-0484` — Impossible Mission](../games/g-l/impossible-mission.md)

## ACT-646

- Назва: Просити допомогу з головоломкою коштом залишку місійного часу
- Переглянуто: `2026-10-02`

### Операційне визначення

гравець обирає додаткову допомогу, яка забирає фіксовану частину залишку місійного часу й або правильно орієнтує вказані фрагменти, або повідомляє, чи вже знайдено потрібні до них частини.

### Включає

Телефонний запит до Агентства в Impossible Mission щодо орієнтації або наявності відповідних частин.

### Виключає

купівлю підказки за валюту; автоматичну навчальну пораду; безплатний необмежений розв’язувач.

### Ігри-носії

- [`GAME-0484` — Impossible Mission](../games/g-l/impossible-mission.md)

## ACT-647

- Назва: Відповідати на показані місця нот у порядку зростання висоти
- Переглянуто: `2026-10-02`

### Операційне визначення

почувши й побачивши набір місць, пов’язаних із нотами, гравець обирає ці місця в порядку зростання висоти звуку, а не повторює порядок показу.

### Включає

Вибір квадратів від низьких нот до високих у кодовій кімнаті Impossible Mission.

### Виключає

повторення початкового порядку, як у Simon; вибір невпорядкованого набору; ритмічне натискання в момент кожного початкового сигналу.

### Ігри-носії

- [`GAME-0484` — Impossible Mission](../games/g-l/impossible-mission.md)

## ACT-648

- Назва: Керувати вертикальним рухом підйомника, стоячи на його платформі
- Переглянуто: `2026-10-02`

### Операційне визначення

гравець стоїть на допустимій платформі підйомника й утримує вертикальну команду, керуючи дозволеним рухом угору чи вниз разом із персонажем.

### Включає

Кімнатні підйомники й рух ліфтом в Impossible Mission.

### Виключає

автоматичний рух платформи від віддаленого перемикача; стрибок персонажа без руху підйомника; телепортацію.

### Ігри-носії

- [`GAME-0484` — Impossible Mission](../games/g-l/impossible-mission.md)
- [`GAME-0553` — The Lost Vikings](../games/s-z/the-lost-vikings.md)

## ACT-649

- Назва: Відповідати на поточну тимчасову команду в живій сцені
- Переглянуто: `2026-10-02`

### Операційне визначення

Під час заданої автором живої сцени гравець натискає команду, яку зараз показує тимчасова підказка, щоб викликати наступну передбачену реакцію, а не обирає довільно спрямовану бойову дію чи відтворює раніше показану послідовність із пам’яті.

### Включає

Відповіді на Quick Timer Event у провулку та барі Heartbeats оригінальної Shenmue.

### Виключає

Зміну ефекту обраної покрокової атаки; перекриття рухомого покажчика; пригадування послідовності після показу; вибір прийому у вільному бою.

### Ігри-носії

- [`GAME-0485` — Shenmue](../games/s-z/shenmue.md)

## ACT-650

- Назва: Обирати дозволений сон у спальні для завершення дня розслідування
- Переглянуто: `2026-10-02`

### Операційне визначення

Коли поточний час дозволяє сон у спальні, гравець обирає цю команду завершення дня й продовжує розслідування наступної дати без вимоги заявленої особистої шкали втоми.

### Включає

Дозволений вибір Sleep у спальні Рьо в оригінальній Shenmue.

### Виключає

Сон виживальника за станом утоми; створення нової щоденної головоломки; вільне перемотування до будь-якого часу зустрічі.

### Ігри-носії

- [`GAME-0523` — Pentiment](../games/m-r/pentiment.md)
- [`GAME-0485` — Shenmue](../games/s-z/shenmue.md)

## ACT-651

- Назва: Обирати доступний склад і розміщувати його на дозволених початкових клітинках
- Переглянуто: `2026-10-02`

### Операційне визначення

Перед дискретною тактичною сутичкою гравець обирає допустимих учасників резерву в межах бойової групи й розміщує кожного на дозволеній початковій клітинці до запуску бойового розкладу.

### Включає

Розміщення бойової групи Гаріланда в оригінальній Final Fantasy Tactics.

### Виключає

Ширину формації в бою реального часу; рух після початку; появу підкріплень; довільних додаткових керованих гостей.

### Ігри-носії

- [`GAME-0486` — Final Fantasy Tactics](../games/a-f/final-fantasy-tactics.md)

## ACT-652

- Назва: Завершувати особистий хід із невикористаними можливостями руху чи дії
- Переглянуто: `2026-10-02`

### Операційне визначення

Гравець свідомо завершує хід активного персонажа й відмовляється від невикористаної окремої можливості руху чи дії, зокрема від обох, замість обов’язково витрачати їх.

### Включає

Wait в оригінальній Final Fantasy Tactics із невикористаною однією чи обома можливостями.

### Виключає

Живий таймер очікування; гарантоване захисне підсилення; скидання всієї готовності до нуля; другий рух.

### Ігри-носії

- [`GAME-0486` — Final Fantasy Tactics](../games/a-f/final-fantasy-tactics.md)
- [`GAME-0514` — Mewgenics](../games/m-r/mewgenics.md)
- [`GAME-0618` — Shining Force III](../games/s-z/shining-force-iii.md)

## ACT-653

- Назва: Обирати кінцевий напрямок персонажа під час завершення тактичного ходу
- Переглянуто: `2026-10-02`

### Операційне визначення

Наприкінці особистого тактичного ходу гравець фіксує напрямок персонажа з дозволеного набору без переміщення; він визначає напрямок подальшого захисту.

### Включає

Вибір напрямку наприкінці активного ходу оригінальної Final Fantasy Tactics.

### Виключає

Поворот камери; розворот між двома напрямками як витратну бойову дію; лише автоматичний напрямок після руху.

### Ігри-носії

- [`GAME-0486` — Final Fantasy Tactics](../games/a-f/final-fantasy-tactics.md)

## ACT-654

- Назва: Змінювати огляд незмінного тактичного поля без зміни його топології
- Переглянуто: `2026-10-02`

### Операційне визначення

Гравець змінює точку огляду незмінного тактичного поля, щоб роздивитися клітинки й висоти; справжні позиції, суміжність і досяжність лишаються незмінними.

### Включає

Керування оглядом поля оригінальної Final Fantasy Tactics.

### Виключає

Шляхи, залежні від перспективи; поворот світу зі зміною суміжності; камеру супроводу безпосередньо керованого героя.

### Ігри-носії

- [`GAME-0486` — Final Fantasy Tactics](../games/a-f/final-fantasy-tactics.md)
- [`GAME-0575` — Metal Gear Acid](../games/m-r/metal-gear-acid.md)

## ACT-655

- Назва: Обирати збережений повний чи зарифлений стан бойових вітрил
- Переглянуто: `2026-10-03`

### Операційне визначення

Гравець перемикає бойове вітрильне судно між доступними станами вітрил, які діють до наступної зміни; швидкість обмінюється на керованість і вразливість, а не отримує миттєве підсилення.

### Включає

Звичайна морська сутичка оригінальної Windows-гри Sid Meier's Pirates!. Рифлення сповільнює судно, але поліпшує керованість і зменшує вразливість вітрил.

### Виключає

Декоративне вітрило; особистий перехід до окремої снасті; тимчасове прискорення; автоматичний маршрут до призначення.

### Ігри-носії

- [`GAME-0487` — Sid Meier's Pirates!](../games/s-z/sid-meiers-pirates.md)

## ACT-656

- Назва: Запитувати доступний залп заряджених бортових гармат
- Переглянуто: `2026-10-03`

### Операційне визначення

Гравець запитує вогонь заряджених бортових гармат; поточне розташування цілей визначає допустимий борт і найближчого допустимого противника, а частково заряджена батарея може стріляти без очікування всіх гармат.

### Включає

Звичайна морська сутичка оригінальної Windows-гри Sid Meier's Pirates!. Команда вогню використовує заряджені гармати борту, зверненого до допустимої цілі.

### Виключає

Постріл із носової гармати; особистий вибір цілі башти; автоматичну стрільбу; обов’язкове заряджання всієї батареї.

### Ігри-носії

- [`GAME-0487` — Sid Meier's Pirates!](../games/s-z/sid-meiers-pirates.md)

## ACT-657

- Назва: Обирати доступні боєприпаси для автоматичного заряджання гармат
- Переглянуто: `2026-10-03`

### Операційне визначення

Гравець змінює тип боєприпасів автоматичного заряджання суднових гармат серед типів, доступних за поточним оснащенням, без особистого заряджання кожної гармати чи купівлі озброєння всередині сутички.

### Включає

Звичайна морська сутичка оригінальної Windows-гри Sid Meier's Pirates!. За наявності оснащення ядра, книпелі й картеч мають різну дальність і переважне пошкодження.

### Виключає

Особисте перезаряджання кожної гармати; купівлю поліпшення; вибір недоступного боєприпасу; окремий ген на кожну назву.

### Ігри-носії

- [`GAME-0487` — Sid Meier's Pirates!](../games/s-z/sid-meiers-pirates.md)

## ACT-658

- Назва: Виконувати живу захисну відповідь за типом атаки в дуелі
- Переглянуто: `2026-10-03`

### Операційне визначення

Гравець виконує доступне пригинання, стрибок чи перехоплення зброєю проти вхідної ближньої атаки, обираючи тип відповіді під час продовження дуелі замість універсального невразливого ухилення.

### Включає

Звичайна морська сутичка оригінальної Windows-гри Sid Meier's Pirates!. Пригинання зупиняє верхній удар; стрибок — нижній; парирування повністю зупиняє випад.

### Виключає

Автоматичний захисний кидок; універсальне ухилення; одну підказану кнопку контратаки; вільний рух ареною.

### Ігри-носії

- [`GAME-0487` — Sid Meier's Pirates!](../games/s-z/sid-meiers-pirates.md)

## ACT-659

- Назва: Пробувати переривану насмішку для зміни переваги дуелі
- Переглянуто: `2026-10-03`

### Операційне визначення

Гравець пробує живу насмішку без прямого пошкодження, завершення якої може змістити ініціативу до персонажа; удар противника може перервати її.

### Включає

Звичайна морська сутичка оригінальної Windows-гри Sid Meier's Pirates!. Завершена насмішка поліпшує перевагу, але вхідний удар може її зупинити.

### Виключає

Декоративну розмову; гарантоване підсилення; команду атакувального пошкодження; меню залякування без часу.

### Ігри-носії

- [`GAME-0487` — Sid Meier's Pirates!](../games/s-z/sid-meiers-pirates.md)

## ACT-660

- Назва: Обирати необов’язкові захоплені ресурси під час розподілу трофея
- Переглянуто: `2026-10-03`

### Операційне визначення

Після захоплення судна гравець приймає чи залишає запропонованих звичайних моряків, обирає кількість вантажу й вирішує, чи зберігати судно, за поточною допустимістю замість автоматичного отримання всіх трофейних ресурсів.

### Включає

Звичайна морська сутичка оригінальної Windows-гри Sid Meier's Pirates!. Захоплений вантаж і збереження судна обираються; від запропонованих моряків можна відмовитися.

### Виключає

Купівлю в крамниці; вибір золота, що переходить автоматично; здобич потоплення; розподіл здобичі всієї кампанії.

### Ігри-носії

- [`GAME-0487` — Sid Meier's Pirates!](../games/s-z/sid-meiers-pirates.md)

## ACT-661

- Назва: Запитувати готовий стан чи очікування власного приєднаного духа
- Переглянуто: `2026-10-04`

### Операційне визначення

Гравець запитує перехід власного духа між приєднаним готовим станом і очікуванням: залишає пасивний внесок або готує духа до подальшого спільного виклику; у бою зміна займає заплановану дію персонажа.

### Включає

Приєднання власного джина чи переведення в очікування бойовою командою оригінальної Golden Sun.

### Виключає

Передавання власника під час бою; звичайна прицільна атака; використання духа, який ще відновлюється; миттєве бойове перемикання без витрати дії.

### Ігри-носії

- [`GAME-0489` — Golden Sun](../games/g-l/golden-sun.md)

## ACT-662

- Назва: Випускати помічника зі спільного місця для предмета
- Переглянуто: `2026-10-04`

### Операційне визначення

Гравець активує помічника, якого носить як предмет, і розміщує його стійке автономне тіло в доступному просторі світу; помічник звільняє спільне місце для предмета й пізніше знову підбирається фізично, а не відкликається з окремого списку загону.

### Включає

Випускання Roadkill з одного із трьох спільних місць Sketch для предметів в оригінальній Comix Zone.

### Виключає

Дистанційне відкликання супутника загону; призначення місця руху автономній істоті; остаточне витрачання помічника; передачу прямого керування персонажем.

### Ігри-носії

- [`GAME-0490` — Comix Zone](../games/a-f/comix-zone.md)

## ACT-663

- Назва: Готувати ракету, захоплювати чи скасовувати її ціль
- Переглянуто: `2026-10-04`

### Операційне визначення

Гравець готує власну ракету до наведення на доступний корабель у поточному прицілі або свідомо скасовує підготовку чи збережену ціль до окремої команди пострілу; наведення зберігає саму ціль і не потребує безперервного утримання команди.

### Включає

Підготовку T, захоплення цілі в прицілі й скасування U в оригінальній BBC Micro Elite.

### Виключає

Безперервне утримання цілі для відносного руху; утримання прицілу заради шкали поступового наведення; автоматичний постріл при появі цілі; застосування протиракетного засобу.

### Ігри-носії

- [`GAME-0491` — Elite](../games/a-f/elite.md)

## ACT-664

- Назва: Запитувати умовне скорочення місцевої просторової відстані
- Переглянуто: `2026-10-04`

### Операційне визначення

Гравець запитує одноразове негайне скорочення відстані вперед за поточним напрямком корабля; команда відрізняється від вибору іншої зоряної системи й залежить від допустимості місцевих мас та середовища.

### Включає

Місцевий стрибок J за поточним напрямком польоту в оригінальній BBC Micro Elite.

### Виключає

Паливний гіперперехід між системами; саме збільшення швидкості; автоматичне стикування; необмежене перенесення в будь-яку точку.

### Ігри-носії

- [`GAME-0491` — Elite](../games/a-f/elite.md)

## ACT-665

- Назва: Прикріплювати мітку наведення або утримувати неживий якір боєприпасів
- Переглянуто: `2026-10-04`

### Операційне визначення

Гравець стріляє скінченною міткою в досяжну живу ціль або утримує її прикріплення на неживій поверхні як якір наступних набоїв; команда позначення відокремлена від витрати основних набоїв і перенаведення збережених пострілів наступною прийнятою міткою цілі.

### Включає

Позначення цілі Bullseye та утримане розміщення пастки на землі чи поверхні в оригінальній Resistance.

### Виключає

Саме прицілювання; озброєння власної ракети для набуття цілі в прицілі; автономну турель; необмежене позначення всіх прихованих ворогів.

### Ігри-носії

- [`GAME-0492` — "Resistance: Fall of Man"](../games/m-r/resistance-fall-of-man.md)

## ACT-666

- Назва: Рухом пальця вирізати допустимий ґрунт для водного маршруту
- Переглянуто: `2026-10-04`

### Операційне визначення

Гравець обирає неперервний рух по екрану, що прибирає перетнутий допустимий ґрунт і відкриває вільний простір; так змінюються канали для рідини, що рухається опосередковано, без вибору її швидкості чи кінцевої позиції.

### Включає

Вирізання рухом пальця коричневого ґрунту навколо незмінного каміння в оригінальному Choose Wisely у Where’s My Water?.

### Виключає

Видобування клітинок місцевості персонажем; удари лопатою в пошуку закопаного предмета; збирання матеріалу в інвентар; вириття бойового укриття; перетягування самої води.

### Ігри-носії

- [`GAME-0493` — Where's My Water?](../games/s-z/wheres-my-water.md)

## ACT-667

- Назва: Дмухати на сумісну місцеву ціль
- Переглянуто: `2026-10-04`

### Операційне визначення

Гравець наказує безпосередньо керованому персонажу дмухнути на придатну близьку ціль довкілля, щоб викликати її визначену місцеву відповідь, не стріляючи зі зброї.

### Включає

Амброзія та сумісні квіти Jungle Hijinxs в оригінальній Wii-версії, на які дмухають присіданням і струшуванням.

### Виключає

Постріл снарядом; автоматичне поле вітру; дмухання на будь-який об’єкт без перевірки придатності.

### Ігри-носії

- [`GAME-0495` — Donkey Kong Country Returns](../games/a-f/donkey-kong-country-returns.md)

## ACT-668

- Назва: Обрати мить пострілу із зайнятої заданої пускової установки
- Переглянуто: `2026-10-04`

### Операційне визначення

Коли керований персонаж перебуває в придатній заданій пусковій установці, гравець безпосередньо обирає мить запуску за авторським маршрутом, не задаючи довільного прицілу чи сили.

### Включає

Постріл із позначеної стрілкою Barrel Cannon після A в Jungle Hijinxs оригінальної Wii-версії.

### Виключає

Автоматичний запуск за входу; довільний балістичний приціл або сила; постріл з екіпірованої зброї.

### Ігри-носії

- [`GAME-0495` — Donkey Kong Country Returns](../games/a-f/donkey-kong-country-returns.md)
- [`GAME-0537` — Kirby Tilt 'n' Tumble](../games/g-l/kirby-tilt-n-tumble.md)

## ACT-669

- Назва: Виконувати позначений спрямований постріл у відповідь
- Переглянуто: `2026-10-04`

### Операційне визначення

Гравець натискає команду стрільби, коли допустима жива ціль має тимчасову позначку для удару у відповідь; це виконує спрямований у ціль контекстний постріл без вільного прицілювання саме цього пострілу.

### Включає

Gun Strike після допустимого точного захисту чи відштовхування важким ударом у сольному пролозі Space Marine 2.

### Виключає

Звичайну прицільну стрільбу; ближнє добивання; захисну дію, що створила позначку; автоматичну шкоду без команди.

### Ігри-носії

- [`GAME-0496` — "Warhammer 40,000: Space Marine 2"](../games/s-z/warhammer-40000-space-marine-2.md)

## ACT-670

- Назва: Змінювати огляд, який безпосередньо перевіряє задане завдання
- Переглянуто: `2026-10-05`

### Операційне визначення

Гравець змінює оглядову камеру або вмикає доступний вид поїздки на транспорті; задане завдання перевіряє цю зміну огляду як умову завершення, не надаючи прямого керування транспортом і не змінюючи геометрії світу.

### Включає

Початкову інструкцію камери й прийняте додаткове завдання поїздки в Mining Miracle релізної Transport Fever 2.

### Виключає

Лише косметичну зміну огляду без перевірки умови; геометрію шляху, керовану проєкцією; пряме кермування; вигадану ручну дію махання.

### Ігри-носії

- [`GAME-0498` — Transport Fever 2](../games/s-z/transport-fever-2.md)

## ACT-671

- Назва: Складати локомотив і вантажні або пасажирські вагони перед купівлею
- Переглянуто: `2026-10-05`

### Операційне визначення

Перед підтвердженням купівлі поїзда гравець обирає його рушійну одиницю й допустимі причеплені вагони, змінюючи запропоновані можливості перевезення, місткість, довжину та ціну, а не задаючи інший склад окремо для кожної зупинки.

### Включає

Складання локомотива з вагонами для руди або пасажирів у вікні купівлі депо релізної Transport Fever 2.

### Виключає

Призначення вже купленого поїзда на лінію; заміну вагонів на кожній зупинці; пізнішу функцію зміни вже придбаного складу; пряме керування транспортом.

### Ігри-носії

- [`GAME-0498` — Transport Fever 2](../games/s-z/transport-fever-2.md)

## ACT-672

- Назва: Виконати призначений додатковий прийом у момент уже розпочатого удару
- Переглянуто: `2026-10-05`

### Операційне визначення

Гравець натискає кнопку вивченого й призначеного додаткового прийому в момент влучання вже розпочатої власної або ворожої атаки, запитуючи передбачений ефект прийому без вибору нової цілі.

### Включає

Вивчені прийоми ланцюга у Wine Cellar в момент влучання зброєю Ashley та захисні прийоми в момент ворожого влучання, зокрема запобігання станам або повернення шкоди, а не лише парирування.

### Виключає

Вибір початкової зброї, закляття чи цілі; звичайна атака, яку можна почати довільно; вимога, щоб кожна захисна відповідь скасовувала отриману шкоду; зупинка рухомого вказівника всередині смуги поступу.

### Ігри-носії

- [`GAME-0499` — Vagrant Story](../games/s-z/vagrant-story.md)

## ACT-673

- Назва: Безповоротно прибрати допустимий запас з інвентарю без компенсації
- Переглянуто: `2026-10-05`

### Операційне визначення

Гравець підтверджує безповоротне вилучення вибраного допустимого предмета або кількості з інвентарю, звільняючи зайняту місткість без ефекту предмета, оплати чи повернення складників.

### Включає

Вилучення неспоряджених предметів або різних запасів у Wine Cellar, щоб звільнити місце відповідної категорії для запропонованої нагороди.

### Виключає

Викидання в ігровий світ із можливістю підібрати знову; використання витратного предмета; продаж або переробка з поверненням складників; вилучення наразі вдягненого предмета, коли умова вилучення це забороняє.

### Ігри-носії

- [`GAME-0511` — Animal Crossing: New Leaf](../games/a-f/animal-crossing-new-leaf.md)
- [`GAME-0512` — Resident Evil Requiem](../games/m-r/resident-evil-requiem.md)
- [`GAME-0499` — Vagrant Story](../games/s-z/vagrant-story.md)

## ACT-674

- Назва: У вибраний момент запитати зупинку циклічного вибору нагороди
- Переглянуто: `2026-10-05`

### Операційне визначення

Поки після сутички циклічно змінюються нагороди, гравець обирає момент запиту на зупинку; команда запускає остаточний вибір, а не дозволяє прямо обрати довільну нагороду чи гарантувати наразі видимий варіант.

### Включає

Вибір моменту натискання Circle у початковій Vagrant Story для післябойового колеса характеристик, описаний в індексованих посібниках гравців і підтверджений записаними станами колеса та результату.

### Виключає

Звичайне меню взаємовиключних варіантів; фізичне захоплення предмета на виході; твердження, що зупинка миттєво закріплює показаний варіант; неперевірені формули позиції колеса чи затримки.

### Ігри-носії

- [`GAME-0499` — Vagrant Story](../games/s-z/vagrant-story.md)

## ACT-675

- Назва: Закріпити або прибрати перелік для збирання складників відомого рецепта
- Переглянуто: `2026-10-05`

### Операційне визначення

Гравець обирає відомий рецепт і додає або прибирає його результат та потрібні складники з поточного переліку для збирання, не запускаючи виготовлення й не резервуючи ці складники.

### Включає

Команду Pin to Checklist для Crude Door, ремонтних засобів і Crude Headlight під час першої підготовки в гаражі та виїзду в Pacific Drive.

### Виключає

Виготовлення вибраного результату; призначення рецепта автоматичному виробництву; встановлення точки на мапі світу; задану авторами вимогу місії, яку гравець не може закріпити або прибрати.

### Ігри-носії

- [`GAME-0500` — Pacific Drive](../games/m-r/pacific-drive.md)

## ACT-676

- Назва: Встановити власну довільну точку на мапі без розрахунку маршруту
- Переглянуто: `2026-10-05`

### Операційне визначення

Гравець обирає місце на локальній мапі як власний орієнтир; команда змінює позначений пункт призначення без розрахунку дорожнього шляху чи переміщення учасника.

### Включає

Команду Pin Waypoint на мапі ARC під час першого виїзду до Radio Station у Pacific Drive.

### Виключає

Автоматично розрахований дорожній маршрут GPS; послідовно з’єднані позначки, що утворюють лінію запланованого маршруту; вибір виходу для його активації; наказ автономного руху.

### Ігри-носії

- [`GAME-0152` — Elden Ring](../games/a-f/elden-ring.md)
- [`GAME-0500` — Pacific Drive](../games/m-r/pacific-drive.md)

## ACT-677

- Назва: Підтвердити один наразі допустимий віддалений вихід
- Переглянуто: `2026-10-05`

### Операційне визначення

На доступній панелі керування виходами гравець обирає одне наразі допустиме віддалене місце й підтверджує його активацію, а не лише позначає цю позицію чи негайно переноситься туди.

### Включає

Вибір координат виходу та команди Link Gateway через заряджений ARC під час першого виїзду в Pacific Drive.

### Виключає

Довільну навігаційну позначку; фізичний в’їзд до активованого виходу; миттєве швидке переміщення; фіксований вихід, що відкривається без вибору місця; подальшу відповідь системи у вигляді небезпеки.

### Ігри-носії

- [`GAME-0500` — Pacific Drive](../games/m-r/pacific-drive.md)

## ACT-678

- Назва: Націлити коротке переміщення збереженої машини ззовні
- Переглянуто: `2026-10-05`

### Операційне визначення

Керуючи персонажем поза його збереженою машиною, гравець націлює допустиме близьке місце відновлення й запитує переміщення цієї машини, зберігаючи керування персонажем, а не кермуючи чи переносячи самого персонажа.

### Включає

Утримування T поза універсалом, щоб скануванням знайти місце переміщення машини під час першої експедиції в Pacific Drive.

### Виключає

Запит відновлення під час безпосереднього керування призначеною для місії машиною; націлене переміщення керованого персонажа; перезапуск цілого рівня; необмежене швидке переміщення на великі відстані.

### Ігри-носії

- [`GAME-0500` — Pacific Drive](../games/m-r/pacific-drive.md)

## ACT-679

- Назва: Увійти до збільшеного прицільного огляду спорядженої зброї або вийти з нього
- Переглянуто: `2026-10-05`

### Операційне визначення

Гравець явно перемикає готову вогнепальну зброю між звичайним оглядом і її прицільним збільшенням без пострілу, зміни самої зброї чи захоплення цілі.

### Включає

Команду Aim/Zoom для наявного пістолета, пістолета-кулемета чи отриманої штурмової гвинтівки у First Encounter оригінальної F.E.A.R. для Windows.

### Виключає

Сам постріл; довільну камеру огляду; захоплення цілі; утримання прицілу для заряджання окремої шкали концентрації; припущення, що вся зброя має однакове збільшення чи перевагу в точності.

### Ігри-носії

- [`GAME-0501` — F.E.A.R.](../games/a-f/fear.md)

## ACT-680

- Назва: Розгорнути здатність планерування в повітрі й керувати нею
- Переглянуто: `2026-10-05`

### Операційне визначення

Уже перебуваючи в повітрі, гравець розгортає набуту здатність планерування й спрямовує подальше зниження до досяжної місцевості, а не вибирає місце призначення для автоматичного переміщення.

### Включає

Hazel розгортає сплетені крила й керує між заданими авторами місцями приземлення в розділі 3 після вивчення Glide.

### Виключає

Чергування розгойдування на прив’язі й планерування; необмежене підняття з тягою; кінематографічний політ; вихід із транспортного засобу; сам звичайний стрибок.

### Ігри-носії

- [`GAME-0561` — Psychonauts 2](../games/m-r/psychonauts-2.md)
- [`GAME-0502` — South of Midnight](../games/s-z/south-of-midnight.md)
- [`GAME-0548` — Space Station Silicon Valley](../games/s-z/space-station-silicon-valley.md)

## ACT-681

- Назва: Використати тимчасову ближню взаємодію з уже переможеним ворогом
- Переглянуто: `2026-10-05`

### Операційне визначення

Коли ворога вже переможено, гравець наближається й виконує необов’язкову контекстну ближню взаємодію до зникнення залишеного тіла; ця команда не потрібна для завдання вирішальної шкоди.

### Включає

Запит Unravel кнопкою Y біля переможеного Haint у South of Midnight.

### Виключає

Подальшу дію при тимчасовому приголомшенні живого противника; звичайний ближній удар; автоматичне зникнення трупа; повернення інвентарю, який перед тим переносили й упустили.

### Ігри-носії

- [`GAME-0502` — South of Midnight](../games/s-z/south-of-midnight.md)

## ACT-682

- Назва: Виконувати відстежувану датчиком хореографію в музичному ритмі
- Переглянуто: `2026-10-05`

### Операційне визначення

Активний гравець безпосередньо рухає кінцівками й тулубом у музичному ритмі, дзеркально повторюючи поточну показану хореографію або виконуючи власні рухи в заданому вільному інтервалі; команда є безперервною відстежуваною траєкторією тіла, а не окремим натисканням панелі чи інструментальної ноти.

### Включає

Повторення Step Side, Hip Notch та інших заданих рухів в оригінальному Dance Central Perform It!; виконання власних рухів під час інтервалу Freestyle цього танцю.

### Виключає

Вибір нот ручним контролером; натискання окремих перемикачів танцювального килимка ногами; закриття просторової протічки кінцівкою; вибір пози, яку персонаж виконує автоматично.

### Ігри-носії

- [`GAME-0503` — Dance Central](../games/a-f/dance-central.md)

## ACT-683

- Назва: Обирати частку зайнятості району
- Переглянуто: `2026-10-06`

### Операційне визначення

Гравець вибирає частку повної зайнятості району, яка зберігається до зміни налаштування, перерозподіляючи спільну робочу силу та разом масштабуючи визначені вимоги району до ресурсів і його обсяг виробництва.

### Включає

Зменшення зайнятості видобувного району, щоб вивільнити працівників для житлового району з дослідницькою установою у Frostpunk 2.

### Виключає

Призначення окремих працівників за іменами; зміну загальної швидкості часу; вибір іншої виробничої рецептури.

### Ігри-носії

- [`GAME-0504` — Frostpunk 2](../games/a-f/frostpunk-2.md)

## ACT-684

- Назва: Резервувати або розширювати зв’язну ділянку району з кількох клітин
- Переглянуто: `2026-10-06`

### Операційне визначення

Гравець вибирає потрібну зв’язну множину клітин ігрового світу для одного району або допустимого прилеглого розширення цього району, а потім підтверджує будівництво поселення на вибраній ділянці.

### Включає

Вибір очищених клітин житлового району та подальший вибір прилеглих клітин його розширення у Frostpunk 2.

### Виключає

Розміщення району на одному гексі; окреме креслення житлових зон без підтвердження кількості клітин району; розчищення мерзлого ґрунту перед будівництвом.

### Ігри-носії

- [`GAME-0504` — Frostpunk 2](../games/a-f/frostpunk-2.md)

## ACT-685

- Назва: Призначати обмежені регіональні команди для розвідки чи збору
- Переглянуто: `2026-10-06`

### Операційне визначення

Гравець призначає визначену кількість доступних регіональних команд для однієї поточно допустимої розвідки чи збору ресурсів, резервуючи ці команди замість керування окремими мандрівниками.

### Включає

Відправлення Frostland Teams на розвідку західного регіону або призначення їх до відкритої ділянки збору ресурсів у Frostpunk 2.

### Виключає

Формування загону з індивідуальним вибором спорядження; безпосереднє водіння розвідника; твердження, що кожна ділянка збору потребує стежки.

### Ігри-носії

- [`GAME-0504` — Frostpunk 2](../games/a-f/frostpunk-2.md)

## ACT-686

- Назва: Задавати напрямлені темпи постачання ресурсів між керованими поселеннями
- Переглянуто: `2026-10-06`

### Операційне визначення

Гравець налаштовує напрям і постійний обсяг за інтервал ігрового часу для кожного дозволеного постачання ресурсу між двома окремо керованими з’єднаними поселеннями.

### Включає

Налаштування постачання нафти зі Старого дредноута до New London і їжі у зворотному напрямі у Frostpunk 2.

### Виключає

Одноразове переселення людей; вибір ціни торговця; прокладання сполучної стежки; ручне переміщення фізичного стосу предметів, який переносять.

### Ігри-носії

- [`GAME-0504` — Frostpunk 2](../games/a-f/frostpunk-2.md)

## ACT-687

- Назва: Обирати управлінську дію щодо конкретної спільноти
- Переглянуто: `2026-10-06`

### Операційне визначення

Гравець звертається до поточної спільноти чи фракції й виконує доступну управлінську дію, розкриті матеріальна плата, користь і наслідок для відносин якої застосовуються до цієї групи.

### Включає

Запит коштів у спільноти або доступну дію підтримки через панель фракції у Frostpunk 2.

### Виключає

Закон, який набуває чинності лише після голосування ради; пасивну зміну відносин; припущення, що обрана дія не має часу відновлення чи плати.

### Ігри-носії

- [`GAME-0504` — Frostpunk 2](../games/a-f/frostpunk-2.md)

## ACT-688

- Назва: Підтвердити прокладання регіональної стежки через допустимі точки з’єднання
- Переглянуто: `2026-10-06`

### Операційне визначення

Гравець обирає регіональну послідовність допустимих точок з’єднання та підтверджує платне будівництво стежки, яка сполучить відкриті місця з мережею поселення.

### Включає

Сполучення New London і Старого дредноута через точки стежки у Frostland у Frostpunk 2.

### Виключає

Малювання місцевої дорожньої мережі для фізичних транспортних засобів; сам вибір темпу постачання; миттєве переміщення до невідкритого місця.

### Ігри-носії

- [`GAME-0504` — Frostpunk 2](../games/a-f/frostpunk-2.md)

## ACT-689

- Назва: Переселяти обрану кількість населення між керованими поселеннями
- Переглянуто: `2026-10-06`

### Операційне визначення

Гравець підтверджує переселення показаної кількості мешканців із допустимого вихідного поселення до окремо керованого місця призначення, змінюючи їхню належність до поселення, а не постійну швидкість потоку ресурсів.

### Включає

Переселення колоністів із New London для заснування чи збільшення колонії Старого дредноута у Frostpunk 2.

### Виключає

Автоматичне зростання колонії; постійне постачання їжі; вибір індивідуальних тактичних позицій; припущення про неперевірений час міграції.

### Ігри-носії

- [`GAME-0504` — Frostpunk 2](../games/a-f/frostpunk-2.md)

## ACT-690

- Назва: Повертати бойовий огляд польоту на чверть оберту
- Переглянуто: `2026-10-06`

### Операційне визначення

Гравець змінює активний напрям прицілювання навколо тіла, що автоматично просувається в польоті, на визначену чверть оберту, відкриваючи бічні чи задні загрози для атаки без розвороту або вільного вибору світового маршруту.

### Включає

Зміну огляду польоту кнопками L/R із кроком 90 градусів у початковій Panzer Dragoon.

### Виключає

Зміну лише відстані камери стеження; керування довільним напрямом вільного польоту; автоматичну кінематографічну камеру; припущення про однакові можливості керування тілом у кожному бойовому напрямі.

### Ігри-носії

- [`GAME-0587` — Panzer Dragoon II Zwei](../games/m-r/panzer-dragoon-ii-zwei.md)
- [`GAME-0505` — Panzer Dragoon](../games/m-r/panzer-dragoon.md)

## ACT-691

- Назва: Набирати цілі утриманим прицілюванням і відпускати підготовлений залп
- Переглянуто: `2026-10-06`

### Операційне визначення

Гравець утримує захоплення цілей, проводячи прицілом через допустимі ворожі цілі, а потім відпускає ту саму команду, щоб виконати підготовлений самонавідний залп по кількох цілях замість безперервної стрільби в одного автоматично утримуваного супротивника.

### Включає

Утримання A/B/C, наведення на ворогів і відпускання самонавідного залпу дракона в початковій Panzer Dragoon.

### Виключає

Підготовку скінченної ракети з інвентарю перед окремою командою вогню; одну автоматично утримувану ціль безперервної стрільби; трактування позначок цілей як уже влучених атак.

### Ігри-носії

- [`GAME-0587` — Panzer Dragoon II Zwei](../games/m-r/panzer-dragoon-ii-zwei.md)
- [`GAME-0505` — Panzer Dragoon](../games/m-r/panzer-dragoon.md)
- [`GAME-0526` — Rez](../games/m-r/rez.md)

## ACT-692

- Назва: Перемикати підготовлену пару предметів у руках під час звичайного керування
- Переглянуто: `2026-10-06`

### Операційне визначення

Гравець перемикає активне спорядження між збереженими підготовленими наборами, разом замінюючи доступні призначення основної та другої руки замість вибору одного предмета з інвентарю чи редагування підготовчих комірок.

### Включає

Команду Y у навчальному відрізку Avowed, що перемикає підготовлені меч зі щитом, дворучний лук і жезл із книгою заклять.

### Виключає

Вибір одного предмета з панелі; перемикання команди зброї на окремо обрану особисту здібність; налаштування комірок інвентарю; отримання нового предмета самим перемиканням.

### Ігри-носії

- [`GAME-0506` — Avowed](../games/a-f/avowed.md)

## ACT-693

- Назва: Запитувати платне повернення розподілених очок персонажа
- Переглянуто: `2026-10-06`

### Операційне визначення

Гравець підтверджує доступне скидання визначеної групи постійно розподілених очок персонажа за ціну у валюті, щоб витрачені очки знову стали доступними для розподілу; цей запит відрізняється від витрачання ще не розподіленого очка.

### Включає

Запит скидання характеристик або здібностей Avowed у меню персонажа після появи можливості розподілу очок.

### Виключає

Безкоштовний перерозподіл Spark; зміну лише споряджених предметів; створення початкового персонажа; автоматичне повернення очок після смерті; припущення про одночасне скидання всіх груп очок.

### Ігри-носії

- [`GAME-0506` — Avowed](../games/a-f/avowed.md)

## ACT-694

- Назва: Обирати запропоновані відкриті клас і транспорт перед заїздом
- Переглянуто: `2026-10-06`

### Операційне визначення

Перед однією скінченною спробою заїзду гравець обирає допустимий відкритий клас транспорту, а потім один запропонований транспорт цього класу, задаючи його властивості керування й зіткнень для спроби без окремої операції володіння гаражем чи вибору типу трансмісії.

### Включає

Вибір будь-якого із семи запропонованих класів і доступного транспорту перед стартом першого заїзду Grizzly у початковій MotorStorm.

### Виключає

Вибір активного транспорту з власного гаража за ACT-291; вибір автомобіля разом із ручною чи автоматичною трансмісією за ACT-608; придбання або налаштування транспорту; зміну класу після початку заїзду.

### Ігри-носії

- [`GAME-0507` — MotorStorm](../games/m-r/motorstorm.md)

## ACT-695

- Назва: Утримувати й відпускати прискорення з урахуванням нагрівання двигуна
- Переглянуто: `2026-10-06`

### Операційне визначення

Безпосередньо керуючи допустимим транспортом, гравець утримує команду прискорення, щоб отримати більший розгін і швидкість ціною накопичення тепла в двигуні, а потім відпускає її для охолодження до руйнівного перегрівання замість витрати скінченного збереженого запасу тяги.

### Включає

Утримуване Boost і свідоме відпускання між фазами нагрівання після початкового прогрівання в початковій MotorStorm.

### Виключає

Списання скінченного запасу тяги за ACT-309; автоматичний розгін без команди прискорення; витрату спільного запасу енергії пошкоджень у F-Zero GX; своєчасне завершення керованого заносу заради одноразового приросту швидкості.

### Ігри-носії

- [`GAME-0507` — MotorStorm](../games/m-r/motorstorm.md)

## ACT-696

- Назва: Запитувати допустиму за обставинами атаку мотоцикліста поруч
- Переглянуто: `2026-10-06`

### Операційне визначення

Безпосередньо керуючи допустимим гоночним транспортом із мотоциклістом, гравець подає спільну команду дії для атаки допустимого мотоцикліста-суперника поруч; за відсутності цих місцевих умов той самий ввід виконує іншу дію без атаки замість гарантованого удару на відстані.

### Включає

Команду Action на MX Bike у початковій MotorStorm, коли інший мотоцикл поруч, та іншу дію, описану інструкцією для випадку без суперника, якого можна атакувати.

### Виключає

Спрямування всього транспорту в суперника за ACT-379; постріл установленою зброєю; атаку з вимогою спорядженого бойового інструмента; безумовний удар по віддаленому мотоциклісту; гарантоване скидання мотоцикліста після кожного прийнятого запиту.

### Ігри-носії

- [`GAME-0507` — MotorStorm](../games/m-r/motorstorm.md)

## ACT-697

- Назва: Змінювати постійний склад офіцерів і призначення до виїзної групи
- Переглянуто: `2026-10-06`

### Операційне визначення

На оперативній базі гравець наймає або звільняє допустимого окремого офіцера та призначає доступних членів складу до обмежених місць активної групи, зберігаючи індивідуальність кожного й спорядження замість вибору взаємозамінних придбаних бойових одиниць.

### Включає

Початкових резервних офіцерів, запропонований найм, Fire і заміну призначеного офіцера перед наступним виїздом у звичайному Commander гри Ready or Not.

### Виключає

Розміщення на стартових тактичних клітинках за ACT-651; розклади військового навчання за ACT-153; захоплення істот до сховища; автоматичне воскресіння відсутнього офіцера; суто декоративні портрети персоналу.

### Ігри-носії

- [`GAME-0508` — Ready or Not](../games/m-r/ready-or-not.md)

## ACT-698

- Назва: Направляти допустимого члена складу на тимчасове лікування стресу
- Переглянуто: `2026-10-06`

### Операційне визначення

У стані керування персоналом гравець запитує лікування допустимого збереженого учасника, усуваючи його з поточної доступності до виїзду замість безпосереднього відновлення бойового здоров’я під час місії.

### Включає

Команду Send To Therapy у Commander гри Ready or Not після зарахування стресу першої місії.

### Виключає

Загальне бойове перев’язування; миттєве лікування смертельної травми; остаточне звільнення офіцера; призначення медичного ліжка колонії; гарантію точної тривалості лікування.

### Ігри-носії

- [`GAME-0508` — Ready or Not](../games/m-r/ready-or-not.md)

## ACT-699

- Назва: Подавати поліцейську вимогу підкоритися чи переміститися за допустимого стану
- Переглянуто: `2026-10-06`

### Операційне визначення

Офіцер під безпосереднім керуванням звертається до досяжної особи з вимогою підкоритися або запитує допустимі поворот, переміщення чи вихід від особи, яка вже здалася або затримана; вимога запитує відповідь, але сама не гарантує здавання й не завершує фізичного затримання.

### Включає

Вимоги підкоритися та команди версії 1.0 гри Ready or Not до осіб, які здалися чи затримані: повернутися, підійти, перейти до позначеного місця або рушити до виходу.

### Виключає

Затримання з безперервним утриманням особи під прицілом за ACT-417; фізичне зв’язування за ACT-341; призначення маршруту групі за ACT-189; гарантоване виконання вимоги активним противником.

### Ігри-носії

- [`GAME-0508` — Ready or Not](../games/m-r/ready-or-not.md)

## ACT-700

- Назва: Обирати поточний тактичний вигляд через камеру без передавання керування
- Переглянуто: `2026-10-06`

### Операційне визначення

Гравець запитує сумісний поточний вигляд із камери інструмента чи камери, яку носить напарник, оглядаючи сцену з цієї обмеженої точки й зберігаючи керування початковим офіцером замість переміщення цього офіцера до камери.

### Включає

Огляд спорядженим Mirror Gun під обраними дверима та перегляд камери офіцера на планшеті в Ready or Not.

### Виключає

Вільну камеру переглядача повторів; всезнавчу мапу противників; перемикання місцевого фільтра нічного бачення; передавання керування носієві камери; нерухомий письмовий інструктаж.

### Ігри-носії

- [`GAME-0508` — Ready or Not](../games/m-r/ready-or-not.md)

## ACT-701

- Назва: Перемикати споряджене нічне бачення без створення місцевого світлового поля
- Переглянуто: `2026-10-06`

### Операційне визначення

Під час безпосереднього керування гравець вмикає або вимикає споряджене обладнання нічного бачення, змінюючи відтворення місцево видимого світла без випромінювання поля ліхтарика чи заміни звичайного керування рухом і зброєю.

### Включає

Використання споряджених NVGs як альтернативи іншому обраному головному спорядженню для огляду темних приміщень місії Ready or Not.

### Виключає

Випромінювання переносного світла ліхтарика за ACT-409; всезнавчий сканер крізь стіни; запас енергії бойового режиму; суто декоративну зміну кольорів у переглядачі повторів.

### Ігри-носії

- [`GAME-0508` — Ready or Not](../games/m-r/ready-or-not.md)

## ACT-702

- Назва: Виконувати самоперев’язування проти поточної кровотечі
- Переглянуто: `2026-10-06`

### Операційне визначення

Гравець виконує дію самодопомоги проти поточної кровотечі, тимчасово відмовляючись від звичайного використання зброї заради запиту зупинки кровотечі без вибору ділянки рани чи відновлення вже втраченого здоров’я.

### Включає

Команду самоперев’язування в Ready or Not; тогочасні повідомлення про помилки релізу підтверджують її наявність, а раніший письмовий матеріал описує задуманий результат без відновлення здоров’я.

### Виключає

Лікування обраної ділянки в медичній панелі за ACT-211; миттєве поповнення здоров’я; придбане відновлювальне зілля; лікування офіцера зі штучним інтелектом через вибір медичного предмета.

### Ігри-носії

- [`GAME-0508` — Ready or Not](../games/m-r/ready-or-not.md)

## ACT-703

- Назва: Запросити перехід із зачепленням за опору без вибору змінної траєкторії польоту
- Переглянуто: `2026-10-06`

### Операційне визначення

Гравець спрямовує багаторазову лінію, яку має при собі, на допустиму опору в ігровому світі й запитує зачеплення та перехід з опорою через місцевий розрив; прийнята команда не вимагає змінювати довжину лінії чи обирати траєкторію вільного польоту після відпускання.

### Включає

Перший провал у храмі Indiana Jones and the Great Circle, де прицільне зачеплення батогом дозволяє перебратися на інший бік.

### Виключає

Односпрямоване підтягування гаком, яке завершується при досягненні цілі (ACT-361); регульоване втягування й обране відпускання з імпульсом (ACT-531); автоматичний перехід без запиту зачеплення; атаки батогом як зброєю.

### Ігри-носії

- [`GAME-0510` — Indiana Jones and the Great Circle](../games/g-l/indiana-jones-and-the-great-circle.md)

## ACT-704

- Назва: Розміщувати переносний зразок у домашній експозиції з можливістю повернення
- Переглянуто: `2026-10-06`

### Операційне визначення

Гравець вибирає переносний зразок тварини й розміщує відповідну його виду експозицію на допустимому вільному місці вдома, звільняючи переносну місткість без продажу, випускання чи пожертви; той самий власний зразок згодом можна знову забрати.

### Включає

Розміщення впійманої риби New Leaf у домашньому акваріумі й подальше повернення до кишень.

### Виключає

Перерозподіл зброї матчу за ACT-186; придбані меблі в призупиненому режимі будівництва за ACT-612; незворотне випускання; пожертву публічному музею; припущення, що в New Leaf акваріум із рибою можна ставити надворі.

### Ігри-носії

- [`GAME-0511` — Animal Crossing: New Leaf](../games/a-f/animal-crossing-new-leaf.md)

## ACT-705

- Назва: Запитувати збереження поточного світу з продовженням гри або виходом із сеансу
- Переглянуто: `2026-10-06`

### Операційне визначення

У доступному меню збереження гравець явно запитує запис поточного стану світу й вибирає продовження звичайної гри або завершення сеансу після запису; цей запит не вибирає старішої гілки історії.

### Включає

Варіанти збереження New Leaf через START після початкового етапу, що дозволяє збереження.

### Виключає

Лише автоматичну контрольну точку; вибір попередньої збереженої історії за TIM-007; споживання одноразового стану призупинення за SYS-1349; зміну системного годинника.

### Ігри-носії

- [`GAME-0511` — Animal Crossing: New Leaf](../games/a-f/animal-crossing-new-leaf.md)
- [`GAME-0513` — Thief: The Dark Project](../games/s-z/thief-the-dark-project.md)

## ACT-706

- Назва: Утримувати контекстну команду пересування важкого об’єкта заданим шляхом
- Переглянуто: `2026-10-06`

### Операційне визначення

Локально керований персонаж взаємодіє з допустимим важким рухомим об’єктом і утримує контекстну команду, щоб пересувати його заданим шляхом до дозволеної позиції зупинки; відпускання припиняє керований рух. Це не поштовх на одну комірку й не вільне перенесення об’єкта.

### Включає

Пересування Ґрейс візка в Nurses Station, щоб дістатися підвищеного контейнера з викруткою й раніше перекритої шафки з травою в першому епізоді Care Center.

### Виключає

Поштовх на одну логічну позицію із зайняттям персонажем звільненого місця за ACT-009; вільне перенесення фізичного предмета; віддалене редагування будови кімнат; автоматичний візок без утримуваної команди пересування.

### Ігри-носії

- [`GAME-0512` — Resident Evil Requiem](../games/m-r/resident-evil-requiem.md)
- [`GAME-0559` — The Last Guardian](../games/s-z/the-last-guardian.md)

## ACT-707

- Назва: Націлити й витратити метальний предмет при собі, який можна розбити, для відвертання уваги
- Переглянуто: `2026-10-06`

### Операційне визначення

Гравець вибирає один предмет, який можна розбити, зі скінченного запасу при собі, націлює його й кидає в напрямку досяжної точки світу; кидок витрачає цю одиницю запасу при собі, а удар може розбити предмет і створити місцевий стимул уваги. Допустимі реакції на прямий контакт належать цілі, а не правилу про гарантовано нешкідливий інертний предмет.

### Включає

Ґрейс кидає Empty Bottle, щоб відвести Дівчину від проходу; у даних про предмет показано Power і Radius, але це не доводить числових коефіцієнтів шкоди чи оглушення оригінальної програми.

### Виключає

Суворо інертне відвертання за ACT-406, яке виключає снаряд зі шкодою; підготовлену тактичну гранату з її запалом і ефектом в області за ACT-184; ручний інструмент, що повертається; доведення того, що кожне влучання оглушує чи вбиває Дівчину; вигадування числового значення шкоди пляшки, яке можна прочитати з оглянутих смуг.

### Ігри-носії

- [`GAME-0512` — Resident Evil Requiem](../games/m-r/resident-evil-requiem.md)

## ACT-708

- Назва: Натягувати й відпускати обмежену прицільну інструментальну стрілу
- Переглянуто: `2026-10-06`

### Операційне визначення

Керований персонаж вибирає тип переносної інструментальної стріли, утримує натяг лука, націлюючись на досяжну допустиму ціль оточення, і відпускає, щоб випустити одну сумісну стрілу; команда витрачає відповідний запас і спрямовує інструментальну дію на оточення, не вимагаючи ворожої бойової цілі чи об’єкта, який можна зруйнувати.

### Включає

Натягування й випускання водяної стріли до допустимого факела маєтку для зміни освітлення в оригінальній місії лорда Баффорда.

### Виключає

Збройну атаку на ворожу ціль чи об’єкт, який можна зруйнувати, за ACT-161; кидання інертного відвертання; багаторазовий трос із командованим поверненням; автоматичну появу води на поверхні світу без прицільного обмеженого снаряда.

### Ігри-носії

- [`GAME-0513` — Thief: The Dark Project](../games/s-z/thief-the-dark-project.md)

## ACT-709

- Назва: Виконувати завершальний удар за ритмічною підказкою
- Переглянуто: `2026-11-16`

### Операційне визначення

Коли після допустимої серії атак відкривається окремий необов’язковий завершальний удар, гравець натискає кнопку атаки в позначений ритмічний момент, щоб виконати додатковий прийом.

### Включає

У Hi-Fi RUSH після потрібної серії натиснути кнопку атаки, коли кільця збігаються.

### Виключає

Звичайна атака в такт заради більшої шкоди; вибір наступної звичайної атаки в серії; обов’язкова підказка біля пристрою; автоматичний завершальний удар без окремого натискання.

### Ігри-носії

- [`GAME-0516` — Hi-Fi RUSH](../games/g-l/hi-fi-rush.md)

## ACT-710

- Назва: Задавати горизонтальну ціль і висоту однією командою руху
- Переглянуто: `2026-11-16`

### Операційне визначення

Перед підтвердженням однієї просторової команди гравець окремо вказує точку на опорній площині й відхилення від неї по вертикалі.

### Включає

У Homeworld позначити точку на диску руху й установити висоту перед підтвердженням.

### Виключає

Вибір цілі в одній площині, зміна висоти камери або окрема команда на підйом.

### Ігри-носії

- [`GAME-0517` — Homeworld](../games/g-l/homeworld.md)

## ACT-711

- Назва: Доручати спеціальному судну захоплення й буксирування цілої цілі
- Переглянуто: `2026-11-16`

### Операційне визначення

Гравець наказує придатному евакуаційному судну захопити доступний об’єкт цілим і взяти його на буксир.

### Включає

Доручити рятувальному корвету захопити останній навчальний дрон у першій місії Homeworld.

### Виключає

Атака заради уламків, підбирання відокремленого предмета, супровід союзника, який рухається самостійно, або здобуття цілі самим дотиком.

### Ігри-носії

- [`GAME-0517` — Homeworld](../games/g-l/homeworld.md)

## ACT-712

- Назва: Обирати й спрямовувати вивчений прийом перетворення
- Переглянуто: `2026-11-16`

### Операційне визначення

Гравець обирає вивчене тілесне перетворення з доступних і застосовує його прийом до досяжної істоти, об’єкта чи клітинки місцевості.

### Включає

У Pokémon Pokopia обрати водяний струмінь, щоб полити Сквіртла, або прийом для пророщування трави.

### Виключає

Спорядження окремого інструмента з інвентарю, автоматичне наслідування або саме вивчення прийому перед застосуванням.

### Ігри-носії

- [`GAME-0518` — Pokémon Pokopia](../games/m-r/pokemon-pokopia.md)

## ACT-713

- Назва: Втягувати доступні предмети в інвентар утриманням кнопки
- Переглянуто: `2026-11-16`

### Операційне визначення

Утримання кнопки збору втягує доступні матеріали й рухомі предмети в інвентар. Так можна зібрати кілька предметів поруч і забрати встановлені меблі, які дозволено переміщати.

### Включає

Зібрати опалі ягоди або забрати рухомий стілець із колод за допомогою втягування.

### Виключає

Миттєве підбирання одного вказаного предмета, утримання твердого тіла у світі гри або споживання предметів заради ефекту.

### Ігри-носії

- [`GAME-0518` — Pokémon Pokopia](../games/m-r/pokemon-pokopia.md)

## ACT-714

- Назва: Ловити кинутий предмет вчасним захопленням
- Переглянуто: `2026-11-16`

### Операційне визначення

Гравець натискає кнопку захоплення, коли придатний кинутий предмет долітає до бійця. Вчасне захоплення зупиняє його рух, і боєць бере предмет у руки.

### Включає

Зловити кинутий стілець у двобої Power Stone.

### Виключає

Підбирання нерухомого предмета, блокування удару, відбиття снаряда без захоплення або спроба зловити непридатне тіло.

### Ігри-носії

- [`GAME-0519` — Power Stone](../games/m-r/power-stone.md)
- [`GAME-0567` — SUPERHOT VR](../games/s-z/superhot-vr.md)

## ACT-715

- Назва: Кидати витратний предмет з урахуванням напрямку й руху носія
- Переглянуто: `2026-11-16`

### Операційне визначення

Гравець витрачає один предмет із запасу й випускає його в ігровий світ. Напрямок керування в цю мить і рух носія впливають на траєкторію.

### Включає

Кинути петарду під час руху на початку Animal Well.

### Виключає

Активація у фіксованій точці, багаторазовий інструмент, що повертається в інвентар, або кидок з окремим налаштуванням сили.

### Ігри-носії

- [`GAME-0520` — Animal Well](../games/a-f/animal-well.md)

## ACT-716

- Назва: Обирати багаторазовий диск за дальністю для наступного кидка
- Переглянуто: `2026-11-16`

### Операційне визначення

Перед кидком гравець обирає один із доступних багаторазових типів снарядів, щоб визначити його характерну дальність. Для наступного кидка тип можна змінити, не витрачаючи запас предметів.

### Включає

У диск-гольфі Wii Sports Resort обрати далекобійний диск на старті або диск для короткого кидка біля цілі.

### Виключає

Витрачання однієї з обмеженого запасу карт руху, використання скінченних боєприпасів або постійне спорядження здобичі з характеристиками.

### Ігри-носії

- [`GAME-0521` — Wii Sports Resort](../games/s-z/wii-sports-resort.md)

## ACT-717

- Назва: Змінювати напрямок підготовки без зміни місця кидка
- Переглянуто: `2026-11-16`

### Операційне визначення

Гравець задає горизонтальний напрямок наступного кидка, залишаючи точку початку на поточному місці. Це окрема від руху відпускання дія, яка не витрачає кидок.

### Включає

Повернути лінію прицілювання з того самого місця на короткій траві перед кидком диска.

### Виключає

Зміна місця, поворот лише камери або керування вже випущеним снарядом.

### Ігри-носії

- [`GAME-0521` — Wii Sports Resort](../games/s-z/wii-sports-resort.md)

## ACT-718

- Назва: Випускати диск у політ у вибраний момент руху контролера
- Переглянуто: `2026-11-16`

### Операційне визначення

Гравець утримує кнопку кидка під час руху контролера з датчиком руху й відпускає її, щоб запустити диск за зафіксованим рухом. Орієнтація і момент відпускання входять у початковий стан польоту.

### Включає

Зробити боковий замах відкаліброваним контролером Wii Remote і відпустити кнопку B у ручному режимі диск-гольфу.

### Виключає

Автоматично вибране відпускання, запуск кулі по доріжці або силовий кидок із наведенням вказівником.

### Ігри-носії

- [`GAME-0521` — Wii Sports Resort](../games/s-z/wii-sports-resort.md)

## ACT-719

- Назва: Обирати основне прицілювання або альтернативний вогонь глибиною натискання однієї кнопки
- Переглянуто: `2026-11-17`

### Операційне визначення

Гравець утримує одну аналогову кнопку на допустимій частковій глибині для прицільного основного вогню або натискає глибше, щоб підготувати альтернативний вогонь. Окрема кнопка виконує постріл у вибраному режимі, якщо він доступний.

### Включає

Після встановлення атропійського зарядного модуля натиснути L2 наполовину для прицілювання або до кінця для альтернативного вогню, а тоді вистрілити кнопкою R2.

### Виключає

Заміна зброї в руках, звичайна кнопка-перемикач без порога глибини натискання або постріл від самої кнопки прицілювання.

### Ігри-носії

- [`GAME-0522` — Returnal](../games/m-r/returnal.md)
- [`GAME-0667` — "SAROS"](../games/s-z/saros.md)

## ACT-720

- Назва: Гасити підскакування під час проходу по хвилі
- Переглянуто: `2026-11-17`

### Операційне визначення

Під час проходу по рухомій хвилі гравець використовує окремий засіб стабілізації, щоб гідроцикл менше підскакував на воді.

### Включає

Натиснути B на придатній хвилі на трасі Санні-Біч.

### Виключає

Пом’якшення лише кермування, відновлення запасу для руху або зміна загального стану води в меню налаштувань.

### Ігри-носії

- [`GAME-0524` — Wave Race 64](../games/s-z/wave-race-64.md)
- [`GAME-0674` — "Wave Race: Blue Storm"](../games/s-z/wave-race-blue-storm.md)

## ACT-721

- Назва: Пересувати обрану плитку в сусідню порожню клітинку
- Переглянуто: `2026-11-17`

### Операційне визначення

Гравець обирає плитку, що має спільний бік із порожньою клітинкою. Плитка займає цю клітинку й залишає порожнім своє попереднє місце. Плитка без потрібного сусідства лишається на місці.

### Включає

Пересунути кубик панелі H в сусідню порожню клітинку, зберігши решту кубиків на їхніх місцях.

### Виключає

Обмін двох зайнятих місць, обмін по діагоналі, пересування всього ряду або заповнення порожньої клітинки новим предметом.

### Ігри-носії

- [`GAME-0528` — The Neverhood](../games/s-z/the-neverhood.md)

## ACT-722

- Назва: Одразу закріплювати активну фігуру в кінці вертикального скидання
- Переглянуто: `2026-11-17`

### Операційне визначення

Окрема команда переміщує активну фігуру прямо вниз до останньої доступної позиції на її шляху й одразу закріплює її там.

### Включає

Миттєво скинути тетроміно й закріпити його, не чекаючи автоматичного падіння чи затримки після контакту.

### Виключає

Прискорення автоматичного падіння, зупинка нижче без закріплення або перенесення за перешкоду.

### Ігри-носії

- [`GAME-0649` — Drop Duchy](../games/a-f/drop-duchy.md)
- [`GAME-0529` — Tetris Effect](../games/s-z/tetris-effect.md)

## ACT-723

- Назва: Обмінювати активну фігуру через одне резервне місце
- Переглянуто: `2026-11-17`

### Операційне визначення

До закріплення активної фігури помісти її в резерв. На стартову позицію вийде збережена фігура або наступна з черги, якщо резерв був порожній. Щоб обміняти фігуру знову, спершу закріпи одну на полі.

### Включає

Залишити квадрат у резерві замість закріплення. Якщо резерв був порожній, зіграти наступною фігурою з черги й повернути квадрат пізніше.

### Виключає

Довільна перестановка черги, збереження другої фігури, отримання іншої без збереження попередньої або кілька обмінів до закріплення.

### Ігри-носії

- [`GAME-0529` — Tetris Effect](../games/s-z/tetris-effect.md)

## ACT-724

- Назва: Обирати момент активації зарядженого режиму розміщення
- Переглянуто: `2026-11-17`

### Операційне визначення

Увімкни тимчасовий режим розміщення, коли шкала показує достатній заряд. Команда витрачає доступний заряд і залишає керування фігурами гравцеві.

### Включає

Активувати Зону після достатньої кількості звичайних ліній і самостійно вибрати, коли витратити накопичений заряд.

### Виключає

Автоматична активація на порозі, пауза без витрати заряду або завершення ряду без входу в режим.

### Ігри-носії

- [`GAME-0529` — Tetris Effect](../games/s-z/tetris-effect.md)

## ACT-725

- Назва: Призначати зміну бойового ряду як дію учасника на раунд
- Переглянуто: `2026-11-17`

### Операційне визначення

До виконання команд вибери новий бойовий ряд для учасника, якому це доступно. Він перейде в межах раунду замість іншої бойової дії. Від ряду залежить, чи він посилює захист і чи користується ним.

### Включає

Перевести Каїма в задній ряд замість атаки. Він більше не дає того самого внеску в захист переднього ряду.

### Виключає

Безкоштовна перестановка до бою, заміна учасника резервним, рух у довільно обрану точку або зміна спорядження зі збереженням команди на раунд.

### Ігри-носії

- [`GAME-0530` — Lost Odyssey](../games/g-l/lost-odyssey.md)

## ACT-726

- Назва: Спрямовувати самостійного супутника до обраного пристрою
- Переглянуто: `2026-11-17`

### Операційне визначення

Гравець обирає доступний пристрій у світі. Супутник сам прямує до нього зі своєї позиції й після прибуття виконує передбачену взаємодію.

### Включає

Спрямувати Потбоя до труби, натискної плити або свічки, поки Обпалений лишається в іншому місці.

### Виключає

Пряме керування супутником, загальна команда йти слідом без цілі або віддалене ввімкнення пристрою без прибуття супутника.

### Ігри-носії

- [`GAME-0543` — Keeper](../games/g-l/keeper.md)
- [`GAME-0684` — "REANIMAL"](../games/m-r/reanimal.md)
- [`GAME-0531` — The Midnight Walk](../games/s-z/the-midnight-walk.md)

## ACT-727

- Назва: Заплющувати очі утриманням кнопки й розплющувати відпусканням
- Переглянуто: `2026-11-17`

### Операційне визначення

Гравець утримує доступну кнопку, щоб заплющити очі персонажа й тимчасово перервати звичайне бачення. Відпускання повертає зір.

### Включає

Спрямувати погляд на перешкоду із синім оком, заплющити очі й відпустити кнопку, щоб побачити, як змінився шлях.

### Виключає

Автоматичне затемнення в сюжетній сцені, простий поворот від цілі або режим пошуку, який зберігає звичайне зображення.

### Ігри-носії

- [`GAME-0531` — The Midnight Walk](../games/s-z/the-midnight-walk.md)

## ACT-728

- Назва: Обирати звичайну або посилену дію тривалістю натискання
- Переглянуто: `2026-11-17`

### Операційне визначення

Коротке натискання виконує звичайну дію. Утримання тієї самої кнопки готує відповідний посилений варіант, доступний після завершення підготовки за виконання його умов.

### Включає

Виконати звичайний особливий постріл відьомського посоха або утримати ту саму кнопку, щоб підготувати його варіант Ω.

### Виключає

Особлива дія на іншій кнопці, заміна зброї або утримання, яке лише затримує ту саму дію.

### Ігри-носії

- [`GAME-0532` — Hades II](../games/g-l/hades-ii.md)

## ACT-729

- Назва: Переносити духа між ядрами нерухомих або рухомих предметів
- Переглянуто: `2026-11-17`

### Операційне визначення

У режимі переміщення гравець проводить від поточного ядра до ядра іншого доступного предмета. Керування залишається за тим самим духом, а новий предмет стає єдиним носієм для наступних дій.

### Включає

Перенести Сіссела з настільної лампи до манекена, а потім до шини окремими переходами між ядрами.

### Виключає

Рух персонажа вільним простором, перемикання на іншого героя, керування предметом без вселення або виконання дії у світі живих самим вибором ядра.

### Ігри-носії

- [`GAME-0533` — "Ghost Trick: Phantom Detective"](../games/g-l/ghost-trick-phantom-detective.md)

## ACT-730

- Назва: Починати втручання у визначений момент перед смертю через тіло загиблого
- Переглянуто: `2026-11-17`

### Операційне визначення

Гравець обирає відмотування в допустимому тілі загиблого. Гра пов’язує цю смерть із визначеним ранішим станом, показує перебіг подій і дозволяє втрутитися без довільного вибору кадру.

### Включає

Уселитися в тіло Лінн і відмотати чотири хвилини, щоб почати першу спробу її порятунку.

### Виключає

Безперервне перемотування історії, довільний вибір моменту або повтор невдалої спроби з уже відкритої контрольної точки.

### Ігри-носії

- [`GAME-0533` — "Ghost Trick: Phantom Detective"](../games/g-l/ghost-trick-phantom-detective.md)

## ACT-731

- Назва: Змінювати форму або напрям смуги обробки ручного інструмента
- Переглянуто: `2026-11-17`

### Операційне визначення

Під час роботи гравець змінює насадку ручного інструмента й тим самим міняє форму або зосередженість струменя. Насадку зі спрямованим розпиленням можна повернути без переміщення персонажа.

### Включає

Установити вужчу водяну насадку для стійкого бруду на краю фургона або повернути віяло струменя вздовж наступної смуги.

### Виключає

Наведення тієї самої смуги на інше місце, заміна персонажа, зміна зовнішнього вигляду або саме придбання поліпшення.

### Ігри-носії

- [`GAME-0534` — PowerWash Simulator 2](../games/m-r/powerwash-simulator-2.md)

## ACT-732

- Назва: Призначати обрану команду на вільну позицію в черзі ходу
- Переглянуто: `2026-11-17`

### Операційне визначення

Обравши команду персонажа, гравець ставить її позначку у вільну часову комірку до виконання. Обраний стовпець визначає момент виконання незалежно від порядку вибору персонажів.

### Включає

Призначити постріл Вайза на пізніший етап ходу, залишивши раніше місце для захисту.

### Виключає

Вибір цілі, автоматичне сортування за швидкістю, зміна ряду в строю або затримання вже розпочатої атаки дією в реальному часі.

### Ігри-носії

- [`GAME-0535` — Skies of Arcadia](../games/s-z/skies-of-arcadia.md)

## ACT-733

- Назва: Покроково прокладати маршрут на сітці вибраної цілі
- Переглянуто: `2026-11-17`

### Операційне визначення

Коли приціл наведено на допустиму ціль, кожне натискання кнопки напрямку продовжує видимий маршрут на одну сусідню допустиму клітинку від його поточного кінця.

### Включає

Навестися на SectorGuard і вести курсор Діани до зеленого вузла по одній клітинці.

### Виключає

Саме лише захоплення цілі, малювання лінії одним безперервним жестом, обертання нерухомих клітинок або вибір двох кінців для автоматичної побудови маршруту.

### Ігри-носії

- [`GAME-0536` — PRAGMATA](../games/m-r/pragmata.md)

## ACT-734

- Назва: Підкидати персонажа різким рухом консолі вгору
- Переглянуто: `2026-11-17`

### Операційне визначення

Короткий рух пристрою з датчиком угору запускає звичайний стрибок персонажа. Плавний нахил окремо керує коченням по поверхні.

### Включає

Різко нахилити Game Boy Color угору, щоб Кірбі підстрибнув над низькою перешкодою або дістав підвішений предмет.

### Виключає

Звичайна кнопка стрибка, запуск із зайнятої лунки, тривалий нахил для розгону або поштовх, який безпосередньо підкидає всі тіла на поверхні.

### Ігри-носії

- [`GAME-0537` — Kirby Tilt 'n' Tumble](../games/g-l/kirby-tilt-n-tumble.md)

## ACT-735

- Назва: Установлювати й скидати нейтральне положення датчика нахилу
- Переглянуто: `2026-11-17`

### Операційне визначення

Гравець тримає пристрій у вказаному положенні й підтверджує калібрування. Скидання змінює положення, від якого гра відлічує подальший нахил.

### Включає

Тримати Game Boy Color горизонтально на екрані калібрування, підтвердити кнопкою A й за потреби скинути налаштування кнопкою Select.

### Виключає

Орієнтація карти чи камери, керування поточним нахилом, лише вибір постави або зміна напрямку ігрової гравітації.

### Ігри-носії

- [`GAME-0537` — Kirby Tilt 'n' Tumble](../games/g-l/kirby-tilt-n-tumble.md)

## ACT-736

- Назва: Пересувати незалежні панелі висновків поверх сцени
- Переглянуто: `2026-11-17`

### Операційне визначення

Гравець окремо розміщує панелі зі словами й відповідями. Сцена лишається доступною, тож чернетку, словник і докази можна звіряти в одному огляді.

### Включає

Відсунути панель слів від коридору й залишити панелі імен та подій відкритими під час огляду доказу.

### Виключає

Перемикання між взаємовиключними екранами огляду й відповіді, переставляння предметів доказу, зміна розміру або положення всього вікна гри.

### Ігри-носії

- [`GAME-0538` — The Rise of the Golden Idol](../games/s-z/the-rise-of-the-golden-idol.md)

## ACT-737

- Назва: Керувати рухом і взаємодією жестами в будь-якій частині ігрового екрана
- Переглянуто: `2026-11-17`

### Операційне визначення

Перетягування від довільної придатної точки задає напрямок руху. Короткий дотик на тому ж екрані виконує звичайний удар або доступну взаємодію з обраним об’єктом.

### Включає

Провести пальцем від нижнього краю галявини, щоб повести Ю, а тоді торкнутися куща чи істоти поруч, щоб замахнутися.

### Виключає

Дотик до місця призначення для автоматичної прокладки шляху, нерухомий екранний стік із фіксованою кнопкою дії або спільне керування кількома персонажами.

### Ігри-носії

- [`GAME-0540` — Afterplace](../games/a-f/afterplace.md)

## ACT-738

- Назва: Скласти й надіслати адресу запису з кількох полів
- Переглянуто: `2026-11-18`

### Операційне визначення

Вибери значення для окремих полів адреси запису. Кожне поле має скінченний набір варіантів. Гравець може виправити чернетку й окремою дією надіслати адресу для пошуку.

### Включає

Вистав номер сцени, вибери зареєстроване місце, увімкни перемикачі потрібних учасників і потягни важіль.

### Виключає

Пошук за довільним текстом розмови, заповнення відповіді розслідування й автоматичне відкриття сцени при кожній зміні поля.

### Ігри-носії

- [`GAME-0541` — The Incident at Galley House](../games/s-z/the-incident-at-galley-house.md)

## ACT-739

- Назва: Керувати прискоренням із тепловим обмеженням без знищення машини
- Переглянуто: `2026-11-18`

### Операційне визначення

Під час керування машиною гравець утримує команду додаткового прискорення, яка не витрачає скінченний запас заряду, і відпускає її, щоб керувати нагріванням. Перегрів тимчасово блокує цю команду, зберігаючи машину.

### Включає

Утримуй напрям на хрестовині пульта для турбоприскорення й відпусти його до перегріву двигуна.

### Виключає

Тяга за рахунок запасу пального, ривок лише після виходу із заносу й прискорення, вичерпання якого знищує машину.

### Ігри-носії

- [`GAME-0542` — Excite Truck](../games/a-f/excite-truck.md)

## ACT-740

- Назва: Прискорювати повернення розбитої машини повторними натисканнями
- Переглянуто: `2026-11-18`

### Операційне визначення

Коли аварія призупиняє звичайне керування, гравець повторює показану команду відновлення, щоб швидше повернути машину до того самого активного заїзду.

### Включає

Після аварії повторно натискай 2, щоб повернутися до перегонів із задокументованим ривком швидкості.

### Виключає

Предмет для відновлення здоров’я, відмотування історії руху, перезапуск усього заїзду й пасивне очікування повторної появи.

### Ігри-носії

- [`GAME-0542` — Excite Truck](../games/a-f/excite-truck.md)

## ACT-741

- Назва: Незалежно спрямовувати встановлену на тілі лампу й утримувати фокусування
- Переглянуто: `2026-11-18`

### Операційне визначення

Гравець спрямовує переносне або встановлене на тілі світло незалежно від руху й утримує окрему команду фокусування, щоб діяти на сумісну ціль у світі зосередженішим променем.

### Включає

Спрямуй лампу маяка правим стіком, а потім утримуй RT на рослині у формі ока в Radiant Grove.

### Виключає

Стрільба боєприпасами, витрата заряду для підсилення ліхтарика, саме обертання огляду й розсіяне світло без команд прицілювання або фокусування.

### Ігри-носії

- [`GAME-0543` — Keeper](../games/g-l/keeper.md)

## ACT-742

- Назва: Відповідати на запам’ятовану послідовність цілей напрямом і командою атаки або порятунку
- Переглянуто: `2026-11-19`

### Операційне визначення

Після появи цілей у впорядкованій ритмічній демонстрації гравець повторює їхні напрями й часовий рисунок, обираючи команду атаки або порятунку відповідно до типу кожної цілі.

### Включає

У стрілецькому обміні Space Channel 5 відповідай на цілі ліворуч, угорі або праворуч кнопкою A для Morolians і B для людей.

### Виключає

Вільне прицілювання в довільні координати, копіювання суто танцювальних символів без вибору за типом цілі й витрачання скінченного запасу боєприпасів.

### Ігри-носії

- [`GAME-0544` — Space Channel 5](../games/s-z/space-channel-5.md)

## ACT-743

- Назва: Призначати доступних виконавців у комірки поточної події
- Переглянуто: `2026-11-19`

### Операційне визначення

Гравець заповнює дозволені комірки виконавців поточної події доступними учасниками складу й підтверджує призначення. Ці персонажі беруться за виклик, а гравець не керує безпосередньо їхніми діями на місці.

### Включає

Обери доступного героя або дозволену групу Z-Team для виклику в Dispatch, перевір запропоновану відповідність і відправ їх.

### Виключає

Призначення постійних професій автономним працівникам, розміщення загону на стартових клітинках бою й безпосередні бойові команди.

### Ігри-носії

- [`GAME-0545` — Dispatch](../games/a-f/dispatch.md)

## ACT-744

- Назва: Обирати самонавідний імпульс гасіння або випуск зарядженого лазера
- Переглянуто: `2026-11-19`

### Операційне визначення

Гравець коротко натискає спільну кнопку вогню для імпульсу, що наводиться на близьке допустиме полум’я, або утримує її до повного показаного заряду й відпускає для сильнішого лазера. Це вибір способу дії на вогонь, а не витрачання скінченних боєприпасів.

### Включає

Коротко натисни B, щоб зберегти кристали після гасіння імпульсом, або повністю заряди й відпусти B проти сильного вогню, роботів чи першого боса Burning Rangers.

### Виключає

Вільне розміщення водної поверхні, стрільба з нерухомої пускової установки, стійка посилення зброї й припущення про однакові ресурси після сильнішого пострілу.

### Ігри-носії

- [`GAME-0546` — Burning Rangers](../games/a-f/burning-rangers.md)

## ACT-745

- Назва: Поєднувати команду тяги з напрямом відносно тіла для маневру пересування
- Переглянуто: `2026-11-19`

### Операційне визначення

Гравець поєднує поточну команду тяги з допустимим напрямом для короткого повітряного ривка або наземного ухильного маневру назад чи вбік. Наявність опори й стан руху визначають допустиму відповідь.

### Включає

Використай A або C з напрямом для повітряного ривка, а вниз або вбік із кнопкою тяги — для наземного сальто чи перекиду в Burning Rangers.

### Виключає

Трюк лише транспортного засобу, припущення про вільний політ від постійного утримання й накладання запасу одного додаткового стрибка на ланцюжок напрямних ривків.

### Ігри-носії

- [`GAME-0546` — Burning Rangers](../games/a-f/burning-rangers.md)

## ACT-746

- Назва: Запитувати негайну голосову вказівку маршруту у віддаленого навігатора
- Переглянуто: `2026-11-19`

### Операційне визначення

Гравець явно запитує навігаційну відповідь для поточної позиції через доступний канал зв’язку. Віддалений навігатор надає місцеву вказівку без пересування керованого персонажа й без відкриття повної карти маршруту.

### Включає

Натисни X або Z, щоб запитати в Chris поточний напрям у Burning Rangers.

### Виключає

Автоматичний пошук шляху, відкриття повної мінікарти, купівля підказки за час місії й прирівнювання прискореного відновлення тією самою кнопкою після удару до запиту маршруту.

### Ігри-носії

- [`GAME-0546` — Burning Rangers](../games/a-f/burning-rangers.md)

## ACT-747

- Назва: Вдаряти по нерухомому м’ячу відстежуваною ключкою
- Переглянуто: `2026-11-19`

### Операційне визначення

Гравець фізично підводить відстежувану головку ключки до м’яча, що лежить у поточній позиції. Напрям і силу удару задають положення в момент контакту та рух замаху, а не відпускання кнопки запуску чи вибір дискретної відстані.

### Включає

Вирівняй площину головки й виконай увімкненою ключкою фізичний удар по м’ячу на Tourist Trap у Walkabout Mini Golf.

### Виключає

Відпускання утримуваної кулі для боулінгу або диска, вибір скінченної картки руху, зупинка шкали сили кнопкою й керування м’ячем після удару.

### Ігри-носії

- [`GAME-0547` — Walkabout Mini Golf](../games/s-z/walkabout-mini-golf.md)

## ACT-748

- Назва: Змінювати місце огляду без пересування м’яча для наступного удару
- Переглянуто: `2026-11-19`

### Операційне визначення

Гравець запитує телепортацію огляду до вибраної точки світу або повернення до поточного об’єкта удару. Це змінює місце огляду й виконання удару, зберігаючи світову позицію об’єкта та накопичений результат.

### Включає

Оглянь поле Tourist Trap збоку або повернися телепортацією до м’яча перед наступним ударом у Walkabout Mini Golf.

### Виключає

Пересування самого м’яча, вибір для нього віддаленої цілі, обертання камери супроводу навколо окремо керованого персонажа й повернення витраченого удару.

### Ігри-носії

- [`GAME-0547` — Walkabout Mini Golf](../games/s-z/walkabout-mini-golf.md)

## ACT-749

- Назва: Прицілювати й відпускати ривок через арену з утримуваним посиленим варіантом
- Переглянуто: `2026-11-19`

### Операційне визначення

Із допустимої опори на внутрішній межі гравець задає вектор перетину й відпускає керування, щоб виконати тілесний ривок через арену. Довша підготовка утриманням може запросити забезпечений запасом посилений варіант замість лише вибору віддаленої точки чи безперервного керування вільним польотом.

### Включає

Лівим сенсорним керуванням Roto Force прицілься й відпусти ривок до іншої внутрішньої стіни; утримуй довше для посилення, коли вистачає надлишкового запасу.

### Виключає

Звичайний крок без попереднього прицілювання, атака з наведенням лише за наявності цілі, телепортація без проміжних зіткнень, декоративний стрибок і припущення про безкоштовне посилення кожного звичайного ривка.

### Ігри-носії

- [`GAME-0549` — Roto Force](../games/m-r/roto-force.md)

## ACT-750

- Назва: Запросити нерухомий перепочинок під час підтримуваного лазіння
- Переглянуто: `2026-11-19`

### Операційне визначення

Гравець навмисно припиняє переміщення й запитує позу відпочинку, залишаючись прикріпленим до поверхні для лазіння, щоб відновити придатний до витрати запас зусиль лише до його поточної доступної місткості, а потім продовжити те саме сходження.

### Включає

Натиснути лівий стік для перепочинку на стіні в Daymark гри Jusant, не діставшись перед цим твердої опори.

### Виключає

Витрата лікувального предмета; сон протягом обраної кількості годин; повернення на контрольну точку; припущення про необмежене пасивне відновлення без припинення лазіння.

### Ігри-носії

- [`GAME-0552` — Jusant](../games/g-l/jusant.md)

## ACT-751

- Назва: Пропонувати збережений зразок чинному відвідувачеві для визначення
- Переглянуто: `2026-11-19`

### Операційне визначення

Гравець обирає один власний зразок і подає його поточному адресованому відвідувачеві як відповідь на його запит рослини. Пропозиція перевіряє ідентичність зразка, але не витрачає унікальну рослину з полиці як скінченну одиницю товару.

### Включає

Запропонуй червоноквітковий St John’s Poppy Вікторії або Lemon Dandy із закрученим листям Ґілбертові в перший день крамниці.

### Виключає

Витрачання переносного предмета доставки за ACT-091; підтвердження назви введенням етикетки; придбання запасної рослини; зарахування невдалої пропозиції як виконаного запиту.

### Ігри-носії

- [`GAME-0554` — Strange Horticulture](../games/s-z/strange-horticulture.md)

## ACT-752

- Назва: Прикріплювати й змінювати непідтверджувальну етикетку зразка
- Переглянуто: `2026-11-19`

### Операційне визначення

Гравець прикріплює або редагує збережену текстову й кольорову етикетку сталого зразка як власну нотатку про його визначення. Етикетку можна змінити, і вона не обов’язково правдива; її текст сам собою не змінює ідентичності рослини й не виконує запиту відвідувача.

### Включає

Відрізняй попередні назви на полиці від повідомлення про визначену рослину та виправляй хибну власну етикетку.

### Виключає

Заблокований підтверджений запис; попереднє тлумачення повторюваного мовного символу за ACT-101; перевірка всього рядка відповіді; перетворення автоматичного підписування на обов’язкове правило.

### Ігри-носії

- [`GAME-0617` — Strange Antiquities](../games/s-z/strange-antiquities.md)
- [`GAME-0554` — Strange Horticulture](../games/s-z/strange-horticulture.md)

## ACT-753

- Назва: Підтверджувати одну клітинку карти як оплачуване дослідницьке відвідання
- Переглянуто: `2026-11-19`

### Операційне визначення

Гравець обирає адресовану клітинку авторської топографічної карти й підтверджує відвідання за доступний дозвіл на дослідження. Зустріч визначається в обраній точці, а не проходженням проміжного маршруту тілом героя.

### Включає

Обери C20 за підказкою Сімони про місто або G5 за відносними вказівками Амоса про ліс.

### Виключає

Передане системі пересування героя за ACT-096; малювання дороги; безкоштовна телепортація видимого тіла; координата поза внутрішньоігровою картою.

### Ігри-носії

- [`GAME-0554` — Strange Horticulture](../games/s-z/strange-horticulture.md)

## ACT-754

- Назва: Чистити доступний бруд на підлозі щіткою в руках
- Переглянуто: `2026-11-19`

### Операційне визначення

Гравець споряджає збережену щітку й повторює локальне чищення доступного бруду на підлозі, пересуваючи тіло для охоплення решти забрудненої поверхні. Щітка безпосередньо торкається цілі, а не створює віддалений струмінь для чищення.

### Включає

Чисть отриманою червоною зубною щіткою відбитки лап і малюнки у вітальні оригінальної Chibi-Robo! для GameCube.

### Виключає

Неперервний спрямований струмінь за ACT-446; усунення твердого садового непотребу за ACT-512; бойовий удар або суто декоративне чищення.

### Ігри-носії

- [`GAME-0555` — Chibi-Robo!](../games/a-f/chibi-robo.md)

## ACT-755

- Назва: Нести й під’єднувати власну вилку живлення до доступної розетки
- Переглянуто: `2026-11-19`

### Операційне визначення

Гравець піднімає власну вилку живлення керованого персонажа, з’єднану з ним кабелем, несе її під час пересування й явно під’єднує до доступної сумісної розетки. Це запускає нерухоме заряджання без передавання окремо здобутого ключа з інвентарю.

### Включає

Підніми вилку, що тягнеться за Чібі-Робо, перед наближенням до розетки у вітальні та під’єднанням.

### Виключає

Відпускання вільного твердого предмета за ACT-048; застосування здобутого ключа за ACT-087; автоматичне заряджання від близькості; мотузка як опора для лазіння.

### Ігри-носії

- [`GAME-0555` — Chibi-Robo!](../games/a-f/chibi-robo.md)

## ACT-756

- Назва: Змінюй поточний сигнал довкілля освітленням фізичного датчика
- Переглянуто: `2026-11-19`

### Операційне визначення

Гравець навмисно підставляє світлу, затінює або переорієнтовує фізичний датчик світла ігрового пристрою, змінюючи вимірюваний сигнал довкілля без переміщення віртуального персонажа чи вибору змодельованого значення денного світла.

### Включає

Зміна справжнього сонячного світла, яке потрапляє на датчик оригінального картриджа Boktai під час маршруту Fog Castle.

### Виключає

Віртуальне перемикання дня й ночі; положення GPS; заряджання лише з накопиченої віртуальної енергії; клавіші сонячного світла в емуляторі; вимірювання без керованої гравцем зміни освітлення.

### Ігри-носії

- [`GAME-0557` — "Boktai: The Sun Is in Your Hand"](../games/a-f/boktai-the-sun-is-in-your-hand.md)

## ACT-757

- Назва: Утримуй команду заряджання від навколишнього джерела
- Переглянуто: `2026-11-19`

### Операційне визначення

Коли керований персонаж перебуває біля чинного допустимого джерела енергії довкілля, гравець утримує окрему команду заряджання, прискорюючи поповнення збереженого запасу переносної зброї; відпускання команди завершує цю позу заряджання.

### Включає

Сонячне заряджання в Boktai надворі або під чинним світловим отвором, поки сонячне світло потрапляє на датчик.

### Виключає

Постріл зі зброї; витрата переносної одиниці поповнення; отримання накопиченого запасу зі станції; лише очікування пасивного заряджання; вигадане перезаряджання магазина.

### Ігри-носії

- [`GAME-0557` — "Boktai: The Sun Is in Your Hand"](../games/a-f/boktai-the-sun-is-in-your-hand.md)

## ACT-758

- Назва: Утримувати позначене оточення відстежуваною рукою незалежно від руху персонажа
- Переглянуто: `2026-11-19`

### Операційне визначення

Гравець підводить відстежуване зображення руки до допустимого пристрою оточення, утримує його керування захватом і рухає або затримує руку, продовжуючи керувати окремим персонажем; пристрій тлумачить цей сигнал за авторським правилом, а персонаж не стає тілом, що тримається.

### Включає

Читач утримує й пересуває позначений камінь у The Clearing або тримає сільське водяне колесо, окремо керуючи Quill.

### Виключає

Вільний предмет на сталій відстані від персонажа; рука фізичного шарнірного тіла, що підтягує власне тіло; двоє людей; команда автоматичного розв’язання маршруту.

### Ігри-носії

- [`GAME-0558` — Moss](../games/m-r/moss.md)

## ACT-759

- Назва: Керувати рухом після автоматичного зачеплення за авторський уступ
- Переглянуто: `2026-11-19`

### Операційне визначення

Після автоматичного зачеплення за допустимий авторський край під час стрибка чи падіння гравець спрямовує підвішеного персонажа вбік, наказує підтягнутися або навмисно відпускає його без утримання окремої кнопки прикріплення для збереження зачеплення.

### Включає

Quill чіпляється за позначені краї The Clearing, пересувається вздовж них, підтягується чи відпускається командою напрямку та стрибка, поки камінь можна рухати незалежно.

### Виключає

Зачеплення Lara з постійним утриманням кнопки дії; довільне лазіння поверхнею з витратою витривалості; окремо наведена зачіпна мотузка; дві незалежно керовані руки персонажа.

### Ігри-носії

- [`GAME-0594` — "Bionic Bay"](../games/a-f/bionic-bay.md)
- [`GAME-0560` — Gunstar Heroes](../games/g-l/gunstar-heroes.md)
- [`GAME-0558` — Moss](../games/m-r/moss.md)
- [`GAME-0559` — The Last Guardian](../games/s-z/the-last-guardian.md)

## ACT-760

- Назва: Оглядати закріплену мініатюрну сцену фізичним рухом відстежуваної голови
- Переглянуто: `2026-11-19`

### Операційне визначення

Гравець фізично нахиляється, повертається чи змінює висоту голови в поточній закріпленій сцені, щоб оглянути раніше перекриту місцеву геометрію, поки окремо керований персонаж залишається на своєму місці у світі; сама зміна огляду не пересуває його й не створює сполучення завдяки проєкції.

### Включає

Читач нахиляється навколо оточення The Clearing чи млина, щоб оглянути уступ і продовження шляху перед командою Quill.

### Виключає

Телепортація огляду до м’яча; поворот слідкувальної камери окремою командою; зміна допустимої суміжності перспективою; пересування геометрії самим поглядом.

### Ігри-носії

- [`GAME-0558` — Moss](../games/m-r/moss.md)

## ACT-761

- Назва: Керувати лазінням допустимими поверхнями з автоматичним утриманням
- Переглянуто: `2026-11-19`

### Операційне визначення

Гравець спрямовує прикріпленого персонажа допустимою поверхнею для лазіння й наказує піднятися, стрибнути чи навмисно відпуститися; звичайне прикріплення зберігається без постійного утримання окремої кнопки захвату чи витрати показаного запасу утримання.

### Включає

Хлопчик видирається опереним тілом Trico й підвісним ланцюгом печери, а потім відпускається на потрібній висоті.

### Виключає

Лише рух уздовж краю й підтягування; постійно утримуваний захват із витратою витривалості; пряме керування власником поверхні; вільне лазіння будь-якою непозначеною стіною.

### Ігри-носії

- [`GAME-0559` — The Last Guardian](../games/s-z/the-last-guardian.md)

## ACT-762

- Назва: Наводити переносну позначку для запиту розряду окремого супутника
- Переглянуто: `2026-11-19`

### Операційне визначення

Тримаючи отриманий сигнальний інструмент, гравець наводить його видиму позначку на місце у світі, щоб попросити доступного супутника про спрямований розряд; керований персонаж позначає ціль, а не випускає атаку із цього інструмента.

### Включає

Хлопчик піднімає дзеркало й утримує його світло на перешкоді в печері, щоб Trico вдарив туди хвостовим розрядом.

### Виключає

Сонячний компас, що показує напрямок до призначення; прямий постріл зброєю персонажа; відбиття вхідного снаряда; пізніші вивчені команди руху тіла.

### Ігри-носії

- [`GAME-0559` — The Last Guardian](../games/s-z/the-last-guardian.md)

## ACT-763

- Назва: Перемикати дві збережені зброї між окремими режимами та їх поєднанням
- Переглянуто: `2026-11-19`

### Операційне визначення

Під час поточного керування гравець перемикає доступну атаку між кожною збереженою зброєю окремо або обома разом; вибір режиму зберігає переносні компоненти замість їх витрачання чи незворотного виготовлення іншого предмета.

### Включає

Gunstar перемикає ліву зброю, праву зброю та їх пару перед стрільбою в Ancient Ruins.

### Виключає

Заміна одного типу зброї машини; перемикання між зброєю й особистою силою; незворотне витрачання двох складників; автоматична стрільба без команди вибору.

### Ігри-носії

- [`GAME-0560` — Gunstar Heroes](../games/g-l/gunstar-heroes.md)

## ACT-764

- Назва: Приймати беззбройну захисну позу проти сумісних поточних атак
- Переглянуто: `2026-11-19`

### Операційне визначення

Персонаж, здатний діяти, запитує або підтримує нерухому захисну позу власним тілом визначеним натисканням кнопок, захищаючись від допустимих вхідних атак без окремого щита чи зброї та без гарантії несприйнятливості до всіх атак.

### Включає

Gunstar одночасно натискає стрільбу й стрибок для захисної пози, описаної в інструкції.

### Виключає

Утримання спорядженого захисного засобу; спрямований високий чи низький бійцівський захист; своєчасне парирування; автоматична броня; обіцянка цілковитої невразливості.

### Ігри-носії

- [`GAME-0560` — Gunstar Heroes](../games/g-l/gunstar-heroes.md)

## ACT-765

- Назва: Випускати утримуваний змагальний диск напрямленим чи дуговим введенням з обраним різновидом кидка
- Переглянуто: `2026-11-20`

### Операційне визначення

Утримуючи спільний змагальний диск, гравець виконує його випуск доступною командою звичайного кидка чи навісу та напрямленим введенням; розпізнаний рух напрямків обирає кидок із вигином, а поточний допустимий заряджений стан чи стан контркидка може підставити дозволений посилений різновид. Команда обирає кидок, а не нове місце руху того, хто тримає диск.

### Включає

Windjammers використовує A для напрямленого звичайного кидка чи кидка з вигином і B для навісу; допустимий посилений стан дозволяє особливий, обертальний чи навісний кидок із подальшим котінням за заданими обмеженнями різновидів.

### Виключає

Фізичний кидок контролером руху; нерухома світова пускова установка; передача товаришеві; футбольний удар, обмежений перетином лінії воріт; ручне керування випущеним диском; окремий ген для кожного спортсмена чи назви кидка.

### Ігри-носії

- [`GAME-0564` — Windjammers](../games/s-z/windjammers.md)

## ACT-766

- Назва: Натискати заплановану просторову мітку в момент змикання кільця
- Переглянуто: `2026-11-20`

### Операційне визначення

Гравець торкається стилусом поточної запланованої пронумерованої сенсорної цілі й відриває його в момент, коли навколишнє кільце наближення досягає межі цілі. Вибір правильного місця на екрані й часу контакту задає одну відповідь на подію ритмічної карти, а не фразу інструктора чи довільно націлену атаку в ігровому світі.

### Включає

Мітки Hit Markers в Elite Beat Agents на початковій сенсорній поверхні DS; послідовні числа задають порядок подій, навіть коли цілі просторово накладаються.

### Виключає

Демонстрація інструктора й пізніша відповідь; швидкий штрих із необхідними рухом і відпусканням; ведення тривалого контакту за рухомою кулькою; введення через підлогову панель чи затискання ладу разом з ударом по струнах.

### Ігри-носії

- [`GAME-0566` — Elite Beat Agents](../games/a-f/elite-beat-agents.md)

## ACT-767

- Назва: Утримувати стилус на екрані й вести його за кулькою вздовж заданої фрази
- Переглянуто: `2026-11-20`

### Операційне визначення

Торкнувшись початку фрази в заданий час, гравець тримає стилус на сенсорній поверхні й веде його за рухомою кулькою в заданому нею темпі вздовж показаного шляху. Якщо є позначений зворотний прохід, контакт триває й під час нього, аж доки заданий кінець не дозволить відпускання.

### Включає

Мітки Phrase Markers в Elite Beat Agents; кулька задає час проходження, а стрілка повернення вимагає продовжувати контакт, а не робити нове незалежне натискання.

### Виключає

Довільне малювання будь-якого шляху; відпускання після швидкого штриха; утримання однієї нерухомої кнопки; припущення, що завчасне обведення всього шляху задовольняє пізніші перевірки рухомої кульки.

### Ігри-носії

- [`GAME-0566` — Elite Beat Agents](../games/a-f/elite-beat-agents.md)

## ACT-768

- Назва: Багаторазово обертати контакт стилуса навколо активної обертальної мітки
- Переглянуто: `2026-11-20`

### Операційне визначення

Під час запланованої обертальної події гравець стилусом багаторазово описує кола навколо її центра, обираючи рух за годинниковою стрілкою або проти неї. Так він подає тривалий кутовий поступ замість одного миттєвого натискання.

### Включає

Обертальна мітка Spin Marker в Elite Beat Agents: обидва напрямки приймаються, а продовження обертання після виконання умови ще може дати бонус.

### Виключає

Дискретний покроковий поворот дошки; нерухомий утримуваний контакт; ведення рухомої кульки вздовж заданого шляху фрази; повертання самої консолі.

### Ігри-носії

- [`GAME-0566` — Elite Beat Agents](../games/a-f/elite-beat-agents.md)

## ACT-769

- Назва: Змінювати положення втіленого погляду фізичними рухами голови й тіла
- Переглянуто: `2026-11-20`

### Операційне визначення

Гравець фізично нахиляється, присідає, повертається чи робить доступний крок у межах кімнати, тож відстежувані погляд і його вразливе просторове положення неперервно рухаються відносно місцевого укриття й атак, що наближаються. Це змінює як загрозу зіткнення, так і видимість без вибору віртуального місця призначення чи командування окремим персонажем.

### Включає

SUPERHOT VR на початковому Quest: переміщення втіленої голови за стійку чи подалі від лінії кулі; цей рух також впливає на окремо визначений час світу.

### Виключає

Нерухома мініатюра, яку оглядає незалежний спостерігач; пересування джойстиком; дискретна команда ухилення із заданим вікном невразливості; необмежений безпечний простір у справжній кімнаті.

### Ігри-носії

- [`GAME-0567` — SUPERHOT VR](../games/s-z/superhot-vr.md)

## ACT-770

- Назва: Бити близького ворога рухом відстежуваної стиснутої руки
- Переглянуто: `2026-11-20`

### Операційне визначення

Гравець формує допустимий кулак введенням керування рукою й фізично спрямовує цю відстежувану руку в досяжного ворога. Рух руки та контакт задають спробу ближнього удару замість вибору готової анімації удару чи самого лише дотику до нерухомої цілі захоплення.

### Включає

Удари кулаками через контролери Touch у ранній звичайній кампанії SUPERHOT VR. Обидві руки лишаються просторово керованими; це не оптичне відстеження голих рук.

### Виключає

Спусковий гачок вогнепальної зброї; абстрактна послідовність бойової команди; автоматична контактна шкода від будь-якої нерухомої відкритої долоні; дистанційна здатність вибуху голови.

### Ігри-носії

- [`GAME-0567` — SUPERHOT VR](../games/s-z/superhot-vr.md)

## ACT-771

- Назва: Забирати досяжну зброю просто з руки ворога
- Переглянуто: `2026-11-20`

### Операційне визначення

Гравець підводить доступну відстежувану руку на відстань захоплення допустимої зброї в руці ворога й виконує захоплення. Володіння переходить безпосередньо від ворога до фізичного предмета в руці гравця, перериваючи озброєну загрозу без попередньої вимоги перетворити зброю на вільний предмет для підбирання.

### Включає

Близькі захоплення для роззброєння в SUPERHOT VR; роззброєний ворог може лишитися живим і після короткого збою продовжити неозброєне наближення.

### Виключає

Підбирання вже вільного пістолета; ловіння вже летючого предмета; автоматичне вбивство його власника; забирання будь-якого предмета з довільної відстані.

### Ігри-носії

- [`GAME-0567` — SUPERHOT VR](../games/s-z/superhot-vr.md)

## ACT-772

- Назва: Викопувати один тимчасовий отвір навскіс під персонажем
- Переглянуто: `2026-11-20`

### Операційне визначення

Гравець обирає лівий або правий бік і починає викопувати сусідню нижню цеглину. Ціль і вільне місце збоку мають дозволяти дію. Отвір стає прохідним після завершення копання.

### Включає

Викопування однієї допустимої потрісканої цеглини клавішею U або O у Lode Runner для Apple II.

### Виключає

Стрибок; видалення цеглини безпосередньо під персонажем; довільна дальність; утворення проходу самим початком копання.

### Ігри-носії

- [`GAME-0569` — Lode Runner](../games/g-l/lode-runner.md)

## ACT-773

- Назва: Витрачати зароблений жетон натхнення на одне постійне розблокування споруди
- Переглянуто: `2026-11-20`

### Операційне визначення

Гравець витрачає зароблений жетон натхнення на доступну позицію в переліку споруд. Відкритий кресленик лишається доступним після вибору. Для встановлення споруди й далі потрібні окремі матеріали та придатне місце.

### Включає

Відкриття першого кресленика храму за божественне натхнення після збирання достатньої відданості зі святилища в Cult of the Lamb.

### Виключає

Витрачання будівельних матеріалів на відкриття споруди; миттєве встановлення придбаної споруди; поліпшення вже встановленої споруди; витрачання окремого запасу сили проповідей.

### Ігри-носії

- [`GAME-0570` — Cult of the Lamb](../games/a-f/cult-of-the-lamb.md)

## ACT-774

- Назва: Підкидати м’яч для подачі й другим натисканням виконувати спрямований удар
- Переглянуто: `2026-11-20`

### Операційне визначення

У стані готовності до подачі перше натискання підкидає м’яч і відкриває часовий проміжок для удару. Друге обране натискання виконує допустиму подачу, а напрямок керування націлює її в поле приймача.

### Включає

У Virtua Tennis підкинь м’яч кнопкою A або B, а потім виконай пласку подачу кнопкою A або різану кнопкою B із вибраним напрямком.

### Виключає

Запуск одним натисканням; керування польотом після удару; вибір напрямку без виконання подачі; відбивання м’яча після завершення стану подачі.

### Ігри-носії

- [`GAME-0571` — Virtua Tennis](../games/s-z/virtua-tennis.md)

## ACT-775

- Назва: Обирати звичайний удар або свічку й націлювати відбивання до контакту
- Переглянуто: `2026-11-20`

### Операційне визначення

Поки м’яч летить до гравця, той задає допустимий звичайний удар або свічку й може вибрати напрямок і глибину до контакту ракетки з м’ячем. Рухом до точки перехоплення керує окремо.

### Включає

У Virtua Tennis дістанься до м’яча, задай звичайний удар кнопкою A або свічку кнопкою B чи X і спрямуй удар до контакту.

### Виключає

Прямий вибір анімації замаху; керування вже вдареним м’ячем; сам рух спортсмена; вибір майбутньої тактики лише в меню.

### Ігри-носії

- [`GAME-0571` — Virtua Tennis](../games/s-z/virtua-tennis.md)

## ACT-776

- Назва: Витрачати активну карту зброї для її альтернативної здібності
- Переглянуто: `2026-11-20`

### Операційне визначення

Натискання кнопки скидання з придатною активною картою витрачає цю копію й виконує її альтернативну дію. Гравець віддає можливість стріляти, яку давала ця копія.

### Включає

У Neon White витрать активну карту пістолета Elevate, щоб піднятися в повітрі.

### Виключає

Постріл з утримуваної карти, скидання абстрактної карти без виконання ефекту або здібність, після якої її зброя лишається доступною без зміни.

### Ігри-носії

- [`GAME-0572` — Neon White](../games/m-r/neon-white.md)

## ACT-777

- Назва: Позначати або скасовувати розкопки для вільних землекопів
- Переглянуто: `2026-11-20`

### Операційне визначення

Гравець позначає придатні ділянки землі чи руди для роботи або знімає позначки до її завершення. Будь-який придатний вільний землекоп може взяти завдання й дістатися позначеної ділянки. Вибирати конкретного працівника не потрібно.

### Включає

У Dungeon Keeper познач земляний прохід або золоту жилу, щоб біси самі взялися за доступну роботу.

### Виключає

Безпосереднє копання вручну, викладання вже розчищеної підлоги або наказ вибраному працівнику піти до конкретного джерела ресурсу.

### Ігри-носії

- [`GAME-0573` — Dungeon Keeper](../games/a-f/dungeon-keeper.md)

## ACT-778

- Назва: Піднімати вибрану істоту рукою й опускати її на захоплену ділянку
- Переглянуто: `2026-11-20`

### Операційне визначення

Гравець бере одну або кілька своїх істот у руку з обмеженою місткістю й відпускає їх на придатну захоплену ділянку. Істоти переміщуються цілими й зберігають самостійність, хоча не проходять проміжний маршрут.

### Включає

У Dungeon Keeper підніми кількох жуків і висади їх біля лицаря, що наближається, на своїй сухій ділянці.

### Виключає

Наказ рухатися через точки маршруту, розміщення куплених бійців біля виробничої споруди, вселення в істоту або атака рукою.

### Ігри-носії

- [`GAME-0573` — Dungeon Keeper](../games/a-f/dungeon-keeper.md)

## ACT-779

- Назва: Створювати працівника платним закляттям на захопленій ділянці
- Переглянуто: `2026-11-20`

### Операційне визначення

Коли закляття створення доступне, гравець обирає придатну власну ділянку й платить ціну, що залежить від поточної кількості працівників. На ділянці з’являється новий землекоп, який може брати завдання.

### Включає

Створи біса в Eversmile після спорудження пташника або скористайся передбаченим сценарієм відновлення після втрати останнього біса.

### Виключає

Вербування через портал, купівля за сталою ціною через чергу підготовки або перенесення вже наявного працівника.

### Ігри-носії

- [`GAME-0573` — Dungeon Keeper](../games/a-f/dungeon-keeper.md)

## ACT-780

- Назва: Перетягувати окремий фрагмент на його місце в контурі
- Переглянуто: `2026-11-20`

### Операційне визначення

Торкнися одного доступного фрагмента, перемісти його в межах активного зображення й розмісти в обраній частині цільового контуру. Орієнтація фрагмента лишається заданою.

### Включає

Перенеси фрагмент поточної репліки Флоренс у відповідну порожню частину мовної хмаринки.

### Виключає

Вибір тексту відповіді, обертання твердої деталі, переміщення всієї сцени або перестановка вже завершеної репліки.

### Ігри-носії

- [`GAME-0574` — Florence](../games/a-f/florence.md)

## ACT-781

- Назва: Перетягувати поточну ілюстровану панель, щоб відкрити наступну сцену
- Переглянуто: `2026-11-20`

### Операційне визначення

Перетягни рухому сюжетну панель у потрібному напрямку, щоб подати наступну сцену в заданій послідовності. Жест просуває сам виклад історії. Розміщення фрагментів усередині сцени є окремою взаємодією.

### Включає

Потягни вгору фрагмент побачення чи перехідну панель у Florence, щоб відкрити наступний момент.

### Виключає

Прокручування ігрового годинника, перестановка двох головоломних панелей, перетягування окремого фрагмента репліки або вибір гілки діалогу.

### Ігри-носії

- [`GAME-0574` — Florence](../games/a-f/florence.md)
- [`GAME-0698` — "Song of Bloom"](../games/s-z/song-of-bloom.md)

## ACT-782

- Назва: Витрачати карту з руки на рух або її власну дію
- Переглянуто: `2026-11-20`

### Операційне визначення

Витрать вибрану карту на дозволений рух або на доступну власну дію карти. За одне використання спрацьовує лише один із цих варіантів.

### Включає

Вибери рух із карти «Пайок», щоб пройти на досяжну клітинку, або застосуй пайок для відновлення здоров’я.

### Виключає

Рух незалежно від карт у руці, автоматичне спрацьовування карт або спеціальна карта руху без іншої дії.

### Ігри-носії

- [`GAME-0575` — Metal Gear Acid](../games/m-r/metal-gear-acid.md)

## ACT-783

- Назва: Забирати вибраний чужий предмет до інвентарю без дозволу
- Переглянуто: `2026-11-20`

### Операційне визначення

Вибери досяжний чужий предмет і забери його без дозволу власника. Предмет потрапляє до інвентарю, а дія вважається несанкціонованою незалежно від подальшої реакції системи.

### Включає

Забери смолу сильфію просто з прилавка Десія без оплати.

### Виключає

Купівля предмета, отримання від власника, підбирання вільного предмета дотиком або реакція міста на крадіжку.

### Ігри-носії

- [`GAME-0576` — The Forgotten City](../games/s-z/the-forgotten-city.md)

## ACT-784

- Назва: Перемістити окремого пасажира на сидіння або стояче місце
- Переглянуто: `2026-11-20`

### Операційне визначення

Гравець обирає одного пасажира з поточної групи й розміщує або переставляє його на вибране доступне місце в салоні. Пасажир зберігає свою особу й побажання.

### Включає

Перетягнути пасажира, який чекає або вже їде барселонським автобусом, на сидіння чи позначене стояче місце.

### Виключає

Вибір повторюваного символу з абстрактного набору, розміщення цілої групи однією дією, зміна порядку без вибору місця, відправлення автобуса.

### Ігри-носії

- [`GAME-0579` — Is This Seat Taken?](../games/g-l/is-this-seat-taken.md)

## ACT-785

- Назва: Розплавити вибране кріплення точковим різаком
- Переглянуто: `2026-11-20`

### Операційне визначення

Гравець утримує вузький промінь на придатному кріпленні, доки воно не розплавиться. Коли гравець відпускає різак чи відводить його, нагрівання припиняється. Яка деталь звільниться, залежить від уцілілих кріплень.

### Включає

Утримувати промінь Stinger на виділеному кріпленні всередині навчального Mackerel.

### Виключає

Розрізання опори жестом, підрив заряду, миттєве натискання або негайне видалення всіх приєднаних деталей.

### Ігри-носії

- [`GAME-0581` — "Hardspace: Shipbreaker"](../games/g-l/hardspace-shipbreaker.md)

## ACT-786

- Назва: Продовжити підготовлений шлях, утримуючи дію в його кінці
- Переглянуто: `2026-11-20`

### Операційне визначення

У поточному кінці маршруту гравець утримує дію взаємодії, щоб продовжити доступний відрізок уздовж коридору етапу. Коли гравець відпускає кнопку, прокладання припиняється, а готовий відрізок зберігається.

### Включає

Утримувати взаємодію в кінці Шляху духів, щоб прокласти його далі на перевалі Мьоко.

### Виключає

Натискання на віддалену ціль для вільного пошуку шляху, довільні відгалуження, керування кожним кроком супровідної особи або миттєва підготовка всього коридору.

### Ігри-носії

- [`GAME-0583` — "Kunitsu-Gami: Path of the Goddess"](../games/g-l/kunitsu-gami-path-of-the-goddess.md)

## ACT-787

- Назва: Брати й відпускати рухомий предмет відстежуваною рукою
- Переглянуто: `2026-11-20`

### Операційне визначення

Вибери доступний рухомий предмет рукою, рух якої відстежує гра. Візьми його й обери, де відпустити або куди покласти.

### Включає

Взяти годинник дослідника, покласти його у відкритий рюкзак, а після повернення відпустити в приймальний лоток Ванно.

### Виключає

Підбирання дотиком, вибір рядка інвентарю, хват за нерухому опору для лазіння та передача предмета персонажу без просторової дії.

### Ігри-носії

- [`GAME-0702` — "Escaping Wonderland"](../games/a-f/escaping-wonderland.md)
- [`GAME-0680` — "Ghost Town"](../games/g-l/ghost-town.md)
- [`GAME-0585` — Into the Radius](../games/g-l/into-the-radius.md)
- [`GAME-0689` — "Shadow Point"](../games/s-z/shadow-point.md)

## ACT-788

- Назва: Відновлювати готовність окремим спорядженим магазином
- Переглянуто: `2026-11-20`

### Операційне визначення

Щоб відновити готовність зброї, візьми окремий магазин із власним запасом набоїв і приєднай його окремим рухом руки.

### Включає

Взяти споряджений магазин і вставити його у зброю, яку тримаєш у грі. Запас набоїв визначає вміст цього магазина, а не спільний лічильник.

### Виключає

Автоматичне поповнення, перезаряджання з абстрактного лічильника, постійне поліпшення та оцінка за натискання в потрібну мить.

### Ігри-носії

- [`GAME-0585` — Into the Radius](../games/g-l/into-the-radius.md)

## ACT-789

- Назва: Піднімати й опускати фотокамеру з видошукачем від першої особи
- Переглянуто: `2026-11-21`

### Операційне визначення

Гравець перемикає персонажа з камерою між звичайним керуванням у просторі та кадруванням від першої особи. Перемикання змінює прицілювання й рух без натискання спуску затвора. Після виходу з видошукача повертається звичайне керування.

### Включає

Підняти Camera Obscura, щоб навести її на Bound Man, і опустити, щоб відійти між знімками.

### Виключає

Спуск затвора (ACT-502), збільшення в прицілі вогнепальної зброї (ACT-679), вільна камера чи камера спостерігача і поворот камери, що слідує за персонажем.

### Ігри-носії

- [`GAME-0591` — Fatal Frame](../games/a-f/fatal-frame.md)
- [`GAME-0732` — "TOEM"](../games/s-z/toem.md)

## ACT-790

- Назва: Позначати доступний фізичний предмет спрямованим дотиком
- Переглянуто: `2026-11-21`

### Операційне визначення

Гравець спрямовано дотягується до придатного фізичного предмета чи вдаряє по ньому, щоб вибрати його для окремої подальшої дії. Дотик позначає ціль, але сам цієї дії не виконує. Предмет залишається окремим тілом у світі.

### Включає

У Bionic Bay вдарити по ближньому ящику, щоб позначити його для подальшого Обміну, поки він стоїть на опорі або рухається за законами фізики.

### Виключає

Віддалене оптичне позначення (ACT-405), перенесення ящика на фіксованій відстані (ACT-048) й обмін місцями під час кроку прямо на сусідню істоту (ACT-067).

### Ігри-носії

- [`GAME-0594` — "Bionic Bay"](../games/a-f/bionic-bay.md)

## ACT-791

- Назва: Натиснути один раз на завершальній долі групи
- Переглянуто: `2026-11-21`

### Операційне визначення

Гравець натискає одну кнопку без вибору цілі на очікуваній завершальній долі вже поданої групи. Під час попередніх імпульсів він не натискає.

### Включає

Один натиск A після шести вступних імпульсів у першому звичайному одиночному завданні Rhythm Doctor.

### Виключає

Змах або вибір позначки на екрані, поєднання кількох кнопок, натиск на кожній долі, утримування кнопки або вибір моменту атаки під спільний ритм.

### Ігри-носії

- [`GAME-0595` — "Rhythm Doctor"](../games/m-r/rhythm-doctor.md)

## ACT-792

- Назва: Навести пускову установку зі складеним бійцем до старту
- Переглянуто: `2026-11-21`

### Операційне визначення

Гравець змінює напрямок нерухомої установки зі складеним бійцем, яким згодом керуватиме. Наприкінці спільного відліку обидві установки спрацьовують автоматично. Гравець визначає траєкторію, а момент запуску задає відлік.

### Включає

У першому двобої на Basic Arena наведи установку Ray 01, щоб його куб полетів до обраного укриття.

### Виключає

Ручний випуск витратного снаряда, вибір точки появи без польоту між позиціями, розгортання нового самостійного бійця й прискорення подальшого відліку розгортання.

### Ігри-носії

- [`GAME-0596` — "Custom Robo"](../games/a-f/custom-robo.md)

## ACT-793

- Назва: Застосувати встановлену непряму зброю з окремим наведенням
- Переглянуто: `2026-11-21`

### Операційне визначення

Гравець запускає окремий вибуховий пристрій із встановленої зброї, задаючи точку на арені або початковий напрямок відповідно до способу атаки. Пристрій далі рухається до зіткнення чи вибуху сам, а боєць може виконувати інші дії.

### Включає

У вступному двобої Custom Robo кнопка R запускає стандартну бомбу до позначки, а L випускає стандартний модуль у заданому початковому напрямку. Бомба летить до точки, а модуль може рухатися до цілі.

### Виключає

Заміна деталі під час бою, витрачання переносної гранати, звичайний прямий постріл і подальше керування випущеним пристроєм тим самим натиском.

### Ігри-носії

- [`GAME-0596` — "Custom Robo"](../games/a-f/custom-robo.md)

## ACT-794

- Назва: Вибрати напрямок і закинути принаду на волосіні
- Переглянуто: `2026-11-21`

### Операційне визначення

Гравець переміщує мітку закидання з нерухомого місця ловлі, обирає досяжну точку й закидає принаду. Вона падає у вибрану точку та лишається на волосіні, щоб нею можна було далі керувати й підтягнути її назад.

### Включає

Пересунь мітку над водою біля Lodge і натисни A на звичайному контролері, щоб закинути обрану принаду.

### Виключає

Прицільний кидок без волосіні для повернення, обов’язковий вибір сили кидка в іншій версії, подальша підсічка або підмотування.

### Ігри-носії

- [`GAME-0598` — "Sega Bass Fishing"](../games/s-z/sega-bass-fishing.md)

## ACT-795

- Назва: Підсікти рибу в мить клювання
- Переглянуто: `2026-11-21`

### Операційне визначення

Коли риба клює на принаду, гравець окремим рухом підсікає її впродовж короткої нагоди. Вдала підсічка чіпляє рибу до волосіні й відкриває виважування, після якого улов можна витягнути.

### Включає

Зі звичайним контролером Dreamcast і типовими налаштуваннями потягни аналоговий важіль униз, коли окунь схопить принаду.

### Виключає

Звичайне підмотування до контакту, автоматична підсічка від контакту або зарахування риби самим рухом підсічки.

### Ігри-носії

- [`GAME-0598` — "Sega Bass Fishing"](../games/s-z/sega-bass-fishing.md)

## ACT-796

- Назва: Окремо підмотувати волосінь і спрямовувати вудлище
- Переглянуто: `2026-11-21`

### Операційне визначення

Гравець може почати або припинити підмотування й незалежно спрямовувати вудлище, щоб вести принаду або виважувати підсічену рибу. Можна припинити крутити котушку й далі реагувати вудлищем.

### Включає

Підмотуй будь-яким курком, а вудлище спрямовуй аналоговим важелем. За надмірного натягу відпусти курок і спрямуй вудлище проти руху риби.

### Виключає

Одне натискання, яке відразу зараховує рибу, автоматичне повернення без керування вудлищем, команда тягнути незачеплену ціль або окрема початкова підсічка.

### Ігри-носії

- [`GAME-0598` — "Sega Bass Fishing"](../games/s-z/sega-bass-fishing.md)

## ACT-797

- Назва: Затиснути й відпустити кнопку стрибка, щоб дістатися вище
- Переглянуто: `2026-11-21`

### Операційне визначення

Коли дошка спирається на придатну поверхню, гравець може затиснути кнопку стрибка й відпустити її для високого стрибка. Напрямок під’їзду й момент відпускання обирають до відриву від опори.

### Включає

У синій залі на початку гри підказка «Високий стрибок» пропонує затиснути й відпустити хрестик, щоб дістатися сходів за розривом підлоги.

### Виключає

Повторне натискання стрибка в повітрі, збережений стрибок після сходу з краю, відрив однакової висоти за будь-якої підготовки або витрата запасу прискорення замість стрибка.

### Ігри-носії

- [`GAME-0687` — "Denshattack!"](../games/a-f/denshattack.md)
- [`GAME-0615` — "Skate Story"](../games/s-z/skate-story.md)
- [`GAME-0599` — "Sword of the Sea"](../games/s-z/sword-of-the-sea.md)

## ACT-798

- Назва: Розпочати кидок відповідно до позиції на майданчику
- Переглянуто: `2026-11-21`

### Операційне визначення

Гравець із м’ячем може виконати спробу закинути його однією контекстною командою. Позиція й напрямок руху визначають кидок у стрибку, лейап або данк. Затиснуті кнопки турбо дають змогу виконати складніший варіант.

### Включає

Натисни кружок за дугою для дальнього кидка або підступи до кільця й натисни його для завершення зблизька. Поєднання з турбо дають складніші варіанти.

### Виключає

Вибір точності відпускання за окремою шкалою, передача м’яча, стрибок на підбиранні або активація особливого кидка, що змінює обидва рахунки.

### Ігри-носії

- [`GAME-0600` — "NBA Street Vol. 2"](../games/m-r/nba-street-vol-2.md)

## ACT-799

- Назва: Виконати трюк із м’ячем із можливим підсиленням турбо
- Переглянуто: `2026-11-21`

### Операційне визначення

Гравець із м’ячем виконує трюк залежно від позиції та затиснутих кнопок турбо. Вдалий трюк може змусити захисника втратити рівновагу й дає очки в окремому заліку за трюки.

### Включає

Натисни квадрат перед захисником і в наступних атаках змінюй поєднання кнопок турбо, щоб виконувати різні трюки.

### Виключає

Звичайна передача, безперервний ривок, задане святкування після влучання або розрахунок очок за всю комбінацію.

### Ігри-носії

- [`GAME-0600` — "NBA Street Vol. 2"](../games/m-r/nba-street-vol-2.md)

## ACT-800

- Назва: Обрати, як використати готовий особливий кидок
- Переглянуто: `2026-11-21`

### Операційне визначення

Команда з м’ячем і готовим особливим кидком може виконати посилену спробу. За відповідних умов можна відкласти першу нагоду або використати поточну, щоб скасувати відкладену нагоду суперника. Кожен варіант має власну команду та передумови.

### Включає

Кружок із двома кнопками турбо запускає спробу Gamebreaker, Select відкладає першу нагоду, а турбо разом із Select скасовує відкладену нагоду суперника.

### Виключає

Звичайний кидок без готової нагоди, автоматичне відкладання, скасування ще не відкладеної нагоди й автоматичний розрахунок рахунку.

### Ігри-носії

- [`GAME-0600` — "NBA Street Vol. 2"](../games/m-r/nba-street-vol-2.md)

## ACT-801

- Назва: Обрати чисту касету й дику істоту для запису
- Переглянуто: `2026-11-21`

### Операційне визначення

Один допущений учасник команди своєю командою на раунд обирає й витрачає одну сумісну чисту касету на одну допустиму дику істоту. Команда призначає спробу скопіювати її форму. Для запису учасник полишає поточну бойову форму.

### Включає

Обери «Запис», звичайну касету й навчального Домінота. Учасник, який записує, стає людиною, а супутникові можна призначити окрему команду.

### Виключає

Ув’язнення й вилучення істоти, пряма атака зі шкодою від зброї, копіювання союзника або вибір уже наявної касети для перетворення.

### Ігри-носії

- [`GAME-0601` — "Cassette Beasts"](../games/a-f/cassette-beasts.md)

## ACT-802

- Назва: Відтворити наявну касету, щоб набути її форми в бою
- Переглянуто: `2026-11-21`

### Операційне визначення

Під час вибору команд у бою гравець обирає допустиму записану касету й призначає її відтворення. Від цього той самий учасник набуває обраної форми з її набором прийомів.

### Включає

Отримавши в навчанні касету Домінота, обери її в меню форм і перетворися на Домінота. Дикий оригінал лишається на боці суперника.

### Виключає

Виклик окремої самостійної істоти, вибір зовнішнього вигляду, передання керування іншій постійній людині або злиття двох союзних тіл.

### Ігри-носії

- [`GAME-0601` — "Cassette Beasts"](../games/a-f/cassette-beasts.md)

## ACT-803

- Назва: Утримувати посадкове гальмування дельтаплана
- Переглянуто: `2026-11-21`

### Операційне визначення

Під час безмоторного польоту гравець утримує кнопку посадкового гальмування, щоб сповільнити рух уперед і підготувати пілота до приземлення на ноги.

### Включає

Утримуй A біля майданчика «Гнізда альбатроса», щоб пілот виставив ноги. Якщо відпустити кнопку до контакту із землею, стан пілота під час посадки може змінитися.

### Виключає

Лише зміна нахилу крила, гальмування коліс на смузі, розкриття нового крила або автоматична посадка.

### Ігри-носії

- [`GAME-0602` — "Pilotwings 64"](../games/m-r/pilotwings-64.md)

## ACT-804

- Назва: Замінити одну деталь велосипеда на наявну
- Переглянуто: `2026-11-21`

### Операційне визначення

Гравець обирає місце для деталі велосипеда й установлює сумісну деталь зі своїх запасів замість поточної. Керованим лишається той самий велосипед.

### Включає

Отримавши колесо для міста на острові Лунардо, вибери його в комірці заднього колеса в меню велосипеда.

### Виключає

Заміна всього велосипеда, відкриття скриньки з деталлю, встановлення модифікатора коштом ліміту модифікацій або зміна лише кольору.

### Ігри-носії

- [`GAME-0603` — "Wheel World"](../games/s-z/wheel-world.md)

## ACT-805

- Назва: Обрати іншу життєву розвилку для створення фахівця
- Переглянуто: `2026-11-21`

### Операційне визначення

Гравець обирає й підтверджує інший варіант давнього рішення на шкалі життя персонажа. Від цього залежить, якого нового члена екіпажу зі своєю спеціальністю буде створено.

### Включає

На квантовому комп’ютері вибери «Залишитися» (Staying Behind), щоб створити першого Техніка.

### Виключає

Перепризначення наявного працівника, вибір класу спорядження, репліка без появи нового члена екіпажу або повтор зі скасуванням поточного стану світу.

### Ігри-носії

- [`GAME-0604` — "The Alters"](../games/s-z/the-alters.md)

## ACT-806

- Назва: Позначати відмінності між відповідними деталями двох зразків
- Переглянуто: `2026-11-21`

### Операційне визначення

Гравець обирає позначені авторами відмінні деталі на двох одночасно показаних зразках доказів. Зараховане порівняння зберігає конкретні розбіжності як зачіпку для розслідування.

### Включає

Порівняй підписи в гостьовій книзі й листі про від’їзд, перевіривши форму відповідних літер.

### Виключає

Лише відкриття двох документів, переписування одного слова, порівняння у вільних нотатках або подання остаточної гіпотези.

### Ігри-носії

- [`GAME-0606` — "The Séance of Blake Manor"](../games/s-z/the-seance-of-blake-manor.md)

## ACT-807

- Назва: Струсити утримувану ціль, не кидаючи її
- Переглянуто: `2026-11-21`

### Операційне визначення

Поки герой тримає придатну ціль, гравець повторює окрему команду напрямку, щоб струсити її й не відпустити.

### Включає

Маріна хапає черв’яка за голову і кілька разів натискає вниз перед кидком.

### Виключає

Струшування контролера, удар по предмету ззовні, відпускання чи кидок і сама поява предмета.

### Ігри-носії

- [`GAME-0607` — "Mischief Makers"](../games/m-r/mischief-makers.md)

## ACT-808

- Назва: Керувати поточною кулінарною дією за підказкою
- Переглянуто: `2026-11-21`

### Операційне визначення

Поки активна підказка, гравець виконує поточну дію на контролері: утримує кнопку, натискає її повторно або влучає в потрібний момент.

### Включає

У Dosa Divas гравець утримує кнопку, щоб налити до позначки, а на наступному етапі повторно натискає вказану кнопку.

### Виключає

Робота стилусом по продукту, вибір рецепта без приготування, вчасне натискання під час атаки або автоматичне приготування.

### Ігри-носії

- [`GAME-0608` — "Dosa Divas"](../games/a-f/dosa-divas.md)

## ACT-809

- Назва: Утримувати команду зміни швидкості незалежно від кута обертання
- Переглянуто: `2026-11-21`

### Операційне визначення

Задаючи напрямок руху, гравець може утримувати одну чи обидві кнопки швидкості. Це змінює швидкість переміщення без прямого вибору кута апарата.

### Включає

У Kuru Kuru Kururin хрестовина рухає апарат, а утримання однієї або обох кнопок пришвидшує переміщення.

### Виключає

Керування кутом, прискорення з часом утримання напрямку, витрата запасу підсилення або вибір сталої швидкості перед заїздом.

### Ігри-носії

- [`GAME-0609` — "Kuru Kuru Kururin"](../games/g-l/kuru-kuru-kururin.md)

## ACT-810

- Назва: Спрямовувати потік снарядів незалежно від руху
- Переглянуто: `2026-11-21`

### Операційне визначення

Під час бою гравець може безперервно змінювати напрямок повторних пострілів незалежно від напрямку руху персонажа.

### Включає

Воїн рухається поперек арени й водночас спрямовує кулі на фланг або в прогалину у ворожому строю.

### Виключає

Нерухома пускова установка з одним пострілом за хід, одноразовий кидок або автоматична атака, напрямок якої визначає гра.

### Ігри-носії

- [`GAME-0610` — "BALL x PIT"](../games/a-f/ball-x-pit.md)
- [`GAME-0734` — "Nex Machina"](../games/m-r/nex-machina.md)

## ACT-811

- Назва: Викликати істоту для захоплення ділянки або вторгнення
- Переглянуто: `2026-11-21`

### Операційне визначення

Після зупинки гравець вибирає придатну карту істоти й оплачує виклик. Істота займає вільну землю або стає нападником проти її захисника.

### Включає

Виклик на вільній ділянці Даннана закріплює її за гравцем. На водній ділянці Райверна Мінотавр вступає в бій із Вовком.

### Виключає

Розіграш карти землі, переміщення істоти на довільну ділянку, предмет у бою або отримання землі лише за зупинку на ній.

### Ігри-носії

- [`GAME-0611` — "Culdcept"](../games/a-f/culdcept.md)

## ACT-812

- Назва: Виконувати дію з однією доступною власною ділянкою
- Переглянуто: `2026-11-21`

### Операційне визначення

На етапі керування територією гравець вибирає одну власну ділянку, доступну з пройденого маршруту або особливої клітинки, і одну дію. Можна підвищити рівень, змінити стихію, замінити або пересунути істоту.

### Включає

Після точної зупинки біля замку в Даннані можна вибрати власну ділянку та поліпшити землю чи замінити істоту.

### Виключає

Керування будь-якою землею без умов, пряме привласнення вільної ділянки, автоматичне поліпшення після кола або виклик у порожнє місце.

### Ігри-носії

- [`GAME-0611` — "Culdcept"](../games/a-f/culdcept.md)

## ACT-813

- Назва: Виконувати вивчений кидок того самого знаряддя без шнурка
- Переглянуто: `2026-11-21`

### Операційне визначення

Коли знаряддя доступне, гравець утримує кнопку вивченого прийому й натискає звичайну кнопку кидка. Знаряддя від’єднується від шнурка й летить далі, ніж за звичайного кидка.

### Включає

На Nintendo Switch поєднання ZR і Y посилає йо-йо через воду до перемикача, якого звичайний кидок не дістає.

### Виключає

Кидок іншого витратного предмета, необмежене розтягування цілого шнурка, підтягування персонажа гаком або керування польотом після випуску.

### Ігри-носії

- [`GAME-0612` — "Pipistrello and the Cursed Yoyo"](../games/m-r/pipistrello-and-the-cursed-yoyo.md)

## ACT-814

- Назва: Накрити персонажа, щоб він випустив знаряддя
- Переглянуто: `2026-11-21`

### Операційне визначення

Під час сутички гравець вибирає з інвентарю покривало й накидає його на персонажа, який тримає потрібне знаряддя. Це заважає персонажеві ним орудувати, без окремого удару чи добровільної передачі.

### Включає

Мік накриває зібраним брезентом розбурханого пасажира після того, як той замахнувся прутом.

### Виключає

Надягання захисного одягу, застосування предмета до дверного механізму, вмовляння обмінятися, передача предмета на прохання або підняття випущеного знаряддя.

### Ігри-носії

- [`GAME-0613` — "The Drifter"](../games/s-z/the-drifter.md)

## ACT-815

- Назва: Прокопувати хід і виринати в придатному місці
- Переглянуто: `2026-11-21`

### Операційне визначення

На придатній клітинці гравець подає команду копати, щоб перейти в підземний шар кімнати або повернутися на поверхню. Під землею можна переміститися й вилізти в іншому місці через наявний або новий отвір.

### Включає

У Mole Mania кнопка A змінює шар, а хрестовина веде під землею на інший бік поверхневої перешкоди.

### Виключає

Спуск фіксованою драбиною до іншої кімнати, падіння зі штрафом, викопування захованої нагороди або перенесення поверхневої кулі під землю.

### Ігри-носії

- [`GAME-0614` — "Mole Mania"](../games/m-r/mole-mania.md)

## ACT-816

- Назва: Утримувати захоплений предмет до готовності до кидка
- Переглянуто: `2026-11-21`

### Операційне визначення

Гравець хапає сусідній предмет, стоїть нерухомо й утримує захоплення до сигналу готовності. Він обирає напрямок, і предмет далі рухається сам. Звичайне штовхання чи тягнення того самого предмета такої підготовки не потребує.

### Включає

Мадді утримує B біля чорної кулі, чекає світіння й обирає напрямок до східної перепони або кидає кулю назад.

### Виключає

Штовхання сусіднього предмета на крок, коротке захоплення без підготовки до кидка, вибір предмета в інвентарі або керування вже випущеною кулею.

### Ігри-носії

- [`GAME-0614` — "Mole Mania"](../games/m-r/mole-mania.md)

## ACT-817

- Назва: Розміщувати заряд поруч або після відпускання захоплення цілі
- Переглянуто: `2026-11-21`

### Операційне визначення

Коротке натискання розміщує звичайний заряд у поточній позиції керованого персонажа. Утримуй ту саму кнопку, щоб захопити допустиму ціль, і відпусти, щоб розмістити заряд на ній. Заряд очікує окремої команди.

### Включає

Натисни «квадрат», щоб поставити звичайний заряд поруч. Або затисни цю кнопку, захопи допустимий пристрій чи опору чотириногої машини й відпусти, щоб розмістити заряд.

### Виключає

Бомба з автоматичним запалом, снаряд, що спрацьовує після відпускання, постійне захоплення для руху навколо цілі або застосування спеціальної рідини окремою кнопкою.

### Ігри-носії

- [`GAME-0616` — Silent Bomber](../games/s-z/silent-bomber.md)

## ACT-818

- Назва: Давати команду підриву розміщених зарядів
- Переглянуто: `2026-11-21`

### Операційне визначення

Гравець обирає момент, коли вже розміщені заряди почнуть спрацьовувати. Команда стосується всього набору, незалежно від того, чи заряд поставлено поруч, чи на допустиму віддалену ціль.

### Включає

Після розміщення зарядів на палубі або допустимих цілях один раз натисни «трикутник». Починається спрацювання вже поставлених зарядів.

### Виключає

Натискання кнопки встановлення, відпускання прицілу до розміщення, очікування автоматичного запалу або окрема команда для кожного заряду.

### Ігри-носії

- [`GAME-0616` — Silent Bomber](../games/s-z/silent-bomber.md)

## ACT-819

- Назва: Вибирати спосіб чуттєвого огляду обраного артефакту
- Переглянуто: `2026-11-21`

### Операційне визначення

Відкрий детальний огляд обраного артефакту й вибери один із доступних способів сприйняття. Під час огляду того самого предмета спосіб можна змінити. Огляд відкриває відомості про предмет і не передає його відвідувачеві.

### Включає

Оглянь окремий зуб у Strange Antiquities і перемикай доступні способи сприйняття, перш ніж вирішиш, що запропонувати.

### Виключає

Автоматичне відкриття назви при вході в огляд, пошукове чуття для відстеження слідів, застосування інструмента до іншого предмета та подальша пропозиція відвідувачеві.

### Ігри-носії

- [`GAME-0617` — Strange Antiquities](../games/s-z/strange-antiquities.md)

## ACT-820

- Назва: Пробити доступну ділянку породи в обраному напрямку
- Переглянуто: `2026-11-21`

### Операційне визначення

Гравець спрямовує удар персонажа в досяжну тверду породу, обираючи найближчу поверхню або вертикальний напрямок. Удар може звільнити зайнятий породою простір, у який потім можна ввійти.

### Включає

Удари вниз крізь шар ґрунту до Давньої печери, а далі підхід до каменя, що приховує самоцвіт на Острові Злитків у Donkey Kong Bananza.

### Виключає

Вибір окремого блока для видобутку інструментом, перенесення матеріалу до запасів самим вирізанням, перемикання на окремий заздалегідь заданий підземний рівень або удар по окремому ворогу.

### Ігри-носії

- [`GAME-0619` — Donkey Kong Bananza](../games/a-f/donkey-kong-bananza.md)

## ACT-821

- Назва: Ударити долонями об землю, щоб обстежити ділянку чи зібрати знахідки
- Переглянуто: `2026-11-21`

### Операційне визначення

Гравець ударяє долонями об землю, і дія поширюється навколо персонажа. Одна команда може зібрати доступні предмети, що лежать вільно, і на короткий час показати розташування придатних прихованих цілей поблизу.

### Включає

Команда удару долонями (Hand Slap), яку показують у першій Давній печері. Спершу підказка пояснює збирання предметів поблизу, пізніше — пошук прихованого.

### Виключає

Пробивання тунелю в обраному напрямку, прилад для сканування однієї вибраної цілі, постійне відкриття мапи, зарахування вмурованого самоцвіту лише від пошуку або обов’язкове спрацювання обох ефектів від кожного удару.

### Ігри-носії

- [`GAME-0619` — Donkey Kong Bananza](../games/a-f/donkey-kong-bananza.md)

## ACT-822

- Назва: Перемкнути активну зброю на підготовлену комірку під час бою
- Переглянуто: `2026-11-21`

### Операційне визначення

Під час бою гравець відкриває меню підготовленої зброї, вибирає одну з наявних комірок і підтверджує зброю для наступних атак. Доки меню відкрите, персонаж не може рухатися чи стріляти.

### Включає

Вибір іншої комірки зброї Force кнопкою A, напрямком і підтвердженням у Alien Soldier.

### Виключає

Підбирання зброї, випадкова заміна комплекту, перемикання зброї машини без меню, що обмежує дії, зупинка бою або поєднання атак із двох комірок.

### Ігри-носії

- [`GAME-0620` — Alien Soldier](../games/a-f/alien-soldier.md)

## ACT-823

- Назва: Перемикати нерухому стрільбу й стрільбу під час руху
- Переглянуто: `2026-11-21`

### Операційне визначення

Присівши, гравець перемикає режим стрільби. У нерухомому режимі персонаж на землі або в зависанні тримається на місці під час звичайної тривалої стрільби й може змінювати напрямок вогню. Рухомий режим дозволяє зміщуватися під час стрільби й витрачає більше енергії вибраної зброї.

### Включає

Білий нерухомий і золотий рухомий режими стрільби Епсилона в Alien Soldier.

### Виключає

Стійка лише для вигляду, постійно незалежне від руху прицілювання без другого режиму, вибір іншої зброї або припущення, що нерухомий режим зупиняє персонажа в польоті.

### Ігри-носії

- [`GAME-0620` — Alien Soldier](../games/a-f/alien-soldier.md)

## ACT-824

- Назва: Зависнути для стрільби повторною командою стрибка
- Переглянуто: `2026-11-21`

### Операційне визначення

Під час стрибка повторна команда стрибка зупиняє персонажа в повітрі в позиції, з якої можна стріляти. Наступна команда стрибка із зависання може знову спрямувати рух угору.

### Включає

Зависання Епсилона та наступний стрибок вище в Alien Soldier.

### Виключає

Подвійний стрибок без зупинки в повітрі, планерування зі спаданням, прикріплення до твердої стелі або положення, з якого не можна стріляти.

### Ігри-носії

- [`GAME-0620` — Alien Soldier](../games/a-f/alien-soldier.md)

## ACT-825

- Назва: Виконати захищений бічний ривок із поточної висоти
- Переглянуто: `2026-11-21`

### Операційне визначення

Гравець натискає сумісну з поточним положенням комбінацію стрибка й робить швидкий бічний ривок в обраному напрямку на поточній висоті над землею. Під час ривка тіло захищене від зіткнень із ворогами та від їхніх атак.

### Включає

Звичайний нульовий ривок (Zero Teleport) з японського посібника Alien Soldier, щоб перетнути лінію атаки чи віддалитися для наступного пострілу.

### Виключає

Телепортація у вибрану кінцеву точку без проміжного руху, наведення на вибрану ціль, постійний захист після прибуття або обов’язкове посилення ривка до атаки незалежно від здоров’я.

### Ігри-носії

- [`GAME-0620` — Alien Soldier](../games/a-f/alien-soldier.md)

## ACT-826

- Назва: Двічі натиснути стрільбу, щоб виставити щит перед собою
- Переглянуто: `2026-11-21`

### Операційне визначення

Гравець двічі швидко натискає кнопку стрільби, щоб ненадовго виставити захисне поле перед персонажем. Поле діє на снаряди, що наближаються до нього, без вибору нападника.

### Включає

Контрполе (Counter Force) на кнопці B в Alien Soldier проти снаряда боса, що відскакує.

### Виключає

Утримання звичайного блоку, відбиття кожного снаряда до джерела, шкода від звичайної тривалої стрільби або підказана контратака проти одного ворога в ближньому бою.

### Ігри-носії

- [`GAME-0620` — Alien Soldier](../games/a-f/alien-soldier.md)

## ACT-827

- Назва: Спрямувати машину крізь один із порталів, щоб обрати спільну трасу
- Переглянуто: `2026-11-21`

### Операційне визначення

Під час гонки в місці розгалуження гонщик, який має право вибору як лідер, визначає наступну спільну трасу, в’їжджаючи в один із запропонованих порталів.

### Включає

В’їзд у кільце переходу (Travel Ring) на межі першого й другого кіл звичайної гонки Sonic Racing: CrossWorlds.

### Виключає

Вибір траси в меню перед гонкою, проїзд іншого гонщика вже вибраним маршрутом, індивідуальне скорочення або застосування особистого предмета для переміщення.

### Ігри-носії

- [`GAME-0621` — "Sonic Racing: CrossWorlds"](../games/s-z/sonic-racing-crossworlds.md)

## ACT-828

- Назва: Виконати трюки в повітрі, щоб прискоритися після приземлення
- Переглянуто: `2026-11-21`

### Операційне визначення

Під час придатного відрізка в повітрі гравець виконує один чи кілька трюків командами напрямку. Гра враховує розпізнані трюки, щоб визначити силу прискорення під час приземлення.

### Включає

Трюки в повітрі (Air Tricks) і лічильник градусів перед повторним прискоренням на землі в Sonic Racing: CrossWorlds.

### Виключає

Саме лише кермування в повітрі, трюк лише заради очок, витрата запасу пального вручну або прискорення від самого відриву від землі.

### Ігри-носії

- [`GAME-0621` — "Sonic Racing: CrossWorlds"](../games/s-z/sonic-racing-crossworlds.md)

## ACT-829

- Назва: Спрямовувати ввімкнений бур крізь проникний ґрунт у тій самій площині
- Переглянуто: `2026-11-21`

### Операційне визначення

Гравець тримає особистий бур увімкненим, щоб увійти в придатний м’який ґрунт і спрямувати персонажа обраним шляхом усередині. Через відкриту межу персонаж може вийти у вільний простір.

### Включає

Керування Пеппер із ввімкненим буром на вигнутому шляху в м’якому ґрунті першого рівня Lost Claim.

### Виключає

Вибір окремого блока для руйнування, перехід на окремий підземний шар, робота встановленого бура або активація фіксованого підземного проходу.

### Ігри-носії

- [`GAME-0622` — "Pepper Grinder"](../games/m-r/pepper-grinder.md)

## ACT-830

- Назва: Прискоритися в ґрунті перед виходом, щоб подовжити політ
- Переглянуто: `2026-11-21`

### Операційне визначення

Під час буріння в придатному ґрунті гравець подає команду прискорення до виходу у вільний простір. Прискорення ближче до межі збільшує швидкість виходу й подовжує подальший політ в обраному напрямку.

### Включає

Натискання кнопки стрибка для прискорення в піщаній ділянці перед вильотом через розрив на рівні Lost Claim.

### Виключає

Звичайний стрибок з опори, додатковий стрибок уже в повітрі, запуск гарматою за фіксованою траєкторією або прискорення лише під час приземлення.

### Ігри-носії

- [`GAME-0622` — "Pepper Grinder"](../games/m-r/pepper-grinder.md)

## ACT-831

- Назва: Провести стилусом через супротивника, щоб завдати удару мечем
- Переглянуто: `2026-11-21`

### Операційне визначення

Гравець проводить коротку лінію через видимого супротивника на тому самому сенсорному екрані, де керує рухом. Гра розпізнає цей жест як команду ударити мечем.

### Включає

У Ninja Gaiden Dragon Sword гравець проводить стилусом через супротивника, щоб виконати удар із землі.

### Виключає

Дотик для руху чи кидка, лінія прицілювання з окремим підтвердженням, поворот важелем перед натисканням кнопки атаки або вибір прийому зі списку.

### Ігри-носії

- [`GAME-0625` — "Ninja Gaiden Dragon Sword"](../games/m-r/ninja-gaiden-dragon-sword.md)

## ACT-832

- Назва: Рухатися заданим шляхом, розвертатися та обирати напрямок на розвилці
- Переглянуто: `2026-11-21`

### Операційне визначення

У режимі руху гравець утримує окрему кнопку, щоб персонаж ішов поточною ділянкою заданого шляху. Інша команда розвертає персонажа. На розвилці гра пропонує обрати один із доступних напрямків.

### Включає

Рух, розворот і вибір коридору на початковому маршруті Killer7 для Nintendo GameCube.

### Виключає

Вільний рух площиною, автоматичний рух без утримання кнопки, пересування полем на відстань із кидка кубика або вибір віддаленої точки з автоматичним пошуком шляху.

### Ігри-носії

- [`GAME-0627` — "Killer7"](../games/g-l/killer7.md)

## ACT-833

- Назва: Утримувати нерухому стійку від першої особи й відпускати кнопку для повернення до руху
- Переглянуто: `2026-11-21`

### Операційне визначення

Утримання кнопки бойової стійки тимчасово зупиняє звичайний рух і переводить камеру в нерухомий вид від першої особи. Керування напрямком тепер рухає приціл. Коли гравець відпускає кнопку, повертаються звичайний ракурс і керування рухом.

### Включає

Ден у першому коридорі Killer7 переходить у бойову стійку й виходить із неї, щоб продовжити рух маршрутом.

### Виключає

Зміна лише масштабу зі збереженням руху, перемикання постійного режиму стрільби, постійний вид від першої особи або автоматичне стеження за обраною ціллю.

### Ігри-носії

- [`GAME-0627` — "Killer7"](../games/g-l/killer7.md)

## ACT-834

- Назва: Вручну поповнювати заряджені постріли з паузою без обліку запасу набоїв
- Переглянуто: `2026-11-21`

### Операційне визначення

Гравець дає команду перезарядити активну зброю. Дія відновлює обмежену кількість готових пострілів після короткої паузи, коли стріляти не можна. Гра не списує набої з окремого облікованого запасу.

### Включає

У першій сутичці Killer7 Ден перезаряджається, а потім знову може стріляти, поки ворог ще на полі.

### Виключає

Перенесення набоїв з обмеженого запасу, отримання іншої зарядженої зброї, автоматичне поповнення під час входу до кімнати або безперервна стрільба без обліку пострілів.

### Ігри-носії

- [`GAME-0627` — "Killer7"](../games/g-l/killer7.md)

## ACT-835

- Назва: Суміщати символи навички з упорядкованим рядом загроз
- Переглянуто: `2026-11-21`

### Операційне визначення

Гравець розташовує доступну навичку з фіксованим порядком символів над рядом загроз. Сумісний символ прибирає загрозу під собою, зірка підходить до будь-якого типу, а пропуск зберігає загрозу в цій позиції. Застосування витрачає один доступний заряд навички й зазначені ресурси.

### Включає

Суміщення «Розслабся» з енергією, міцністю авто й грошима у вступній події з трактором у Keep Driving. «Спробуй» має одну універсальну зірку.

### Виключає

Переставляння загроз, незалежний вибір позиції для кожного символу, очищення всього ряду без суміщення або використання пропуску як зірки.

### Ігри-носії

- [`GAME-0628` — "Keep Driving"](../games/g-l/keep-driving.md)

## ACT-836

- Назва: Установлювати знайдену деталь у відповідне гніздо споруди
- Переглянуто: `2026-11-21`

### Операційне визначення

У режимі складання поселення гравець обирає вже знайдену вільну деталь і ставить її у відповідне гніздо конкретної наявної споруди. Після встановлення деталь зникає з вільного запасу та стає частиною споруди. Сама споруда вже може стояти на мапі.

### Включає

Установлення знайденого колеса у відповідне гніздо вже розміщеного будинку Пейдж у Dark Cloud.

### Виключає

Розміщення цілої споруди на мапі, вільний вибір місця для оздоби, створення нової деталі з матеріалів або вставляння довільної деталі в будь-яке гніздо.

### Ігри-носії

- [`GAME-0629` — "Dark Cloud"](../games/a-f/dark-cloud.md)

## ACT-837

- Назва: Обирати позицію щодо учасника або пропускати нагоду висловитися
- Переглянуто: `2026-11-22`

### Операційне визначення

Під час обговорення гравець може обрати одну доступну позицію щодо того, хто говорить або кого обговорюють, наприклад підтримати підозру чи захистити учасника. Можна й пропустити нагоду, нічого не сказавши. Вибір впливає на обговорення, а голос подається окремо.

### Включає

У Gnosia гравець може відреагувати на підозру Сецу або промовчати під час першого обговорення другого дня.

### Виключає

Подання остаточного голосу, довільний текст розмови, зміна справжньої ролі або припущення, що одна репліка гарантує наступний голос.

### Ігри-носії

- [`GAME-0630` — "Gnosia"](../games/g-l/gnosia.md)

## ACT-838

- Назва: Подавати один голос за відсторонення доступного учасника
- Переглянуто: `2026-11-22`

### Операційне визначення

На окремому екрані голосування гравець обирає одного доступного учасника й підтверджує голос за його відсторонення. Вибір додає один голос, а результат визначає підрахунок усіх голосів.

### Включає

Вибір SQ другого дня першої петлі Gnosia для японської PlayStation Vita.

### Виключає

Висловлення підозри без голосу, одноосібне відсторонення, голосування за арену, голос за вже відстороненого учасника або вибір кількох цілей одним голосом.

### Ігри-носії

- [`GAME-0630` — "Gnosia"](../games/g-l/gnosia.md)

## ACT-839

- Назва: Бити по вільному м’ячу поруч одразу або після замаху
- Переглянуто: `2026-11-22`

### Операційне визначення

Коли вільний м’яч у межах досяжності, гравець штовхає орган керування ударом уперед і б’є одразу. Можна спершу відвести його назад для замаху, а тоді штовхнути вперед. М’яч летить туди, куди повернений персонаж. Обирати конкретного одержувача чи цілитися у ворота не потрібно.

### Включає

У despelote можна одразу відбити шкільний м’яч від конусів або виконати сильніший удар із замахом на перерві.

### Виключає

Команда пасу з вибором доступного партнера, удар із фіксованою ціллю у воротах суперника, фізичний замах ключкою з відстеженням її руху або керування м’ячем після удару.

### Ігри-носії

- [`GAME-0631` — "despelote"](../games/a-f/despelote.md)

## ACT-840

- Назва: Підготувати форсаж тягою вперед і повторно натиснути газ
- Переглянуто: `2026-11-22`

### Операційне визначення

Під час руху гравець утримує керування вперед, щоб підготувати форсаж. Коли з’являється сигнал готовності, гравець коротко відпускає звичайний газ і знову натискає його. Це запускає тривалий форсаж. Відпускання газу чи гальмування вимикає форсаж.

### Включає

На Nintendo 64 у Star Wars Episode I: Racer треба дочекатися жовтого сигналу, потім відпустити й знову натиснути A.

### Виключає

Кнопка форсажу, яка діє одразу під час утримання, одноразовий розігрів після старту, прискорення після виходу із заносу або витрачання запасу нітро.

### Ігри-носії

- [`GAME-0632` — "Star Wars Episode I: Racer"](../games/s-z/star-wars-episode-i-racer.md)

## ACT-841

- Назва: Утримувати ремонт на ходу ціною поточної швидкості
- Переглянуто: `2026-11-22`

### Операційне визначення

Коли пошкоджений болід ще рухається, гравець утримує кнопку ремонту. Стан боліда поступово відновлюється, а швидкість обмежується. Болід лишається на трасі. Коли гравець відпускає кнопку, ремонт припиняється незалежно від того, чи завершився він.

### Включає

У Star Wars Episode I: Racer після контакту зі стіною на Boonta Training Course можна утримувати R для ремонту.

### Виключає

Ремонт у меню між заїздами, повернення на трасу після аварії, миттєве відновлення від підібраного предмета або призупинення гонки.

### Ігри-носії

- [`GAME-0632` — "Star Wars Episode I: Racer"](../games/s-z/star-wars-episode-i-racer.md)

## ACT-842

- Назва: Підтвердити визначення виду за описом живої істоти
- Переглянуто: `2026-11-22`

### Операційне визначення

Оглянувши живу істоту, гравець обирає та підтверджує один із запропонованих описів, який відповідає її видимим ознакам або поведінці. Правильна відповідь додає іменований запис до довідника. Сама істота ще не приєднується.

### Включає

У Flock гравець зіставляє Bewl із запропонованими описами й підтверджує вид Basking Bewl.

### Виключає

Вибір імені для вже прирученої істоти, автоматичне визначення виду одним скануванням, передання предмета експертові або приручення тварини.

### Ігри-носії

- [`GAME-0633` — "Flock"](../games/a-f/flock.md)

## ACT-843

- Назва: Вибрати відстань у польоті й заспівати
- Переглянуто: `2026-11-22`

### Операційне визначення

Під час приручення гравець змінює своє положення відносно істоти й окремо подає команду співу. Поточна відстань впливає на оцінку, тому наблизитися й заспівати — різні дії.

### Включає

На Xbox у Flock гравець суміщає позначки відстані й натискає A, щоб заспівати для Basking Bewl.

### Виключає

Автоматичне спрацювання від близькості, спів за фіксованою ритмічною розміткою незалежно від відстані, пряме керування істотою або вибір уже прирученого учасника з меню.

### Ігри-носії

- [`GAME-0633` — "Flock"](../games/a-f/flock.md)

## ACT-844

- Назва: Струсити маракас на вказаній висоті в момент прибуття позначки
- Переглянуто: `2026-11-22`

### Операційне визначення

Для звичайної позначки піднеси маракас до вказаної висоти й струси його, коли позначка дійде до цільового кола. За сигналом швидкого струшування повторюй рух, поки триває цей сигнал.

### Включає

Струшування маракаса Dreamcast під час прибуття позначки до верхнього, середнього чи нижнього кола та в проміжку, відведеному на швидкі повтори.

### Виключає

Утримання пози без струшування, крок на танцювальному килимку, натискання кнопки геймпада за позначкою та безперервна хореографія всім тілом.

### Ігри-носії

- [`GAME-0634` — "Samba de Amigo"](../games/s-z/samba-de-amigo.md)

## ACT-845

- Назва: Утримати обидва маракаси в показаній позі
- Переглянуто: `2026-11-22`

### Операційне визначення

За окремим сигналом пози розташуй обидва маракаси, як показано, й утримуй їх до оцінки. Струшувати їх, як для звичайної позначки, не потрібно.

### Включає

Відтворення двох положень, позначених на силуеті в грі для Dreamcast.

### Виключає

Почергові рухи руками без утримання, хореографія всім тілом, вільний вибір жесту й імітація пози геймпадом.

### Ігри-носії

- [`GAME-0634` — "Samba de Amigo"](../games/s-z/samba-de-amigo.md)

## ACT-846

- Назва: Утримати кнопку напрямку, щоб перейти в інший доступний період спогаду
- Переглянуто: `2026-11-22`

### Операційне визначення

Коли в цій місцевості стають доступні обидва періоди, утримай кнопку переходу в обраному напрямку часу. Звичайний рух і необов’язкова розмова такого переходу не запускають.

### Включає

Окремі підказки, як утримати кнопку для переходу в пізніший або раніший період під час першого Причастя в школі.

### Виключає

Завантаження розділу, безперервне перемотування дій, зміна минулих подій і перший сюжетний перехід після розмови на даху.

### Ігри-носії

- [`GAME-0635` — "1000xRESIST"](../games/0-9/1000xresist.md)

## ACT-847

- Назва: Обрати співрозмовника й повідомити про стан завдання через пристрій зв’язку
- Переглянуто: `2026-11-22`

### Операційне визначення

Відкрий вікно зв’язку, вибери потрібного члена екіпажу зі списку, а тоді натисни піктограму теми про стан завдання. Якщо умови виконано, повідомлення може просунути завдання.

### Включає

Вибір Бордена та теми про готовність спорядження в ігровому пристрої PenUltimate під час роботи на поверхні Аттіли.

### Виключає

Розмова в тій самій сцені без вибору каналу, автоматичні повідомлення, отримання лише підказки маршруту й запуск мінігри на пристрої.

### Ігри-носії

- [`GAME-0636` — "The Dig"](../games/s-z/the-dig.md)

## ACT-848

- Назва: Прокласти довільну стіну або огорожу
- Переглянуто: `2026-11-22`

### Операційне визначення

Перетягування вказівника в просторі прокладає стіну або огорожу за проведеною лінією. Споруда лишається на місці. Гравець не вибирає клітинок і не ставить кожну секцію окремо.

### Включає

Проведення кам’яної стіни або огорожі окремим інструментом у Tiny Glade.

### Виключає

Нанесення стежки на поверхню, автоматична побудова маршруту між двома точками, розміщення готової будівлі або наказ будувати по клітинках.

### Ігри-носії

- [`GAME-0637` — "Tiny Glade"](../games/s-z/tiny-glade.md)

## ACT-849

- Назва: Нанести або стерти ділянку стежки пензлем
- Переглянуто: `2026-11-22`

### Операційне визначення

Гравець проводить потрібним пензлем по місцевості, додаючи або прибираючи частину стежки. Межі зміни визначає слід пензля. З’єднувати окремі вузли не потрібно.

### Включає

Провести стежку по траві до перешкоди й стерти лише частину її ділянки спеціальною гумкою в Tiny Glade.

### Виключає

Проведення стіни, вибір кінців для автоматичного маршруту, зміна лише декоративних позначок на незмінному полі або встановлення готового отвору в стіні.

### Ігри-носії

- [`GAME-0637` — "Tiny Glade"](../games/s-z/tiny-glade.md)

## ACT-850

- Назва: Навести й вистрілити мотузкою після призначення навички
- Переглянуто: `2026-11-22`

### Операційне визначення

Після призначення навички стрільби мотузкою самостійній істоті гравець наводить приціл на окрему ділянку місцевості. Для пострілу потрібна окрема команда.

### Включає

Призначення навички Roper у Lemmings 2 для Amiga й постріл у відповідну ділянку місцевості попереду лемінга.

### Виключає

Призначення навички без другої цілі, покрокове керування істотою, підтягування стрільця гаком до опори або встановлення готового мосту.

### Ігри-носії

- [`GAME-0638` — "Lemmings 2: The Tribes"](../games/g-l/lemmings-2-the-tribes.md)

## ACT-851

- Назва: Вибрати трюк у повітрі або на опорі під час руху на роликах
- Переглянуто: `2026-11-22`

### Операційне визначення

Гравець вибирає трюк відповідно до стану ролера. У повітрі можна втримати захват або поєднати його з обертанням, а для трюку на опорі потрібно спрямувати ролера до відповідної поверхні.

### Включає

Захват Tail Grab або Melancholy, його поєднання із сальто в повітрі чи ковзання по поручню в Rollerdrome.

### Виключає

Пасивний рух на роликах, обов’язковий перехід через manual або revert для серії на скейтборді, оцінювання приземлення чи автоматичний контакт без вибору трюку.

### Ігри-носії

- [`GAME-0639` — "Rollerdrome"](../games/m-r/rollerdrome.md)

## ACT-852

- Назва: Утримувати біг у напрямку, щоб набрати швидкість
- Переглянуто: `2026-11-22`

### Операційне визначення

Утримуй кнопку бігу й спрямовуй персонажа по опорі. У міру бігу він переходить у швидший режим руху. На бігу можна стрибати й змінювати напрямок, а будова маршруту визначає, де вдасться зберегти швидкість.

### Включає

У John Gutter Пеппіно розганяється, пробиває ряд сирних блоків і продовжує швидко рухатись під час стрибка.

### Виключає

Окремий ривок на фіксовану відстань, зовнішня платформа-прискорювач, спринт за витратний ресурс або звичайний рух в обраному напрямку.

### Ігри-носії

- [`GAME-0640` — "Pizza Tower"](../games/m-r/pizza-tower.md)

## ACT-853

- Назва: Окремо обирати бійця й початкову зброю
- Переглянуто: `2026-11-22`

### Операційне визначення

Перед першим двобоєм в одиночному сюжетному режимі вибери бійця, а потім в окремому меню вибери його основну зброю. Обидва рішення визначають, з чим персонаж почне двобій.

### Включає

Почни сюжетний режим за Уцусемі й вибери нодаті в меню зброї.

### Виключає

Призначення обох сторін локального матчу, вибір арени, зміна стійки в бою або підбирання зброї на місцевості.

### Ігри-носії

- [`GAME-0641` — "Bushido Blade"](../games/a-f/bushido-blade.md)

## ACT-854

- Назва: Застосовувати складник або приладдя до обраної посудини чи форми
- Переглянуто: `2026-11-22`

### Операційне визначення

Перенеси видимий складник або його приладдя до потрібної посудини чи форми, щоб виконати відповідну дію. Форму з тканиною й тістом можна поставити в пароварку цілком.

### Включає

Поклади тканину на форму для ідлі, додай тісто до вистелених заглиблень і постав наповнену форму у відкриту пароварку.

### Виключає

Вибір готового рецепта в меню, вчасне натискання для оцінки роботи з приладдям або викладання готової страви на продаж.

### Ігри-носії

- [`GAME-0642` — "Venba"](../games/s-z/venba.md)

## ACT-855

- Назва: Повертати встановлені форми між додаваннями
- Переглянуто: `2026-11-22`

### Операційне визначення

Поверни встановлені форми у відкритій пароварці до або між наступними додаваннями. Поворот змінює видиме розташування заглиблень і отворів для пари. Форми та тісто залишаються в посудині.

### Включає

Скористайся поворотом установлених форм для ідлі, а потім постав наступну наповнену форму.

### Виключає

Поворот однієї пласкої плитки, вибір орієнтації вільної деталі тільки перед встановленням або висновок про приховані правила повороту за одним зображенням.

### Ігри-носії

- [`GAME-0642` — "Venba"](../games/s-z/venba.md)

## ACT-856

- Назва: Утримувати кнопку атаки для заряду й відпускати її для ривка
- Переглянуто: `2026-11-22`

### Операційне визначення

Утримуй кнопку звичайної атаки, щоб підготувати ракетну дію. Коли заряд готовий, вибери напрямок і відпусти кнопку атаки. Від напрямку залежить, чи персонаж зробить ривок, чи обернеться на місці.

### Включає

Утримай атаку перед замковою шахтою, спрямуй ривок навскіс угору й відпусти кнопку. У посібнику окремо описано обертання з напрямком униз або без напрямку.

### Виключає

Очікування пасивного відновлення ривка, випуск снаряда без переміщення персонажа, утримання кнопки стрибка для більшої висоти й вільне керування польотом.

### Ігри-носії

- [`GAME-0643` — "Rocket Knight Adventures"](../games/m-r/rocket-knight-adventures.md)

## ACT-857

- Назва: Кермувати машиною, що біжить, окремо від кнопки дії
- Переглянуто: `2026-11-22`

### Операційне визначення

Повертай екранне кермо, щоб змінити напрямок руху машини під час безперервного бігу трасою. Окрема екранна кнопка виконує дію пересування, доступну на цій трасі.

### Включає

Увійди в поворот і залиш окрему кнопку з пружиною для наступного розриву.

### Виключає

Вибір однієї з фіксованих смуг жестом, поворот лише у визначених місцях, керування нахилом телефона або припущення, що кожна форма потребує окремої педалі газу.

### Ігри-носії

- [`GAME-0644` — "WHAT THE CAR?"](../games/s-z/what-the-car.md)

## ACT-858

- Назва: Стрибати кнопкою з пружиною в обраний момент розбігу
- Переглянуто: `2026-11-22`

### Операційне визначення

Скористайся доступною кнопкою з пружиною, коли наближаєшся до розриву чи перешкоди. Машина відривається від траси й рухається по дузі. Напрямок можна задавати окремо.

### Включає

Скеруй машину до дальньої смуги, натисни кнопку стрибка перед смугастим краєм і приземлися на наступну ділянку дороги.

### Виключає

Заряджання стрибка на опорі з підтвердженим запуском після відпускання, автоматичний підкид від дотику без натискання, заданий запуск на трасу або припущення, що ранець на іншому рівні працює так само.

### Ігри-носії

- [`GAME-0644` — "WHAT THE CAR?"](../games/s-z/what-the-car.md)

## ACT-859

- Назва: Рухати й ставити одну вибрану руку чи ногу під час підйому
- Переглянуто: `2026-11-22`

### Операційне визначення

Поки поточна поза має опору, скористайся запропонованою рукою чи ногою або вибери її вручну. Спрямуй вибрану кінцівку до досяжної ділянки скелі й постав її, перш ніж робити наступний рух.

### Включає

Не зміщуй ногу з опори. Перемкнися на руку, дотягнися нею до наступного виступу й візьмися за нього.

### Виключає

Одночасне незалежне керування двома руками, автоматичний рух за позначеним виступом або підтягування до віддаленої точки кріплення.

### Ігри-носії

- [`GAME-0646` — Cairn](../games/a-f/cairn.md)

## ACT-860

- Назва: Переходити в сусідній сектор навколо ворожої групи
- Переглянуто: `2026-11-22`

### Операційне визначення

Коли персонаж може змінювати позицію, обери рух за годинниковою стрілкою або проти неї. Персонаж переходить у сусідній сектор відносно тієї самої групи, змінюючи вразливість і напрямок атаки.

### Включає

Перемісти дракона на один сектор навколо групи, щоб знайти безпечнішу позицію, і затримайся там.

### Виключає

Поворот лише камери, керування на заданій трасі, перехід до іншої групи або рух під час атаки, яку не можна перервати.

### Ігри-носії

- [`GAME-0647` — Panzer Dragoon Saga](../games/m-r/panzer-dragoon-saga.md)

## ACT-861

- Назва: Визначити порядок розгорнутих загонів обох сторін перед боєм
- Переглянуто: `2026-11-22`

### Операційне визначення

Перед початком бою гравець додає кожен розгорнутий союзний і ворожий загін до однієї послідовності в обраному порядку. Почати бій можна, коли до неї внесено всі допустимі загони.

### Включає

Після заповнення поля Лісистої місцевості натиснути на позначки трьох союзних і двох ворожих загонів. Потім почати спланований бій.

### Виключає

Накази окремим бійцям під час бою, визначення порядку лише союзних ходів або прийняття вже заданого порядку сутички.

### Ігри-носії

- [`GAME-0649` — Drop Duchy](../games/a-f/drop-duchy.md)

## ACT-862

- Назва: Захопити доступну ворожу зброю в бойове кріплення літака
- Переглянуто: `2026-11-22`

### Операційне визначення

Підведи літак до контакту з доступною ворожою зброєю або дістань її маніпулятором. Захоплена зброя стає придатною до застосування з поточного кріплення просто під час бою.

### Включає

Наблизитися до знешкодженого носія Vulcan на першому рівні й застосувати захоплений Vulcan проти наступної хвилі.

### Виключає

Відібрати зброю з рук активного ворога, обрати зброю між рівнями або підібрати тільки боєприпаси окремо від самої зброї.

### Ігри-носії

- [`GAME-0650` — Einhänder](../games/a-f/einhander.md)

## ACT-863

- Назва: Поміняти дві встановлені зброї між каналами вогню
- Переглянуто: `2026-11-22`

### Операційне визначення

Команда міняє місцями зброю у двох кріпленнях, доступних одночасно. Кожна зброя зберігає свої залишки боєзапасу й поточний стан. Далі можна стріляти з будь-якого каналу окремо або з обох разом.

### Включає

Поміняти канали Vulcan і Spreader, поки обидва модулі встановлено на Astraea під час першого рівня.

### Виключає

Прокручування запасних модулів у єдиному активному каналі, прибирання однієї зброї та повернення її в готовність або поєднання двох компонентів у третій режим атаки.

### Ігри-носії

- [`GAME-0650` — Einhänder](../games/a-f/einhander.md)

## ACT-864

- Назва: Вийняти або вставити фізичне слово у визначене місце речення
- Переглянуто: `2026-11-22`

### Операційне визначення

Біля доступного змінного місця в реченні гравець виймає рухоме слово або вставляє на вільне місце слово, яке несе. Поза реченням слово лишається предметом у світі. Його можна віднести до іншого визначеного місця в тексті.

### Включає

Вийняти DRAINED («осушений») з речення про рів, покласти його й вставити принесене FULL («повний»).

### Виключає

Вільне введення тексту, перетягування відповіді зі списку, вирівнювання цілого речення на сітці або збирання декоративних написів.

### Ігри-носії

- [`GAME-0651` — The Plucky Squire](../games/s-z/the-plucky-squire.md)

## ACT-865

- Назва: Відмовитися від поточного набору, щоб розширити наступний вибір
- Переглянуто: `2026-11-23`

### Операційне визначення

Якщо у вікні вибору на паузі нічого не обрано, гравець може запросити ширшу наступну пропозицію й повернутися до бою без передавання нових засобів атаки на цей відрізок.

### Включає

Натиснути ADD («додати»), не обравши жодного з п’яти початкових чипів у третьому шкільному бою.

### Виключає

Витрачання або скидання обраного заради негайного добору, обмін постійного інвентарю або перезарядження зброї зі збереженням поточного набору.

### Ігри-носії

- [`GAME-0652` — Mega Man Battle Network](../games/m-r/mega-man-battle-network.md)

## ACT-866

- Назва: Відкрити уточнювальні репліки за підказкою в розмові
- Переглянуто: `2026-11-23`

### Операційне визначення

Під час розмови гравець реагує на щойно позначену репліку й відкриває варіанти уточнення. Натискання підказки й вибір однієї з відкритих реплік є окремими діями.

### Включає

Торкнутися жовтого значка, коли дівчинка засмучується на сходах, а потім обрати репліку, що веде до складання її пазла.

### Виключає

Вибір уже відкритої репліки, пошук в архіві свідчень після розмови, зіставлення речового доказу із записаним свідченням або звичайне гортання тексту.

### Ігри-носії

- [`GAME-0654` — "Hotel Dusk: Room 215"](../games/g-l/hotel-dusk-room-215.md)

## ACT-867

- Назва: Утримувати гальмо й відпускати його для ривка
- Переглянуто: `2026-11-23`

### Операційне визначення

Гравець утримує кнопку, щоб пригальмувати машину, яка сама рухається вперед, і накопичити заряд. Відпускання тієї самої кнопки одразу запускає ривок. Під час утримання можна кермувати.

### Включає

Утримуй B на Warp Star, щоб пройти поворот Floria Fields повільніше, і відпусти на виході. Гальмувати й накопичувати заряд можна й без повороту.

### Виключає

Звичайне гальмування без ривка за відпусканням, заряд лише за проходження рівнів заносу або окреме витрачання збереженого запасу прискорення.

### Ігри-носії

- [`GAME-0655` — "Kirby Air Riders"](../games/g-l/kirby-air-riders.md)

## ACT-868

- Назва: Поміняти заряджену кулю з наступною
- Переглянуто: `2026-11-23`

### Операційне визначення

Перед пострілом гравець торкається наступної кулі, щоб поміняти її місцями із зарядженою. Попередня заряджена куля лишається наступною, а обмін не витрачає постріл.

### Включає

На початку другого рівня поміняти місцями синю заряджену й жовту наступну кулі. Жовта стає доступною для удару по жовтих блоках, а синя лишається в черзі.

### Виключає

Викидання зарядженої кулі, вільний вибір з усього запасу, постріл наступною кулею без обміну або зміна кольору самої кулі.

### Ігри-носії

- [`GAME-0657` — "Spire Blast"](../games/s-z/spire-blast.md)

## ACT-869

- Назва: Торкнутися видимого блока, щоб вистрілити в нього
- Переглянуто: `2026-11-23`

### Операційне визначення

Гравець торканням обирає одну видиму точку на поверхні об’ємної споруди. Те саме торкання запускає заряджену кулю до вибраної точки без окремого налаштування сили чи траєкторії.

### Включає

Повернути огляд до жовтої ділянки другого рівня й торкнутися її, коли заряджено жовту кулю.

### Виключає

Відтягування пускового пристрою для вибору сили, керування кулею в польоті, зникнення блока без снаряда або саме лише обертання огляду.

### Ігри-носії

- [`GAME-0657` — "Spire Blast"](../games/s-z/spire-blast.md)

## ACT-870

- Назва: Розставити іменних бійців у рядах одного загону
- Переглянуто: `2026-11-23`

### Операційне визначення

Обери доступного іменного бійця та постав його на конкретне місце в передньому або задньому ряду загону. У сутичці кожен боєць має власну позицію й роль, а на мапі гравець командує всім загоном як одним цілим.

### Включає

Перед виходом на поле в Call to Action додати Годріка до загону Алена, у якому є два місця.

### Виключає

Команда двом самостійним загонам стати в лінію, вибір стійки, вибір резерву без розподілу за позиціями або переміщення одного розгорнутого бійця на полі.

### Ігри-носії

- [`GAME-0658` — "Unicorn Overlord"](../games/s-z/unicorn-overlord.md)

## ACT-871

- Назва: Замінити загін у майбутній сутичці на союзний загін поблизу
- Переглянуто: `2026-11-23`

### Операційне визначення

Коли загін зустрів ворога, а бій іще не почався, обери допустимий союзний загін поблизу, щоб він вступив у цю сутичку замість першого.

### Включає

Скористатися можливістю заміни й обрати допустимий загін поблизу для сутички біля мосту в Call to Action.

### Виключає

Перестановка бійців у тому самому загоні, заміна загону з будь-якої відстані, виклик підтримки без заміни основних учасників або нова команда руху після бою.

### Ігри-носії

- [`GAME-0658` — "Unicorn Overlord"](../games/s-z/unicorn-overlord.md)

## ACT-872

- Назва: Спрямувати видовжені руки до істоти або опори
- Переглянуто: `2026-11-23`

### Операційне визначення

Гравець спрямовує захоплення видовженими руками на доступну ціль. Та сама кнопка дає змогу вхопитися за придатну опору або схопити вразливу істоту. Від цілі залежить, яка дія можлива після захоплення.

### Включає

Спрямувати руки Рістара на перекладину над ним або на відкритого ворога на планеті Флора.

### Виключає

Підбирання предмета простим дотиком тіла, прямий удар без захоплення, постріл окремим гаком або вибір наперед визначеного місця запуску.

### Ігри-носії

- [`GAME-0659` — "Ristar"](../games/m-r/ristar.md)

## ACT-873

- Назва: Розкрутитися на нерухомій рукоятці й відпустити її для керованого польоту
- Переглянуто: `2026-11-23`

### Операційне визначення

Утримуйся на нерухомій опорі й натискай напрямок, щоб набирати швидкість обертання. Вибери мить, коли відпустити рукоятку й злетіти. Далі змінюй напрямок вільного польоту кнопками руху.

### Включає

Утримувати звичайну зіркову рукоятку наприкінці першої ділянки Флори, розігнатися й відпустити її, щоб полетіти.

### Виключає

Зміна довжини троса під час розгойдування, відпускання ліани, що рухалася сама, миттєвий ривок без обертання або автоматичне переміщення за фіксованим маршрутом.

### Ігри-носії

- [`GAME-0659` — "Ristar"](../games/m-r/ristar.md)

## ACT-874

- Назва: Додати вибране обличчя з доказу до доступних портретів
- Переглянуто: `2026-11-23`

### Операційне визначення

Вибери обличчя на незмінному зображенні-доказі, щоб додати окремий портрет. Тоді його можна вибрати для картки людини. Саме зображення від цього не змінюється, а гра не встановлює особу автоматично.

### Включає

Вибрати обличчя сестер на початковій світлині Руттрі й побачити окремі портрети у списку вибору.

### Виключає

Саме лише збільшення, знімання довільного кадру, вилучення фрази або додавання вже зареєстрованого портрета до картки.

### Ігри-носії

- [`GAME-0660` — "The Roottrees are Dead"](../games/s-z/the-roottrees-are-dead.md)

## ACT-875

- Назва: Окремо редагувати поля попередньої картки родича
- Переглянуто: `2026-11-23`

### Операційне визначення

У картці родича, яка вже має місце в дереві, вибирай і змінюй ім’я, заняття та портрет незалежно одне від одного, поки картку ще не підтверджено. Редагування одного поля не підтверджує його.

### Включає

Заповнити три поля кожної картки сестер у вступному завданні про Руттрі й за потреби повернутися до раніше заповненого поля до підтвердження.

### Виключає

Призначення особи зі складеним описом її долі, довільні нотатки, додавання портрета з джерела та автоматичне підтвердження правильних записів.

### Ігри-носії

- [`GAME-0660` — "The Roottrees are Dead"](../games/s-z/the-roottrees-are-dead.md)

## ACT-876

- Назва: Змінювати тягу в повітрі й гальмувати після торкання
- Переглянуто: `2026-11-23`

### Операційне визначення

У повітрі гравець змінює поточний рівень тяги. Коли літак уже котиться землею, кнопка зменшення тяги вмикає колісне гальмо. Гравець сам вирішує, коли його застосувати.

### Включає

На заході легкого літака на посадку збільшувати або зменшувати тягу кнопками A та B. Після торкання смуги натиснути B, щоб зупинити літак.

### Виключає

Окремі кнопки для повітряного й колісного гальм, гальмування планера підняттям носа, автоматична зупинка або саме лише регулювання тяги.

### Ігри-носії

- [`GAME-0661` — "Pilotwings"](../games/m-r/pilotwings.md)

## ACT-877

- Назва: Скерувати відстежений удар, що переносить персонажа до цілі
- Переглянуто: `2026-11-23`

### Операційне визначення

Гравець вибирає допустимого супротивника й виконує розпізнаваний жест удару контролером. Один зарахований жест запускає допоміжне наближення персонажа й заплановане влучання у вибрану ціль.

### Включає

У сутичці біля перших заручників у каналізації виконай відстежений жест Punch-To в бік позначеного супротивника поза безпосередньою досяжністю. Гра сама наблизить персонажа для удару.

### Виключає

Окрема команда руху з подальшим ударом, влучання лише від зіткнення руки, снаряд, за якого персонаж лишається на місці, або контратака у відповідь на удар.

### Ігри-носії

- [`GAME-0662` — "Batman: Arkham Shadow"](../games/a-f/batman-arkham-shadow.md)

## ACT-878

- Назва: Почати планерувальний удар із висоти за підказкою
- Переглянуто: `2026-11-23`

### Операційне визначення

Із допустимої підвищеної позиції гравець вибирає супротивника нижче та запускає доступний планерувальний удар. Команда поєднує спуск із влучанням у вибраного супротивника.

### Включає

З оглядового майданчика в каналізації утримуй команду Glide Kick, коли позначена ціль унизу, щоб спуститися в зал і влучити в неї.

### Виключає

Спуск без вибраного супротивника, вибір місця на висоті для переміщення, удар із наближенням по землі або вільне падіння з окремим прицілюванням для удару.

### Ігри-носії

- [`GAME-0662` — "Batman: Arkham Shadow"](../games/a-f/batman-arkham-shadow.md)

## ACT-879

- Назва: Утримувати музичну фразу й вести кутовий сектор аналоговим стіком
- Переглянуто: `2026-11-23`

### Операційне визначення

Гравець аналоговим стіком спрямовує активний кутовий сектор зі спільної точки оцінювання й окремо вибирає момент натискання для гри на струнах. На протяжній фразі можна утримувати кнопку й далі вести сектор до відпускання.

### Включає

Під час заряджання або атаки в першій пісні спрямуй сектор на фразу, натисни на її початку й утримуй кнопку, поки лінія змінює напрямок.

### Виключає

Вибір сталої смуги лада, ведення пальцем по екрану, утримання ноти без окремого наведення або відповіді на чотири символи захисту.

### Ігри-носії

- [`GAME-0663` — "Gitaroo Man"](../games/g-l/gitaroo-man.md)

## ACT-880

- Назва: Вчасно відповідати на символ захисту відповідною кнопкою
- Переглянуто: `2026-11-23`

### Операційне визначення

Гравець читає символ захисту й натискає відповідну основну кнопку, коли символ досягає спільної центральної точки. Смуга й символ визначають потрібну кнопку без одночасного наведення стіком.

### Включає

У першому відрізку захисту дочекайся, поки хрестик або трикутник дійде до точки, і натисни відповідну кнопку замість обраної кнопки гри на струнах.

### Виключає

Безперервне утримання блоку, довільний блок без показаного символу, одночасне ведення сектору або повторення запам’ятованої послідовності вчителя.

### Ігри-носії

- [`GAME-0663` — "Gitaroo Man"](../games/g-l/gitaroo-man.md)

## ACT-881

- Назва: Вкласти один кубик із відомим значенням у гніздо спорядження
- Переглянуто: `2026-11-23`

### Операційне визначення

Вибрати доступний кинутий кубик і вкласти його в конкретне гніздо придатного предмета спорядження, щоб передати йому цей кубик.

### Включає

Перетягування вільного кубика Воїна в гніздо меча, бойової сокири, підвищення значення або перекидання.

### Виключає

Витрачання очок зі спільного запасу, кидок без призначення та вибір цілі атаки незалежно від кубика.

### Ігри-носії

- [`GAME-0664` — "Dicey Dungeons"](../games/a-f/dicey-dungeons.md)

## ACT-882

- Назва: Забрати одну нагороду за рівень у запас спорядження
- Переглянуто: `2026-11-23`

### Операційне визначення

Вибрати один із взаємовиключних предметів, запропонованих після підвищення рівня, і додати його до запасу, зберігши поточне активне спорядження.

### Включає

Вибір шипованого щита з двох нагород Воїна за третій рівень і поява щита в наплічнику.

### Виключає

Нагорода, яка одразу займає активну комірку, добір карти в колоду, звичайна покупка й переміщення вже наявних предметів.

### Ігри-носії

- [`GAME-0664` — "Dicey Dungeons"](../games/a-f/dicey-dungeons.md)

## ACT-883

- Назва: Вибрати іншу траєкторію удару швидким подвійним натисканням
- Переглянуто: `2026-11-23`

### Операційне визначення

Коли можна вдарити по м’ячу, швидко натиснути ту саму кнопку двічі, щоб вибрати інший контакт із м’ячем і траєкторію замість варіанта за одне натискання.

### Включає

Два швидкі натискання A дають низовий удар, а два натискання C — м’який перекид замість звичайних варіантів.

### Виключає

Утримання кнопки для заряджання, окрема кнопка для іншого удару й другий сигнал після контакту для оцінювання вже обраної дії.

### Ігри-носії

- [`GAME-0665` — "Sega Worldwide Soccer '97"](../games/s-z/sega-worldwide-soccer-97.md)

## ACT-884

- Назва: Налаштувати склад і розташування команди для матчу з прямим керуванням
- Переглянуто: `2026-11-23`

### Операційне визначення

Вибрати тактику, розташування, тип захисту й допустимих гравців на один матч, у якому людина далі безпосередньо рухає поточного футболіста.

### Включає

Вибір тактики, схеми, типу захисту й замін перед початком матчу або в меню стратегії під час нього.

### Виключає

Налаштування повністю автоматичного матчу менеджера, купівля чи редагування футболістів і окреме безперервне керування позицією кожного гравця.

### Ігри-носії

- [`GAME-0665` — "Sega Worldwide Soccer '97"](../games/s-z/sega-worldwide-soccer-97.md)

## ACT-885

- Назва: Вибрати, що перенести в новий матч після зарахованого результату
- Переглянуто: `2026-11-23`

### Операційне визначення

Після завершення окремого матчу обрати нову гру з тими самими командами, повернутися до вибору команд або умов зі збереженням відповідних попередніх налаштувань чи вийти з режиму.

### Включає

Чотири варіанти продовження товариської гри після виходу з екрана результатів.

### Виключає

Повтор кадрів попереднього матчу, автоматичний перехід у наступний раунд змагання й перезапуск незавершеної спроби.

### Ігри-носії

- [`GAME-0665` — "Sega Worldwide Soccer '97"](../games/s-z/sega-worldwide-soccer-97.md)

## ACT-886

- Назва: Дати команді негайну вказівку в захисті, керуючи одним футболістом
- Переглянуто: `2026-11-23`

### Операційне визначення

Під час активного захисту дати командну вказівку, яка змінює реакцію інших футболістів на атаку, зберігши пряме керування рухом одного гравця.

### Включає

Виклик пресингу, персональної опіки або кроку всієї лінії для спроби офсайдної пастки.

### Виключає

Повідомлення іншій людині, сам лише вибір складу перед матчем і ручне керування кожним захисником.

### Ігри-носії

- [`GAME-0665` — "Sega Worldwide Soccer '97"](../games/s-z/sega-worldwide-soccer-97.md)

## ACT-887

- Назва: Нанести мазок у точці, вибраній окремим курсором
- Переглянуто: `2026-11-23`

### Операційне визначення

Гравець наводить пензель незалежно від руху персонажа й наносить фарбу в обраній точці. Мазком можна подіяти на об’єкт поруч, поки персонаж стоїть на місці.

### Включає

Зафарбувати нижній гриб із правого уступу в Supper Woods, перш ніж зробити крок на гриб.

### Виключає

Рух персонажа до курсора, витрата спорядженого жетона фарби в гнізді, малювання контуру прохідної стежки чи крок на збільшену шапинку.

### Ігри-носії

- [`GAME-0666` — "Chicory: A Colorful Tale"](../games/a-f/chicory-a-colorful-tale.md)

## ACT-888

- Назва: Утримувати й опускати енергетичний щит навколо тіла
- Переглянуто: `2026-11-23`

### Операційне визначення

Гравець утримує окрему кнопку захисту, щоб оточити керованого персонажа енергетичним полем, і відпускає її, щоб прибрати поле. Поки вистачає енергії, персонаж може рухатися з піднятим щитом.

### Включає

Утримувати R1 під час синього залпу Prophet і рухатися зі щитом Солтарі, а потім опустити його для атаки.

### Виключає

Спрямований фронтальний блок зброєю, пасивна броня, миттєве парирування або окремо поставлена стіна, що лишається на місці після руху персонажа.

### Ігри-носії

- [`GAME-0667` — "SAROS"](../games/s-z/saros.md)

## ACT-889

- Назва: Стрибок між переднім і заднім планами
- Переглянуто: `2026-11-23`

### Операційне визначення

У визначеній точці переходу гравець поєднує стрибок із напрямком углиб або назовні, щоб приземлитися на окремому шляху переднього чи заднього плану.

### Включає

Доступний стрибок на задній план до початкової хатини й поштової скриньки в Tomba!.

### Виключає

Стрибок уздовж того самого шляху, вільний рух площиною та перемикання видимого шару без переміщення персонажа.

### Ігри-носії

- [`GAME-0668` — "Tomba!"](../games/s-z/tomba.md)

## ACT-890

- Назва: Випуск вибраного предмета події в поточну сцену
- Переглянуто: `2026-11-23`

### Операційне визначення

Гравець вибирає здобутий предмет події в інвентарі та окремою командою випускає його в поточній сцені, без окремого наведення на механізм чи отримувача.

### Включає

Вибір і підтвердження Лютого вихору (Furious Tornado) в меню Use Item біля туману в Tomba!.

### Виключає

Підбирання предмета, застосування ключа до окремо вибраного замка, передавання предмета отримувачеві та автоматичне застосування при вході.

### Ігри-носії

- [`GAME-0668` — "Tomba!"](../games/s-z/tomba.md)

## ACT-891

- Назва: Поворот позицій утримуваних плиток навколо персонажа
- Переглянуто: `2026-11-23`

### Операційне визначення

Гравець повертає позиції утримуваних плиток відносно персонажа, а зображення на їхніх поверхнях зберігають початковий напрямок.

### Включає

Переміщення останньої деталі картини «Бреберн» із позиції над Вілмотом праворуч від нього перед з’єднанням.

### Виключає

Поворот самої деталі картини, поворот камери та переміщення плитки, яку персонаж не утримує.

### Ігри-носії

- [`GAME-0669` — "Wilmot Works It Out"](../games/s-z/wilmot-works-it-out.md)

## ACT-892

- Назва: Вибір і підтвердження місця на стіні для готової картини
- Переглянуто: `2026-11-23`

### Операційне визначення

Після того як гра прийме складену на підлозі картину, гравець переходить в окремий режим розміщення на стіні, вибирає місце й підтверджує, де вона висітиме.

### Включає

Перенесення готової картини «Бреберн» до стіни галереї та підтвердження місця поруч із першою картиною або під нею.

### Виключає

Переміщення окремих плиток, завершення складання через розміщення на стіні, автоматичне розміщення й вибір орієнтації куплених меблів.

### Ігри-носії

- [`GAME-0669` — "Wilmot Works It Out"](../games/s-z/wilmot-works-it-out.md)

## ACT-893

- Назва: Підбирання навички з прив’язкою до вибраної бойової кнопки
- Переглянуто: `2026-11-23`

### Операційне визначення

Гравець підходить до доступної капсули й натискає бойову кнопку, до якої хоче одразу прив’язати її навичку. Можна вибрати вже зайняту кнопку, замінивши попередню навичку.

### Включає

Підійти до капсули Laser, Flash Barrier або Vacuum Slash на Highway і призначити навичку на потрібну кнопку в Phantom Dust.

### Виключає

Автоматичне підбирання, вибір готової навички з інвентарю й редагування арсеналу між боями.

### Ігри-носії

- [`GAME-0670` — "Phantom Dust"](../games/m-r/phantom-dust.md)

## ACT-894

- Назва: Посадити доступну живу істоту на спину персонажа
- Переглянуто: `2026-11-23`

### Операційне визначення

Гравець виконує дію поруч із придатною живою істотою й садовить її на спину свого персонажа. Істота пересувається разом із ним і лишається доступною для наступної взаємодії.

### Включає

Підхопити Glubbit хвостом, посадити його на спину Йоші й піднести до сусідньої гілки з яблуками.

### Виключає

Ковтання істоти для створення боєприпасів, перенесення неживого ключа чи ящика, їзду верхи або звичайне ведення супутника поруч.

### Ігри-носії

- [`GAME-0671` — "Yoshi and the Mysterious Book"](../games/s-z/yoshi-and-the-mysterious-book.md)

## ACT-895

- Назва: Підбити рухому кулю фліпером з потрібного боку
- Переглянуто: `2026-11-23`

### Операційне визначення

Гравець приводить у рух закріплений фліпер вибраного боку, поки куля вже рухається. Контакт у потрібний момент змінює її напрямок залежно від траєкторії наближення й руху фліпера.

### Включає

Натиснути лівий або правий фліпер, коли куля при падінні досягає фліпера. Вибрати момент, щоб відправити її назад до голів.

### Виключає

Пуск кулі зі стартового жолоба, пряме керування кулею, пасивний відскок від борту або дистанційний удар без контакту з важелем.

### Ігри-носії

- [`GAME-0704` — "Alien Crush"](../games/a-f/alien-crush.md)
- [`GAME-0672` — "Devil's Crush"](../games/a-f/devils-crush.md)

## ACT-896

- Назва: Коротко штовхнути стіл, щоб змістити рухому кулю
- Переглянуто: `2026-11-23`

### Операційне визначення

Гравець робить окремий поштовх столу, який може відхилити вільну кулю без контакту з фліпером.

### Включає

Натиснути описану в посібнику кнопку II, щоб штовхнути стіл і змінити хід кулі.

### Виключає

Тривале нахиляння для безперервного керування тілом, рух фліпера, зміну загальної осі тяжіння або наведення окремого запуску.

### Ігри-носії

- [`GAME-0704` — "Alien Crush"](../games/a-f/alien-crush.md)
- [`GAME-0672` — "Devil's Crush"](../games/a-f/devils-crush.md)

## ACT-897

- Назва: Закріпити один наявний кубик персонажа за дією з перевіркою навички
- Переглянуто: `2026-11-23`

### Операційне визначення

Гравець вибирає наявний кубик конкретного персонажа з відомим значенням, призначає його дії з перевіркою навички й підтверджує вибір.

### Включає

Покласти один із наявних кубиків Серафіна в комірку дії «Зробити отвір» і підтвердити дію.

### Виключає

Запит на загальний кидок без розподілу, спорядження предмета в комірці або вибір завдання без призначення відомого кубика.

### Ігри-носії

- [`GAME-0673` — "Citizen Sleeper 2: Starward Vector"](../games/a-f/citizen-sleeper-2-starward-vector.md)

## ACT-898

- Назва: Підтвердити екіпаж контракту з обов’язковими й необов’язковими учасниками
- Переглянуто: `2026-11-23`

### Операційне визначення

Перед вильотом на контракт гравець підтверджує склад щонайменше з одним обов’язковим учасником і може додати доступних супутників із власними кубиками дій і навичками.

### Включає

Залишити обов’язкового Серафіна в екіпажі й вирішити, чи брати доступну Нію на завдання «Сигнал Конвея».

### Виключає

Суто візуальний вибір команди, однакові взаємозамінні місця або найм учасника без власних дій.

### Ігри-носії

- [`GAME-0673` — "Citizen Sleeper 2: Starward Vector"](../games/a-f/citizen-sleeper-2-starward-vector.md)

## ACT-899

- Назва: Ввести команду трюку на воді або під час стрибка
- Переглянуто: `2026-11-24`

### Операційне визначення

Гравець у заданому порядку рухає стік, іноді з натиснутою кнопкою, щоб виконати окремий трюк на воді, на трампліні або в повітрі.

### Включає

Ввести команду сальто під час з’їзду з трампліна або окрему команду стійки на руках, рухаючись по воді.

### Виключає

Звичайне кермування чи пригинання, лише повітряний трюк заради прискорення або нарахування за трюк від самого входження в кільце.

### Ігри-носії

- [`GAME-0674` — "Wave Race: Blue Storm"](../games/s-z/wave-race-blue-storm.md)

## ACT-900

- Назва: Задати початковий напрямок стрілки під час планування
- Переглянуто: `2026-11-24`

### Операційне визначення

До запуску гравець змінює позначений початковий напрямок на вже прокладеному розгалуженні, зберігаючи його геометрію.

### Включає

Торкнутися позначки стрілки перед станціями, щоб перший поїзд зі спільної колії рушив до червоної станції.

### Виключає

Малювання чи заміну самої колії, переведення стрілки під поїздом під час руху або її автоматичне перемикання після проїзду.

### Ігри-носії

- [`GAME-0675` — "Teeny Tiny Trains"](../games/s-z/teeny-tiny-trains.md)

## ACT-901

- Назва: Додати поштовх під час руху накатом
- Переглянуто: `2026-11-24`

### Операційне визначення

Під час руху гравець може відштовхнутися, щоб додати ходу. Для звичайного руху накатом не потрібно утримувати кнопку прискорення.

### Включає

На спуску натиснути Y, щоб відштовхнутися. Для кермування й трюків є окремі команди.

### Виключає

Зміну темпу всієї симуляції, витрату запасу нітро, утримання звичайного акселератора або вибір напрямку.

### Ігри-носії

- [`GAME-0676` — "Mixtape"](../games/m-r/mixtape.md)

## ACT-902

- Назва: Обрати окремий трюк на скейтборді під час руху
- Переглянуто: `2026-11-24`

### Операційне визначення

Під час руху гравець вибирає команду трюку. Окремі команди запускають звичайний стрибок, обертання дошки чи захват. Після трюку можна далі їхати.

### Включає

Зробити оллі кнопкою A, коли наближається авто, або на вільній ділянці обрати окрему команду фліпу чи ґребу.

### Виключає

Кермування й поштовх, автоматичний трюк біля декорації, тривалий баланс на колесах або розворот дошки для продовження серії з підрахунком очок.

### Ігри-носії

- [`GAME-0676` — "Mixtape"](../games/m-r/mixtape.md)

## ACT-903

- Назва: Захопити енергетичний ключ на відстані й спрямувати його в гніздо
- Переглянуто: `2026-11-24`

### Операційне визначення

У відповідному режимі огляду гравець здобутим знаряддям захоплює доступний енергетичний ключ. Утримуючи його на відстані, гравець наводиться й відпускає ключ у бік вибраного гнізда.

### Включає

У психічному візорі затиснути ZL, щоб захопити енергетичну сферу, навестися на сумісне гніздо й відпустити сферу в його бік.

### Виключає

Піднести ключ до замка упритул, завершити утримуване сканування, перемістити закріплений вузол напрямною або керувати вже випущеним променем.

### Ігри-носії

- [`GAME-0678` — "Metroid Prime 4: Beyond"](../games/m-r/metroid-prime-4-beyond.md)

## ACT-904

- Назва: Утримувати прискорення на підході до придатної поверхні
- Переглянуто: `2026-11-24`

### Операційне визначення

Безпосередньо керуючи персонажем, гравець утримує кнопку прискорення на підході до придатної вигнутої чи крутої поверхні. Команду можна подати під час руху в обраному напрямку.

### Включає

Утримувати прискорення на підході до вигнутої рампи, щоб Сонік набрав швидкість для проходження дугою.

### Виключає

Автоматичне прискорення від контакту з трасою, звичайний стрибок, прискорення машини залежно від нагріву двигуна чи твердження про точний час утримання.

### Ігри-носії

- [`GAME-0682` — "Sonic Dream Team"](../games/s-z/sonic-dream-team.md)

## ACT-905

- Назва: Повертати диск у вибраному напрямку до цифри під покажчиком
- Переглянуто: `2026-11-24`

### Операційне визначення

У наближеному вигляді механізму веди стилусом по колу, щоб повернути диск у вибраному напрямку й підвести цифру під нерухомий покажчик. Якщо потрібен ще один оберт, продовжуй рух повз ті самі позначки.

### Включає

Оберни диск поштової скриньки проти годинникової стрілки від першого суміщення із сімкою, доки сімка знову не опиниться під покажчиком.

### Виключає

Введення числа, натискання окремих кнопок, поворот ключа чи вільне обертання окремої деталі для суміщення з її місцем.

### Ігри-носії

- [`GAME-0683` — "Last Window: The Secret of Cape West"](../games/g-l/last-window-the-secret-of-cape-west.md)

## ACT-906

- Назва: Розмістити здобуті меблі з колекції в режимі редагування
- Переглянуто: `2026-11-24`

### Операційне визначення

Вибери вже здобутий предмет із колекції меблів і постав його в кімнаті. У режимі редагування можна взяти й пересунути предмет, перш ніж повернутися до звичайного керування в кімнаті.

### Включає

Вибери простий стілець, отриманий за першу сітку, постав його на підлогу, а потім візьми й пересунь на іншу клітинку в режимі редагування.

### Виключає

Купівля й розміщення меблів за плату, автоматичне встановлення сюжетного предмета, використання стільця поза режимом редагування або попередній перегляд без фактичного розміщення.

### Ігри-носії

- [`GAME-0685` — "Squeakross: Home Squeak Home"](../games/s-z/squeakross-home-squeak-home.md)

## ACT-907

- Назва: Скласти й виконати команду з дієслова та назв предметів
- Переглянуто: `2026-11-24`

### Операційне визначення

Вибери показане дієслово й додай до підготовленої команди потрібні назви об’єктів зі сцени або спорядження. Підтвердь готову команду, щоб її виконати. Службові слова, наприклад прийменник для знаряддя, підставляє інтерфейс.

### Включає

Вибери команду відмикання, вкажи на вхідні двері, додай ключ зі спорядження й підтвердь готову команду.

### Виключає

Введення довільного тексту, тривале утримання одного режиму інструмента, негайне виконання однієї команди з меню або саме лише наведення на названий предмет.

### Ігри-носії

- [`GAME-0686` — "Maniac Mansion"](../games/m-r/maniac-mansion.md)

## ACT-908

- Назва: Перестрибнути на сусідню колію
- Переглянуто: `2026-11-24`

### Операційне визначення

Поки керований вагон у повітрі, вибери доступну сусідню колію збоку й спрямуй вагон до неї перед приземленням. Після вдалого переходу вагон їде далі новою колією.

### Включає

Стрибни між коліями в ущелині, спрямуй вагон до сусідньої колії й приземлися на неї.

### Виключає

Вибір гілки на розвилці під час руху рейками, зміна колії без відриву коліс, саме лише обертання вагона в повітрі або автоматичний проїзд без вибору сусідньої колії.

### Ігри-носії

- [`GAME-0687` — "Denshattack!"](../games/a-f/denshattack.md)

## ACT-909

- Назва: Вчасно почати занос на позначеному повороті колії
- Переглянуто: `2026-11-24`

### Операційне визначення

Коли вагон наближається до позначеного повороту, увімкни занос для цього повороту. За вдалий момент початку гра може окремо зарахувати чистий занос, поки вагон проходить вигин своєю колією.

### Включає

На позначеному повороті виконай занос і перевір позначку вдалого виконання або поступ додаткового завдання.

### Виключає

Вільне кермування на дорожньому повороті, накопичення ступенів заряду з винагородою після відпускання, зміна колії або утримання вагона на одній парі коліс після стрибка.

### Ігри-носії

- [`GAME-0687` — "Denshattack!"](../games/a-f/denshattack.md)

## ACT-910

- Назва: Накопичити обертання на місці й відпустити для ривка
- Переглянуто: `2026-11-24`

### Операційне визначення

Поки персонаж стоїть на опорі, утримуй напрямок присідання й натисни кнопку обертання. Персонаж готує обертання на місці. Коли відпустиш напрямок присідання, персонаж різко покотиться в бік, куди повернений.

### Включає

За звичайного керування Соніком утримуй «вниз» і натисни A, щоб підготувати ривок з обертанням на місці. Відпусти «вниз», щоб покотитися з цієї точки.

### Виключає

Перехід у перекат із уже набраною швидкістю, стрибок із місця, відпускання кнопки стрибка, автоматичний підкид пружиною або приписування точної швидкості певній кількості обертань.

### Ігри-носії

- [`GAME-0690` — "Sonic Advance"](../games/s-z/sonic-advance.md)

## ACT-911

- Назва: Захопити придатного ворога прямим влучанням короткого імпульсу
- Переглянуто: `2026-11-24`

### Операційне визначення

Спрямуй короткий імпульс у придатного активного ворога. Після прямого влучання ворог переходить у стан захоплення: персонаж несе його із собою й може відпустити окремою дією.

### Включає

У Klonoa 2 вітряний снаряд надуває звичайного Му й підіймає його над Клоноа біля першого навчального уступу.

### Виключає

Підбирання нерухомого предмета дотиком, захоплення істоти до постійного складу, прив’язування скопійованої сили до кнопки або удар, що усуває ворога без захоплення.

### Ігри-носії

- [`GAME-0692` — "Klonoa 2: Lunatea's Veil"](../games/g-l/klonoa-2-lunateas-veil.md)

## ACT-912

- Назва: Підняти плитку попереду в порожній жезл
- Переглянуто: `2026-11-24`

### Операційне визначення

Перебуваючи на твердій підлозі, спрямуй порожній жезл на досяжну звичайну плитку попереду й підніми її. Тепер її можна перенести на інше місце.

### Включає

На поверсі B002 у Void Stranger Ґрей піднімає звичайну плитку безпосередньо перед собою за допомогою початкового Жезла Порожнечі.

### Виключає

Видобування матеріалу з блоку, збирання вільного предмета, зсування плитки безпосередньо в сусідню порожню клітинку або укладання вже захопленої плитки.

### Ігри-носії

- [`GAME-0693` — "Void Stranger"](../games/s-z/void-stranger.md)

## ACT-913

- Назва: Підтвердити продаж усієї партії руди за показаною ціною
- Переглянуто: `2026-11-24`

### Операційне визначення

На придатному пункті збуту гравець одним підтвердженням продає показану партію. Кількість проданої руди списується з рюкзака, а до балансу додається загальна сума за всіма видами.

### Включає

Комп’ютер у майстерні в A Game About Digging A Hole об’єднує два камені й одну одиницю вугілля в один продаж на чотири долари.

### Виключає

Продаж одного окремо вибраного предмета, автоматичне зарахування вільного мінералу при дотику до приймача або автоматична оплата за руду під час виходу на поверхню.

### Ігри-носії

- [`GAME-0694` — "A Game About Digging A Hole"](../games/a-f/a-game-about-digging-a-hole.md)

## ACT-914

- Назва: Обрати форму удару розбігом і стрибком
- Переглянуто: `2026-11-24`

### Операційне визначення

Гравець натискає звичайну кнопку атаки, рухаючись зі спорядженою зброєю ближнього бою. Розбіг, стрибок або їх поєднання дають різні удари, які відрізняються від удару з місця переміщенням і зоною дії.

### Включає

У Terranigma Арк тією самою командою атаки й тим самим списом завдає удару з розбігу, обертового удару в стрибку або ковзного удару після стрибка з розбігу.

### Виключає

Заміна спорядження, перехід в окрему бойову стійку, автоматичне наведення на ціль або стрибок, який не визначає форму удару.

### Ігри-носії

- [`GAME-0695` — "Terranigma"](../games/s-z/terranigma.md)

## ACT-915

- Назва: Обрати попереднє проходження джерелом умов поточної сцени
- Переглянуто: `2026-11-24`

### Операційне визначення

Коли гра пропонує вибрати, за ким іти, гравець обирає придатний збережений запис проходження й підтверджує його як джерело успадкованих умов сцени. Обране джерело можна розпізнати під час дій у новому проходженні.

### Включає

Перед першою сценою порятунку з Нахе в Tides of Tomorrow меню вибору дає змогу підтвердити запис іншого завершеного або ще незавершеного проходження.

### Виключає

Вибір анонімного початкового коду місцевості, приєднання до спільної гри в реальному часі, завантаження власної контрольної точки або отримання випадкового запису без вибору.

### Ігри-носії

- [`GAME-0696` — "Tides of Tomorrow"](../games/s-z/tides-of-tomorrow.md)

## ACT-916

- Назва: Відкрити місцевий відгомін обраного попередника
- Переглянуто: `2026-11-24`

### Операційне визначення

За відповідної підказки в поточній сцені гравець сам вмикає режим спостереження. Він показує дії з обраного попереднього проходження. Роль і запаси поточного гравця зберігаються.

### Включає

На човні Нахе в Tides of Tomorrow команда припливів часу показує попереднього мандрівника в місці, яке згодом може зайняти теперішній герой.

### Виключає

Керування попереднім персонажем, обернення часу поточного проходження, автоматичний рух героя маршрутом або письмовий переказ, якого не можна переглянути на місці.

### Ігри-носії

- [`GAME-0696` — "Tides of Tomorrow"](../games/s-z/tides-of-tomorrow.md)

## ACT-917

- Назва: Викликати атаку комбінацією базових кнопок
- Переглянуто: `2026-11-24`

### Операційне визначення

Під час польоту гравець натискає одну кнопку вогню, визначене поєднання кнопок або окрему кнопку, що його замінює. Команда одразу викликає відповідну атаку, без попереднього вибору спорядження.

### Включає

У Radiant Silvergun поєднання двох із трьох кнопок вогню може дати самонавідну плазму, віяло назад із пострілом уперед або атаку по кількох цілях. Усі три разом викликають меч.

### Виключає

Прокручування списку зброї, постріл після зміни спорядження в меню, вибір режиму за контекстною підказкою або одночасний вогонь із двох незалежних гармат.

### Ігри-носії

- [`GAME-0697` — "Radiant Silvergun"](../games/m-r/radiant-silvergun.md)

## ACT-918

- Назва: Намалювати позначку на відповідній ілюстрації сюжету
- Переглянуто: `2026-11-24`

### Операційне визначення

Гравець відтворює підказану позначку на відповідному зображенні в сюжеті. Жест стосується конкретної деталі зображення. Коли гра його розпізнає, відкривається пов’язана інтерактивна сцена без окремої команди підтвердження.

### Включає

У Song of Bloom відтвори червоне коло з підказки бутона на вершині крейдяної гори, щоб перейти до пейзажу.

### Виключає

Обведення відповіді з окремим підтвердженням, пересування окремої деталі, декоративне малювання або застосування вивченого засобу зміни світу в іншому режимі.

### Ігри-носії

- [`GAME-0698` — "Song of Bloom"](../games/s-z/song-of-bloom.md)

## ACT-919

- Назва: Утримувати вузол поступу, щоб переглянути його підказку
- Переглянуто: `2026-11-24`

### Операційне визначення

Гравець торкається вузла на спільному екрані поступу й утримує дотик, щоб переглянути підказку для пов’язаного маршруту. Перегляд не зараховує проходження вузла.

### Включає

У Song of Bloom утримання першого бутона показує гору з червоною позначкою до того, як цей бутон розквітне.

### Виключає

Оплата нового рівня підказки, підбирання підказки до запасу, обертання фізичного доказу або активація вузла для завершення маршруту.

### Ігри-носії

- [`GAME-0698` — "Song of Bloom"](../games/s-z/song-of-bloom.md)

## ACT-920

- Назва: Оглянути кандидата у світі й вибрати спосіб прийняття до загону
- Переглянуто: `2026-11-24`

### Операційне визначення

Гравець взаємодіє з місцем, де перебуває конкретний кандидат, і відкриває його картку. Можна вибрати один із доступних способів прийняття цього кандидата або закрити картку, залишивши місце в загоні вільним.

### Включає

У Dungeon Master натисни на дзеркало чемпіона й вибери воскресіння або перевтілення. Огляд можна скасувати й продовжити пошук.

### Виключає

Загальний редактор складу, купівля взаємозамінного бійця, перенесення вже активного персонажа або вибір репліки, що не змінює склад загону.

### Ігри-носії

- [`GAME-0699` — "Dungeon Master"](../games/a-f/dungeon-master.md)

## ACT-921

- Назва: Задати силу запуску кулі, утримуючи кнопку пружинного плунжера
- Переглянуто: `2026-11-24`

### Операційне визначення

Поки куля чекає в пусковій доріжці, утримуй кнопку плунжера. Це визначає стиск пружини й силу початкового поштовху. Після запуску куля рухається столом і відскакує від перешкод.

### Включає

В Alien Crush утримання кнопки I на TurboPad стискає пружину для запуску з правої доріжки нижньої частини столу.

### Виключає

Удар фліпером по кулі в русі, пряме керування кулею після запуску, вибір готового типу подачі або заряджання атаки без підготовленої кулі й пружини.

### Ігри-носії

- [`GAME-0704` — "Alien Crush"](../games/a-f/alien-crush.md)

## ACT-922

- Назва: Позначити категорію розбіжності в акті незавершеної перевірки
- Переглянуто: `2026-11-24`

### Операційне визначення

До рішення у справі гравець позначає ймовірну розбіжність у відповідній категорії окремого акта. Позначка існує окремо від результату звіряння двох фактів і від остаточного рішення.

### Включає

У Contraband Police познач ймовірну проблему зі строком дії або фотографією в акті перевірки, перш ніж поставити штамп у паспорті.

### Виключає

Виділення двох фактів, позначення відповідних деталей безпосередньо на обох документах, автоматична позначка після звіряння або остаточний штамп.

### Ігри-носії

- [`GAME-0705` — "Contraband Police"](../games/a-f/contraband-police.md)

## ACT-923

- Назва: Повернути напрям руху на чверть оберту на місці
- Переглянуто: `2026-11-24`

### Операційне визначення

На поточній опорі гравець повертає напрям руху ліворуч або праворуч на 90 градусів і лишається на тій самій клітинці. Наступна команда руху вперед використовує цей напрям у площині опори.

### Включає

У Kula World зроби один поворот на кам’яній грані, щоб спрямувати наступний перекат або підкотитися до стінки.

### Виключає

Рух боком незалежно від напряму, миттєвий крок у вибраний бік, окрема команда розвороту на 180 градусів, поворот лише камери або поворот із закріпленим інструментом, який при цьому зачіпає предмети.

### Ігри-носії

- [`GAME-0706` — "Kula World"](../games/g-l/kula-world.md)

## ACT-924

- Назва: Поставити виділену нерухому зброю всередині визнаного укріплення
- Переглянуто: `2026-11-24`

### Операційне визначення

Під час окремої фази розміщення гравець обирає дозволене місце всередині вже визнаного укріплення й ставить туди одну виділену нерухому одиницю зброї. Вона лишається на цьому місці в наступному бою.

### Включає

У Rampart гравець ставить одну з виділених гармат на вільне місце всередині синьої ділянки перед боєм.

### Виключає

Наказ рухатися вже розгорнутому бійцю, укладання частини муру, підбирання переносної зброї або вибір нової споруди з меню покупок.

### Ігри-носії

- [`GAME-0708` — "Rampart"](../games/m-r/rampart.md)

## ACT-925

- Назва: Окремо підняти, спрямувати й опустити обрану стопу
- Переглянуто: `2026-11-24`

### Операційне визначення

Гравець утримує кнопку підйому обраної стопи, спрямовує підняту стопу й відпускає кнопку, щоб опустити її. Друга стопа може лишатися на землі, поки гравець обирає нову опору.

### Включає

У Baby Steps на PS5 утримуй L2 для лівої стопи або R2 для правої, скоригуй положення піднятої стопи лівим стіком і відпусти відповідний курок.

### Виключає

Автоматичний крок лише за напрямом руху, одночасний стрибок двома ногами або вибір кінцівки, щоб ухопитися за виступ під час лазіння.

### Ігри-носії

- [`GAME-0709` — "Baby Steps"](../games/a-f/baby-steps.md)

## ACT-926

- Назва: Задати гравітацію й кількість кіл для наступного заїзду
- Переглянуто: `2026-11-24`

### Операційне визначення

Перед стартом на поточній трасі гравець обирає гравітацію для всього заїзду й потрібну кількість кіл. Обидва параметри діють у наступному заїзді без редагування окремих секцій дороги.

### Включає

У Racing Destruction Set у меню видно земну гравітацію, а перед зафіксованим одиночним заїздом кількість кіл змінюється з двох до трьох.

### Виключає

Зміна напряму гравітації під час гри, збільшення ліміту часу, заміна двигуна автомобіля або задання ухилу одній секції траси.

### Ігри-носії

- [`GAME-0710` — "Racing Destruction Set"](../games/m-r/racing-destruction-set.md)

## ACT-927

- Назва: Поставити або змінити багаторазову секцію дороги в редакторі
- Переглянуто: `2026-11-24`

### Операційне визначення

У редакторі гравець обирає доступну секцію для певного місця на мапі, може змінити дозволений профіль чи покриття та ставить її на поточній трасі або замінює наявну секцію.

### Включає

У Racing Destruction Set обери трамплін із набору деталей, за потреби скоригуй його висоту й ширину та постав поруч із сусідніми секціями.

### Виключає

Витрачання унікальних деталей з обмеженого запасу, малювання дороги суцільною лінією, водіння на вже готовій секції або купівля цілої траси.

### Ігри-носії

- [`GAME-0710` — "Racing Destruction Set"](../games/m-r/racing-destruction-set.md)

## ACT-928

- Назва: Ударом задати напрям кулі, яка вже в грі
- Переглянуто: `2026-11-25`

### Операційне визначення

Рухомий боєць наближається до кулі, яка вже в грі. Під час удару він задає їй вихідний напрям. Та сама куля продовжує рух.

### Включає

У Firestriker Слейдер підходить до Тріалайта, утримує потрібний напрям і натискає A або B, щоб спрямувати кулю через трав’яну арену.

### Виключає

Випускання нового снаряда, вибір кута на нерухомому пусковому пристрої, пасивний контакт із відбивачем або натискання закріпленої лапки пінболу.

### Ігри-носії

- [`GAME-0713` — "Firestriker"](../games/a-f/firestriker.md)

## ACT-929

- Назва: Рухати нижнього захисника окремо від основного бійця
- Переглянуто: `2026-11-25`

### Операційне визначення

Під час одиночної гри окремі команди пересувають захисника нижньою лінією. Гравець при цьому зберігає керування основним бійцем. Команда руху сама по собі не відбиває кулю.

### Включає

У Firestriker кнопка L рухає Вейна ліворуч, а R — праворуч уздовж нижньої перепони незалежно від Слейдера.

### Виключає

Перемикання активного персонажа, поворот нерухомої лапки пінболу, рух єдиного відбивача або безпосереднє наведення кулі захисником.

### Ігри-носії

- [`GAME-0713` — "Firestriker"](../games/a-f/firestriker.md)

## ACT-930

- Назва: Обрати платну провокацію для певного настрою суперника
- Переглянуто: `2026-11-25`

### Операційне визначення

Обери команду з указаним настроєм і застосуй її до доступного суперника за вказану витрату бойового ресурсу. Під час виконання провокація намагається викликати цей настрій. Результат залежить від вразливості цілі.

### Включає

У Thirsty Suitors Джала обирає провокацію, що викликає жагу, проти Серджіо в закусочній. У його внутрішньому світі вона обирає провокацію, що викликає лють.

### Виключає

Вибір репліки сам по собі, зміна власної стійки нападника, перетягування уваги ворога захисною провокацією або настрій як побічний ефект удару.

### Ігри-носії

- [`GAME-0714` — "Thirsty Suitors"](../games/s-z/thirsty-suitors.md)

## ACT-931

- Назва: Запустити падіння ряду спрямованим поштовхом
- Переглянуто: `2026-11-25`

### Операційне визначення

Підведи героя в позицію для поштовху між вертикальними кісточками або поруч із ними. Задай напрям поштовху, щоб повалити сусідню кісточку.

### Включає

На першій платформі Pushover мураха займає позицію на лівому кінці готового ряду й штовхає першу звичайну кісточку праворуч.

### Виключає

Зіткнення з кісточкою під час ходьби, пересування вертикального предмета на одну клітинку, перенесення кісточки або окреме повалення кожної наступної кісточки.

### Ігри-носії

- [`GAME-0715` — "Pushover"](../games/m-r/pushover.md)

## ACT-932

- Назва: Повернути зону дії споруди перед встановленням
- Переглянуто: `2026-11-25`

### Операційне визначення

Зміни напрям зони дії споруди, поки її встановлення ще не підтверджено. У тому самому місці споруда може охопити інші ділянки місцевості.

### Включає

У Terra Nil під час наведення зрошувача на очищений ґрунт видно команду повороту й спрямовану зону дії.

### Виключає

Поворот камери, поворот твердої деталі для вміщення в ємність, рух курсора без зміни напряму або поворот ручного розпилювача.

### Ігри-носії

- [`GAME-0716` — "Terra Nil"](../games/s-z/terra-nil.md)

## ACT-933

- Назва: Вчасно натискати одну кнопку під час місцевого хору
- Переглянуто: `2026-11-25`

### Операційне визначення

Коли почнеться місцевий хор, натискай ту саму кнопку за наступними підказками. Кожне нове натискання відповідає на одну підказку без вибору напряму, смуги нот чи іншої дії.

### Включає

У Franzea 1 муймуй підказує натискати «Коло» вчасно, поки символи нот рухаються навколо сцени.

### Виключає

Очікування початку співу, натискання для поділу на маршруті, вибір між кількома кнопками інструмента або одне натискання наприкінці вступу.

### Ігри-носії

- [`GAME-0717` — "LocoRoco 2"](../games/g-l/locoroco-2.md)

## ACT-934

- Назва: Позначити ймовірне місце за ескізом маршруту з вершини
- Переглянуто: `2026-11-25`

### Операційне визначення

З доступної оглядової точки обери уривок мапи, наведися на ймовірне місце й постав, перенеси або прибери його позначку. Так ти записуєш здогад перед тим, як іти до місця.

### Включає

На вершині The Bald Edge в A Highland Song обери ескіз східного берега, впізнай скелю у формі зуба й познач місце поруч із нею.

### Виключає

Ланцюжок сполучених позначок, поворот фрагмента для з’єднання мапи, вибір місця автоматичного переходу або підтвердження уривка безпосередньо на місці.

### Ігри-носії

- [`GAME-0718` — "A Highland Song"](../games/a-f/a-highland-song.md)

## ACT-935

- Назва: Обрати або відкликати самостійного супутника під час проходження
- Переглянуто: `2026-11-25`

### Операційне визначення

Під час проходження відкрий вибір супутника. Переглянь доступних істот або варіант без супутника й підтвердь вибір. Потім знову керуй основним персонажем із вибраною підтримкою.

### Включає

У лісі в Alisia Dragoon меню дає змінити Дракона Фрая на Громового крука. Гравець і далі керує Алісією.

### Виключає

Вимушена заміна бійця під прямими командами, наказ супутнику виконати конкретну атаку, кидок супутника в обрану точку або перемикання між персонажами під прямим керуванням.

### Ігри-носії

- [`GAME-0719` — "Alisia Dragoon"](../games/a-f/alisia-dragoon.md)

## ACT-936

- Назва: Утримувати кнопку, щоб прискорити плавання в новій формі
- Переглянуто: `2026-11-25`

### Операційне визначення

Під водою утримуй призначену кнопку прискорення, коли активна форма підтримує вільне плавання. Під час прискорення можна й далі обирати напрям.

### Включає

У затоці Бобів Кадзе в масці акули пливе під кам’яним виступом. У записі з позначкою Xbox підказка пропонує утримувати A для прискорення.

### Виключає

Окремий ривок-атака, короткий поштовх течії, зміна форми від перетину поверхні води або запас кисню.

### Ігри-носії

- [`GAME-0720` — "Kaze and the Wild Masks"](../games/g-l/kaze-and-the-wild-masks.md)

## ACT-937

- Назва: Повернути всю модель, щоб оглянути її з іншого боку
- Переглянуто: `2026-11-25`

### Операційне визначення

Коли вибрано весь предмет, поверни його цілком. Розташування, поворот і розмір частин відносно одна одної зберігаються. Потім можна знову вибрати окрему частину.

### Включає

У The Shape of Things поверни розібраний компас цілком, а потім кнопкою вибору перейди до окремої частини.

### Виключає

Поворот однієї частини відносно сусідніх, зміна допустимості дій через ракурс або перетворення зображення на фізичний об’єкт.

### Ігри-носії

- [`GAME-0721` — "The Shape of Things"](../games/s-z/the-shape-of-things.md)

## ACT-938

- Назва: Змінити вибрану частину способом, заданим головоломкою
- Переглянуто: `2026-11-25`

### Операційне визначення

Вибери одну частину поточного предмета й змінюй її окремо від сусідніх. Від головоломки залежить, чи команда повертає частину, зсуває її або змінює розмір.

### Включає

У The Shape of Things частини компаса повертаються, частини шишки зсуваються, а частини рюкзака змінюють розмір. Рух праворуч або ліворуч діє на вибрану частину.

### Виключає

Довільне розміщення вільних деталей, поворот усього предмета для огляду, вибір будь-якого способу з меню або одночасне застосування всіх перетворень.

### Ігри-носії

- [`GAME-0721` — "The Shape of Things"](../games/s-z/the-shape-of-things.md)

## ACT-939

- Назва: Прицілитися й випустити залп із поточної точки вгорі шахти
- Переглянуто: `2026-11-25`

### Операційне визначення

Гравець веде пальцем, щоб вибрати напрям від поточної точки пуску вгорі шахти. Коли він відпускає палець, усі кульки цього залпу вилітають в обраному напрямку. Кількість кульок у залпі й запас залпів рахуються окремо.

### Включає

У holedown наведи лінію на бічну стіну та відпусти палець. Усі кульки залпу летять у вибраному напрямку, навіть якщо на початку доступна лише одна.

### Виключає

Керування відбивною платформою, окремий напрям для кожної кульки, керування кулькою в польоті або вибір сили пострілу з рогатки.

### Ігри-носії

- [`GAME-0723` — "holedown"](../games/g-l/holedown.md)

## ACT-940

- Назва: Натискати кнопку вчасно за позицією ноти на вибраній доріжці
- Переглянуто: `2026-11-25`

### Операційне визначення

Коли нота на вибраній доріжці доходить до лінії зчитування, гравець натискає кнопку для її позиції. Перехід на іншу доріжку змінює доступні ноти, а пісня продовжує йти в тому самому темпі.

### Включає

У Frequency використовуй L1, R1, R2 або відповідні кнопки на лицьовій панелі для лівої, середньої й правої нот. Щоб зіграти ноти іншого інструмента, спочатку перейди на його доріжку.

### Виключає

Окреме затискання ладу й удар по струнах, натискання для ноти на іншій доріжці або вільна гра без заданого моменту.

### Ігри-носії

- [`GAME-0724` — "Frequency"](../games/a-f/frequency.md)

## ACT-941

- Назва: Замкнути контур і створити захисну оболонку навколо вантажу
- Переглянуто: `2026-11-25`

### Операційне визначення

У режимі малювання обведи придатний вантаж замкненим контуром. Після замикання з’явиться рухома оболонка з умістом, яку можна спрямовувати окремо.

### Включає

Утримуй кнопку малювання й обведи сімох духів біля першого небесного каменя у Tir Tairngire в Soul Bubbles.

### Виключає

Вибір наявного носія, прокладання дороги для іншого персонажа, обведення цілей без створення нового тіла й захоплення бульбашкою, яка сама піднімається після дотику.

### Ігри-носії

- [`GAME-0726` — "Soul Bubbles"](../games/s-z/soul-bubbles.md)

## ACT-942

- Назва: Провести крізь бульбашку, щоб спрямувати на неї потік повітря
- Переглянуто: `2026-11-25`

### Операційне визначення

Проведи стилусом крізь бульбашку в потрібний бік. Довший рух штовхне сильніше, а бульбашка далі рухатиметься під дією потоку.

### Включає

Звичайними рухами стилуса штовхай бульбашку з духами лісовим проходом Tir Tairngire до Куба-брами в Soul Bubbles.

### Виключає

Перетягування за вказівником, поштовх на фіксованій сітці, постійний вітер у середовищі й керування видихом у мікрофон.

### Ігри-носії

- [`GAME-0726` — "Soul Bubbles"](../games/s-z/soul-bubbles.md)

## ACT-943

- Назва: Розділити бульбашку чи з’єднати дотичні бульбашки рухом стилуса
- Переглянуто: `2026-11-25`

### Операційне визначення

Утримуй той самий режим редагування. Розітни одну бульбашку рухом упоперек або проведи від центра однієї дотичної бульбашки до центра іншої, щоб з’єднати їх. Отримані бульбашки далі можна спрямовувати.

### Включає

Підказка маски тигра й окремі бульбашки після розрізу біля тісного проходу в Tir Tairngire 1.

### Виключає

Звичайний потік повітря, перерізання нерухомої мотузки, автоматичне злиття при дотику й копіювання без поділу наявної оболонки.

### Ігри-носії

- [`GAME-0726` — "Soul Bubbles"](../games/s-z/soul-bubbles.md)

## ACT-944

- Назва: Утримувати дотик у режимі здування, щоб зменшити бульбашку
- Переглянуто: `2026-11-25`

### Операційне визначення

Увімкни режим здування й утримуй стилус усередині бульбашки. Відпусти, щоб зупинитися на потрібному розмірі. Якщо тримати далі, оболонка лусне.

### Включає

У першій вправі зі здування в Tir Tairngire маска слона допомагає зменшити бульбашку з духами, щоб провести її крізь вузький прохід.

### Виключає

Пасивне розтягування об стіну, поділ оболонки, перемикання між готовими розмірами та зменшення через пряме пошкодження вмісту.

### Ігри-носії

- [`GAME-0726` — "Soul Bubbles"](../games/s-z/soul-bubbles.md)

## ACT-945

- Назва: Затягнути наживлений гвинт окремим ручним інструментом
- Переглянуто: `2026-11-25`

### Операційне визначення

Приклади викрутку до наживленого гвинта. Користуйся нею, доки гвинт не заглибиться в кріплення. Самого встановлення гвинта в отвір для цього замало.

### Включає

У Familiar з Miniatures встав два гвинти в отвори кріпильної планки й затягни їх викруткою врівень із поверхнею.

### Виключає

Перетягування гвинта одразу в остаточне положення, забивання штифта, повертання всієї конструкції й декоративне знаряддя, яке не застосовують до кріплення.

### Ігри-носії

- [`GAME-0727` — "Miniatures"](../games/m-r/miniatures.md)

## ACT-946

- Назва: Утримувати тягу й спрямовувати мех у польоті
- Переглянуто: `2026-11-25`

### Операційне визначення

Утримуй кнопку польоту, щоб рушії підіймали мех, і спрямовуй його вбік у межах проходу. За потреби відпусти кнопку й натисни знову, щоб змінити підйом і пройти між перешкодами.

### Включає

У Rescue at Axis 5 утримуй B, щоб підняти Nitro шахтою станції. Відпускай і натискай кнопку знову, коли треба скоригувати політ між платформами.

### Виключає

Окремий стрибок або короткий ривок, вибір точки призначення, перемикання постійного режиму польоту й припущення, що всі мехи літають однаково.

### Ігри-носії

- [`GAME-0728` — "Metal Warriors"](../games/m-r/metal-warriors.md)

## ACT-947

- Назва: Перетягнути предмет на інше місце в упорядкованому ряду
- Переглянуто: `2026-11-25`

### Операційне визначення

Вибери рухомий предмет, перетягни його з поточного місця до проміжку між іншими предметами ряду й постав. Предмети між старим і новим місцем посунуться без окремої дії для кожного.

### Включає

У головоломці з першою полицею перетягни найвищу книжку із середини на лівий край. Книжки між цими місцями посунуться, зберігаючи відносний порядок.

### Виключає

Обмін двох предметів місцями, зміна текстового значення у фіксованій позиції, переміщення всього ряду разом і вільне розміщення предмета без вибору його місця в порядку.

### Ігри-носії

- [`GAME-0730` — "A Little to the Left"](../games/a-f/a-little-to-the-left.md)

## ACT-948

- Назва: Спрямовувати заклинання на клітинку за напрямком і позою
- Переглянуто: `2026-11-25`

### Операційне визначення

Скеруй заклинання на клітинку, до якої можна дістати на певній відстані від керованого персонажа. Напрямок визначає бік, а поза змінює розташування цілі. Під час стрибка в межі дії може потрапити інша клітинка.

### Включає

У Solomon’s Key кнопка A спрямовує заклинання вперед, коли Дана стоїть, або нижче, коли він присідає. Під час стрибка можна дістати клітинку на іншій висоті.

### Виключає

Довільний вибір віддаленої клітинки, взаємодія лише з наявним перемикачем, рух проходом або сама зміна заповненості цільової клітинки.

### Ігри-носії

- [`GAME-0733` — "Solomon's Key"](../games/s-z/solomons-key.md)

## ACT-949

- Назва: Вибирати малюнок порядком напрямків у графіті
- Переглянуто: `2026-11-25`

### Операційне визначення

Під час роботи з позначеною поверхнею гравець веде вказівник через допустимі точки у вибраному порядку. Прийнята послідовність визначає новий малюнок. Різні допустимі послідовності можуть давати різні малюнки в тому самому місці.

### Включає

На першій стіні пагорба Версум з’єднай показані точки стіком Xbox. Під час повторної спроби вибери інший порядок, щоб нанести на цю стіну інший малюнок.

### Виключає

Виконання єдиної заданої послідовності для перевірки вводу, нанесення заздалегідь вибраної наліпки однією кнопкою, довільне малювання пікселів і повторне зарахування репутації за місце.

### Ігри-носії

- [`GAME-0736` — "Bomb Rush Cyberfunk"](../games/a-f/bomb-rush-cyberfunk.md)

## ACT-950

- Назва: Братися за грань блока й змінювати глибину висування
- Переглянуто: `2026-11-25`

### Операційне визначення

Гравець береться за доступну грань блока й штовхає чи тягне його вздовж сталої осі. Кожне завершене зміщення переводить той самий блок у сусіднє положення за глибиною. Висота й форма блока зберігаються.

### Включає

В уроці 3 Pullblox візьмися за нижній помаранчевий блок і кілька разів відступи з ним. Потім стрибни на відкриту сходинку, щоб дістатися наступного блока.

### Виключає

Вільне пересування ящика за двома осями, зміна ракурсу незмінної стіни, видовження одного краю без зміщення передньої грані й підйом нерухомими сходами.

### Ігри-носії

- [`GAME-0737` — "Pullblox"](../games/m-r/pullblox.md)

## ACT-951

- Назва: Спрямовувати й виконувати стрибок між придатними опорами
- Переглянуто: `2026-11-25`

### Операційне визначення

Закріпившись на придатній опорі, гравець наводиться на допустиму точку приземлення на іншій поверхні й відпускає керування рухом, щоб стрибнути. Так можна цілитися в доступну опору на підлозі, стелі чи стіні.

### Включає

У Порожнечі в Dandara наведися керуванням стрибка з початкової смуги на підлозі на смугу на стелі й відпусти. З нової опори спрямуй наступний стрибок униз, до іншої смуги на підлозі.

### Виключає

Вільний стрибок у довільну точку, безперервне керування в польоті, телепорт без перетину проміжного простору й окремий рух, що потребує заряджання.

### Ігри-носії

- [`GAME-0738` — "Dandara: Trials of Fear Edition"](../games/a-f/dandara-trials-of-fear-edition.md)
