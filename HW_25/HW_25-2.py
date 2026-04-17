"""Логирование ошибок

Перенаправьте в предыдущей задаче вывод ошибок в
файл errors.log в соответствии с форматом ниже.

Пример вывода:
2025-02-23 22:38:53,686 - ERROR - test.py - 16 - Ошибка:
Введено некорректное число.
"""

import logging

logging.basicConfig(
    filename="errors.log",
    level=logging.ERROR,
    force=True,  # force=True удалит старые обработчики среды (лучше всегда писать)
    encoding='utf-8',  # добавила, чтоб корректно отображался текст ошибки (лучше всегда писать)
    format="%(asctime)s - %(levelname)s - %(filename)s - %(lineno)d - %(message)s",
)


def a_div_b():
    try:
        a = float(input("Введите делимое: "))
        b = float(input("Введите делитель: "))

        print(f"Результат: {a / b}")

    except ValueError:
        logging.error("Ошибка: Введено некорректное число.")
    except ZeroDivisionError:
        logging.error("Ошибка: Деление на ноль невозможно.")


a_div_b()