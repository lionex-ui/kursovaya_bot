from aiogram import types
from aiogram.utils.keyboard import InlineKeyboardBuilder


class Start:

    text = "Вітаю! Оберіть дію: "

    builder = InlineKeyboardBuilder()
    builder.row(
        *[
            types.InlineKeyboardButton(
                text="Додання даних",
                callback_data="data_add"
            ),
            types.InlineKeyboardButton(
                text="Видалення даних",
                callback_data="data_delete"
            ),
            types.InlineKeyboardButton(
                text="Оновлення даних",
                callback_data="data_edit"
            ),
            types.InlineKeyboardButton(
                text="Виведення даних",
                callback_data="data_get"
            )
        ],
        width=1
    )
