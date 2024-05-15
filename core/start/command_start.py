from Telegram_Bot_Python.message_config.message import StartMessage
from ..keyboard.reply import reply_keyboard
from ..utils.commands import set_commands
import sqlite3


async def get_start(message, bot):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    try:
        cursor.execute("INSERT INTO YourTableName (user_id, generate_mode) VALUES (?, ?) "
                       "ON CONFLICT(user_id) DO NOTHING", (message.from_user.id, 1))
        conn.commit()
    except sqlite3.IntegrityError:
        pass

    conn.close()
    await set_commands(bot)
    await message.answer(StartMessage.WELCOME_MESSAGE, reply_markup=reply_keyboard)