from aiogram import Router, types, F
from aiogram.fsm.context import FSMContext
from aiogram.filters.state import StatesGroup, State

from src.data_edit import texts
from src.data_edit.database import *


router = Router()


class EditGroup(StatesGroup):
    group_id = State()
    name = State()


@router.callback_query(F.data == "data_edit_group")
async def data_edit_group(callback: types.CallbackQuery, state: FSMContext):
    await callback.answer()

    await callback.message.answer(
        text=texts.Edit.Group.group_id_request
    )

    await state.set_state(EditGroup.group_id)


@router.message(EditGroup.group_id)
async def group_id_processing(msg: types.Message, state: FSMContext):
    await state.update_data(group_id=msg.text)

    await msg.answer(
        text=texts.Edit.Group.group_name_request
    )

    await state.set_state(EditGroup.name)


@router.message(EditGroup.name)
async def group_name_processing(msg: types.Message, state: FSMContext, session: AsyncSession):
    data = await state.get_data()
    group_id = int(data.get("group_id"))
    name = msg.text
    await state.clear()

    await update_group(group_id, name, session)

    await msg.answer(
        text=texts.Edit.successful_text
    )

    await msg.answer(
        text=texts.Main.text,
        reply_markup=texts.Main.builder.as_markup()
    )
