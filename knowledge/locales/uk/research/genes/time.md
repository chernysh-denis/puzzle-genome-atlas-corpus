# Гени часу

## TIM-001

- Назва: Один хід із повним виконанням команди
- Переглянуто: `2026-08-24`

### Операційне визначення

Гравець подає одну команду, система повністю виконує всі спричинені нею зміни й лише після цього приймає наступну команду.

### Включає

Один напрямок у 2048 із наступними рухом, злиттями, нарахуванням очок і появою плитки; одне відкриття в Minesweeper з наступним розширенням нульової області; один хід Royal Match з наступними всіма ефектами збігів, підсилювачів, падіння, поповнення й каскадів; один вибір джерела й місця призначення у Water Sort з наступним максимальним переливанням; один напрямок у Baba Is You з наступними рухом і повторним обчисленням правил; один свайп Threes із наступними однокроковим зсувом, злиттям і введенням наступника; один розіграш або скидання в Balatro з наступними оцінюванням і поповненням руки; один стрибок Peg Solitaire з наступним вилученням проміжного кілка; одне розміщення плитки Dorfromantik із наступним розв’язанням країв, груп, завдань, рахунку й запасу; один рух або поворот у Stephen’s Sausage Roll із наступними контактом виделки, ковзанням чи коченням ковбаски, готуванням і перевірками поразки чи завершення; один рух у A Good Snowman Is Hard to Build із наступними витрачанням снігу, зростанням, перенесенням стосу й перевірками завершення; один крок голови Snakebird із наступними поширенням тіла, зростанням від фрукта, активацією виходу, падінням без опори й перевірками смерті чи завершення; одне бінарне твердження в Hexcells Infinite з наступними негайною перевіркою істинності, обробкою помилки й перевіркою завершення; одне витратне за хід переміщення, редагування черги чи активація черги в Shogun Showdown із наступним повним просуванням станів гравця й ворогів; одне штовхання в A Monster’s Expedition із наступними повним перекиданням або максимальним коченням колоди, укладанням мосту й перевіркою прибуття; одна команда Bonfire Peaks із наступними повним рухом форми предмета, який несе персонаж, знищенням у вогні й перевіркою завершення; одне підтвердження карти й напрямку в Golf Peaks із наступними повним поетапним рухом м’яча, реакцією рельєфу, усталенням і оцінюванням потрапляння в лунку; одне розміщення inbento з наступними перевіркою контуру, витрачанням запасу, перезаписом накритих клітинок і перевіркою точного рецепта; одне підтвердження початкової області та кольору в KAMI з наступними повним перефарбуванням компоненти, злиттям суміжних компонент одного класу, обліком ходів і оцінюванням усього поля; одне натискання тригера HOOK із наступним повним зв’язаним втягуванням, вилученням або оцінюванням зіткнення та скидання; один напрямок в Inertia з наступними повним прямолінійним ковзанням, збиранням під час проходження, зупиненням і перевірками міни чи завершення; один завершений хід персонажа або ворога у Clair Obscur: Expedition 33.

### Виключає

Введення в реальному часі та одночасне незавершене планування.

### Ігри-носії

- [`GAME-0001` — "2048"](../games/0-9/2048.md)
- [`GAME-0044` — A Good Snowman Is Hard to Build](../games/a-f/a-good-snowman-is-hard-to-build.md)
- [`GAME-0054` — A Monster’s Expedition](../games/a-f/a-monsters-expedition.md)
- [`GAME-0013` — Baba Is You](../games/a-f/baba-is-you.md)
- [`GAME-0017` — Balatro](../games/a-f/balatro.md)
- [`GAME-0148` — Baldur’s Gate 3](../games/a-f/baldurs-gate-3.md)
- [`GAME-0055` — Bonfire Peaks](../games/a-f/bonfire-peaks.md)
- [`GAME-0053` — Can of Wormholes](../games/a-f/can-of-wormholes.md)
- [`GAME-0109` — Candy Crush Saga](../games/a-f/candy-crush-saga.md)
- [`GAME-0144` — Clair Obscur: Expedition 33](../games/a-f/clair-obscur-expedition-33.md)
- [`GAME-0020` — Dorfromantik](../games/a-f/dorfromantik.md)
- [`GAME-0057` — Golf Peaks](../games/g-l/golf-peaks.md)
- [`GAME-0049` — Hexcells Infinite](../games/g-l/hexcells-infinite.md)
- [`GAME-0060` — HOOK](../games/g-l/hook.md)
- [`GAME-0099` — HyperRogue](../games/g-l/hyperrogue.md)
- [`GAME-0058` — inbento](../games/g-l/inbento.md)
- [`GAME-0070` — Inertia](../games/g-l/inertia.md)
- [`GAME-0059` — KAMI](../games/g-l/kami.md)
- [`GAME-0003` — Minesweeper](../games/m-r/minesweeper.md)
- [`GAME-0019` — Peg Solitaire](../games/m-r/peg-solitaire.md)
- [`GAME-0009` — Royal Match](../games/m-r/royal-match.md)
- [`GAME-0050` — Shogun Showdown](../games/s-z/shogun-showdown.md)
- [`GAME-0045` — Snakebird](../games/s-z/snakebird.md)
- [`GAME-0043` — Stephen’s Sausage Roll](../games/s-z/stephens-sausage-roll.md)
- [`GAME-0015` — Threes](../games/s-z/threes.md)
- [`GAME-0010` — Water Sort](../games/s-z/water-sort.md)

## TIM-002

- Назва: Послідовні дії у власному темпі
- Переглянуто: `2026-08-24`

### Операційне визначення

Гравець може робити паузу між дискретними діями, і кожна завершена дія змінює стан без кроку системи, зумовленого часом.

### Включає

