import google.generativeai as genai
import os
from dotenv import load_dotenv
from ..keyboard.reply import reply_keyboard

load_dotenv()


async def gpt_answer(message, bot):
    try:
        loading_message = await message.answer("📄 Мы отвечаем на Ваш вопрос, дождитесь окончания генерации.",
                                               reply_markup=reply_keyboard)
        genai.configure(api_key=os.getenv('API_KEY'))
        model = genai.GenerativeModel(model_name="gemini-pro")
        response = model.generate_content(message.text)
        await bot.delete_message(chat_id=loading_message.chat.id, message_id=loading_message.message_id)
        await message.answer(response.text, reply_markup=reply_keyboard)
    except Exception as e:
        await message.answer(f"An error occurred: {str(e)}")



