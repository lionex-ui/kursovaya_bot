import datetime

from aiogram import Router, types, F
from aiogram.fsm.context import FSMContext
from aiogram.filters.state import StatesGroup, State

from src.data_edit import texts
from src.data_edit.database import *


router = Router()


class EditEducator(StatesGroup):
    educator_id = State()
    group_id = State()
    first_name = State()
    last_name = State()
    sex = State()
    birthday = State()


@router.callback_query(F.data == "data_edit_educator")
async def data_edit_educator(callback: types.CallbackQuery, state: FSMContext):
    await callback.answer()

    await callback.message.answer(
        text=texts.Edit.Educator.educator_id_request
    )

    await state.set_state(EditEducator.educator_id)


@router.message(EditEducator.educator_id)
async def educator_id_processing(msg: types.Message, state: FSMContext):
    await state.update_data(educator_id=msg.text)

    await msg.answer(
        text=texts.Edit.Educator.group_id_request
    )

    await state.set_state(EditEducator.group_id)


@router.message(EditEducator.group_id)
async def educator_group_id_processing(msg: types.Message, state: FSMContext):
    await state.update_data(group_id=msg.text)

    await msg.answer(
        text=texts.Edit.Educator.first_name_request
    )

    await state.set_state(EditEducator.first_name)


@router.message(EditEducator.first_name)
async def educator_first_name_processing(msg: types.Message, state: FSMContext):
    await state.update_data(first_name=msg.text)

    await msg.answer(
        text=texts.Edit.Educator.last_name_request
    )

    await state.set_state(EditEducator.last_name)


@router.message(EditEducator.last_name)
async def educator_last_name_processing(msg: types.Message, state: FSMContext):
    await state.update_data(last_name=msg.text)

    await msg.answer(
        text=texts.Edit.Educator.sex_request
    )

    await state.set_state(EditEducator.sex)


@router.message(EditEducator.sex)
async def educator_sex_processing(msg: types.Message, state: FSMContext):
    await state.update_data(sex=msg.text)

    await msg.answer(
        text=texts.Edit.Educator.birthday_request
    )

    await state.set_state(EditEducator.birthday)


@router.message(EditEducator.birthday)
async def educator_birthday_processing(msg: types.Message, state: FSMContext, session: AsyncSession):
    data = await state.get_data()
    educator_id = int(data.get("educator_id"))
    group_id = int(data.get("group_id"))
    first_name = data.get("first_name")
    last_name = data.get("last_name")
    sex = data.get("sex")
    birthday = datetime.strptime(msg.text, "%Y.%m.%d")
    await state.clear()

    await update_educator(educator_id, group_id, first_name, last_name, sex, birthday, session)

    await msg.answer(
        text=texts.Edit.successful_text
    )

    await msg.answer(
        text=texts.Main.text,
        reply_markup=texts.Main.builder.as_markup()
    )
