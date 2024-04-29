from aiogram import Router, types, F

from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State

from src.data_get import texts
from src.data_get.database import *


router = Router()


class GetEducatorById(StatesGroup):
    educator_id = State()


@router.callback_query(F.data == "data_get_educator")
async def data_get_educator(callback: types.CallbackQuery):
    await callback.answer()

    await callback.message.answer(
        text=texts.Educator.text,
        reply_markup=texts.Educator.builder.as_markup()
    )


@router.callback_query(F.data.startswith("data_get_educator_all"))
async def data_get_educator_all(callback: types.CallbackQuery, session: AsyncSession):
    callback_data = callback.data.split("||")
    current_page = int(callback_data[1] if len(callback_data) >= 2 else 1)
    data = await get_educator(session)

    if len(data) < current_page:
        return await callback.answer(text="Це остання сторінка", show_alert=False)
    elif current_page < 1:
        return await callback.answer(text="Це перша сторінка", show_alert=False)

    await callback.answer()

    educator_data = data[current_page - 1]

    if len(callback_data) >= 2:
        await callback.message.edit_text(
            text=texts.Educator.All.text.format(
                educator_id=educator_data[0],
                group_id=educator_data[1],
                first_name=educator_data[2],
                last_name=educator_data[3],
                sex=educator_data[4],
                date=educator_data[5],
                current_page=current_page,
                all_pages=len(data)
            ),
            reply_markup=await texts.Educator.All.get_buttons(current_page)
        )
    else:
        await callback.message.answer(
            text=texts.Educator.All.text.format(
                educator_id=educator_data[0],
                group_id=educator_data[1],
                first_name=educator_data[2],
                last_name=educator_data[3],
                sex=educator_data[4],
                date=educator_data[5],
                current_page=current_page,
                all_pages=len(data)
            ),
            reply_markup=await texts.Educator.All.get_buttons(current_page)
        )


@router.callback_query(F.data == "data_get_educator_by_id")
async def data_get_educator_by_id(callback: types.CallbackQuery, state: FSMContext):
    await callback.answer()

    await callback.message.answer(
        text=texts.Educator.ById.request_text
    )

    await state.set_state(GetEducatorById.educator_id)


@router.message(GetEducatorById.educator_id)
async def get_educator_by_id_processing(msg: types.Message, state: FSMContext, session: AsyncSession):
    educator_id = int(msg.text)
    educator_data = await get_educator_by_id(educator_id, session)

    if educator_data is None:
        return await msg.answer(
            text=texts.Educator.ById.not_found_text
        )

    await msg.answer(
        text=texts.Educator.ById.text.format(
            educator_id=educator_data[0],
            group_id=educator_data[1],
            first_name=educator_data[2],
            last_name=educator_data[3],
            sex=educator_data[4],
            date=educator_data[5]
        ),
        reply_markup=texts.Educator.ById.builder.as_markup()
    )

    await state.clear()


@router.callback_query(F.data == "data_get_educator_name")
async def data_get_educator_name(callback: types.CallbackQuery, session: AsyncSession):
    await callback.answer()

    name, count = await get_most_frequent_educator_name(session)

    await callback.message.answer(
        text=texts.Educator.Name.text.format(
            name=name,
            count=count
        ),
        reply_markup=texts.Educator.Name.builder.as_markup()
    )


@router.callback_query(F.data == "data_get_educator_avg_age")
async def data_get_educator_avg_age(callback: types.CallbackQuery, session: AsyncSession):
    age = await get_avg_educator_age(session)

    await callback.message.answer(
        text=texts.Educator.AvgAge.text.format(
            age=age
        ),
        reply_markup=texts.Educator.AvgAge.builder.as_markup()
    )

    await callback.answer()


@router.callback_query(F.data == "data_get_educator_group_by_year")
async def data_get_educator_group_by_year(callback: types.CallbackQuery, session: AsyncSession):
    data = await group_educator_by_year(session)

    message = ""
    for row in data:
        message += texts.Educator.GroupByYear.text.format(
            year=int(row[0]),
            amount=row[1],
            ids=", ".join(map(str, row[2]))
        )

    await callback.message.answer(
        text=message,
        reply_markup=texts.Educator.GroupByYear.builder.as_markup()
    )

    await callback.answer()
