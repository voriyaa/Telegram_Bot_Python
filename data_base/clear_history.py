import sqlite3


async def clear_history(message):
    try:
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()

        cursor.execute("UPDATE YourTableName SET history=? WHERE user_id=?", (None, message.from_user.id))

        conn.commit()
        conn.close()

        await message.answer("История успешно очищена.")
    except Exception as e:
        await message.answer(f"Произошла ошибка при очистке истории: {str(e)}")
