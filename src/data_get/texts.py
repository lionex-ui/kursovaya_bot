from aiogram import types
from aiogram.utils.keyboard import InlineKeyboardBuilder


class Main:

    text = "Оберіть про кого отримати інформацію: "

    builder = InlineKeyboardBuilder()
    builder.row(
        *[
            types.InlineKeyboardButton(
                text="Дитина",
                callback_data="data_get_child"
            ),
            types.InlineKeyboardButton(
                text="Вихователь",
                callback_data="data_get_educator"
            ),
            types.InlineKeyboardButton(
                text="Група",
                callback_data="data_get_group"
            ),
            types.InlineKeyboardButton(
                text="Назад",
                callback_data="start"
            )
        ],
        width=3
    )


class Child:

    text = "Оберіть що саме потрібно вивести: "

    builder = InlineKeyboardBuilder()
    builder.row(
        *[
            types.InlineKeyboardButton(
                text="Всю інформацію",
                callback_data="data_get_child_all"
            ),
            types.InlineKeyboardButton(
                text="Інформацію по одній дитині",
                callback_data="data_get_child_by_id"
            ),
            types.InlineKeyboardButton(
                text="Найпопулярніше ім'я",
                callback_data="data_get_child_name"
            ),
            types.InlineKeyboardButton(
                text="Середній вік",
                callback_data="data_get_child_avg_age"
            ),
            types.InlineKeyboardButton(
                text="Групування по року народження",
                callback_data="data_get_child_group_by_year"
            ),
            types.InlineKeyboardButton(
                text="Назад",
                callback_data="data_get"
            )
        ],
        width=1
    )

    class All:

        text = ("ID: {child_id}\n"
                "ID Групи: {group_id}\n"
                "Ім'я: {first_name}\n"
                "Прізвище: {last_name}\n"
                "Стать: {sex}\n"
                "Дата народженяя: {date}\n\n"
                "Сторінка {current_page}/{all_pages}")

        @staticmethod
        async def get_buttons(current_page: int) -> types.InlineKeyboardMarkup:
            builder = InlineKeyboardBuilder()
            builder.row(
                *[
                    types.InlineKeyboardButton(
                        text="⬅️",
                        callback_data=f"data_get_child_all||{current_page - 1}"
                    ),
                    types.InlineKeyboardButton(
                        text="Назад",
                        callback_data="data_get_child"
                    ),
                    types.InlineKeyboardButton(
                        text="➡️",
                        callback_data=f"data_get_child_all||{current_page + 1}"
                    )
                ],
                width=3
            )

            return builder.as_markup()

    class ById:

        request_text = "Введіть ID дитини: "

        text = ("ID: {child_id}\n"
                "ID Групи: {group_id}\n"
                "Ім'я: {first_name}\n"
                "Прізвище: {last_name}\n"
                "Стать: {sex}\n"
                "Дата народженяя: {date}")

        not_found_text = "Немає дитини з таким ID."

        builder = InlineKeyboardBuilder()
        builder.add(
            *[
                types.InlineKeyboardButton(
                    text="Назад",
                    callback_data="data_get_child"
                )
            ]
        )

    class Name:

        text = ("Найпопулярніше ім'я: {name}\n"
                "Воно повторюється {count} разів.")

        builder = InlineKeyboardBuilder()
        builder.add(
            *[
                types.InlineKeyboardButton(
                    text="Назад",
                    callback_data="data_get_child"
                )
            ]
        )

    class AvgAge:

        request_text = "Введіть ID групи: "

        text = "Середній вік дітей: {age} роки(-ів)."

        builder = InlineKeyboardBuilder()
        builder.add(
            *[
                types.InlineKeyboardButton(
                    text="Назад",
                    callback_data="data_get_child"
                )
            ]
        )

    class GroupByYear:

        text = ("Рік: {year}\n"
                "Кіл-ть дітей: {amount}\n"
                "Список ID: {ids}\n\n")

        builder = InlineKeyboardBuilder()
        builder.add(
            *[
                types.InlineKeyboardButton(
                    text="Назад",
                    callback_data="data_get_child"
                )
            ]
        )


