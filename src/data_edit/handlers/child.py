import datetime

from aiogram import Router, types, F
from aiogram.fsm.context import FSMContext
from aiogram.filters.state import StatesGroup, State

from src.data_edit import texts
from src.data_edit.database import *


router = Router()


class EditChild(StatesGroup):
    child_id = State()
    group_id = State()
    first_name = State()
    last_name = State()
    sex = State()
    birthday = State()


@router.callback_query(F.data == "data_edit_child")
async def data_edit_child(callback: types.CallbackQuery, state: FSMContext):
    await callback.answer()

    await callback.message.answer(
        text=texts.Edit.Child.child_id_request
    )

    await state.set_state(EditChild.child_id)


@router.message(EditChild.child_id)
async def child_id_processing(msg: types.Message, state: FSMContext):
    await state.update_data(child_id=msg.text)

    await msg.answer(
        text=texts.Edit.Child.group_id_request
    )

    await state.set_state(EditChild.group_id)


@router.message(EditChild.group_id)
async def child_group_id_processing(msg: types.Message, state: FSMContext):
    await state.update_data(group_id=msg.text)

    await msg.answer(
        text=texts.Edit.Child.first_name_request
    )

    await state.set_state(EditChild.first_name)


@router.message(EditChild.first_name)
async def child_first_name_processing(msg: types.Message, state: FSMContext):
    await state.update_data(first_name=msg.text)

    await msg.answer(
        text=texts.Edit.Child.last_name_request
    )

    await state.set_state(EditChild.last_name)


@router.message(EditChild.last_name)
async def child_last_name_processing(msg: types.Message, state: FSMContext):
    await state.update_data(last_name=msg.text)

    await msg.answer(
        text=texts.Edit.Child.sex_request
    )

    await state.set_state(EditChild.sex)


@router.message(EditChild.sex)
async def child_sex_processing(msg: types.Message, state: FSMContext):
    await state.update_data(sex=msg.text)

    await msg.answer(
        text=texts.Edit.Child.birthday_request
    )

    await state.set_state(EditChild.birthday)


@router.message(EditChild.birthday)
async def child_birthday_processing(msg: types.Message, state: FSMContext, session: AsyncSession):
    data = await state.get_data()
    child_id = int(data.get("child_id"))
    group_id = int(data.get("group_id"))
    first_name = data.get("first_name")
    last_name = data.get("last_name")
    sex = data.get("sex")
    birthday = datetime.strptime(msg.text, "%Y.%m.%d")
    await state.clear()

    await update_child(child_id, group_id, first_name, last_name, sex, birthday, session)

    await msg.answer(
        text=texts.Edit.successful_text
    )

    await msg.answer(
        text=texts.Main.text,
        reply_markup=texts.Main.builder.as_markup()
    )
