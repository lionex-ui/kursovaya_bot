from aiogram import Router, types, F

from src.data_get import texts

from src.data_get.handlers import child
from src.data_get.handlers import group
from src.data_get.handlers import educator


router = Router()
router.include_routers(child.router, educator.router, group.router)


@router.callback_query(F.data == "data_get")
async def data_get(callback: types.CallbackQuery):
    await callback.answer()

    await callback.message.answer(
        text=texts.Main.text,
        reply_markup=texts.Main.builder.as_markup()
    )
