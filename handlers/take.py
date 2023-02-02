from loader import dp 
from aiogram.types import Message
import game 
import random


@dp.message_handler()
async def mes_help(message: Message):
    if game.new_game:
        for duel in game.total:
            if message.from_user.id == duel[0]:
                count = message.text
                name = message.from_user.first_name
                if count.isdigit() and 0 < int(count) <29:
                    duel[2] -= int(count)
                    await check_win(message, 'Ты', duel)    
                    if game.new_game:
                        await message.answer(f'{duel[1]} взял {count} конфет и на столе осталось {duel[2]}\n Теперь ход бота...')
        
                    bot_take = random.randint(1,28) if duel[2] >28 else duel[2]
                    duel[2] -= bot_take

                    await check_win(message, 'Бот', duel)
                    if game.new_game:
                        await message.answer(f'Бот взял {bot_take} конфет и на столе осталось {duel[2]}\n Теперь твой ход...')

            else:
                await message.answer(f'Введите число от 1 до 28')



async def check_win(message: Message, win: str, total: list):
    if total[2] <= 0:
        await message.answer(f'{win} Победил!')
        game.new_game = False
        game.total.remove(total)


