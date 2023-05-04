# Api

## Перечисления

Эти перечисления хранятся в независимых от языка [minecraft-data](https://github.com/PrismarineJS/minecraft-data)проект, и доступ к нему осуществляется через [node-minecraft-data](https://github.com/PrismarineJS/node-minecraft-data)
### minecraft-data
Данные доступны в [node-minecraft-data](https://github.com/PrismarineJS/node-minecraft-data) модуль

`require('minecraft-data')(bot.version)` дает вам доступ к нему.
### mcdata.blocks
блоки, проиндексированные по id

### mcdata.items
элементы, проиндексированные по id

### mcdata.materials

Ключом является материал. Значение - это объект, ключом которого является идентификатор элемента
инструмента, а значение - множитель эффективности.

### mcdata.recipes
рецепты, индексированные по id

### mcdata.instruments
инструменты, проиндексированные по id

### mcdata.biomes
биомы, индексированные по id

### mcdata.entities
сущности, индексированные по id