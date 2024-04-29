from aiogram import Router, types, F

from src.data_edit import texts

import src.data_edit.handlers.child as child
import src.data_edit.handlers.group as group
import src.data_edit.handlers.educator as educator


router = Router()
router.include_routers(child.router, educator.router, group.router)


@router.callback_query(F.data == "data_edit")
async def data_edit(callback: types.CallbackQuery):
    await callback.answer()

    await callback.message.answer(
        text=texts.Main.text,
        reply_markup=texts.Main.builder.as_markup()
    )
