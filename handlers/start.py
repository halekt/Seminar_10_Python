from loader import dp 
from aiogram.types import Message
import game 

@dp.message_handler(commands=['start'])
async def mes_start(message: Message):
    await dp.bot.send_message(message.from_user.id, f'К чату присоединился {message.from_user.full_name}')
    await message.answer(f'Привет, {message.from_user.full_name} Мы будем играть в конфеты. Бери от 1 до 28')
    print(message)

    for duel in game.total:
        if message.from_user.id == duel[0]:
            break

    else:
        game.new_game = True
        my_game = [message.from_user.id, message.from_user.first_name, 150]
        game.total.append(my_game)



