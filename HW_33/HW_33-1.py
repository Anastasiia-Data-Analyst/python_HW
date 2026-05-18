"""1. Класс Person
Создайте класс Person, представляющий человека.
● Каждый человек должен иметь имя.
● Добавьте метод introduce(), который выводит приветствие с именем.
Пример вывода:
Hello, my name is Alice."""


class Person:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        print(f"Hello, my name is {self.name}.")


person = Person("Alice")
person.introduce()