Розв’язання фізичного кубика Рубіка без таймера; розв’язання друкованого Sudoku без зовнішнього змагального таймера; класичний рівень Sokoban без таймера чи автоматичного руху; класичний FreeCell із ручним перенесенням карт; розв’язання друкованого Nonogram без зовнішнього таймера; дослідження корабля, огляд застиглих спогадів і редагування книги в Return of the Obra Dinn; звичайне дослідження видів, розділення шарів і компонування панелей Gorogoa; рух, штовхання й переходи між контейнерами в Patrick’s Parabox; прокреслення та редагування базової панелі The Witness без таймера; переставляння фрагментів мапи Carto й ходіння утвореним світом без примусового годинника; огляд, виділення термінів і редагування сувою події в The Case of the Golden Idol; малювання, відведення назад і повторне малювання маршрутів LYNE без примусового годинника чи часового кроку поля; призначення та редагування кількості цяток Hexologic без примусового годинника чи автоматичного кроку світу; огляд і вибір допустимої трійки з фіксованого пасьянсного поля SET без строку; завершення пропозицій Mastermind проти одного фіксованого коду без строку; введення спроб Wordle без строку для окремого рядка; натискання кнопок Lights Out без примусового годинника чи автономної зміни поля між натисканнями; призначення та редагування діагоналей Slant без строку; установлення та редагування позначок зайнятості Tents без примусового годинника; установлення та редагування пар Dominosa; циклічна зміна та редагування кратностей зв’язків Bridges; установлення та редагування ламп Light Up без автономної зміни чи строку; вибір і редагування ребер Loopy без примусового годинника чи часового кроку поля; призначення та редагування кольорів областей Map без автономного перебігу; малювання та редагування меж областей Galaxies без примусового годинника; призначення та редагування цифр Filling без строку; призначення та редагування цифр Keen без строку; обертання, фіксація та редагування плиток Net без примусового годинника чи автономної зміни мережі; зсув і редагування ліній Netslide без автоматичного перебігу між ходами; огляд і маніпулювання першим сейфом The Room без примусового годинника; повторне складання Josef на звалищі Machinarium без автономного перебігу між підтвердженими взаємодіями; передавання інгредієнтів батареї Red Edison у Day of the Tentacle без розпаду часткового набору чи строку; обертання мосту Chapter I в Monument Valley та вибір місця призначення Ida без строку чи незалежного перебігу світу між командами; анотування, зіставлення та редагування гіпотез щодо гліфів Chants of Sennaar, поки світ чекає наступної дискретної команди.

### Виключає

Змагальний час як зовнішня умова оцінювання; автоматичне розв’язання після дії; безперервна зміна стану в реальному часі.

### Ігри-носії

- [`GAME-0066` — Black Box](../games/a-f/black-box.md)
- [`GAME-0173` — Blue Prince](../games/a-f/blue-prince.md)
- [`GAME-0074` — Bridges](../games/a-f/bridges.md)
- [`GAME-0040` — Carto](../games/a-f/carto.md)
- [`GAME-0101` — Chants of Sennaar](../games/a-f/chants-of-sennaar.md)
- [`GAME-0011` — Chess](../games/a-f/chess.md)
- [`GAME-0108` — Cocoon](../games/a-f/cocoon.md)
- [`GAME-0088` — Day of the Tentacle](../games/a-f/day-of-the-tentacle.md)
- [`GAME-0073` — Dominosa](../games/a-f/dominosa.md)
- [`GAME-0079` — Filling](../games/a-f/filling.md)
- [`GAME-0012` — Flow Free](../games/a-f/flow-free.md)
- [`GAME-0007` — FreeCell](../games/a-f/freecell.md)
- [`GAME-0078` — Galaxies](../games/g-l/galaxies.md)
- [`GAME-0024` — Gorogoa](../games/g-l/gorogoa.md)
- [`GAME-0106` — Her Story](../games/g-l/her-story.md)
- [`GAME-0062` — Hexologic](../games/g-l/hexologic.md)
- [`GAME-0123` — Inscryption](../games/g-l/inscryption.md)
- [`GAME-0080` — Keen](../games/g-l/keen.md)
- [`GAME-0075` — Light Up](../games/g-l/light-up.md)
- [`GAME-0069` — Lights Out](../games/g-l/lights-out.md)
- [`GAME-0076` — Loopy](../games/g-l/loopy.md)
- [`GAME-0061` — LYNE](../games/g-l/lyne.md)
- [`GAME-0086` — Machinarium](../games/m-r/machinarium.md)
- [`GAME-0077` — Map](../games/m-r/map.md)
- [`GAME-0065` — Mastermind](../games/m-r/mastermind.md)
- [`GAME-0093` — Monument Valley](../games/m-r/monument-valley.md)
- [`GAME-0111` — Myst](../games/m-r/myst.md)
- [`GAME-0083` — Net](../games/m-r/net.md)
- [`GAME-0084` — Netslide](../games/m-r/netslide.md)
- [`GAME-0008` — Nonogram](../games/m-r/nonogram.md)
- [`GAME-0117` — OneShot](../games/m-r/oneshot.md)
- [`GAME-0036` — "Patrick’s Parabox"](../games/m-r/patricks-parabox.md)
- [`GAME-0081` — Pearl](../games/m-r/pearl.md)
- [`GAME-0023` — Return of the Obra Dinn](../games/m-r/return-of-the-obra-dinn.md)
- [`GAME-0002` — "Rubik’s Cube"](../games/m-r/rubiks-cube.md)
- [`GAME-0063` — Rush Hour](../games/m-r/rush-hour.md)
- [`GAME-0064` — SET](../games/s-z/set.md)
- [`GAME-0082` — Signpost](../games/s-z/signpost.md)
- [`GAME-0071` — Slant](../games/s-z/slant.md)
- [`GAME-0006` — Sokoban](../games/s-z/sokoban.md)
- [`GAME-0156` — Strands](../games/s-z/strands.md)
- [`GAME-0005` — Sudoku](../games/s-z/sudoku.md)
- [`GAME-0072` — Tents](../games/s-z/tents.md)
- [`GAME-0046` — The Case of the Golden Idol](../games/s-z/the-case-of-the-golden-idol.md)
- [`GAME-0102` — The Password Game](../games/s-z/the-password-game.md)
- [`GAME-0107` — The Pedestrian](../games/s-z/the-pedestrian.md)
- [`GAME-0085` — The Room](../games/s-z/the-room.md)
- [`GAME-0090` — The Talos Principle](../games/s-z/the-talos-principle.md)
- [`GAME-0039` — The Witness](../games/s-z/the-witness.md)
- [`GAME-0115` — Unpacking](../games/s-z/unpacking.md)
- [`GAME-0068` — Wordle](../games/s-z/wordle.md)

## TIM-003

- Назва: Давати команди, поки світ змінюється в реальному часі
- Переглянуто: `2026-09-04`

### Операційне визначення

Система змінює стан, у якому приймаються рішення, за розкладом реального часу й водночас приймає команди гравця протягом обмеженого проміжку до остаточної фіксації поточного стану.

