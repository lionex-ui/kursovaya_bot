import datetime

from aiogram import Router, types, F
from aiogram.fsm.context import FSMContext
from aiogram.filters.state import StatesGroup, State

from src.data_add import texts
from src.data_add.database import *


router = Router()


class AddChild(StatesGroup):
    group_id = State()
    first_name = State()
    last_name = State()
    sex = State()
    birthday = State()


@router.callback_query(F.data == "data_add_child")
async def data_add_child(callback: types.CallbackQuery, state: FSMContext):
    await callback.answer()

    await callback.message.answer(
        text=texts.Add.Child.group_id_request
    )

    await state.set_state(AddChild.group_id)


@router.message(AddChild.group_id)
async def child_group_id_processing(msg: types.Message, state: FSMContext):
    await state.update_data(group_id=msg.text)

    await msg.answer(
        text=texts.Add.Child.first_name_request
    )

    await state.set_state(AddChild.first_name)


@router.message(AddChild.first_name)
async def child_first_name_processing(msg: types.Message, state: FSMContext):
    await state.update_data(first_name=msg.text)

    await msg.answer(
        text=texts.Add.Child.last_name_request
    )

    await state.set_state(AddChild.last_name)


@router.message(AddChild.last_name)
async def child_last_name_processing(msg: types.Message, state: FSMContext):
    await state.update_data(last_name=msg.text)

    await msg.answer(
        text=texts.Add.Child.sex_request
    )

    await state.set_state(AddChild.sex)


@router.message(AddChild.sex)
async def child_sex_processing(msg: types.Message, state: FSMContext):
    await state.update_data(sex=msg.text)

    await msg.answer(
        text=texts.Add.Child.birthday_request
    )

    await state.set_state(AddChild.birthday)


@router.message(AddChild.birthday)
async def child_birthday_processing(msg: types.Message, state: FSMContext, session: AsyncSession):
    data = await state.get_data()
    group_id = int(data.get("group_id"))
    first_name = data.get("first_name")
    last_name = data.get("last_name")
    sex = data.get("sex")
    birthday = datetime.strptime(msg.text, "%Y.%m.%d")
    await state.clear()

    await insert_child(group_id, first_name, last_name, sex, birthday, session)

    await msg.answer(
        text=texts.Add.successful_text
    )

    await msg.answer(
        text=texts.Main.text,
        reply_markup=texts.Main.builder.as_markup()
    )
