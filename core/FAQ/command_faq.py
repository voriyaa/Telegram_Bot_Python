from ..keyboard.reply import reply_keyboard


async def command_faq(message, bot):
    await message.answer("❓ Если у вас есть вопрос, вы можете написать с 10:00 до 22:00 c пнд по пт @tooolateee", reply_markup=reply_keyboard)