### Включає

Переміщення, обертання або прискорення тетроміно NES Tetris, поки гравітація продовжує планувати падіння й остаточну фіксацію; розміщення елементів Pipe Dream, поки Flooz просувається побудованим трубопроводом; редагування мережі Mini Metro, поки станції, попит і транспорт змінюються за активним годинником симуляції; перерізання опор у Cut the Rope, поки цукерка продовжує гойдатися, падати й стикатися під дією живої фізики; компонування панелі Gorogoa під час єдиної рухомої задачі на точний момент, визначеної розробником; приєднання вузлів World of Goo, поки тривають гравітація, пружність, плавучість і рух вільних кульок; віддавання наказів загонам Bad North, поки просуваються транспортні судна, солдати й бій, зі сповільненням під час вибору як параметром; розміщення карт Loop Hero та заміна спорядження, поки просуваються герой, добовий цикл і сутички, з паузою як засобом планування; навігація й редагування випробування HUMANITY, поки ворота випускають людей і натовп рухається, із зупиненням часу та прискоренням; зміна положення маршрутних пристроїв Tin Hearts, поки солдатики йдуть і стикаються, з паузою та прискоренням як засобами зміни швидкості; рух і постріли порталами, поки триває фізика тіла в Portal; біг, стрибки або керування перемикачами, поки вороги й платформи Braid рухаються; відправлення й відкликання Pikmin, поки просуваються поверхневі роботи, перенесення, бій і добовий цикл; створення й обмін тілами The Swapper, поки тривають сповільнені гравітація та зіткнення; рух, стрибки й накладання зображень, поки фізика тіла Viewfinder лишається активною; складання й застосування рибальського пристрою The Longest Journey, поки його невиправлене надуте каченя продовжує втрачати повітря до замикання затискача; переміщення, прицілювання й відпускання шахової фігури Superliminal, поки лишаються активними оновлення положення предмета в руках та гравітація відпущеного тіла; зміна системи відліку гравітації Manifold Garden або керування періодичним падінням, поки триває фізика тіла; перенесення, опускання й перехід із рекурсивним ключем Maquette, поки лишаються активними положення ключа в руках, зіткнення й рух персонажа; розміщення, налаштування чи вилучення фабричних об’єктів Factorio, поки за активним годинником симуляції тривають видобування, перевезення, виробництво, дослідження, електропостачання, забруднення та дії ворогів; редагування доріг, зон, служб і політик SimCity 4 або Cities: Skylines, поки за активним годинником тривають забудова, рух і фінанси; навігація, прицілювання, бій, зламування й водіння в Cyberpunk 2077, поки персонажі світу й бій просуваються в реальному часі; рух, атаки, лікування, застосування здібностей і боротьба за ціль в Marvel Rivals, поки бій і годинники цілі лишаються активними; навігація, удари, застосування здібностей, зв’язування й ухилення в Hollow Knight: Silksong, поки вороги та небезпеки рухаються в реальному часі; пересування, застосування гака, керування перемикачами, пілотування й стрільба в Chapter 1 Split Fiction, поки небезпеки, транспорт і противники продовжують діяти в реальному часі; керування Farrah, поки потреби, настрій, автономні дії та спілкування тривають у режимі життя The Sims 4; рух, передачі, удари, перемикання й відбирання в EA SPORTS FC 26, поки м’яч, гравці, арбітр і годинник матчу продовжують діяти; коротке або тривале натискання єдиної вертикальної команди Geometry Dash, поки Stereo Madness продовжує автоматичний рух, фізику та заданий автором відлік рівня; рух, атаки, захист, кидки або витрачання Drive у Street Fighter 6, поки обидва бійці, снаряди, стани відновлення й годинник раунду лишаються активними; рух, спостереження, прорив, стрільба, застосування пристроїв, установлення чи вимкнення деактиватора в Rainbow Six Siege, поки відліки фаз й противники продовжують діяти; перегляд ролей, вказівок і замін Football Manager 26, поки автономний матч, стан гравців і годинник змінюються; кермування, стрибки, прискорення й контакт із м’ячем Rocket League, поки всі авто, фізика м’яча, можливості майданчиків і годинник матчу лишаються активними; кермування, гальмування, прискорення й тарани Need for Speed Payback, поки автовоз, Enforcers, дорожній рух, пошкодження й тиск місії продовжують діяти; кермування, гальмування й проходження контрольних точок у Trackmania, поки автомобіль рухається, а годинник заїзду не зупиняється; кермування й гальмування Need for Speed Underground, поки троє суперників, стан зіткнень і годинник вступного Circuit продовжують діяти.

### Виключає

Команду, після якої всі наслідки обчислюються до кінця без подальшого введення; дії у власному темпі без зміни стану з часом; зовнішній секундомір, який лише вимірює результат.

### Ігри-носії

