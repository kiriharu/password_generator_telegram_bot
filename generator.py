import string
import secrets

lowercase = [letters for letters in string.ascii_lowercase]
uppercase = [letters for letters in string.ascii_uppercase]
nums = [n for n in range(0, 10)]
spec_chars = "!#$%&'()*+,-./:;<=>?@[]^_`{|}~"


def generate_password(length: int, add_lowercase: bool = False, add_uppercase: bool = False,
                      add_nums: bool = False, add_spec: bool = False) -> str:
    chars = []
    if add_lowercase:
        chars += lowercase
    if add_uppercase:
        chars += uppercase
    if add_nums:
        chars += nums
    if add_spec:
        chars += spec_chars

    return ''.join(str(secrets.choice(chars)) for _ in range(length))


def generate_only_numbers(length: int) -> str: return generate_password(length, add_nums=True)


def generate_only_str(length: int) -> str: return generate_password(length, add_uppercase=True, add_lowercase=True)


def generate_str_and_numbers(length: int) -> str: return generate_password(length,
                                                                           add_uppercase=True,
                                                                           add_lowercase=True,
                                                                           add_nums=True)


def generate_str_nums_and_spec(length: int) -> str: return generate_password(length,
                                                                             add_uppercase=True,
                                                                             add_lowercase=True,
                                                                             add_nums=True,
                                                                             add_spec=True)
