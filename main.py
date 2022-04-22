import os
os.system('pip install -r requirements.txt')
import string
import random
from typing import Any
from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
from keep_alive import keep_alive

token = ('bot_token')
dp = Dispatcher()

characters = list(string.ascii_letters + string.digits + '!@#$%^&*()')

@dp.message(commands={"start"})
async def command_start_handler(message: Message) -> None:
    await message.answer(f'Привет, <b>{message.from_user.full_name}!</b>\nЯ могу генерировать пароли\nОтправь мне желаемую длину пароля')


@dp.message()
async def echo_handler(message: types.Message) -> Any:
    if message.text.isnumeric():
        length = int(message.text)
        if length > 1000:
            await message.answer('Maximum password length - 1000 characters')
            return
        await message.answer(generate_password(length))
        
def generate_password(length: int):
    password = []
    for i in range(length):
        password.append(random.choice(characters))
    random.shuffle(password)
    return ''.join(password)

def main() -> None:
    bot = Bot(token, parse_mode='HTML')
    dp.run_polling(bot)


if __name__ == '__main__':
    keep_alive()
    main()