- [`GAME-0233` — 7 Days to Die](../games/0-9/7-days-to-die.md)
- [`GAME-0228` — A Way Out](../games/a-f/a-way-out.md)
- [`GAME-0124` — Against the Storm](../games/a-f/against-the-storm.md)
- [`GAME-0179` — Age of Empires II: Definitive Edition](../games/a-f/age-of-empires-ii-definitive-edition.md)
- [`GAME-0223` — Aion Classic](../games/a-f/aion-classic.md)
- [`GAME-0257` — "Alien: Isolation"](../games/a-f/alien-isolation.md)
- [`GAME-0110` — Angry Birds Classic](../games/a-f/angry-birds-classic.md)
- [`GAME-0132` — Anno 1800](../games/a-f/anno-1800.md)
- [`GAME-0097` — Antichamber](../games/a-f/antichamber.md)
- [`GAME-0154` — Apex Legends](../games/a-f/apex-legends.md)
- [`GAME-0143` — ARC Raiders](../games/a-f/arc-raiders.md)
- [`GAME-0242` — "Asphalt Legends"](../games/a-f/asphalt-legends.md)
- [`GAME-0027` — Bad North: Jotunn Edition](../games/a-f/bad-north.md)
- [`GAME-0148` — Baldur’s Gate 3](../games/a-f/baldurs-gate-3.md)
- [`GAME-0255` — "Batman: Arkham Asylum Game of the Year Edition"](../games/a-f/batman-arkham-asylum-game-of-the-year-edition.md)
- [`GAME-0234` — Battlefield 2042](../games/a-f/battlefield-2042.md)
- [`GAME-0149` — Battlefield 6](../games/a-f/battlefield-6.md)
- [`GAME-0243` — Battlefield Hardline](../games/a-f/battlefield-hardline.md)
- [`GAME-0220` — Battlefield V](../games/a-f/battlefield-v.md)
- [`GAME-0195` — BeamNG.drive](../games/a-f/beamng-drive.md)
- [`GAME-0256` — "BioShock™ Remastered"](../games/a-f/bioshock-remastered.md)
- [`GAME-0189` — "Black Myth: Wukong"](../games/a-f/black-myth-wukong.md)
- [`GAME-0034` — Braid, Anniversary Edition](../games/a-f/braid.md)
- [`GAME-0198` — Brawlhalla](../games/a-f/brawlhalla.md)
- [`GAME-0222` — "Call of Juarez: Gunslinger"](../games/a-f/call-of-juarez-gunslinger.md)
- [`GAME-0135` — "Captain of Industry"](../games/a-f/captain-of-industry.md)
- [`GAME-0121` — "Cities: Skylines"](../games/a-f/cities-skylines.md)
- [`GAME-0144` — Clair Obscur: Expedition 33](../games/a-f/clair-obscur-expedition-33.md)
- [`GAME-0254` — CONTROL Ultimate Edition](../games/a-f/control-ultimate-edition.md)
- [`GAME-0209` — Cossacks 3](../games/a-f/cossacks-3.md)
- [`GAME-0137` — Counter-Strike 2](../games/a-f/counter-strike-2.md)
- [`GAME-0218` — Counter-Strike](../games/a-f/counter-strike.md)
- [`GAME-0204` — "Crusader Kings III"](../games/a-f/crusader-kings-iii.md)
- [`GAME-0246` — Crysis Remastered](../games/a-f/crysis-remastered.md)
- [`GAME-0021` — Cut the Rope](../games/a-f/cut-the-rope.md)
- [`GAME-0146` — Cyberpunk 2077](../games/a-f/cyberpunk-2077.md)
- [`GAME-0210` — DayZ](../games/a-f/dayz.md)
- [`GAME-0161` — Dead by Daylight](../games/a-f/dead-by-daylight.md)
- [`GAME-0259` — "Dead Space (2023 remake)"](../games/a-f/dead-space-2023.md)
- [`GAME-0200` — Delta Force](../games/a-f/delta-force.md)
- [`GAME-0193` — Destiny 2](../games/a-f/destiny-2.md)
- [`GAME-0252` — "Detroit: Become Human"](../games/a-f/detroit-become-human.md)
- [`GAME-0247` — Dishonored (2012)](../games/a-f/dishonored-2012.md)
- [`GAME-0186` — "Don’t Starve Together"](../games/a-f/dont-starve-together.md)
- [`GAME-0245` — DOOM (2016)](../games/a-f/doom-2016.md)
- [`GAME-0138` — Dota 2](../games/a-f/dota-2.md)
- [`GAME-0126` — Dwarf Fortress](../games/a-f/dwarf-fortress.md)
- [`GAME-0131` — Dyson Sphere Program](../games/a-f/dyson-sphere-program.md)
- [`GAME-0163` — EA SPORTS FC 26](../games/a-f/ea-sports-fc-26.md)
- [`GAME-0092` — Echochrome](../games/a-f/echochrome.md)
- [`GAME-0152` — Elden Ring](../games/a-f/elden-ring.md)
- [`GAME-0169` — Euro Truck Simulator 2](../games/a-f/euro-truck-simulator-2.md)
- [`GAME-0119` — Factorio](../games/a-f/factorio.md)
- [`GAME-0231` — Fallout 4](../games/a-f/fallout-4.md)
- [`GAME-0236` — Far Cry 3](../games/a-f/far-cry-3.md)
- [`GAME-0196` — Farming Simulator 25](../games/a-f/farming-simulator-25.md)
- [`GAME-0091` — Fez](../games/a-f/fez.md)
- [`GAME-0188` — FINAL FANTASY XIV Online](../games/a-f/final-fantasy-xiv-online.md)
- [`GAME-0175` — Football Manager 26](../games/a-f/football-manager-26.md)
- [`GAME-0227` — Fortnite](../games/a-f/fortnite.md)
- [`GAME-0171` — Forza Horizon 6](../games/a-f/forza-horizon-6.md)
- [`GAME-0130` — Frostpunk](../games/a-f/frostpunk.md)
- [`GAME-0167` — Geometry Dash](../games/g-l/geometry-dash.md)
- [`GAME-0024` — Gorogoa](../games/g-l/gorogoa.md)
- [`GAME-0145` — Grand Theft Auto V](../games/g-l/grand-theft-auto-v.md)
- [`GAME-0251` — Hades](../games/g-l/hades.md)
- [`GAME-0239` — Half-Life (1998)](../games/g-l/half-life-1998.md)
- [`GAME-0212` — Half-Life 2](../games/g-l/half-life-2.md)
- [`GAME-0182` — Hearts of Iron IV](../games/g-l/hearts-of-iron-iv.md)
- [`GAME-0159` — Helldivers 2](../games/g-l/helldivers-2.md)
- [`GAME-0248` — HITMAN World of Assassination](../games/g-l/hitman-world-of-assassination.md)
- [`GAME-0150` — "Hollow Knight: Silksong"](../games/g-l/hollow-knight-silksong.md)
- [`GAME-0112` — Human: Fall Flat](../games/g-l/human-fall-flat.md)
- [`GAME-0029` — HUMANITY](../games/g-l/humanity.md)
- [`GAME-0098` — Hyperbolica](../games/g-l/hyperbolica.md)
- [`GAME-0215` — It Takes Two](../games/g-l/it-takes-two.md)
- [`GAME-0100` — Keep Talking and Nobody Explodes](../games/g-l/keep-talking-and-nobody-explodes.md)
- [`GAME-0240` — "Kingdom Come: Deliverance II"](../games/g-l/kingdom-come-deliverance-ii.md)
- [`GAME-0192` — Left 4 Dead 2](../games/g-l/left-4-dead-2.md)
- [`GAME-0025` — Lemmings](../games/g-l/lemmings.md)
- [`GAME-0219` — Lineage II](../games/g-l/lineage-ii.md)
- [`GAME-0028` — Loop Hero](../games/g-l/loop-hero.md)
- [`GAME-0214` — "Mafia (2002)"](../games/m-r/mafia-2002.md)
- [`GAME-0095` — Manifold Garden](../games/m-r/manifold-garden.md)
- [`GAME-0096` — Maquette](../games/m-r/maquette.md)
- [`GAME-0147` — Marvel Rivals](../games/m-r/marvel-rivals.md)
- [`GAME-0238` — "Max Payne (2001)"](../games/m-r/max-payne-2001.md)
- [`GAME-0260` — Metro Exodus](../games/m-r/metro-exodus.md)
- [`GAME-0180` — Microsoft Flight Simulator 2024](../games/m-r/microsoft-flight-simulator-2024.md)
- [`GAME-0129` — Minecraft](../games/m-r/minecraft.md)
- [`GAME-0018` — Mini Metro](../games/m-r/mini-metro.md)
- [`GAME-0051` — Mini Motorways](../games/m-r/mini-motorways.md)
- [`GAME-0151` — Monster Hunter Wilds](../games/m-r/monster-hunter-wilds.md)
- [`GAME-0207` — 'Monster Hunter: World'](../games/m-r/monster-hunter-world.md)
- [`GAME-0194` — "Mount & Blade II: Bannerlord"](../games/m-r/mount-and-blade-ii-bannerlord.md)
- [`GAME-0202` — "NARAKA: BLADEPOINT"](../games/m-r/naraka-bladepoint.md)
- [`GAME-0241` — NBA 2K26](../games/m-r/nba-2k26.md)
- [`GAME-0244` — "Need for Speed Heat"](../games/m-r/need-for-speed-heat.md)
- [`GAME-0226` — "Need for Speed: Most Wanted (2005)"](../games/m-r/need-for-speed-most-wanted-2005.md)
- [`GAME-0208` — 'Need for Speed Payback'](../games/m-r/need-for-speed-payback.md)
- [`GAME-0235` — "Need for Speed: The Run"](../games/m-r/need-for-speed-the-run.md)
- [`GAME-0199` — "Need for Speed Unbound"](../games/m-r/need-for-speed-unbound.md)
- [`GAME-0217` — "Need for Speed Underground"](../games/m-r/need-for-speed-underground.md)
- [`GAME-0229` — "No Man’s Sky"](../games/m-r/no-mans-sky.md)
- [`GAME-0224` — Once Human](../games/m-r/once-human.md)
- [`GAME-0105` — Outer Wilds](../games/m-r/outer-wilds.md)
- [`GAME-0181` — Overwatch](../games/m-r/overwatch.md)
- [`GAME-0125` — Oxygen Not Included](../games/m-r/oxygen-not-included.md)
- [`GAME-0139` — Palworld](../games/m-r/palworld.md)
- [`GAME-0162` — Path of Exile 2](../games/m-r/path-of-exile-2.md)
- [`GAME-0201` — PAYDAY 2](../games/m-r/payday-2.md)
- [`GAME-0232` — PAYDAY 3](../games/m-r/payday-3.md)
- [`GAME-0203` — "PEAK"](../games/m-r/peak.md)
- [`GAME-0114` — Peggle Deluxe](../games/m-r/peggle-deluxe.md)
- [`GAME-0035` — Pikmin 4](../games/m-r/pikmin-4.md)
- [`GAME-0016` — Pipe Mania / Pipe Dream](../games/m-r/pipe-mania.md)
- [`GAME-0160` — "Pokémon Legends: Z-A"](../games/m-r/pokemon-legends-z-a.md)
- [`GAME-0113` — Portal 2 — Cooperative Campaign](../games/m-r/portal-2-co-op.md)
- [`GAME-0033` — Portal](../games/m-r/portal.md)
- [`GAME-0258` — "Prey (2017)"](../games/m-r/prey-2017.md)
- [`GAME-0142` — Project Zomboid](../games/m-r/project-zomboid.md)
- [`GAME-0140` — "PUBG: BATTLEGROUNDS"](../games/m-r/pubg-battlegrounds.md)
- [`GAME-0165` — Red Dead Redemption 2](../games/m-r/red-dead-redemption-2.md)
- [`GAME-0249` — Resident Evil 4 (2023 remake)](../games/m-r/resident-evil-4-2023.md)
- [`GAME-0127` — RimWorld](../games/m-r/rimworld.md)
- [`GAME-0177` — Rocket League](../games/m-r/rocket-league.md)
- [`GAME-0141` — Rust](../games/m-r/rust.md)
- [`GAME-0128` — Satisfactory](../games/s-z/satisfactory.md)
- [`GAME-0237` — "Serious Sam HD: The First Encounter"](../games/s-z/serious-sam-hd-the-first-encounter.md)
- [`GAME-0122` — shapez 2 - Factory](../games/s-z/shapez-2.md)
- [`GAME-0118` — SimCity 4 Deluxe Edition](../games/s-z/simcity-4-deluxe-edition.md)
- [`GAME-0157` — Split Fiction](../games/s-z/split-fiction.md)
- [`GAME-0170` — "S.T.A.L.K.E.R. 2: Heart of Chornobyl"](../games/s-z/stalker-2-heart-of-chornobyl.md)
- [`GAME-0230` — "STAR WARS Battlefront II (2017)"](../games/s-z/star-wars-battlefront-ii-2017.md)
- [`GAME-0213` — "STAR WARS Jedi: Fallen Order"](../games/s-z/star-wars-jedi-fallen-order.md)
- [`GAME-0225` — "STAR WARS: Squadrons"](../games/s-z/star-wars-squadrons.md)
- [`GAME-0172` — Street Fighter 6](../games/s-z/street-fighter-6.md)
- [`GAME-0178` — Subnautica](../games/s-z/subnautica.md)
- [`GAME-0094` — Superliminal](../games/s-z/superliminal.md)
- [`GAME-0136` — "Surviving Mars: Relaunched"](../games/s-z/surviving-mars.md)
- [`GAME-0187` — Team Fortress 2](../games/s-z/team-fortress-2.md)
- [`GAME-0153` — Terraria](../games/s-z/terraria.md)
- [`GAME-0004` — Tetris](../games/s-z/tetris.md)
- [`GAME-0164` — "The Binding of Isaac: Rebirth"](../games/s-z/the-binding-of-isaac-rebirth.md)
- [`GAME-0190` — "The Elder Scrolls V: Skyrim Special Edition"](../games/s-z/the-elder-scrolls-v-skyrim-special-edition.md)
- [`GAME-0261` — The Last of Us Part I](../games/s-z/the-last-of-us-part-i.md)
- [`GAME-0087` — The Longest Journey](../games/s-z/the-longest-journey.md)
- [`GAME-0158` — The Sims 4](../games/s-z/the-sims-4.md)
- [`GAME-0116` — The Stanley Parable: Ultra Deluxe](../games/s-z/the-stanley-parable-ultra-deluxe.md)
- [`GAME-0038` — The Swapper](../games/s-z/the-swapper.md)
- [`GAME-0205` — "The Witcher 3: Wild Hunt"](../games/s-z/the-witcher-3-wild-hunt.md)
- [`GAME-0133` — Timberborn](../games/s-z/timberborn.md)
- [`GAME-0030` — Tin Hearts](../games/s-z/tin-hearts.md)
- [`GAME-0253` — "Titanfall 2"](../games/s-z/titanfall-2.md)
- [`GAME-0174` — Tom Clancy’s Rainbow Six Siege](../games/s-z/tom-clancys-rainbow-six-siege.md)
- [`GAME-0250` — Tomb Raider (2013)](../games/s-z/tomb-raider-2013.md)
- [`GAME-0191` — "Total War: WARHAMMER III"](../games/s-z/total-war-warhammer-iii.md)
- [`GAME-0216` — Trackmania](../games/s-z/trackmania.md)
- [`GAME-0197` — Valheim](../games/s-z/valheim.md)
- [`GAME-0183` — Vampire Survivors](../games/s-z/vampire-survivors.md)
- [`GAME-0041` — Viewfinder](../games/s-z/viewfinder.md)
- [`GAME-0184` — War Thunder](../games/s-z/war-thunder.md)
- [`GAME-0168` — Warframe](../games/s-z/warframe.md)
- [`GAME-0134` — "Workers & Resources: Soviet Republic"](../games/s-z/workers-resources-soviet-republic.md)
- [`GAME-0026` — World of Goo](../games/s-z/world-of-goo.md)
- [`GAME-0211` — World of Tanks](../games/s-z/world-of-tanks.md)
- [`GAME-0221` — World of Warcraft](../games/s-z/world-of-warcraft.md)

