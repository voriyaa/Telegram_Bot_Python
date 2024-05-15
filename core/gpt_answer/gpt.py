import google.generativeai as genai
import os
import sqlite3
from dotenv import load_dotenv
from ..keyboard.reply import reply_keyboard

load_dotenv()


async def gpt_answer(message, bot):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    cursor.execute("SELECT generate_mode, history FROM YourTableName WHERE user_id=?", (message.from_user.id,))
    user_data = cursor.fetchone()
    generate_mode, history = user_data
    history = ('' if history is None else history)
    if generate_mode == 1:
        try:
            loading_message = await message.answer("📄 Мы отвечаем на Ваш вопрос, дождитесь окончания генерации.",
                                                   reply_markup=reply_keyboard)
            genai.configure(api_key=os.getenv('API_KEY'))
            model = genai.GenerativeModel(model_name="gemini-pro")
            history += f"User: {message.text}\n"
            response = model.generate_content(
                history + 'Это диалог между тобой и пользователем телеграм бота'
                          'в формате его сообщение через раз и твои через раз.'
                          'Тебе нужно продолжить диалог и знай что в диалоге самое'
                          'важное сообщение это последнее, т.е. сначала посмотри и '
                          'запомни весь диалог и потом ответь на его последнее '
                          'сообщение.'
                          'Кстати если что это все один человек. Так что можешь'
                          'Хранить его данные в одном месте.'
                          'Кстати не надо писать тебе всякие User: и Gemini:'
                          'это делаю я(телеграм бот) сам'
            )
            await bot.delete_message(chat_id=loading_message.chat.id, message_id=loading_message.message_id)
            history += f'Gemini: {response.text}\n'
            await message.answer(response.text, reply_markup=reply_keyboard)

            cursor.execute("UPDATE YourTableName SET history=? WHERE user_id=?", (history, message.from_user.id))
            conn.commit()
        except Exception as e:
            await message.answer(f"An error occurred: {str(e)}")
    else:
        await message.answer("США временно запретили мне генерировать изображения, но скоро все заработает!")
