"""
2. Статистика продаж
Дан список продаж в виде кортежей (товар, количество, цена).
Напишите программу, которая:
Вычисляет общую выручку для каждого товара.
Возвращает словарь с товарами {товар: выручка},
отсортированный по убыванию выручки.
"""

sales = [
    ("Laptop", 5, 1200),
    ("Mouse", 50, 20),
    ("Keyboard", 30, 50),
    ("Monitor", 10, 300),
    ("Chair", 20, 800),
]

# Пример вывода:
# {"Chair": 16000, "Laptop": 6000,
# "Monitor": 3000, "Keyboard": 1500, "Mouse": 1000}


def calculate_revenue(sales):
    revenues = map(lambda item: (item[0], item[1] * item[2]), sales)
    return dict(sorted(revenues, key=lambda x: x[1], reverse=True))


print(calculate_revenue(sales))