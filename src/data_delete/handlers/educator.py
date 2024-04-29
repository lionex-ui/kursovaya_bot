from aiogram import Router, types, F
from aiogram.fsm.context import FSMContext
from aiogram.filters.state import StatesGroup, State

from src.data_delete import texts
from src.data_delete.database import *

router = Router()


class DeleteEducator(StatesGroup):
    id = State()


@router.callback_query(F.data == "data_delete_educator")
async def data_delete_educator(callback: types.CallbackQuery, state: FSMContext):
    await callback.answer()

    await callback.message.answer(
        text=texts.Delete.id_request
    )

    await state.set_state(DeleteEducator.id)


@router.message(DeleteEducator.id)
async def educator_id_processing(msg: types.Message, session: AsyncSession):
    educator_id = int(msg.text)

    await delete_educator(educator_id, session)

    await msg.answer(
        text=texts.Delete.successful_text
    )

    await msg.answer(
        text=texts.Main.text,
        reply_markup=texts.Main.builder.as_markup()
    )
