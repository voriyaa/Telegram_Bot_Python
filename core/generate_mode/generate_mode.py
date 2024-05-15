import sqlite3
from ..keyboard.reply import reply_keyboard


async def change_mode_to_text(message):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM YourTableName WHERE user_id=?", (message.from_user.id,))
    existing_user = cursor.fetchone()

    if existing_user:
        cursor.execute("UPDATE YourTableName SET generate_mode=? WHERE user_id=?", (1, message.from_user.id))
    else:
        cursor.execute("INSERT INTO YourTableName (user_id, generate_mode) VALUES (?, ?)", (message.from_user.id, 1))

    conn.commit()
    conn.close()
    await message.answer('Спроси мне о чем угодно и я отвечу тебе', reply_markup=reply_keyboard)


async def change_mode_to_image(message):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM YourTableName WHERE user_id=?", (message.from_user.id,))
    existing_user = cursor.fetchone()

    if existing_user:
        cursor.execute("UPDATE YourTableName SET generate_mode=? WHERE user_id=?", (2, message.from_user.id))
    else:
        cursor.execute("INSERT INTO YourTableName (user_id, generate_mode) VALUES (?, ?)", (message.from_user.id, 2))

    conn.commit()
    conn.close()
    await message.answer('Отправь мне запрос к картинке.', reply_markup=reply_keyboard)
