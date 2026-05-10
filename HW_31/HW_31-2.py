'''Реализуйте программу, которая должна:
● Прочитать строку с тегами, введёнными пользователем.
● Разделить её на отдельные теги, независимо от того, чем они были разделены (запятые, точки с
запятой, слэши или пробелы).
● Удалить лишние пробелы и пустые значения.
Данные:
tag_input = "python, data-science / machine-learning; AI neural-networks"
'''

import re

tag_input = "python, data-science / machine-learning; AI neural-networks"

print(re.split(r"[,;/\s]+", tag_input))