## TIM-004

- Назва: Почергові ходи суперників
- Переглянуто: `2026-08-24`

### Операційне визначення

Двоє супротивних учасників ухвалюють рішення по черзі у фіксованому порядку; під час кожного ходу право рішення має лише один учасник, а завершена дія передає наступне рішення іншій стороні.

### Включає

Білі ходять першими, після чого білі й чорні чергуються у шахах.

### Виключає

Автоматичну відповідь системи; одночасне планування; усі ходи одного гравця; дії в реальному часі без окремих ходів.

### Ігри-носії

- [`GAME-0011` — Chess](../games/a-f/chess.md)

## TIM-005

- Назва: Фаза планування перед виконанням зафіксованих ворожих дій
- Переглянуто: `2026-08-27`

### Операційне визначення

Під час однієї фази планування гравець може в гнучкому порядку віддати обмежену кількість команд, потім завершує фазу й спостерігає виконання вже визначених ворожих і запланованих системних подій перед наступним плануванням.

### Включає

Фаза гравця Into the Breach перед фазами середовища й атак Vek; фаза розіграшу карт Fights in Tight Spaces перед упорядкованими підготовленими атаками та наступною рукою; фаза гравця Slay the Spire з гнучким використанням карт і зіль, після якої йдуть `End Turn`, ворожі наміри та наступна рука.

