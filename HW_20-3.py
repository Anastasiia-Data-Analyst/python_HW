"""
Объединение словарей
Напишите функцию, которая принимает любое количество
словарей и объединяет их в один. Если ключи повторяются,
используется значение из последнего словаря.
Данные:
dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}
dict3 = {"d": 5}
Пример вызова:
print(merge_dicts(dict1, dict2, dict3))
"""

def merge_dicts(*args):
    result = {}
    for d in args: # Перебираем каждый переданный словарь по очереди
        result.update(d) # update добавляет пары ключ-значение в result
    return result

dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}
dict3 = {"d": 5}

print(merge_dicts(dict1, dict2, dict3))
