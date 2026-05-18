"""2. Класс Student
На основе класса Person создайте класс Student.
● Студент должен иметь имя и номер курса.
● Метод introduce() должен сначала выводить базовое приветствие, а затем
строку: I'm on course <номер_курса>.
Пример вывода:
Hello, my name is Alice.
I'm on course 2."""


class Person:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        print(f"Hello, my name is {self.name}.")


class Student(Person):
    def __init__(self, name, course):
        super().__init__(name)
        self.course = course

    def introduce(self):
        super().introduce()
        print(f"I'm on course {self.course}.")


student = Student("Alice", 2)
student.introduce()