### Виключає

Одну команду гравця з негайним повним розв’язанням; почергові ходи, вибрані двома людьми; одночасне приховане планування.

### Ігри-носії

- [`GAME-0047` — Fights in Tight Spaces](../games/a-f/fights-in-tight-spaces.md)
- [`GAME-0123` — Inscryption](../games/g-l/inscryption.md)
- [`GAME-0014` — Into the Breach](../games/g-l/into-the-breach.md)
- [`GAME-0155` — Slay the Spire 2](../games/s-z/slay-the-spire-2.md)
- [`GAME-0120` — Slay the Spire](../games/s-z/slay-the-spire.md)
- [`GAME-0176` — XCOM 2](../games/s-z/xcom-2.md)

## TIM-006

- Назва: Редаговане проєктування перед скидним автоматичним запуском
- Переглянуто: `2026-08-24`

### Операційне визначення

Гравець без тиску часу редагує постійну конструкцію машини та будь-який заданий автором розклад команд, а потім запускає детерміноване багатоциклове виконання, у якому редагування конструкції недоступне, доки виконання не зупиниться, не зазнає помилки, не завершиться або не буде скинуте.

### Включає

Повторюваний цикл побудови, програмування, тестування й перегляду Opus Magnum; редагування маршруту та символів SpaceChem без тиску часу з подальшими зафіксованими циклічними тестами реактора; компонування конвеєрів Infinifactory без тиску часу з подальшою зафіксованою симуляцією фабрики, яку можна призупинити, зупинити й скинути.

### Виключає

Редагування, поки активна симуляція триває; одну вхідну дію з однією завершеною автоматичною відповіддю; обмежену тактичну фазу планування з подальшим ворожим розв’язанням і ще однією фазою планування в межах місії.

### Ігри-носії

- [`GAME-0042` — Infinifactory](../games/g-l/infinifactory.md)
- [`GAME-0022` — Opus Magnum](../games/m-r/opus-magnum.md)
- [`GAME-0032` — SpaceChem](../games/s-z/spacechem.md)

## TIM-007

- Назва: Завантажити попередній стан і створити інше продовження
- Переглянуто: `2026-08-24`

### Операційне визначення

Гра зберігає попередні стани світу, дозволяє відновити один із них і продовжити з новими діями; нове продовження не зобов’язане повторювати події, які сталися після початкового збереження.

### Включає

Перемотування Tin Hearts до моменту перед падінням солдатика, переміщення маршрутного блока й продовження іншим шляхом; перемотування Timelie до моменту перед захопленням, зміну команди з часовою позначкою й пошук замінного майбутнього; перемотування вже прожитих станів Braid і відновлення з іншим локальним рухом, де позначені винятки для сутностей є параметром; відновлення збереженого кількома хвилинами раніше автозбереження Pikmin 4 і розігрування інших призначень завдань; перемотування Viewfinder до моменту перед падінням або руйнівним розміщенням фотографії та продовження з іншою позою; відновлення ручного або автоматичного збереження Cyberpunk 2077 і вибір інших бойових дій, реплік або маршруту.

