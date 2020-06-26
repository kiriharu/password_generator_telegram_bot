from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup


def bool_to_emoji(arg: bool) -> str:
    if arg:
        return "✅"
    return "❌"


def settings_keyboard(user_data: dict) -> InlineKeyboardMarkup:
    buttons = InlineKeyboardMarkup()
    buttons.add(
        InlineKeyboardButton(
            bool_to_emoji(user_data['allow_numbers']), callback_data="nums"
        ),
        InlineKeyboardButton(
            f"Цифры", callback_data="nums"
        )
    )
    buttons.add(
        InlineKeyboardButton(
            bool_to_emoji(user_data['allow_lowercase']), callback_data="lowercase"
        ),
        InlineKeyboardButton(
            f"Прописные буквы", callback_data="lowercase"
        )
    )
    buttons.add(
        InlineKeyboardButton(
            bool_to_emoji(user_data['allow_uppercase']), callback_data="uppercase"
        ),
        InlineKeyboardButton(
            f"Строчные буквы", callback_data="uppercase"
        )
    )
    buttons.add(
        InlineKeyboardButton(
            bool_to_emoji(user_data['allow_spec']), callback_data="spec_chars"
        ),
        InlineKeyboardButton(
            f"Спец. символы", callback_data="spec_chars"
        )
    )
    buttons.add(
        InlineKeyboardButton(
            f"Количество паролей", callback_data="pass_count"
        ),
        InlineKeyboardButton(
            user_data['pass_count'], callback_data="pass_count"
        )
    )
    buttons.add(
        InlineKeyboardButton(
            f"Длина паролей: ", callback_data="pass_len"
        ),
        InlineKeyboardButton(
            user_data['pass_len'], callback_data="pass_len"
        )
    )
    return buttons
