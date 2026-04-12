"""
Сумма цифр числа
Напишите рекурсивную функцию, которая находит сумму всех цифр числа.

Данные:
num = 43197

Пример вывода:
24
"""

def sum_digits(n):
    if n == 0:
        return 0
    return n % 10 + sum_digits(n // 10)

num = 43197
print(sum_digits(num))


# Хвостовая рекурсия
def sum_digits_tail(n, acc=0):
    if n == 0:
        return acc
    return sum_digits_tail(n // 10, acc + (n % 10))

num = 43197
print(sum_digits_tail(num))