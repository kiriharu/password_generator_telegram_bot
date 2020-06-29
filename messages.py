msg = dict(
    ru=dict(
        start="""Тут короче сообщение о том, как все у нас хорошо и какой у нас классный генератор паролей!
Настройки в /settings
Генерировать пароль через /generate""",
        need_int="Неправильный ввод, вам нужно ввести число.",
        int_too_big="Слишком большое число. Необходимо указать число до {}",
        int_too_small="Слишком маленькое число, необходимо указать число больше ноля.",
        pass_count_setted="Количество паролей для вывода установлено на {}",
        pass_len_setted="Размер паролей установлен на {}",
        pass_len_generation_question="Какого размера пароли вы хотите получать при генерации?",
        pass_count_question="Какое количество паролей вы хотите получать при генерации?",
        settings_message="Ваши настройки на данный момент:",
        nothing_to_generate="""Тебе нет из чего генерировать пароль!
Вернись в настройки через через /settings и установи напротив хоть одну галочку.""",

        keyboard_nums="Цифры",
        keyboard_lowercase="Прописные буквы",
        keyboard_uppercase="Строчные буквы",
        keyboard_spec_chars="Спец. символы",
        keyboard_pass_count="Количество паролей",
        keyboard_pass_len="Длина паролей",

        inline_only_int="Только цифры",
        inline_only_str="Только строчные и прописные буквы",
        inline_str_and_numbers="Строчные и прописные буквы с цифрами",
        inline_str_nums_and_specs="Строчные и прописные буквы, цифры, спецсимволы",
    ),
    en=dict(
        start="""Simple eng message""",
        need_int="Incorrect input, you need to enter a number.",
        int_too_big="Too many. You must enter a number up to {}",
        int_too_small="Too small. You must enter a number bigger than 0.",
        pass_count_setted="The number of passwords for output is set to {}",
        pass_len_setted="Password length set to {}",
        pass_len_generation_question="What passwords size do you want to receive after generation?",
        pass_count_question="What count of passwords do you want to receive after generation?",
        settings_message="Your settings right now:",
        nothing_to_generate="""You set all checkmarks to no!
Go back to /settings and set at least one checkmark option.""",

        keyboard_nums="Numbers",
        keyboard_lowercase="Lowercase",
        keyboard_uppercase="Uppercase",
        keyboard_spec_chars="Special chars",
        keyboard_pass_count="Passwords count",
        keyboard_pass_len="Password length",

        inline_only_int="Only numbers",
        inline_only_str="Only lowercase and uppercase chars",
        inline_str_and_numbers="Lowercase, uppercase chars and numbers",
        inline_str_nums_and_specs="Lowercase and uppercase chars, numbers and spec. chars",
    )
)