class Educator:

    text = "Оберіть що саме потрібно вивести: "

    builder = InlineKeyboardBuilder()
    builder.row(
        *[
            types.InlineKeyboardButton(
                text="Всю інформацію",
                callback_data="data_get_educator_all"
            ),
            types.InlineKeyboardButton(
                text="Інформацію по одному вихователю",
                callback_data="data_get_educator_by_id"
            ),
            types.InlineKeyboardButton(
                text="Найпопулярніше ім'я",
                callback_data="data_get_educator_name"
            ),
            types.InlineKeyboardButton(
                text="Середній вік",
                callback_data="data_get_educator_avg_age"
            ),
            types.InlineKeyboardButton(
                text="Групування по року народження",
                callback_data="data_get_educator_group_by_year"
            ),
            types.InlineKeyboardButton(
                text="Назад",
                callback_data="data_get"
            )
        ],
        width=1
    )

    class All:

        text = ("ID: {educator_id}\n"
                "ID Групи: {group_id}\n"
                "Ім'я: {first_name}\n"
                "Прізвище: {last_name}\n"
                "Стать: {sex}\n"
                "Дата народженяя: {date}\n\n"
                "Сторінка {current_page}/{all_pages}")

        @staticmethod
        async def get_buttons(current_page: int) -> types.InlineKeyboardMarkup:
            builder = InlineKeyboardBuilder()
            builder.row(
                *[
                    types.InlineKeyboardButton(
                        text="⬅️",
                        callback_data=f"data_get_educator_all||{current_page - 1}"
                    ),
                    types.InlineKeyboardButton(
                        text="Назад",
                        callback_data="data_get_educator"
                    ),
                    types.InlineKeyboardButton(
                        text="➡️",
                        callback_data=f"data_get_educator_all||{current_page + 1}"
                    )
                ],
                width=3
            )

            return builder.as_markup()

    class ById:

        request_text = "Введіть ID вихователя: "

        text = ("ID: {educator_id}\n"
                "ID Групи: {group_id}\n"
                "Ім'я: {first_name}\n"
                "Прізвище: {last_name}\n"
                "Стать: {sex}\n"
                "Дата народженяя: {date}")

        not_found_text = "Немає educator з таким ID."

        builder = InlineKeyboardBuilder()
        builder.add(
            *[
                types.InlineKeyboardButton(
                    text="Назад",
                    callback_data="data_get_educator"
                )
            ]
        )

    class Name:

        text = ("Найпопулярніше ім'я: {name}\n"
                "Воно повторюється {count} разів.")

        builder = InlineKeyboardBuilder()
        builder.add(
            *[
                types.InlineKeyboardButton(
                    text="Назад",
                    callback_data="data_get_educator"
                )
            ]
        )

    class AvgAge:

        text = "Середній вік: {age} роки(-ів)."

        builder = InlineKeyboardBuilder()
        builder.add(
            *[
                types.InlineKeyboardButton(
                    text="Назад",
                    callback_data="data_get_educator"
                )
            ]
        )

    class GroupByYear:

        text = ("Рік: {year}\n"
                "Кіл-ть вихователів: {amount}\n"
                "Список ID: {ids}\n\n")

        builder = InlineKeyboardBuilder()
        builder.add(
            *[
                types.InlineKeyboardButton(
                    text="Назад",
                    callback_data="data_get_educator"
                )
            ]
        )


class Group:

    text = "Оберіть що саме потрібно вивести: "

    builder = InlineKeyboardBuilder()
    builder.row(
        *[
            types.InlineKeyboardButton(
                text="Вивести всю інформацію",
                callback_data="data_get_group_all"
            )
        ]
    )

    class All:

        text = ("ID: {group_id}\n"
                "Назва групи: {group_name}\n"
                "Ім'я та прізвище вихователя: {educator_name}\n"
                "Кіл-ть дітей: {children_amount}\n"
                "Сторінка {current_page}/{all_pages}")

        @staticmethod
        async def get_buttons(current_page: int) -> types.InlineKeyboardMarkup:
            builder = InlineKeyboardBuilder()
            builder.row(
                *[
                    types.InlineKeyboardButton(
                        text="⬅️",
                        callback_data=f"data_get_group_all||{current_page - 1}"
                    ),
                    types.InlineKeyboardButton(
                        text="Назад",
                        callback_data="data_get_group"
                    ),
                    types.InlineKeyboardButton(
                        text="➡️",
                        callback_data=f"data_get_group_all||{current_page + 1}"
                    )
                ],
                width=3
            )

            return builder.as_markup()
