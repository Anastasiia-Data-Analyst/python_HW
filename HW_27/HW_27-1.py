"""
Фильтрация по ключевому слову
Напишите программу, которая ищет в файле все строки,
содержащие указанное пользователем слово, и сохраняет их в новый файл.

- Имя нового файла формируется как <keyword>_<original_filename>.
- Если файл не существует, программа должна вывести ошибку.
- Если совпадения не найдены, новый файл не создаётся.

Используйте файл system_log.txt.
"""

import os
import sys

filename = "HW/HW_27/system_log.txt"
keyword = input("Введите ключевое слово: ").lower()

try:
    with open(filename, "r", encoding="utf-8") as file:
        lines = [line for line in file if keyword in line.lower()]
except FileNotFoundError:
    print(f"Ошибка: файл '{filename}' не существует.")
    sys.exit(1)

if lines:
    new_filename = os.path.join(
        os.path.dirname(filename),
        f"{keyword}_{os.path.basename(filename)}"
    )
    with open(new_filename, "w", encoding="utf-8") as file:
        file.writelines(lines)
else:
    print("Совпадения не найдены.")