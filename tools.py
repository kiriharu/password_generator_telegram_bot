from telebot.types import Message
import messages


def get_translated_message(text_attr: str, message: Message = None, lang_code: str = None):
    lang = ''
    if message:
        lang = message.from_user.language_code
    if lang_code:
        lang = lang_code
    if not messages.msg.get(lang):
        lang = "en"
    return messages.msg[lang][text_attr]