## Классы

### vec3

См. [andrewrk/node-vec3](https://github.com/andrewrk/node-vec3)
Все точки в mineflayer поставляются как экземпляры этого класса.

* x - юг
* y - вверх
* z - запад
Функции и методы, требующие аргумента в виде точки, принимают экземпляры `Vec3`.
а также массив с 3 значениями и объект со свойствами `x`, `y` и `z`.
свойствами.

### mineflayer.Location

### Entity

Сущности представляют игроков, мобов и объекты. Они испускаются
во многих событиях, и вы можете получить доступ к собственной сущности с помощью `bot.entity`.
См. [prismarine-entity](https://github.com/PrismarineJS/prismarine-entity)

#### Данные скина игрока

Данные о скине хранятся в свойстве `skinData` объекта игрока, если оно присутствует.

```js
// player.skinData
{
  url: 'http://textures.minecraft.net/texture/...',
  model: 'slim' // or 'classic'
}
```

### Блок
См. [prismarine-block](https://github.com/PrismarineJS/prismarine-block)

Также `block.blockEntity` является дополнительным полем с данными сущности блока как `Object`.
```js
// sign.blockEntity
{
  x: -53,
  y: 88,
  z: 66,
  id: 'minecraft:sign', // 'Sign' in 1.10
  Text1: { toString: Function }, // ChatMessage object
  Text2: { toString: Function }, // ChatMessage object
  Text3: { toString: Function }, // ChatMessage object
  Text4: { toString: Function } // ChatMessage object
}
```

### Биом

См.[prismarine-biome](https://github.com/PrismarineJS/prismarine-biome)

### Item

См.[prismarine-item](https://github.com/PrismarineJS/prismarine-item)

### windows.Window (базовый класс)

См.[prismarine-windows](https://github.com/PrismarineJS/prismarine-windows)

#### window.deposit(itemType, metadata, count, nbt)
Эта функция возвращает `Promise`, аргументом которого является `void`, когда депонирование завершено.

 * `itemType` - числовой идентификатор предмета
 * `метаданные` - числовое значение. `null` означает соответствие чему-либо.
 * `count` - сколько предметов нужно депонировать. `null` - псевдоним 1.
 * `nbt` - совпадение с данными nbt. `null` - не сопоставлять с nbt.
#### window.withdraw(itemType, metadata, count, nbt)

Эта функция возвращает `Promise`, с `void` в качестве аргумента после завершения вывода. Выбрасывает ошибку, если у бота нет свободного места в инвентаре.

* `itemType` - числовой идентификатор предмета.
* `метаданные` - числовое значение. `null` означает, что соответствует чему-либо.
* `count` - сколько предметов нужно изъять. `null` - псевдоним 1.
* `nbt` - совпадение с данными nbt. `null` - не сопоставлять с nbt.

#### window.close()

### Рецепт

См.[prismarine-recipe](https://github.com/PrismarineJS/prismarine-recipe)

### mineflayer.Container

Расширяет windows.Window для сундуков, раздатчиков и т.д..
См. `bot.openContainer(chestBlock или minecartchestEntity)`.

### mineflayer.Furnace

Расширяет windows.Window для печей, плавильных печей и т.д....
См. `bot.openFurnace(furnaceBlock)`.

#### furnace "update"

Срабатывает при обновлении `furnace.fuel` и/или `furnace.progress`.

#### furnace.takeInput()

Эта функция возвращает `Promise`, аргументом которого является `item`.


#### furnace.takeFuel()

Эта функция возвращает `обещание` с `элементом` в качестве аргумента после завершения.


#### furnace.takeOutput()

Эта функция возвращает `обещание` с `элементом` в качестве аргумента после завершения.


#### furnace.putInput(itemType, metadata, count)

Эта функция возвращает `Promise` с `void` в качестве аргумента после завершения.

#### furnace.putFuel(itemType, metadata, count)

Эта функция возвращает `Promise`, аргументом которой является `void`.

#### furnace.inputItem()

Возвращает экземпляр `Item`, который является входным.

#### furnace.fuelItem()

Возвращает экземпляр `Item`, который является топливом.

#### furnace.outputItem()

Возвращает экземпляр `Item`, который является выходом.

#### печь.топливо

Сколько топлива осталось между 0 и 1.

#### furnace.progress

Сколько приготовлено на входе между 0 и 1.

### mineflayer.EnchantmentTable

Расширяет windows.Window для таблиц зачарований.
См. `bot.openEnchantmentTable(enchantmentTableBlock)`.

#### enchantmentTable "ready"

Срабатывает, когда `enchantmentTable.enchantments` полностью заполнена и вы
можно сделать выбор, вызвав `enchantmentTable.enchant(choice)`.

#### enchantmentTable.targetItem()

Получает целевой элемент. Это как входной, так и выходной элемент
таблицы приворотов.

#### enchantmentTable.xpseed

16-битный xpseed, отправленный сервером.

#### enchantmentTable.enchantments

Массив длины 3, который представляет собой 3 зачарования на выбор.
`level` может быть `-1`, если сервер еще не отправил данные.

Выглядит как:
```js
[
  {
    level: 3
  },
  {
    level: 4
  },
  {
    level: 9
  }
]
```
#### enchantmentTable.enchant(choice)

Эта функция возвращает `Promise` с `item` в качестве аргумента, если предмет был зачарован.

 * `choice` - [0-2], индекс зачарования, которое вы хотите выбрать.

#### enchantmentTable.takeTargetItem()

Эта функция возвращает `Promise`, аргументом которого является `item`.


#### enchantmentTable.putTargetItem(item)

Эта функция возвращает `Promise` с `void` в качестве аргумента после завершения.


#### enchantmentTable.putLapis(item)

Эта функция возвращает `Promise`, аргументом которого является `void`.


### mineflayer.anvil

Расширяет windows.Window для наковален.
См. `bot.openAnvil(anvilBlock)`.

#### anvil.combine(itemOne, itemTwo[, name])

Эта функция возвращает `Promise`, аргументом которой является `void`.


#### anvil.combine(item[, name])

Эта функция возвращает `Promise`, аргументом которого является `void`.


#### житель деревни "готов"

Срабатывает, когда загружается `villager.trades`.

#### villager.trades

Массив сделок.

Выглядит как:
```js
[
  {
    firstInput: Item,
    output: Item,
    hasSecondItem: false,
    secondaryInput: null,
    disabled: false,
    tooluses: 0,
    maxTradeuses: 7
  },
  {
    firstInput: Item,
    output: Item,
    hasSecondItem: false,
    secondaryInput: null,
    disabled: false,
    tooluses: 0,
    maxTradeuses: 7
  },
  {
    firstInput: Item,
    output: Item,
    hasSecondItem: true,
    secondaryInput: Item,
    disabled: false,
    tooluses: 0,
    maxTradeuses: 7
  }
]
```

#### villager.trade(tradeIndex, [times])
То же самое, что [bot.trade(villagerInstance, tradeIndex, [times])](#bottradevillagerinstance-tradeindex-times)

### mineflayer.ScoreBoard

#### ScoreBoard.name

Имя табло.

#### ScoreBoard.title

Заголовок табло (не всегда равен названию).

#### ScoreBoard.itemsMap

Объект, в котором содержатся все элементы табло

```js
{
  wvffle: { name: 'wvffle', value: 3 },
  dzikoysk: { name: 'dzikoysk', value: 6 }
}
```
#### ScoreBoard.items

Массив, содержащий все отсортированные элементы табло.
```js
[
  { name: 'dzikoysk', value: 6 },
  { name: 'wvffle', value: 3 }
]
```
### mineflayer.Team

#### Team.name

Название команды

#### Team.friendlyFire

#### Team.nameTagVisibility

Одно из `всегда`, `скрыть для других команд`, `скрыть для собственной команды`.

#### Team.collisionRule

Одно из `always`, `pushOtherTeams`, `pushOwnTeam`.

#### Team.color

Цвет (или форматирование) названия команды, например, `темно-зеленый`, `красный`, `подчеркнутый`.

#### Team.prefix

Компонент чата, содержащий префикс команды

#### Team.suffix

Компонент чата, содержащий суффикс команды

#### Team.members

Массив членов команды. Имена пользователей для игроков и UUID для других сущностей.

### mineflayer.BossBar

#### BossBar.title

Заголовок панели босса, экземпляр ChatMessage

#### BossBar.health

Процент здоровья босса, от `0` до `1`

#### BossBar.dividers

Количество разделителей панели боссов, одно из `0`, `6`, `10`, `12`, `20`.

#### BossBar.entityUUID

uuid объекта босс-бара

#### BossBar.shouldDarkenSky

Определяет, нужно ли затемнять небо.

#### BossBar.isDragonBar

Определяет, является ли панель босса панелью дракона.

#### BossBar.createFog

Определяет, создает ли босс-бар туман.

#### BossBar.color

Определяет, какого цвета будет босс-бар, один из `розового`, `синего`, `красного`, `зеленого`, `желтого`, `пурпурного`, `белого`.

### mineflayer.Particle

#### Particle.id

Идентификатор частицы, как определено в  [protocol](https://wiki.vg/Protocol#Particle)
#### Particle.name

Имя частицы, как определено в [protocol](https://wiki.vg/Protocol#Particle)

#### Particle.position

Vec3 экземпляр места, где была создана частица

#### Particle.offset

Vec3 экземпляр смещения частицы

#### Particle.longDistanceRender

Определяет, следует ли принудительно рендерить частицу, несмотря на настройки частиц клиента, и увеличивает максимальное расстояние просмотра с 256 до 65536.

#### Particle.count

Количество созданных частиц

#### Particle.movementSpeed

Скорость движения частицы в случайном направлении