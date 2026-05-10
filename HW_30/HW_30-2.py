'''Генератор уникальных элементов
Создайте генератор, который принимает список элементов и выдаёт только
уникальные значения, сохраняя порядок их появления в исходном списке.
Данные:
data = [3, 1, 2, 3, 4, 1, 5, 2, 6, 7, 5, 8]'''

def unique_generator(data):
    
    seen = set()
    
    for item in data:
        
        if item not in seen:
            seen.add(item)
            yield item
            
data = [3, 1, 2, 3, 4, 1, 5, 2, 6, 7, 5, 8]

gen = unique_generator(data)

for number in gen:
    print(number)