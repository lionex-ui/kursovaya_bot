from aiogram import Router, types, F

from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State

from src.data_get import texts
from src.data_get.database import *


router = Router()


class GetChildById(StatesGroup):
    child_id = State()


class GetChildAvgAge(StatesGroup):
    group_id = State()


@router.callback_query(F.data == "data_get_child")
async def data_get_child(callback: types.CallbackQuery):
    await callback.answer()

    await callback.message.answer(
        text=texts.Child.text,
        reply_markup=texts.Child.builder.as_markup()
    )


@router.callback_query(F.data.startswith("data_get_child_all"))
async def data_get_child_all(callback: types.CallbackQuery, session: AsyncSession):
    callback_data = callback.data.split("||")
    current_page = int(callback_data[1] if len(callback_data) >= 2 else 1)
    data = await get_children(session)

    if len(data) < current_page:
        return await callback.answer(text="Це остання сторінка", show_alert=False)
    elif current_page < 1:
        return await callback.answer(text="Це перша сторінка", show_alert=False)

    await callback.answer()

    child_data = data[current_page - 1]

    if len(callback_data) >= 2:
        await callback.message.edit_text(
            text=texts.Child.All.text.format(
                child_id=child_data[0],
                group_id=child_data[1],
                first_name=child_data[2],
                last_name=child_data[3],
                sex=child_data[4],
                date=child_data[5],
                current_page=current_page,
                all_pages=len(data)
            ),
            reply_markup=await texts.Child.All.get_buttons(current_page)
        )
    else:
        await callback.message.answer(
            text=texts.Child.All.text.format(
                child_id=child_data[0],
                group_id=child_data[1],
                first_name=child_data[2],
                last_name=child_data[3],
                sex=child_data[4],
                date=child_data[5],
                current_page=current_page,
                all_pages=len(data)
            ),
            reply_markup=await texts.Child.All.get_buttons(current_page)
        )


@router.callback_query(F.data == "data_get_child_by_id")
async def data_get_child_by_id(callback: types.CallbackQuery, state: FSMContext):
    await callback.answer()

    await callback.message.answer(
        text=texts.Child.ById.request_text
    )

    await state.set_state(GetChildById.child_id)


@router.message(GetChildById.child_id)
async def get_child_by_id_processing(msg: types.Message, state: FSMContext, session: AsyncSession):
    child_id = int(msg.text)
    child_data = await get_child_by_id(child_id, session)

    if child_data is None:
        return await msg.answer(
            text=texts.Child.ById.not_found_text
        )

    await msg.answer(
        text=texts.Child.ById.text.format(
            child_id=child_data[0],
            group_id=child_data[1],
            first_name=child_data[2],
            last_name=child_data[3],
            sex=child_data[4],
            date=child_data[5]
        ),
        reply_markup=texts.Child.ById.builder.as_markup()
    )

    await state.clear()


@router.callback_query(F.data == "data_get_child_name")
async def data_get_child_name(callback: types.CallbackQuery, session: AsyncSession):
    await callback.answer()

    name, count = await get_most_frequent_child_name(session)

    await callback.message.answer(
        text=texts.Child.Name.text.format(
            name=name,
            count=count
        ),
        reply_markup=texts.Child.Name.builder.as_markup()
    )


@router.callback_query(F.data == "data_get_child_avg_age")
async def data_get_child_avg_age(callback: types.CallbackQuery, state: FSMContext):
    await callback.answer()

    await callback.message.answer(
        text=texts.Child.AvgAge.request_text
    )

    await state.set_state(GetChildAvgAge.group_id)


@router.message(GetChildAvgAge.group_id)
async def get_child_avg_age_group_id_processing(msg: types.Message, state: FSMContext, session: AsyncSession):
    group_id = int(msg.text)
    age = await get_avg_child_age(group_id, session)

    await msg.answer(
        text=texts.Child.AvgAge.text.format(
            age=age
        ),
        reply_markup=texts.Child.AvgAge.builder.as_markup()
    )

    await state.clear()


@router.callback_query(F.data == "data_get_child_group_by_year")
async def data_get_child_group_by_year(callback: types.CallbackQuery, session: AsyncSession):
    data = await group_children_by_year(session)

    message = ""
    for row in data:
        message += texts.Child.GroupByYear.text.format(
            year=int(row[0]),
            amount=row[1],
            ids=", ".join(map(str, row[2]))
        )

    await callback.message.answer(
        text=message,
        reply_markup=texts.Child.GroupByYear.builder.as_markup()
    )

    await callback.answer()