### Виключає

Перезапуск рівня з початкового стану; скасування одного дискретного ходу в головоломці без часового тиску; перегляд неінтерактивного повтору.

### Ігри-носії

- [`GAME-0257` — "Alien: Isolation"](../games/a-f/alien-isolation.md)
- [`GAME-0148` — Baldur’s Gate 3](../games/a-f/baldurs-gate-3.md)
- [`GAME-0256` — "BioShock™ Remastered"](../games/a-f/bioshock-remastered.md)
- [`GAME-0034` — Braid, Anniversary Edition](../games/a-f/braid.md)
- [`GAME-0146` — Cyberpunk 2077](../games/a-f/cyberpunk-2077.md)
- [`GAME-0259` — "Dead Space (2023 remake)"](../games/a-f/dead-space-2023.md)
- [`GAME-0231` — Fallout 4](../games/a-f/fallout-4.md)
- [`GAME-0260` — Metro Exodus](../games/m-r/metro-exodus.md)
- [`GAME-0035` — Pikmin 4](../games/m-r/pikmin-4.md)
- [`GAME-0258` — "Prey (2017)"](../games/m-r/prey-2017.md)
- [`GAME-0190` — "The Elder Scrolls V: Skyrim Special Edition"](../games/s-z/the-elder-scrolls-v-skyrim-special-edition.md)
- [`GAME-0261` — The Last of Us Part I](../games/s-z/the-last-of-us-part-i.md)
- [`GAME-0031` — Timelie](../games/s-z/timelie.md)
- [`GAME-0030` — Tin Hearts](../games/s-z/tin-hearts.md)
- [`GAME-0041` — Viewfinder](../games/s-z/viewfinder.md)

## TIM-008

- Назва: Редагована детермінована часова шкала з довільним доступом
- Переглянуто: `2026-08-24`

### Операційне визначення

Один курсор адресує минулі, поточні й майбутні моменти симуляції; гравець може оглядати детерміноване розв’язання та редагувати команди акторів у вибраний момент, не переходячи до окремої заблокованої фази виконання.

### Включає

Часову шкалу Timelie у вигляді медіаплеєра, де команди дівчини й кота можна вставляти або очищати після переходу назад чи вперед у часі.

### Виключає

Проєкт машини, який редагують лише до заблокованого запуску; втручання наживо в реальному часі з паузою; засоби керування повтором, які не можуть змінювати план.

### Ігри-носії

- [`GAME-0031` — Timelie](../games/s-z/timelie.md)

## TIM-009

- Назва: Проєктування транспортної схеми у власному темпі перед заблокованим одноразовим проходженням
- Переглянуто: `2026-08-24`

### Операційне визначення

Гравець без тиску часу створює одну повну просторову транспортну схему, а потім запускає одне детерміноване проходження, під час якого редагування схеми недоступне, доки множина транспортних засобів не досягне успіху, не зазнає невдачі, не зупиниться або не буде скинута.

### Включає

Прокладання колії Cosmic Express від входу до виходу, запуск потяга й зміна маршруту лише після завершення або скидання прогону; компонування залізничної схеми Railbound перед одночасним запуском усіх пронумерованих вагонів.

### Виключає

Редагування мережі, поки транспортні засоби продовжують рухатися; циклічна машина, що повторно виконує розклад інструкцій; одна дискретна команда, за якою йде одна негайна автоматична відповідь.

### Ігри-носії

- [`GAME-0037` — Cosmic Express](../games/a-f/cosmic-express.md)
- [`GAME-0056` — Railbound](../games/m-r/railbound.md)

## TIM-010

- Назва: Редагована тактична чернетка з прогнозом до підтвердження
- Переглянуто: `2026-08-23`

### Операційне визначення

Гравець гнучко задає послідовність обмеженого тактичного ходу, запускає точну автоматичну симуляцію наслідків, може відновити й змінити попередні кроки чернетки, а потім підтверджує один прийнятий результат до початку наступного ходу.

### Включає

Послідовність дія / Foresee / відкіт / підтвердження у Tactical Breach Wizards, після якої ворожий рух створює обставини наступного ходу.

### Виключає

Ворожі атаки, зафіксовані до планування й виконані після нього; довільне редагування кількох моментів змодельованого часу; проєктування машини перед заблокованим прогоном; звичайне дискретне скасування без фази прогнозу.

### Ігри-носії

- [`GAME-0048` — Tactical Breach Wizards](../games/s-z/tactical-breach-wizards.md)

## TIM-011

- Назва: Редагована мережа з повторюваним обмеженим оцінюванням руху
- Переглянуто: `2026-08-23`

### Операційне визначення

Гравець редагує постійну мережу без примусового строку завершення планування, а потім запускає обмежене автоматичне оцінювання транспортного руху. Після отримання результату або виникнення затору ту саму збережену конструкцію можна змінити й оцінити знову.

### Включає

Завершення мережі у Freeways, запуск прискореного змодельованого дня, подальше скасування змін або додавання доріг і повторний запуск оцінювання.

### Виключає

Безперервне редагування під час нескінченної симуляції з накопиченням рахунку; детермінована циклічна виробнича машина, заблокована на час випробування; один фіксований маршрут, який витрачається одним проходженням.

### Ігри-носії

- [`GAME-0052` — Freeways](../games/a-f/freeways.md)

## TIM-012

- Назва: Чергування автоматичного показу та відтворення гравцем
- Переглянуто: `2026-08-23`

### Операційне визначення

Гра чергує автоматичну фазу, що послідовно показує повну поточну ціль без вибору гравця, і фазу відповіді, під час якої система припиняє додавати сигнали та приймає впорядковане введення гравця; точне завершення повертає керування до автоматичного показу.

### Включає

Simon показує світлову послідовність, чекає на її відтворення, а потім показує збережену послідовність разом з одним новим сигналом.

### Виключає

Одночасне втручання в світ, який просувається в реальному часі; редаговану фазу планування перед заблокованим запуском; одну звичайну дискретну дію з негайним розв’язанням наслідків; обов’язкове обмеження часу на відповідь.

### Ігри-носії

