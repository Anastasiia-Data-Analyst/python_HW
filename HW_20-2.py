"""
Фильтрация чисел по чётности
Напишите функцию, которая принимает filter_type ("even" или "odd")
и произвольное количество чисел, возвращая только те,
которые соответствуют фильтру.
Пример вызова:
print(filter_numbers("even", 1, 2, 3, 4, 5, 6))
print(filter_numbers("odd", 10, 15, 20, 25))
print(filter_numbers("prime", 2, 3, 5, 7))

Пример вывода:
[2, 4, 6]
[15, 25]
Некорректный фильтр
"""


def filter_numbers(filter_type, *args):
    if filter_type == "even":
        return [x for x in args if x % 2 == 0]
    elif filter_type == "odd":
        return [x for x in args if x % 2 != 0]
    else:
        return "Некорректный фильтр"


print(filter_numbers("even", 1, 2, 3, 4, 5, 6))
print(filter_numbers("odd", 10, 15, 20, 25))
print(filter_numbers("prime", 2, 3, 5, 7))