import datetime

from aiogram import Router, types, F
from aiogram.fsm.context import FSMContext
from aiogram.filters.state import StatesGroup, State

from src.data_add import texts
from src.data_add.database import *


router = Router()


class AddEducator(StatesGroup):
    group_id = State()
    first_name = State()
    last_name = State()
    sex = State()
    birthday = State()


@router.callback_query(F.data == "data_add_educator")
async def data_add_educator(callback: types.CallbackQuery, state: FSMContext):
    await callback.answer()

    await callback.message.answer(
        text=texts.Add.Educator.group_id_request
    )

    await state.set_state(AddEducator.group_id)


@router.message(AddEducator.group_id)
async def educator_group_id_processing(msg: types.Message, state: FSMContext):
    await state.update_data(group_id=msg.text)

    await msg.answer(
        text=texts.Add.Educator.first_name_request
    )

    await state.set_state(AddEducator.first_name)


@router.message(AddEducator.first_name)
async def educator_first_name_processing(msg: types.Message, state: FSMContext):
    await state.update_data(first_name=msg.text)

    await msg.answer(
        text=texts.Add.Educator.last_name_request
    )

    await state.set_state(AddEducator.last_name)


@router.message(AddEducator.last_name)
async def educator_last_name_processing(msg: types.Message, state: FSMContext):
    await state.update_data(last_name=msg.text)

    await msg.answer(
        text=texts.Add.Educator.sex_request
    )

    await state.set_state(AddEducator.sex)


@router.message(AddEducator.sex)
async def educator_sex_processing(msg: types.Message, state: FSMContext):
    await state.update_data(sex=msg.text)

    await msg.answer(
        text=texts.Add.Educator.birthday_request
    )

    await state.set_state(AddEducator.birthday)


@router.message(AddEducator.birthday)
async def educator_birthday_processing(msg: types.Message, state: FSMContext, session: AsyncSession):
    data = await state.get_data()
    group_id = int(data.get("group_id"))
    first_name = data.get("first_name")
    last_name = data.get("last_name")
    sex = data.get("sex")
    birthday = datetime.strptime(msg.text, "%Y.%m.%d")
    await state.clear()

    await insert_educator(group_id, first_name, last_name, sex, birthday, session)

    await msg.answer(
        text=texts.Add.successful_text
    )

    await msg.answer(
        text=texts.Main.text,
        reply_markup=texts.Main.builder.as_markup()
    )
