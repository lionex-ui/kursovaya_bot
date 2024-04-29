from aiogram import types
from aiogram.utils.keyboard import InlineKeyboardBuilder


class Main:

    text = "Оберіть кого редагувати: "

    builder = InlineKeyboardBuilder()
    builder.row(
        *[
            types.InlineKeyboardButton(
                text="Дитина",
                callback_data="data_edit_child"
            ),
            types.InlineKeyboardButton(
                text="Вихователь",
                callback_data="data_edit_educator"
            ),
            types.InlineKeyboardButton(
                text="Група",
                callback_data="data_edit_group"
            ),
            types.InlineKeyboardButton(
                text="Назад",
                callback_data="start"
            )
        ],
        width=3
    )


class Edit:

    successful_text = "Дані успішно змінені."

    class Child:

        child_id_request = "Введіть ID дитини: "
        group_id_request = "Введіть ID групи: "
        first_name_request = "Введіть ім'я дитини: "
        last_name_request = "Введіть прізвище дитини: "
        sex_request = "Введіть стать дитини: "
        birthday_request = "Введіть дату народження дитини (рррр.мм.дд): "

    class Educator:

        educator_id_request = "Введіть ID вихователя: "
        group_id_request = "Введіть ID групи: "
        first_name_request = "Введіть ім'я вихователя: "
        last_name_request = "Введіть прізвище вихователя: "
        sex_request = "Введіть стать вихователя: "
        birthday_request = "Введіть дату народження вихователя (рррр.мм.дд): "

    class Group:

        group_id_request = "Введіть ID групи: "
        group_name_request = "Введіть назву групи: "
