"""
Поиск и удаление дубликатов
Напишите программу, которая удаляет дублирующиеся строки из файла
и сохраняет результат в новый файл.

- Имя нового файла формируется как unique_<original_filename>.
- Если файл не существует, программа должна вывести ошибку.
- Исходный порядок строк должен сохраниться.
- Если в файле нет дубликатов, создаётся точная копия файла.

Используйте файл movies_to_watch.txt.
"""

import os
import sys

filename = "HW/HW_27/movies_to_watch.txt"

try:
    with open(filename, "r", encoding="utf-8") as file:
        lines = file.readlines()
except FileNotFoundError:
    print(f"Ошибка: файл '{filename}' не существует.")
    sys.exit(1)


new_filename = os.path.join(
    os.path.dirname(filename), f"unique_{os.path.basename(filename)}"
)

with open(new_filename, "w", encoding="utf-8") as file:
    file.writelines(list(dict.fromkeys(lines)))