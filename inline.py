from telebot.types import InlineQueryResultArticle, InputTextMessageContent
from uuid import uuid4
from settings import only_numbers_pic_url, only_str_pic_url, str_and_numbers_pic_url, str_nums_and_spec_pic_url
from generator import generate_only_numbers, generate_only_str, generate_str_and_numbers, generate_str_nums_and_spec
import messages


def only_numbers(length: int) -> InlineQueryResultArticle:
    return InlineQueryResultArticle(
        uuid4().hex,
        messages.inline_only_int,
        InputTextMessageContent(generate_only_numbers(length)),
        thumb_url=only_numbers_pic_url
    )


def only_str(length: int) -> InlineQueryResultArticle:
    return InlineQueryResultArticle(
        uuid4().hex,
        messages.inline_only_str,
        InputTextMessageContent(generate_only_str(length)),
        thumb_url=only_str_pic_url
    )


def str_and_numbers(length: int) -> InlineQueryResultArticle:
    return InlineQueryResultArticle(
        uuid4().hex,
        messages.inline_str_and_numbers,
        InputTextMessageContent(generate_str_and_numbers(length)),
        thumb_url=str_and_numbers_pic_url
    )


def str_nums_and_spec(length: int) -> InlineQueryResultArticle:
    return InlineQueryResultArticle(
        uuid4().hex,
        messages.inline_str_nums_and_specs,
        InputTextMessageContent(generate_str_nums_and_spec(length)),
        thumb_url=str_nums_and_spec_pic_url
    )
