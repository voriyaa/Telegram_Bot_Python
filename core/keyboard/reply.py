from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, KeyboardButtonPollType

reply_keyboard = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(text='📑 Генерация текста'),
        KeyboardButton(text='🖼 Генерация картинок'),
    ]
], resize_keyboard=True, one_time_keyboard=True,  selective=True)