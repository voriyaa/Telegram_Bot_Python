from Telegram_Bot_Python.message_config.message import StartMessage
from ..keyboard.reply import reply_keyboard


async def get_start(message):
    await message.answer(StartMessage.WELCOME_MESSAGE, reply_markup=reply_keyboard)