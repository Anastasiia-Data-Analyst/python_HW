"""
1. Выбор заказов
У вас есть список заказов.
Каждый заказ содержит название продукта и его цену.

Напишите функцию, которая:
Отбирает заказы дороже 500.
Создаёт список названий отобранных продуктов в алфавитном порядке.
Возвращает итоговый список названий.
"""

orders = [
    {"product": "Laptop", "price": 1200},
    {"product": "Mouse", "price": 50},
    {"product": "Keyboard", "price": 100},
    {"product": "Monitor", "price": 300},
    {"product": "Chair", "price": 800},
    {"product": "Desk", "price": 400},
]

# Пример вывода:
# ['Chair', 'Laptop']


def filter_orders(orders, min_price=500):
    f_orders = filter(lambda order: order["price"] > min_price, orders)
    return sorted([order["product"] for order in f_orders])


print(filter_orders(orders))