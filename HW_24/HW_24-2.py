"""Сумма вложенных чисел

Напишите рекурсивную функцию, которая суммирует все числа
во вложенных списках.

Данные:
nested_numbers = [1, [2, 3], [4, [5, 6]], 7]

Пример вывода:
28
"""

def sum_nested(lst, i=0):
    if i == len(lst):
        return 0

    current = lst[i]

    if isinstance(current, list):
        return sum_nested(current) + sum_nested(lst, i + 1)

    return current + sum_nested(lst, i + 1)

nested_numbers = [1, [2, 3], [4, [5, 6]], 7]
print(sum_nested(nested_numbers))


'''
def sum_nested_tail(nested_list, i=0, acc=0):
    if i == len(nested_list):
        return acc

    item = nested_list[i]

    if isinstance(item, list):
        acc = sum_nested_tail(item, 0, acc)
    else:
        acc += item

    return sum_nested_tail(nested_list, i + 1, acc)

nested_numbers = [1, [2, 3], [4, [5, 6]], 7]
result = sum_nested_tail(nested_numbers)
print(result)
'''