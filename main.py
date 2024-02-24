from aiogram import Bot, Dispatcher
from config import BOT_TOKEN
import asyncio
import logging

from handlers.command_handler import command_router


async def main():

    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()
    dp.include_router(command_router)
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Bot stopped!')

