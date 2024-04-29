import sys
import logging

import asyncio

from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage

from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

from middleware.db import DbSessionMiddleware

from config import DB_HOST, DB_PORT, DB_USER, DB_PASS, DB_NAME, TOKEN

import start.router as start
import data_add.router as data_add
import data_get.router as data_get
import data_edit.router as data_edit
import data_delete.router as data_delete


async def main():
    database_url = f"postgresql+asyncpg://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    engine = create_async_engine(database_url)
    async_session_maker = async_sessionmaker(engine, expire_on_commit=False)

    bot = Bot(token=TOKEN)
    dp = Dispatcher(bot=bot, storage=MemoryStorage())

    dp.update.middleware(DbSessionMiddleware(session_pool=async_session_maker))

    dp.include_routers(start.router, data_add.router, data_delete.router, data_edit.router, data_get.router)

    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
