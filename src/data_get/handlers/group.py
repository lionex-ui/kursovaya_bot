from aiogram import Router, types, F

from src.data_get import texts
from src.data_get.database import *


router = Router()


@router.callback_query(F.data == "data_get_group")
async def data_get_group(callback: types.CallbackQuery):
    await callback.answer()

    await callback.message.answer(
        text=texts.Group.text,
        reply_markup=texts.Group.builder.as_markup()
    )


@router.callback_query(F.data.startswith("data_get_group_all"))
async def data_get_group_all(callback: types.CallbackQuery, session: AsyncSession):
    callback_data = callback.data.split("||")
    current_page = int(callback_data[1] if len(callback_data) >= 2 else 1)
    data = await get_groups(session)

    if len(data) < current_page:
        return await callback.answer(text="Це остання сторінка", show_alert=False)
    elif current_page < 1:
        return await callback.answer(text="Це перша сторінка", show_alert=False)

    await callback.answer()

    group_data = data[current_page - 1]

    if len(callback_data) >= 2:
        await callback.message.edit_text(
            text=texts.Group.All.text.format(
                group_id=group_data[0],
                group_name=group_data[1],
                educator_name=group_data[2],
                children_amount=group_data[3],
                current_page=current_page,
                all_pages=len(data)
            ),
            reply_markup=await texts.Group.All.get_buttons(current_page)
        )
    else:
        await callback.message.answer(
            text=texts.Group.All.text.format(
                group_id=group_data[0],
                group_name=group_data[1],
                educator_name=group_data[2],
                children_amount=group_data[3],
                current_page=current_page,
                all_pages=len(data)
            ),
            reply_markup=await texts.Group.All.get_buttons(current_page)
        )
