from aiogram import Bot
from aiogram.types import BotCommand, BotCommandScopeDefault


async def set_commands(bot: Bot):
    commands = [
        BotCommand(
            command='start',
            description='Перезапуск 🚀'
        ),
        BotCommand(
            command='faq',
            description='Помощь ❓'
        )
    ]

    await bot.set_my_commands(commands, BotCommandScopeDefault())
