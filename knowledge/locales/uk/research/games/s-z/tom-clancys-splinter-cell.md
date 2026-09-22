# GAME-0349 — "Tom Clancy’s Splinter Cell"

Перевірений український дослідницький огляд. Стабільні ідентифікатори
та межі механік відповідають канонічному англійському запису.

- Статус аналізу: `перевірено`
- Дата перегляду: `2026-09-21`

## Механічний профіль

Sam керує власною помітністю: Stealth Meter показує освітлення, швидкість і поза змінюють шум, а світло, камера, патруль і непритомне тіло лишаються причинними об’єктами світу. Training Course навчає lock pick, допиту, keypad, retinal scanner, приховування тіла й тихого руху, а Police Station складає ці правила в одну місію до Wilkes і збереженого наступного checkpoint.

## Опис механіки

Stealth Meter показує, наскільки Sam освітлений, а швидкість і поза визначають шум та ризик виявлення. Тренування поєднує lock pick, допит, retinal scanner, знищення світла й приховування непритомного тіла; Police Station переносить ці правила в місію до van Wilkes. Це реконструкція за джерелами, не гра на Xbox.

## Межа аналізу

Перший північноамериканський англомовний роздрібний випуск Tom Clancy's Splinter Cell для оригінального Xbox, US-012, title ID 5553000C, 2002-11-17; новий профіль на Normal від першого звичайного керування у Training Course через повну Police Station до перезавантаженого першого checkpoint Defense Ministry. Фіксований маршрут: пройти калібрування й смугу перешкод; відкрити тренувальний замок; схопити trainee ззаду, допитати для коду й увести його; примусити іншого trainee пройти retinal scanner; вистрілити у світло перед camera; нелетально знешкодити guard і покласти непритомне тіло в тіні; тихо пройти chains та glass; завершити Training. У Police Station дістатися contact через rooftop і burning building; отримати обов’язкові computer/data facts; пройти balcony, zip line, lock-picked door і dead drop; увести 5929; знайти Madison і Blaustein; відкрити security surveillance; дістатися van Wilkes; прийняти завершення, зберегти перший Defense Ministry checkpoint, вийти й завантажити його. Включено analog speed, crouch, back-to-wall, climbing, mantle, zip line, wall/split jump, directed sight, occlusion, movement sound, light-dependent acquisition, Stealth Meter, Life, pistol/light shot, nonlethal rear neutralisation, interrogation, forced retinal cooperation, body carry/place, doors, computers, data, keypads, lock pick, camera, objectives, suspicion/combat, checkpoint save/load і mission handoff. Виключено thermal vision, SC-20K, sticky/distraction cameras, jammer, gas, explosives, lethal clearance, optional medkits/data, alarm maximisation, Defense Ministry після reload, later missions, DLC packs, multiplayer, інші платформи/видання, backward-compatible enhancements, remake, sequel, чити й моди.

## Статус безпосереднього проходження

Безпосередньої гри не проводили: диск, Xbox, контролер, профіль, checkpoint, executable, dump, емулятор, скриншот, відео й аудіо не використовували. Оригінальний англомовний Xbox-посібник встановлює керування, Stealth Meter, світло, шум, alarm, body handling, interrogation, forced cooperation, security fixtures і checkpoint rules; Xbox підтверджує продукт, а два незалежні письмові маршрути — Training та Police Station. Локальний контроль лише реконструює заявлені стани, не запускає програму й не вимірює точні пороги світла, шуму, шкоди чи колізій.

## Канонічний склад генів

- [`ACT-008`](../../genes/actions.md#act-008) — Безпосередньо пересувати керованого персонажа
- [`ACT-107`](../../genes/actions.md#act-107) — Дізнатися в розмові факт, потрібний для подальшої дії
- [`ACT-161`](../../genes/actions.md#act-161) — Прицілитися й атакувати досяжну ціль поточною зброєю
- [`ACT-202`](../../genes/actions.md#act-202) — Змінити положення або конфігурацію тіла персонажа
- [`ACT-341`](../../genes/actions.md#act-341) — Виконати контекстну взаємодію зі станом сутності світу
- [`ACT-344`](../../genes/actions.md#act-344) — Дослідити й повернути замок крихкою відмичкою
- [`ACT-491`](../../genes/actions.md#act-491) — Перенести й покласти непритомне тіло
- [`SYS-057`](../../genes/system-behaviours.md#sys-057) — Переслідування або відволікання автономного ворога за сприйняттям
- [`SYS-215`](../../genes/system-behaviours.md#sys-215) — Проводити безпосередньо керований бій у реальному часі
- [`SYS-369`](../../genes/system-behaviours.md#sys-369) — Після провалу відновлювати авторську контрольну точку
- [`SYS-373`](../../genes/system-behaviours.md#sys-373) — Перетворювати підозру на виявлення й бій
- [`SYS-578`](../../genes/system-behaviours.md#sys-578) — Змінювати єдиний запас здоров’я поточної спроби
- [`SYS-780`](../../genes/system-behaviours.md#sys-780) — Переносити стан завершеного авторського сегмента у керування наступника
- [`SYS-797`](../../genes/system-behaviours.md#sys-797) — Перетворювати місцеву освітленість на тиск ворожого сприйняття
- [`CON-077`](../../genes/constraints.md#con-077) — Напрямлене вороже сприйняття, обмежене перекриттями
- [`CON-282`](../../genes/constraints.md#con-282) — Основні сюжетні бої відкриваються в установленій черзі
- [`CON-285`](../../genes/constraints.md#con-285) — Дія зброєю потребує сумісного спорядження й поточного стану
- [`CON-330`](../../genes/constraints.md#con-330) — Важливі люди, транспорт і область місії мають лишатися неушкодженими
- [`CON-335`](../../genes/constraints.md#con-335) — Приховане знешкодження потребує ворога, який ще не виявив гравця
- [`INF-073`](../../genes/information.md#inf-073) — Панель швидкого доступу й стан активного спорядження видимі
- [`INF-075`](../../genes/information.md#inf-075) — Показники здоров’я, потреб, захисту й міцності видимі
- [`INF-115`](../../genes/information.md#inf-115) — Зір і просторовий звук відкривають лише частину стану суперника
- [`INF-125`](../../genes/information.md#inf-125) — Мапа показує досліджений маршрут і поточну ціль
- [`INF-316`](../../genes/information.md#inf-316) — Показувати поточну зорову освітленість особистим індикатором
- [`OBJ-155`](../../genes/objectives.md#obj-155) — Завершити один авторський сегмент виживання й зберегти керування в наступнику
- [`TIM-003`](../../genes/time.md#tim-003) — Давати команди, поки світ змінюється в реальному часі
- [`TIM-007`](../../genes/time.md#tim-007) — Завантажити попередній стан і створити інше продовження

## Перевірені комбінації

- Немає окремої перевіреної комбінації.
