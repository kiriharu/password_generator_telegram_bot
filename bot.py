from telebot import TeleBot, logger as telelogger
from telebot.types import Message, CallbackQuery, InlineQuery
from storage import UserStorage
from settings import TELEGRAM_BOT_TOKEN, MAX_PASS_COUNT, MAX_PASS_LEN
from keyboards import settings_keyboard
from generator import generate_password
from html import escape
import logging
import inline
import messages


# TODO: В докере сделать db.json вне контейнера
# TODO: Генерация паролей из своего словаря
# TODO: multilang, acho
# TODO: Генерация паролей из словаря
# TODO: Readme на английском и русском

bot = TeleBot(TELEGRAM_BOT_TOKEN)
logger = telelogger
telelogger.setLevel(logging.INFO)
storj = UserStorage()


def send_settings_message(chat_id: int) -> None:
    bot.send_message(
        chat_id,
        messages.settings_message,
        reply_markup=settings_keyboard(storj.get_or_create(chat_id))
    )


def edit_settings_message(chat_id: int, message_id: int) -> None:
    bot.edit_message_text(
        messages.settings_message,
        chat_id, message_id,
        reply_markup=settings_keyboard(storj.get_or_create(chat_id))
    )


def check_for_generate_nothing(user_data: dict) -> bool:
    """
    Check settings for options, if all bool options is false return True.
    This check is necessary, at least one list should exist for password generation

    :param user_data:
    :return:
    """
    if not any([user_data["allow_lowercase"],
                user_data["allow_uppercase"],
                user_data["allow_numbers"],
                user_data["allow_spec"]]):
        return True


def invert_setting(field: str, query: CallbackQuery) -> None:
    """
    Invert setting in database by field and edit message provided by query
    :param field: Field in database to invert
    :param query: Callback query
    :return:
    """
    user_id = query.message.chat.id
    filled_field = storj.get_or_create(user_id)[field]
    storj.update(field, not filled_field, user_id)
    edit_settings_message(user_id, query.message.message_id)


# Commands
@bot.message_handler(commands=['start'])
def send_welcome(message: Message) -> None:
    chat_id = message.chat.id
    logger.info(f"Send welcome to {chat_id}")
    bot.reply_to(message, messages.start)
    storj.get_or_create(message.chat.id)


@bot.message_handler(commands=['settings'])
def settings(message: Message) -> None:
    chat_id = message.chat.id
    logger.info(f"Send settings to {chat_id}")
    send_settings_message(chat_id)


@bot.message_handler(commands=['generate'])
def generate(message: Message) -> None:
    chat_id = message.chat.id
    logger.info(f"Generate password for {chat_id}")
    user_data = storj.get_or_create(chat_id)
    if check_for_generate_nothing(user_data):
        return bot.send_message(chat_id, messages.nothing_to_generate)
    passwords = [escape(generate_password(
        length=int(user_data["pass_len"]),
        add_lowercase=user_data["allow_lowercase"],
        add_uppercase=user_data["allow_uppercase"],
        add_nums=user_data["allow_numbers"],
        add_spec=user_data["allow_spec"]
    )) for _ in range(0, user_data["pass_count"])]
    passwords = list(map(lambda password: f"<code>{password}</code>", passwords))
    bot.send_message(chat_id, '\n'.join(passwords), parse_mode="html")


# Next step handler


def pass_count_and_len_step(message: Message, options: dict) -> None:
    """
    Step handler for write new values of pass_count and pass_len to database
    This function check value for is_digit, max_val is bigger then val, val less then 0 and update val to database
    After all, bot reply a success_message and send settings message

    :param message: Message obj
    :param options: dict with max_val, db_field and success_message
    :return:
    """
    chat_id = message.chat.id
    val = message.text
    if not str.isdigit(val):
        return bot.reply_to(message, messages.need_int)
    # Converting to int after checking
    val = int(val)
    if val > options["max_val"]:
        return bot.reply_to(message, messages.int_to_big.format(options["max_val"]))
    if val <= 0:
        return bot.reply_to(message, messages.int_to_small)

    storj.update(options["db_field"], val, chat_id)
    bot.reply_to(message, options["success_message"].format(val))

    # Sending settings keyboard...
    send_settings_message(chat_id)


# Callback handlers


@bot.callback_query_handler(lambda query: query.data in ["nums", "lowercase", "uppercase", "spec_chars"])
def invert_bool_settings(query: CallbackQuery) -> None:
    logger.info(f"{query.from_user.id} invert settings...")
    if query.data == "nums":
        invert_setting("allow_numbers", query)
    if query.data == "lowercase":
        invert_setting("allow_lowercase", query)
    if query.data == "uppercase":
        invert_setting("allow_uppercase", query)
    if query.data == "spec_chars":
        invert_setting("allow_spec", query)


@bot.callback_query_handler(lambda query: query.data in ["pass_count", "pass_len"])
def pass_count_and_len_callback(query: CallbackQuery) -> None:
    chat_id = query.message.chat.id
    logger.info(f"{query.from_user.id} setting {query.data}")
    if query.data == "pass_count":
        bot.send_message(chat_id, messages.pass_count_question)
        bot.register_next_step_handler_by_chat_id(
            chat_id, pass_count_and_len_step, dict(
                max_val=MAX_PASS_COUNT,
                db_field="pass_count",
                success_message=messages.pass_count_setted
            )
        )
    if query.data == "pass_len":
        bot.send_message(chat_id, messages.pass_generation_question)
        bot.register_next_step_handler_by_chat_id(
            chat_id, pass_count_and_len_step, dict(
                max_val=MAX_PASS_LEN,
                db_field="pass_len",
                success_message=messages.pass_len_setted
            )
        )


@bot.inline_handler(lambda q: q.query.isdigit() and 0 < int(q.query) < 64)
def inline_handler(query: InlineQuery):
    try:
        logger.info(f"Sending inline to {query.from_user.id}")
        length = int(query.query)
        only_numbers = inline.only_numbers(length)
        only_str = inline.only_str(length)
        str_and_numbers = inline.str_and_numbers(length)
        str_nums_and_spec = inline.str_nums_and_spec(length)
        bot.answer_inline_query(query.id, [
            only_numbers, only_str, str_and_numbers, str_nums_and_spec
        ], cache_time=0)
    except Exception as e:
        logger.error(f"Exception occurred in inline handler: {e}")


bot.infinity_polling()
