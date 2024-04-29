from aiogram import Router, types, F
from aiogram.fsm.context import FSMContext
from aiogram.filters.state import StatesGroup, State

from src.data_add import texts
from src.data_add.database import *


router = Router()


class AddGroup(StatesGroup):
    name = State()


@router.callback_query(F.data == "data_add_group")
async def data_add_group(callback: types.CallbackQuery, state: FSMContext):
    await callback.answer()

    await callback.message.answer(
        text=texts.Add.Group.group_name_request
    )

    await state.set_state(AddGroup.name)


@router.message(AddGroup.name)
async def group_name_processing(msg: types.Message, state: FSMContext, session: AsyncSession):
    name = msg.text
    await state.clear()

    await insert_group(name, session)

    await msg.answer(
        text=texts.Add.successful_text
    )

    await msg.answer(
        text=texts.Main.text,
        reply_markup=texts.Main.builder.as_markup()
    )
