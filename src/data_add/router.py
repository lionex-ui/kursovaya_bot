from aiogram import Router, types, F

from src.data_add import texts

import src.data_add.handlers.child as child
import src.data_add.handlers.group as group
import src.data_add.handlers.educator as educator


router = Router()
router.include_routers(child.router, educator.router, group.router)


@router.callback_query(F.data == "data_add")
async def data_add(callback: types.CallbackQuery):
    await callback.answer()

    await callback.message.answer(
        text=texts.Main.text,
        reply_markup=texts.Main.builder.as_markup()
    )
