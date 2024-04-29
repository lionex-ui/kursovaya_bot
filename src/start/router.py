from aiogram import Router, types, F
from aiogram.filters import CommandStart

from src.start import texts

router = Router()


@router.message(CommandStart())
async def start_by_message(msg: types.Message):
    await msg.answer(
        text=texts.Start.text,
        reply_markup=texts.Start.builder.as_markup()
    )


@router.callback_query(F.data == "start")
async def start_by_callback(callback: types.CallbackQuery):
    await callback.answer()

    await callback.message.answer(
        text=texts.Start.text,
        reply_markup=texts.Start.builder.as_markup()
    )
