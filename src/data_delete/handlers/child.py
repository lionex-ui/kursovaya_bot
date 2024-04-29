from aiogram import Router, types, F
from aiogram.fsm.context import FSMContext
from aiogram.filters.state import StatesGroup, State

from src.data_delete import texts
from src.data_delete.database import *


router = Router()


class DeleteChild(StatesGroup):
    id = State()


@router.callback_query(F.data == "data_delete_child")
async def data_delete_child(callback: types.CallbackQuery, state: FSMContext):
    await callback.answer()

    await callback.message.answer(
        text=texts.Delete.id_request
    )

    await state.set_state(DeleteChild.id)


@router.message(DeleteChild.id)
async def child_id_processing(msg: types.Message, session: AsyncSession):
    child_id = int(msg.text)

    await delete_child(child_id, session)

    await msg.answer(
        text=texts.Delete.successful_text
    )

    await msg.answer(
        text=texts.Main.text,
        reply_markup=texts.Main.builder.as_markup()
    )


@router.callback_query(F.data == "data_delete_old_child")
async def data_delete_old_child(callback: types.CallbackQuery, session: AsyncSession):
    await delete_old_children(session)

    await callback.message.answer(
        text=texts.Delete.successful_text
    )

    await callback.answer()
