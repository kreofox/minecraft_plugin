from javacript import require
from javacript import on

mineflayer = require('mineflayer')
pathfinder = require('mineflayer-pathfinder')

bot = mineflayer.createBot({
    'host': '', # minecraft server ip
    'username': 'Bob',
    'version': '' #version Minecraft
})

bot.loadPlugin(pathfinder.pathfinder)

@On(bot, 'spawn')
def spawn(*args):
    mcData = require('minecraft-data')(bot.version)
    movements = pathfinder.Movements(bot, mcData)

    @On(bot, 'chat')
    def msgHandler(this, user, message, *args):
        if user != 'Bob':
            if 'сюда' in message:
                player = bot.plaers[user]
                target = player.entity

                bot.pathfinder.setMovements(movements)
                goal = GoalFollow(target, 1)
                bot.pathfinder.setGoal(goal, True)
