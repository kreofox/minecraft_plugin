const mineflayer = require('mineflayer');

const bot = mineflayer.createBot({
    host: 'localhost',
    port: 25565,
    username: 'BotName'
})

bot.on('chat', (username, message) =>{
    if (username === bot.username) return;

    bot.chat(message);
})

bot.on('spawn', () => {
    bot.chat('Hello, I`m bot Minecraft!')
})