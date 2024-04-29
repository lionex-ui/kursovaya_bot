from aiogram import types
from aiogram.utils.keyboard import InlineKeyboardBuilder


class Main:

    text = "Оберіть кого видалити: "

    builder = InlineKeyboardBuilder()
    builder.row(
        *[
            types.InlineKeyboardButton(
                text="Дитина",
                callback_data="data_delete_child"
            ),
            types.InlineKeyboardButton(
                text="Вихователь",
                callback_data="data_delete_educator"
            ),
            types.InlineKeyboardButton(
                text="Група",
                callback_data="data_delete_group"
            )
        ],
        width=3
    )
    builder.row(
        *[
            types.InlineKeyboardButton(
                text="Видалити дітей старших 10 років",
                callback_data="data_delete_old_child"
            ),
            types.InlineKeyboardButton(
                text="Назад",
                callback_data="start"
            )
        ],
        width=1
    )


class Delete:

    id_request = "Введіть ID: "
    successful_text = "Дані успішно видалені."
