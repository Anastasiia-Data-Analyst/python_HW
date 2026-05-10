'''Напишите функцию, которая принимает списки типов одежды, цветов и размеров, а затем генерирует все возможные комбинации в формате "Clothe - Color - Size".
Данные:
clothes = ["T-shirt", "Jeans", "Jacket"]
colors = ["Red", "Blue", "Black"]
sizes = ["S", "M", "L"]
'''

import itertools

clothes = ["T-shirt", "Jeans", "Jacket"]
colors = ["Red", "Blue", "Black"]
sizes = ["S", "M", "L"]

combinations = itertools.product(clothes, colors, sizes)

for clothe, color, size in combinations:
    print(f"{clothe} - {color} - {size}")