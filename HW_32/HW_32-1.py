"""1. Класс Rectangle
Создайте класс Rectangle, который описывает прямоугольник.
● У каждого объекта должны быть два поля: width и height.
● Добавьте метод get_area(), который возвращает площадь прямоугольника.
● Создайте объект прямоугольника с произвольными значениями.
● Выведите его площадь.
● Измените ширину и высоту.
● Выведите новую площадь.
Пример вывода:
Площадь: 20
Новая площадь: 35"""


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height

    def set_dimensions(self, new_width, new_height):
        self.width = new_width
        self.height = new_height


my_rect = Rectangle(4, 5)
print(f"Площадь: {my_rect.get_area()}")

my_rect.set_dimensions(5, 7)
print(f"Новая площадь: {my_rect.get_area()}")
