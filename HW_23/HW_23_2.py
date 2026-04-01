"""
2. Сумма вложенных чисел
Напишите функцию, которая принимает список словарей,
где каждый словарь содержит имя пользователя и список баллов.
Функция должна вернуть сумму всех чисел.
Добавьте документацию и аннотации типов для всех
параметров и возвращаемого значения.
"""

from typing import Any

data = [
    {"name": "Alice", "scores": [10, 20, 30]},
    {"name": "Bob", "scores": [5, 15, 25]},
    {"name": "Charlie", "scores": [7, 17, 27]},
]
# Пример вывода:
# Итоговый балл: 156


def total_scores(data: list[dict[str, Any]]) -> int:
    return sum(sum(user["scores"]) for user in data)


result = total_scores(data)
print(f"Итоговый балл: {result}")



'''from typing import TypedDict


class User(TypedDict):
    name: str
    scores: list[int]


data: list[User] = [
    {"name": "Alice", "scores": [10, 20, 30]},
    {"name": "Bob", "scores": [5, 15, 25]},
    {"name": "Charlie", "scores": [7, 17, 27]},
]


def total_scores(data: list[User]) -> int:
    return sum(sum(user["scores"]) for user in data)


result = total_scores(data)
print(f"Итоговый балл: {result}")'''