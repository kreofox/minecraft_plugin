## Бот

### mineflayer.createBot(options)

Создает и возвращает экземпляр класса bot.
`options` - это объект, содержащий необязательные свойства :
* имя пользователя : по умолчанию 'Player'
* порт : по умолчанию 25565
* пароль : может быть опущен (если токены также опущены, то бот пытается подключиться в автономном режиме)
* host : по умолчанию localhost
* version : по умолчанию автоматически угадывает версию сервера. Пример значения: "1.12.2"
* auth : по умолчанию 'mojang', также может быть 'microsoft'.
* clientToken : генерируется, если указан пароль.
* accessToken : генерируется, если указан пароль
* logErrors : true по умолчанию, перехватывать ошибки и записывать их в журнал
* hideErrors : по умолчанию true, не записывать ошибки в журнал (даже если logErrors равен true)
* keepAlive : посылать пакеты для поддержания жизни: по умолчанию true
* checkTimeoutInterval : по умолчанию `30*1000` (30s), проверяем, получен ли keepalive в этот период, отключаем в противном случае.
* loadInternalPlugins : по умолчанию true
* storageBuilder : необязательная функция, принимает в качестве аргументов version и worldName и возвращает экземпляр чего-то с тем же API, что и prismarine-provider-anvil. Будет использоваться для сохранения мира.
* client : экземпляр node-minecraft-protocol, если не указан, mineflayer создает свой собственный клиент. Это может быть использовано для использования mineflayer через прокси многих клиентов или ванильного клиента и клиента mineflayer.
* brand : название бренда для используемого клиента. По умолчанию - vanilla. Может использоваться для имитации пользовательских клиентов для серверов, которые этого требуют.
* plugins : объект : по умолчанию {}
- pluginName : false: не загружать внутренний плагин с заданным именем, т.е. `pluginName`.
- pluginName : true : загрузить внутренний плагин с заданным именем, т.е. `pluginName`, даже если loadInternalplugins установлен в false
- pluginName : функция инжекта внешнего плагина: загружает внешний плагин, переопределяя внутренний плагин с заданным именем, т.е. `pluginName`.
* physicsEnabled : true по умолчанию, должна ли физика влиять на бота? может быть изменена через bot.physicsEnabled
* [chat](#bot.settings.chat)
 * [colorsEnabled](#bot.settings.colorsEnabled)
 * [viewDistance](#bot.settings.viewDistance)
 * [difficulty](#bot.settings.difficulty)
 * [skinParts](#bot.settings.skinParts)
 * [enableTextFiltering](#bot.settings.enableTextFiltering)
 * [enableServerListing](#bot.settings.enableServerListing)
 * chatLengthLimit : максимальное количество символов, которое может быть отправлено в одном сообщении. Если это значение не задано, оно будет равно 100 в версии < 1.11 и 256 в версии >= 1.11.
* defaultChatPatterns: по умолчанию имеет значение true, установите значение false, чтобы не добавлять шаблоны, такие как чат и шепот.
### Свойства

#### bot.registry

Экземпляр minecraft-данных, используемых ботом. Передайте его конструкторам, которые ожидают получить экземпляр minecraft-data, например, prismarine-block.

#### bot.world

Синхронное представление мира. См. документацию по адресу http://github.com/PrismarineJS/prismarine-world.

##### world "blockUpdate" (oldBlock, newBlock)

Срабатывает при обновлении блока. Оба `старыйБлок` и `новыйБлок` предоставляются для
сравнения.
При обычном обновлении блока `oldBlock` может быть `null`.

##### world "blockUpdate:(x, y, z)" (oldBlock, newBlock)

Срабатывает для определенной точки. Оба `старыйБлок` и `новыйБлок` предоставляются для
сравнения. Все слушатели получают null для `oldBlock` и `newBlock` и автоматически удаляются при выгрузке мира.
`oldBlock` может быть `null` при обычном обновлении блока.


#### bot.entity

Ваша собственная сущность. См. `Entity`.

#### bot.entities

Все близлежащие сущности. Этот объект представляет собой карту entityId к entity.

#### bot.username

Используйте этот объект, чтобы узнать свое имя.

#### bot.spawnPoint

Координаты основной точки спавна, на которую указывают все компасы.

#### bot.heldItem

Предмет в руке бота, представленный как [prismarine-item](https://github.com/PrismarineJS/prismarine-item) экземпляр, заданный с произвольными метаданными, nbtdata и т.д.

#### bot.usingHeldItem

Использует ли бот предмет, который держит в руках, например, ест ли он еду или использует щит.

#### bot.game.levelType

#### bot.game.dimension

#### bot.game.difficulty

#### bot.game.gameMode

#### bot.game.hardcore

#### bot.game.maxPlayers

#### bot.game.serverBrand

#### bot.game.minY

минимальный y мира

#### bot.game.height

высота мира

#### bot.physicsEnabled

Включить физику, по умолчанию true.

#### bot.player

Объект игрока бота
```js
{
  username: 'player',
  displayName: { toString: Function }, // ChatMessage object.
  gamemode: 0,
  ping: 28,
  entity: entity // null if you are too far away
}
```
Пинг игрока начинается с 0, вам может потребоваться немного подождать, пока сервер отправит свой реальный пинг.

#### bot.players

Карта имени пользователя для людей, играющих в игру.

#### bot.tablist

Объект tablist бота имеет два ключа, `header` и `footer`.
```js
{
  header: { toString: Function }, // ChatMessage object.
  footer: { toString: Function } // ChatMessage object.
}
```
#### bot.isRaining

#### bot.rainState

Число, указывающее на текущий уровень дождя. Когда дождя нет, это
будет равно 0. Когда начнется дождь, это значение будет увеличиваться
постепенно увеличиваясь до 1. Когда дождь прекращается, это значение постепенно уменьшается до 0.

Каждый раз, когда `bot.rainState` изменяется, испускается событие "weatherUpdate".

#### bot.thunderState

Число, указывающее на текущий уровень грозы. Когда грозы нет, это число
будет равно 0. Когда начнется гроза, это значение будет увеличиваться
постепенно до 1. Когда гроза прекращается, это значение постепенно уменьшается до 0.

Каждый раз, когда `bot.thunderState` изменяется, происходит событие "weatherUpdate".

Это то же самое, что и `bot.rainState`, но для грозы.
Для грозы изменяются и `bot.rainState`, и `bot.thunderState`.

#### bot.chatPatterns

Это массив объектов паттернов следующего формата:
( /regex/, "chattype", "description")
 * /regex/ - шаблон регулярного выражения, который должен иметь как минимум две группы захвата
 * 'chattype' - тип чата, которому соответствует шаблон, например, "chat" или "whisper", но может быть любым.
 * 'description' - описание того, для чего предназначен шаблон, необязательно.

#### bot.settings.chat

Выборы:

 * `enabled` (по умолчанию)
 * ``команды только``
 * ``отключено``

#### bot.settings.colorsEnabled

По умолчанию true - получать или нет цветовые коды в чатах от сервера.

#### bot.settings.viewDistance

Может быть строкой, указанной ниже, или положительным числом.
Варианты:
 * `far` (по умолчанию)
 * `нормальное`
 * `короткий`
 * `маленький`

#### bot.settings.difficulty

То же, что и в server.properties.

#### bot.settings.skinParts

Эти булевы настройки контролируют, должны ли быть видны дополнительные детали скина на скине собственного игрока.

##### bot.settings.skinParts.showCape - булево

Если у вас есть плащ, вы можете отключить его, установив это значение в false.

##### bot.settings.skinParts.showJacket - boolean

##### bot.settings.skinParts.showLeftSleeve - булево

##### bot.settings.skinParts.showRightSleeve - булево

##### bot.settings.skinParts.showLeftPants - булево

##### bot.settings.skinParts.showRightPants - булево

##### bot.settings.skinParts.showHat - булево

#### bot.settings.enableTextFiltering - boolean
Не используется, по умолчанию имеет значение false в клиенте Notchian (Vanilla).
#### bot.settings.enableServerListing - boolean
Этот параметр отправляется на сервер, чтобы определить, должен ли игрок отображаться в списках серверов.
#### bot.experience.level

#### bot.experience.points

Общее количество очков опыта.

#### bot.experience.progress

От 0 до 1 - количество для перехода на следующий уровень.

#### bot.health

Число в диапазоне [0, 20], представляющее количество полусердец.

#### bot.food

Число в диапазоне [0, 20], представляющее собой количество полутуловищ-полуног.

#### bot.foodSaturation

Насыщение пищи действует как "перезарядка" пищи. Стоимость еды не будет уменьшаться
пока насыщенность больше нуля. Игроки, вошедшие в игру, автоматически получают
насыщение 5,0. Потребление пищи увеличивает насыщенность, а также запас еды.

#### bot.oxygenLevel

Число в диапазоне [0, 20], представляющее количество иконок воды, известное как уровень кислорода.

#### bot.physics

Отредактируйте эти числа, чтобы настроить гравитацию, скорость прыжка, конечную скорость и т.д.
Делайте это на свой страх и риск.

#### bot.simpleClick.leftMouse (слот)

абстракция над `bot.clickWindow(slot, 0, 0)`.

#### bot.simpleClick.rightMouse (slot)

абстракция над `bot.clickWindow(slot, 1, 0)`

#### bot.time.doDaylightCycle

Истинно или ложно значение геймерского правила doDaylightCycle.

#### bot.time.bigTime

Общее количество тиков с 0-го дня.

Это значение имеет тип BigInt и является точным даже при очень больших значениях. (более 2^51 - 1 тиков).

#### bot.time.time

Общее количество тиков с 0-го дня.

Поскольку предел числа в Javascript составляет 2^51 - 1, bot.time.time становится неточным выше этого предела и рекомендуется использовать bot.time.bigTime.
Однако в реальности вам, скорее всего, никогда не понадобится использовать bot.time.bigTime, поскольку он достигнет 2^51 - 1 тиков естественным образом только через ~14280821 реальных лет.

#### bot.time.timeOfDay

Время суток, в тиках.

Время основано на тиках, где 20 тиков происходят каждую секунду. В сутках 24000
тиков в сутках, поэтому дни в Minecraft длятся ровно 20 минут.

Время суток основано на временной метке, умноженной на 24000. 0 - это восход солнца, 6000
полдень, 12000 - закат, а 18000 - полночь.

#### bot.time.day

День мира.

#### bot.time.isDay

Является ли сегодня днем или нет.

Основывается на том, находится ли текущее время суток между 13000 и 23000 тиками.

#### bot.time.moonPhase

Фаза луны.

0-7, где 0 - полнолуние.

#### bot.time.bigAge

Возраст мира, в тиках.

Это значение имеет тип BigInt и является точным даже при очень больших значениях. (более 2^51 - 1 тиков).

#### bot.time.age

Возраст мира, в тиках.

Поскольку предел числа в Javascript равен 2^51 - 1, bot.time.age становится неточным выше этого предела и рекомендуется использовать bot.time.bigAge.
Однако в реальности вам, скорее всего, никогда не понадобится использовать bot.time.bigAge, поскольку он достигнет 2^51 - 1 тиков естественным образом только через ~14280821 реальных лет.

#### bot.quickBarSlot

Какой слот быстрого бара выбран (0 - 8).

#### bot.inventory

A [`Window`](https://github.com/PrismarineJS/prismarine-windows#windowswindow-base-class) 

экземпляр, представляющий ваш инвентарь.

#### bot.targetDigBlock

Блок, который вы сейчас копаете, или `null`.

#### bot.isSleeping

Булево число, указывающее, спите вы или нет.

#### bot.scoreboards

Все табло, известные боту, в объекте имя табло -> табло.
* `belowName` - scoreboard placed in belowName
 * `sidebar` - scoreboard placed in sidebar
 * `list` - scoreboard placed in list
 * `0-18` - slots defined in [protocol](https://wiki.vg/Protocol#Display_Scoreboard) 

#### bot.teams

Все команды, известные боту

#### bot.teamMap

Сопоставление члена команды с командой. Использует имена пользователей для игроков и UUID для сущностей.

#### bot.controlState

Объект, ключами которого являются основные состояния управления: ['вперед', 'назад', 'влево', 'вправо', 'прыжок', 'спринт', 'красться'].

Установка значений для этого объекта вызывает [bot.setControlState](#botsetcontrolstatecontrol-state).