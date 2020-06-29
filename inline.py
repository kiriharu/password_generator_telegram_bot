from telebot.types import InlineQueryResultArticle, InputTextMessageContent
from uuid import uuid4
from tools import get_translated_message
from settings import only_numbers_pic_url, only_str_pic_url, str_and_numbers_pic_url, str_nums_and_spec_pic_url
from generator import generate_only_numbers, generate_only_str, generate_str_and_numbers, generate_str_nums_and_spec
import messages


def only_numbers(length: int, lang_code: str) -> InlineQueryResultArticle:
    return InlineQueryResultArticle(
        uuid4().hex,
        get_translated_message('inline_only_int', lang_code=lang_code),
        InputTextMessageContent(generate_only_numbers(length)),
        thumb_url=only_numbers_pic_url
    )


def only_str(length: int, lang_code: str) -> InlineQueryResultArticle:
    return InlineQueryResultArticle(
        uuid4().hex,
        get_translated_message('inline_only_str', lang_code=lang_code),
        InputTextMessageContent(generate_only_str(length)),
        thumb_url=only_str_pic_url
    )


def str_and_numbers(length: int, lang_code: str) -> InlineQueryResultArticle:
    return InlineQueryResultArticle(
        uuid4().hex,
        get_translated_message('inline_str_and_numbers', lang_code=lang_code),
        InputTextMessageContent(generate_str_and_numbers(length)),
        thumb_url=str_and_numbers_pic_url
    )


def str_nums_and_spec(length: int, lang_code: str) -> InlineQueryResultArticle:
    return InlineQueryResultArticle(
        uuid4().hex,
        get_translated_message('inline_str_nums_and_specs', lang_code=lang_code),
        InputTextMessageContent(generate_str_nums_and_spec(length)),
        thumb_url=str_nums_and_spec_pic_url
    )
