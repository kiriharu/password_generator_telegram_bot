from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup
from tools import get_translated_message


def bool_to_emoji(arg: bool) -> str:
    if arg:
        return "✅"
    return "❌"


def settings_keyboard(user_data: dict, lang_code: str) -> InlineKeyboardMarkup:
    buttons = InlineKeyboardMarkup()
    buttons.add(
        InlineKeyboardButton(
            bool_to_emoji(user_data['allow_numbers']), callback_data="nums"
        ),
        InlineKeyboardButton(
            get_translated_message('keyboard_nums', lang_code=lang_code), callback_data="nums"
        )
    )
    buttons.add(
        InlineKeyboardButton(
            bool_to_emoji(user_data['allow_lowercase']), callback_data="lowercase"
        ),
        InlineKeyboardButton(
            get_translated_message('keyboard_lowercase', lang_code=lang_code), callback_data="lowercase"
        )
    )
    buttons.add(
        InlineKeyboardButton(
            bool_to_emoji(user_data['allow_uppercase']), callback_data="uppercase"
        ),
        InlineKeyboardButton(
            get_translated_message('keyboard_uppercase', lang_code=lang_code), callback_data="uppercase"
        )
    )
    buttons.add(
        InlineKeyboardButton(
            bool_to_emoji(user_data['allow_spec']), callback_data="spec_chars"
        ),
        InlineKeyboardButton(
            get_translated_message('keyboard_spec_chars', lang_code=lang_code), callback_data="spec_chars"
        )
    )
    buttons.add(
        InlineKeyboardButton(
            get_translated_message('keyboard_pass_count', lang_code=lang_code), callback_data="pass_count"
        ),
        InlineKeyboardButton(
            user_data['pass_count'], callback_data="pass_count"
        )
    )
    buttons.add(
        InlineKeyboardButton(
            get_translated_message('keyboard_pass_len', lang_code=lang_code), callback_data="pass_len"
        ),
        InlineKeyboardButton(
            user_data['pass_len'], callback_data="pass_len"
        )
    )
    return buttons