- [`GAME-0067` — Simon](../games/s-z/simon.md)

## TIM-013

- Назва: Завершений прогрес планує оновлення світу наступного дня
- Переглянуто: `2026-08-23`

### Операційне визначення

Виконання поточного предиката поступу негайно записує завершення, але його постійний наслідок для стану світу реалізується лише після переходу через кінець дня й стає доступним наступного ігрового дня.

### Включає

Stardew Valley позначає `Boiler Room` завершеною після заповнення останнього пакета, показує нічний ремонт вагонеток Junimos і відкриває подорож вагонетками наступного дня.

### Виключає

Негайний автоматичний наслідок до наступного введення; крайній термін у реальному часі; фіксовану кількість тактичних ходів; косметичну зміну дня й ночі без нової можливості.

### Ігри-носії

- [`GAME-0089` — Stardew Valley](../games/s-z/stardew-valley.md)

## TIM-014

- Назва: Зміна в реальному часі обмежує надходження нових справ
- Переглянуто: `2026-08-23`

### Операційне визначення

Робочий годинник іде, поки гравець послідовно перевіряє справи; досягнення кінця зміни зазвичай не дає зайти наступній справі, але дозволяє завершити вже відкриту або обов’язковий сценарний мінімум.

### Включає

Зміну Papers, Please від 6:00 до 18:00, у якій поточного відвідувача можна обробити після затемнення годинника, а день подовжується, якщо обов’язкового сценарного відвідувача ще не прийнято.

### Виключає

Остаточний крайній термін спроби; симуляцію живого світу, яка змінює поточну справу; зовнішній таймер швидкісного проходження; фіксовану кількість дій.

### Ігри-носії

- [`GAME-0103` — Papers, Please](../games/m-r/papers-please.md)

## TIM-015

- Назва: Коротка бездіяльність завершує введення коду без штрафу світу
- Переглянуто: `2026-08-23`

### Операційне визначення

Після початку символічної послідовності надмірна бездіяльність у реальному часі очищає її незавершений буфер, але не змінює ціль у світі чи стан гравця, тому повну послідовність можна спробувати ввести знову.

### Включає

Надто довгу паузу між напрямками Святого Хреста в TUNIC із подальшим повторним початком коду дверей біля фонтану; «Допомога з послідовністю» усуває цю часову вимогу.

### Виключає

Кінцевий відлік спроби; світ, що продовжує змінюватися під час бездіяльності; фіксований бюджет ходів; твердження про точну тривалість, не підтверджене доказами.

### Ігри-носії

- [`GAME-0104` — TUNIC](../games/s-z/tunic.md)

## TIM-016

- Назва: Фіксований цикл світу в реальному часі завершується скиданням
- Переглянуто: `2026-08-23`

### Операційне визначення

Після початку повторюваної симуляції її світ продовжує змінюватися, а гравець — керувати ним, доки задана авторами кінцева подія фіксованої тривалості не завершить поточну ітерацію та не запустить наступну.

### Включає

Приблизно 22-хвилинний цикл сонячної системи Outer Wilds після встановлення зв’язку, що завершується надновою та новим пробудженням біля багаття.

### Виключає

Таймер, що лише оцінює результат; кінець робочої зміни, після якого поточна справа лишається відкритою; автоматичний прогін, під час якого введення заблоковано, але який можна скинути.

### Ігри-носії

- [`GAME-0105` — Outer Wilds](../games/m-r/outer-wilds.md)

## TIM-017

- Назва: Продовжувати серверний час за відсутності гравця
- Переглянуто: `2026-08-24`

### Операційне визначення

Спільний світ продовжує жити за серверним часом, поки гравець від’єднаний, тому витрати на утримання, руйнування, тіла від’єднаних гравців і ворожі дії можуть змінити його стан до повернення.

### Включає

Збереження світу та рейди за відсутності власника в межах одного циклу Rust.

### Виключає

Призупинений одиночний світ; рішення в реальному часі під час під’єднання; саме видалення стану під час планового скидання.

### Ігри-носії

- [`GAME-0141` — Rust](../games/m-r/rust.md)

## TIM-018

- Назва: Чергувати багатокомандні ходи цілих цивілізацій
- Переглянуто: `2026-08-27`

### Операційне визначення

Надавати кожній цивілізації послідовний хід, у межах якого вона виконує будь-яку кількість допустимих наказів одиницям, містам, економіці, дослідженню й дипломатії, а потім передає керування.

### Включає

Один хід Риму, за ним окремі ходи Греції, Єгипту й Німеччини.

### Виключає

Одночасне виконання в реальному часі; чергування після кожної одиничної дії; багатокористувацький режим.

### Ігри-носії

- [`GAME-0166` — Sid Meier’s Civilization VI](../games/s-z/sid-meiers-civilization-vi.md)
- [`GAME-0191` — "Total War: WARHAMMER III"](../games/s-z/total-war-warhammer-iii.md)

## TIM-019

- Назва: Чергувати активні ходи з вкладеними вікнами пріоритету
- Переглянуто: `2026-08-31`

### Операційне визначення

Гравці почергово отримують активний хід, але обидва можуть діяти у наданих вікнах пріоритету; послідовні відмови виконують об’єкт або просувають фазу.

### Включає

Визначену партію MTG Arena для двох гравців із діями в головній фазі, оголошеннями в бою й миттєвими відповідями під час ходу будь-якого гравця.

### Виключає

Чергування по одній дії; приховані накази; автономну ворожу фазу; реальний час.

### Ігри-носії

- [`GAME-0185` — "Magic: The Gathering Arena"](../games/m-r/magic-the-gathering-arena.md)

## TIM-020

- Назва: Чергувати фазові ходи із завершуваними вікнами ланцюга
- Переглянуто: `2026-09-01`

### Операційне визначення

Гравці по черзі мають активний хід із визначеними фазами, а допустима активація тимчасово передає право відповіді між сторонами, доки завершений ланцюг не розв’яжеться повністю у зворотному порядку й не поверне керування до поточної фази.

### Включає

Визначений двобій Tutorial у Master Duel.

### Виключає

Пріоритет MTG і розв’язання одного верхнього об’єкта; одночасні приховані накази; фазу планування перед автоматичним ходом ворога.

### Ігри-носії

- [`GAME-0206` — "Yu-Gi-Oh! Master Duel"](../games/s-z/yu-gi-oh-master-duel.md)
