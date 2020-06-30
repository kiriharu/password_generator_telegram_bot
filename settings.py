from dotenv import load_dotenv
import os

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)

# Loading token from .env
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

DEFAULT_PASS_LEN = 8
DEFAULT_PASS_COUNT = 3
DEFAULT_ALLOW_NUMBERS = True
DEFAULT_ALLOW_LOWERCASE = True
DEFAULT_ALLOW_UPPERCASE = True
DEFAULT_ALLOW_SPEC = False

MAX_PASS_LEN = 64
MAX_PASS_COUNT = 16

only_numbers_pic_url = "https://raw.githubusercontent.com/" \
                       "kiriharu/password_generator_telegram_bot/master/img/only_numbers.png"
only_str_pic_url = "https://raw.githubusercontent.com/" \
                   "kiriharu/password_generator_telegram_bot/master/img/only_str.png"
str_and_numbers_pic_url = "https://raw.githubusercontent.com/" \
                          "kiriharu/password_generator_telegram_bot/master/img/str_and_numbers.png"

str_nums_and_spec_pic_url = "https://raw.githubusercontent.com/" \
                          "kiriharu/password_generator_telegram_bot/master/str_nums_and_spec.png"